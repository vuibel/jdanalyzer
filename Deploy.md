# Deployment Guide

## Prerequisites

- Git installed
- GitHub account
- Repository files ready

## Deployment Steps

### Step 1: Initialize Git Repo
```bash
cd jdanalyzer
git init
git add .
git commit -m "Initial commit: Job Description Fit Analyzer v1.0"
```

### Step 2: Create GitHub Repo
1. Go to https://github.com/new
2. Name: `jdanalyzer` (or your preferred name)
3. Description: "AI-powered tool to analyze job posting fit and generate positioning strategies"
4. Public or Private (your choice)
5. **Do NOT** initialize with README (you already have one)
6. Click "Create repository"

### Step 3: Push to GitHub
```bash
git remote add origin git@github.com:YOUR_USERNAME/jdanalyzer.git
git branch -M main
git push -u origin main
```

## Common Issues

**"Git push rejected"**
- Make sure you've set up SSH keys with GitHub
- Or use HTTPS: `git remote set-url origin https://github.com/YOUR_USERNAME/jdanalyzer.git`

## Next Steps

1. Customize `CANDIDATE_PROFILE` in `analyze_jd.py` with your background
2. Test with sample job descriptions
3. Start analyzing real job postings
