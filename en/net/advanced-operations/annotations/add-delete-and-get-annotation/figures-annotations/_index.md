---
title: Add Figures Annotations using C#
linktitle: Figures Annotations
type: docs
weight: 30
url: /net/figures-annotation/
description: This article describes how to add, get, and delete figures annotations from your PDF document with Aspose.PDF for .NET
lastmod: "2023-09-12"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Add Figures Annotations using C#",
    "alternativeHeadline": "Enhance PDF Documents with Comprehensive Figure Annotations",
    "abstract": "Introducing the new Figures Annotations feature in Aspose.PDF for .NET, which empowers users to seamlessly add, retrieve, and delete various types of annotations including lines, squares, circles, polygons, and polylines in PDF documents. This functionality enhances document interactivity, allowing for clearer communication and visual markup directly within the PDF files. Optimize your PDF editing tasks with this robust annotation toolset tailored for developers using C#",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "pdf, figures annotations, line annotation, square annotation, circle annotation, polygon annotation, polyline annotation, free text annotation, ink annotation, Aspose.PDF for .NET",
    "wordcount": "2125",
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
    "url": "/net/figures-annotation/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/figures-annotation/"
    },
    "dateModified": "2024-11-25",
    "description": "This article describes how to add, get, and delete figures annotations from your PDF document with Aspose.PDF for .NET"
}
</script>

PDF document management app provides various tools for annotating documents. From the perspective of the internal structure of PDF, these tools are annotations. We support the following kinds of drawing tools.

* Line Annottaion - tool for drawing lines and arrows.
* Square Annotation - for drwaing squares and rectangles.
* Circle Annotation - for ovals and circles.
* FreeText Annotaion - for Callout comment.
* Polygon Annotation - for polygons and clouds.
* Polyline Annotation - for Connected Lines.

## Adding Shapes and Figures on Page

The approach to adding the annotation is typical for any of them.

The following code snippet also work with [Aspose.PDF.Drawing](/pdf/net/drawing/) library.

1. Load the PDF file or create new by [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).
1. Create the new annottaion and set parameters (new Rectangle, new Point, title, color, width etc).
1. Create the new [PopupAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/popupannotation/methods/index).
1. Link Popup annotation with original one.
1. Add annotation to the page

## Adding Lines or Arrows

The purpose of line annotation is to display a straightforward line or arrow on the page.
To create Line we need to new LineAnnotation object.  
The constructor of the LineAnnotation class takes four parameters:

* The page where the annotation will be added.
* The rectangle that defines the boundary of the annotation.
* The two points that define the start and end of the line.

Also we need to initialize some properties:

* `Title` - usually, it's the name of the user, who made this comment.
* `Subject` - can be any string, but in common cases it's a name of annotation.

To style our line we need to set color, width, starting style, and ending style. These properties control how the annotation will look and behave in the PDF viewer. For example, the `StartingStyle` and `EndingStyle` properties determine what kind of shape will be drawn at the ends of the line, such as an open arrow, a closed arrow, a circle, etc.

The following code snippet shows how to add Line Annotation to a PDF file:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET

