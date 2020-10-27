---
title: Working with Images in PDF
type: docs
weight: 20
url: /net/working-with-images-in-pdf/
---
# Working with Images in PDF

## Add Image to Existing PDF File

Every PDF page contains Resources and Contents properties. Resources can be images and forms for example, while content is represented by a set of PDF operators. Each operator has its name and argument. This example uses operators to add anh image to a PDF file.

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
```
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
>By default, the JPEG quality is set to 100%. To apply better compression and quality, use the following overloads:
- the Replace method overload is added into the XImageCollection class: public void Replace(int index, Stream stream, int quality)
- the Add method overload is added into the XImageCollection class: public void Add(Stream stream, int quality)

## Add Reference of a single Image multiple times in a PDF Document 

Sometimes we have a requirement to use same image multiple times in a PDF document. Adding a new instance increases the resultant PDF document. We have added a new method XImageCollection.Add(XImage) in Aspose.PDF for .NET 17.1.0. This method allows to add reference to the same PDF object as original image that optimize the PDF Document size.
```
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
## Delete Images from a PDF File

To delete an image from a PDF file:

1. Create a Document object and open the input PDF file.
1. Get the Page that holds the image from the Document object’s Pages collection.
1. Images are held in the Images collection, found in the page’s Resources collection.
1. Delete an image with the Images collection’s Delete method.
1. Saved the output like using the Document object’s Save method.
1. The following code snippet shows how to delete an image from a PDF file.
```
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Images();

// Open document
Document pdfDocument = new Document(dataDir+ "DeleteImages.pdf");

// Delete a particular image
pdfDocument.Pages[1].Resources.Images.Delete(1);

dataDir = dataDir + "DeleteImages_out.pdf";
// Save updated PDF file
pdfDocument.Save(dataDir);
```
## Extract Images from the PDF File

