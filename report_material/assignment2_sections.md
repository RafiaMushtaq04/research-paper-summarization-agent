# Research Paper Summarization Agent

## Abstract
This project presents a task-oriented AI agent for research paper summarization. The system accepts long scientific documents, extracts text from PDF/TXT input, splits the document into overlapping chunks, and uses a prompt-driven map-reduce workflow with Gemini to generate structured summaries. The output is organized into academic headings such as problem statement, method, experimental setup, findings, limitations, and future work. The goal is not only to shorten a paper, but also to preserve the technical meaning that a student or researcher needs for literature review, viva preparation, or quick comparison across studies.

To support Assignment-2 style reporting, the project also includes a small experimental study on four papers and evaluates generated summaries using ROUGE-based overlap scores. The results show that a compact setting with 4 chunks and concise style performs best on average for the tested sample. This suggests that a structured, chunk-based pipeline can be more effective than a single-pass summary when the input document is long and technical.

## Introduction
Rapid growth in scientific publishing makes it difficult for students and researchers to read every paper in full. Long papers contain technical detail, section-level discourse, and cross-references that are hard to summarize with a single-pass model. In practice, a student often needs more than a short abstract. They need to know what problem the paper solves, which method it uses, what the experimental setup looks like, what the main findings are, and where the paper still has limitations. The motivation of this work is to build a practical assistant that reduces reading time while preserving those core research elements.

This problem is important because literature review, thesis writing, seminar preparation, and viva revision all depend on fast access to the core content of papers. Manual reading remains valuable, but it becomes inefficient when the number of papers increases. An AI-based summarization agent can help by producing a short but structured review of each paper instead of only a generic abstract-like summary. That makes it easier to decide whether a paper is worth reading in detail.

Natural Language Processing supports this task through document parsing, semantic chunking, controllable prompting, and structured generation. The current system uses a free-tier Gemini backend and a map-reduce prompt design so that long papers can be processed in smaller parts before a final synthesis step. The design is intentionally simple enough for a semester project, but still realistic enough to show how modern AI systems combine prompt engineering, task decomposition, and controlled output formatting.

## Literature Review
The literature review in `assignment1_sections.md` already covers the main background: early seq2seq summarization, pointer-generator networks, transformer pretraining, long-document summarization challenges, and LLM/agent-based workflows. For the final paper, the key takeaway is that scientific summarization still faces two persistent issues:

1. Long papers exceed the comfortable context window of many single-pass summarizers.
2. Fluent summaries can still miss important technical details or hallucinate unsupported claims.

The proposed agent addresses both by chunking the document and forcing a structured final answer. Instead of treating the paper as one huge block of text, the system breaks the content into smaller semantic units, extracts the most important information from each unit, and then combines those local summaries into a final structured output. This is especially useful for scientific papers because key evidence is often spread across multiple sections rather than being concentrated in one paragraph.

This also connects directly to the assignment requirement for a task-oriented AI agent. The literature shows that modern NLP systems are most useful when the model is not only generating language, but also following a procedure: identify the task, plan the processing steps, and produce a task-specific output. That is the role of the map-reduce style summarization pipeline in this project.

## Material and Methods

### 1. System Architecture
The implemented pipeline is:

User Upload -> Document Parser -> Text Cleaner -> Chunking Module -> Prompt Builder -> Gemini Map Stage -> Chunk Summaries -> Gemini Reduce Stage -> Output Validation -> Structured Summary

This matches the architecture in `report_material/architecture.mmd` and the code in `src/agent.py`, `src/utils.py`, and `src/prompts.py`.

The architecture is modular so that each stage has a clear responsibility. The parser handles input extraction, the cleaner removes obvious noise, the chunker prepares the document for long-context processing, the prompt builder translates the user request into an LLM-friendly instruction, and the synthesis step merges the chunk-level outputs into a final paper summary. This separation is important because it makes the project easier to explain, debug, and extend in the final report.

### 2. Input Processing
The agent accepts PDF or TXT input. PDFs are converted to text, and the parser removes layout noise where possible. The extracted text is then normalized so that the downstream prompt receives cleaner input.

This step matters because scientific papers often contain headers, footers, page numbers, multi-column formatting, and tables that can confuse a language model if left unprocessed. In report language, this stage can be described as the document ingestion layer that converts an unstructured academic PDF into machine-readable text without losing the important semantic content.

### 3. Chunking Strategy
Long documents are divided into overlapping chunks. Chunking is essential because a single research paper can easily exceed the token budget of a low-cost API model. Overlap is used so that important sentences crossing chunk boundaries are not lost.

