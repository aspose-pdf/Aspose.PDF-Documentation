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
    "alternativeHeadline": "How to add Figures Annotations in PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "pdf, c#, figures annotations, polygon annotation, line annotation, square annotation, circle annotation",
    "wordcount": "302",
    "proficiencyLevel":"Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF Doc Team",
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
    "dateModified": "2022-02-04",
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
// Load the PDF file
Document document = new Document(_dataDir + "Appartments.pdf");

// Create Line Annotation
var lineAnnotation = new LineAnnotation(
    document.Pages[1],
    new Rectangle(550, 93, 562, 439),
    new Point(556, 99), new Point(556, 443))
{
    Title = "John Smith",
    Color = Color.Red,
    Width = 3,
    StartingStyle = LineEnding.OpenArrow,
    EndingStyle = LineEnding.OpenArrow,
    Popup = new PopupAnnotation(document.Pages[1], new Rectangle(842, 124, 1021, 266))
};

// Add annotation to the page
document.Pages[1].Annotations.Add(lineAnnotation);
document.Save(_dataDir + "Appartments_mod.pdf");
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
var dataDir = "<path-to-file>";
// Load the PDF file
Document document = new Document(dataDir + "appartments.pdf");

// Create Cirlce Annotation
var circleAnnotation = new CircleAnnotation(document.Pages[1], new Rectangle(270, 160, 483, 383))
{
    Title = "John Smith",
    Subject = "Circle",
    Color = Color.Red,
    InteriorColor = Color.MistyRose,
    Opacity = 0.5,        
    Popup = new PopupAnnotation(document.Pages[1], new Rectangle(842, 316, 1021, 459))
};

// Create Square Annotation
var squareAnnotation = new SquareAnnotation(document.Pages[1], new Rectangle(67, 317, 261, 459))
{
    Title = "John Smith",
    Subject = "Rectangle",
    Color = Color.Blue,
    InteriorColor = Color.BlueViolet,
    Opacity = 0.25,
    Popup = new PopupAnnotation(document.Pages[1], new Rectangle(842, 196, 1021, 338))
};

// Add annotation to the page
document.Pages[1].Annotations.Add(circleAnnotation);
document.Pages[1].Annotations.Add(squareAnnotation);
document.Save(dataDir + "appartments_mod.pdf");
```

As an example, we will see the following result of adding Square and Circle annotations to a PDF document:

![Circle and Square Annotation demo](circle_demo.png)

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
// Load the PDF file
Document document = new Document(dataDir + "appartments.pdf");

// Create Polygon Annotation
var polygonAnnotation = new PolygonAnnotation(document.Pages[1],
    new Rectangle(270, 193, 571, 383),
    new Point[] {
        new Point(274, 381),
        new Point(555, 381),
        new Point(555, 304),
        new Point(570, 304),
        new Point(570, 195),
        new Point(274, 195)})
{
    Title = "John Smith",
    Color = Color.Blue,
    InteriorColor = Color.BlueViolet,
    Opacity = 0.25,
    Popup = new PopupAnnotation(document.Pages[1], new Rectangle(842, 196, 1021, 338))
};

// Create PoliLine Annotation
var polylineAnnotation = new PolylineAnnotation(document.Pages[1],
    new Rectangle(270, 193, 571, 383),
    new Point[] {
        new Point(545,150),
        new Point(545,190),
        new Point(667,190),
        new Point(667,110),
        new Point(626,111)
        })
{
    Title = "John Smith",
    Color = Color.Red,
    Popup = new PopupAnnotation(document.Pages[1], new Rectangle(842, 196, 1021, 338))
};

// Add annotation to the page
document.Pages[1].Annotations.Add(polygonAnnotation);
document.Pages[1].Annotations.Add(polylineAnnotation);
document.Save(dataDir + "appartments_mod.pdf");
```

## Getting Figures

All annotations are stored in the `Annotations` collection. Any annotation can introduce its type through `AnnotationType` property. Therefore, we can make a LINQ query to filter the desired annotations.

### Getting Line Annotations

The example below explains how to obtain all Line Annotations from the first page of the PDF document.

```csharp
// Load the PDF file
Document document = new Document(_dataDir + "Appartments_mod.pdf");
var lineAnnotations = document.Pages[1].Annotations
    .Where(a => a.AnnotationType == AnnotationType.Line)
    .Cast<LineAnnotation>();
foreach (var la in lineAnnotations)
{
    Console.WriteLine($"[{la.Starting.X},{la.Starting.Y}]-[{la.Ending.X},{la.Ending.Y}]");
}   
```

### Getting Circle Annotations

The example below explains how to obtain all Polyline Annotations from the first page of the PDF document.

```csharp
// Load the PDF file
Document document = new Document(_dataDir + "Appartments_mod.pdf");
var circleAnnotations = document.Pages[1].Annotations
    .Where(a => a.AnnotationType == AnnotationType.Line)
    .Cast<CircleAnnotation>();
foreach (var ca in circleAnnotations)
{
    Console.WriteLine($"[{ca.Rect}]");
}   
```

### Getting Square Annotations

The example below explains how to obtain all Polyline Annotations from the first page of the PDF document.

```csharp
// Load the PDF file
Document document = new Document(_dataDir + "Appartments_mod.pdf");
var squareAnnotations = document.Pages[1].Annotations
    .Where(a => a.AnnotationType == AnnotationType.Square)
    .Cast<SquareAnnotation>();
foreach (var sq in squareAnnotations)
{
    Console.WriteLine($"[{sq.Rect}]");
}
```

### Getting Polyline Annotations

The example below explains how to obtain all Polyline Annotations from the first page of the PDF document.

