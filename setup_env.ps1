# Setup environment and install dependencies
Write-Host "Setting up Python environment..." -ForegroundColor Cyan

# Check for venv
if (!(Test-Path "venv")) {
    Write-Host "Creating virtual environment..."
    python -m venv venv
}

# Activate and install
Write-Host "Installing dependencies from requirements.txt..."
.\venv\Scripts\pip install -r requirements.txt

Write-Host "Done! Please restart your IDE and select the './venv' interpreter to clear linter errors." -ForegroundColor Green
