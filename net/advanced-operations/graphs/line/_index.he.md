---
title: הוספת אובייקט קו לקובץ PDF
linktitle: הוספת קו
type: docs
weight: 40
url: /net/add-line/
description: מאמר זה מסביר איך ליצור אובייקט קו ב-PDF שלך באמצעות Aspose.PDF עבור .NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "הוספת אובייקט קו לקובץ PDF",
    "alternativeHeadline": "איך ליצור אובייקט קו בקובץ PDF",
    "author": {
        "@type": "Person",
        "name":"אנסטסיה חולוב",
        "givenName": "אנסטסיה",
        "familyName": "חולוב",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "יצירת מסמכי PDF",
    "keywords": "pdf, c#, קו ב-pdf",
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
                "availableLanguage": "אנגלית"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "מכירות",
                "areaServed": "GB",
                "availableLanguage": "אנגלית"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "מכירות",
                "areaServed": "AU",
                "availableLanguage": "אנגלית"
            }
        ]
    },
    "url": "/net/add-line/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-line/"
    },
    "dateModified": "2022-02-04",
    "description": "מאמר זה מסביר איך ליצור אובייקט קו ב-PDF שלך באמצעות Aspose.PDF עבור .NET."
}
</script>
הקטע הבא של קוד עובד גם עם ספריית [Aspose.PDF.Drawing](/pdf/net/drawing/).

## הוספת אובייקט קו

Aspose.PDF עבור .NET תומך בתכונה להוספת אובייקטים גרפיים (לדוגמה גרף, קו, מלבן וכו') למסמכי PDF. אתה גם מקבל את היתרון להוסיף אובייקט [קו](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/line) שם אתה יכול גם לציין את דפוס הקו, הצבע ועיצובים נוספים לאלמנט הקו.

עקוב אחרי השלבים למטה:

1. צור מסמך PDF חדש [מסמך](https://reference.aspose.com/pdf/net/aspose.pdf/document)

1. הוסף [דף](https://reference.aspose.com/pdf/net/aspose.pdf/page) לאוסף הדפים של קובץ PDF

1. צור מופע [גרף](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/graph).

1. הוסף אובייקט גרף לאוסף הפסקאות של מופע הדף.

1. צור מופע [מלבן](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/rectangle).

1. הגדר רוחב הקו.

1.
1. שמור את קובץ ה-PDF שלך.

הקטע קוד הבא מציג איך להוסיף אובייקט [מלבן](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/rectangle) שממולא בצבע.

```csharp
        public static void AddLineObjectToPDF()
        {
            // צור מופע של מסמך
            var document = new Document();

            // הוסף דף לאוסף הדפים של קובץ ה-PDF
            var page = document.Pages.Add();

            // צור מופע של גרף
            var graph = new Aspose.Pdf.Drawing.Graph(100, 400);

            // הוסף אובייקט גרף לאוסף הפסקאות של מופע הדף
            page.Paragraphs.Add(graph);

            // צור מופע של מלבן
            var line = new Line(new float[] { 100, 100, 200, 100 });

            // ציין צבע מילוי עבור אובייקט הגרף
            line.GraphInfo.DashArray = new int[] { 0, 1, 0 };
            line.GraphInfo.DashPhase = 1;

            // הוסף אובייקט מלבן לאוסף הצורות של אובייקט הגרף
            graph.Shapes.Add(line);

            // שמור את קובץ ה-PDF
            document.Save(_dataDir + "AddLineObject_out.pdf");
        }
```
![Add Line](add_line.png)

## כיצד להוסיף קו מקווקו למסמך PDF שלך

```csharp
        public static void DashLengthInBlackAndDashLengthInWhite()
        {
            // יצירת מופע מסמך
            var document = new Document();

            // הוספת דף לאוסף הדפים של קובץ PDF
            var page = document.Pages.Add();

            // יצירת אובייקט ציור עם מידות מסוימות
            var canvas = new Aspose.Pdf.Drawing.Graph(100, 400);
            // הוספת אובייקט הציור לאוסף הפסקאות של מופע הדף
            page.Paragraphs.Add(canvas);

            // יצירת אובייקט קו
            var line = new Line(new float[] { 100, 100, 200, 100 });
            // הגדרת צבע לאובייקט הקו
            line.GraphInfo.Color = Color.Red;
            // ציון מערך הדאש לאובייקט הקו
            line.GraphInfo.DashArray = new int[] { 0, 1, 0 };
            // הגדרת שלב הדאש למופע הקו
            line.GraphInfo.DashPhase = 1;
            // הוספת הקו לאוסף הצורות של אובייקט הציור
            canvas.Shapes.Add(line);
            // שמירת קובץ PDF
            document.Save(_dataDir + "DashLengthInBlackAndDashLengthInWhite_out.pdf");
        }
```
בואו נבדוק את התוצאה:

![קו מקווקו](dash_line.png)

## שרטוט קו לאורך הדף

ניתן גם להשתמש באובייקט של קו כדי לצייר חצייה המתחילה מהפינה השמאלית-תחתונה לפינה הימנית-עליונה ומהפינה השמאלית-עליונה לפינה הימנית-תחתונה.

אנא עיינו בקטע הקוד הבא כדי לבצע דרישה זו.

```csharp
   public static void ExampleLineAcrossPage()
        {

            // יצירת מופע מסמך
            var document = new Document();

            // הוספת דף לאוסף הדפים של קובץ PDF
            var page = document.Pages.Add();
            // הגדרת שולי הדף בכל הצדדים כ-0

            page.PageInfo.Margin.Left = 0;
            page.PageInfo.Margin.Right = 0;
            page.PageInfo.Margin.Bottom = 0;
            page.PageInfo.Margin.Top = 0;

            // יצירת אובייקט גרף עם רוחב וגובה שווים לממדי הדף
            var graph = new Aspose.Pdf.Drawing.Graph(
                (float)page.PageInfo.Width,
                (float)page.PageInfo.Height);

            // יצירת אובייקט הקו הראשון המתחיל מהפינה התחתונה-שמאלית לפינה העליונה-ימנית של הדף
            var line = new Line(
                    new float[]{
                        (float)page.Rect.LLX, 0,
                        (float)page.PageInfo.Width,
                        (float)page.Rect.URY });

            // הוספת הקו לאוסף הצורות של אובייקט הגרף
            graph.Shapes.Add(line);
            // שרטוט קו מהפינה העליונה-שמאלית של הדף לפינה התחתונה-ימנית של הדף
            var line2 = new Line(
                new float[]{ 0,
                    (float) page.Rect.URY,
                    (float) page.PageInfo.Width,
                    (float) page.Rect.LLX });

            // הוספת הקו לאוסף הצורות של אובייקט הגרף
            graph.Shapes.Add(line2);

            // הוספת אובייקט הגרף לאוסף הפסקאות של הדף
            page.Paragraphs.Add(graph);

            // שמירת קובץ PDF
            document.Save(_dataDir + "ExampleLineAcrossPage_out.pdf");
        }
```
![Drawing Line](draw_line.png)

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
                "availableLanguage": "אנגלית"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "מכירות",
                "areaServed": "GB",
                "availableLanguage": "אנגלית"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "מכירות",
                "areaServed": "AU",
                "availableLanguage": "אנגלית"
            }
        ]
    },
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "ספריית ניהול PDF עבור .NET",
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