```csharp
// Load the PDF file
Document document = new Document(_dataDir + "Appartments_mod.pdf");
var polyAnnotations = document.Pages[1].Annotations
    .Where(a => a.AnnotationType == AnnotationType.PolyLine)
    .Cast<PolylineAnnotation>();
foreach (var pa in polyAnnotations)
{
    Console.WriteLine($"[{pa.Rect}]");
}     
```

### Getting Polygon Annotations

The example below explains how to obtain all Polygon Annotations from the first page of the PDF document.

```csharp
Document document = new Document(_dataDir + "Appartments_mod.pdf");
var polyAnnotations = document.Pages[1].Annotations
    .Where(a => a.AnnotationType == AnnotationType.Polygon)
    .Cast<PolygonAnnotation>();
foreach (var pa in polyAnnotations)
{
    Console.WriteLine($"[{pa.Rect}]");
} 
```

## Deleting Figures

The approach to removing annotation from PDF in pretty simple:

* Select annotations to delete (make some collection).
* Iterate over collection using a foreach loop, and deletes each annotation from the annotations collection using the Delete method.

### Deleting Line Annotation

```csharp
// Load the PDF file
Document document = new Document(_dataDir + "Appartments_mod.pdf");
var lineAnnotations = document.Pages[1].Annotations
    .Where(a => a.AnnotationType == AnnotationType.Line)
    .Cast<LineAnnotation>();

foreach (var la in lineAnnotations)
{
    document.Pages[1].Annotations.Delete(la);
}
```

### Delete Circle and Square Annotations

```csharp
// Load the PDF file
Document document = new Document(_dataDir + "Appartments_mod.pdf");
var figures = document.Pages[1].Annotations
    .Where(a =>
        a.AnnotationType == AnnotationType.Circle
        || a.AnnotationType == AnnotationType.Square);

foreach (var fig in figures)
{
    document.Pages[1].Annotations.Delete(fig);
}
document.Save(_dataDir + "Appartments_del.pdf");
```

### Delete Polygon and Polyline Annotations

The following code snippet shows how Delete Polygon and Polyline Annotations from a PDF file.

```csharp
// Load the PDF file
Document document = new Document(_dataDir + "Appartments_mod.pdf");
var polyAnnotations = document.Pages[1].Annotations
                .Where(a => a.AnnotationType == AnnotationType.PolyLine
                || a.AnnotationType == AnnotationType.Polygon);

foreach (var pa in polyAnnotations)
{
    document.Pages[1].Annotations.Delete(pa);
}

// Save result file
document.Save(_dataDir + "Appartments_del.pdf");
```

## How to add Ink Annotation to PDF file

An Ink Annotation represents a freehand "scribble" composed of one or more disjoint paths. When opened, it shall display a pop-up window containing the text of the associated note.

The [InkAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/inkannotation) represents freehand scribble composed of one or more disjoint points. Please try using the following code snippet to add InkAnnotation in PDF document.

```csharp
// Load the PDF file
Document document = new Document(_dataDir + "appartments.pdf");
Page page = document.Pages[1];

Rectangle arect = new Rectangle(156.574, 521.316, 541.168, 575.703);

IList<Point[]> inkList = new List<Point[]>();
Point[] arrpt = new[]
{
    new Point(209.727,542.263),
    new Point(209.727,541.94),
    new Point(209.727,541.616)
};
inkList.Add(arrpt);

InkAnnotation ia = new InkAnnotation(page, arect, inkList)
{
    Title = "John Smith",
    Subject = "Pencil",
    Color = Color.LightBlue,
    CapStyle = CapStyle.Rounded,
    Opacity = 0.5
};
Border border = new Border(ia)
{
    Width = 25
};
ia.Border = border;
page.Annotations.Add(ia);

// Save output file
document.Save(_dataDir + "appartments_mod.pdf");
```

### Set Line width of InkAnnotation

The width of [InkAnnottion](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/inkannotation) can be changed using LineInfo and Border objects.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

Document doc = new Document();
doc.Pages.Add();
IList<Point[]> inkList = new List<Point[]>();
LineInfo lineInfo = new LineInfo();
lineInfo.VerticeCoordinate = new float[] { 55, 55, 70, 70, 70, 90, 150, 60 };
lineInfo.Visibility = true;
lineInfo.LineColor = System.Drawing.Color.Red;
lineInfo.LineWidth = 2;
int length = lineInfo.VerticeCoordinate.Length / 2;
Aspose.Pdf.Point[] gesture = new Aspose.Pdf.Point[length];
for (int i = 0; i < length; i++)
{
   gesture[i] = new Aspose.Pdf.Point(lineInfo.VerticeCoordinate[2 * i], lineInfo.VerticeCoordinate[2 * i + 1]);
}

inkList.Add(gesture);
InkAnnotation a1 = new InkAnnotation(doc.Pages[1], new Aspose.Pdf.Rectangle(100, 100, 300, 300), inkList);
a1.Subject = "Test";
a1.Title = "Title";
a1.Color = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.Green);
Border border = new Border(a1);
border.Width = 3;
border.Effect = BorderEffect.Cloudy;
border.Dash = new Dash(1, 1);
border.Style = BorderStyle.Solid;
doc.Pages[1].Annotations.Add(a1);

// Save output file
doc.Save(dataDir + "lnkAnnotationLineWidth_out.pdf");
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
    // Load the PDF file
    Document document = new Document(dataDir + "Appartments_mod.pdf");
    var circleAnnotations = document.Pages[1].Annotations
        .Where(a => a.AnnotationType == AnnotationType.Circle)
        .Cast<CircleAnnotation>();

    foreach (var ca in circleAnnotations)
    {
        document.Pages[1].Annotations.Delete(ca);
    }

    // Save result file
    document.Save(dataDir + "Appartments_del.pdf");
}
```
