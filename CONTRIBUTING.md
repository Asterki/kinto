# Contributing to Kinto

Thank you for your interest in contributing to Kinto! We welcome contributions from the community and are excited to see what you'll bring to the project.

## Table of Contents

- [Contributing to Kinto](#contributing-to-kinto)
  - [Table of Contents](#table-of-contents)
  - [Getting Started](#getting-started)
  - [Code of Conduct](#code-of-conduct)
  - [How to Contribute](#how-to-contribute)
    - [Reporting Issues](#reporting-issues)
    - [Suggesting Features](#suggesting-features)
    - [Submitting Pull Requests](#submitting-pull-requests)
  - [Development Workflow](#development-workflow)
    - [Setting Up the Development Environment](#setting-up-the-development-environment)
    - [Writing Tests](#writing-tests)
    - [Commit Guidelines](#commit-guidelines)

## Getting Started

Before you start contributing, make sure you take a look at the project documentation, which will give you an overview of the project's architecture, features, and current status.

## Code of Conduct

We adhere to a [Code of Conduct](CODE_OF_CONDUCT.md) that we expect all contributors to follow. Please make sure you read and understand it.

## How to Contribute

### Reporting Issues

If you encounter any issues with the project, feel free to report them by opening a new issue. Please include the following details:

- A clear and descriptive title.
- Steps to reproduce the issue.
- Any relevant logs or screenshots.
- The version of Python and Kinto you are using.

### Suggesting Features

We are always looking to improve the project! If you have a feature request, please open a new issue and describe:

- The problem your feature would solve.
- A detailed explanation of how it would work.
- Any examples or mockups if applicable.

### Submitting Pull Requests

We love pull requests! Here's a quick guide:

1. **Fork the repository**: Click the "Fork" button at the top right of the project page.
2. **Clone your fork**: 
   ```bash
   git clone https://github.com/Asterki/kinto.git
   ```
3. **Create a branch**: 
   ```bash
   git checkout -b feature-branch-name
   ```
4. **Make your changes**: Ensure your code follows the project's style guide.
5. **Test your changes**: Run existing tests and add new tests as necessary.
6. **Commit your changes**:
   ```bash
   git commit -m "Add concise and descriptive commit message"
   ```
7. **Push to your fork**:
   ```bash
   git push origin feature-branch-name
   ```
8. **Submit a pull request**: Go to the original repository on GitHub and click "New Pull Request."

## Development Workflow

### Setting Up the Development Environment

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Asterki/kinto.git
   ```
2. **Create a virtual environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

### Writing Tests

We use [unittest](https://docs.python.org/3/library/unittest.html) for testing. Ensure all new features and bug fixes come with appropriate test coverage. To run tests, use:

```bash
python3 -m unittest 
```

### Commit Guidelines

- Use clear and concise commit messages.
- Follow the [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) specification.
- Break up larger commits into smaller, logically grouped changes.

Thank you for contributing to Kinto!
