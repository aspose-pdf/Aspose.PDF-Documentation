---
title: Add, Get or Delete Polygon/Polyline Annotations using Aspose.PDF for .NET
linktitle: Polygon/Polyline Annotations
type: docs
weight: 60
url: /net/add-polygon-and-polyline-annotations/
description: Aspose.PDF for .NET allows you to add, get, and delete the polygon and polyline annotations from your PDF document.
---

The Polyline tool allows you to create shapes and outlines with an arbitrary number of sides on the document.

**Polygon Annotations** represent polygons on a page. They can have any number of vertices connected by straight lines.

**Polyline Annotations** are also similar to polygons, the only difference is that the first and last vertices are not implicitly connected.

Steps with which we create Polygon and Polyline annotations:

1. Load the PDF file - new [Document](https://apireference.aspose.com/pdf/net/aspose.pdf/document).
1. Create new [Polygon Annotation](https://apireference.aspose.com/pdf/net/aspose.pdf.annotations/polygonannotation) and set Polygon parameters (new Rectangle, new Points, title, color, InteriorColor and Opacity).
1. Create a new [PopupAnnotation](https://apireference.aspose.com/pdf/net/aspose.pdf.annotations/popupannotation/methods/index). 
1. Next, Create a [PoliLine Annotation](https://apireference.aspose.com/pdf/net/aspose.pdf.annotations/polylineannotation) and repeat all actions.
1. After we can Add annotations to the page.

The following code snippet shows how to add Polygon and Polyline Annotations to a PDF file:

```csharp
using Aspose.Pdf.Annotations;
using System;
using System.Linq;

namespace Aspose.Pdf.Examples.Advanced
{
    class ExamplePolygonAnnotation
    {
        // The path to the documents directory.
        private const string _dataDir = "..\\..\\..\\..\\Samples";        
        public static void AddPolynnotation()
        {
            try
            {
                // Load the PDF file
                Document document = new Document(System.IO.Path.Combine(_dataDir, "appartments.pdf"));

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
                document.Save(System.IO.Path.Combine(_dataDir, "appartments_mod.pdf"));
            }
            catch (Exception ex)
            {
                Console.WriteLine(ex.Message);
            }
        }    
```

Please try using the following code snippet to Get Polygon and Polyline Annotations in PDF document.

```csharp
        public static void GetPolyAnnotation()
        {
            // Load the PDF file
            Document document = new Document(System.IO.Path.Combine(_dataDir, "Appartments_mod.pdf"));
            var polyAnnotations = document.Pages[1].Annotations
                .Where(a => a.AnnotationType == AnnotationType.PolyLine)
                .Cast<PolylineAnnotation>();
            foreach (var pa in polyAnnotations)
            {
                Console.WriteLine($"[{pa.Rect}]");
            }
        }        
        
```

The following code snippet shows how Delete Polygon and Polyline Annotations from a PDF file.

```csharp
        public static void DeletePolyAnnotation()
        {
            // Load the PDF file
            Document document = new Document(System.IO.Path.Combine(_dataDir, "Appartments_mod.pdf"));
            var polyAnnotations = document.Pages[1].Annotations
                            .Where(a => a.AnnotationType == AnnotationType.PolyLine)
                            .Cast<PolylineAnnotation>();

            foreach (var pa in polyAnnotations)
            {
                document.Pages[1].Annotations.Delete(pa);
            }
            document.Save(System.IO.Path.Combine(_dataDir, "Appartments_del.pdf"));
        }
    }
}
```
