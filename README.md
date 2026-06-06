# Research Paper Summarization Agent

An AI assistant for summarizing long research papers into structured, readable academic summaries. The system ingests PDF or TXT documents, cleans and chunks the text, then uses a prompt-driven map-reduce workflow to generate a final summary with sections such as overview, method, results, limitations, and future work.

## Overview

This project is designed as a practical natural-language AI agent for long-document understanding. It is useful for:

- research paper summarization
- literature review support
- viva preparation
- quick comparison across papers
- controlled summarization with focus-aware output

## Features

- PDF and TXT input support
- configurable summary style: concise or detailed
- focus control for methodology, results, literature review, and more
- chunk-based processing for long documents
- Gemini backend support, with Ollama as an alternative local option
- experimental sweep and automatic ROUGE evaluation
- interactive text-paste mode for natural-language queries

## Project Structure

- `app.py`: CLI entry point
- `src/config.py`: environment-based configuration
- `src/utils.py`: input parsing and chunking
- `src/prompts.py`: prompt templates
- `src/agent.py`: summarization pipeline and model adapters
- `src/interactive.py`: interactive terminal mode
- `tools/experiment_runner.py`: experiment batch runner
- `tools/evaluate_summaries.py`: automatic evaluation
- `report_material/`: paper-ready notes, sections, and diagram source
- `results/`: generated summaries and evaluation outputs

## Setup

### 1. Create and activate a virtual environment
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### 2. Configure environment variables
Copy the example file and edit your local `.env`:
```powershell
copy .env.example .env
```

For Gemini usage, set:
```env
MODEL_BACKEND=gemini
GEMINI_API_KEY=your_api_key_here
GEMINI_MODEL=models/gemini-flash-lite-latest
```

For Ollama usage, set:
```env
MODEL_BACKEND=ollama
OLLAMA_MODEL=llama3.1:8b
OLLAMA_BASE_URL=http://localhost:11434
```

## Usage

### Summarize a research paper
```powershell
python app.py --input "Research papers\sample_Paper_1 (1).pdf" --style concise --max-chunks 4 --output "results\sample_summary.md"
```

### Summarize with a focus
```powershell
python app.py --input "Research papers\sample_Paper_1 (1).pdf" --style detailed --max-chunks 6 --focus "methods and main contributions" --output "results\focused_summary.md"
```

### Run the interactive natural-language mode
```powershell
python src/interactive.py
```

### Run the experiment sweep on the first four papers
```powershell
python run_experiments_first4.py
```

### Run evaluation
```powershell
python tools/evaluate_summaries.py
```

## System Overview

The pipeline follows a staged design:

Document input -> parsing and text cleaning -> chunking -> map-stage prompting -> chunk-level summaries -> reduce-stage synthesis -> output formatting and validation

This design keeps the agent practical for long scientific papers and makes the summarization behavior easy to explain, test, and extend.

## Experiments and Results

The repository includes experiment outputs and evaluation artifacts produced during testing. The current best tested configuration on the four-paper sweep was:

- `max_chunks = 4`
- `style = concise`

Average ROUGE scores:

- ROUGE-1: `0.3510`
- ROUGE-2: `0.0913`
- ROUGE-L: `0.1734`

## Security and GitHub Upload Notes

- Do not commit `.env`
- Keep API keys only in your local environment file
- Commit `.env.example` instead of `.env`
- The included `.gitignore` already excludes secrets, virtual environments, and local run outputs

## License

Add your preferred license before publishing the repository.
