---
title: Set Image Size
linktitle: Set Image Size
type: docs
weight: 80
url: /net/set-image-size/
description: This section describes how to set image size PDF file using C# library.
lastmod: "2021-06-05"
---

It is possible to set the size of an image that’s being added to a PDF file. In order to set size, you can use FixWidth and FixHeight properties of Aspose.Pdf.Image Class. The following code snippet demonstrates how to set the size of an image:

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Images();
// Instantiate Document object
Document doc = new Document();
// add page to pages collection of PDF file
Aspose.Pdf.Page page = doc.Pages.Add();
// Create an image instance
Aspose.Pdf.Image img = new Aspose.Pdf.Image();
// Set Image Width and Height in Points
img.FixWidth = 100;
img.FixHeight = 100;
// Set image type as SVG
img.FileType = Aspose.Pdf.ImageFileType.Unknown;
// Path for source file
img.File = dataDir + "aspose-logo.jpg";
page.Paragraphs.Add(img);
//Set page properties
page.PageInfo.Width = 800;
page.PageInfo.Height = 800;
dataDir = dataDir + "SetImageSize_out.pdf";
// save resultant PDF file
doc.Save(dataDir);
```
