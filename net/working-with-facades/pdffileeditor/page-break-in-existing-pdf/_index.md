---
title: Page Break in existing PDF
type: docs
weight: 30
url: /net/page-break-in-existing-pdf/
description: This section explains how to break pages in an existing PDF using PdfFileEditor class.
lastmod: "2021-01-18"
draft: false
---

As a default layout, the contents inside PDF files are added in Top-Left to Bottom-Right layout. Once the contents exceed beyond page bottom margin, the page break occurs. However you may come across a requirement to insert page break depending upon requirement. A method named AddPageBreak(...) method is added in [PdfFileEditor](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) class to accomplish this requirement.

1. [public void AddPageBreak(Document src, Document dest, PageBreak[] pageBreaks)](https://apireference.aspose.com/pdf/net/aspose.pdf.facades.pdffileeditor/addpagebreak/methods/1)
1. [public void AddPageBreak(string src, string dest, PageBreak[] pageBreaks)](https://apireference.aspose.com/pdf/net/aspose.pdf.facades.pdffileeditor/addpagebreak/methods/2)
1. [public void AddPageBreak(Stream src, Stream dest, PageBreak[] pageBreaks)](https://apireference.aspose.com/pdf/net/aspose.pdf.facades.pdffileeditor/addpagebreak/methods/3)

- src is source document/path to document/stream with source document
- dest is destination document/path where document will be saved/stream where document will be saved
- PageBreak is array of page break objects. It have two properties: index of page where page break must be placed and vertical position of the page break on the page.

## Example 1 (Add page break )

```csharp
public static void PageBrakeExample01()
{
    // Instantiate Document instance
    Document doc = new Document(_dataDir + "Sample-Document-01.pdf");
    // Instantiate blank Document instance
    Document dest = new Document();
    // Create PdfFileEditor object
    PdfFileEditor fileEditor = new PdfFileEditor();
    fileEditor.AddPageBreak(doc, dest, new PdfFileEditor.PageBreak[]
    {
        new PdfFileEditor.PageBreak(1, 450)
    });
    // Save resultant file
    dest.Save(_dataDir + "PageBreak_out.pdf");
}
```

## Example 2

```csharp
public static void PageBrakeExample02()
{
    // Create PdfFileEditor object
    PdfFileEditor fileEditor = new PdfFileEditor();

    fileEditor.AddPageBreak(_dataDir + "Sample-Document-02.pdf",
        _dataDir + "PageBreakWithDestPath_out.pdf",
        new PdfFileEditor.PageBreak[]
        {
            new PdfFileEditor.PageBreak(1, 450)
        });
}
```

## Example 3

```csharp
public static void PageBrakeExample03()
{
    Stream src = new FileStream(_dataDir + "Sample-Document-03.pdf", FileMode.Open, FileAccess.Read);
    Stream dest = new FileStream(_dataDir + "PageBreakWithStream_out.pdf", FileMode.Create, FileAccess.ReadWrite);
    PdfFileEditor fileEditor = new PdfFileEditor();
    fileEditor.AddPageBreak(src, dest,
        new PdfFileEditor.PageBreak[]
        {
            new PdfFileEditor.PageBreak(1, 450)
        });
    dest.Close();
    src.Close();
}
```