private static void AddLineAnnotation()
{
    // The path to the documents directory
    string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
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

		// Save PDF document
		document.Save(dataDir + "AddLineAnnotation_out.pdf");
	}
}
```

## Adding Square or Circle

The [Square](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/squareannotation) and [Circle](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/circleannotation) annotations will display a rectangle or an ellipse on the page. When opened, they shall display a pop-up window containing the text of the associated note. Square annotations are like Circle annotations (instances of the Aspose. Pdf. Annotations. CircleAnnotation class) apart from the shape.

### Adding Circle annotation

To draw a new circle or ellipse annotation, we need to create a new CircleAnnotation object. The constructor of the `CircleAnnotation` class takes two parameters:

* The page where the annotation will be added.
* The rectangle that defines the boundary of the annotation.

Also we can sets some properties of the `CircleAnnotation` object, such as the title, color, interior color, opacity. These properties control how the annotation will look and behave in the PDF viewer. Here and further in the Square the `InteriorColor` color is the fill color and `Color` is border color.

### Adding Square annotation

Drawing a rectangle is the same as drawing a circle. The following code snippet shows how to add circle and square annotations to a PDF page.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET

private static void AddCircleAndSquareAnnotations()
{
    // The path to the documents directory
    string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "appartments.pdf"))
	{
		// Create Circle Annotation
		var circleAnnotation = new Aspose.Pdf.Annotations.CircleAnnotation(document.Pages[1], new Aspose.Pdf.Rectangle(270, 160, 483, 383))
		{
			Title = "John Smith",
			Subject = "Circle",
			Color = Aspose.Pdf.Color.Red,
			InteriorColor = Aspose.Pdf.Color.MistyRose,
			Opacity = 0.5,
			Popup = new Aspose.Pdf.Annotations.PopupAnnotation(document.Pages[1], new Aspose.Pdf.Rectangle(842, 316, 1021, 459))
		};

		// Create Square Annotation
		var squareAnnotation = new Aspose.Pdf.Annotations.SquareAnnotation(document.Pages[1], new Aspose.Pdf.Rectangle(67, 317, 261, 459))
		{
			Title = "John Smith",
			Subject = "Rectangle",
			Color = Aspose.Pdf.Color.Blue,
			InteriorColor = Aspose.Pdf.Color.BlueViolet,
			Opacity = 0.25,
			Popup = new Aspose.Pdf.Annotations.PopupAnnotation(document.Pages[1], new Aspose.Pdf.Rectangle(842, 196, 1021, 338))
		};

		// Add annotations to the page
		document.Pages[1].Annotations.Add(circleAnnotation);
		document.Pages[1].Annotations.Add(squareAnnotation);

		// Save PDF document
		document.Save(dataDir + "AddCircleAndSquareAnnotations_out.pdf");
	}
}
```

As an example, we will see the following result of adding Square and Circle annotations to a PDF document:

## Adding Polygon and Polyline Annotations

The Poly- tool allows you to create shapes and outlines with an arbitrary number of sides on the document.

**Polygon Annotations** represent polygons on a page. They can have any number of vertices connected by straight lines.
**Polyline Annotations** are also similar to polygons, the only difference is that the first and last vertices are not implicitly connected.

### Adding Polygon Annotation

PolygonAnnotation is responsible for polygon annotations. The constructor of the PolygonAnnotation class takes three parameters:

* The page where the annotation will be added.
* The rectangle that defines the boundary of the annotation.
* The array of points that define the vertices of the polygon.

`Color` and `InteriorColor` are used for the border and fill colors respectively.

### Adding Polyline Annotation

PolygonAnnotation is responsible for polygon annotations. The constructor of the PolygonAnnotation class takes three parameters:

* The page where the annotation will be added.
* The rectangle that defines the boundary of the annotation.
* The array of points that define the vertices of the polygon.

Instead `PolygonAnnotation` we can't fill this shape, so we don't need to use `InteriorColor`.

The following code snippet shows how to add Polygon and Polyline Annotations to a PDF file:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET

