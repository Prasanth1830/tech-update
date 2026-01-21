# GitHub Actions Setup Guide

Follow these steps to enable daily automated news reports via GitHub Actions:

## Step 1: Create a GitHub Repository

1. Go to [github.com/new](https://github.com/new)
2. Name it: `Tech-news-agent`
3. Add a description: "Custom Python agent for tech news fetching and summarization"
4. Choose **Public** or **Private**
5. Click **Create repository**

## Step 2: Add GitHub Secrets

The workflow needs your API keys. Add them as repository secrets:

1. Go to your repository on GitHub
2. Navigate to **Settings > Secrets and variables > Actions**
3. Click **New repository secret** and add:
   - **Name**: `OPENAI_API_KEY`
   - **Value**: `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`

4. Click **New repository secret** again:
   - **Name**: `NEWS_API_KEY`
   - **Value**: `98ce48fbcbe14a20b3b184cefcedce06`

5. (Optional) Add email notification secrets:
   - `EMAIL_SERVER`: Your SMTP server (e.g., smtp.gmail.com)
   - `EMAIL_PORT`: SMTP port (e.g., 587)
   - `EMAIL_USERNAME`: Your email
   - `EMAIL_PASSWORD`: Your app password
   - `EMAIL_RECIPIENT`: Recipient email address

## Step 3: Push Your Code to GitHub

Replace `YOUR_USERNAME` and `YOUR_REPO_NAME` in the commands below:

```bash
# Add GitHub remote
git remote add origin https://github.com/YOUR_USERNAME/Tech-news-agent.git

# Rename branch if needed (local branch is 'GitWork')
git branch -M main

# Push to GitHub
git push -u origin main
```

## Step 4: Verify and Run

1. Go to your repository on GitHub
2. Click the **Actions** tab
3. You should see **Daily Tech News Report** workflow
4. Click on it and select **Run workflow** to trigger manually

## Schedule Information

The workflow is configured to run:
- **Every day at 8:00 AM UTC** (via cron schedule)
- **Manual trigger** available anytime via GitHub Actions UI

## View Results

1. After workflow runs, go to **Actions** tab
2. Click on the workflow run
3. Download artifacts containing the report JSON

## Troubleshooting

- **Workflow not showing**: Enable GitHub Actions in Settings
- **Quota error**: Add credits to OpenAI account
- **Missing API keys**: Verify secrets are added correctly in repository settings
- **Artifact download fails**: Check if workflow completed successfully

---

**Next Steps:**
1. Create GitHub repo with your username
2. Add the API key secrets
3. Push code: `git push -u origin main`
4. Manually trigger workflow for testing
