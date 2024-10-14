---
title: הדגשת תגובה ב-PDF באמצעות C#
linktitle: הדגשת תגובה
type: docs
weight: 20
url: /net/highlights-annotation/
description: תגובות העריכה מוצגות בטקסט כהדגשות, קווים תחתונים, קווים חוצים או קווים מקוטעים בטקסט של מסמך.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "הדגשת תגובות ב-PDF באמצעות C#",
    "alternativeHeadline": "איך להוסיף תגובות הדגשה ב-PDF",
    "author": {
        "@type": "Person",
        "name":"אנסטסיה הולוב",
        "givenName": "אנסטסיה",
        "familyName": "הולוב",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "יצירת מסמכי PDF",
    "keywords": "pdf, c#, הדגשת תגובה, תגובת עריכת טקסט",
    "wordcount": "302",
    "proficiencyLevel":"מתחיל",
    "publisher": {
        "@type": "Organization",
        "name": "צוות מסמכי Aspose.PDF",
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
                "contactType": "מכירות",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "מכירות",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "מכירות",
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
    "dateModified": "2022-02-04",
    "description": "תגובות העריכה מוצגות בטקסט כהדגשות, קווים תחתונים, קווים חוצים או קווים מקוטעים בטקסט של מסמך."
}
</script>
הערות סימון טקסט יופיעו כהדגשות, קווים תחתונים, קווי חוצה או קווים מקומטים בטקסט של מסמך. כאשר ייפתחו, הן יציגו חלון קופץ המכיל את טקסט ההערה המקושרת.

ניתן לערוך את המאפיינים של הערות סימון הטקסט במסמך PDF באמצעות חלון המאפיינים שמסופק בשליטת צפיין ה-PDF. ניתן לשנות את הצבע, השקיפות, המחבר והנושא של הערת סימון הטקסט.

ניתן לקבל או להגדיר את ההגדרות של הערות ההדגשה באמצעות המאפיין highlightSettings. מאפיין highlightSettings משמש להגדרת הצבע, השקיפות, המחבר, הנושא, תאריך השינוי והאם הערה נעולה.

כמו כן ניתן לקבל או להגדיר את ההגדרות של הערות הקו החוצה באמצעות המאפיין strikethroughSettings. מאפיין strikethroughSettings משמש להגדרת הצבע, השקיפות, המחבר, הנושא, תאריך השינוי והאם הערה נעולה.

התכונה הבאה היא היכולת לקבל או להגדיר את ההגדרות של הערות הקו התחתון באמצעות המאפיין underlineSettings.
התכונה הבאה היא היכולת לקבל או להגדיר את ההגדרות של ההדגשות בקו תחתון באמצעות המאפיין underlineSettings.

קטע הקוד הבא עובד גם עם ספריית [Aspose.PDF.Drawing](/pdf/net/drawing/).

## הוספת אנוטציה לסימון טקסט

כדי להוסיף אנוטציה לסימון טקסט למסמך PDF, עלינו לבצע את הפעולות הבאות:

1. טעינת קובץ ה-PDF - אובייקט [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) חדש.
1. יצירת אנוטציות:
    - [HighlightAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/highlightannotation) והגדרת פרמטרים (כותרת, צבע).
    - [StrikeOutAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/strikeoutannotation) והגדרת פרמטרים (כותרת, צבע).
    - [SquigglyAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/squigglyannotation) והגדרת פרמטרים (כותרת, צבע).
    - [UnderlineAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/underlineannotation) והגדרת פרמטרים (כותרת, צבע).
- [UnderlineAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/underlineannotation) והגדרת פרמטרים (כותרת, צבע).
1. לאחר מכן עלינו להוסיף את כל ההערות לעמוד.

```csharp
using Aspose.Pdf.Annotations;
using Aspose.Pdf.Text;
using System;
using System.Linq;

namespace Aspose.Pdf.Examples.Advanced
{
    class ExampleTextMarkupAnnotation
    {
        // נתיב לספריית המסמכים.
        private const string _dataDir = "..\\..\\..\\..\\Samples";

        public static void AddTextMarkupAnnotation()
        {
            try
            {
                // טעינת קובץ ה-PDF
                Document document = new Document(System.IO.Path.Combine(_dataDir, "sample.pdf"));
                var tfa = new Aspose.Pdf.Text.TextFragmentAbsorber("PDF");
                tfa.Visit(document.Pages[1]);

                // יצירת הערות
                HighlightAnnotation highlightAnnotation = new HighlightAnnotation(document.Pages[1],
                   tfa.TextFragments[1].Rectangle )
                {
                    Title = "משתמש Aspose",
                    Color = Color.LightGreen
                };

                StrikeOutAnnotation strikeOutAnnotation = new StrikeOutAnnotation(
                   document.Pages[1],
                   tfa.TextFragments[2].Rectangle)
                {
                    Title = "משתמש Aspose",
                    Color = Color.Blue
                };
                SquigglyAnnotation squigglyAnnotation = new SquigglyAnnotation(document.Pages[1],
                    tfa.TextFragments[3].Rectangle)
                {
                    Title = "משתמש Aspose",
                    Color = Color.Red
                };
                UnderlineAnnotation underlineAnnotation = new UnderlineAnnotation(document.Pages[1],
                    tfa.TextFragments[4].Rectangle)
                {
                    Title = "משתמש Aspose",
                    Color = Color.Violet
                };
                // הוספת הערה לעמוד
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

אם אתה רוצה להדגיש קטע רב שורות עליך להשתמש בדוגמה מתקדמת:

```csharp
        /// <summary>
        /// דוגמה מתקדמת אם אתה רוצה להדגיש קטע רב שורות
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
                    Title = "משתמש Aspose",
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
                Title = "משתמש Aspose",
                Color = color,
                Modified = DateTime.Now,
                QuadPoints = quadPoints
            };
        }

        /// <summary>
        /// איך לקבל טקסט מודגש
        /// </summary>
        public static void GetHighlightedText()
        {
            // טען את קובץ ה-PDF
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
## קבל אנוטציית סימון טקסט

נסה להשתמש בקטע הקוד הבא כדי לקבל אנוטציית סימון טקסט ממסמך PDF.

```csharp
    public static void GetTextMarkupAnnotation()
    {
        // טען את קובץ ה-PDF
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

## מחק אנוטציית סימון טקסט

קטע הקוד הבא מראה כיצד למחוק אנוטציית סימון טקסט מקובץ PDF.

```csharp
    public static void DeleteTextMarkupAnnotation()
    {
        // טען את קובץ ה-PDF
        Document document = new Document(System.IO.Path.Combine(_dataDir, "sample_mod.pdf"));
        var textMarkupAnnotations = document.Pages[1].Annotations
            .Where(a => a.AnnotationType == AnnotationType.Highlight
            ||a.AnnotationType == AnnotationType.Squiggly)
            .Cast<TextMarkupAnnotation>();
            foreach (var ta in textMarkupAnnotations)
            {
            document.Pages[1].Annotations.Delete(ta);
            }
            document.Save(System.IO.Path.Combine(_dataDir, "sample_del.pdf"));
    }
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "ספריית Aspose.PDF עבור .NET",
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
                "contactType": "מכירות",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "מכירות",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "מכירות",
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
    "applicationCategory": "ספריית עיבוד PDF עבור .NET",
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
```

