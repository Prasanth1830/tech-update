# 🚀 GitHub Actions Workflow - Complete Setup Guide

## Overview

Your Tech News Agent is ready for **automated daily execution via GitHub Actions**. The workflow will:
- Run **every day at 8:00 AM UTC** automatically
- Fetch tech news from NewsAPI
- Summarize with OpenAI GPT
- Save reports to artifacts
- Optionally send email notifications

---

## ⚡ Quick Start (5 Minutes)

### 1️⃣ Create GitHub Repository
```
Visit: https://github.com/new
Repository name: Tech-news-agent
Description: Custom Python agent for tech news
Visibility: Public (recommended) or Private
Click: Create repository
```

### 2️⃣ Add Repository Secrets
```
Go to: Your Repo → Settings → Secrets and variables → Actions
Create 2 secrets:

Secret 1:
  Name: OPENAI_API_KEY
  Value: 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

Secret 2:
  Name: NEWS_API_KEY
  Value: 98ce48fbcbe14a20b3b184cefcedce06
```

### 3️⃣ Push Code to GitHub
```powershell
cd "c:\Users\pc\OneDrive\Documents\Tech-news-agent"

# Add GitHub as remote (replace YOUR_USERNAME)
git remote add origin https://github.com/YOUR_USERNAME/Tech-news-agent.git

# Rename branch to main (if needed)
git branch -M main

# Push code
git push -u origin main
```

### 4️⃣ Test Workflow
```
1. Go to GitHub repo → Actions tab
2. Select "Daily Tech News Report" workflow
3. Click "Run workflow" → "Run workflow" button
4. Wait 2-3 minutes for completion
5. Download artifacts (tech news report JSON)
```

---

## 📅 Workflow Schedule

| Trigger | Time | Frequency |
|---------|------|-----------|
| **Automatic** | 8:00 AM UTC daily | Every 24 hours |
| **Manual** | Anytime | On-demand via Actions UI |

**UTC to Your Timezone:**
- UTC+0: 8:00 AM
- UTC+1: 9:00 AM
- UTC+5:30: 1:30 PM
- UTC-5: 3:00 AM (previous day)
- UTC-8: 12:00 AM midnight (previous day)

To change schedule, edit `.github/workflows/daily_news.yml` line 5:
```yaml
- cron: '0 8 * * *'  # Change first '0' for hour, second '8' for minute
```

---

## 🔐 Optional: Email Notifications

Add these secrets to receive email reports:

```
EMAIL_SERVER: smtp.gmail.com
EMAIL_PORT: 587
EMAIL_USERNAME: your-email@gmail.com
EMAIL_PASSWORD: your-app-password
EMAIL_RECIPIENT: recipient@example.com
```

For Gmail:
1. Enable 2-factor authentication
2. Generate app password: myaccount.google.com/apppasswords
3. Use app password in EMAIL_PASSWORD secret

---

## 📊 Viewing Results

### In GitHub Actions UI:
1. Go to **Actions** tab in your repository
2. Select **Daily Tech News Report** workflow
3. Click on any workflow run
4. View logs in real-time
5. Download artifacts:
   - Click **Artifacts**
   - Download `news-reports` zip file
   - Extract `tech_news_report_YYYY-MM-DD.json`

### Report Contents:
```json
{
  "timestamp": "2026-01-21T10:00:00",
  "total_articles": 22,
  "impact_breakdown": {
    "high": 3,
    "medium": 8,
    "low": 11
  },
  "articles_by_impact": { ... },
  "articles": [ ... ]
}
```

---

## 🛠️ Troubleshooting

### Workflow Not Running
**Problem**: Workflow doesn't appear in Actions tab
```
Solution:
1. Verify files pushed: git push -u origin main
2. Check branch: Should be 'main' or 'master'
3. Enable Actions: Settings → Actions → Allow all actions
```

### API Key Errors
**Problem**: "invalid API key" or "unauthorized"
```
Solution:
1. Go to Settings → Secrets and variables → Actions
2. Verify OPENAI_API_KEY and NEWS_API_KEY are exact
3. No extra spaces or quotes
4. Keys must include "sk-proj-..." for OpenAI
```

### Quota Exceeded
**Problem**: "insufficient quota" from OpenAI
```
Solution:
1. Go to openai.com/account/billing/overview
2. Add payment method or credits
3. Check usage: openai.com/account/usage
4. Rerun workflow after adding credits
```

### Workflow Errors
**To debug**:
1. Go to workflow run
2. Click "generate-news-report" job
3. Expand failed step for error details
4. Check logs for specific error messages

---

## 📝 Making Changes

### Update Schedule
Edit `.github/workflows/daily_news.yml`:
```yaml
on:
  schedule:
    - cron: '0 9 * * *'  # Change to 9:00 AM UTC
```

### Change Keywords
Edit `src/news_fetcher.py` line 17:
```python
self.keywords = ["AI", "software", "cloud", "infrastructure", "security", "analyst"]
```

### Change Model
Edit `.env` or workflow:
```yaml
MODEL_NAME=gpt-3.5-turbo  # or gpt-4
```

After changes:
```powershell
git add .
git commit -m "Update workflow configuration"
git push
```

---

## ✅ Checklist Before Going Live

- [ ] GitHub account created
- [ ] Repository created (Tech-news-agent)
- [ ] Two secrets added (OPENAI_API_KEY, NEWS_API_KEY)
- [ ] Code pushed: `git push -u origin main`
- [ ] Workflow visible in Actions tab
- [ ] Manual run tested successfully
- [ ] Artifacts downloaded and verified
- [ ] (Optional) Email notifications configured

---

## 📞 Support

### Common Issues:
- **No articles fetched**: Check NEWS_API_KEY quota
- **GPT errors**: Verify OPENAI_API_KEY has credits
- **Workflow not running**: Verify branch is 'main'
- **Artifacts missing**: Check workflow completed without errors

### Workflow File:
Location: `.github/workflows/daily_news.yml`
Schedule: Line 5 (cron expression)
Secrets: Lines 30-32

---

## 🎯 Next Steps

1. **Now**: Push to GitHub with git commands above
2. **After push**: Verify workflow in Actions tab
3. **Test**: Run manually to confirm it works
4. **Monitor**: Check Actions tab for daily runs
5. **Enhance**: Add email notifications (optional)

---

**Your Tech News Agent is production-ready! 🚀**

Questions? Check the full documentation in [README.md](README.md)
