import json
import requests
import time
from dataclasses import dataclass
from typing import List
import google.generativeai as genai
import google.api_core.exceptions as gexc

from .config import settings
from .prompts import SYSTEM_PROMPT, MAP_PROMPT_TEMPLATE, REDUCE_PROMPT_TEMPLATE


@dataclass
class SummaryRequest:
    chunks: List[str]
    style: str = "concise"
    focus: str = "overall paper"
    max_chunks: int = 8


class LLMClient:
    def __init__(self) -> None:
        self.backend = settings.model_backend
        if self.backend == "gemini":
            if not settings.gemini_api_key:
                raise ValueError("GEMINI_API_KEY is missing. Add it in your .env file.")
            genai.configure(api_key=settings.gemini_api_key)
            self.gemini_model = genai.GenerativeModel(settings.gemini_model)

    def generate(self, prompt: str, system_prompt: str = "") -> str:
        if self.backend == "ollama":
            return self._generate_ollama(prompt, system_prompt)
        if self.backend == "openai":
            raise NotImplementedError("OpenAI adapter not yet implemented in this starter.")
        if self.backend == "gemini":
            return self._generate_gemini(prompt, system_prompt)
        raise ValueError(f"Unsupported MODEL_BACKEND: {self.backend}")

    def _generate_ollama(self, prompt: str, system_prompt: str = "") -> str:
        url = f"{settings.ollama_base_url.rstrip('/')}/api/chat"
        payload = {
            "model": settings.ollama_model,
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt},
            ],
            "stream": False,
            "options": {"temperature": 0.2},
        }
        resp = requests.post(url, json=payload, timeout=120)
        resp.raise_for_status()
        data = resp.json()
        return data["message"]["content"].strip()

    def _generate_gemini(self, prompt: str, system_prompt: str = "") -> str:
        merged_prompt = f"{system_prompt}\n\n{prompt}".strip()

        max_retries = 6
        backoff = 2
        for attempt in range(1, max_retries + 1):
            try:
                response = self.gemini_model.generate_content(merged_prompt)
                if not response or not getattr(response, "text", ""):
                    raise ValueError("Gemini returned an empty response.")
                # brief pause to avoid hitting per-minute request spikes
                time.sleep(0.3)
                return response.text.strip()
            except gexc.ResourceExhausted as e:
                wait = backoff ** attempt
                print(f"Gemini quota hit (ResourceExhausted). Retry {attempt}/{max_retries} in {wait}s.")
                time.sleep(wait)
                continue
            except Exception as e:
                # For transient gRPC errors, retry a few times
                if attempt < max_retries:
                    wait = backoff ** attempt
                    print(f"Transient error calling Gemini: {e}. Retry {attempt}/{max_retries} in {wait}s.")
                    time.sleep(wait)
                    continue
                raise


class PaperSummarizationAgent:
    def __init__(self, llm: LLMClient) -> None:
        self.llm = llm

    def summarize(self, req: SummaryRequest) -> str:
        selected_chunks = req.chunks[: req.max_chunks]
        partials = []

        for idx, chunk in enumerate(selected_chunks, start=1):
            map_prompt = MAP_PROMPT_TEMPLATE.format(chunk_text=chunk)
            result = self.llm.generate(map_prompt, SYSTEM_PROMPT)
            partials.append(f"Chunk {idx}:\n{result}")

        reduce_prompt = REDUCE_PROMPT_TEMPLATE.format(
            focus=req.focus,
            style=req.style,
            partial_summaries="\n\n".join(partials),
        )

        return self.llm.generate(reduce_prompt, SYSTEM_PROMPT)


def safe_json_parse(raw_text: str) -> dict:
    try:
        return json.loads(raw_text)
    except Exception:
        return {"raw": raw_text}
