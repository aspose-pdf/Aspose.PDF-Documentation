---
title: Adding Images and Text 
type: docs
weight: 10
url: /net/adding-images-and-text-using-pdffilemend-class/
description: This section explains how to Add Images and Text using PdfFileMend class.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Adding Images and Text",
    "alternativeHeadline": "Enhance PDF by Adding Images and Text Precisely",
    "abstract": "Enhance your PDF documents effortlessly with the new PdfFileMend class, which allows you to add images and text at specified locations within existing PDFs. Utilize the intuitive AddImage and AddText methods to integrate various image formats and formatted text seamlessly, ensuring precision in placement and page selection. Streamline your PDF manipulation tasks with the ability to customize image overlays and text wrapping, making your documents visually compelling and informative",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1324",
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
    "url": "/net/adding-images-and-text-using-pdffilemend-class/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/adding-images-and-text-using-pdffilemend-class/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF can perform not only simple and easy tasks but also cope with more complex goals. Check the next section for advanced users and developers."
}
</script>

[PdfFileMend](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend) class can help you add images and text in an existing PDF document, at a specified location. It provides two methods with the names [AddImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend/methods/addimage/index) and [AddText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend/methods/addtext/index). [AddImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend/methods/addimage/index) method allows you to add images of type JPG, GIF, PNG, and BMP. [AddText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend/methods/addtext/index) method takes an argument of type [FormattedText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formattedtext) class and adds it in the existing PDF file. The images and text can be added in a rectangle region specified by the coordinates of lower left and upper right points. While adding images you can specify either image file path or a stream of an image file. In order to specify the page number at which the image or text needs to be added, both of these methods provide an argument of page number. So, you can not only add the images and text at the specified location but also on a specified page as well.

