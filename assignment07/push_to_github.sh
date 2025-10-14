#!/bin/bash
# ============================================
# Add and push all p{i}/p{i}.py and other files
# Repo: https://github.com/aabasimel/python-object-oriented-programming
# Author: Ahmed Abasimel
# ============================================

# Exit immediately if a command fails
set -e

# Go to your project directory (change if needed)
cd "$(dirname "$0")"

echo "Current directory: $(pwd)"

# Ensure Git is initialized
if [ ! -d ".git" ]; then
    echo "Initializing new git repository..."
    git init
    git remote add origin https://github.com/aabasimel/programming_in_python
else
    echo "Git repository already initialized."
fi

# Add all p{i}/p{i}.py files if they exist
echo "Adding all p{i}/p{i}.py files..."
for dir in p*/; do
    if [ -d "$dir" ]; then
        pyfile="${dir%/}/${dir%/}.py"
        if [ -f "$pyfile" ]; then
            echo "  Found and adding: $pyfile"
            git add "$pyfile"
        else
            echo "  Skipping $dir (no ${dir%/}.py file found)"
        fi
    fi
done

# Add all other files
echo "Adding all other files..."
git add .

# Commit changes
echo "Committing changes..."
git commit -m "Add p{i}/p{i}.py files and other project files" || echo "No new changes to commit."

# Push to GitHub
echo "Pushing to GitHub..."
git branch -M main
git push -u origin main

echo "✅ All files successfully pushed to https://github.com/aabasimel/python-object-oriented-programming"

