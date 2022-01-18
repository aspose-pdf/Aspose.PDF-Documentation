---
title: Set Default Font Name
linktitle: Set Default Font Name
type: docs
weight: 90
url: /net/set-default-font-name/
description: This section describes how to set default font name using Aspose.PDF for .NET library.
lastmod: "2021-06-05"
---

**Aspose.PDF for .NET** API allows you to set a default font name when a font is not available in the document. You can use DefaultFontName property of RenderingOptions class to set the default font name. In case DefaultFontName is set to null the **Times New Roman** font will be used. The following code snippet shows how to set a default font name when saving PDF into an image:

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

using (Document pdfDocument = new Document(dataDir + "input.pdf"))
{
    using (FileStream imageStream = new FileStream(dataDir + "SetDefaultFontName.png", FileMode.Create))
    {
        Resolution resolution = new Resolution(300);
        PngDevice pngDevice = new PngDevice(resolution);
        RenderingOptions ro = new RenderingOptions();
        ro.DefaultFontName = "Arial";
        pngDevice.RenderingOptions = ro;
        pngDevice.Process(pdfDocument.Pages[1], imageStream);
    }
}
```
