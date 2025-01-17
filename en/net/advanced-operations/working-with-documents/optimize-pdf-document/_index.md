---
title: Optimize, Compress or Reduce PDF Size in C#
linktitle: Optimize PDF
type: docs
weight: 40
url: /net/optimize-pdf/
description: Optimize PDF file, shrink all images, reduce size PDF, Unembed fonts, Remove unused objects with C#.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
aliases:
    - /net/changing-page-sizes-in-a-pdf-file/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Optimize, Compress or Reduce PDF Size in C#",
    "alternativeHeadline": "Optimize PDF Files Efficiently with C#",
    "abstract": "The new PDF optimization feature in C# allows developers to significantly reduce PDF file sizes by employing multiple strategies, such as compressing images, unembedding fonts, and removing unused objects. This enhancement improves efficiency for web publishing, email sharing, and storage, providing an effective solution for managing large PDF documents",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "optimize pdf, compress pdf size, reduce pdf size, optimize pdf c#, unembed fonts, remove unused objects, shrink images, optimization methods, pdf document generation, Aspose.PDF",
    "wordcount": "2282",
    "proficiencyLevel": "Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF for .NET",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "sales",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "sales",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "sales",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/net/optimize-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/optimize-pdf/"
    },
    "dateModified": "2024-11-25",
    "description": "Optimize PDF file, shrink all images, reduce size PDF, Unembed fonts, Remove unused objects with C#."
}
</script>

A PDF document may sometimes contain additional data. Reducing the size of a PDF file will help you optimize network transfer and storage. This is especially handy for publishing on web pages, sharing on social networks, sending by e-mail, or archiving in storage. We can use several techniques to optimize PDF:

- Optimize page content for online browsing.
- Shrink or compress all images.
- Enable reusing page content.
- Merge duplicate streams.
- Unembed fonts.
- Remove unused objects.
- Remove flattening form fields.
- Remove or flatten annotations.

{{% alert color="primary" %}}

 Detailed explanation of optimization methods can be found in the Optimization Methods Overview page.

{{% /alert %}}

## Optimize PDF Document for the Web

Optimization, or linearization for Web, refers to the process of making a PDF file suitable for online browsing using a web browser. To optimize a file for web display:

1. Open the input document in an [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) object.
1. Use the [Optimize](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/optimize) method.
1. Save the optimized document using the [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) method.

The following code snippet also work with [Aspose.PDF.Drawing](/pdf/net/drawing/) library.

The following code snippet shows how to optimize a PDF document for the web.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void OptimizeDocument()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "OptimizeDocument.pdf"))
    {
		// Optimize for web
		document.Optimize();

		// Save PDF document
		document.Save(dataDir + "OptimizeDocument_out.pdf");
	}
}
```

## Reduce Size PDF

The [OptimizeResources()](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/optimizeresources) method allows you to reduce the document size by weeding out the unnecessary information. By default, this method works as follows:

- Resources that are not used on the document pages are removed.
- Equal resources are joined into one object.
- Unused objects are deleted.

The snippet below is an example. Note, though, that this method cannot guarantee document shrinking.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ShrinkDocument()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ShrinkDocument.pdf"))
	{
		// Optimize PDF document. Note, though, that this method cannot guarantee document shrinking
		document.OptimizeResources();

		// Save PDF document
		document.Save(dataDir + "ShrinkDocument_out.pdf");
	}
}
```

## Optimization Strategy Management