private static void AddPolygonAndPolylineAnnotations()
{
    // The path to the documents directory
    string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "appartments.pdf"))
	{
		// Create Polygon Annotation
		var polygonAnnotation = new Aspose.Pdf.Annotations.PolygonAnnotation(
			document.Pages[1],
			new Aspose.Pdf.Rectangle(270, 193, 571, 383),
			new Aspose.Pdf.Point[] {
				new Aspose.Pdf.Point(274, 381),
				new Aspose.Pdf.Point(555, 381),
				new Aspose.Pdf.Point(555, 304),
				new Aspose.Pdf.Point(570, 304),
				new Aspose.Pdf.Point(570, 195),
				new Aspose.Pdf.Point(274, 195)
			})
		{
			Title = "John Smith",
			Color = Aspose.Pdf.Color.Blue,
			InteriorColor = Aspose.Pdf.Color.BlueViolet,
			Opacity = 0.25,
			Popup = new Aspose.Pdf.Annotations.PopupAnnotation(document.Pages[1], new Aspose.Pdf.Rectangle(842, 196, 1021, 338))
		};

		// Create Polyline Annotation
		var polylineAnnotation = new Aspose.Pdf.Annotations.PolylineAnnotation(
			document.Pages[1],
			new Aspose.Pdf.Rectangle(270, 193, 571, 383),
			new Aspose.Pdf.Point[] {
				new Aspose.Pdf.Point(545, 150),
				new Aspose.Pdf.Point(545, 190),
				new Aspose.Pdf.Point(667, 190),
				new Aspose.Pdf.Point(667, 110),
				new Aspose.Pdf.Point(626, 111)
			})
		{
			Title = "John Smith",
			Color = Aspose.Pdf.Color.Red,
			Popup = new Aspose.Pdf.Annotations.PopupAnnotation(document.Pages[1], new Aspose.Pdf.Rectangle(842, 196, 1021, 338))
		};

		// Add annotations to the page
		document.Pages[1].Annotations.Add(polygonAnnotation);
		document.Pages[1].Annotations.Add(polylineAnnotation);

		// Save PDF document
		document.Save(dataDir + "AddPolygonAndPolylineAnnotations_out.pdf");
	}
}
```

## Getting Figures

All annotations are stored in the `Annotations` collection. Any annotation can introduce its type through `AnnotationType` property. Therefore, we can make a LINQ query to filter the desired annotations.

### Getting Line Annotations

The example below explains how to obtain all Line Annotations from the first page of the PDF document.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET

private static void ReadLineAnnotations()
{
    // The path to the documents directory
    string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "Appartments_mod.pdf"))
	{
		// Get all line annotations from the first page
		var lineAnnotations = document.Pages[1].Annotations
			.Where(a => a.AnnotationType == Aspose.Pdf.Annotations.AnnotationType.Line)
			.Cast<Aspose.Pdf.Annotations.LineAnnotation>();

		// Iterate through each line annotation and print its coordinates
		foreach (var la in lineAnnotations)
		{
			Console.WriteLine($"[{la.Starting.X},{la.Starting.Y}]-[{la.Ending.X},{la.Ending.Y}]");
		}
	}
}
```

### Getting Circle Annotations

The example below explains how to obtain all Polyline Annotations from the first page of the PDF document.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET

private static void ReadCircleAnnotations()
{
    // The path to the documents directory
    string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "Appartments_mod.pdf"))
	{
		// Get all circle annotations from the first page
		var circleAnnotations = document.Pages[1].Annotations
			.Where(a => a.AnnotationType == Aspose.Pdf.Annotations.AnnotationType.Circle)
			.Cast<Aspose.Pdf.Annotations.CircleAnnotation>();

		// Iterate through each circle annotation and print its rectangle
		foreach (var ca in circleAnnotations)
		{
			Console.WriteLine($"[{ca.Rect}]");
		}
	}
}
```

### Getting Square Annotations

The example below explains how to obtain all Polyline Annotations from the first page of the PDF document.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET

private static void ReadSquareAnnotations()
{
    // The path to the documents directory
    string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "Appartments_mod.pdf"))
	{
		// Get all square annotations from the first page
		var squareAnnotations = document.Pages[1].Annotations
			.Where(a => a.AnnotationType == Aspose.Pdf.Annotations.AnnotationType.Square)
			.Cast<Aspose.Pdf.Annotations.SquareAnnotation>();

		// Iterate through each square annotation and print its rectangle
		foreach (var sq in squareAnnotations)
		{
			Console.WriteLine($"[{sq.Rect}]");
		}
	}
}
```

### Getting Polyline Annotations

The example below explains how to obtain all Polyline Annotations from the first page of the PDF document.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET

