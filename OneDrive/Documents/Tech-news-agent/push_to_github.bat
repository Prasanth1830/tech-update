@echo off
REM Tech News Agent - Push to GitHub Script
REM Replace YOUR_USERNAME with your actual GitHub username

setlocal enabledelayedexpansion

cls
echo.
echo ╔════════════════════════════════════════════════════════════════╗
echo ║     Tech News Agent - Push to GitHub                          ║
echo ╚════════════════════════════════════════════════════════════════╝
echo.

set /p USERNAME="Enter your GitHub username: "

if "!USERNAME!"=="" (
    echo Error: GitHub username cannot be empty
    exit /b 1
)

echo.
echo Configuring git remote...
cd /d "c:\Users\pc\OneDrive\Documents\Tech-news-agent"

REM Remove old remote
git remote remove origin 2>nul

REM Add new remote with username
git remote add origin https://github.com/!USERNAME!/tech-update.git

echo.
echo Renaming branch to main...
git branch -M main

echo.
echo Pushing code to GitHub...
git push -u origin main

if %ERRORLEVEL% equ 0 (
    echo.
    echo ✓ Successfully pushed to GitHub!
    echo.
    echo Next steps:
    echo 1. Go to: https://github.com/!USERNAME!/tech-update
    echo 2. Click: Actions tab
    echo 3. Select: Daily Tech News Report
    echo 4. Click: Run workflow
    echo.
) else (
    echo.
    echo ✗ Push failed. Check your credentials and try again.
    echo.
)

pause
