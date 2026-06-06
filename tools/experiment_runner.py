import os
import time
from pathlib import Path

from src.agent import LLMClient, PaperSummarizationAgent, SummaryRequest
from src.utils import read_input_text, chunk_text


DATA_DIR = Path(__file__).resolve().parents[1] / ".." / "Research papers"
OUT_DIR = Path(__file__).parent.parent / "results"
REF_DIR = Path(__file__).parent.parent / "refs"


def extract_abstract(full_text: str) -> str:
    # Try to locate the Abstract section
    lowered = full_text.lower()
    idx = lowered.find("abstract")
    if idx == -1:
        # fallback: first 300-450 words
        return " ".join(full_text.split()[:350])
    # find end (next heading common words)
    tail = full_text[idx:]
    for sep in ["introduction", "1.", "i.", "keywords"]:
        j = tail.lower().find(sep)
        if j > 20:
            return tail[:j].strip()
    return "\n".join(tail.splitlines()[:20])


def run_experiments(papers_dir: Path = DATA_DIR):
    OUT_DIR.mkdir(exist_ok=True)
    REF_DIR.mkdir(exist_ok=True)

    llm = LLMClient()
    agent = PaperSummarizationAgent(llm)

    configs = [4, 6, 8]
    styles = ["concise", "detailed"]

    metadata_lines = ["paper,config_chunks,style,output_file,seconds"]

    for pdf in sorted(papers_dir.glob("*.pdf")):
        print("Processing", pdf.name)
        text = read_input_text(str(pdf))
        # save reference abstract
        abstract = extract_abstract(text)
        ref_path = REF_DIR / (pdf.stem + ".ref.txt")
        ref_path.write_text(abstract if isinstance(abstract, str) else "\n".join(abstract), encoding="utf-8")

        chunks = chunk_text(text, chunk_size=1800, overlap=250)
        for c in configs:
            for style in styles:
                req = SummaryRequest(chunks=chunks, style=style, focus="overall paper", max_chunks=c)
                start = time.time()
                out_name = f"{pdf.stem}_chunks{c}_{style}.md"
                out_path = OUT_DIR / out_name
                if out_path.exists():
                    print("Skipping existing:", out_name)
                    metadata_lines.append(f"{pdf.name},{c},{style},{out_name},skipped")
                    continue
                try:
                    out = agent.summarize(req)
                except Exception as e:
                    print(f"Error summarizing {pdf.name} cfg {c} {style}: {e}")
                    metadata_lines.append(f"{pdf.name},{c},{style},{out_name},error")
                    continue
                elapsed = time.time() - start

                out_path.write_text(out, encoding="utf-8")
                metadata_lines.append(f"{pdf.name},{c},{style},{out_name},{elapsed:.2f}")

    (OUT_DIR / "metadata.csv").write_text("\n".join(metadata_lines), encoding="utf-8")
    print("Experiments complete. Results in:", OUT_DIR)


if __name__ == "__main__":
    run_experiments()
