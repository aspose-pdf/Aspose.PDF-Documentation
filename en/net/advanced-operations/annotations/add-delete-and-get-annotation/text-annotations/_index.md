---
title: Using Text Annotation for PDF
linktitle: Text Annotation
type: docs
weight: 10
url: /net/text-annotation/
description: Aspose.PDF for .NET allows you to Add, Get, and Delete Text Annotation from your PDF document.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.5
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Using Text Annotation for PDF",
    "alternativeHeadline": "Enhance PDFs with Dynamic Text Annotations",
    "abstract": "Aspose.PDF for .NET introduces advanced text annotation capabilities, allowing users to effortlessly add, retrieve, or remove text annotations within PDF documents. This feature enhances the PDF editing process by enabling precise placement and customization of annotations, thereby improving document interaction and usability",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Text Annotation, PDF document generation, Aspose.PDF for .NET, Add Annotation, Delete Annotation, Free Text Annotation, Popup Annotation, StrikeOutAnnotation, AnnotationCollection, Aspose.PDF library",
    "wordcount": "2636",
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
    "url": "/net/text-annotation/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/text-annotation/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF for .NET allows you to Add, Get, and Delete Text Annotation from your PDF document."
}
</script>

## How to add Text Annotation into existing PDF file

The following code snippet also work with [Aspose.PDF.Drawing](/pdf/net/drawing/) library.

A Text Annotation is an annotation attached to a specific location in a PDF document. When closed, the annotation is displayed as an icon; when opened, it should display a pop-up window containing the note text in the font and size chosen by the reader.

