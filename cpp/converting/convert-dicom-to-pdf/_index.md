---
title: Convert DICOM to PDF | C#
linktitle: Convert DICOM to PDF
type: docs
weight: 250
url: /net/convert-dicom-to-pdf/
lastmod: "2021-06-05"
description: Convert medical images saved in DICOM format to a PDF file using Aspose.PDF for .NET.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

<abbr title="Digital Imaging and Communications in Medicine">DICOM</abbr> format is the medical industry standard for the creation, storage, transmission, and visualization of digital medical images and documents of examined patients.

**Aspsoe.PDF for .NET** allows you to convert DICOM and SVG images, but for technical reasons to add images you need to specify the type of file to be added to PDF:

1. Create an object of the Image class.
1. Add the image to a page's Paragraphs collection.
1. Specify the [FileType](https://apireference.aspose.com/pdf/net/aspose.pdf/image/properties/filetype) property.
1. Specify the file's path or source.
    - If an image is at a location on the hard drive, specify the path location using the Image.File property.
    - If an image is placed in a MemoryStream, pass the object holding the image to the Image.ImageStream property.

The following code snippet shows how to convert DICOM files to PDF  format with Aspose.PDF. You should load DICOM image, place the image on a page in a PDF file and save the output as PDF.

```csharp
private const string _dataDir = "..\\..\\..\\..\\Samples";
// Convert DICOM images to PDF using Image class
public static void ConvertDICOMtoPDF()
{
    // Instantiate Document Object
    Document pdfDocument = new Document();

    // Add a page to pages collection of document
    Page page = pdfDocument.Pages.Add();

    Image image = new Image
    {
        FileType = ImageFileType.Dicom,
        File = System.IO.Path.Combine(_dataDir,"bmode.dcm")
    };
    pdfDocument.Pages[1].Paragraphs.Add(image);
    // Save output as PDF format
    pdfDocument.Save(System.IO.Path.Combine(_dataDir,"PDFWithDicomImage_out.pdf"));
}
```
