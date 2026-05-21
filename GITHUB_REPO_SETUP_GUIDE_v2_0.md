# GitHub Repository Setup Guide v2.0

1. Create a new GitHub repository.
2. Copy the contents of `release_candidate_repo/` into the repository root.
3. Commit and push.
4. Open the Actions tab.
5. Run **Master Prime External Verifier** manually.
6. Set `independent=true` only if the runner/reviewer is independent from the builder.
7. Download the `master-prime-verifier-evidence` artifact.
8. Fill `external_run_capture_packet/github_external_run_record.json`.
9. Import the completed verifier report using the intake tool.
10. Do not claim Level 6 until the evidence is reviewed and accepted.
