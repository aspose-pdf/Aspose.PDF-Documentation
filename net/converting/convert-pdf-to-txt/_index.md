---
title: Convert PDF to text using C#
linktitle: Convert PDF to text
type: docs
weight: 120
url: /net/convert-pdf-to-txt/
lastmod: "2021-06-05"
description: With Aspose.PDF for .NET you can convert a whole PDF document to a text file or convert only a PDF page to a text file.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

**Aspose.PDF for .NET** support converting whole PDF document and single page to a Text file.

## Convert whole PDF document to Text file

You can convert PDF document to TXT file using [Visit](https://apireference.aspose.com/pdf/net/aspose.pdf.text/textabsorber/methods/visit/index) method of [TextAbsorber](https://apireference.aspose.com/pdf/net/aspose.pdf.text/textabsorber) class.

The following code snippet explains how to extract the texts from the all pages.

```csharp
public static void ConvertPDFDocToTXT()
{
    // Open document
    Document pdfDocument = new Document(_dataDir + "demo.pdf");
    TextAbsorber ta = new TextAbsorber();
    ta.Visit(pdfDocument);
    // Save the extracted text in text file
    File.WriteAllText(_dataDir + "input_Text_Extracted_out.txt",ta.Text);
}
```

## Live Example

Aspose.PDF for .NET presents you online free application ["PDF to Text"](https://products.aspose.app/pdf/conversion/pdf-to-txt), where you may try to investigate the functionality and quality it works.

[![Convert PDF to Text file](pdf_to_text.png)](https://products.aspose.app/pdf/conversion/pdf-to-txt)

## Convert PDF page to text file

You can convert PDF document to TXT file with Aspose.PDF for .NET. You should use `Visit` method of `TextAbsorber` class for resolve this task.

The following code snippet explains how to extract the texts from the particular pages.

```csharp
public static void ConvertPDFPagestoTXT()
{
    Document pdfDocument = new Document(System.IO.Path.Combine(_dataDir, "demo.pdf"));
    TextAbsorber ta = new TextAbsorber();
    var pages = new [] {1, 3, 4};
    foreach (var page in pages)
    {
        ta.Visit(pdfDocument.Pages[page]);
    }
   
    // Save the extracted text in text file
    File.WriteAllText(System.IO.Path.Combine(_dataDir, "input_Text_Extracted_out.txt"), ta.Text);
}
```