private static void ReadPolylineAnnotations()
{
    // The path to the documents directory
    string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "Appartments_mod.pdf"))
	{
		// Get all polyline annotations from the first page
		var polyAnnotations = document.Pages[1].Annotations
			.Where(a => a.AnnotationType == Aspose.Pdf.Annotations.AnnotationType.PolyLine)
			.Cast<Aspose.Pdf.Annotations.PolylineAnnotation>();

		// Iterate through each polyline annotation and print its rectangle
		foreach (var pa in polyAnnotations)
		{
			Console.WriteLine($"[{pa.Rect}]");
		}
	}
}
```

### Getting Polygon Annotations

The example below explains how to obtain all Polygon Annotations from the first page of the PDF document.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET

private static void ReadPolygonAnnotations()
{
    // The path to the documents directory
    string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "Appartments_mod.pdf"))
	{
		// Get all polygon annotations from the first page
		var polyAnnotations = document.Pages[1].Annotations
			.Where(a => a.AnnotationType == Aspose.Pdf.Annotations.AnnotationType.Polygon)
			.Cast<Aspose.Pdf.Annotations.PolygonAnnotation>();

		// Iterate through each polygon annotation and print its rectangle
		foreach (var pa in polyAnnotations)
		{
			Console.WriteLine($"[{pa.Rect}]");
		}
	}
}
```

## Deleting Figures

The approach to removing annotation from PDF in pretty simple:

* Select annotations to delete (make some collection).
* Iterate over collection using a foreach loop, and deletes each annotation from the annotations collection using the Delete method.

### Deleting Line Annotation

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET

private static void DeleteLineAnnotations()
{
    // The path to the documents directory
    string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "Appartments_mod.pdf"))
	{
		// Get all line annotations from the first page
		var lineAnnotations = document.Pages[1].Annotations
			.Where(a => a.AnnotationType == Aspose.Pdf.Annotations.AnnotationType.Line)
			.Cast<Aspose.Pdf.Annotations.LineAnnotation>();

		// Iterate through each line annotation and delete it
		foreach (var la in lineAnnotations)
		{
			document.Pages[1].Annotations.Delete(la);
		}

		// Save PDF document
		document.Save(dataDir + "DeleteLineAnnotations_out.pdf");
	}
}
```

### Delete Circle and Square Annotations

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET

private static void DeleteCircleAndSquareAnnotations()
{
    // The path to the documents directory
    string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "Appartments_mod.pdf"))
	{
		// Get all circle and square annotations from the first page
		var figures = document.Pages[1].Annotations
			.Where(a =>
				a.AnnotationType == Aspose.Pdf.Annotations.AnnotationType.Circle
				|| a.AnnotationType == Aspose.Pdf.Annotations.AnnotationType.Square);

		// Iterate through each figure annotation and delete it
		foreach (var fig in figures)
		{
			document.Pages[1].Annotations.Delete(fig);
		}

		// Save PDF document
		document.Save(dataDir + "DeleteCircleAndSquareAnnotations_out.pdf");
	}
}
```

### Delete Polygon and Polyline Annotations

The following code snippet shows how Delete Polygon and Polyline Annotations from a PDF file.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET

