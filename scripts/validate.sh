#!/bin/bash
# Validation script for OpenGov-EarlyFrench
# Author: Nik Jois <nikjois@llamasearch.ai>

set -e

# Prefer explicit python3/pip3 via env overrides
PY=${PYTHON:-python3}
PIP=${PIP:-pip3}

echo "==================================================================="
echo "OpenGov-EarlyFrench - Complete Validation"
echo "==================================================================="

# Colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Track overall success
ALL_PASSED=true

echo ""
echo -e "${BLUE}1. Checking Project Structure...${NC}"
echo "-------------------------------------------------------------------"

# Check essential files
files_to_check=(
    "pyproject.toml"
    "README.md"
    "LICENSE"
    "Dockerfile"
    "docker-compose.yml"
    "Makefile"
    "opengov_earlyfrench/__init__.py"
    "opengov_earlyfrench/config.py"
    "opengov_earlyfrench/cli.py"
    "opengov_earlyfrench/api/main.py"
    "opengov_earlyfrench/core/pronunciation_coach.py"
    "opengov_earlyfrench/core/verb_conjugator.py"
    "opengov_earlyfrench/core/gender_teacher.py"
    "opengov_earlyfrench/ai/conversation.py"
    "tests/test_pronunciation_coach.py"
    "tests/test_verb_conjugator.py"
    "tests/test_gender_teacher.py"
    "tests/test_api.py"
)

for file in "${files_to_check[@]}"; do
    if [ -f "$file" ]; then
        echo -e "${GREEN}✓${NC} $file"
    else
        echo -e "${RED}✗${NC} $file (missing)"
        ALL_PASSED=false
    fi
done

echo ""
echo -e "${BLUE}2. Checking Python Environment...${NC}"
echo "-------------------------------------------------------------------"

# Check Python version
python_version=$($PY --version 2>&1 | awk '{print $2}')
echo -e "${GREEN}✓${NC} Python version: $python_version"

# Check if package is installed
if $PY -c "import opengov_earlyfrench" 2>/dev/null; then
    echo -e "${GREEN}✓${NC} Package is importable"
    
    # Check version
    version=$($PY -c "import opengov_earlyfrench; print(opengov_earlyfrench.__version__)")
    echo -e "${GREEN}✓${NC} Package version: $version"
    
    # Check author
    author=$($PY -c "import opengov_earlyfrench; print(opengov_earlyfrench.__author__)")
    echo -e "${GREEN}✓${NC} Package author: $author"
else
    echo -e "${YELLOW}⚠${NC} Package not installed (run: pip install -e .)"
fi

echo ""
echo -e "${BLUE}3. Checking Module Imports...${NC}"
echo "-------------------------------------------------------------------"

# Test core imports
modules_to_test=(
    "opengov_earlyfrench.config"
    "opengov_earlyfrench.core.pronunciation_coach"
    "opengov_earlyfrench.core.verb_conjugator"
    "opengov_earlyfrench.core.gender_teacher"
    "opengov_earlyfrench.core.models"
    "opengov_earlyfrench.ai.conversation"
    "opengov_earlyfrench.api.main"
    "opengov_earlyfrench.cli"
)

for module in "${modules_to_test[@]}"; do
    if $PY -c "import $module" 2>/dev/null; then
        echo -e "${GREEN}✓${NC} $module"
    else
        echo -e "${RED}✗${NC} $module (import failed)"
        ALL_PASSED=false
    fi
done

echo ""
echo -e "${BLUE}4. Running Tests...${NC}"
echo "-------------------------------------------------------------------"

if command -v pytest &> /dev/null; then
    if pytest tests/ -q --tb=no; then
        echo -e "${GREEN}✓${NC} All tests passed"
    else
        echo -e "${RED}✗${NC} Some tests failed"
        ALL_PASSED=false
    fi
else
    echo -e "${YELLOW}⚠${NC} pytest not found, skipping tests"
fi

echo ""
echo -e "${BLUE}5. Checking Code Quality...${NC}"
echo "-------------------------------------------------------------------"

# Check with ruff
if command -v ruff &> /dev/null; then
    if ruff check opengov_earlyfrench tests --quiet 2>/dev/null; then
        echo -e "${GREEN}✓${NC} Ruff linting passed"
    else
        echo -e "${YELLOW}⚠${NC} Ruff found some issues (non-critical)"
    fi
else
    echo -e "${YELLOW}⚠${NC} ruff not found, skipping lint check"
fi

# Check with black
if command -v black &> /dev/null; then
    if black --check opengov_earlyfrench tests --quiet 2>/dev/null; then
        echo -e "${GREEN}✓${NC} Black formatting check passed"
    else
        echo -e "${YELLOW}⚠${NC} Code formatting needs adjustment"
    fi
else
    echo -e "${YELLOW}⚠${NC} black not found, skipping format check"
fi

echo ""
echo -e "${BLUE}6. Checking CLI Commands...${NC}"
echo "-------------------------------------------------------------------"

if command -v francais &> /dev/null; then
    echo -e "${GREEN}✓${NC} CLI command 'francais' is available"
    
    # Test version command
    if francais version &>/dev/null; then
        echo -e "${GREEN}✓${NC} francais version command works"
    fi
else
    echo -e "${YELLOW}⚠${NC} CLI command 'francais' not found (run: pip install -e .)"
fi

echo ""
echo -e "${BLUE}7. Checking Docker Configuration...${NC}"
echo "-------------------------------------------------------------------"

if command -v docker &> /dev/null; then
    echo -e "${GREEN}✓${NC} Docker is available"
    
    if [ -f "Dockerfile" ]; then
        echo -e "${GREEN}✓${NC} Dockerfile exists"
    fi
    
    if [ -f "docker-compose.yml" ]; then
        echo -e "${GREEN}✓${NC} docker-compose.yml exists"
    fi
else
    echo -e "${YELLOW}⚠${NC} Docker not found"
fi

echo ""
echo -e "${BLUE}8. Checking Scripts...${NC}"
echo "-------------------------------------------------------------------"

scripts=(
    "scripts/build.sh"
    "scripts/test.sh"
    "scripts/deploy.sh"
    "scripts/validate.sh"
)

for script in "${scripts[@]}"; do
    if [ -f "$script" ] && [ -x "$script" ]; then
        echo -e "${GREEN}✓${NC} $script (executable)"
    elif [ -f "$script" ]; then
        echo -e "${YELLOW}⚠${NC} $script (not executable, run: chmod +x $script)"
    else
        echo -e "${RED}✗${NC} $script (missing)"
        ALL_PASSED=false
    fi
done

echo ""
echo "==================================================================="
echo "Validation Summary"
echo "==================================================================="

if [ "$ALL_PASSED" = true ]; then
    echo -e "${GREEN}✓ All critical checks passed!${NC}"
    echo ""
    echo "Next steps:"
    echo "  1. Install package: pip install -e ."
    echo "  2. Run tests: make test"
    echo "  3. Start server: make serve"
    echo "  4. Or use CLI: francais --help"
    echo "  5. Deploy with Docker: make docker-up"
    exit 0
else
    echo -e "${RED}✗ Some checks failed. Please review the output above.${NC}"
    exit 1
fi
