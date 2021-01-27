---
title: Support for DICOM Images
linktitle: Support for DICOM Images
type: docs
weight: 10
url: /net/support-for-dicom-mages/
description: This section describes how to support for DICOM images in PDF file using C# library.
lastmod: "2021-01-27"
---

**Aspose.PDF for .NET** supports functionality to add DICOM images to PDF documents. The following code snippet shows how to use this functionality.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Images();

using (Document pdfDocument = new Document())
{
    pdfDocument.Pages.Add();
    Aspose.Pdf.Image image = new Aspose.Pdf.Image();
    image.FileType = ImageFileType.Dicom;
    image.ImageStream = new FileStream(dataDir + "0002.dcm", FileMode.Open, FileAccess.Read);
    pdfDocument.Pages[1].Paragraphs.Add(image);
    // Save output as PDF format
    pdfDocument.Save(dataDir + "PdfWithDicomImage_out.pdf");
}
```