private static void DeletePolylineAndPolygonAnnotations()
{
    // The path to the documents directory
    string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "Appartments_mod.pdf"))
	{
		// Get all polyline and polygon annotations from the first page
		var polyAnnotations = document.Pages[1].Annotations
			.Where(a => a.AnnotationType == Aspose.Pdf.Annotations.AnnotationType.PolyLine
						|| a.AnnotationType == Aspose.Pdf.Annotations.AnnotationType.Polygon);

		// Iterate through each polyline or polygon annotation and delete it
		foreach (var pa in polyAnnotations)
		{
			document.Pages[1].Annotations.Delete(pa);
		}

		// Save PDF document
		document.Save(dataDir + DeletePolylineAndPolygonAnnotations_out.pdf");
	}
}
```

## How to add Ink Annotation to PDF file

An Ink Annotation represents a freehand "scribble" composed of one or more disjoint paths. When opened, it shall display a pop-up window containing the text of the associated note.

The [InkAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/inkannotation) represents freehand scribble composed of one or more disjoint points. Please try using the following code snippet to add InkAnnotation in PDF document.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET

private static void AddInkAnnotation()
{
    // The path to the documents directory
    string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "appartments.pdf"))
	{
		var page = document.Pages[1];

		// Define the rectangle for the ink annotation
		var arect = new Aspose.Pdf.Rectangle(156.574, 521.316, 541.168, 575.703);

		// Create a list of ink paths
		IList<Aspose.Pdf.Point[]> inkList = new List<Aspose.Pdf.Point[]>();
		var arrpt = new[]
		{
			new Aspose.Pdf.Point(209.727, 542.263),
			new Aspose.Pdf.Point(209.727, 541.94),
			new Aspose.Pdf.Point(209.727, 541.616)
		};
		inkList.Add(arrpt);

		// Create the ink annotation
		var ia = new Aspose.Pdf.Annotations.InkAnnotation(page, arect, inkList)
		{
			Title = "John Smith",
			Subject = "Pencil",
			Color = Aspose.Pdf.Color.LightBlue,
			CapStyle = Aspose.Pdf.Annotations.CapStyle.Rounded,
			Opacity = 0.5
		};

		// Set the border for the annotation
		var border = new Aspose.Pdf.Annotations.Border(ia)
		{
			Width = 25
		};
		ia.Border = border;

		// Add the annotation to the page
		page.Annotations.Add(ia);

		// Save PDF document
		document.Save(dataDir + "AddInkAnnotation_out.pdf");
	}
}
```

### Set Line width of InkAnnotation

The width of [InkAnnottion](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/inkannotation) can be changed using LineInfo and Border objects.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET

private static void AddInkAnnotationWithLineWidth()
{
    // The path to the documents directory
    string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
	{
		document.Pages.Add();

		// Create a list of ink paths
		IList<Aspose.Pdf.Point[]> inkList = new List<Aspose.Pdf.Point[]>();

		// Define line information
		var lineInfo = new Aspose.Pdf.Facades.LineInfo
		{
			VerticeCoordinate = new float[] { 55, 55, 70, 70, 70, 90, 150, 60 },
			Visibility = true,
			LineColor = System.Drawing.Color.Red,
			LineWidth = 2
		};

		// Convert line coordinates to Aspose.Pdf.Point array
		int length = lineInfo.VerticeCoordinate.Length / 2;
		var gesture = new Aspose.Pdf.Point[length];
		for (int i = 0; i < length; i++)
		{
			gesture[i] = new Aspose.Pdf.Point(lineInfo.VerticeCoordinate[2 * i], lineInfo.VerticeCoordinate[2 * i + 1]);
		}

		// Add the gesture to the ink list
		inkList.Add(gesture);

		// Create the ink annotation
		var a1 = new Aspose.Pdf.Annotations.InkAnnotation(document.Pages[1], new Aspose.Pdf.Rectangle(100, 100, 300, 300), inkList)
		{
			Subject = "Test",
			Title = "Title",
			Color = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.Green)
		};

		// Set the border for the annotation
		var border = new Aspose.Pdf.Annotations.Border(a1)
		{
			Width = 3,
			Effect = Aspose.Pdf.Annotations.BorderEffect.Cloudy,
			Dash = new Aspose.Pdf.Annotations.Dash(1, 1),
			Style = Aspose.Pdf.Annotations.BorderStyle.Solid
		};
		a1.Border = border;

		// Add the annotation to the page
		document.Pages[1].Annotations.Add(a1);

		// Save PDF document
		document.Save(dataDir + "lnkAnnotationLineWidth_out.pdf");
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



### Delete Circle Annotation

The following code snippet shows how to Delete Circle Annotation from PDF file.

```csharp
public static void DeleteCircleAnnotation()
{
    // Open PDF document
    Document document = new Document(dataDir + "Appartments_mod.pdf");
    var circleAnnotations = document.Pages[1].Annotations
        .Where(a => a.AnnotationType == AnnotationType.Circle)
        .Cast<CircleAnnotation>();

    foreach (var ca in circleAnnotations)
    {
        document.Pages[1].Annotations.Delete(ca);
    }

    // Save PDF document
    document.Save(dataDir + "DeleteCircleAnnotation_out.pdf");
}
```