We can also customize the optimization strategy. Currently, the [OptimizeResources()](https://reference.aspose.com/pdf/net/aspose.pdf.document/optimizeresources/methods/1) method uses 5 techniques. These techniques can be applied using the OptimizeResources() method with the [OptimizationOptions](https://reference.aspose.com/pdf/net/aspose.pdf.optimization/optimizationoptions) parameter.

### Shrinking or Compressing All Images

We have two ways to work with images: reduce image quality and/or change their resolution. In any case, [ImageCompressionOptions](https://reference.aspose.com/pdf/net/aspose.pdf.optimization/imagecompressionoptions) should be applied. In the following example, we shrink images by reducing [ImageQuality](https://reference.aspose.com/pdf/net/aspose.pdf.optimization/imagecompressionoptions/properties/imagequality) to 50.

`ImageQuality` works similarly to JPEG quality, where value 0 is the lowest and value 100 is the highest.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ShrinkImage()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "Shrinkimage.pdf"))
	{
		// Initialize OptimizationOptions
		var optimizeOptions = new Aspose.Pdf.Optimization.OptimizationOptions();

		// Set CompressImages option
		optimizeOptions.ImageCompressionOptions.CompressImages = true;

		// Set ImageQuality option
		optimizeOptions.ImageCompressionOptions.ImageQuality = 50;

		// Optimize PDF document using OptimizationOptions
		document.OptimizeResources(optimizeOptions);

		// Save PDF document
		document.Save(dataDir + "Shrinkimage_out.pdf");
	}
}
```

Another way is to resize the images with a lower resolution. In this case, we should set ResizeImages to true and MaxResolution to the appropriate value.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ResizeImages()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ResizeImage.pdf"))
	{
		// Initialize OptimizationOptions
		var optimizeOptions = new Aspose.Pdf.Optimization.OptimizationOptions();

		// Set CompressImages option
		optimizeOptions.ImageCompressionOptions.CompressImages = true;

		// Set ImageQuality option
		optimizeOptions.ImageCompressionOptions.ImageQuality = 75;

		// Set ResizeImage option
		optimizeOptions.ImageCompressionOptions.ResizeImages = true;

		// Set MaxResolution option
		optimizeOptions.ImageCompressionOptions.MaxResolution = 300;

		// Optimize PDF document using OptimizationOptions
		document.OptimizeResources(optimizeOptions);

		// Save PDF document
		document.Save(dataDir + "ResizeImages_out.pdf");
	}
}
```

Another important issue is the execution time. But again, we can manage this setting too. Currently, we can use two algorithms - Standard and Fast. To control the execution time we should set a [Version](https://reference.aspose.com/pdf/net/aspose.pdf.optimization/imagecompressionoptions/properties/version) property. The following snippet demonstrates the Fast algorithm:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void FastShrinkImages()
{
    // Initialize Time
    var time = DateTime.Now.Ticks;

    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "Shrinkimage.pdf"))
	{
		// Initialize OptimizationOptions
		var optimizeOptions = new Aspose.Pdf.Optimization.OptimizationOptions();

		// Set CompressImages option
		optimizeOptions.ImageCompressionOptions.CompressImages = true;

		// Set ImageQuality option
		optimizeOptions.ImageCompressionOptions.ImageQuality = 75;

		// Set Image Compression Version to fast
		optimizeOptions.ImageCompressionOptions.Version = Aspose.Pdf.Optimization.ImageCompressionVersion.Fast;

		// Optimize PDF document using OptimizationOptions
		document.OptimizeResources(optimizeOptions);

		// Save PDF document
		document.Save(dataDir + "FastShrinkImages_out.pdf");
	}

    // Output the time taken for the operation
    Console.WriteLine("Ticks: {0}", DateTime.Now.Ticks - time);
}
```

### Removing Unused Objects

A PDF document sometimes contains the PDF objects that are not referenced from any other object in the document. This may happen, for example, when a page is removed from the document page tree but the page object itself isn’t removed. Removing these objects doesn’t make the document invalid but rather shrinks it.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void OptimizeDocument()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "OptimizeDocument.pdf"))
    {
		// Set RemoveUsedObject option
		var optimizeOptions = new Aspose.Pdf.Optimization.OptimizationOptions
		{
			RemoveUnusedObjects = true
		};
		
		// Optimize PDF document using OptimizationOptions
		document.OptimizeResources(optimizeOptions);

		// Save PDF document
		document.Save(dataDir + "OptimizeDocument_out.pdf");
	}
}
```

### Removing Unused Streams

