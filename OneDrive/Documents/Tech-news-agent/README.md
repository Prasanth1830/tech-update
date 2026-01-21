# 🚀 Tech News Agent

A custom Python agent that fetches tech news articles and generates business-focused summaries using OpenAI GPT-4. Fully automated with GitHub Actions or local cron scheduling.

## 📋 Features

- **News Fetching**: Pulls articles from NewsAPI based on tech keywords (AI, software, cloud, infrastructure, security, analyst)
- **AI Summarization**: Uses GPT-4 to generate concise summaries with business impact analysis
- **Impact Classification**: Categorizes articles as HIGH, MEDIUM, or LOW impact
- **JSON Reports**: Generates detailed JSON reports saved to `output/` directory
- **Automation**: 
  - GitHub Actions workflow for daily scheduled runs
  - Local scheduler using APScheduler for development/testing
- **Comprehensive Logging**: Detailed console output and structured reporting

## 🛠️ Installation & Setup

### Prerequisites
- Python 3.9+
- API Keys for:
  - [OpenAI API](https://platform.openai.com/api-keys)
  - [NewsAPI](https://newsapi.org/)
  - GitHub account (for automation)

### Step 1: Clone & Install Dependencies

```bash
cd Tech-news-agent
pip install -r requirements.txt
```

### Step 2: Configure Environment Variables

Create a `.env` file in the root directory:

```bash
cp .env.example .env
```

Edit `.env` with your API keys:
```env
OPENAI_API_KEY=your_openai_api_key_here
NEWS_API_KEY=your_newsapi_key_here
MODEL_NAME=gpt-4
MAX_ARTICLES_PER_KEYWORD=5
```

## 🚀 Usage

### Run Agent Manually

```bash
python -m src.main
```

This will:
1. Fetch articles from NewsAPI based on predefined keywords
2. Generate summaries using GPT-4
3. Classify by business impact
4. Save report to `output/tech_news_report_YYYY-MM-DD.json`
5. Print summary to console

### Local Scheduler (Development)

Run the agent daily at 8:00 AM:

```bash
# Add 'schedule' to requirements.txt first
pip install schedule

python scheduler.py
```

Press `Ctrl+C` to stop.

### GitHub Actions (Production)

The workflow runs automatically every day at 8:00 AM UTC.

**Setup Steps:**

1. Push code to GitHub repository
2. Add secrets in GitHub repo settings (`Settings > Secrets and variables > Actions`):
   - `OPENAI_API_KEY`
   - `NEWS_API_KEY`

3. (Optional) Add email notification secrets:
   - `EMAIL_SERVER`
   - `EMAIL_PORT`
   - `EMAIL_USERNAME`
   - `EMAIL_PASSWORD`
   - `EMAIL_RECIPIENT`

4. Monitor runs in **Actions** tab
5. Download reports from artifacts

## 📁 Project Structure

```
Tech-news-agent/
├── src/
│   ├── main.py           # Main orchestrator
│   ├── news_fetcher.py   # NewsAPI integration
│   └── summarizer.py     # GPT-4 summarization
├── .github/
│   └── workflows/
│       └── daily_news.yml   # GitHub Actions workflow
├── output/               # Generated reports (created on first run)
├── .env.example          # Environment template
├── requirements.txt      # Python dependencies
├── scheduler.py          # Local cron scheduler
└── README.md             # This file
```

## 📊 Report Format

Generated JSON reports include:
- **timestamp**: When report was generated
- **total_articles**: Number of articles processed
- **impact_breakdown**: Count by impact level
- **articles_by_impact**: Articles grouped by impact
- **articles**: Full article data with summaries

Example:
```json
{
  "timestamp": "2026-01-21T10:30:00",
  "total_articles": 15,
  "impact_breakdown": {
    "high": 3,
    "medium": 8,
    "low": 4
  },
  "articles_by_impact": {
    "high": [...],
    "medium": [...],
    "low": [...]
  }
}
```

## 🔑 Configuration

Edit `.env` to customize:

| Variable | Description | Default |
|----------|-------------|---------|
| `OPENAI_API_KEY` | Your OpenAI API key | Required |
| `NEWS_API_KEY` | Your NewsAPI key | Required |
| `MODEL_NAME` | GPT model to use | gpt-4 |
| `MAX_ARTICLES_PER_KEYWORD` | Articles per keyword | 5 |

Keywords are hardcoded in `src/news_fetcher.py`:
- AI
- software
- cloud
- infrastructure
- security
- analyst

## 🐛 Troubleshooting

### "NEWS_API_KEY not found"
- Ensure `.env` file exists and contains `NEWS_API_KEY`
- Check for typos in environment variable names

### "OPENAI_API_KEY not found"
- Verify OpenAI key is set in `.env`
- Ensure key has GPT-4 access

### Low article count
- Check NewsAPI quota (free tier: 100 requests/day)
- Extend date range in `news_fetcher.py` (currently 7 days)
- Add more keywords to search

### API Rate Limits
- NewsAPI: 100/day (free) or higher (paid)
- OpenAI: Check usage at https://platform.openai.com/account/usage

## 📈 Enhancement Ideas

- Add Slack/Email notifications with high-impact articles
- Store reports in database (PostgreSQL, MongoDB)
- Create web dashboard to view reports
- Add sentiment analysis
- Multi-language support
- Filter by industry/company
- Integrate with downstream tools (Jira, Confluence)

## 📝 License

MIT License - Feel free to use and modify

## 🤝 Contributing

Contributions welcome! Feel free to submit issues and pull requests.

## 📧 Contact

For questions or support, open an issue in the repository.
