---
title: PDF sticky Annotations using C#
linktitle: Sticky Annotation
type: docs
weight: 50
url: /net/sticky-annotations/
description: Learn how to create sticky annotations, such as notes and highlights, in PDFs using Aspose.PDF in .NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "PDF sticky Annotations using C#",
    "alternativeHeadline": "Add Sticky Watermark Annotations to PDF with C#",
    "abstract": "Introducing the new PDF Sticky Annotations feature in C#, which allows users to create and customize watermark annotations directly within PDF documents. This functionality supports setting specific text positions, controlling opacity, and efficiently reusing images, enhancing the overall document presentation while optimizing file sizes",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "PDF sticky annotations, C# sticky annotations, Watermark Annotation, Aspose.PDF.Drawing, PDF document generation, opacity property, XImageCollection, optimize PDF size",
    "wordcount": "453",
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
    "url": "/net/sticky-annotations/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/sticky-annotations/"
    },
    "dateModified": "2024-11-25",
    "description": "This topic about sticky annotations, as an example we shows the Watermark Annotation in the text."
}
</script>

The following code snippet also work with [Aspose.PDF.Drawing](/pdf/net/drawing/) library.

## Add Watermark Annotation

A watermark annotation shall be used to represent graphics that shall be printed at a fixed size and position on a page, regardless of the dimensions of the printed page.

You can add Watermark Text using [WatermarkAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/watermarkannotation) at a specific position of the PDF page. The opacity of Watermark can also be controlled by using opacity property.

Please check the following code snippet to add WatermarkAnnotation.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET

private static void AddWatermarkAnnotation()
{
    // The path to the documents directory
    string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open the document
    using (var document = new Aspose.Pdf.Document(dataDir + "source.pdf"))
	{
		// Load Page object to add Annotation
		var page = document.Pages[1];

		// Create Watermark Annotation
		var wa = new Aspose.Pdf.Annotations.WatermarkAnnotation(page, new Aspose.Pdf.Rectangle(100, 500, 400, 600));

		// Add annotation into Annotation collection of Page
		page.Annotations.Add(wa);

		// Create TextState for Font settings
		var ts = new Aspose.Pdf.Text.TextState();
		ts.ForegroundColor = Aspose.Pdf.Color.Blue;
		ts.Font = Aspose.Pdf.Text.FontRepository.FindFont("Times New Roman");
		ts.FontSize = 32;

		// Set opacity level of Annotation Text
		wa.Opacity = 0.5;

		// Add Text in Annotation
		wa.SetTextAndState(new string[] { "HELLO", "Line 1", "Line 2" }, ts);

		// Save the Document
		document.Save(dataDir + "Output_out.pdf");
	}
}
```

## Add Reference of a single Image multiple times in a PDF Document

Sometimes we have a requirement to use same image multiple times in a PDF document. Adding a new instance increases the resultant PDF document. We have added a new method XImageCollection.Add(XImage) in Aspose.PDF for .NET 17.1.0. This method allows to add reference to the same PDF object as original image that optimize the PDF Document size.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET

private static void AddWatermarkAnnotationWithImage()
{
    // The path to the documents directory
    string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Define the rectangle for the image
    var imageRectangle = new Aspose.Pdf.Rectangle(0, 0, 30, 15);

    // Open the document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
	{
		// Open the image stream
		using (var imageStream = File.Open(dataDir + "icon.png", FileMode.Open))
		{
			XImage image = null;

			// Iterate through each page in the document
			foreach (Page page in document.Pages)
			{
				// Create a Watermark Annotation
				var annotation = new Aspose.Pdf.Annotations.WatermarkAnnotation(page, page.Rect);
				XForm form = annotation.Appearance["N"];
				form.BBox = page.Rect;

				string name;

				// Add the image to the form resources if it hasn't been added yet
				if (image == null)
				{
					name = form.Resources.Images.Add(imageStream);
					image = form.Resources.Images[name];
				}
				else
				{
					name = form.Resources.Images.Add(image);
				}

				// Add operators to the form contents to place the image
				form.Contents.Add(new Aspose.Pdf.Operators.GSave());
				form.Contents.Add(new Aspose.Pdf.Operators.ConcatenateMatrix(new Aspose.Pdf.Matrix(imageRectangle.Width, 0, 0, imageRectangle.Height, 0, 0)));
				form.Contents.Add(new Aspose.Pdf.Operators.Do(name));
				form.Contents.Add(new Aspose.Pdf.Operators.GRestore());

				// Add the annotation to the page
				page.Annotations.Add(annotation, false);

				// Adjust the image rectangle size for the next iteration
				imageRectangle = new Aspose.Pdf.Rectangle(0, 0, imageRectangle.Width * 1.01, imageRectangle.Height * 1.01);
			}
		}

		// Save the document
		document.Save(dataDir + "output_out.pdf");
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
