# Contributing to OpenGov-EarlyFrench

Thank you for considering contributing to OpenGov-EarlyFrench! This document provides guidelines and instructions for contributing.

## Code of Conduct

By participating in this project, you agree to maintain a respectful and inclusive environment for all contributors.

## How to Contribute

### Reporting Bugs

1. Check if the bug has already been reported in [Issues](https://github.com/llamasearchai/OpenGov-EarlyFrench/issues)
2. If not, create a new issue using the bug report template
3. Include:
   - Clear description of the bug
   - Steps to reproduce
   - Expected vs actual behavior
   - Environment details (OS, Python version, etc.)
   - Relevant logs or screenshots

### Suggesting Features

1. Check existing feature requests in [Issues](https://github.com/llamasearchai/OpenGov-EarlyFrench/issues)
2. Create a new issue using the feature request template
3. Describe:
   - The problem you're trying to solve
   - Your proposed solution
   - Alternative approaches considered
   - Why this feature would be valuable

### Pull Requests

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes following our coding standards
4. Add tests for new functionality
5. Ensure all tests pass (`pytest`)
6. Update documentation as needed
7. Commit your changes with clear messages
8. Push to your fork
9. Open a Pull Request

## Development Setup

```bash
# Clone the repository
git clone https://github.com/llamasearchai/OpenGov-EarlyFrench.git
cd OpenGov-EarlyFrench

# Install dependencies
pip install -e ".[dev]"

# Run tests
pytest

# Run linter
ruff check opengov_earlyfrench tests

# Format code
black opengov_earlyfrench tests

# Type check
mypy opengov_earlyfrench
```

## Coding Standards

### Python Style

- Follow PEP 8 style guide
- Use Black for code formatting (line length: 100)
- Use Ruff for linting
- Add type hints to all functions
- Write docstrings for all public APIs
- No emojis in code or comments
- No placeholders or TODO comments in production code

### Testing

- Write unit tests for new functionality
- Maintain or improve code coverage
- Use pytest fixtures for common setup
- Test both success and error cases
- Include edge cases

### Documentation

- Update README.md for new features
- Add docstrings with examples
- Update API documentation
- Include type hints in docstrings
- Keep CHANGELOG.md up to date

### Commit Messages

Follow the Conventional Commits specification:

```
<type>(<scope>): <subject>

<body>

<footer>
```

Types:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting, etc.)
- `refactor`: Code refactoring
- `test`: Adding or updating tests
- `chore`: Maintenance tasks
- `ci`: CI/CD changes

Examples:
```
feat(pronunciation): Add regional accent support

Implement support for Quebec, Belgian, and Swiss French accents
with pronunciation variations and examples.

Closes #123
```

```
fix(conjugator): Correct passé composé for être verbs

Fix agreement issues with past participles when using être
as auxiliary verb.

Fixes #456
```

## Review Process

1. All pull requests require review before merging
2. Automated CI checks must pass
3. Code coverage should not decrease
4. Documentation must be updated
5. At least one maintainer approval required

## Project Structure

```
opengov-earlyfrench/
├── opengov_earlyfrench/    # Main package
│   ├── core/               # Core learning modules
│   ├── ai/                 # AI features
│   ├── api/                # REST API
│   └── cli.py              # CLI interface
├── tests/                  # Test suite
├── scripts/                # Automation scripts
├── docs/                   # Documentation
└── .github/                # GitHub workflows
```

## Getting Help

- GitHub Issues: For bugs and feature requests
- GitHub Discussions: For questions and discussions
- Email: nikjois@llamasearch.ai

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

## Recognition

Contributors will be recognized in:
- CHANGELOG.md for their specific contributions
- README.md contributors section
- GitHub contributor graphs

Thank you for contributing to making French learning accessible!
