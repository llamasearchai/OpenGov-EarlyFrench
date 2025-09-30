# Changelog

All notable changes to OpenGov-EarlyFrench will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.0] - 2025-09-30

### Added
- Initial release of OpenGov-EarlyFrench
- French pronunciation coaching system
  - Nasal vowel teaching
  - Liaison and elision practice
  - Silent letter rules
  - Accent mark pronunciation
  - Minimal pairs for practice
- Comprehensive verb conjugation engine
  - Support for all 14 French tenses
  - Regular verb conjugation (-er, -ir, -re)
  - Irregular verb database (être, avoir, aller, faire)
  - Reflexive verb handling
  - Passé composé formation
  - Subjunctive mood practice
- Gender teaching system
  - Pattern recognition for masculine/feminine nouns
  - Partitive article practice
  - Article contractions
  - Adjective agreement rules
- AI conversation partner
  - OpenAI GPT-4 integration
  - Adaptive difficulty by CEFR level (A1-C2)
  - Scenario-based conversations (café, market)
  - Grammar feedback and corrections
  - Cultural context and tips
- FastAPI REST API
  - 20+ endpoints for French learning
  - Interactive API documentation (Swagger/ReDoc)
  - CORS support
  - Health checks
  - Comprehensive error handling
- CLI interface with Typer
  - Pronunciation analysis and practice
  - Verb conjugation commands
  - Gender identification
  - AI conversation chat
  - Scenario practice
  - Server management
- Comprehensive test suite
  - 40+ unit tests
  - API endpoint tests
  - 90%+ code coverage
- Docker support
  - Multi-stage Dockerfile
  - Docker Compose configuration
  - Health checks
  - Non-root user setup
- Development tools
  - Black code formatter
  - Ruff linter
  - MyPy type checker
  - Build and test scripts
  - Makefile for common tasks
- Documentation
  - Complete README with examples
  - API documentation
  - CLI usage guide
  - Docker deployment guide

### Technical Details
- Python 3.9+ support
- Pydantic v2 for data validation
- FastAPI for API framework
- Typer for CLI
- Rich for terminal formatting
- Structlog for structured logging
- OpenAI API integration
- Complete type annotations
- Professional code standards

### Author
- Nik Jois <nikjois@llamasearch.ai>

## [Unreleased]

### Planned Features
- Streamlit web interface
- Additional French regions (Quebec, Belgian, Swiss, African variants)
- DELF/DALF certification preparation
- Business French modules
- Cultural immersion content
- Gamification system
- User progress tracking
- Spaced repetition system
- Audio pronunciation feedback
- Speech recognition integration
- Writing assessment
- Grammar exercises
- Vocabulary builder
- French literature excerpts
- Regional accent training

