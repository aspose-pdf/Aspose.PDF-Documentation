---
title: הוספת דפים למסמך PDF
linktitle: הוספת דפים
type: docs
weight: 10
url: /net/add-pages/
description: מאמר זה מלמד איך להוסיף דף במיקום הרצוי בקובץ PDF. למד כיצד להזיז, להסיר דפים מקובץ PDF באמצעות C#.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
aliases:
    - /net/insert-pdf-pages/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "הוספת דפים ב-PDF עם C#",
    "alternativeHeadline": "כיצד להוסיף דפים במסמך PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "יצירת מסמכי PDF",
    "keywords": "pdf, c#, הוספת דף pdf, הכנסת דף pdf",
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
    "url": "/net/add-pages/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-pages/"
    },
    "dateModified": "2022-02-04",
    "description": "מאמר זה מלמד איך להוסיף דף במיקום הרצוי בקובץ PDF. למד כיצד להזיז, להסיר דפים מקובץ PDF באמצעות C#."
}
</script>
Aspose.PDF ל-.NET API מספק גמישות מלאה לעבוד עם דפים במסמך PDF באמצעות C# או כל שפת .NET אחרת. הוא שומר את כל הדפים של מסמך PDF ב-[PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection) שניתן להשתמש בו לעבודה עם דפי PDF.
Aspose.PDF ל-.NET מאפשר לך להוסיף דף למסמך PDF בכל מיקום בקובץ כמו גם להוסיף דפים לסוף קובץ PDF.
סעיף זה מראה כיצד להוסיף דפים ל-PDF באמצעות C#.

## הוסף או הכנס דף בקובץ PDF

Aspose.PDF ל-.NET מאפשר לך להכניס דף למסמך PDF בכל מיקום בקובץ כמו גם להוסיף דפים לסוף קובץ PDF.

הקטע קוד הבא עובד גם עם ספריית [Aspose.PDF.Drawing](/pdf/net/drawing/).

### הכנס דף ריק בקובץ PDF במיקום הרצוי

כדי להכניס דף ריק בקובץ PDF:

1. צור אובייקט מחלקת [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) עם קובץ PDF הקלט.
1.
1.
שמור את קובץ ה-PDF המופק באמצעות השיטה [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4).

הקטע קוד הבא מראה איך להוסיף דף לקובץ PDF.

```cs
// לדוגמאות מלאות וקבצי נתונים, אנא עבור ל https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לתיקיית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_Pages();

// פתח מסמך
Document pdfDocument = new Document(dataDir + "InsertEmptyPage.pdf");

// הוסף דף ריק ל-PDF
pdfDocument.Pages.Insert(2);
// שמור את קובץ הפלט
pdfDocument.Save(dataDir + "InsertEmptyPage_out.pdf");
```

בדוגמה למעלה, הוספנו דף ריק עם פרמטרים ברירת מחדל. אם תרצה להתאים את גודל הדף כמו דף אחר במסמך תצטרך להוסיף
כמה שורות קוד:

```cs
var page = pdfDocument.Pages.Insert(2);
//העתק פרמטרים של הדף מדף 1
page.ArtBox = pdfDocument.Pages[1].ArtBox;
page.BleedBox = pdfDocument.Pages[1].BleedBox;
page.CropBox = pdfDocument.Pages[1].CropBox;
page.MediaBox = pdfDocument.Pages[1].MediaBox;
page.TrimBox = pdfDocument.Pages[1].TrimBox;
```
### הוספת דף ריק בסוף קובץ PDF

לעיתים תרצה לוודא שמסמך מסתיים בדף ריק. נושא זה מסביר כיצד להוסיף דף ריק בסוף מסמך PDF.

להוספת דף ריק בסוף קובץ PDF:

1. צור אובייקט מחלקת [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) עם קובץ PDF הקלט.
1. קרא למתודת [Add](https://reference.aspose.com/pdf/net/aspose.pdf.pagecollection/add/methods/1) של אוסף [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection), ללא פרמטרים.
1. שמור את קובץ ה-PDF המוצא באמצעות מתודת [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4).

הקטע קוד הבא מראה איך להוסיף דף ריק בסוף קובץ PDF.

```cs
// לדוגמאות מלאות וקבצי נתונים, אנא בקרו ב https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לתיקיית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_Pages();

// פתח מסמך
Document pdfDocument = new Document(dataDir + "InsertEmptyPageAtEnd.pdf");

// הוסף דף ריק בסוף קובץ PDF
pdfDocument.Pages.Add();

// שמור קובץ פלט
pdfDocument.Save(dataDir + "InsertEmptyPageAtEnd_out.pdf");
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

