---
title: PDF Square/Circle Annotations
linktitle: Square/Circle Annotations
type: docs
weight: 50
url: /net/add-square-and-circle-annotations/
description: This article describes how to add, get, and delete the Square and Circle annotations from your PDF document with Aspose.PDF for .NET
lastmod: "2020-12-25"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Square and Circle annotations shall display, respectively, a rectangle or an ellipse on the page. When opened, they shall display a pop-up window containing the text of the associated note.
Square annotations are like Circle annotations (instances of the Aspose.Pdf.Annotations.CircleAnnotation class) apart from the shape.

Steps for creating Square and Circle Annotations:

1. Load the PDF file - new [Document](https://apireference.aspose.com/pdf/net/aspose.pdf/document).
1. Create new [Circle Annotation](https://apireference.aspose.com/pdf/net/aspose.pdf.annotations/circleannotation) and set Circle parameters (new Rectangle, title, color, InteriorColor, Opacity).
1. Create a new [PopupAnnotation](https://apireference.aspose.com/pdf/net/aspose.pdf.annotations/popupannotation/methods/index). 
1. Next we need to create [Square Annotation](https://apireference.aspose.com/pdf/net/aspose.pdf.annotations/squareannotation).
1. Set the same Square parameters (new Rectangle, title, color, InteriorColor, Opacity).
1. After we need to Add Square and Circle Annotations to the page.

The following code snippet shows you how to add Circle Annotations in a PDF page.

```csharp
using Aspose.Pdf.Annotations;
using System;
using System.Linq;

namespace Aspose.Pdf.Examples.Advanced
{
    class ExampleCircleAnnotation
    {
        // The path to the documents directory.
        private const string _dataDir = "..\\..\\..\\..\\Samples";
        public static void AddCirlceAnnotation()
        {
            try
            {
                // Load the PDF file
                Document document = new Document(System.IO.Path.Combine(_dataDir, "appartments.pdf"));

                // Create Cirlce Annotation 
                var circleAnnotation = new CircleAnnotation(document.Pages[1], new Rectangle(270, 160, 483, 383))
                {
                    Title = "John Smith",
                    Color = Color.Red,
                    InteriorColor = Color.MistyRose,
                    Opacity = 0.5,
                    Popup = new PopupAnnotation(document.Pages[1], new Rectangle(842, 316, 1021, 459))
                };

                // Create Square Annotation 
                var squareAnnotation = new SquareAnnotation(document.Pages[1], new Rectangle(67, 317, 261, 459))
                {
                    Title = "John Smith",
                    Color = Color.Blue,
                    InteriorColor = Color.BlueViolet,
                    Opacity = 0.25,
                    Popup = new PopupAnnotation(document.Pages[1], new Rectangle(842, 196, 1021, 338))
                };

                // Add annotation to the page 
                document.Pages[1].Annotations.Add(circleAnnotation);
                document.Pages[1].Annotations.Add(squareAnnotation);
                document.Save(System.IO.Path.Combine(_dataDir, "appartments_mod.pdf"));
            }
            catch (Exception ex)
            {
                Console.WriteLine(ex.Message);
            }
        }
```

As an example, we will see the following result of adding Square and Circle annotations to a PDF document:

![Circle and Square Annotation demo](circle_demo.png)

Please try using the following code snippet to Get Circle Annotation from PDF document.

```csharp
public static void GetCircleAnnotation()
{
    // Load the PDF file
    Document document = new Document(System.IO.Path.Combine(_dataDir, "Appartments_mod.pdf"));
    var circleAnnotations = document.Pages[1].Annotations
        .Where(a => a.AnnotationType == AnnotationType.Line)
        .Cast<CircleAnnotation>();
    foreach (var ca in circleAnnotations)
    {
        Console.WriteLine($"[{ca.Rect}]");
    }
}
```

The following code snippet shows how to Delete Circle Annotation from PDF file.

```csharp
public static void DeleteCircleAnnotation()
{
    // Load the PDF file
    Document document = new Document(System.IO.Path.Combine(_dataDir, "Appartments_mod.pdf"));
    var circleAnnotations = document.Pages[1].Annotations
        .Where(a => a.AnnotationType == AnnotationType.Circle)
        .Cast<CircleAnnotation>();

    foreach (var ca in circleAnnotations)
    {
        document.Pages[1].Annotations.Delete(ca);
    }
    document.Save(System.IO.Path.Combine(_dataDir, "Appartments_del.pdf"));
}
```
