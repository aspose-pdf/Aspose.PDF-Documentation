---
title: העברת דפים ב-PDF תכנותית ב-C#
linktitle: העברת דפי PDF
type: docs
weight: 20
url: /net/move-pages/
description: נסה להעביר דפים למיקום הרצוי או לסוף קובץ PDF באמצעות Aspose.PDF עבור .NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "העברת דפים ב-PDF תכנותית ב-C#",
    "alternativeHeadline": "איך להעביר דפי PDF עם .NET",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "יצירת מסמכי PDF",
    "keywords": "pdf, c#, הזזת דף PDF",
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
    "url": "/net/move-pages/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/move-pages/"
    },
    "dateModified": "2022-02-04",
    "description": "נסה להעביר דפים למיקום הרצוי או לסוף קובץ PDF באמצעות Aspose.PDF עבור .NET."
}
</script>
## העברת עמוד ממסמך PDF אחד למסמך אחר

נושא זה מסביר כיצד להעביר עמוד ממסמך PDF אחד לסוף מסמך אחר באמצעות C#.

הקטע קוד הבא עובד גם עם ספריית [Aspose.PDF.Drawing](/pdf/net/drawing/).

כדי להעביר עמוד עלינו:

1. ליצור אובייקט מחלקת [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) עם קובץ ה-PDF המקורי.
1. ליצור אובייקט מחלקת [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) עם קובץ ה-PDF היעד.
1. לקבל עמוד מאוסף [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection).
1. [להוסיף](https://reference.aspose.com/pdf/net/aspose.pdf.pagecollection/add/methods/1) עמוד למסמך היעד.
1. לשמור את ה-PDF המוצא באמצעות השיטה [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4).
1. [למחוק](https://reference.aspose.com/pdf/net/aspose.pdf.pagecollection/delete/methods/1) עמוד במסמך המקור.
1.

הקטע הבא מראה לך איך להזיז דף אחד.

```csharp
var srcFileName = "<הכנס שם קובץ>";
var dstFileName = "<הכנס שם קובץ>";
var srcDocument = new Document(srcFileName);
var dstDocument = new Document();
var page = srcDocument.Pages[2];
dstDocument.Pages.Add(page);
// שמור את קובץ הפלט
dstDocument.Save(srcFileName);
srcDocument.Pages.Delete(2);
srcDocument.Save(dstFileName);
```

## העברת קבוצת דפים ממסמך PDF אחד לאחר

1. צור אובייקט מחלקת [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) עם קובץ ה-PDF המקורי.
1. צור אובייקט מחלקת [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) עם קובץ ה-PDF היעד.
1. הגדר מערך עם מספרי הדפים להעברה.
1. בצע לולאה דרך המערך:
    1. קבל דף מאוסף הדפים [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection).
    1.
1. שמור את קובץ ה-PDF המוצא באמצעות השיטה [שמור](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4).
1. [מחק](https://reference.aspose.com/pdf/net/aspose.pdf.pagecollection/delete/methods/2) דף במסמך המקור באמצעות מערך.
1. שמור את קובץ ה-PDF המקור באמצעות השיטה [שמור](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4).

קטע הקוד הבא מראה איך להעביר כמה דפים ממסמך PDF אחד לאחר.

```csharp
var srcFileName = "<הכנס שם קובץ>";
var dstFileName = "<הכנס שם קובץ>";
var srcDocument = new Aspose.Pdf.Document(srcFileName);
var dstDocument = new Aspose.Pdf.Document();
var pages = new []{ 1, 3 };
foreach (var pageIndex in pages)
{
    var page = srcDocument.Pages[pageIndex];
    dstDocument.Pages.Add(page);
}                       
// שמור קבצים פלט
dstDocument.Save(dstFileName);
srcDocument.Pages.Delete(pages);
srcDocument.Save(srcFileName);
```
1.
1. קבל דף מאוסף הדפים [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection).
1. [הוסף](https://reference.aspose.com/pdf/net/aspose.pdf.pagecollection/add/methods/1) דף למיקום החדש (לדוגמה לסוף).
1. [מחק](https://reference.aspose.com/pdf/net/aspose.pdf.pagecollection/delete/methods/1) דף במיקום הקודם.
1. שמור את קובץ ה-PDF המוצא באמצעות הפונקציה [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4).

```csharp
var srcFileName = "<הזן שם קובץ>";
var dstFileName = "<הזן שם קובץ>";
var srcDocument = new Aspose.Pdf.Document(srcFileName);

var page = srcDocument.Pages[2];
srcDocument.Pages.Add(page);
srcDocument.Pages.Delete(2);          

// שמור קובץ פלט
srcDocument.Save(dstFileName);
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

