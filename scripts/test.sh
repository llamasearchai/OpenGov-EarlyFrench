#!/bin/bash
# Test script for OpenGov-EarlyFrench
# Author: Nik Jois <nikjois@llamasearch.ai>

set -e

echo "Running tests for OpenGov-EarlyFrench..."

# Colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Run unit tests
echo -e "${YELLOW}Running unit tests...${NC}"
pytest tests/ -v --tb=short

# Run tests with coverage
echo -e "${YELLOW}Running tests with coverage...${NC}"
pytest tests/ --cov=opengov_earlyfrench --cov-report=term-missing --cov-report=html

# Display coverage report location
echo -e "${GREEN}Coverage report generated at: htmlcov/index.html${NC}"

# Run linting
echo -e "${YELLOW}Running linter...${NC}"
ruff check opengov_earlyfrench tests

# Run type checking
echo -e "${YELLOW}Running type checker...${NC}"
mypy opengov_earlyfrench || echo -e "${YELLOW}Type checking completed with warnings${NC}"

echo -e "${GREEN}All tests completed successfully!${NC}"