Sometimes the document contains the unused resource streams. These streams are not “unused objects” because they are referenced from a page resource dictionary. Thus, they are not removed with a “remove unused objects” method. But these streams are never used with the page contents. This may happen in cases when an image has been removed from the page but not from the page resources. Also, this situation often occurs when pages are extracted from the document and document pages have “common” resources, that is, the same Resources object. Page contents are analyzed in order to determine if a resource stream is used or not. Unused streams are removed. It sometimes decreases the document size. The use of this technique is similar to the previous step:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void OptimizePdfDocument()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "OptimizeDocument.pdf"))
	{
		// Set RemoveUsedStreams option
		var optimizeOptions = new Aspose.Pdf.Optimization.OptimizationOptions
		{
			RemoveUnusedStreams = true
		};

		// Optimize PDF document using OptimizationOptions
		document.OptimizeResources(optimizeOptions);

		// Save PDF document
		document.Save(dataDir + "OptimizeDocument_out.pdf");
	}
}
```

### Linking Duplicate Streams

Some documents can contain several identical resource streams (like images, for instance). This may happen, say when a document is concatenated with itself. The output document contains two independent copies of the same resource stream. We analyze all resource streams and compare them. If streams are duplicated, they are merged, that is, only one copy is left. The references are changed appropriately, and the copies of the object are removed. In some cases, it helps to decrease the document size.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void OptimizePdfDocumentWithLinkDuplicateStreams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "OptimizeDocument.pdf"))
	{
		// Set LinkDuplicateStreams option
		var optimizeOptions = new Aspose.Pdf.Optimization.OptimizationOptions
		{
			LinkDuplicateStreams = true
		};

		// Optimize PDF document using OptimizationOptions
		document.OptimizeResources(optimizeOptions);

		// Save PDF document
		document.Save(dataDir + "OptimizeDocument_out.pdf");
	}
}
```

Additionally, we can use [AllowReusePageContent](https://reference.aspose.com/pdf/net/aspose.pdf.optimization/optimizationoptions/properties/allowreusepagecontent) settings. If this property is set to true, the page content will be reused when optimizing the document for identical pages.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void OptimizePdfDocumentWithReusePageContent()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "OptimizeDocument.pdf"))
	{
		// Set AllowReusePageContent option
		var optimizeOptions = new Aspose.Pdf.Optimization.OptimizationOptions
		{
			AllowReusePageContent = true
		};

		Console.WriteLine("Start");

		// Optimize PDF document using OptimizationOptions
		document.OptimizeResources(optimizeOptions);

		// Save PDF document
		document.Save(dataDir + "OptimizeDocument_out.pdf");
	}

    Console.WriteLine("Finished");

    // Calculate and display file sizes
    var fi1 = new FileInfo(dataDir + "OptimizeDocument.pdf");
    var fi2 = new FileInfo(dataDir + "OptimizeDocument_out.pdf");
    Console.WriteLine("Original file size: {0}. Reduced file size: {1}", fi1.Length, fi2.Length);
}
```

### Unembedding Fonts

If the document uses embedded fonts, it means that all font data is stored in the document. The advantage is that the document is viewable regardless of whether the font is installed on the user's machine or not. But embedding fonts makes the document larger. The unembed fonts method removes all embedded fonts. Thus, the document size decreases but the document itself may become unreadable if the correct font is not installed.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void OptimizePdfDocumentWithUnembedFonts()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "OptimizeDocument.pdf"))
	{
		// Set UnembedFonts option
		var optimizeOptions = new Aspose.Pdf.Optimization.OptimizationOptions
		{
			UnembedFonts = true
		};

		Console.WriteLine("Start");

		// Optimize PDF document using OptimizationOptions
		document.OptimizeResources(optimizeOptions);

		// Save PDF document
		document.Save(dataDir + "OptimizeDocument_out.pdf");	
	}
	
    Console.WriteLine("Finished");

    // Calculate and display file sizes
    var fi1 = new FileInfo(dataDir + "OptimizeDocument.pdf");
    var fi2 = new FileInfo(dataDir + "OptimizeDocument_out.pdf");
    Console.WriteLine("Original file size: {0}. Reduced file size: {1}", fi1.Length, fi2.Length);
}
```

The optimization resources apply these methods to the document. If any of these methods are applied, the document size will most probably decrease. If none of these methods is applied, the document size will not change which is obvious.

## Additional Ways to Reduce the PDF Document Size

### Removing or Flattening Annotations

Annotations can be deleted when they are unnecessary. When they are needed but do not require additional editing, they can be flattened. Both of these techniques will reduce the file size.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void FlattenAnnotationsInPdfDocument()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "OptimizeDocument.pdf"))
	{
		// Flatten annotations
		foreach (var page in document.Pages)
		{
			foreach (var annotation in page.Annotations)
			{
				annotation.Flatten();
			}
		}

		// Save PDF document
		document.Save(dataDir + "OptimizeDocument_out.pdf");
	}
}
```

### Removing Form Fields

If the PDF document contains AcroForms, we can try to reduce the file size by flattening form fields.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void FlattenPdfForms()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Load source PDF form
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
	{
		// Flatten Forms
		if (document.Form.Fields.Lenght > 0)
		{
			foreach (var item in document.Form.Fields)
			{
				item.Flatten();
			}
		}

		// Save PDF document
		document.Save(dataDir + "FlattenForms_out.pdf");
	}
}
```

