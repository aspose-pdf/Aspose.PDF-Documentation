---
title: Convert PostScript to PDF using C#
linktitle: Convert PostScript to PDF
type: docs
weight: 370
url: /net/convert-postscript-to-pdf/
lastmod: "2021-06-05"
description: Conversion PostScript to PDF format is possible with C# library. Aspose.PDF allows you to use PsLoadOptions class for this task.
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

**Aspose.PDF for .NET** support features converting PostScript files to PDF format. One of the features from Aspose.PDF is that you can set a set of font folders to be used during conversion.

In order to convert a PostScript file to PDF format, Aspose.PDF for .NET offers [PsLoadOptions](https://apireference.aspose.com/pdf/net/aspose.pdf/psloadoptions) class which is used to initialize the LoadOptions object. Later this object can be passed as an argument to Document object constructor, which will help PDF Rendering Engine to determine the format of source document.

Following code snippet can be used to convert a PostScript file into PDF format with Aspose.PDF for .NET:

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string _dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();
// Create a new instance of PsLoadOptions
PsLoadOptions options = new PsLoadOptions();
// Open .ps document with created load options
Document pdfDocument = new Document(_dataDir + "input.ps", options);
// Save document
pdfDocument.Save(dataDir + "PSToPDF.pdf");
```

Additionally, you can set a set of font folders that will be used during conversion:

```csharp
public static void ConvertPostscriptToPDFAvdanced()
{
    PsLoadOptions options = new PsLoadOptions
    {
        FontsFolders = new [] { @"c:\tmp\fonts1", @"c:\tmp\fonts2"}
    };
    Document pdfDocument = new Document(_dataDir + "input.ps", options);
    pdfDocument.Save(_dataDir + "ps_test.pdf");
}
```
