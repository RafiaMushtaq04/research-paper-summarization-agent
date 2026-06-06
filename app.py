import argparse
from pathlib import Path
from rich.console import Console

from src.agent import LLMClient, PaperSummarizationAgent, SummaryRequest
from src.utils import read_input_text, chunk_text


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Research Paper Summarization Agent")
    parser.add_argument("--input", required=True, help="Path to input file (PDF/TXT/MD)")
    parser.add_argument("--output", default="", help="Optional path to save markdown output")
    parser.add_argument("--style", default="concise", help="Summary style: concise|detailed")
    parser.add_argument("--focus", default="overall paper", help="Focus area for summarization")
    parser.add_argument("--chunk-size", type=int, default=1800, help="Characters per chunk")
    parser.add_argument("--overlap", type=int, default=250, help="Chunk overlap in characters")
    parser.add_argument("--max-chunks", type=int, default=8, help="Max chunks to process")
    return parser


def main() -> None:
    console = Console()
    args = build_parser().parse_args()

    text = read_input_text(args.input)
    chunks = chunk_text(text, chunk_size=args.chunk_size, overlap=args.overlap)

    llm = LLMClient()
    agent = PaperSummarizationAgent(llm)

    req = SummaryRequest(
        chunks=chunks,
        style=args.style,
        focus=args.focus,
        max_chunks=args.max_chunks,
    )

    console.print(f"[bold cyan]Loaded chunks:[/bold cyan] {len(chunks)}")
    summary = agent.summarize(req)

    if args.output:
        output_path = Path(args.output)
        output_path.write_text(summary, encoding="utf-8")
        console.print(f"[green]Saved summary to:[/green] {output_path}")
    else:
        console.print("\n[bold green]Summary[/bold green]\n")
        console.print(summary)


if __name__ == "__main__":
    main()
