# Makefile for OpenGov-EarlyFrench
# Author: Nik Jois <nikjois@llamasearch.ai>

.PHONY: help install test lint format type-check build serve clean docker-build docker-up docker-down docker-logs

help:
	@echo "OpenGov-EarlyFrench - French Language Learning Platform"
	@echo ""
	@echo "Available targets:"
	@echo "  install       - Install dependencies"
	@echo "  test          - Run tests with coverage"
	@echo "  lint          - Run linter"
	@echo "  format        - Format code"
	@echo "  type-check    - Run type checker"
	@echo "  build         - Build and validate project"
	@echo "  serve         - Start API server"
	@echo "  clean         - Clean build artifacts"
	@echo "  docker-build  - Build Docker image"
	@echo "  docker-up     - Start Docker containers"
	@echo "  docker-down   - Stop Docker containers"
	@echo "  docker-logs   - View Docker logs"

install:
	pip install -e ".[dev]"

test:
	pytest tests/ --cov=opengov_earlyfrench --cov-report=term-missing --cov-report=html -v

lint:
	ruff check opengov_earlyfrench tests

format:
	black opengov_earlyfrench tests

type-check:
	mypy opengov_earlyfrench

build:
	@bash scripts/build.sh

serve:
	uvicorn opengov_earlyfrench.api.main:app --reload --host 0.0.0.0 --port 8000

clean:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info
	rm -rf .pytest_cache
	rm -rf .mypy_cache
	rm -rf .ruff_cache
	rm -rf htmlcov
	rm -rf .coverage
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

docker-build:
	docker-compose build

docker-up:
	docker-compose up -d

docker-down:
	docker-compose down

docker-logs:
	docker-compose logs -f api

