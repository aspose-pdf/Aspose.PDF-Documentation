---
title: Convert PDF/A to PDF format using C#
linktitle: Convert PDF/A to PDF format
type: docs
weight: 90
url: /net/convert-pdfa-to-pdf/
lastmod: "2021-10-18"
description: This topic show you how to Aspose.PDF allows to convert a PDF file to a PDF/A compliant PDF file. 
sitemap:
    changefreq: "weekly"
    priority: 0.8
---

## Convert PDF/A document to PDF

Convert PDF/A document to PDF means removing <abbr title="Portable Document Format Archive
">PDF/A</abbr> restriction from the original document. Class [Document](https://apireference.aspose.com/pdf/net/aspose.pdf/document) has method [RemovePdfaCompliance(..)](https://apireference.aspose.com/pdf/net/aspose.pdf/document/methods/removepdfacompliance) to remove
the PDF compliance information from input/source file.

```csharp
public static void ConvertPDFAtoPDF()
{
    // For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
    Document pdfDocument = new Document(_dataDir + "PDFAToPDF.pdf");
    // Remove PDF/A compliance information
    pdfDocument.RemovePdfaCompliance();
    // Save updated document
    pdfDocument.Save(_dataDir + "PDFAToPDF_out.pdf");
}
```

This info also removes if you make any changes in the document (e.g. add pages). In the following example, the output document loses PDF/A compliance after the page adding.

```csharp
public static void ConvertPDFAtoPDFAdvanced()
{
    // For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
    Document pdfDocument = new Document(_dataDir + "PDFAToPDF.pdf");
    // Adding a new (empty) page removes PDF/A compliance information.
    pdfDocument.Pages.Add();
    // Save updated document
    pdfDocument.Save(_dataDir + "PDFAToPDF_out.pdf");
}
```