Annotations are contained by the [Annotations](https://reference.aspose.com/pdf/net/aspose.pdf.annotations) collection of a particular Page. This collection contains the annotations for that individual page only; every page has its own Annotations collection.

To add an annotation to a particular page, add it to that page's Annotations collection with the [Add](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/annotationcollection/methods/add) method.

1. First, create an annotation that you want to add to the PDF.
1. Then open the input PDF.
1. Add the annotation to the [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) object's Annotations collection.

The following code snippet shows you how to add an annotation in a PDF page.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET

private static void AddTextAnnotationToPdf()
{
    // The path to the documents directory
    string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Load document
    using (var document = new Aspose.Pdf.Document(dataDir + "AddAnnotation.pdf"))
	{
		// Create text annotation
		var textAnnotation = new Aspose.Pdf.Annotations.TextAnnotation(document.Pages[1], new Aspose.Pdf.Rectangle(200, 400, 400, 600));
		textAnnotation.Title = "Sample Annotation Title";
		textAnnotation.Subject = "Sample Subject";
		textAnnotation.SetReviewState(Aspose.Pdf.Annotations.AnnotationState.Accepted);
		textAnnotation.Contents = "Sample contents for the annotation";
		textAnnotation.Open = true;
		textAnnotation.Icon = Aspose.Pdf.Annotations.TextIcon.Key;

		// Set border for the annotation
		var border = new Aspose.Pdf.Annotations.Border(textAnnotation);
		border.Width = 5;
		border.Dash = new Aspose.Pdf.Annotations.Dash(1, 1);
		textAnnotation.Border = border;
		textAnnotation.Rect = new Aspose.Pdf.Rectangle(200, 400, 400, 600);

		// Add annotation to the annotations collection of the page
		document.Pages[1].Annotations.Add(textAnnotation);

		// Save the updated document
		document.Save(dataDir + "AddAnnotation_out.pdf");
	}
}
```

## How to add Popup Annotation

A Pop-up Annotation displays text in a pop-up window for entry and editing. It shall not appear alone but is associated with a markup annotation, its parent annotation, and shall be used for editing the parent's text.

It shall have no appearance stream or associated actions of its own and shall be identified by the Popup entry in the parent's annotation dictionary.

The following code snippet shows you how to add [Popup Annotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/popupannotation) in a PDF page using an example of adding a parent's [Line annotation](/pdf/net/figures-annotation/#how-to-add-line-annotation-into-existing-pdf-file).

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET

private static void AddLineAnnotation()
{
    // The path to the documents directory
    string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Load the PDF file
    using (var document = new Aspose.Pdf.Document(dataDir + "Appartments.pdf"))
	{
		// Create Line Annotation
		var lineAnnotation = new Aspose.Pdf.Annotations.LineAnnotation(
			document.Pages[1],
			new Aspose.Pdf.Rectangle(550, 93, 562, 439),
			new Aspose.Pdf.Point(556, 99), new Aspose.Pdf.Point(556, 443))
		{
			Title = "John Smith",
			Color = Aspose.Pdf.Color.Red,
			Width = 3,
			StartingStyle = Aspose.Pdf.Annotations.LineEnding.OpenArrow,
			EndingStyle = Aspose.Pdf.Annotations.LineEnding.OpenArrow,
			Popup = new Aspose.Pdf.Annotations.PopupAnnotation(document.Pages[1], new Aspose.Pdf.Rectangle(842, 124, 1021, 266))
		};

		// Add annotation to the page
		document.Pages[1].Annotations.Add(lineAnnotation);

		// Save the updated document
		document.Save(dataDir + "Appartments_mod.pdf");
	}
}
```

## How to add (or Create) new Free Text Annotation

A free text annotation displays text directly on the page. The [PdfContentEditor.CreateFreeText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/createfreetext) method allows creating this type of annotation. In the following snippet, we add free text annotation above the first occurrence of the string.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET

private static void AddFreeTextAnnotationDemo()
{
    // The path to the documents directory
    string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Load the PDF file
    using (var document = new Aspose.Pdf.Document(dataDir + "pdf-sample.pdf"))
	{
		var pdfContentEditor = new Aspose.Pdf.Facades.PdfContentEditor(document);

		// Assuming tfa is an instance of TextFragmentAbsorber or similar
		var tfa = new Aspose.Pdf.Text.TextFragmentAbsorber();
		tfa.Visit(document.Pages[1]);

		if (tfa.TextFragments.Count <= 0)
		{
			return;
		}

		// Define the rectangle for the free text annotation
		var rect = new System.Drawing.Rectangle
		{
			X = (int)tfa.TextFragments[1].Rectangle.LLX,
			Y = (int)tfa.TextFragments[1].Rectangle.URY + 5,
			Height = 18,
			Width = 100
		};

		// Create free text annotation
		pdfContentEditor.CreateFreeText(rect, "Free Text Demo", 1); // Last param is the page number

		// Save the updated document
		pdfContentEditor.Save(dataDir + "pdf-sample-0.pdf");
	}
}
```

### Set Callout Property for FreeTextAnnotation

For a more flexible configuration of annotation in the PDF document, Aspose.PDF for .NET provides [Callout](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/freetextannotation/properties/callout) property of [FreeTextAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/freetextannotation) class which allows specifying Array of point of callout line. The following code snippet show, how to use this functionality:

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET

private static void AddFreeTextCalloutAnnotation()
{
    // The path to the documents directory
    string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Create a new PDF document
    using (var document = new Aspose.Pdf.Document())
	{
		var page = document.Pages.Add();

		// Create default appearance for the annotation
		var da = new Aspose.Pdf.Annotations.DefaultAppearance();
		da.TextColor = System.Drawing.Color.Red;
		da.FontSize = 10;

		// Create free text annotation with callout
		var fta = new Aspose.Pdf.Annotations.FreeTextAnnotation(page, new Aspose.Pdf.Rectangle(422.25, 645.75, 583.5, 702.75), da);
		fta.Intent = Aspose.Pdf.Annotations.FreeTextIntent.FreeTextCallout;
		fta.EndingStyle = Aspose.Pdf.Annotations.LineEnding.OpenArrow;
		fta.Callout = new Aspose.Pdf.Point[]
		{
			new Aspose.Pdf.Point(428.25, 651.75),
			new Aspose.Pdf.Point(462.75, 681.375),
			new Aspose.Pdf.Point(474, 681.375)
		};

		// Add the annotation to the page
		page.Annotations.Add(fta);

		// Set rich text for the annotation
		fta.RichText = "<body xmlns=\"http://www.w3.org/1999/xhtml\" xmlns:xfa=\"http://www.xfa.org/schema/xfa-data/1.0/\" xfa:APIVersion=\"Acrobat:11.0.23\" xfa:spec=\"2.0.2\"  style=\"color:#FF0000;font-weight:normal;font-style:normal;font-stretch:normal\"><p dir=\"ltr\"><span style=\"font-size:9.0pt;font-family:Helvetica\">This is a sample</span></p></body>";

		// Save the document
		document.Save(dataDir + "SetCalloutProperty.pdf");
	}
}
```

### Set Callout Property for XFDF File

If you use import from XFDF file please use callout-line name instead just Callout. The following code snippet shows, how to use this functionality:

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET

private static void ImportAnnotationsFromXfdf()
{
    // The path to the documents directory
    string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Load the PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "AddAnnotation.pdf"))
	{
		// Create an XFDF string builder
		var xfdf = new StringBuilder();
		xfdf.AppendLine("<?xml version=\"1.0\" encoding=\"UTF-8\"?><xfdf xmlns=\"http://ns.adobe.com/xfdf/\" xml:space=\"preserve\"><annots>");

		// Call the method to create XFDF content
		CreateXfdf(ref xfdf);

		xfdf.AppendLine("</annots></xfdf>");

		// Import annotations from the XFDF string
		document.ImportAnnotationsFromXfdf(new MemoryStream(Encoding.UTF8.GetBytes(xfdf.ToString())));

		// Save the updated document
		document.Save(dataDir + "SetCalloutPropertyXFDF.pdf");
	}
}
```

The following method is being used to CreateXfdf:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET

private static void CreateXfdf(ref StringBuilder pXfdf)
{
    pXfdf.Append("<freetext");
    pXfdf.Append(" page=\"0\"");
    pXfdf.Append(" rect=\"422.25,645.75,583.5,702.75\"");
    pXfdf.Append(" intent=\"FreeTextCallout\"");
    pXfdf.Append(" callout-line=\"428.25,651.75,462.75,681.375,474,681.375\"");
    pXfdf.Append(" tail=\"OpenArrow\"");
    pXfdf.AppendLine(">");
    pXfdf.Append("<contents-richtext><body ");
    pXfdf.Append(" style=\"font-size:10.0pt;text-align:left;color:#FF0000;font-weight:normal;font-style:normal;font-family:Helvetica;font-stretch:normal\">");
    pXfdf.Append("<p dir=\"ltr\">This is a sample</p>");
    pXfdf.Append("</body></contents-richtext>");
    pXfdf.AppendLine("<defaultappearance>/Helv 12 Tf 1 0 0 rg</defaultappearance>");
    pXfdf.AppendLine("</freetext>");
}
```

