# PowerShell script to create branches for python-net language commits
# This script finds all commits with "python-net-{lang}" pattern and creates branches

param(
    [switch]$Push,
    [switch]$DryRun,
    [string[]]$ExcludeLanguages = @("ar")  # Already created branches
)

Write-Host "Finding python-net language commits..." -ForegroundColor Cyan

# Get all commits matching the pattern
$commits = git log --oneline --all | Select-String -Pattern "python-net-\w+" | ForEach-Object {
    $line = $_.Line
    if ($line -match '^(\w+)\s+(python-net-(\w+))') {
        [PSCustomObject]@{
            Hash     = $matches[1]
            Message  = $matches[2]
            Language = $matches[3]
        }
    }
}

if (-not $commits) {
    Write-Host "No python-net language commits found." -ForegroundColor Yellow
    exit 0
}

Write-Host "`nFound $($commits.Count) language commit(s):" -ForegroundColor Green
$commits | Format-Table -AutoSize

# Filter out excluded languages
$commitsToProcess = $commits | Where-Object { $_.Language -notin $ExcludeLanguages }

if ($commitsToProcess.Count -eq 0) {
    Write-Host "`nAll languages are excluded. Nothing to do." -ForegroundColor Yellow
    exit 0
}

Write-Host "`nProcessing $($commitsToProcess.Count) language(s) (excluding: $($ExcludeLanguages -join ', ')):" -ForegroundColor Cyan

$results = @()

foreach ($commit in $commitsToProcess) {
    $branchName = $commit.Message
    $commitHash = $commit.Hash
    $language = $commit.Language
    
    Write-Host "`nProcessing: $branchName ($language) from commit $commitHash" -ForegroundColor White
    
    # Check if branch already exists
    $branchExists = git branch --list $branchName
    
    if ($branchExists) {
        Write-Host "  ⚠ Branch '$branchName' already exists locally. Skipping." -ForegroundColor Yellow
        $results += [PSCustomObject]@{
            Language = $language
            Branch   = $branchName
            Status   = "Skipped (exists)"
            Pushed   = $false
        }
        continue
    }
    
    if ($DryRun) {
        Write-Host "  [DRY RUN] Would create branch: $branchName from $commitHash" -ForegroundColor Magenta
        $results += [PSCustomObject]@{
            Language = $language
            Branch   = $branchName
            Status   = "Dry Run"
            Pushed   = $false
        }
    }
    else {
        try {
            # Create branch
            Write-Host "  Creating branch '$branchName'..." -ForegroundColor Gray
            git branch $branchName $commitHash
            
            if ($LASTEXITCODE -eq 0) {
                Write-Host "  ✓ Branch created successfully" -ForegroundColor Green
                $pushed = $false
                
                # Push if requested
                if ($Push) {
                    Write-Host "  Pushing to origin..." -ForegroundColor Gray
                    git push -u origin $branchName
                    
                    if ($LASTEXITCODE -eq 0) {
                        Write-Host "  ✓ Pushed successfully" -ForegroundColor Green
                        $pushed = $true
                    }
                    else {
                        Write-Host "  ✗ Push failed" -ForegroundColor Red
                    }
                }
                
                $results += [PSCustomObject]@{
                    Language = $language
                    Branch   = $branchName
                    Status   = "Created"
                    Pushed   = $pushed
                }
            }
            else {
                Write-Host "  ✗ Failed to create branch" -ForegroundColor Red
                $results += [PSCustomObject]@{
                    Language = $language
                    Branch   = $branchName
                    Status   = "Failed"
                    Pushed   = $false
                }
            }
        }
        catch {
            Write-Host "  ✗ Error: $_" -ForegroundColor Red
            $results += [PSCustomObject]@{
                Language = $language
                Branch   = $branchName
                Status   = "Error"
                Pushed   = $false
            }
        }
    }
}

# Summary
Write-Host "`n" + ("=" * 70) -ForegroundColor Cyan
Write-Host "SUMMARY" -ForegroundColor Cyan
Write-Host ("=" * 70) -ForegroundColor Cyan
$results | Format-Table -AutoSize

if (-not $DryRun -and -not $Push) {
    Write-Host "`nNote: Branches were created locally but not pushed." -ForegroundColor Yellow
    Write-Host "To push all branches, run: .\create-language-branches.ps1 -Push" -ForegroundColor Yellow
}

if ($DryRun) {
    Write-Host "`nThis was a dry run. No changes were made." -ForegroundColor Magenta
    Write-Host "To execute, run: .\create-language-branches.ps1" -ForegroundColor Yellow
}

Write-Host "`nTo create pull requests, visit:" -ForegroundColor Cyan
foreach ($result in $results | Where-Object { $_.Status -eq "Created" -and $_.Pushed }) {
    Write-Host "  https://github.com/aspose-pdf/Aspose.PDF-Documentation/pull/new/$($result.Branch)" -ForegroundColor Gray
}
