---
title: הוספת אובייקט עקומה לקובץ PDF
linktitle: הוספת עקומה
type: docs
weight: 30
url: /net/add-curve/
description: מאמר זה מסביר כיצד ליצור אובייקט עקומה ב-PDF שלך באמצעות Aspose.PDF עבור .NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "הוספת אובייקט עקומה לקובץ PDF",
    "alternativeHeadline": "כיצד ליצור אובייקט עקומה בקובץ PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "יצירת מסמכי PDF",
    "keywords": "pdf, .net, עקומה ב-pdf",
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
    "url": "/net/add-curve/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-curve/"
    },
    "dateModified": "2022-02-04",
    "description": "מאמר זה מסביר כיצד ליצור אובייקט עקומה ב-PDF שלך באמצעות Aspose.PDF עבור .NET."
}
</script>

הקטע הבא בקוד עובד גם עם ספריית [Aspose.PDF.Drawing](/pdf/net/drawing/).

## הוספת אובייקט עקומה

גרף [עקומה](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/curve) הוא איחוד מחובר של קווים פרויקטיביים, כל קו נפגש עם שלושה אחרים בנקודות כפולות רגילות.

Aspose.PDF עבור .NET מראה כיצד להשתמש בעקומות בזייר בגרפים שלך.
עקומות בזייר משמשות רבות בגרפיקת מחשב לדגמת עקומים חלקים. העקומה מוכלת לחלוטין במעטפת הקמורה של נקודות הבקרה שלה, ניתן להציג את הנקודות באופן גרפי ולהשתמש בהן לשליטה אינטואיטיבית בעקומה.
כל העקומה מוכלת במרובע שפינותיו הן ארבע הנקודות הנתונות (מעטפתן הקמורה).

במאמר זה, נחקור עקומות גרפיות פשוטות ועקומות מלאות, שאתה יכול ליצור במסמך PDF שלך.

עקוב אחרי השלבים למטה:

1. צור מופע של [מסמך](https://reference.aspose.com/pdf/net/aspose.pdf/document)
1. הגדר [מסגרת](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/graph/properties/border) לאובייקט ציור

1. הוסף [גרף](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/graph) לאוסף הפסקאות של הדף

1. שמור את קובץ ה-PDF שלנו

```csharp
 public static void ExampleCurve()
        {
            // צור מופע של מסמך
            var document = new Document();

            // הוסף דף לאוסף הדפים של קובץ ה-PDF
            var page = document.Pages.Add();

            // צור אובייקט ציור עם ממדים מסוימים
            var graph = new Aspose.Pdf.Drawing.Graph(400, 200);

            // הגדר מסגרת לאובייקט הציור
            var borderInfo = new BorderInfo(BorderSide.All, Color.Green);
            graph.Border = borderInfo;

            var curve1 = new Curve(new float[] { 10, 10, 50, 60, 70, 10, 100, 120 });
            curve1.GraphInfo.Color = Color.GreenYellow;
            graph.Shapes.Add(curve1);

            // הוסף אובייקט גרף לאוסף הפסקאות של הדף
            page.Paragraphs.Add(graph);

            // שמור את קובץ ה-PDF
            document.Save(_dataDir + "DrawingCurve1_out.pdf");
        }
```
התמונה הבאה מראה את התוצאה שהושגה עם קטע הקוד שלנו:

![ציור עקומה](drawing_curve.png)

## יצירת אובייקט עקומה מלאה

דוגמה זו מראה כיצד להוסיף אובייקט עקומה שמלא בצבע.

```csharp
      public static void CurveFilled()
        {
            // צור מופע מסמך
            var document = new Document();

            // הוסף דף לאוסף הדפים של קובץ PDF
            var page = document.Pages.Add();

            // צור אובייקט ציור עם ממדים מסוימים
            var graph = new Aspose.Pdf.Drawing.Graph(400, 200);

            // הגדר מסגרת לאובייקט הציור
            var borderInfo = new BorderInfo(BorderSide.All, Color.Green);
            graph.Border = borderInfo;

            var curve1 = new Curve(new float[] { 10, 10, 50, 60, 70, 10, 100, 120 });
            curve1.GraphInfo.FillColor = Color.GreenYellow;
            graph.Shapes.Add(curve1);

            // הוסף את אובייקט הגרף לאוסף הפסקאות של הדף
            page.Paragraphs.Add(graph);

            // שמור את קובץ ה-PDF
            document.Save(_dataDir + "DrawingCurve2_out.pdf");
        }
```
צפו בתוצאה של הוספת עקומה מלאה:

![עקומה מלאה](filled_curve.png)

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
    "applicationCategory": "ספריית עריכת PDF עבור .NET",
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

