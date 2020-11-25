---
title: Add Caret Annotation
type: docs
weight: 90
url: /net/add-caret-annotation/
---

Caret Annotation is a symbol that indicates text editing. Caret Annotation is also markup annotation, so the Caret class derives from the Markup class and also provides functions to get or set properties of the Caret Annotation and reset the flow of the Caret Annotation appearance.

Steps with which we create an Line annotation:
1. Load the PDF file - new [Document](https://apireference.aspose.com/pdf/net/aspose.pdf/document).
1. Create new [Caret Annotation](https://apireference.aspose.com/pdf/net/aspose.pdf.annotations/caretannotation) and set Caret parameters (new Rectangle, title, Subject, Flags, color, width, StartingStyle and EndingStyle). This annotation is used to indicate the insertion of text.
1. Create new [Caret Annotation](https://apireference.aspose.com/pdf/net/aspose.pdf.annotations/caretannotation) and set Caret parameters (new Rectangle, title, Subject, Flags, color, width, StartingStyle and EndingStyle). This annotation is used to indicate the replacement of text.
1.  Create new [strikeOutAnnotation](https://apireference.aspose.com/pdf/net/aspose.pdf.annotations/strikeoutannotation) and set parameters (new Rectangle, title, color, new QuadPoints and new points, Subject, InReplyTo,ReplyType).
1. After we can Add annotations to the page.

The following code snippet shows how to add Caret Annotation to a PDF file:

```csharp
using Aspose.Pdf.Annotations;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Aspose.Pdf.Examples.Advanced
{
    class ExampleCaretAnnotation
    {
        // The path to the documents directory.
        private const string _dataDir = "..\\..\\..\\..\\Samples";     
        public static void AddCaretAnnotation()
        {
            // Load the PDF file
            Document document = new Document(System.IO.Path.Combine(_dataDir, "sample.pdf"));
            // This annotation is used to indicate the insertion of text
            var caretAnnotation1 = new CaretAnnotation(document.Pages[1], new Rectangle(299.988, 713.664, 308.708, 720.769))
            {
                Title = "Aspose User",
                Subject = "Inserted text 1",
                Flags = AnnotationFlags.Print,
                Color = Color.Blue
            };
            // This annotation is used to indicate the replacement of text
            var caretAnnotation2 = new CaretAnnotation(document.Pages[1], new Rectangle(361.246, 727.908, 370.081, 735.107))
            {
                Flags = AnnotationFlags.Print,
                Subject = "Inserted text 2",
                Title = "Aspose User",
                Color = Color.Blue
            };

            var strikeOutAnnotation = new StrikeOutAnnotation(document.Pages[1],
                new Rectangle(318.407, 727.826, 368.916, 740.098))
            {
                Color = Color.Blue,
                QuadPoints = new[] {
                new Point(321.66, 739.416),
                new Point(365.664, 739.416),
                new Point(321.66, 728.508),
                new Point(365.664, 728.508)
            },
                Subject = "Cross-out",
                InReplyTo = caretAnnotation2,
                ReplyType = ReplyType.Group                
            };

            document.Pages[1].Annotations.Add(caretAnnotation1);
            document.Pages[1].Annotations.Add(caretAnnotation2);
            document.Pages[1].Annotations.Add(strikeOutAnnotation);

            document.Save(System.IO.Path.Combine(_dataDir, "sample_caret.pdf"));
        }
```
Please try using the following code snippet to Get Caret  Annotation in PDF document.
        
```csharp        
        public static void GetCaretAnnotation()
        {
            // Load the PDF file
            Document document = new Document(System.IO.Path.Combine(_dataDir, "sample_caret.pdf"));
            var caretAnnotations = document.Pages[1].Annotations
                .Where(a => a.AnnotationType == AnnotationType.Caret)
                .Cast<CaretAnnotation>();
            foreach (var ca in caretAnnotations)
            {
                Console.WriteLine($"{ca.Rect}");
            }
        }
```
The following code snippet shows how Delete Caret Annotation from a PDF file.
```csharp
        public static void DeleteCaretAnnotation()
        {
            // Load the PDF file
            Document document = new Document(System.IO.Path.Combine(_dataDir, "sample_caret.pdf"));
            var caretAnnotations = document.Pages[1].Annotations
                .Where(a => a.AnnotationType == AnnotationType.Caret)
                .Cast<CaretAnnotation>();

            foreach (var ca in caretAnnotations)            
            {                                
                document.Pages[1].Annotations.Delete(ca);
            }
            document.Save(System.IO.Path.Combine(_dataDir, "sample_caret_del.pdf"));
        }
    }
}

```