Images are an important part of the contents of a PDF document. Manipulating images in an existing PDF file is a common requirement of the people working with PDF files. In this article, we’ll explore how the images can be manipulated, in an existing PDF file, with the help of [Aspose.Pdf.Facades namespace](https://reference.aspose.com/pdf/net/aspose.pdf.facades) of [Aspose.PDF for .NET](/pdf/net/). All the image related operations of [Aspose.Pdf.Facades namespace](https://reference.aspose.com/pdf/net/aspose.pdf.facades) have been consolidated in this article.

## Implementation details

[Aspose.Pdf.Facades namespace](https://reference.aspose.com/pdf/net/aspose.pdf.facades) allows you to add new images in an existing PDF file. You can also replace or remove an existing image. A PDF file can also be converted to images. You can either convert each individual page into a single image or a complete PDF file into one image. It allows you to formats i.e. JPEG, BMP, PNG and TIFF etc. You can extract the images from a PDF file as well. You can use four classes of [Aspose.Pdf.Facades namespace](https://reference.aspose.com/pdf/net/aspose.pdf.facades) to implement these operations i.e. [PdfFileMend](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend), [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor), [PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor) and [PdfConverter](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter).

## Image Operations

In this section, we’ll have a detailed look into these image operations. We’ll also see the code snippets to show the use of the related classes and methods. First of all, let's have a look at adding an image in an existing PDF file. We can use [AddImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend/methods/addimage/index) method of [PdfFileMend](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend) class to add a new image. Using this method, you can not only specify the page number on which you want to add the image, but also the location of the image can be specified.

## Add Image in an Existing PDF File (Facades)

You can use [AddImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend/methods/addimage) method of the [PdfFileMend](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend) class. The [AddImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend/methods/addimage) method requires the image to be added, the page number at which the image needs to be added and the coordinate information. After that, save the updated PDF file using [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/close) method.

In the following example, we add image to the page using imageStream:

```csharp
private static void AddImage01()
{
	var dataDir = RunExamples.GetDataDir_AsposePdf_Images();  // Using dynamic path

	// Create Document and PdfFileMend objects using 'using' block to ensure proper disposal
	using (var document = new Aspose.Pdf.Document(dataDir + "AddImage.pdf"))
	using (var mender = new Aspose.Pdf.Facades.PdfFileMend())
	{
		// Load image into stream
		using (var imageStream = System.IO.File.OpenRead(dataDir + "AddImage.png"))
		{
			mender.BindPdf(document);
			mender.AddImage(imageStream, 1, 10, 650, 110, 750); // Add image to first page

			// Save the updated PDF file with '_out' suffix
			mender.Save(dataDir + "AddImage_out.pdf");
		}
	}
}
```

![Add Image](/pdf/net/images/add_image1.png)

With the help of [CompositingParameters](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffilemend/addimage/methods/1), we can superimpose one image on top of another:

```csharp
private static void AddImage02()
{
	var dataDir = RunExamples.GetDataDir_AsposePdf_Images();  // Using dynamic path

	// Create Document and PdfFileMend objects using 'using' block to ensure proper disposal
	using (var document = new Aspose.Pdf.Document(dataDir + "AddImage.pdf"))
	using (var mender = new Aspose.Pdf.Facades.PdfFileMend())
	{
		// Load image into stream
		using (var imageStream = System.IO.File.OpenRead(dataDir + "AddImage.png"))
		{
			mender.BindPdf(document);

			int pageNum = 1;
			int lowerLeftX = 10;
			int lowerLeftY = 650;
			int upperRightX = 110;
			int upperRightY = 750;

			// Use compositing parameters for the image
			var compositingParameters = new Aspose.Pdf.CompositingParameters(Aspose.Pdf.BlendMode.Multiply);

			mender.AddImage(imageStream, pageNum, lowerLeftX, lowerLeftY, upperRightX, upperRightY, compositingParameters);

			// Save the output file with '_out' suffix
			mender.Save(dataDir + "AddImage_out.pdf");
		}
	}
}
```

![Add Image](/pdf/net/images/add_image2.png)

There are several ways to store an image in PDF file. We will demonstrate one of them in the following example:

```csharp
private static void AddImage03()
{
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();  // Using dynamic path

    // Create Document and PdfFileMend objects using 'using' block to ensure proper disposal
    using (var document = new Aspose.Pdf.Document(dataDir + "AddImage.pdf"))
    using (var mender = new Aspose.Pdf.Facades.PdfFileMend())
    {
        // Load image into stream
        using (var imageStream = System.IO.File.OpenRead(dataDir + "AddImage.png"))
        {
            mender.BindPdf(document);

            int pageNum = 1;
            int lowerLeftX = 10;
            int lowerLeftY = 650;
            int upperRightX = 110;
            int upperRightY = 750;

            // Use compositing parameters with BlendMode.Exclusion and ImageFilterType.Flate
            var compositingParameters = new Aspose.Pdf.CompositingParameters(
                Aspose.Pdf.BlendMode.Exclusion,
                Aspose.Pdf.ImageFilterType.Flate);

            mender.AddImage(imageStream, pageNum, lowerLeftX, lowerLeftY, upperRightX, upperRightY, compositingParameters);

            // Save the output file with '_out' suffix
            mender.Save(dataDir + "AddImage_out.pdf");
        }
    }
}
```

```csharp
private static void AddImage04()
{
	var dataDir = RunExamples.GetDataDir_AsposePdf_Images();  // Using dynamic path

	// Create Document and PdfFileMend objects using 'using' block to ensure proper disposal
	using (var document = new Aspose.Pdf.Document(dataDir + "AddImage.pdf"))
	using (var mender = new Aspose.Pdf.Facades.PdfFileMend())
	{
		// Load image into stream
		using (var imageStream = System.IO.File.OpenRead(dataDir + "AddImage.png"))
		{
			mender.BindPdf(document);

			int pageNum = 1;
			int lowerLeftX = 10;
			int lowerLeftY = 650;
			int upperRightX = 110;
			int upperRightY = 750;

			// Use compositing parameters with BlendMode.Multiply, ImageFilterType.Flate and false
			var compositingParameters = new Aspose.Pdf.CompositingParameters(
				Aspose.Pdf.BlendMode.Multiply,
				Aspose.Pdf.ImageFilterType.Flate,
				false);

			mender.AddImage(imageStream, pageNum, lowerLeftX, lowerLeftY, upperRightX, upperRightY, compositingParameters);

			// Save the output file with '_out' suffix
			mender.Save(dataDir + "AddImage_outp.pdf");
		}
	}
}
```

## Add Text in an Existing PDF File (facades)

We can add text in several ways. Consider the first. We take the [FormattedText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formattedtext) and add it to the Page. After, we indicate the coordinates of the lower left corner, and then we add our text to the Page.

```csharp
private static void AddText01()
{
	var dataDir = RunExamples.GetDataDir_AsposePdf_Images();  // Using dynamic path

	// Create PdfFileMend object using 'using' block to ensure proper disposal
	using (var mender = new Aspose.Pdf.Facades.PdfFileMend())
	{
		mender.BindPdf(dataDir + "AddImage.pdf");

		// Create formatted text
		var message = new Aspose.Pdf.Facades.FormattedText("Welcome to Aspose!");

		// Add text to the first page at position (10, 750)
		mender.AddText(message, 1, 10, 750);

		// Save the output file with '_out' suffix
		mender.Save(dataDir + "AddText_out.pdf");
	}
}
```

Check how it's looks:

![Add Text](/pdf/net/images/add_text.png)

The second way to add [FormattedText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formattedtext). Additionally, we indicate a rectangle in which our text should fit.

```csharp
private static void AddText02()
{
	var dataDir = RunExamples.GetDataDir_AsposePdf_Images();  // Using dynamic path

	// Create PdfFileMend object using 'using' block to ensure proper disposal
	using (var mender = new Aspose.Pdf.Facades.PdfFileMend())
	{
		mender.BindPdf(dataDir + "AddImage.pdf");

		// Create formatted text
		var message = new Aspose.Pdf.Facades.FormattedText("Welcome to Aspose! Welcome to Aspose!");

		// Add text to the first page at the specified position with wrapping
		mender.AddText(message, 1, 10, 700, 55, 810);

		// Set word wrapping mode to wrap by words
		mender.WrapMode = Aspose.Pdf.Facades.WordWrapMode.ByWords;

		// Save the output file with '_out' suffix
		mender.Save(dataDir + "AddText_out.pdf");
	}
}
```

The third example provides the ability to Add Text to specified pages. In our example, let's add a caption on pages 1 and 3 of the document.

```csharp
private static void AddText03()
{
	var dataDir = RunExamples.GetDataDir_AsposePdf_Images();  // Using dynamic path

	// Create Document object and add pages
	using (var document = new Aspose.Pdf.Document(dataDir + "AddImage.pdf"))
	{
		document.Pages.Add();
		document.Pages.Add();
		document.Pages.Add();

		// Create PdfFileMend object using 'using' block to ensure proper disposal
		using (var mender = new Aspose.Pdf.Facades.PdfFileMend())
		{
			mender.BindPdf(document);

			// Create formatted text
			var message = new Aspose.Pdf.Facades.FormattedText("Welcome to Aspose!");

			// Specify the pages where text should be added
			int[] pageNums = new int[] { 1, 3 };

			// Add text to the specified pages at the specified coordinates
			mender.AddText(message, pageNums, 10, 750, 310, 760);

			// Save the output file with '_out' suffix
			mender.Save(dataDir + "AddText_out.pdf");
		}
	}
}
```
