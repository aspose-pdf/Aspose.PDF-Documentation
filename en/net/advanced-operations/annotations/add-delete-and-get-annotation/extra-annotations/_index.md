---
title: Extra Annotations using C#
linktitle: Extra Annotations
type: docs
weight: 60
url: /net/extra-annotations/
description: Learn how to add additional annotations to PDF files in .NET using Aspose.PDF for interactive document features.
lastmod: "2023-09-12"
sitemap:
    changefreq: "monthly"
    priority: 0.5
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Extra Annotations using C#",
    "alternativeHeadline": "Enhance PDF Annotations with C#",
    "abstract": "Introducing the Extra Annotations feature in C#, which allows developers to seamlessly add, retrieve, and remove various annotations from PDF documents. This robust functionality enhances PDF interaction by enabling precise text editing and document manipulation, including the ability to add caret and redaction annotations effectively. Optimize your PDF handling with these advanced capabilities designed for intuitive document management",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Extra Annotations, Caret Annotation, PDF document manipulation, Aspose.PDF for .NET, Redaction Annotation, Markup annotation, Delete Caret Annotation, Get Caret Annotation, StrikeOutAnnotation, PdfAnnotationEditor",
    "wordcount": "929",
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
    "url": "/net/extra-annotations/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/extra-annotations/"
    },
    "dateModified": "2024-11-25",
    "description": "This section describes how to add, get, and delete extra kinds of annotations from your PDF document."
}
</script>

## How to add Caret Annotation into existing PDF file

Caret Annotation is a symbol that indicates text editing. Caret Annotation is also markup annotation, so the Caret class derives from the Markup class and also provides functions to get or set properties of the Caret Annotation and reset the flow of the Caret Annotation appearance.

The following code snippet also work with [Aspose.PDF.Drawing](/pdf/net/drawing/) library.

Steps with which we create Caret annotation:

1. Load the PDF file - new [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).
1. Create new [Caret Annotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/caretannotation) and set Caret parameters (new Rectangle, title, Subject, Flags, color, width, StartingStyle and EndingStyle). This annotation is used to indicate the insertion of text.
1. Create new [Caret Annotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/caretannotation) and set Caret parameters (new Rectangle, title, Subject, Flags, color, width, StartingStyle and EndingStyle). This annotation is used to indicate the replacement of text.
1. Create new [StrikeOutAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/strikeoutannotation) and set parameters (new Rectangle, title, color, new QuadPoints and new points, Subject, InReplyTo,ReplyType).
1. After we can Add annotations to the page.

The following code snippet shows how to add Caret Annotation to a PDF file:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET

private static void AddCaretAnnotations()
{
    // The path to the documents directory
    string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "sample.pdf"))
	{
		// Create Caret Annotation for text insertion
		var caretAnnotation1 = new Aspose.Pdf.Annotations.CaretAnnotation(document.Pages[1], new Aspose.Pdf.Rectangle(299.988, 713.664, 308.708, 720.769))
		{
			Title = "Aspose User",
			Subject = "Inserted text 1",
			Flags = Aspose.Pdf.Annotations.AnnotationFlags.Print,
			Color = Aspose.Pdf.Color.Blue
		};

		// Create Caret Annotation for text replacement
		var caretAnnotation2 = new Aspose.Pdf.Annotations.CaretAnnotation(document.Pages[1], new Aspose.Pdf.Rectangle(361.246, 727.908, 370.081, 735.107))
		{
			Flags = Aspose.Pdf.Annotations.AnnotationFlags.Print,
			Subject = "Inserted text 2",
			Title = "Aspose User",
			Color = Aspose.Pdf.Color.Blue
		};

		// Create StrikeOut Annotation
		var strikeOutAnnotation = new Aspose.Pdf.Annotations.StrikeOutAnnotation(document.Pages[1],
			new Rectangle(318.407, 727.826, 368.916, 740.098))
		{
			Color = Aspose.Pdf.Color.Blue,
			QuadPoints = new[] {
				new Point(321.66, 739.416),
				new Point(365.664, 739.416),
				new Point(321.66, 728.508),
				new Point(365.664, 728.508)
			},
			Subject = "Cross-out",
			InReplyTo = caretAnnotation2,
			ReplyType = Aspose.Pdf.Annotations.ReplyType.Group
		};

		document.Pages[1].Annotations.Add(caretAnnotation1);
		document.Pages[1].Annotations.Add(caretAnnotation2);
		document.Pages[1].Annotations.Add(strikeOutAnnotation);

		// Save PDF document
		document.Save(dataDir + "AddCaretAnnotations_out.pdf");
	}
}
```

### Get Caret Annotation

Please try using the following code snippet to Get Caret Annotation in PDF document:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET

private static void GetCaretAnnotation()
{
    // The path to the documents directory
    string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "sample_caret.pdf"))
	{
		// Get Caret annotations from the first page
		var caretAnnotations = document.Pages[1].Annotations
			.Where(a => a.AnnotationType == Aspose.Pdf.Annotations.AnnotationType.Caret)
			.Cast<Aspose.Pdf.Annotations.CaretAnnotation>();

		// Iterate through the annotations and print their details
		foreach (var ca in caretAnnotations)
		{
			Console.WriteLine($"{ca.Rect}");
		}
	}
}
```

