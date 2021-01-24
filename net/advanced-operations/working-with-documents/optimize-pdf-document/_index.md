---
title: Optimize PDF 
type: docs
weight: 30
url: /net/optimize-pdf/
description: Optimize PDF file, shrink all images, reduce size PDF, Unembed fonts, Remove unused objects with C#.
lastmod: "2020-12-22"
aliases: 
    - /net/changing-page-sizes-in-a-pdf-file/
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

A PDF document may sometimes contain additional data. Reducing the size of a PDF file will help you optimize network transfer and storage. This is especially handy for publishing on web pages, sharing on social networks, sending by e-mail, or archiving in storage. We can use several techniques to optimize PDF:

- Optimize page content for online browsing
- Shrink or compress all images
- Enable reusing page content
- Merge duplicate streams
- Unembed fonts
- Remove unused objects 
- Remove flattening form fields 
- Remove or flatten annotations

{{% alert color="primary" %}}

 Detailed explanation of optimization methods can be found in the Optimization Methods Overview page.

{{% /alert %}}

## Optimize PDF Document for the Web

Optimization, or linearization for Web, refers to the process of making a PDF file suitable for online browsing using a web browser. To optimize a file for web display:

1. Open the input document in an [Document](https://apireference.aspose.com/pdf/net/aspose.pdf/document) object.
1. Use the [Optimize](https://apireference.aspose.com/pdf/net/aspose.pdf/document/methods/optimize) method.
1. Save the optimized document using the [Save](https://apireference.aspose.com/pdf/net/aspose.pdf/document/methods/save) method.

The following code snippet shows how to optimize a PDF document for the web.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Open document
Document pdfDocument = new Document(dataDir + "OptimizeDocument.pdf");

// Optimize for web
pdfDocument.Optimize();

dataDir = dataDir + "OptimizeDocument_out.pdf";

// Save output document
pdfDocument.Save(dataDir);
```

## Reduce Size PDF

The [OptimizeResources()](https://apireference.aspose.com/pdf/net/aspose.pdf/document/methods/optimizeresources) method allows you to reduce the document size by weeding out the unnecessary information. By default, this method works as follows:

- Resources that are not used on the document pages are removed 
- Equal resources are joined into one object
- Unused objects are deleted

The snippet below is an example. Note, though, that this method cannot guarantee document shrinking.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
// Open document
Document pdfDocument = new Document(dataDir + "ShrinkDocument.pdf");
// Optimize PDF document. Note, though, that this method cannot guarantee document shrinking
pdfDocument.OptimizeResources();
dataDir = dataDir + "ShrinkDocument_out.pdf";
// Save updated document
pdfDocument.Save(dataDir);
```

## Optimization Strategy Management

We can also customize the optimization strategy. Currently, the [OptimizeResources()](https://apireference.aspose.com/pdf/net/aspose.pdf.document/optimizeresources/methods/1) method uses 5 techniques. These techniques can be applied using the OptimizeResources() method with the [OptimizationOptions](https://apireference.aspose.com/pdf/net/aspose.pdf.optimization/optimizationoptions) parameter.

### Shrinking or Compressing All Images

We have two ways to work with images: reduce image quality and/or change their resolution. In any case, [ImageCompressionOptions](https://apireference.aspose.com/pdf/net/aspose.pdf.optimization/imagecompressionoptions) should be applied. In the following example, we shrink images by reducing [ImageQuality](https://apireference.aspose.com/pdf/net/aspose.pdf.optimization/imagecompressionoptions/properties/imagequality) to 50.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Images();
// Open document
Document pdfDocument = new Document(dataDir + "Shrinkimage.pdf");
// Initialize OptimizationOptions
var optimizeOptions = new Pdf.Optimization.OptimizationOptions();
// Set CompressImages option
optimizeOptions.ImageCompressionOptions.CompressImages = true;
// Set ImageQuality option
optimizeOptions.ImageCompressionOptions.ImageQuality = 50;
// Optimize PDF document using OptimizationOptions
pdfDocument.OptimizeResources(optimizeOptions);
dataDir = dataDir + "Shrinkimage_out.pdf";
// Save updated document
pdfDocument.Save(dataDir);
```

Another way is to resize the images with a lower resolution. In this case, we should set ResizeImages to true and MaxResolution to the appropriate value.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Initialize Time
var time = DateTime.Now.Ticks;
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Images();
// Open document
Document pdfDocument = new Document(dataDir + "ResizeImage.pdf");
// Initialize OptimizationOptions
var optimizeOptions = new Pdf.Optimization.OptimizationOptions();
// Set CompressImages option
optimizeOptions.ImageCompressionOptions.CompressImages = true;
// Set ImageQuality option 
optimizeOptions.ImageCompressionOptions.ImageQuality = 75;
// Set ResizeImage option
optimizeOptions.ImageCompressionOptions.ResizeImages = true;
// Set MaxResolution option
optimizeOptions.ImageCompressionOptions.MaxResolution = 300;
// Optimize PDF document using OptimizationOptions
pdfDocument.OptimizeResources(optimizeOptions);
dataDir = dataDir + "ResizeImages_out.pdf";
// Save updated document
pdfDocument.Save(dataDir);
```

Another important issue is the execution time. But again, we can manage this setting too. Currently, we can use two algorithms - Standard and Fast. To control the execution time we should set a [Version](https://apireference.aspose.com/pdf/net/aspose.pdf.optimization/imagecompressionoptions/properties/version) property. The following snippet demonstrates the Fast algorithm:

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Initialize Time
var time = DateTime.Now.Ticks;
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Images();
// Open document
Document pdfDocument = new Document(dataDir + "Shrinkimage.pdf");
// Initialize OptimizationOptions
var optimizeOptions = new Pdf.Optimization.OptimizationOptions();
// Set CompressImages option
optimizeOptions.ImageCompressionOptions.CompressImages = true;
// Set ImageQuality option
optimizeOptions.ImageCompressionOptions.ImageQuality = 75;
// Set Imagae Compression Version to fast 
optimizeOptions.ImageCompressionOptions.Version = Pdf.Optimization.ImageCompressionVersion.Fast;
// Optimize PDF document using OptimizationOptions
pdfDocument.OptimizeResources(optimizeOptions);
dataDir = dataDir + "FastShrinkImages_out.pdf";
// Save updated document
pdfDocument.Save(dataDir);
Console.WriteLine("Ticks: {0}", DateTime.Now.Ticks - time);
```

### Removing Unused Objects

A PDF document sometimes contains the PDF objects that are not referenced from any other object in the document. This may happen, for example, when a page is removed from the document page tree but the page object itself isn’t removed. Removing these objects doesn’t make the document invalid but rather shrinks it.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
// Open document
Document pdfDocument = new Document(dataDir + "OptimizeDocument.pdf");
// Set RemoveUsedObject option 
var optimizeOptions = new Pdf.Optimization.OptimizationOptions
{
    RemoveUnusedObjects = true
};
// Optimize PDF document using OptimizationOptions
pdfDocument.OptimizeResources(optimizeOptions);
dataDir = dataDir + "OptimizeDocument_out.pdf";
// Save updated document
pdfDocument.Save(dataDir);
```

### Removing Unused Streams

Sometimes the document contains the unused resource streams. These streams are not “unused objects” because they are referenced from a page resource dictionary. Thus, they are not removed with a “remove unused objects” method. But these streams are never used with the page contents. This may happen in cases when an image has been removed from the page but not from the page resources. Also, this situation often occurs when pages are extracted from the document and document pages have “common” resources, that is, the same Resources object. Page contents are analyzed in order to determine if a resource stream is used or not. Unused streams are removed. It sometimes decreases the document size. The use of this technique is similar to the previous step:

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
// Open document
Document pdfDocument = new Document(dataDir + "OptimizeDocument.pdf");
// Set RemoveUsedStreams option 
var optimizeOptions = new Pdf.Optimization.OptimizationOptions
{
    RemoveUnusedStreams = true
};
// Optimize PDF document using OptimizationOptions
pdfDocument.OptimizeResources(optimizeOptions);
dataDir = dataDir + "OptimizeDocument_out.pdf";
// Save updated document
pdfDocument.Save(dataDir);
```

### Linking Duplicate Streams

Some documents can contain several identical resource streams (like images, for instance). This may happen, say when a document is concatenated with itself. The output document contains two independent copies of the same resource stream. We analyze all resource streams and compare them. If streams are duplicated, they are merged, that is, only one copy is left. The references are changed appropriately, and the copies of the object are removed. In some cases, it helps to decrease the document size.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
// Open document
Document pdfDocument = new Document(dataDir + "OptimizeDocument.pdf");
// Set LinkDuplcateStreams option 
var optimizeOptions = new Pdf.Optimization.OptimizationOptions
{
    LinkDuplcateStreams = true
};
// Optimize PDF document using OptimizationOptions
pdfDocument.OptimizeResources(optimizeOptions);
dataDir = dataDir + "OptimizeDocument_out.pdf";
// Save updated document
pdfDocument.Save(dataDir);
```

Additionally, we can use [AllowReusePageContent](https://apireference.aspose.com/pdf/net/aspose.pdf.optimization/optimizationoptions/properties/allowreusepagecontent) settings. If this property is set to true, the page content will be reused when optimizing the document for identical pages.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
// Open document
Document pdfDocument = new Document(dataDir + "OptimizeDocument.pdf");
// Set AllowReusePageContent  option 
var optimizeOptions = new Pdf.Optimization.OptimizationOptions
{
    AllowReusePageContent = true
};
Console.WriteLine("Start");
// Optimize PDF document using OptimizationOptions
pdfDocument.OptimizeResources(optimizeOptions);
// Save updated document
pdfDocument.Save(dataDir + "OptimizeDocument_out.pdf");
Console.WriteLine("Finished");
var fi1 = new System.IO.FileInfo(dataDir + "OptimizeDocument.pdf");
var fi2 = new System.IO.FileInfo(dataDir + "OptimizeDocument_out.pdf");
Console.WriteLine("Original file size: {0}. Reduced file size: {1}", fi1.Length, fi2.Length);
```

### Unembedding Fonts

If the document uses embedded fonts, it means that all font data is stored in the document. The advantage is that the document is viewable regardless of whether the font is installed on the user’s machine or not. But embedding fonts makes the document larger. The unembed fonts method removes all embedded fonts. Thus, the document size decreases but the document itself may become unreadable if the correct font is not installed.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
// Open document
Document pdfDocument = new Document(dataDir + "OptimizeDocument.pdf");
// Set UnembedFonts  option
var optimizeOptions = new Pdf.Optimization.OptimizationOptions
{
    UnembedFonts = true
};
Console.WriteLine("Start");
// Optimize PDF document using OptimizationOptions
pdfDocument.OptimizeResources(optimizeOptions);
// Save updated document
pdfDocument.Save(dataDir + "OptimizeDocument_out.pdf");
Console.WriteLine("Finished");
var fi1 = new System.IO.FileInfo(dataDir + "OptimizeDocument.pdf");
var fi2 = new System.IO.FileInfo(dataDir + "OptimizeDocument_out.pdf");
Console.WriteLine("Original file size: {0}. Reduced file size: {1}", fi1.Length, fi2.Length);
```

The optimization resources apply these methods to the document. If any of these methods are applied, the document size will most probably decrease. If none of these methods is applied, the document size will not change which is obvious.

## Additional Ways to Reduce the PDF Document Size

### Removing or Flattening Annotations

Annotations can be deleted when they are unnecessary. When they are needed but do not require additional editing, they can be flattened. Both of these techniques will reduce the file size.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
// Open document
Document pdfDocument = new Document(dataDir + "OptimizeDocument.pdf");
// Flatten annotations
foreach (var page in pdfDocument.Pages)
{
    foreach (var annotation in page.Annotations)
    {
        annotation.Flatten();
    }

}
// Save updated document
pdfDocument.Save(dataDir + "OptimizeDocument_out.pdf");
```

### Removing Form Fields

If the PDF document contains AcroForms, we can try to reduce the file size by flattening form fields.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

// Load source PDF form
Document doc = new Document(dataDir + "input.pdf");

// Flatten Forms
if (doc.Form.Fields.Count() > 0)
{
    foreach (var item in doc.Form.Fields)
    {
        item.Flatten();
    }
}

dataDir = dataDir + "FlattenForms_out.pdf";
// Save the updated document
doc.Save(dataDir);
```

### Convert a PDF from RGB colorspace to grayscale

A PDF file comprises Text, Image, Attachment, Annotations, Graphs, and other objects. You may come across a requirement to convert a PDF from RGB colorspace to grayscale so that it would be faster while printing those PDF files. Also, when the file is converted to grayscale, the document size is reduced too, but it can just as well cause a decrease in the document quality. This feature is currently supported by the Pre-Flight feature of Adobe Acrobat, but when talking about Office automation, Aspose.PDF is an ultimate solution to provide such leverages for document manipulations. In order to accomplish this requirement, the following code snippet can be used.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Load source PDF file
using (Document document = new Document(dataDir + "input.pdf"))
{
    Aspose.Pdf.RgbToDeviceGrayConversionStrategy strategy = new Aspose.Pdf.RgbToDeviceGrayConversionStrategy();
    for (int idxPage = 1; idxPage <= document.Pages.Count; idxPage++)
    {
        // Get instance of particular page inside PDF
        Page page = document.Pages[idxPage];
        // Convert the RGB colorspace image to GrayScale colorspace
        strategy.Convert(page);
    }
    // Save resultant file
    document.Save(dataDir + "Test-gray_out.pdf");
}
```

### FlateDecode Compression

{{% alert color="primary" %}}

This feature is supported by version 18.12 or greater.

{{% /alert %}}

Aspose.PDF for .NET provides support of FlateDecode compression for PDF Optimisation functionality. The following code snippet below shows how to use the option in Optimization to store images with **FlateDecode** compression:

{{< gist "aspose-com-gists" "63473b1ba28e09e229cfbf4430eabd8a" "Examples-CSharp-AsposePDF-Images-FlateDecodeCompression-1.cs" >}}

### **Store Image in XImageCollection**

Aspose.PDF for .NET provides the ability to store new images into **XImageCollection** with FlateDecode compression. To enable this option you can use **ImageFilterType.Flate** flag. The following code snippet shows how to use this functionality:

{{< gist "aspose-com-gists" "63473b1ba28e09e229cfbf4430eabd8a" "Examples-CSharp-AsposePDF-Images-StoreImageInXImageCollection-1.cs" >}}
