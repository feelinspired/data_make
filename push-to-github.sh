#!/bin/bash

# Quick GitHub Push Script
# Run this after creating your GitHub repository

echo ""
echo "🚀 Quick GitHub Push"
echo "===================="
echo ""

# Get GitHub username
read -p "Enter your GitHub username: " username

if [ -z "$username" ]; then
    echo "❌ Username cannot be empty"
    exit 1
fi

echo ""
echo "📝 Repository URL will be:"
echo "   https://github.com/$username/data-whisperer"
echo ""

# Check if remote already exists
if git remote | grep -q "origin"; then
    echo "⚠️  Remote 'origin' already exists. Removing..."
    git remote remove origin
fi

# Add remote
echo "🔗 Adding GitHub remote..."
git remote add origin "https://github.com/$username/data-whisperer.git"

# Ensure on main branch
echo "🌿 Switching to main branch..."
git branch -M main

echo ""
echo "✅ Ready to push!"
echo ""
echo "Run this command to push:"
echo ""
echo "   git push -u origin main"
echo ""
echo "You'll be asked for your GitHub credentials:"
echo "  • Username: $username"
echo "  • Password: Use a Personal Access Token (not your password!)"
echo "    Create one at: https://github.com/settings/tokens"
echo ""

read -p "Push now? (y/n): " push_now

if [ "$push_now" = "y" ] || [ "$push_now" = "Y" ]; then
    echo ""
    echo "🚀 Pushing to GitHub..."
    git push -u origin main
    
    if [ $? -eq 0 ]; then
        echo ""
        echo "🎉 SUCCESS! Your code is now on GitHub!"
        echo ""
        echo "View it at: https://github.com/$username/data-whisperer"
        echo ""
    else
        echo ""
        echo "❌ Push failed. Please check your credentials and try again."
        echo ""
        echo "Manual push command:"
        echo "   git push -u origin main"
        echo ""
    fi
else
    echo ""
    echo "📌 When you're ready, run:"
    echo "   git push -u origin main"
    echo ""
fi
