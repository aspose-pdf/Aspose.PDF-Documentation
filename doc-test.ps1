param (
    [Parameter(Mandatory = $true, HelpMessage = "Specify the mode: 'prod' or 'develop'")]
    [ValidateSet("prod", "develop")]
    [string]$Mode
)

switch ($mode.ToLower()) {
    "prod" {
        $branch = "master"
        $link = "docs.aspose.com"
        Write-Output "Run in Prod mode."
        break
    }
    "develop" {
        $branch = "develop"
        $link = "docs-qa.aspose.com"
        Write-Output "Run in QA mode"
        break
    }
}

Remove-Item E:\doc-test\ -Force -Recurse
New-Item -ItemType Directory -Path E:\doc-test\
Set-Location E:\doc-test\
git clone https://github.com/aspose-pdf/Aspose.PDF-Hugo-template .
npm install
New-Item -ItemType Directory -Path E:\doc-test\content
Set-Location  E:\doc-test\content
git clone -b $branch --single-branch https://github.com/aspose-pdf/Aspose.PDF-Documentation.git .
Set-Location  E:\doc-test\
hugo --baseURL https://$link/pdf/ --config ./config.toml,.\configs\$link-pdf.toml