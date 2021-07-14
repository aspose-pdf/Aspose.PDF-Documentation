---
title: PDF Line Annotation | C#
linktitle: Line Annotation
type: docs
weight: 40
url: /net/line-annotation/
description: This article shows how you can add, get, and delete line annotation from your PDF document.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

The purpose of a Line Annotation is to display a single straight line on the page. When opened, it shall display a pop-up window containing the text of the associated note.
This feature additional entries specific to a line annotation. These entries are encrypted in the form of letters, for example, LL, BS, IC, and so on.

Also, Line Annotation can include a caption to a line annotation, which is specified by setting Cap to `true`.

## How to add Line Annotation into existing PDF file

The next feature allows the effect of applying a caption to a Line Annotation that has a leader offset.
Also, this kind of annotation allows you to define Line ending styles.

Steps with which we create an Line annotation:

1. Load the PDF file - new [Document](https://apireference.aspose.com/pdf/net/aspose.pdf/document).
1. Create new [Line Annotation](https://apireference.aspose.com/pdf/net/aspose.pdf.annotations/lineannotation/methods/index) and set Line parameters (new Rectangle, new Point, title, color, width, StartingStyle and EndingStyle).
1. Create a new [PopupAnnotation](https://apireference.aspose.com/pdf/net/aspose.pdf.annotations/popupannotation/methods/index).
1. After we can Add annotation to the page

The following code snippet shows how to add Line Annotation to a PDF file:

```csharp
using Aspose.Pdf.Annotations;
using System;
using System.Linq;

namespace Aspose.Pdf.Examples.Advanced
{
    class ExampleLineAnnotation
    {
        // The path to the documents directory.
        private const string _dataDir = "..\\..\\..\\..\\Samples";
        public static void AddLineAnnotation()
        {
            try
            {
                // Load the PDF file
                Document document = new Document(System.IO.Path.Combine(_dataDir, "Appartments.pdf"));

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
                document.Save(System.IO.Path.Combine(_dataDir, "Appartments_mod.pdf"));
            }
            catch (Exception ex)
            {
                Console.WriteLine(ex.Message);
            }
        }
```
## Get Line Annotation

Please try using the following code snippet to Get Line Annotation in PDF document.

```csharp
        public static void GetLineAnnotation()
        {
            // Load the PDF file
            Document document = new Document(System.IO.Path.Combine(_dataDir, "Appartments_mod.pdf"));
            var lineAnnotations = document.Pages[1].Annotations
                .Where(a => a.AnnotationType == AnnotationType.Line)
                .Cast<LineAnnotation>();
            foreach (var la in lineAnnotations)
            {
                Console.WriteLine($"[{la.Starting.X},{la.Starting.Y}]-[{la.Ending.X},{la.Ending.Y}]");
            }
        }
```
## Delete Line Annotation

The following code snippet shows how Delete Line Annotation from a PDF file.

```csharp
        public static void DeleteLineAnnotation()
        {
            // Load the PDF file
            Document document = new Document(System.IO.Path.Combine(_dataDir, "Appartments_mod.pdf"));
            var lineAnnotations = document.Pages[1].Annotations
                .Where(a => a.AnnotationType == AnnotationType.Line)
                .Cast<LineAnnotation>();

            foreach (var la in lineAnnotations)
            {
                document.Pages[1].Annotations.Delete(la);
            }
            document.Save(System.IO.Path.Combine(_dataDir, "Appartments_del.pdf"));
        }
    }
}
```