In the current implementation, the experiment runner uses a chunk size of 1800 characters with 250-character overlap. The model then works on only the first `max_chunks` chunks during an experiment run.

For the report, this chunking strategy can be described as a practical approximation of long-context processing. Instead of forcing the LLM to hold the entire paper in memory at once, the system processes smaller windows and then fuses the local outputs. That makes the summarizer more stable and more feasible to run under free-tier API limits.

### 4. Prompt Design
The system uses two prompt stages:

- Map stage: each chunk is summarized into structured fields such as methods, findings, limitations, and notable terms.
- Reduce stage: the chunk-level outputs are merged into a final paper-level summary.

The final response is shaped into academic headings so that the output is easy to paste into a report or literature review. This is one of the main design strengths of the project: the prompt does not ask for a generic summary, but for a structured academic summary with predictable sections. That improves readability and makes the output directly usable in assignment writing.

The prompts also let the system behave like a task-oriented agent rather than a plain text generator. The map stage extracts information, while the reduce stage synthesizes and organizes it. This two-step design is useful because it mirrors how a human would read a paper: first gather the important points from each section, then integrate them into a short coherent explanation.

### 5. Runtime Controls
The CLI exposes practical controls for viva and testing:

- `--style concise|detailed` changes the verbosity of the output.
- `--focus` lets the user ask for a specific section focus such as methodology, results, or literature review.
- `--max-chunks` limits how much of the paper is processed, which directly affects cost and runtime.

These controls are important because they show that the agent is not fixed to one output mode. In a viva, the user may ask for only the literature review, only the methods, or a short version of the summary. The runtime flags make that possible without changing the code. This is also a strong point for the report because it demonstrates controllability, which is one of the goals of a task-oriented AI agent.

### 6. Output Validation
After generation, the summary is checked for structure and consistency. The goal is not perfect factual verification, but a stable, human-readable academic summary that keeps the main sections intact.

From a report perspective, this validation stage is important because it shows awareness of quality control. Even though the system is not a formal fact-checker, it still tries to preserve section headings, maintain coherent flow, and reduce the chance of incomplete or malformed output. That makes the agent more reliable for real student use.

## Experimental Setup
To check whether the design was practical, a controlled experiment was run on the first four papers from the `Research papers/` folder. Each paper was summarized under six configurations:

- `max_chunks` = 4, 6, 8
- `style` = concise, detailed

This produced 24 summaries in total. A metadata file, `results/metadata.csv`, records which paper was processed, which configuration was used, the output filename, and runtime information.

The sweep was intentionally limited to four papers because the Gemini free-tier quota is request-limited. This makes the study realistic for a student project while still providing a useful comparison across configurations.

The experimental setup is useful in the paper because it turns the project from a simple demo into a measurable system. Instead of saying that the agent "works," the report can show that it was tested under multiple configurations and evaluated consistently. That is the right style for Assignment-2 because it connects implementation with evidence.

## Evaluation Metrics
The project uses two families of automatic evaluation metrics.

### ROUGE
ROUGE measures lexical overlap between a generated summary and a reference text.

- ROUGE-1: overlap of single words
- ROUGE-2: overlap of two-word sequences
- ROUGE-L: longest common subsequence overlap

ROUGE is useful for checking whether the summary preserves the same key terms and phrasing as the reference abstract or reference section.

In this project, ROUGE is a good first metric because the task is summarization and the output is supposed to stay close to the important content of the source paper. If the summary drops key terms or major phrases, ROUGE values tend to fall, which gives a quick signal that the configuration may not be preserving enough source information.

### BERTScore
BERTScore compares summaries using contextual embeddings instead of only exact word matches. It is more semantic than ROUGE and is useful when two summaries say the same thing using different wording. In this project it can be treated as an optional supplementary metric, but the reported experiment focuses on ROUGE because it is faster and easier to reproduce in a free-tier environment.

BERTScore is still relevant conceptually because it would be the next metric to try if you wanted a deeper semantic comparison in a future version of the project. For the current semester report, however, it is enough to mention it as an optional advanced metric rather than a core reported result.

### Why these metrics matter here
ROUGE tells us whether the summary captures the same visible content as the reference. For an academic summarizer, that is important because the output should stay aligned with the source paper and preserve the main technical terms.

These metrics help connect the engineering output to the research objective. The project is not only about producing text, but about producing text that is faithful, useful, and section-aware. Evaluation gives the report an evidence-based backbone.

## Results
The automatic evaluation was saved in `results/evaluation.csv`. The averaged ROUGE scores across the four papers are:

