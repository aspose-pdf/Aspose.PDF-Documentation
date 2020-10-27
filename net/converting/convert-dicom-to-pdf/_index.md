---
title: Convert DICOM to PDF
type: docs
weight: 80
url: /net/convert-dicom-to-pdf/
---
# Convert DICOM or SVG images to PDF using Image class

Aspsoe.PDF for .NET allows you to convert DICOM and SVG images, but for technical reasons to add images you need to specify the type of file to be added to PDF:

1. Create an object of the Image class.
1. Add the image to a page's Paragraphs collection.
1. Specify the `FileType` property.
1. Specify the file's path or source.
    - If an image is at a location on the hard drive, specify the path location using the Image.File property.
    - If an image is placed in a MemoryStream, pass the object holding the image to the Image.ImageStream property.

The following code snippet shows how to load DICOM image, place the image on a page in a PDF file and save the output as PDF.
```
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-Java
String dataDir = com.aspose.pdf.examples.Utils.getSharedDataDir(AddImage.class) + "Images/";
// Load image into stream
java.io.FileInputStream imageStream = new java.io.FileInputStream(new java.io.File(dataDir + "0002.dcm"));
		
Document pdfDocument = new Document();
pdfDocument.getPages().add();
   com.aspose.pdf.Image image = new com.aspose.pdf.Image();
   image.setFileType(ImageFileType.Dicom);
   image.setImageStream(imageStream);
   pdfDocument.getPages().get_Item(1).getParagraphs().add(image);
   // Save output as PDF format
   pdfDocument.save(dataDir + "PdfWithDicomImage_out.pdf");
   ```