$ErrorActionPreference = 'Stop'
$root = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)
$docxPath = Join-Path $root 'thesis\final_thesis.docx'

$word = New-Object -ComObject Word.Application
$word.Visible = $false
$word.DisplayAlerts = 0
$document = $null
try {
    $document = $word.Documents.Open($docxPath, $false, $false)
    Write-Output 'Opened Word document.'
    if ($document.Sections.Count -eq 1) {
        foreach ($heading in @('Chapter 1: Introduction', 'Contents')) {
            $paragraph = $null
            foreach ($candidate in $document.Paragraphs) {
                if ($candidate.Range.Text.Trim() -eq $heading) {
                    $paragraph = $candidate
                    break
                }
            }
            if ($null -eq $paragraph) { throw "Missing heading: $heading" }
            $point = $document.Range($paragraph.Range.Start, $paragraph.Range.Start)
            $point.InsertBreak(2) # wdSectionBreakNextPage
            Write-Output "Inserted section break before $heading."
        }
    }

    if ($document.Sections.Count -ne 3) {
        throw "Expected title, front matter and main-body sections; found $($document.Sections.Count)."
    }

    $frontFooter = $document.Sections.Item(2).Footers.Item(1)
    $frontFooter.LinkToPrevious = $false
    $frontPages = $frontFooter.PageNumbers
    $null = $frontPages.Add(1, $true) # centred page numbers
    $frontPages.NumberStyle = 2 # lowercase Roman
    $frontPages.RestartNumberingAtSection = $true
    $frontPages.StartingNumber = 1
    Write-Output 'Set front matter page numbers.'

    $bodyFooter = $document.Sections.Item(3).Footers.Item(1)
    $bodyFooter.LinkToPrevious = $false
    $bodyPages = $bodyFooter.PageNumbers
    $null = $bodyPages.Add(1, $true)
    $bodyPages.NumberStyle = 0 # Arabic
    $bodyPages.RestartNumberingAtSection = $true
    $bodyPages.StartingNumber = 1
    Write-Output 'Set body page numbers.'

    $document.Repaginate()
    Write-Output 'Repaginated.'
    $null = $document.Fields.Update()
    Write-Output 'Updated fields.'
    Write-Output 'Saving Word document.'
    $document.Save()
    Write-Output "Finalised $docxPath ($($document.ComputeStatistics(2)) pages)"
}
finally {
    if ($null -ne $document) { $document.Close(0) }
    $word.Quit()
}
