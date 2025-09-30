# OpenGov-EarlyFrench - Quick Start Guide

## Installation

### Option 1: Standard Installation

```bash
# Clone the repository
git clone https://github.com/llamasearchai/opengov-earlyfrench.git
cd opengov-earlyfrench

# Install the package
pip install -e .

# Or with development dependencies
pip install -e ".[dev]"
```

### Option 2: Using UV (Recommended for faster installation)

```bash
# Install uv
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install the package
uv pip install -e .
```

## Configuration

1. Copy the example environment file:
```bash
cp .env.example .env
```

2. Edit `.env` and add your OpenAI API key:
```bash
OPENAI_API_KEY=sk-your-actual-api-key-here
```

## Quick Test

Test that everything is installed correctly:

```bash
# Check version
francais version

# Test pronunciation analysis
francais pronunciation --text "Bonjour"

# Test verb conjugation
francais conjugate être

# Test gender identification
francais gender information
```

## Start the API Server

```bash
# Start the FastAPI server
francais serve

# Or use uvicorn directly
uvicorn opengov_earlyfrench.api.main:app --reload

# Access the API
# - API: http://localhost:8000
# - Docs: http://localhost:8000/docs
# - Health: http://localhost:8000/health
```

## Run Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=opengov_earlyfrench --cov-report=html

# View coverage report
open htmlcov/index.html
```

## Docker Deployment

```bash
# Build and start containers
docker-compose up -d

# View logs
docker-compose logs -f api

# Stop containers
docker-compose down
```

## Common Commands

### Pronunciation Practice

```bash
# Learn nasal vowels
francais pronunciation --nasal

# Practice liaison
francais pronunciation --liaison "les amis"

# Analyze text
francais pronunciation --text "Je voudrais un café"
```

### Verb Conjugation

```bash
# Conjugate in present tense
francais conjugate parler

# Conjugate in different tense
francais conjugate parler --tense imparfait

# Practice reflexive verbs
francais conjugate "se lever" --reflexive

# Practice subjunctive
francais conjugate être --subjunctive
```

### Gender Learning

```bash
# Identify gender
francais gender table

# Practice partitive articles
francais gender anything --partitive

# Learn contractions
francais gender anything --contractions
```

### AI Conversation

```bash
# Start conversation (A1 level)
francais chat

# Start at different level
francais chat --level B1

# Practice scenario
francais scenario café
francais scenario marché
```

## Development

```bash
# Format code
make format

# Run linter
make lint

# Run type checker
make type-check

# Run all checks and tests
make build

# Clean build artifacts
make clean
```

## Troubleshooting

### Import Errors

If you get import errors, ensure the package is installed:
```bash
pip install -e .
```

### Missing Dependencies

Install all dependencies including development tools:
```bash
pip install -e ".[dev]"
```

### OpenAI API Errors

Ensure your `.env` file has a valid OpenAI API key:
```bash
OPENAI_API_KEY=sk-your-actual-key-here
```

### Port Already in Use

If port 8000 is already in use, specify a different port:
```bash
francais serve --port 8001
```

## Next Steps

1. Explore the API documentation at http://localhost:8000/docs
2. Try different CLI commands with `francais --help`
3. Read the full README.md for detailed features
4. Check out the examples in the API documentation

## Support

For issues or questions:
- GitHub Issues: https://github.com/llamasearchai/opengov-earlyfrench/issues
- Email: nikjois@llamasearch.ai

## Author

Nik Jois <nikjois@llamasearch.ai>

Bon apprentissage du français!

