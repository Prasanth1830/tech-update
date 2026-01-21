# Tech News Agent - Push to GitHub (PowerShell)
# This script pushes your code to GitHub

param(
    [Parameter(Mandatory=$false)]
    [string]$Username
)

Write-Host "`n╔════════════════════════════════════════════════════════════════╗" -ForegroundColor Cyan
Write-Host "║   Tech News Agent - Push to GitHub                            ║" -ForegroundColor Cyan
Write-Host "╚════════════════════════════════════════════════════════════════╝`n" -ForegroundColor Cyan

# If username not provided, ask for it
if ([string]::IsNullOrEmpty($Username)) {
    $Username = Read-Host "Enter your GitHub username"
}

if ([string]::IsNullOrEmpty($Username)) {
    Write-Host "✗ Error: Username cannot be empty" -ForegroundColor Red
    exit 1
}

# Navigate to project
cd "c:\Users\pc\OneDrive\Documents\Tech-news-agent"

Write-Host "Configuring git remote for user: $Username" -ForegroundColor Yellow

# Remove old remote
git remote remove origin 2>$null

# Add new remote
git remote add origin "https://github.com/$Username/tech-update.git"

Write-Host "Renaming branch to main..." -ForegroundColor Yellow
git branch -M main

Write-Host "`nPushing code to GitHub..." -ForegroundColor Yellow
git push -u origin main

if ($LASTEXITCODE -eq 0) {
    Write-Host "`n✓ Successfully pushed to GitHub!`n" -ForegroundColor Green
    Write-Host "📋 Next Steps:`n" -ForegroundColor Green
    Write-Host "   1. Go to: https://github.com/$Username/tech-update" -ForegroundColor Cyan
    Write-Host "   2. Click: Actions tab" -ForegroundColor Cyan
    Write-Host "   3. See: Daily Tech News Report workflow" -ForegroundColor Cyan
    Write-Host "   4. Click: Run workflow → Run workflow`n" -ForegroundColor Cyan
    Write-Host "🎉 Your Tech News Agent is now live!`n" -ForegroundColor Green
} else {
    Write-Host "`n✗ Push failed. Check credentials and try again." -ForegroundColor Red
}
