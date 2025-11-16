#!/bin/bash

# GitHub Repository Setup Script for Data Whisperer
# This script will help you push your code to a new GitHub repository

echo "🔮 Data Whisperer - GitHub Repository Setup"
echo "==========================================="
echo ""

# Check if git is installed
if ! command -v git &> /dev/null; then
    echo "❌ Git is not installed. Please install git first:"
    echo "   brew install git"
    exit 1
fi

echo "✅ Git is installed"
echo ""

# Initialize git repository if not already initialized
if [ ! -d .git ]; then
    echo "📦 Initializing Git repository..."
    git init
    echo "✅ Git repository initialized"
else
    echo "✅ Git repository already exists"
fi

echo ""
echo "📝 Setting up .gitignore..."
# Ensure .gitignore exists
if [ ! -f .gitignore ]; then
    cat > .gitignore << 'EOF'
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
venv/
env/
ENV/
.venv
*.log
instance/
.pytest_cache/
.coverage
htmlcov/
dist/
build/
*.egg-info/
.DS_Store
*.pyc
EOF
    echo "✅ .gitignore created"
else
    echo "✅ .gitignore already exists"
fi

echo ""
echo "📋 Staging files for commit..."
git add .
echo "✅ Files staged"

echo ""
echo "💾 Creating initial commit..."
git commit -m "Initial commit: Data Whisperer - Smart field mapping application

Features:
- Intelligent field mapping with confidence scoring
- Smart name matching (camelCase, snake_case, synonyms)
- 5 data transformations (lowercase, uppercase, trim, to_string, to_int)
- Interactive UI with live preview
- Export mapping configurations as JSON
- Beautiful dark-themed responsive design
- Flask REST API with 4 endpoints

Tech stack: Python 3, Flask, Vanilla JavaScript, Modern CSS3"

echo "✅ Initial commit created"
echo ""

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "📌 NEXT STEPS - Create GitHub Repository"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "1. Go to: https://github.com/new"
echo ""
echo "2. Repository settings:"
echo "   • Name: data-whisperer"
echo "   • Description: Smart field mapping between JSON structures with AI-powered suggestions"
echo "   • Visibility: Public (or Private)"
echo "   • DON'T initialize with README, .gitignore, or license"
echo ""
echo "3. After creating the repository, copy YOUR repository URL"
echo "   (It will look like: https://github.com/YOUR_USERNAME/data-whisperer.git)"
echo ""
echo "4. Run these commands (replace YOUR_USERNAME):"
echo ""
echo "   git remote add origin https://github.com/YOUR_USERNAME/data-whisperer.git"
echo "   git branch -M main"
echo "   git push -u origin main"
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "💡 TIP: If you use SSH keys, use this format instead:"
echo "   git remote add origin git@github.com:YOUR_USERNAME/data-whisperer.git"
echo ""
echo "🎉 Your code is ready to push to GitHub!"
echo ""
