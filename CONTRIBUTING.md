# Contributing to MovieIQ

Thank you for your interest in contributing to MovieIQ! This document provides guidelines and instructions for contributing.

## Code of Conduct

- Be respectful and inclusive
- Provide constructive feedback
- Welcome diverse perspectives
- Keep discussions professional

## Getting Started

### 1. Fork the Repository

```bash
# Click "Fork" on GitHub
git clone https://github.com/YOUR-USERNAME/MovieIQ-Predictive-Analytics-on-Film-Success.git
cd MovieIQ-Predictive-Analytics-on-Film-Success
```

### 2. Create a Feature Branch

```bash
git checkout -b feature/amazing-feature
```

### 3. Set Up Development Environment

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\\Scripts\\activate
pip install -r requirements.txt
```

### 4. Make Your Changes

- Write clean, readable code
- Add docstrings to functions
- Follow PEP 8 style guidelines
- Test your changes locally

### 5. Test Your Changes

```bash
streamlit run app.py
# Test all features in browser
```

### 6. Commit and Push

```bash
git add .
git commit -m "Add: Amazing new feature"
git push origin feature/amazing-feature
```

### 7. Create a Pull Request

- Go to GitHub repository
- Click "New Pull Request"
- Provide clear description of changes
- Reference any related issues

## Types of Contributions

### 🐛 Bug Reports

Create an issue with:
- Clear title and description
- Steps to reproduce
- Expected vs actual behavior
- Screenshots if applicable
- System information (OS, Python version, etc.)

### ✨ Feature Requests

Create an issue with:
- Clear description of feature
- Use cases and benefits
- Potential implementation approach
- Mockups or examples

### 📚 Documentation

- Improve README
- Add code comments
- Create tutorials
- Fix typos

### 🔧 Code Improvements

- Refactoring
- Performance optimization
- Bug fixes
- New features

## Coding Standards

### Python Style

```python
# Follow PEP 8
# 4 spaces for indentation
# max line length 88 characters
# Use type hints where applicable

def process_data(df: pd.DataFrame) -> pd.DataFrame:
    """Process and clean data.
    
    Args:
        df: Input dataframe
        
    Returns:
        Cleaned dataframe
    """
    return df.dropna()
```

### Git Commit Messages

```
Type: Brief description (50 chars max)

Detailed explanation if needed.
Wrap at 72 characters.

Fix #issue-number
```

Types:
- `Add:` New feature
- `Fix:` Bug fix
- `Doc:` Documentation
- `Refactor:` Code refactoring
- `Test:` Adding tests
- `Perf:` Performance improvement

### Branch Naming

```
feature/feature-name
fix/bug-name
doc/documentation-name
refactor/component-name
```

## Pull Request Process

1. **Update Requirements**
   ```bash
   pip freeze > requirements.txt
   ```

2. **Write Tests** (if applicable)

3. **Update Documentation**
   - README.md
   - Docstrings
   - Comments

4. **Self-Review**
   - Check for typos
   - Verify functionality
   - Test on multiple environments

5. **Create PR**
   - Clear title
   - Description of changes
   - Screenshots/videos if UI changes
   - Reference issues

6. **Address Feedback**
   - Respond to reviewer comments
   - Make requested changes
   - Push updates

## Running Tests

```bash
# Install test dependencies (optional)
pip install pytest pytest-streamlit

# Run tests
pytest

# Run with coverage
pytest --cov
```

## Building Documentation

Documentation uses Markdown:

```markdown
# Heading 1
## Heading 2

**Bold text**
*Italic text*

- Bullet point
- Another point

1. Numbered
2. List

[Link text](https://url.com)
```

## Questions?

- Open a GitHub Discussion
- Comment on relevant issues
- Reach out to maintainers

## License

By contributing, you agree that your contributions will be licensed under the same MIT License.

---

Thank you for contributing! 🎉