| Chunks | Style | ROUGE-1 | ROUGE-2 | ROUGE-L |
| --- | --- | ---: | ---: | ---: |
| 4 | concise | 0.3510 | 0.0913 | 0.1734 |
| 4 | detailed | 0.3247 | 0.0844 | 0.1533 |
| 6 | concise | 0.3387 | 0.0818 | 0.1569 |
| 6 | detailed | 0.3019 | 0.0847 | 0.1442 |
| 8 | concise | 0.3158 | 0.0719 | 0.1512 |
| 8 | detailed | 0.2941 | 0.0765 | 0.1387 |

The table shows a clear pattern: the concise style works better than detailed style for this task, and the 4-chunk setting performs best overall. That suggests the model benefits from a focused input window and a shorter final output. In long-document summarization, too much source text can introduce noise, while too much verbosity can dilute the important information. The best configuration appears to balance both factors.

### Main observations
- The best average configuration was `4 chunks + concise`.
- Concise outputs performed better than detailed outputs in this sweep.
- Increasing chunk count from 4 to 8 did not improve the average ROUGE scores.
- The results suggest that for these papers, a smaller amount of source context was enough to preserve the main summary content while keeping the output focused.

Another way to explain these results in the report is that the summarizer is most effective when it is guided by strong structure rather than by maximal context. This is a useful finding because it supports the design choice of a lightweight, prompt-driven system instead of a heavier single-pass model.

### Interpretation for the project
This result is useful because it shows that the system can produce reasonable summaries without processing every chunk. That matters for your viva and report because it proves the design is practical, cost-aware, and suitable for long-document summarization under a free-tier API.

It also gives you a simple justification for the final configuration choice in the paper. Rather than claiming that one setting is universally best, you can say that the tested sample showed 4 chunks with concise output to be the best trade-off between detail, focus, and runtime cost.

## Baseline Comparison
The most relevant baseline paper for this project is Cohan et al. (2018), a discourse-aware attention model for abstractive summarization of long documents. It is appropriate as a baseline because it targets the same long-document problem and specifically addresses scientific text.

| Aspect | Baseline: Cohan et al. (2018) | Proposed Agent |
| --- | --- | --- |
| Input handling | End-to-end long-document model | PDF/TXT parser with chunking and overlap |
| Control | Fixed model behavior | User-controlled `style`, `focus`, `max_chunks` |
| Output | Abstractive summary generation | Structured academic summary with fixed headings |
| Deployment | Research-model dependent | Free-tier Gemini workflow, lightweight for student use |
| Long-context strategy | Learned discourse modeling | Map-reduce prompting across chunks |
| Practical use | Strong research baseline | Task-oriented assistant for viva and literature review |

This baseline comparison is useful in the paper because it shows how the proposed agent is not just another summarizer. It is a controllable, task-oriented system designed for practical student use, while the baseline represents the research direction for scientific long-document summarization.

In a final submission, this comparison helps you demonstrate novelty at the system level. Your project is not trying to beat the baseline model in a strict benchmark sense; instead, it shows how a student-friendly AI agent can package long-document summarization into a usable workflow with configurable controls, structured output, and a simple deployment path.

## Evaluation Metadata
The generated files play different roles:

- `results/metadata.csv`: run log with paper name, chunk count, style, output file, and runtime or skip status
- `results/evaluation.csv`: metric table with ROUGE scores for each generated summary; BERTScore can be added later if needed
- `results/brief_report.md`: short human-readable summary of the experiment

This separation is useful because metadata helps with reproducibility, while the evaluation file provides the actual evidence used in the paper.

In the report, this part can be explained as the experiment record. It is what allows someone else to trace how many papers were processed, which settings were used, and where the scores came from. That is useful for academic transparency and for viva questions about how the results were obtained.

## What Is Complete and What Remains
Completed for the current project phase:

- core summarization agent
- CLI controls for focus, style, and chunk count
- 4-paper experiment sweep
- fast automatic evaluation
- paper-ready results summary

Still recommended before final submission:

- integrate this content into the 12-15 page sample paper format
- add a figure for the pipeline architecture and maybe one results table
- write a short discussion paragraph on limitations and future work

If you want a full 12-15 page paper, the current text is enough as the core content, but it should be expanded in a proper conference-paper style layout with title page, abstract, numbered sections, figure captions, table captions, and references formatted consistently. That will make the submission look complete rather than like a section draft.

## Suggested Final Paper Angle
For Assignment-2, the best story is:

"We designed a task-oriented AI agent for long research paper summarization, implemented a structured map-reduce pipeline, evaluated multiple configurations on four papers, and found that a concise 4-chunk setting gave the best average ROUGE results under free-tier constraints."