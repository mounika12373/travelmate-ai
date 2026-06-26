param (
    [Parameter(Mandatory=$true)]
    [string]$Token
)

$ErrorActionPreference = "Stop"

# 1. Define Runner Directory inside the workspace to avoid root admin conflicts
$RunnerDir = Join-Path $PSScriptRoot "gitlab-runner"
if (-not (Test-Path $RunnerDir)) {
    New-Item -ItemType Directory -Path $RunnerDir | Out-Null
    Write-Host "[OK] Created directory: $RunnerDir"
}

$ExePath = Join-Path $RunnerDir "gitlab-runner.exe"

# 2. Download GitLab Runner binary if not present
if (-not (Test-Path $ExePath)) {
    Write-Host "[INFO] Downloading GitLab Runner for Windows..."
    $DownloadUrl = "https://gitlab-runner-downloads.s3.amazonaws.com/latest/binaries/gitlab-runner-windows-amd64.exe"
    try {
        Invoke-WebRequest -Uri $DownloadUrl -OutFile $ExePath -UseBasicParsing
        Write-Host "[OK] Download completed successfully."
    } catch {
        Write-Error "Failed to download GitLab Runner. Please verify your internet connection. Error: $_"
    }
} else {
    Write-Host "[INFO] GitLab Runner binary already exists."
}

# Move into the runner directory
Push-Location $RunnerDir

# 3. Register the Runner non-interactively
Write-Host "[INFO] Registering local GitLab Runner with code.swecha.org..."
try {
    # Run registration non-interactively
    & ".\gitlab-runner.exe" register `
        --non-interactive `
        --url "https://code.swecha.org/" `
        --registration-token "$Token" `
        --executor "shell" `
        --shell "powershell" `
        --description "Local Hackathon Runner" `
        --tag-list "local,windows"
        
    Write-Host "[OK] Runner registered successfully."
} catch {
    Pop-Location
    Write-Error "Failed to register runner. Please double-check your Token. Error: $_"
}

# 4. Install and Start the service
Write-Host "[INFO] Installing and starting GitLab Runner service..."
Write-Host "[NOTE] This step requires Administrator rights. If it fails, please run PowerShell as Administrator and run: cd '$RunnerDir'; .\gitlab-runner.exe install; .\gitlab-runner.exe start"

try {
    & ".\gitlab-runner.exe" install
    & ".\gitlab-runner.exe" start
    Write-Host "[SUCCESS] Local GitLab Runner is fully set up and running!"
} catch {
    Write-Host "[WARNING] Service installation requires administrator privileges. Please open PowerShell as Administrator and run the following manually:"
    Write-Host "cd '$RunnerDir'"
    Write-Host ".\gitlab-runner.exe install"
    Write-Host ".\gitlab-runner.exe start"
}

Pop-Location