### Make Free Text Annotation Invisible

Sometimes, it is necessary to create a watermark that isn’t visible in the document when viewing it but should be visible when the document is printed. Use annotation flags for this purpose. The following code snippet shows how.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET

private static void AddInvisibleAnnotation()
{
    // The path to the documents directory
    string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Load the PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
	{
		// Create a free text annotation
		var annotation = new Aspose.Pdf.Annotations.FreeTextAnnotation(
			document.Pages[1],
			new Aspose.Pdf.Rectangle(50, 600, 250, 650),
			new Aspose.Pdf.Annotations.DefaultAppearance("Helvetica", 16, System.Drawing.Color.Red)
		);

		annotation.Contents = "ABCDEFG";
		annotation.Characteristics.Border = System.Drawing.Color.Red;
		annotation.Flags = Aspose.Pdf.Annotations.AnnotationFlags.Print | Aspose.Pdf.Annotations.AnnotationFlags.NoView;

		// Add the annotation to the page
		document.Pages[1].Annotations.Add(annotation);

		// Save the updated document
		document.Save(dataDir + "InvisibleAnnotation_out.pdf");
	}
}
```

### Set Formatting of FreeTextAnnotation

This part looks at how to format the text in a free text annotation.

Annotations are contained in a [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) object's [AnnotationCollection](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/annotationcollection) collection. When adding a [FreeTextAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/freetextannotation) to a PDF document, you can specify the formatting information such as font, size, color and so on using the [DefaultAppearance](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/defaultappearance/methods/index) class. It is also possible to specify the formatting information using the TextStyle property. Furthermore, you can update the formatting of any FreeTextAnnotation already in the PDF document.

The [TextStyle](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/textstyle) class supports working with the default style entry. This class allows you to set color, font size and font name:

- The FontName property gets or sets the font name (string).
- The FontSize property gets and sets the default text size (double).
- The System.Drawing.Color property gets and sets the text colour (color).
- The TextAlignment property gets and sets the annotation's text alignment (alignment).

The following code snippet shows how to add a FreeTextAnnotation with specific text formatting.

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET

private static void AddFreeAnnotation()
{
    // The path to the documents directory
    string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open document
    using (var document = new Aspose.Pdf.Document(dataDir + "SetFreeTextAnnotationFormatting.pdf"))
    {
        // Instantiate DefaultAppearance object
        var defaultAppearance = new Aspose.Pdf.Annotations.DefaultAppearance("Arial", 28, System.Drawing.Color.Red);

        // Create annotation
        var freetext = new Aspose.Pdf.Annotations.FreeTextAnnotation(document.Pages[1], new Aspose.Pdf.Rectangle(200, 400, 400, 600), defaultAppearance);

        // Specify the contents of annotation
        freetext.Contents = "Free Text";

        // Add annotation to annotations collection of page
        document.Pages[1].Annotations.Add(freetext);

        // Save the updated document
        document.Save(dataDir + "SetFreeTextAnnotationFormatting_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET

private static void AddFreeAnnotation(string fontName = "Arial", float fontSize = 28)
{
     // The path to the documents directory.
    string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();
	
    using (var document = new Aspose.Pdf.Document(dataDir + "SetFreeTextAnnotationFormatting.pdf"))
	{
		// Set default values
		var textColor = System.Drawing.Color.Red;
		var position = new Aspose.Pdf.Rectangle(200, 400, 400, 600);

		// Instantiate DefaultAppearance object
		Aspose.Pdf.Annotations.DefaultAppearance defaultAppearance = new(fontName, fontSize, textColor);
		// Create annotation
		var freetext = new Aspose.Pdf.Annotations.FreeTextAnnotation(document.Pages[1], position, defaultAppearance)
		{
			// Specify the contents of annotation
			Contents = "Free Text"
		};
		// Add anootation to annotations collection of page
		document.Pages[1].Annotations.Add(freetext);

		// Save the updated document
		document.Save(dataDir + "SetFreeTextAnnotationFormatting_out.pdf");
	}
}
```
{{< /tab >}}
{{< /tabs >}}

