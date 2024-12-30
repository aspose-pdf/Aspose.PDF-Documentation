---
title: PDF Highlight Annotation using C#
linktitle: Highlight Annotation
type: docs
weight: 20
url: /net/highlights-annotation/
description: Learn how to add highlights annotation to PDF documents in .NET using Aspose.PDF for text emphasis and review.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "PDF Highlight Annotation using C#",
    "alternativeHeadline": "PDF Annotations with Customizable Highlighting Options",
    "abstract": "The new PDF Highlight Annotation feature using C# allows users to seamlessly add and customize text markup annotations in their PDF documents. This functionality includes options for highlights, underlines, strikeouts, and jagged underlines, all of which can be edited for color, opacity, and metadata, enhancing document interactivity and clarity",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "PDF Highlight Annotation, C#, text markup annotation, highlight settings, strikethrough settings, underline settings, add annotation, delete annotation, Aspose.PDF.Drawing, markup annotations",
    "wordcount": "958",
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
    "url": "/net/highlights-annotation/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/highlights-annotation/"
    },
    "dateModified": "2024-11-25",
    "description": "The Markup annotations are presented in the text as highlights, underlines, strikeouts, or jagged underlines in the text of a document."
}
</script>

Text Markup Annotations shall appear as highlights, underlines, strikeouts, or jagged (“squiggly”) underlines in the text of a document. When opened, they shall display a pop-up window containing the text of the associated note.

The properties of the text markup annotations in the PDF document can be edited using the properties window provided in the PDF viewer control. The color, opacity, author, and subject of the text markup annotation can be modified.

Its is possible to get or set the settings of the highlight annotations using the highlightSettings property. The highlightSettings property is used to set the color, opacity, author, subject, modifiedDate and isLocked properties of the highlight annotations.

Also possible to get or set the settings of the strikethrough annotations using the strikethroughSettings property. The strikethroughSettings property is used to set the color, opacity, author, subject, modifiedDate, and isLocked properties of the strikethrough annotations.

The next feature is the ability to get or set the settings of the underline annotations using the underlineSettings property. The underlineSettings property is used to set the color, opacity, author, subject, modifiedDate, and isLocked properties of the underline annotations.

The following code snippet also work with [Aspose.PDF.Drawing](/pdf/net/drawing/) library.

## Add Text Markup Annotation

In order to add an Text Markup Annotation to the PDF document, we need to perform the following actions:

1. Load the PDF file - new [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) object.
1. Create annotations:
    - [HighlightAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/highlightannotation) and set parameters (title, color).
    - [StrikeOutAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/strikeoutannotation) and set parameters (title, color).
    - [SquigglyAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/squigglyannotation) and set parameters (title, color).
    - [UnderlineAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/underlineannotation) and set parameters (title, color).
1. After we should add all annotations to the page.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET

