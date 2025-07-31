---
title: "Introducing mkdocs-llmstxt-md: Making Documentation LLM-Friendly"
description: "A new MkDocs plugin that bridges the gap between traditional documentation and AI/LLM workflows by serving markdown files alongside HTML and generating LLM-optimized index files."
author: "Nok Lam Chan"
date: "2025-07-31"
categories:
  - python
  - llm
  - mkdocs
keywords:
  - MkDocs
  - LLM
  - Documentation
  - AI
  - Markdown
  - Python Plugin
---

I'm excited to announce the release of **mkdocs-llmstxt-md**, a new MkDocs plugin that bridges the gap between traditional documentation and AI/LLM workflows.

## The Problem

As AI tools become more integrated into development workflows, there's a growing need for documentation that's easily consumable by Large Language Models (LLMs). While HTML documentation looks great for humans, LLMs work much better with structured markdown content. This creates a friction point: do you optimize for human readers or AI consumption?

## The Solution

`mkdocs-llmstxt-md` solves this by making your MkDocs documentation work seamlessly for both audiences. The plugin automatically:

- **Serves original markdown files** at `.md` URLs alongside your HTML pages
- **Generates `llms.txt` index files** that provide LLMs with a structured overview of your documentation
- **Creates `llms-full.txt` files** containing your complete documentation in a single, LLM-friendly format
- **Adds copy-to-markdown buttons** so users can easily grab markdown content

## Key Features

### Smart Content Organization
The plugin uses a flexible section-based configuration that supports glob patterns:

```yaml
plugins:
  - llms-txt:
      sections:
        "Getting Started":
          - index.md: "Main documentation"
          - quickstart.md: "Quick start guide"
        "API Reference":
          - "api/*.md"  # Automatically includes all API docs
```

### LLM-Optimized Output
The generated `llms.txt` provides a clean, structured index that LLMs can quickly parse:

```markdown
# My Documentation

Brief description of the project

## Getting Started
- [Documentation](https://example.com/index.md): Main documentation
- [Quick Start](https://example.com/quickstart.md): Quick start guide

## API Reference
- [Overview](https://example.com/api/overview.md)
- [Functions](https://example.com/api/functions.md)
```

### Universal Compatibility
Since the plugin generates standard markdown files and uses simple HTTP serving, it works with any hosting platform and doesn't require special server configuration.

## Real-World Impact

This approach has immediate benefits for teams using AI coding assistants:

- **Faster context loading**: LLMs can quickly ingest documentation via direct markdown URLs
- **No HTML parsing**: Clean markdown content eliminates formatting noise
- **Single-file option**: The `llms-full.txt` provides complete documentation in one request
- **Human-friendly**: Original HTML documentation remains unchanged

## Modern Release Process

The project showcases modern Python packaging practices with GitHub Actions and PyPI Trusted Publishing - no API tokens required, just secure OIDC authentication.

## Get Started

Install the plugin:
```bash
pip install mkdocs-llmstxt-md
```

Add it to your `mkdocs.yml`:
```yaml
plugins:
  - llms-txt:
      sections:
        "Documentation":
          - "*.md"
```

That's it! Your next `mkdocs build` will generate LLM-friendly versions of your documentation.

## Looking Forward

This plugin represents a broader trend toward making development tools more AI-friendly without sacrificing human usability. As AI becomes more integrated into our workflows, we need infrastructure that works seamlessly for both human and machine consumption.

Try it out and let me know how it works for your documentation needs!

---

**Links:**
- [PyPI Package](https://pypi.org/project/mkdocs-llmstxt-md/)
- [GitHub Repository](https://github.com/noklam/mkdocs-llmstxt-md)
- [Documentation](https://github.com/noklam/mkdocs-llmstxt-md#readme)