{{% alert color="primary" %}}

When you change the contents or text style of a free text annotation, the annotation's appearance is regenerated to reflect changes.

{{% /alert %}}

### Strike Out Words using StrikeOutAnnotation

Aspose.PDF for .NET allows you to add, delete and update annotations in PDF documents. One of the classes allows you to strike out annotations too. This is useful when you want to strike out one or more text fragments in a documect. Annotations are held in a [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) object's [AnnotationCollection](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/annotationcollection) collection. A class named [StrikeOutAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/strikeoutannotation) can be used to add strike out annotations to a PDF document.

To strike out a certain TextFragment:

1. Search for a TextFragment in the PDF file.
1. Get the TextFragment object's coordinates.
1. Use the coordinates to instantiate a StrikeOutAnnotation object.

The following code snippet shows how to search for a particular TextFragment and add a StrikeOutAnnotation to that object.

{{< gist "aspose-pdf" "7e1330795d76012fcb04248bb81d45b3" "Examples-CSharp-AsposePDF-Annotations-StrikeOutWords-StrikeOutWords.cs" >}}

{{% alert color="primary" %}}

This feature is supported by version 19.6 or greater.

{{% /alert %}}

## Delete All Annotations from Page of PDF File

A [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) object's [AnnotationCollection](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/annotationcollection) collection contains all the annotations for that particular page. To delete all the annotations from a page, call the *Delete* method of the AnnotationCollectoin collection.

The following code snippet shows you how to delete all the annotations from a particular page.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET

private static void DeleteAllAnnotationsFromPage()
{
    // The path to the documents directory
    string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Load the PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "DeleteAllAnnotationsFromPage.pdf"))
	{
		// Delete all annotations from the first page
		document.Pages[1].Annotations.Delete();

		// Save the updated document
		document.Save(dataDir + "DeleteAllAnnotationsFromPage_out.pdf");
	}
}
```

## Delete Particular Annotation from PDF File

{{% alert color="primary" %}}

You can check the quality of Aspose.PDF and get the results online at this link:
[products.aspose.app/pdf/annotation](https://products.aspose.app/pdf/annotation)

{{% /alert %}}

Aspose.PDF allows you to remove a particular Annotation from PDF file. This topic explains how.

To delete a particular annotation from a PDF, call the [AnnotationCollection collection's Delete method](https://reference.aspose.com/pdf/net/aspose.pdf.annotations.annotationcollection/delete/methods/1). This collection belongs to the [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) object. The Delete method requires the index of the annotation you want to delete. Then, save the updated PDF file. The following code snippet shows how to delete a particular annotation.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET

private static void DeleteParticularAnnotation()
{
    // The path to the documents directory
    string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Load the PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "DeleteParticularAnnotation.pdf"))
	{
		// Delete a particular annotation by index (e.g., the first annotation on the first page)
		document.Pages[1].Annotations.Delete(1);

		// Save the updated document
		document.Save(dataDir + "DeleteParticularAnnotation_out.pdf");
	}
}
```

