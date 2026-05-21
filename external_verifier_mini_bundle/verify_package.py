#!/usr/bin/env python3
from pathlib import Path
import json, sys
root = Path(sys.argv[-1]) if "--package-root" in sys.argv else Path(".")
required = [
    ".github/workflows/external-verifier.yml",
    "tools/ci_verifier.py",
    "README.md"
]
missing = [p for p in required if not (root / p).exists()]
print(json.dumps({"status":"PASS" if not missing else "FAIL", "missing":missing, "boundary":"Minimal release-candidate repo verifier."}, indent=2))
raise SystemExit(0 if not missing else 1)
