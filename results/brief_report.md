# Experiment Brief Report

## Setup
- Dataset: first 4 papers from `Research papers/`
- Sweep: `max_chunks` in `{4, 6, 8}` and `style` in `{concise, detailed}`
- Total outputs: 24 summaries
- Evaluation: ROUGE-1/2/L on all 24 summaries
- BERTScore: skipped in fast mode to avoid large model downloads and keep evaluation lightweight

## Summary of Results
Average ROUGE by configuration across the 4 papers:

| Chunks | Style | ROUGE-1 | ROUGE-2 | ROUGE-L |
| --- | --- | ---: | ---: | ---: |
| 4 | concise | 0.3510 | 0.0913 | 0.1734 |
| 4 | detailed | 0.3247 | 0.0844 | 0.1533 |
| 6 | concise | 0.3387 | 0.0818 | 0.1569 |
| 6 | detailed | 0.3019 | 0.0847 | 0.1442 |
| 8 | concise | 0.3158 | 0.0719 | 0.1512 |
| 8 | detailed | 0.2941 | 0.0765 | 0.1387 |

## Best Configuration
- Best overall average: `4 chunks + concise`
- Reason: it gave the strongest ROUGE-1, ROUGE-2, and ROUGE-L averages among the tested settings.

## Notes
- Concise summaries generally outperformed detailed summaries in this sweep.
- Increasing chunk count from 4 to 8 did not improve the average scores.
- The fast evaluation path was chosen because it is much more stable on this machine and avoids large BERTScore model downloads.