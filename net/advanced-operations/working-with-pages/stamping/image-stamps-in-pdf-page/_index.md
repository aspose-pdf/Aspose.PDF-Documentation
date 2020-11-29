---
title:  Image stamps in PDF page
type: docs
weight: 10
url: /net/image-stamps-in-pdf-page/
description: Add the Image Stamp in your PDF document using ImageStamp class with the Aspose.PDF library.
---

## Adding Image Stamp in PDF File

You can use the ImageStamp class to add an image stamp to a PDF file. The ImageStamp class provides the properties necessary for creating an image-based stamp, such as height, width, opacity and so on.

To add an image stamp:

1. Create a Document object and an ImageStamp object using required properties.
1. Call the Page class’ AddStamp method to add the stamp to the PDF.
The following code snippet shows how to add image stamp in the PDF file.
```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

// Open document
Document pdfDocument = new Document(dataDir+ "AddImageStamp.pdf");

// Create image stamp
ImageStamp imageStamp = new ImageStamp(dataDir + "aspose-logo.jpg");
imageStamp.Background = true;
imageStamp.XIndent = 100;
imageStamp.YIndent = 100;
imageStamp.Height = 300;
imageStamp.Width = 300;
imageStamp.Rotate = Rotation.on270;
imageStamp.Opacity = 0.5;
// Add stamp to particular page
pdfDocument.Pages[1].AddStamp(imageStamp);

dataDir = dataDir + "AddImageStamp_out.pdf";
// Save output document
pdfDocument.Save(dataDir);
```
## Control Image Quality when Adding a Stamp

When adding an image as a stamp object, you can control the quality of the image. The Quality property of the ImageStamp class is used for this purpose. It indicates the quality of image in percents (valid values are 0..100).
```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

// Open document
Document pdfDocument = new Document(dataDir+ "AddImageStamp.pdf");

// Create image stamp
ImageStamp imageStamp = new ImageStamp(dataDir + "aspose-logo.jpg");

imageStamp.Quality = 10;
pdfDocument.Pages[1].AddStamp(imageStamp);
pdfDocument.Save(dataDir + "ControlImageQuality_out.pdf");
```
## Image Stamp as Background in Floating Box

Aspose.PDF API lets you add image stamp as background in a floating box. The BackgroundImage property of FloatingBox class can be used to set the background image stamp for a floating box as shown in following code sample.
```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

// Instantiate Document object
Document doc = new Document();
// Add page to PDF document
Page page = doc.Pages.Add();
// Create FloatingBox object
FloatingBox aBox = new FloatingBox(200, 100);
// Set left position for FloatingBox
aBox.Left = 40;
// Set Top position for FloatingBox
aBox.Top = 80;
// Set the Horizontal alignment for FloatingBox
aBox.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Center;
// Add text fragment to paragraphs collection of FloatingBox
aBox.Paragraphs.Add(new TextFragment("main text"));
// Set border for FloatingBox
aBox.Border = new BorderInfo(BorderSide.All, Aspose.Pdf.Color.Red);
// Add background image
aBox.BackgroundImage = new Image
{
    File = dataDir + "aspose-logo.jpg"
};
// Set background color for FloatingBox
aBox.BackgroundColor = Aspose.Pdf.Color.Yellow;
// Add FloatingBox to paragraphs collection of page object
page.Paragraphs.Add(aBox);
// Save the PDF document
doc.Save(dataDir + "AddImageStampAsBackgroundInFloatingBox_out.pdf");
```