### Delete Caret Annotation

The following code snippet shows how Delete Caret Annotation from a PDF file.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET

private static void DeleteCaretAnnotation()
{
    // The path to the documents directory
    string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "sample_caret.pdf"))
	{
		// Get Caret annotations from the first page
		var caretAnnotations = document.Pages[1].Annotations
			.Where(a => a.AnnotationType == Aspose.Pdf.Annotations.AnnotationType.Caret)
			.Cast<Aspose.Pdf.Annotations.CaretAnnotation>();

		// Delete each Caret annotation
		foreach (var ca in caretAnnotations)
		{
			document.Pages[1].Annotations.Delete(ca);
		}

		// Save PDF document after deleting annotations
		document.Save(dataDir + "DeleteCaretAnnotation_out.pdf");
	}
}
```

## Redact certain page region with Redaction Annotation using Aspose.PDF for .NET

Aspose.PDF for .NET supports the feature to add as well as manipulate Annotations in an existing PDF file. Recently some of our customers posted a required to redact (remove text, image, etc elements from) a certain page region of PDF document. In order to fulfill this requirement, a class named RedactionAnnotation is provided, which can be used to redact certain page regions or it can be used to manipulate existing RedactionAnnotations and redact them (i.e. flatten annotation and remove the text under it).

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void RedactPage()
{
    // The path to the documents directory
    string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
	{
		// Create RedactionAnnotation instance for a specific page region
		var annot = new Aspose.Pdf.Annotations.RedactionAnnotation(document.Pages[1], new Aspose.Pdf.Rectangle(200, 500, 300, 600));
		annot.FillColor = Aspose.Pdf.Color.Green;
		annot.BorderColor = Aspose.Pdf.Color.Yellow;
		annot.Color = Aspose.Pdf.Color.Blue;

		// Text to be printed on the redact annotation
		annot.OverlayText = "REDACTED";
		annot.TextAlignment = Aspose.Pdf.HorizontalAlignment.Center;

		// Repeat Overlay text over the redact Annotation
		annot.Repeat = true;

		// Add annotation to the annotations collection of the first page
		document.Pages[1].Annotations.Add(annot);

		// Flattens annotation and redacts page contents (i.e., removes text and image under the redacted annotation)
		annot.Redact();

		// Save the result document
		document.Save(dataDir + "RedactPage_out.pdf");
	}
}
```

### Facades approach

Aspose.Pdf.Facades namespace also has a class named [PdfAnnotationEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor) which provides the feature to manipulate existing Annotations inside PDF file. This class contains a method named [RedactArea(..)](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor/methods/redactarea) which provides the capability to remove certain page regions.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void RedactPageWithFacadesApproach()
{
    // The path to the documents directory
    string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Create an instance of PdfAnnotationEditor
    using (var editor = new Aspose.Pdf.Facades.PdfAnnotationEditor())
	{
		// Redact a specific page region
		editor.RedactArea(1, new Aspose.Pdf.Rectangle(100, 100, 20, 70), System.Drawing.Color.White);

		// Bind the PDF document
		editor.BindPdf(dataDir + "input.pdf");

		// Save the result document
		editor.Save(dataDir + "FacadesApproach_out.pdf");
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