Images are held in each page’s [Resources](https://apireference.aspose.com/pdf/net/aspose.pdf/resources) collection’s [Images](https://apireference.aspose.com/pdf/net/aspose.pdf/resources/properties/images) collection. To extract a particular page, then get the image from the Images collection using the particular index of the image.

The image’s index returns an [XImage](https://apireference.aspose.com/pdf/net/aspose.pdf/ximage) object. This object provides a Save method which can be used to save the extracted image. The following code snippet shows how to extract images from a PDF file.
```
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Images();

// Open document
Document pdfDocument = new Document(dataDir+ "ExtractImages.pdf");

// Extract a particular image
XImage xImage = pdfDocument.Pages[1].Resources.Images[1];

FileStream outputImage = new FileStream(dataDir + "output.jpg", FileMode.Create);

// Save output image
xImage.Save(outputImage, ImageFormat.Jpeg);
outputImage.Close();

dataDir = dataDir + "ExtractImages_out.pdf";

// Save updated PDF file
pdfDocument.Save(dataDir);
```
## Get the Resolution and Dimensions of Embedded Images

This topic explains how to use the operator classes in the Aspose.PDF namespace which provide the capability to get resolution and dimension information about images without having to extract them.

There are different ways of achieving this. This article explains how to use an `arraylist` and [image placement classes](https://apireference.aspose.com/pdf/net/aspose.pdf/imageplacement).
1. First, load the source PDF file (with images).
1. Then create an ArrayList object to hold the names of any images in the document.
1. Get the images using the Page.Resources.Images property.
1. Create a stack object to hold the image’s graphics state and use it to keep track of different image states.
1. Create a ConcatenateMatrix object which defines current transformation. It also supports scaling, rotating, and skewing any content. It concatenates the new matrix with previous one. Please note that we cannot define the transformation from scratch but only modify the existing transformation.
1. Because we can modify the matrix with ConcatenateMatrix, we may also need to revert back to the original image state. Use GSave and GRestore operators. These operators are paired so they should be called together. For example, if you do some graphics work with complex transformations and finally return transformations back to initial state, the approach will be something like this:
```
// Draw some text

GSave

ConcatenateMatrix  // rotate contents after the operator

// Some graphics work

ConcatenateMatrix // scale (with previous rotation) contents after the operator

// Some other graphics work

GRestore

// Draw some text
```
As a result, text is drawn in regular form but some transformations are performed between the text operators. In order to display the image or to draw form objects and images, we need to use the Do operator.

We also have a class named XImage which provides two properties,l Width and Height, which can be used to get image dimensions.

1. Perform some calculations to compute the image resolution.
1. Display the information in a Command Prompt along with the image name.

The following code snippet shows you how to get an image’s dimensions and resolution without extracting the image from the PDF document.
```
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Images();

// Load the source PDF file
Document doc = new Document(dataDir+ "ImageInformation.pdf");

// Define the default resolution for image
int defaultResolution = 72;
System.Collections.Stack graphicsState = new System.Collections.Stack();
// Define array list object which will hold image names
System.Collections.ArrayList imageNames = new System.Collections.ArrayList(doc.Pages[1].Resources.Images.Names);
// Insert an object to stack
graphicsState.Push(new System.Drawing.Drawing2D.Matrix(1, 0, 0, 1, 0, 0));

// Get all the operators on first page of document
foreach (Operator op in doc.Pages[1].Contents)
{
    // Use GSave/GRestore operators to revert the transformations back to previously set
    Aspose.Pdf.Operators.GSave opSaveState = op as Aspose.Pdf.Operators.GSave;
    Aspose.Pdf.Operators.GRestore opRestoreState = op as Aspose.Pdf.Operators.GRestore;
    // Instantiate ConcatenateMatrix object as it defines current transformation matrix.
    Aspose.Pdf.Operators.ConcatenateMatrix opCtm = op as Aspose.Pdf.Operators.ConcatenateMatrix;
    // Create Do operator which draws objects from resources. It draws Form objects and Image objects
    Aspose.Pdf.Operators.Do opDo = op as Aspose.Pdf.Operators.Do;

    if (opSaveState != null)
    {
        // Save previous state and push current state to the top of the stack
        graphicsState.Push(((System.Drawing.Drawing2D.Matrix)graphicsState.Peek()).Clone());
    }
    else if (opRestoreState != null)
    {
        // Throw away current state and restore previous one
        graphicsState.Pop();
    }
    else if (opCtm != null)
    {
        System.Drawing.Drawing2D.Matrix cm = new System.Drawing.Drawing2D.Matrix(
           (float)opCtm.Matrix.A,
           (float)opCtm.Matrix.B,
           (float)opCtm.Matrix.C,
           (float)opCtm.Matrix.D,
           (float)opCtm.Matrix.E,
           (float)opCtm.Matrix.F);

        // Multiply current matrix with the state matrix
        ((System.Drawing.Drawing2D.Matrix)graphicsState.Peek()).Multiply(cm);

        continue;
    }
    else if (opDo != null)
    {
        // In case this is an image drawing operator
        if (imageNames.Contains(opDo.Name))
        {
            System.Drawing.Drawing2D.Matrix lastCTM = (System.Drawing.Drawing2D.Matrix)graphicsState.Peek();
            // Create XImage object to hold images of first pdf page
            XImage image = doc.Pages[1].Resources.Images[opDo.Name];

            // Get image dimensions
            double scaledWidth = Math.Sqrt(Math.Pow(lastCTM.Elements[0], 2) + Math.Pow(lastCTM.Elements[1], 2));
            double scaledHeight = Math.Sqrt(Math.Pow(lastCTM.Elements[2], 2) + Math.Pow(lastCTM.Elements[3], 2));
            // Get Height and Width information of image
            double originalWidth = image.Width;
            double originalHeight = image.Height;

            // Compute resolution based on above information
            double resHorizontal = originalWidth * defaultResolution / scaledWidth;
            double resVertical = originalHeight * defaultResolution / scaledHeight;

            // Display Dimension and Resolution information of each image
            Console.Out.WriteLine(
                    string.Format(dataDir + "image {0} ({1:.##}:{2:.##}): res {3:.##} x {4:.##}",
                                 opDo.Name, scaledWidth, scaledHeight, resHorizontal,
                                 resVertical));
        }
    }
}
```
## Working with Image Placement

With the release of Aspose.PDF for .NET 7.0.0, we introduced classes called [ImagePlacement](https://apireference.aspose.com/pdf/net/aspose.pdf/imageplacement), [ImagePlacementAbsorber](https://apireference.aspose.com/pdf/net/aspose.pdf/imageplacementabsorber) and [ImagePlacementCollection](https://apireference.aspose.com/pdf/net/aspose.pdf/imageplacementcollection) which provide similar capability as the classes described above to get an image’s resolution and position in a PDF document.

- ImagePlacementAbsorber performs image usage search as the ImagePlacement objects collection.
- ImagePlacement provides the members Resolution and Rectangle that return actual image placement values.
```
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Images();


// Load the source PDF document
Aspose.Pdf.Document doc = new Aspose.Pdf.Document(dataDir+ "ImagePlacement.pdf");
ImagePlacementAbsorber abs = new ImagePlacementAbsorber();
            
// Load the contents of first page
doc.Pages[1].Accept(abs);
foreach (ImagePlacement imagePlacement in abs.ImagePlacements)
{
    // Get image properties
    Console.Out.WriteLine("image width:" + imagePlacement.Rectangle.Width);
    Console.Out.WriteLine("image height:" + imagePlacement.Rectangle.Height);
    Console.Out.WriteLine("image LLX:" + imagePlacement.Rectangle.LLX);
    Console.Out.WriteLine("image LLY:" + imagePlacement.Rectangle.LLY);
    Console.Out.WriteLine("image horizontal resolution:" + imagePlacement.Resolution.X);
    Console.Out.WriteLine("image vertical resolution:" + imagePlacement.Resolution.Y);

    // Retrieve image with visible dimensions
    Bitmap scaledImage;
    using (MemoryStream imageStream = new MemoryStream())
    {
        // Retrieve image from resources
        imagePlacement.Image.Save(imageStream, System.Drawing.Imaging.ImageFormat.Png);
        Bitmap resourceImage = (Bitmap)Bitmap.FromStream(imageStream);
        // Create bitmap with actual dimensions
        scaledImage = new Bitmap(resourceImage, (int)imagePlacement.Rectangle.Width, (int)imagePlacement.Rectangle.Height);
    }
}
```
## Search and Get Images from PDF Document

The ImagePlacementAbsorber allows you to search among images on all pages in a PDF document.

To search a whole document for images:

1. Call the Pages collection’s Accept method. The Accept method takes an ImagePlacementAbsorber object as a parameter. This returns a collection of ImagePlacement objects.
1. Loop through the ImagePlacements objects and get their properties (Image, dimensions, resolution and so on).

The following code snippet shows how to search a document for all its images.
```
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Images();

// Open document
Aspose.Pdf.Document doc = new Aspose.Pdf.Document(dataDir+ "SearchAndGetImages.pdf");

// Create ImagePlacementAbsorber object to perform image placement search
ImagePlacementAbsorber abs = new ImagePlacementAbsorber();

// Accept the absorber for all the pages
doc.Pages.Accept(abs);

// Loop through all ImagePlacements, get image and ImagePlacement Properties
foreach (ImagePlacement imagePlacement in abs.ImagePlacements)
{
    // Get the image using ImagePlacement object
    XImage image = imagePlacement.Image;

    // Display image placement properties for all placements
    Console.Out.WriteLine("image width:" + imagePlacement.Rectangle.Width);
    Console.Out.WriteLine("image height:" + imagePlacement.Rectangle.Height);
    Console.Out.WriteLine("image LLX:" + imagePlacement.Rectangle.LLX);
    Console.Out.WriteLine("image LLY:" + imagePlacement.Rectangle.LLY);
    Console.Out.WriteLine("image horizontal resolution:" + imagePlacement.Resolution.X);
    Console.Out.WriteLine("image vertical resolution:" + imagePlacement.Resolution.Y);
}
```
To get an image from an individual page, use the following code:

```
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
doc.Pages[1].Accept(abs);
```
## Identify if image inside PDF is Colored or Black & White

Different type of compression can be applied over images to reduce their size. The type of compression being applied over image depends upon the ColorSpace of source image i.e. if image is Color (RGB), then apply JPEG2000 compression, and if it is Black & White, then JBIG2/JBIG2000 compression should be applied. Therefore identifying each image type and using an appropriate type of compression will create best/optimized output.

A PDF file may contain Text, Image, Graph, Attachment, Annotation etc elements and if the source PDF file contains images, we can determine image Color space and apply appropriate compression for image to reduce PDF file size. The following code snippet shows the steps to Identify if image inside PDF is Colored or Black & White.

```
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
## Replace Image in Existing PDF File

The Images collection’s Replace method allows you to replace an image in an existing PDF file.

The Images collection can be found in a page’s Resources collection. To replace an image:

1. Open the PDF file using the Document object.
2. Replaced the , save the updated PDF file using Save method of the Document object.

The following code snippet shows you how to replace an image in a PDF file.
```
// Open document
Document pdfDocument = new Document("input.pdf");
// Replace a particular image
pdfDocument.Pages[1].Resources.Images.Replace(1, new FileStream("lovely.jpg", FileMode.Open));
// Save updated PDF file
pdfDocument.Save("output.pdf");
```
## Control Image Quality

It is possible to control the quality of an image that’s being added to a PDF file. Use the overloaded Replace method in the XImageCollection class: public void Replace(int index, Stream stream, int quality)

The following code snippet demonstrates how to convert all the document images into JPEGs that use 80% quality for compression.
```
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
## Set Image Size

It is possible to set the size of an image that’s being added to a PDF file. In order to set size, you can use FixWidth and FixHeight properties of Aspose.Pdf.Image Class. The following code snippet demonstrates how to set the size of an image:
```
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
## Set Default Font Name

Aspose.PDF for .NET API allows you to set a default font name when a font is not available in the document. You can use DefaultFontName property of RenderingOptions class to set the default font name. In case DefaultFontName is set to null the Times New Roman font will be used. The following code snippet shows how to set a default font name when saving PDF into an image:
```
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
## Support for DICOM Images 

Aspose.PDF for .NET supports functionality to add DICOM images to PDF documents. The following code snippet shows how to use this functionality.
```
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
