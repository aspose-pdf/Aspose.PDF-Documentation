---
title: הוספת אובייקט קשת לקובץ PDF
linktitle: הוסף קשת
type: docs
weight: 10
url: /net/add-arc/
description: המאמר מסביר כיצד ליצור אובייקט קשת ב-PDF שלך באמצעות Aspose.PDF עבור .NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "הוספת אובייקט קשת לקובץ PDF",
    "alternativeHeadline": "איך ליצור קשת בקובץ PDF",
    "author": {
        "@type": "Person",
        "name":"אנסטסיה חולוב",
        "givenName": "אנסטסיה",
        "familyName": "חולוב",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "יצירת מסמכי PDF",
    "keywords": "pdf, c#, קשת ב-pdf",
    "wordcount": "302",
    "proficiencyLevel":"מתחיל",
    "publisher": {
        "@type": "Organization",
        "name": "צוות מסמכים של Aspose.PDF",
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
    "url": "/net/add-arc/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-arc/"
    },
    "dateModified": "2022-02-04",
    "description": "המאמר מסביר כיצד ליצור אובייקט קשת ב-PDF שלך באמצעות Aspose.PDF עבור .NET."
}
</script>
הקטע הבא של קוד עובד גם עם ספריית [Aspose.PDF.Drawing](/pdf/net/drawing/).

## הוספת אובייקט קשת

Aspose.PDF עבור .NET תומך בתכונה להוסיף אובייקטים גרפיים (לדוגמה גרף, קו, מלבן וכו') למסמכי PDF. הוא גם מציע את התכונה למלא אובייקט קשת בצבע מסוים.

עקוב אחר השלבים למטה:

1. צור מופע של [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document)

1. צור [אובייקט ציור](https://reference.aspose.com/pdf/net/aspose.pdf.drawing) במידות מסוימות

1. הגדר [מסגרת](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/graph/properties/border) לאובייקט ציור

1. הוסף אובייקט [גרף](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/graph) לאוסף פסקאות של עמוד

1. שמור את קובץ ה-PDF שלנו

הקטע הבא של קוד מראה איך להוסיף אובייקט [קשת](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/arc).

```csharp
 public static void Arc()
        {
            // צור מופע של מסמך
            var document = new Document();

            // הוסף עמוד לאוסף העמודים של קובץ ה-PDF
            var page = document.Pages.Add();

            // צור אובייקט ציור עם מידות מסוימות
            var graph = new Aspose.Pdf.Drawing.Graph(400, 400);
            // הגדר מסגרת לאובייקט ציור
            var borderInfo = new BorderInfo(BorderSide.All, Color.Green);
            graph.Border = borderInfo;

            var arc1 = new Arc(100, 100, 95, 0, 90);
            arc1.GraphInfo.Color = Color.GreenYellow;
            graph.Shapes.Add(arc1);

            var arc2 = new Arc(100, 100, 90, 70, 180);
            arc2.GraphInfo.Color = Color.DarkBlue;
            graph.Shapes.Add(arc2);

            var arc3 = new Arc(100, 100, 85, 120, 210);
            arc3.GraphInfo.Color = Color.Red;
            graph.Shapes.Add(arc3);

            // הוסף אובייקט גרף לאוסף פסקאות של עמוד
            page.Paragraphs.Add(graph);

            // שמור את קובץ ה-PDF
            document.Save(_dataDir + "DrawingArc_out.pdf");

        }
```
## יצירת אובייקט קשת מלאה

הדוגמה הבאה מראה כיצד להוסיף אובייקט קשת שמלא בצבע ובמידות מסוימות.

```csharp
        public static void ArcFilled()
        {
            // יצירת מופע של מסמך
            var document = new Document();

            // הוספת דף לאוסף הדפים של קובץ PDF
            var page = document.Pages.Add();

            // יצירת אובייקט ציור עם מידות מסוימות
            var graph = new Aspose.Pdf.Drawing.Graph(400, 400);
            // הגדרת גבול לאובייקט הציור
            var borderInfo = new BorderInfo(BorderSide.All, Color.Green);
            graph.Border = borderInfo;

            var arc = new Arc(100, 100, 95, 0, 90);
            arc.GraphInfo.FillColor = Color.GreenYellow;
            graph.Shapes.Add(arc);

            var line = new Line(new float[] { 195, 100, 100, 100, 100, 195 });
            line.GraphInfo.FillColor = Color.GreenYellow;
            graph.Shapes.Add(line);

            // הוספת אובייקט הגרף לאוסף הפסקאות של הדף
            page.Paragraphs.Add(graph);

            // שמירת קובץ PDF
            document.Save(_dataDir + "ExampleFilledArc_out.pdf");

        }
```
בואו נראה את תוצאת הוספת קשת מלאה:

![קשת מלאה](filled_arc.png)

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
    "applicationCategory": "ספריית עיבוד PDF ל-.NET",
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

