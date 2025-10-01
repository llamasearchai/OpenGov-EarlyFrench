Title: Maintain 100% coverage, robust CLI, CI-ready

Summary
- Python 3.9 compatibility across the codebase
- Verified CLI and API; added launcher script
- 100% tests and coverage with comprehensive CLI/API tests
- Pre-commit hooks and GitHub Actions CI
- Documentation updates (badges, banner)

Changes
- Compatibility: replace PEP 604 unions with typing.Union/Optional
- Tests: add CLI, API chat, configuration, and extra verb coverage
- Tooling: add pre-commit (ruff/black/mypy) and CI workflow
- Scripts: prefer PY/PIP env, safer install/test flows
- Docs: CI and coverage badges; project banner

Validation
- pytest --cov=opengov_earlyfrench: 100% coverage
- ruff check: clean
- black --check: clean
- Manual smoke tests for CLI and API endpoints

Checklist
- [ ] CI passes on this PR
- [ ] No placeholders or emojis in code or docs
- [ ] CLI commands work as described
- [ ] API endpoints respond and /docs renders

Notes
- The chat command gracefully handles missing OPENAI_API_KEY during tests.

