# Master Prime Release Candidate Repository

This is the minimal repository layout for external verification.

## Run locally

```bash
python tools/ci_verifier.py --package-root . --out-dir ci_verifier_output --reviewer-name "Verifier Name" --independent
```

## GitHub Actions

Run `.github/workflows/external-verifier.yml` manually.

Boundary: This repo template is not itself external proof.
