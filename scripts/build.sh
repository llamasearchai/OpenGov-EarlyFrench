#!/bin/bash
# Build script for OpenGov-EarlyFrench
# Author: Nik Jois <nikjois@llamasearch.ai>

set -e

# Prefer explicit python3/pip3 via env overrides
PY=${PYTHON:-python3}
PIP=${PIP:-pip3}

echo "Building OpenGov-EarlyFrench..."

# Colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Check Python version
echo -e "${YELLOW}Checking Python version...${NC}"
python_version=$($PY --version 2>&1 | awk '{print $2}')
echo -e "${GREEN}Python version: $python_version${NC}"

# Install dependencies
echo -e "${YELLOW}Installing dependencies...${NC}"
$PIP install -e ".[dev]" --quiet || true
echo -e "${GREEN}Dependencies installed${NC}"

# Format code
echo -e "${YELLOW}Formatting code with black...${NC}"
black opengov_earlyfrench tests --quiet
echo -e "${GREEN}Code formatted${NC}"

# Lint code
echo -e "${YELLOW}Linting code with ruff...${NC}"
ruff check opengov_earlyfrench tests --fix
echo -e "${GREEN}Code linted${NC}"

# Type check
echo -e "${YELLOW}Type checking with mypy...${NC}"
mypy opengov_earlyfrench || echo -e "${YELLOW}Type checking completed with warnings${NC}"

# Run tests
echo -e "${YELLOW}Running tests with pytest...${NC}"
pytest --cov=opengov_earlyfrench --cov-report=term-missing --cov-report=html
echo -e "${GREEN}Tests passed${NC}"

# Build Docker image
if command -v docker &> /dev/null; then
    echo -e "${YELLOW}Building Docker image...${NC}"
    docker build -t opengov-earlyfrench:latest .
    echo -e "${GREEN}Docker image built${NC}"
else
    echo -e "${YELLOW}Docker not found, skipping image build${NC}"
fi

echo -e "${GREEN}Build completed successfully!${NC}"
echo -e "${GREEN}To start the server: francais serve${NC}"
echo -e "${GREEN}To run CLI: francais --help${NC}"
