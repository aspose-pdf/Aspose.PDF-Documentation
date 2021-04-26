---
title: Add Image to PDF | C#
linktitle: Add Image
type: docs
weight: 10
url: /net/add-image-to-existing-pdf-file/
description: This section describes how to add image to existing PDF file PDF file using C# library.
lastmod: "2021-02-26"
---

## Add Image in an Existing PDF File

Every PDF page contains Resources and Contents properties. Resources can be images and forms for example, while content is represented by a set of PDF operators. Each operator has its name and argument. This example uses operators to add an image to a PDF file.

To add an image to an existing PDF file:

- Create a Document object and open the input PDF document.
- Get the page you want to add an image to.
- Add the image into the page’s Resources collection.
- Use operators to place the image on the page:
- Use the GSave operator to save the current graphical state.
- Use ConcatenateMatrix operator to specify where the image is to be placed.
- Use the Do operator to draw the image on the page.
- Finally, use GRestore operator to save the updated graphical state.
- Save the file.
The following code snippet shows how to add the image in a PDF document.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Images();

// Open document
Document pdfDocument = new Document(dataDir+ "AddImage.pdf");

// Set coordinates
int lowerLeftX = 100;
int lowerLeftY = 100;
int upperRightX = 200;
int upperRightY = 200;

// Get the page where image needs to be added
Page page = pdfDocument.Pages[1];
// Load image into stream
FileStream imageStream = new FileStream(dataDir + "aspose-logo.jpg", FileMode.Open);
// Add image to Images collection of Page Resources
page.Resources.Images.Add(imageStream);
// Using GSave operator: this operator saves current graphics state
page.Contents.Add(new Aspose.Pdf.Operators.GSave());
// Create Rectangle and Matrix objects
Aspose.Pdf.Rectangle rectangle = new Aspose.Pdf.Rectangle(lowerLeftX, lowerLeftY, upperRightX, upperRightY);
Matrix matrix = new Matrix(new double[] { rectangle.URX - rectangle.LLX, 0, 0, rectangle.URY - rectangle.LLY, rectangle.LLX, rectangle.LLY });
// Using ConcatenateMatrix (concatenate matrix) operator: defines how image must be placed
page.Contents.Add(new Aspose.Pdf.Operators.ConcatenateMatrix(matrix));
XImage ximage = page.Resources.Images[page.Resources.Images.Count];
// Using Do operator: this operator draws image
page.Contents.Add(new Aspose.Pdf.Operators.Do(ximage.Name));
// Using GRestore operator: this operator restores graphics state
page.Contents.Add(new Aspose.Pdf.Operators.GRestore());
dataDir = dataDir + "AddImage_out.pdf";
// Save updated document
pdfDocument.Save(dataDir);
```

{{% alert color="primary" %}}

By default, the JPEG quality is set to 100%. To apply better compression and quality, use the following overloads:

{{% /alert %}}

- the Replace method overload is added into the XImageCollection class: public void Replace(int index, Stream stream, int quality)
- the Add method overload is added into the XImageCollection class: public void Add(Stam stream, int quality)

## Add Image in an Existing PDF File (Facades)

There is also an alternative, easier way to add a Image to a PDF file. You can use [AddImage](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend/methods/addimage/index) method of the [PdfFileMend](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend) class. The [AddImage](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend/methods/addimage/index) method requires the image to be added, the page number at which the image needs to be added and the coordinate information. After that, save the updated PDF file using Close method. The following code snippet shows you how to add image in an existing PDF file.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdfFacades_Images();

// Open document
PdfFileMend mender = new PdfFileMend();

// Create PdfFileMend object to add text
mender.BindPdf(dataDir + "AddImage.pdf");

// Add image in the PDF file
mender.AddImage(dataDir+ "aspose-logo.jpg", 1, 100, 600, 200, 700);

// Save changes
mender.Save(dataDir + "AddImage_out.pdf");

// Close PdfFileMend object
mender.Close();
```

## Add Reference of a single Image multiple times in a PDF Document

Sometimes we have a requirement to use same image multiple times in a PDF document. Adding a new instance increases the resultant PDF document. We have added a new method XImageCollection.Add(XImage) in Aspose.PDF for .NET 17.1.0. This method allows to add reference to the same PDF object as original image that optimize the PDF Document size.

