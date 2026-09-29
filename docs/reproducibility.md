# Reproducibility

Reproducibility is **partial**. The final paper, aggregate result tables, figures, and a deterministic validation script are included. The validator can be run from the repository root:

```bash
python scripts/verify_release.py
```

It checks the published headline metrics, the 27/27 direction and 8/27 exact-value results, the 2,000-draw bootstrap interpretation, required artifacts, README links, and portability. Full feature construction and model retraining require row-level source data that are not redistributed.
