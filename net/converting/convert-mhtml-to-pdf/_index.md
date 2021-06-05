---
title: Convert MHTML to PDF | C#
linktitle: Convert MHTML to PDF
type: docs
weight: 290
url: /net/convert-mhtml-to-pdf/
lastmod: "2021-06-05"
description: This article describes how to convert MHT or MHTML files to PDF format programmatically with C# and Aspose.PDF for .NET.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Live Example

Aspose.PDF for .NET presents you online free application ["MHTML to PDF"](https://products.aspose.app/pdf/conversion/mhtml-to-pdf), where you may try to investigate the functionality and quality it works.

[![MHTML to PDF](mhtml.png)](https://products.aspose.app/pdf/conversion/mhtml-to-pdf)

<abbr title="MIME encapsulation of aggregate HTML documents">MHTML</abbr>, short for MIME HTML, is a web page archive format used to combine resources that are typically represented by external links (such as images, Flash animations, Java applets, and audio files) with HTML code into a single file. The content of an MHTML file is encoded as if it were an HTML email message, using the MIME type multipart/related. Aspose.PDF for .NET can convert HTML files to PDF format and with the release of Aspose.PDF for .NET 9.0.0, we have introduced a new feature that lets you convert MHTML files to PDF format.
Next code snippet show how to covert MHTML files to PDF format with C#:

```csharp
public static void ConvertMHTtoPDF()
{
    MhtLoadOptions options = new MhtLoadOptions()
    {
        PageInfo = { Width = 842, Height = 1191, IsLandscape = true}
    };
    Document pdfDocument= new Document(_dataDir + "fileformatinfo.mht", options);
    pdfDocument.Save(_dataDir + "mhtml_test.PDF");
}
```
