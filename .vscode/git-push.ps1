
Write-Host "====================================="
Write-Host "       GITHUB AUTOMATIC PUSH"
Write-Host "====================================="

# Check Git repository
git rev-parse --is-inside-work-tree | Out-Null

if ($LASTEXITCODE -ne 0) {
    Write-Host "Error: Not inside a Git repository."
    exit 1
}

# Get commit message
$commitMessage = Read-Host "Enter your commit message"

if ([string]::IsNullOrWhiteSpace($commitMessage)) {
    Write-Host "Error: Commit message cannot be empty."
    exit 1
}

# Identify current branch
$branch = git branch --show-current

if ([string]::IsNullOrWhiteSpace($branch)) {
    Write-Host "Error: Could not identify Git branch."
    exit 1
}

Write-Host "`nAdding changes..."
git add -A

if ($LASTEXITCODE -ne 0) {
    Write-Host "Error: Git add failed."
    exit 1
}

# Check whether there are changes to commit
git diff --cached --quiet

if ($LASTEXITCODE -eq 0) {
    Write-Host "No changes to commit."
    exit 0
}
elseif ($LASTEXITCODE -ne 1) {
    Write-Host "Error: Could not check staged changes."
    exit 1
}

Write-Host "`nCreating commit..."
git commit -m "$commitMessage"

if ($LASTEXITCODE -ne 0) {
    Write-Host "Error: Git commit failed."
    exit 1
}

Write-Host "`nPushing to GitHub..."
git push -u origin $branch

if ($LASTEXITCODE -ne 0) {
    Write-Host "Error: Git push failed. Check the Git output."
    exit 1
}

Write-Host "`n====================================="
Write-Host "  SUCCESS! PUSHED TO GITHUB"
Write-Host "====================================="
