---
title: Add Headers and Footers of PDF File
type: docs
weight: 20
url: /net/add-headers-and-footers-of-pdf-file/
description: Aspose.PDF allows you to add headers and footers to your PDF file using TextStamp class.
lastmod: "2020-12-16"
---

## Adding Text in Header of PDF File

You can use [TextStamp](https://apireference.aspose.com/pdf/net/aspose.pdf/textstamp) class to add text in the header of a PDF file. TextStamp class provides properties necessary to create a text based stamp like font size, font style, and font color etc. In order to add text in the header, you need to create a Document object and a TextStamp object using required properties. After that, you can call AddStamp method of the Page to add the text in the header of the PDF.

You need to set the TopMargin property in such a way that it adjusts the text in the header area of your PDF. You also need to set HorizontalAlignment to Center and VerticalAlignment to Top. The following code snippet shows you how to add text in the header of a PDF file.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

// Open document
Document pdfDocument = new Document(dataDir+ "TextinHeader.pdf");

// Create header
TextStamp textStamp = new TextStamp("Header Text");
// Set properties of the stamp
textStamp.TopMargin = 10;
textStamp.HorizontalAlignment = HorizontalAlignment.Center;
textStamp.VerticalAlignment = VerticalAlignment.Top;
// Add header on all pages
foreach (Page page in pdfDocument.Pages)
{
    page.AddStamp(textStamp);
}

// Save updated document
pdfDocument.Save(dataDir+ "TextinHeader_out.pdf");
```

## Adding Text in Footer of PDF File

You can use TextStamp class to add text in the footer of a PDF file. TextStamp class provides properties necessary to create a text based stamp like font size, font style, and font color etc. In order to add text in the footer, you need to create a Document object and a TextStamp object using required properties. After that, you can call AddStamp method of the Page to add the text in the footer of the PDF.

{{% alert color="primary" %}}

You need to set the Bottom Margin property in such a way that it adjusts the text in the footer area of your PDF. You also need to set HorizontalAlignment to Center and VerticalAlignment to Bottom 

{{% /alert %}}

The following code snippet shows you how to add text in the footer of a PDF file.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

// Open document
Document pdfDocument = new Document(dataDir+ "TextinFooter.pdf");
// Create footer
TextStamp textStamp = new TextStamp("Footer Text");
// Set properties of the stamp
textStamp.BottomMargin = 10;
textStamp.HorizontalAlignment = HorizontalAlignment.Center;
textStamp.VerticalAlignment = VerticalAlignment.Bottom;
// Add footer on all pages
foreach (Page page in pdfDocument.Pages)
{
    page.AddStamp(textStamp);
}
dataDir = dataDir + "TextinFooter_out.pdf";
// Save updated PDF file
pdfDocument.Save(dataDir);
```

## Adding Image in Header of PDF File

You can use [ImageStamp](https://apireference.aspose.com/pdf/net/aspose.pdf/ImageStamp) class to add image in the header of a PDF file. Image Stamp class provides properties necessary to create image based stamp like font size, font style, and font color etc. In order to add image in the header, you need to create a Document object and a Image Stamp object using required properties. After that, you can call [AddStamp](https://apireference.aspose.com/pdf/net/aspose.pdf/page/methods/addstamp) method of the Page to add the image in the header of the PDF.

{{% alert color="primary" %}}

You need to set the TopMargin property in such a way that it adjusts the image in the header area of your PDF. You also need to set HorizontalAlignment to Center and VerticalAlignment to Top .

{{% /alert %}}

The following code snippet shows you how to add image in the header of a PDF file.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

// Open document
Document pdfDocument = new Document(dataDir+ "ImageinHeader.pdf");

// Create header
ImageStamp imageStamp = new ImageStamp(dataDir+ "aspose-logo.jpg");
// Set properties of the stamp
imageStamp.TopMargin = 10;
imageStamp.HorizontalAlignment = HorizontalAlignment.Center;
imageStamp.VerticalAlignment = VerticalAlignment.Top;
// Add header on all pages
foreach (Page page in pdfDocument.Pages)
{
    page.AddStamp(imageStamp);
}
dataDir = dataDir + "ImageinHeader_out.pdf";
// Save updated document
pdfDocument.Save(dataDir);
```

## Adding Image in Footer of PDF File

You can use Image Stamp class to add image in the footer of a PDF file. Image Stamp class provides properties necessary to create image based stamp like font size, font style, and font color etc. In order to add image in the footer, you need to create a Document object and an Image Stamp object using required properties. After that, you can call AddStamp method of the Page to add the image in the footer of the PDF.

{{% alert color="primary" %}}

You need to set the [BottomMargin](https://apireference.aspose.com/pdf/net/aspose.pdf/stamp/properties/bottommargin) property in such a way that it adjusts the image in the footer area of your PDF. You also need to set [HorizontalAlignment](https://apireference.aspose.com/pdf/net/aspose.pdf/stamp/properties/horizontalalignment) to `Center` and [VerticalAlignment](https://apireference.aspose.com/pdf/net/aspose.pdf/stamp/properties/verticalalignment) to `Bottom`.

{{% /alert %}}

The following code snippet shows you how to add image in the footer of a PDF file.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

// Open document
Document pdfDocument = new Document(dataDir+ "ImageInFooter.pdf");
// Create footer
ImageStamp imageStamp = new ImageStamp(dataDir+ "aspose-logo.jpg");
// Set properties of the stamp
imageStamp.BottomMargin = 10;
imageStamp.HorizontalAlignment = HorizontalAlignment.Center;
imageStamp.VerticalAlignment = VerticalAlignment.Bottom;
// Add footer on all pages
foreach (Page page in pdfDocument.Pages)
{
    page.AddStamp(imageStamp);
}
dataDir = dataDir + "ImageInFooter_out.pdf";
// Save updated PDF file
pdfDocument.Save(dataDir);
```

## Adding different Headers in one PDF File

We know that we can add TextStamp in Header/Footer section of the document by using TopMargin or Bottom Margin properties, but sometimes we may have the requirement to add multiple header/footers in a single PDF document. In order to accomplish this requirement, we will create individual TextStamp objects (number of objects depends upon the number of Header/Footers required)and will add them to PDF document. We may also specify different formatting information for individual stamp object. In following example, we have created Document object and three TextStamp objects and then we have used [AddStamp](https://apireference.aspose.com/pdf/net/aspose.pdf/page/methods/addstamp) method of the Page to add the text in the header section of the PDF. The following code snippet shows you how to add image in the footer of a PDF file.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

// Open source document
Aspose.Pdf.Document doc = new Aspose.Pdf.Document(dataDir+ "AddingDifferentHeaders.pdf");

// Create three stamps
Aspose.Pdf.TextStamp stamp1 = new Aspose.Pdf.TextStamp("Header 1");
Aspose.Pdf.TextStamp stamp2 = new Aspose.Pdf.TextStamp("Header 2");
Aspose.Pdf.TextStamp stamp3 = new Aspose.Pdf.TextStamp("Header 3");

// Set stamp alignment (place stamp on page top, centered horiznotally)
stamp1.VerticalAlignment = Aspose.Pdf.VerticalAlignment.Top;
stamp1.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Center;
// Specify the font style as Bold
stamp1.TextState.FontStyle = FontStyles.Bold;
// Set the text fore ground color information as red
stamp1.TextState.ForegroundColor = Color.Red;
// Specify the font size as 14
stamp1.TextState.FontSize = 14;

// Now we need to set the vertical alignment of 2nd stamp object as Top
stamp2.VerticalAlignment = Aspose.Pdf.VerticalAlignment.Top;
// Set Horizontal alignment information for stamp as Center aligned
stamp2.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Center;
// Set the zooming factor for stamp object
stamp2.Zoom = 10;

// Set the formatting of 3rd stamp object
// Specify the Vertical alignment information for stamp object as TOP
stamp3.VerticalAlignment = Aspose.Pdf.VerticalAlignment.Top;
// Set the Horizontal alignment inforamtion for stamp object as Center aligned
stamp3.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Center;
// Set the rotation angle for stamp object
stamp3.RotateAngle = 35;
// Set pink as background color for stamp
stamp3.TextState.BackgroundColor = Color.Pink;
// Change the font face information for stamp to Verdana
stamp3.TextState.Font = FontRepository.FindFont("Verdana");
// First stamp is added on first page;
doc.Pages[1].AddStamp(stamp1);
// Second stamp is added on second page;
doc.Pages[2].AddStamp(stamp2);
// Third stamp is added on third page.
doc.Pages[3].AddStamp(stamp3);
dataDir = dataDir + "multiheader_out.pdf";
// Save the updated document
doc.Save(dataDir);
```
