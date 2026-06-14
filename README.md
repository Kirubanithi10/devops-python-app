# devops-python-app

A Python Flask app with a full CI/CD pipeline using GitHub Actions.

![CI Pipeline](https://github.com/Kirubanithi10/devops-python-app/actions/workflows/ci.yml/badge.svg)

## What this project does
- Python Flask REST API
- Automated testing with pytest
- Code linting with flake8
- Docker containerization
- Auto build and push to GitHub Container Registry on every push

## Run locally
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 app.py
```

## Run with Docker
```bash
docker pull ghcr.io/kirubanithi10/devops-python-app:latest
docker run -p 5000:5000 ghcr.io/kirubanithi10/devops-python-app:latest
```

## API Endpoints
- `GET /` — returns Hello DevOps message
- `GET /health` — returns health status