## Get All Annotations from Page of PDF Document

Aspose.PDF allows you to get annotations from an entire document, or from a given page. To get all annotations from the page in a PDF document, loop through the [AnnotationCollection](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/annotationcollection) collection of desired page resources. The following code snippet shows you how to get all the annotations of a page.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET

private static void GetAllAnnotationsFromPage()
{
    // The path to the documents directory
    string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Load the PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "GetAllAnnotationsFromPage.pdf"))
	{
		// Loop through all the annotations on the first page
		foreach (Aspose.Pdf.Annotations.MarkupAnnotation annotation in document.Pages[1].Annotations)
		{
			// Get annotation properties
			Console.WriteLine("Title : {0} ", annotation.Title);
			Console.WriteLine("Subject : {0} ", annotation.Subject);
			Console.WriteLine("Contents : {0} ", annotation.Contents);
		}
	}
}
```

Please note that to get all annotations from the whole PDF, you have to loop through the document's PageCollection Class collection before navigating through the AnnotationCollection class collection. You can get each annotation of the collection in a base annotation type called MarkupAnnotation Class and then show its properties.

## Get Particular Annotation from PDF File

Annotations are associated with individual pages and stored in a [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) object's [AnnotationCOllection](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/annotationcollection) collection. To get a particular annotation, specify its index. This returns an [Annotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/annotation) object which needs to be cast to a particular annotation type, for example [TextAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/textannotation). The following code snippet shows how to get a particular annotation and its properties.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET

private static void GetParticularAnnotation()
{
    // The path to the documents directory
    string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Load the PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "GetParticularAnnotation.pdf"))
	{
		// Get a particular annotation by index (e.g., the first annotation on the first page)
		var textAnnotation = (Aspose.Pdf.Annotations.TextAnnotation)document.Pages[1].Annotations[1];

		// Get annotation properties
		Console.WriteLine("Title : {0} ", textAnnotation.Title);
		Console.WriteLine("Subject : {0} ", textAnnotation.Subject);
		Console.WriteLine("Contents : {0} ", textAnnotation.Contents);
	}
}
```

## Get Resource of Annotation

Aspose.PDF allows you to get a resource of annotation from an entire document, or from a given page. The following code snippet shows you how to get the resource of annotation as [FileSpecification](https://reference.aspose.com/pdf/net/aspose.pdf/filespecification) object of input PDF file.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET

private static void AddAndGetResourceOfAnnotation()
{
    // The path to the documents directory
    string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Load the PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "AddAnnotation.pdf"))
	{
		// Create a screen annotation with a SWF file
		var sa = new Aspose.Pdf.Annotations.ScreenAnnotation(document.Pages[1], new Aspose.Pdf.Rectangle(100, 400, 300, 600), dataDir + "AddSwfFileAsAnnotation.swf");
		document.Pages[1].Annotations.Add(sa);

		// Save the document with the new annotation
		document.Save(dataDir + "GetResourceOfAnnotation_Out.pdf");

		// Open the updated document
		var document1 = new Aspose.Pdf.Document(dataDir + "GetResourceOfAnnotation_Out.pdf");

		// Get the action of the annotation
		var action = (document1.Pages[1].Annotations[1] as Aspose.Pdf.Annotations.ScreenAnnotation).Action as Aspose.Pdf.Annotations.RenditionAction;

		// Get the rendition of the rendition action
		var rendition = action.Rendition;

		// Get the media clip
		var clip = (rendition as Aspose.Pdf.Annotations.MediaRendition).MediaClip;
		var data = (clip as Aspose.Pdf.Annotations.MediaClipData).Data;

		// Read the media data
		using (var ms = new MemoryStream())
		{
			byte[] buffer = new byte[1024];
			int read = 0;

			// Data of media are accessible in FileSpecification.Contents
			using (var source = data.Contents)
			{
				while ((read = source.Read(buffer, 0, buffer.Length)) > 0)
				{
					ms.Write(buffer, 0, read);
				}
			}

			Console.WriteLine(rendition.Name);
			Console.WriteLine(action.RenditionOperation);
		}
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
