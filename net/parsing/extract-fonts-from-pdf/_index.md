---
title: Extract fonts from PDF C#
linktitle: Extract fonts from PDF
type: docs
weight: 30
url: /net/extract-fonts-from-pdf/
description: Use the Aspose.PDF for. NET library to extract all embedded fonts from your PDF document.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

In case you want to get all fonts from a PDF document, you can use FontUtilities.GetAllFonts() method provided in Document class. Please check following code snippet in order to get all fonts from an existing PDF document:

The next code snippet also works with a new graphical [Aspose.Drawing](/pdf/net/drawing/) interface.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
Document doc = new Document(dataDir + "input.pdf");
Aspose.Pdf.Text.Font[] fonts = doc.FontUtilities.GetAllFonts();
foreach (Aspose.Pdf.Text.Font font in fonts)
{
    Console.WriteLine(font.FontName);
}
```
