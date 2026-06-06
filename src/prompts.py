SYSTEM_PROMPT = """
You are an academic assistant. Produce faithful, evidence-grounded summaries.
Do not invent claims that are not in the source text.
If information is missing, write: Not clearly stated in the provided text.
""".strip()


MAP_PROMPT_TEMPLATE = """
You are reading one chunk from a research paper.

Task:
1) Extract key points from this chunk only.
2) Keep points factual and short.
3) Capture methodology, dataset, findings, and limitations if present.

Return JSON with keys:
- chunk_summary
- methods
- findings
- limitations
- notable_terms

Chunk text:
{chunk_text}
""".strip()


REDUCE_PROMPT_TEMPLATE = """
You are given partial summaries of a research paper from multiple chunks.
Synthesize a final report.

User focus: {focus}
Style: {style}

Return markdown with these headings:
1. Paper Overview
2. Problem Statement
3. Proposed Method
4. Data and Experimental Setup
5. Main Results
6. Strengths
7. Limitations
8. Future Work
9. 5-Bullet Ultra-Short Summary

Partial summaries:
{partial_summaries}
""".strip()