```csharp
 Aspose.PDF.Rectangle imageRectangle = new Aspose.PDF.Rectangle(0, 0, 30, 15);

using (Aspose.PDF.Document document = new Aspose.PDF.Document("input.pdf"))
{
    using (var imageStream = File.Open("icon.png", FileMode.Open))
    {
        XImage image = null;
        foreach (Page page in document.Pages)
        {
            WatermarkAnnotation annotation = new WatermarkAnnotation(page, page.Rect);
            XForm form = annotation.Appearance["N"];
            form.BBox = page.Rect;
            string name;
            if (image == null)
            {
                name = form.Resources.Images.Add(imageStream);
                image = form.Resources.Images[name];
            }
            else
            {
                name = form.Resources.Images.Add(image);
            }
            form.Contents.Add(new Operator.GSave());
            form.Contents.Add(new Operator.ConcatenateMatrix(new Aspose.PDF.Matrix(imageRectangle.Width, 0, 0, imageRectangle.Height, 0, 0)));
            form.Contents.Add(new Operator.Do(name));
            form.Contents.Add(new Operator.GRestore());
            page.Annotations.Add(annotation, false);
            imageRectangle = new Aspose.PDF.Rectangle(0, 0, imageRectangle.Width * 1.01, imageRectangle.Height * 1.01);
        }
    }
    document.Save("output.pdf");
}
```

## Identify if image inside PDF is Colored or Black & White

Different type of compression can be applied over images to reduce their size. The type of compression being applied over image depends upon the ColorSpace of source image i.e. if image is Color (RGB), then apply JPEG2000 compression, and if it is Black & White, then JBIG2/JBIG2000 compression should be applied. Therefore identifying each image type and using an appropriate type of compression will create best/optimized output.

A PDF file may contain Text, Image, Graph, Attachment, Annotation etc elements and if the source PDF file contains images, we can determine image Color space and apply appropriate compression for image to reduce PDF file size. The following code snippet shows the steps to Identify if image inside PDF is Colored or Black & White.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Images();

// Counter for grayscale images
int grayscaled = 0;
// Counter for RGB images
int rgd = 0;

using (Document document = new Document(dataDir + "ExtractImages.pdf"))
{
    foreach (Page page in document.Pages)
    {
        Console.WriteLine("--------------------------------");
        ImagePlacementAbsorber abs = new ImagePlacementAbsorber();
        page.Accept(abs);
        // Get the count of images over specific page
        Console.WriteLine("Total Images = {0} over page number {1}", abs.ImagePlacements.Count, page.Number);
        // Document.Pages[29].Accept(abs);
        int image_counter = 1;
        foreach (ImagePlacement ia in abs.ImagePlacements)
        {
            ColorType colorType = ia.Image.GetColorType();
            switch (colorType)
            {
                case ColorType.Grayscale:
                    ++grayscaled;
                    Console.WriteLine("Image {0} is GrayScale...", image_counter);
                    break;
                case ColorType.Rgb:
                    ++rgd;
                    Console.WriteLine("Image {0} is RGB...", image_counter);
                    break;
            }
            image_counter += 1;
        }
    }
}
```

## Control Image Quality

It is possible to control the quality of an image that’s being added to a PDF file. Use the overloaded [Replace](https://apireference.aspose.com/pdf/net/aspose.pdf.ximagecollection/replace/methods/1) method in the [XImageCollection](https://apireference.aspose.com/pdf/net/aspose.pdf/ximagecollection) class.

The following code snippet demonstrates how to convert all the document images into JPEGs that use 80% quality for compression.

```csharp
Aspose.PDF.Document pdfDocument = new Aspose.PDF.Document(inFile);
foreach (Aspose.PDF.Page page in pdfDocument.Pages)
{
    int idx = 1;
    foreach (Aspose.PDF.XImage image in page.Resources.Images)
    {
        using (MemoryStream imageStream = new MemoryStream())
        {
            image.Save(imageStream, System.Drawing.Imaging.ImageFormat.Jpeg);
            page.Resources.Images.Replace(idx, imageStream, 80);
            idx = idx + 1;
        }
    }
}

// pdfDocument.OptimizeResources();

pdfDocument.Save(outFile);
```

