$ErrorActionPreference = 'Stop'

function Write-ProgressLine {
    param([string]$Message)
    Write-Host "[EduMind] $Message" -ForegroundColor Cyan
}

$projectRoot = (Resolve-Path (Join-Path $PSScriptRoot '')).Path
$datasetRoot = Join-Path $projectRoot 'data\datasets'
$downloadsDir = Join-Path $datasetRoot 'downloads'
$processedDir = Join-Path $datasetRoot 'processed'
$scriptsDir = Join-Path $datasetRoot 'scripts'

Write-ProgressLine "Project root: $projectRoot"
Write-ProgressLine "Checking required tooling..."

$pythonCommand = Get-Command python -ErrorAction SilentlyContinue
if (-not $pythonCommand) {
    throw "Python is required but was not found on PATH. Install Python 3.10+ and try again."
}

$pythonVersion = & python --version 2>&1
Write-ProgressLine "Python: $pythonVersion"

$pipCommand = Get-Command pip -ErrorAction SilentlyContinue
if (-not $pipCommand) {
    Write-ProgressLine "pip not found on PATH; using python -m pip fallback."
}

$gitCommand = Get-Command git -ErrorAction SilentlyContinue
if ($gitCommand) {
    Write-ProgressLine "Git: $((git --version 2>&1))"
} else {
    Write-ProgressLine "Git not found; continuing because the pipeline can work with local files."
}

foreach ($dir in @($downloadsDir, $processedDir, $scriptsDir)) {
    if (-not (Test-Path $dir)) {
        New-Item -ItemType Directory -Path $dir -Force | Out-Null
        Write-ProgressLine "Created directory: $dir"
    } else {
        Write-ProgressLine "Directory exists: $dir"
    }
}

$sourceUrl = 'https://github.com/GhanaNLP/ghana-corpus-builder'
$sourceTarget = Join-Path $downloadsDir 'ghana_corpus_builder_repo'
$sampleTarget = Join-Path $downloadsDir 'ghana_qa_sample.csv'

Write-ProgressLine "Checking whether a local sample dataset is already available..."
if (-not (Test-Path $sampleTarget)) {
    $samplePath = Join-Path $projectRoot 'data\datasets\ghana_qa_sample.csv'
    if (Test-Path $samplePath) {
        Copy-Item $samplePath $sampleTarget -Force
        Write-ProgressLine "Copied bundled sample dataset into download folder."
    }
}

if (-not (Test-Path $sourceTarget) -and $gitCommand) {
    Write-ProgressLine "Cloning GhanaNLP corpus builder sample repository to downloads folder..."
    try {
        git clone --depth 1 $sourceUrl $sourceTarget | Out-Null
    }
    catch {
        Write-ProgressLine "Git clone failed; continuing with local files only."
    }
}

if (-not (Test-Path $sourceTarget) -and -not (Test-Path $sampleTarget)) {
    Write-ProgressLine "No source dataset was found locally or remotely. The script will still build a valid empty dataset structure."
}

$scriptPath = Join-Path $scriptsDir 'build_edumind_dataset.py'
if (Test-Path $scriptPath) {
    Write-ProgressLine "Running EduMind dataset processing pipeline..."
    & python $scriptPath
} else {
    throw "Dataset pipeline script not found: $scriptPath"
}

Write-ProgressLine "Installation and processing step completed."
Write-ProgressLine "Outputs are stored under: $processedDir"
Write-ProgressLine "Raw downloads are stored under: $downloadsDir"
