---
title: Convert CGM to PDF | C#
linktitle: Convert CGM to PDF
type: docs
weight: 260
url: /net/convert-cgm-to-pdf/
description: Convert CGM files to PDF documents with Aspose.PDF library. These files used in CAD and presentation graphics applications
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

<abbr title="Computer Graphics Metafile">CGM</abbr> is a file extension for a Computer Graphics Metafile format commonly used in CAD (computer-aided design) and presentation graphics applications. CGM is a vector graphics format that supports three different encoding methods: binary (best for program read speed), character-based (produces the smallest file size and allows for faster data transfers) or cleartext encoding (allows users to read and modify the file with a text editor).

Check next code snippet for converting CGM files  to PDF format.

1. Create an instance of [CgmLoadOptions](https://apireference.aspose.com/pdf/net/aspose.pdf/cgmloadoptions) class.
1. Create an instance of [Document](https://apireference.aspose.com/pdf/net/aspose.pdf/document) class with mention source filename and options.
1. Save the document with the desired file name.

```csharp
public static void ConvertCGMtoPDF()
{
    CgmLoadOptions option = new CgmLoadOptions();
    Document pdfDocument= new Document(_dataDir+"corvette.cgm", option);
    pdfDocument.Save(_dataDir+"CGMtoPDF.pdf");
}
```
