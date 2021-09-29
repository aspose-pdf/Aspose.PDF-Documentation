---
title: PDF Text Markup Annotation using C#
linktitle: Text Markup Annotation
type: docs
weight: 70
url: /net/text-markup-annotation/
description: The Markup annotations are presented in the text as highlights, underlines, strikeouts, or jagged underlines in the text of a document.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Text Markup Annotations shall appear as highlights, underlines, strikeouts, or jagged (“squiggly”) underlines in the text of a document. When opened, they shall display a pop-up window containing the text of the associated note.

The properties of the text markup annotations in the PDF document can be edited using the properties window provided in the PDF viewer control. The color, opacity, author, and subject of the text markup annotation can be modified.

Its is possible to get or set the settings of the highlight annotations using the highlightSettings property. The highlightSettings property is used to set the color, opacity, author, subject, modifiedDate and isLocked properties of the highlight annotations.

Also possible to get or set the settings of the strikethrough annotations using the strikethroughSettings property. The strikethroughSettings property is used to set the color, opacity, author, subject, modifiedDate, and isLocked properties of the strikethrough annotations.

The next feature is the ability to get or set the settings of the underline annotations using the underlineSettings property. The underlineSettings property is used to set the color, opacity, author, subject, modifiedDate, and isLocked properties of the underline annotations.

## Add Text Markup Annotation

In order to add an Text Markup Annotation to the PDF document, we need to perform the following actions:

1. Load the PDF file - new [Document](https://apireference.aspose.com/pdf/net/aspose.pdf/document) object.
1. Create annotations:
    - [HighlightAnnotation](https://apireference.aspose.com/pdf/net/aspose.pdf.annotations/highlightannotation) and set parameters (title, color).
    - [StrikeOutAnnotation](https://apireference.aspose.com/pdf/net/aspose.pdf.annotations/strikeoutannotation) and set parameters (title, color).
    - [SquigglyAnnotation](https://apireference.aspose.com/pdf/net/aspose.pdf.annotations/squigglyannotation) and set parameters (title, color).
    - [UnderlineAnnotation](https://apireference.aspose.com/pdf/net/aspose.pdf.annotations/underlineannotation) and set parameters (title, color).
1. After we should add all annotations to the page.

```csharp
using Aspose.Pdf.Annotations;
using Aspose.Pdf.Text;
using System;
using System.Linq;

namespace Aspose.Pdf.Examples.Advanced
{
    class ExampleTextMarkupAnnotation
    {
        // The path to the documents directory.
        private const string _dataDir = "..\\..\\..\\..\\Samples";

        public static void AddTextMarkupAnnotation()
        {
            try
            {
                // Load the PDF file
                Document document = new Document(System.IO.Path.Combine(_dataDir, "sample.pdf"));
                var tfa = new Aspose.Pdf.Text.TextFragmentAbsorber("PDF");
                tfa.Visit(document.Pages[1]);

                //Create annotations
                HighlightAnnotation highlightAnnotation = new HighlightAnnotation(document.Pages[1],
                   tfa.TextFragments[1].Rectangle )
                {
                    Title = "Aspose User",
                    Color = Color.LightGreen
                };

                StrikeOutAnnotation strikeOutAnnotation = new StrikeOutAnnotation(
                   document.Pages[1],
                   tfa.TextFragments[2].Rectangle)
                {
                    Title = "Aspose User",
                    Color = Color.Blue
                };
                SquigglyAnnotation squigglyAnnotation = new SquigglyAnnotation(document.Pages[1],
                    tfa.TextFragments[3].Rectangle)
                {
                    Title = "Aspose User",
                    Color = Color.Red
                };
                UnderlineAnnotation underlineAnnotation = new UnderlineAnnotation(document.Pages[1],
                    tfa.TextFragments[4].Rectangle)
                {
                    Title = "Aspose User",
                    Color = Color.Violet
                };
                // Add annotation to the page
                document.Pages[1].Annotations.Add(highlightAnnotation);
                document.Pages[1].Annotations.Add(squigglyAnnotation);
                document.Pages[1].Annotations.Add(strikeOutAnnotation);
                document.Pages[1].Annotations.Add(underlineAnnotation);
                document.Save(System.IO.Path.Combine(_dataDir, "sample_mod.pdf"));
            }
            catch (Exception ex)
            {
                Console.WriteLine(ex.Message);
            }
        }
```

If you want to highlight a multi-line fragment you should use advanced example:

```csharp
        /// <summary>
        /// Advanced example for you want to highlight a multi-line fragment
        /// </summary>
        public static void AddHighlightAnnotationAdvanced()
        {
            var document = new Document(System.IO.Path.Combine(_dataDir, "sample_mod.pdf"));
            var page = document.Pages[1];
            var tfa = new TextFragmentAbsorber(@"Adobe\W+Acrobat\W+Reader", new TextSearchOptions(true));
            tfa.Visit(page);
            foreach (var textFragment in tfa.TextFragments)
            {
                var highlightAnnotation = HighLightTextFragment(page, textFragment, Color.Yellow);
                page.Annotations.Add(highlightAnnotation);
            }
            document.Save(System.IO.Path.Combine(_dataDir, "sample_mod.pdf"));
        }
        private static HighlightAnnotation HighLightTextFragment(Aspose.Pdf.Page page,
            TextFragment textFragment, Color color)
        {
            if (textFragment.Segments.Count == 1)
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
            Document document = new Document(System.IO.Path.Combine(_dataDir, "sample_mod.pdf"));
            var highlightAnnotations = document.Pages[1].Annotations
                .Where(a => a.AnnotationType == AnnotationType.Highlight)
                .Cast<HighlightAnnotation>();
            foreach (var ta in highlightAnnotations)
            {
                Console.WriteLine($"[{ta.GetMarkedText()}]");
            }
        }
```
## Get Text Markup Annotation

Please try using the following code snippet to Get Text Markup Annotation from PDF document.

```csharp       
        public static void GetTextMarkupAnnotation()
        {
            // Load the PDF file
            Document document = new Document(System.IO.Path.Combine(_dataDir, "sample_mod.pdf"));
            var textMarkupAnnotations = document.Pages[1].Annotations
                .Where(a => a.AnnotationType == AnnotationType.Highlight
                || a.AnnotationType == AnnotationType.Squiggly)
                .Cast<TextMarkupAnnotation>();
            foreach (var ta in textMarkupAnnotations)
            {
                Console.WriteLine($"[{ta.AnnotationType} {ta.Rect}]");
            }
        }
```
## Delete Text Markup Annotation

The following code snippet shows how to Delete Text Markup Annotation from PDF file.

```csharp
        public static void DeleteTextMarkupAnnotation()
        {
            // Load the PDF file
            Document document = new Document(System.IO.Path.Combine(_dataDir, "sample_mod.pdf"));
            var textMarkupAnnotations = document.Pages[1].Annotations
                .Where(a => a.AnnotationType == AnnotationType.Highlight
                || a.AnnotationType == AnnotationType.Squiggly)
                .Cast<TextMarkupAnnotation>();
            foreach (var ta in textMarkupAnnotations)
            {
                document.Pages[1].Annotations.Delete(ta);
            }
            document.Save(System.IO.Path.Combine(_dataDir, "sample_del.pdf"));
        }
    }
}
```
