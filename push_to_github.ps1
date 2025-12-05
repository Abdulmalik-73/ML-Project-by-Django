# Push to GitHub script
# Usage: .\push_to_github.ps1

$repoUrl = "https://github.com/Abdulmalik-73/ML-Project-by-Django.git"
$projectPath = Get-Location

Write-Host "🚀 Pushing Haramaya House Price Prediction to GitHub..." -ForegroundColor Green
Write-Host "Repository: $repoUrl" -ForegroundColor Cyan

# Initialize git if not already initialized
if (-not (Test-Path ".git")) {
    Write-Host "📝 Initializing Git repository..." -ForegroundColor Yellow
    git init
}

# Add all files
Write-Host "📦 Adding all files..." -ForegroundColor Yellow
git add .

# Create commit
Write-Host "💾 Creating commit..." -ForegroundColor Yellow
git commit -m "Initial commit: Haramaya House Price Prediction System with 50K dataset and 96.65% accurate ML model"

# Add remote
Write-Host "🔗 Adding remote repository..." -ForegroundColor Yellow
git remote remove origin 2>$null
git remote add origin $repoUrl

# Push to GitHub
Write-Host "⬆️  Pushing to GitHub..." -ForegroundColor Yellow
git branch -M main
git push -u origin main

Write-Host "✅ Successfully pushed to GitHub!" -ForegroundColor Green
Write-Host "Repository: $repoUrl" -ForegroundColor Cyan
