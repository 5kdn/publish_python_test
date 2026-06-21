Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

$projectRoot = Split-Path -Parent $PSScriptRoot

Push-Location $projectRoot
try {
    python -m pip install ".[build]"
    python -m PyInstaller --noconfirm .\packaging\publish_python.spec
}
finally {
    Pop-Location
}
