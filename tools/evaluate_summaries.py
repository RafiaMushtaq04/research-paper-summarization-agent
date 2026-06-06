import os
from pathlib import Path
from rouge_score import rouge_scorer


RESULTS_DIR = Path(__file__).parent.parent / "results"
REF_DIR = Path(__file__).parent.parent / "refs"
USE_BERTSCORE = os.getenv("USE_BERTSCORE", "0") == "1"
BERTSCORE_MODEL = os.getenv("BERTSCORE_MODEL", "distilroberta-base")


def load_text(p: Path) -> str:
    return p.read_text(encoding="utf-8") if p.exists() else ""


def evaluate():
    scorer = rouge_scorer.RougeScorer(["rouge1", "rouge2", "rougeL"], use_stemmer=True)
    rows = ["file,rouge1_f,rouge2_f,rougeL_f,bert_f1,bert_precision,bert_recall"]

    bert_score = None
    if USE_BERTSCORE:
        from bert_score import score as bert_score  # lazy import for fast mode

    preds = sorted(RESULTS_DIR.glob("*.md"))
    for p in preds:
        ref = REF_DIR / (p.stem.split("_chunks")[0] + ".ref.txt")
        ref_text = load_text(ref)
        pred_text = load_text(p)
        if not ref_text or not pred_text:
            continue

        r = scorer.score(ref_text, pred_text)
        if USE_BERTSCORE and bert_score is not None:
            bert_p, bert_r, bert_f = bert_score([pred_text], [ref_text], model_type=BERTSCORE_MODEL, lang="en")
            bert_vals = f"{bert_f[0]:.4f},{bert_p[0]:.4f},{bert_r[0]:.4f}"
        else:
            bert_vals = "NA,NA,NA"

        rows.append(f"{p.name},{r['rouge1'].fmeasure:.4f},{r['rouge2'].fmeasure:.4f},{r['rougeL'].fmeasure:.4f},{bert_vals}")

    out = Path(__file__).parent.parent / "results" / "evaluation.csv"
    out.write_text("\n".join(rows), encoding="utf-8")
    print("Evaluation saved to:", out)


if __name__ == "__main__":
    evaluate()