// The path to the documents directory.
private static void AddTextMarkupAnnotations()
{
    // The path to the documents directory
    string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Load the PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "sample.pdf"))
	{
		// Create a TextFragmentAbsorber to find the text "PDF"
		var tfa = new Aspose.Pdf.Text.TextFragmentAbsorber("PDF");
		tfa.Visit(document.Pages[1]);

		// Create annotations for the found text fragments
		var highlightAnnotation = new Aspose.Pdf.Annotations.HighlightAnnotation(document.Pages[1], tfa.TextFragments[1].Rectangle)
		{
			Title = "Aspose User",
			Color = Aspose.Pdf.Color.LightGreen
		};

		var strikeOutAnnotation = new Aspose.Pdf.Annotations.StrikeOutAnnotation(document.Pages[1], tfa.TextFragments[2].Rectangle)
		{
			Title = "Aspose User",
			Color = Aspose.Pdf.Color.Blue
		};

		var squigglyAnnotation = new Aspose.Pdf.Annotations.SquigglyAnnotation(document.Pages[1], tfa.TextFragments[3].Rectangle)
		{
			Title = "Aspose User",
			Color = Aspose.Pdf.Color.Red
		};

		var underlineAnnotation = new Aspose.Pdf.Annotations.UnderlineAnnotation(document.Pages[1], tfa.TextFragments[4].Rectangle)
		{
			Title = "Aspose User",
			Color = Aspose.Pdf.Color.Violet
		};

		// Add annotations to the page
		document.Pages[1].Annotations.Add(highlightAnnotation);
		document.Pages[1].Annotations.Add(squigglyAnnotation);
		document.Pages[1].Annotations.Add(strikeOutAnnotation);
		document.Pages[1].Annotations.Add(underlineAnnotation);

		// Save the updated document
		document.Save(dataDir + "sample_mod_out.pdf");
	}
}
```

If you want to highlight a multi-line fragment you should use advanced example:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET

/// <summary>
/// Advanced example for you want to highlight a multi-line fragment
/// </summary>
public static void AddHighlightAnnotationAdvanced()
{
    using (var document = new Aspose.Pdf.Document(dataDir + "sample_mod.pdf"))
	{
		var page = document.Pages[1];
		var tfa = new TextFragmentAbsorber(@"Adobe\W+Acrobat\W+Reader", new TextSearchOptions(true));
		tfa.Visit(page);
		foreach (var textFragment in tfa.TextFragments)
		{
			var highlightAnnotation = HighLightTextFragment(page, textFragment, Color.Yellow);
			page.Annotations.Add(highlightAnnotation);
		}
		document.Save(dataDir + "sample_mod_out.pdf");
	}
}

private static HighlightAnnotation HighLightTextFragment(Page page,
    TextFragment textFragment, Color color)
{
    if (textFragment.Segments.Count == 1)
    {
        return new HighlightAnnotation(page, textFragment.Segments[1].Rectangle)
        {
            Title = "Aspose User",
            Color = color,
            Modified = DateTime.Now,
            QuadPoints = new Point[]
            {
                new Point(textFragment.Segments[1].Rectangle.LLX, textFragment.Segments[1].Rectangle.URY),
                new Point(textFragment.Segments[1].Rectangle.URX, textFragment.Segments[1].Rectangle.URY),
                new Point(textFragment.Segments[1].Rectangle.LLX, textFragment.Segments[1].Rectangle.LLY),
                new Point(textFragment.Segments[1].Rectangle.URX, textFragment.Segments[1].Rectangle.LLY)
            }
        };
    }

    var offset = 0;
    var quadPoints = new Point[textFragment.Segments.Count * 4];
    foreach (var segment in textFragment.Segments)
    {
        quadPoints[offset + 0] = new Point(segment.Rectangle.LLX, segment.Rectangle.URY);
        quadPoints[offset + 1] = new Point(segment.Rectangle.URX, segment.Rectangle.URY);
        quadPoints[offset + 2] = new Point(segment.Rectangle.LLX, segment.Rectangle.LLY);
        quadPoints[offset + 3] = new Point(segment.Rectangle.URX, segment.Rectangle.LLY);
        offset += 4;
    }

    var llx = quadPoints.Min(pt => pt.X);
    var lly = quadPoints.Min(pt => pt.Y);
    var urx = quadPoints.Max(pt => pt.X);
    var ury = quadPoints.Max(pt => pt.Y);
    return new HighlightAnnotation(page, new Rectangle(llx, lly, urx, ury))
    {
        Title = "Aspose User",
        Color = color,
        Modified = DateTime.Now,
        QuadPoints = quadPoints
    };
}

/// <summary>
/// How to get a Highlighted Text
/// </summary>
public static void GetHighlightedText()
{
    // Load the PDF file
    using (var document = new Aspose.Pdf.Document(dataDir + "sample_mod.pdf"))
	{
		var highlightAnnotations = document.Pages[1].Annotations
			.Where(a => a.AnnotationType == AnnotationType.Highlight)
			.Cast<HighlightAnnotation>();
		foreach (var ta in highlightAnnotations)
		{
			Console.WriteLine($"[{ta.GetMarkedText()}]");
		}
	}
}
```

## Get Text Markup Annotation

Please try using the following code snippet to Get Text Markup Annotation from PDF document.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET

public static void GetTextMarkupAnnotation()
{
    // Load the PDF file
    using (var document = new Aspose.Pdf.Document(dataDir + "sample_mod.pdf"))
	{
		var textMarkupAnnotations = document.Pages[1].Annotations
			.Where(a => a.AnnotationType == AnnotationType.Highlight
			|| a.AnnotationType == AnnotationType.Squiggly)
			.Cast<TextMarkupAnnotation>();
		foreach (var ta in textMarkupAnnotations)
		{
			Console.WriteLine($"[{ta.AnnotationType} {ta.Rect}]");
		}
	}
}
```

## Delete Text Markup Annotation

The following code snippet shows how to Delete Text Markup Annotation from PDF file.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET

public static void DeleteTextMarkupAnnotation()
{
    // Load the PDF file
    using (var document = new Aspose.Pdf.Document(dataDir + "sample_mod.pdf"))
	{
		var textMarkupAnnotations = document.Pages[1].Annotations
			.Where(a => a.AnnotationType == AnnotationType.Highlight
			||a.AnnotationType == AnnotationType.Squiggly)
			.Cast<TextMarkupAnnotation>();
		foreach (var ta in textMarkupAnnotations)
		{
			document.Pages[1].Annotations.Delete(ta);
		}
		document.Save(dataDir + "sample_del_out.pdf");
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