### Convert a PDF from RGB colorspace to grayscale

A PDF file comprises Text, Image, Attachment, Annotations, Graphs, and other objects. You may come across a requirement to convert a PDF from RGB colorspace to grayscale so that it would be faster while printing those PDF files. Also, when the file is converted to grayscale, the document size is reduced too, but it can just as well cause a decrease in the document quality. This feature is currently supported by the Pre-Flight feature of Adobe Acrobat, but when talking about Office automation, Aspose.PDF is an ultimate solution to provide such leverages for document manipulations. In order to accomplish this requirement, the following code snippet can be used.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertRgbToGrayScale()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
	{
		// Create RGB to DeviceGray conversion strategy
		var strategy = new Aspose.Pdf.RgbToDeviceGrayConversionStrategy();

		// Iterate through each page
		for (int idxPage = 1; idxPage <= document.Pages.Count; idxPage++)
		{
			// Get instance of particular page inside PDF
			var page = document.Pages[idxPage];

			// Convert the RGB colorspace image to GrayScale colorspace
			strategy.Convert(page);
		}

		// Save PDF document
		document.Save(dataDir + "TestGray_out.pdf");
	}
}
```

### FlateDecode Compression

{{% alert color="primary" %}}

This feature is supported by version 18.12 or greater.

{{% /alert %}}

Aspose.PDF for .NET provides support of FlateDecode compression for PDF Optimisation functionality. The following code snippet below shows how to use the option in Optimization to store images with **FlateDecode** compression:

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void OptimizeDocumentImagesWithFlateCompression()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "AddImage.pdf"))
    {
        // Initialize OptimizationOptions
        var optimizationOptions = new Aspose.Pdf.Optimization.OptimizationOptions();

        // To optimize images using FlateDecode compression, set optimization options to Flate
        optimizationOptions.ImageCompressionOptions.Encoding = Aspose.Pdf.Optimization.ImageEncoding.Flate;

        // Set optimization options
        document.OptimizeResources(optimizationOptions);

        // Save PDF document
        document.Save(dataDir + "OptimizeDocumentImagesWithFlateCompression_out.pdf");
    }
}
```

### **Store Image in XImageCollection**

Aspose.PDF for .NET provides the ability to store new images into **XImageCollection** with FlateDecode compression. To enable this option you can use **ImageFilterType.Flate** flag. The following code snippet shows how to use this functionality:

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddImageToPdfWithFlateCompression()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add a new page to the document
        var page = document.Pages.Add();

        // Open the image file stream
        using (var imageStream = new FileStream(dataDir + "aspose-logo.jpg", FileMode.Open))
        {
            // Add the image to the page resources with Flate compression
            page.Resources.Images.Add(imageStream, Aspose.Pdf.ImageFilterType.Flate);
        }

        // Get the added image
        var ximage = page.Resources.Images[page.Resources.Images.Count];

        // Save the current graphics state
        page.Contents.Add(new Aspose.Pdf.Operators.GSave());

        // Set coordinates for the image placement
        int lowerLeftX = 0;
        int lowerLeftY = 0;
        int upperRightX = 600;
        int upperRightY = 600;

        var rectangle = new Aspose.Pdf.Rectangle(lowerLeftX, lowerLeftY, upperRightX, upperRightY);
        var matrix = new Aspose.Pdf.Matrix(new double[]
        {
            rectangle.URX - rectangle.LLX, 0, 0, rectangle.URY - rectangle.LLY, rectangle.LLX, rectangle.LLY
        });

        // Use ConcatenateMatrix operator to define how the image must be placed
        page.Contents.Add(new Aspose.Pdf.Operators.ConcatenateMatrix(matrix));
        page.Contents.Add(new Aspose.Pdf.Operators.Do(ximage.Name));

        // Restore the graphics state
        page.Contents.Add(new Aspose.Pdf.Operators.GRestore());

        // Save the document
        document.Save(dataDir + "AddImageToPdfWithFlateCompression_out.pdf");
    }
}
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for .NET Library",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "sales",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "sales",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "sales",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "PDF Manipulation Library for .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/net/create-pdf-document/screenshot.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>
