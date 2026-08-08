# production-ready-cicd
Production-ready CI/CD pipeline demonstrating DevOps, DevSecOps and container security best practices with GitHub Actions.

feature branch
      ↓
Pull Request
      ↓
CI
├── Ruff
├── Format check
├── Pytest
├── Docker build
├── Trivy scan
└── SBOM generation
      ↓
Merge to main
      ↓
Release workflow
      ↓
GHCR