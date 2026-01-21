# 🎯 GitHub Actions Quick Reference Card

## Deployment in 4 Steps

```
STEP 1: Create Repo          (1 min)    https://github.com/new
STEP 2: Add Secrets          (2 min)    Settings → Secrets
STEP 3: Push Code            (2 min)    git push -u origin main
STEP 4: Test Workflow        (5 min)    Actions → Run workflow
─────────────────────────────────────────────────────────
TOTAL TIME TO AUTOMATION:    ~10 min ⏱️
```

---

## Essential Commands

```powershell
# Navigate to project
cd "c:\Users\pc\OneDrive\Documents\Tech-news-agent"

# Set up remote (replace USERNAME)
git remote add origin https://github.com/USERNAME/Tech-news-agent.git

# Rename branch
git branch -M main

# Push to GitHub
git push -u origin main

# Check status
git status

# View recent commits
git log --oneline -5
```

---

## GitHub Secrets to Add

| Name | Value |
|------|-------|
| `OPENAI_API_KEY` | `sk-proj-h9DRkbBDBc8J...` (your full key) |
| `NEWS_API_KEY` | `98ce48fbcbe14a20b3b1...` (your full key) |

**Location**: Settings → Secrets and variables → Actions

---

## Files to Know

| File | Purpose | Notes |
|------|---------|-------|
| `.github/workflows/daily_news.yml` | GitHub Actions workflow | Runs daily at 8 AM UTC |
| `src/main.py` | Orchestrator | Main entry point |
| `src/news_fetcher.py` | NewsAPI integration | Fetches articles |
| `src/summarizer.py` | OpenAI integration | Summarizes with GPT |
| `.env.example` | Environment template | Copy to `.env` |
| `requirements.txt` | Dependencies | pip install -r requirements.txt |

---

## Workflow Triggers

### Automatic (Daily)
```yaml
Schedule: 0 8 * * *  (8:00 AM UTC every day)
First run: Next scheduled day after deployment
```

### Manual (On-Demand)
```
Location: GitHub repo → Actions tab
Click: "Daily Tech News Report" workflow
Click: "Run workflow" button
```

---

## Monitoring

### Check Status
1. Go to GitHub repository
2. Click **Actions** tab
3. See workflow history
4. Click run to view logs

### Download Reports
1. Click completed workflow run
2. Scroll to **Artifacts**
3. Download `news-reports` zip
4. Extract `tech_news_report_YYYY-MM-DD.json`

---

## Troubleshooting

| Error | Fix |
|-------|-----|
| "remote already exists" | `git remote remove origin` |
| Workflow not visible | Wait 1-2 min, refresh page |
| API quota error | Add credits to OpenAI account |
| Secret not found | Check exact name (case-sensitive) |
| No articles fetched | Verify NEWS_API_KEY is correct |

---

## After Deployment

✅ Workflow runs automatically 8 AM UTC daily
✅ Manual runs available anytime
✅ Reports saved for 90 days
✅ Full logs visible in Actions tab
✅ Email notifications available (optional)

---

## Make Changes

1. Edit files locally
2. Test: `python -m src.main`
3. Commit: `git add . ; git commit -m "message"`
4. Push: `git push`
5. Workflow auto-updates

---

## Documentation

- **DEPLOYMENT_READY.md** ← Start here!
- **DEPLOYMENT_CHECKLIST.md** ← Step-by-step guide
- **GITHUB_ACTIONS_QUICK_START.md** ← Quick reference
- **README.md** ← Full documentation

---

## Key Facts

- ✅ Fetches: 22+ articles daily
- ✅ Keywords: AI, software, cloud, infrastructure, security, analyst
- ✅ Model: GPT-3.5-turbo (or GPT-4)
- ✅ Schedule: Daily 8 AM UTC + on-demand
- ✅ Storage: 90-day artifact retention
- ✅ Cost: Depends on API usage

---

**You're ready to deploy! Follow the 4 steps above.** 🚀
