---
title: הוספה ומחיקה של סימניה
linktitle: הוספה ומחיקה של סימניה
type: docs
weight: 10
url: /net/add-and-delete-bookmark/
description: ניתן להוסיף סימניה למסמך PDF באמצעות C#. ניתן למחוק כל הסימניות או סימניות מסוימות ממסמך PDF.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
aliases:
    - /net/add-and-delete-a-bookmark/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "הוספה ומחיקה של סימניה",
    "alternativeHeadline": "איך להוסיף ולמחוק סימניה ממסמך PDF",
    "author": {
        "@type": "Person",
        "name":"Andriy Andrukhovskiy",
        "givenName": "Andriy",
        "familyName": "Andrukhovskiy",
        "url":"https://www.linkedin.com/in/andruhovski/"
    },
    "genre": "יצירת מסמכי PDF",
    "keywords": "pdf, c#, מחיקת סימניה, הוספת סימניה",
    "wordcount": "302",
    "proficiencyLevel":"מתחיל",
    "publisher": {
        "@type": "Organization",
        "name": "צוות Aspose.PDF Doc",
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
    "url": "/net/add-and-delete-bookmark/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-and-delete-bookmark/"
    },
    "dateModified": "2022-02-04",
    "description": "ניתן להוסיף סימניה למסמך PDF באמצעות C#. ניתן למחוק כל הסימניות או סימניות מסוימות ממסמך PDF."
}
</script>
הקוד הבא עובד גם עם ספריית [Aspose.PDF.Drawing](/pdf/net/drawing/).

## הוספת סימניה למסמך PDF

סימניות מאוחסנות באוסף [OutlineItemCollection](https://reference.aspose.com/pdf/net/aspose.pdf/outlineitemcollection) שנמצא בתוך אוסף [OutlineCollection](https://reference.aspose.com/pdf/net/aspose.pdf/outlinecollection).

להוספת סימניה ל-PDF:

1. פתח מסמך PDF באמצעות אובייקט [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).
1. צור סימניה והגדר את מאפייניה.
1. הוסף את אוסף [OutlineItemCollection](https://reference.aspose.com/pdf/net/aspose.pdf/outlineitemcollection) לאוסף ה-Outlines.

הקטע קוד הבא מראה איך להוסיף סימניה במסמך PDF.

```csharp
// לדוגמאות מלאות וקבצי נתונים, אנא עבור ל https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לספריית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_Bookmarks();

// פתיחת מסמך
Document pdfDocument = new Document(dataDir + "AddBookmark.pdf");

// יצירת אובייקט סימניה
OutlineItemCollection pdfOutline = new OutlineItemCollection(pdfDocument.Outlines);
pdfOutline.Title = "Test Outline";
pdfOutline.Italic = true;
pdfOutline.Bold = true;
// הגדרת מספר העמוד ליעד
pdfOutline.Action = new GoToAction(pdfDocument.Pages[1]);
// הוספת סימניה לאוסף ה-outline של המסמך.
pdfDocument.Outlines.Add(pdfOutline);

dataDir = dataDir + "AddBookmark_out.pdf";
// שמירת הפלט
pdfDocument.Save(dataDir);
```
## הוספת סימניה משנית למסמך PDF

סימניות יכולות להיות מקוננות, מה שמציין יחס היררכי בין סימניות הורה לילד. מאמר זה מסביר איך להוסיף סימניה ילדה, כלומר סימניה ברמה השנייה, לקובץ PDF.

כדי להוסיף סימניה ילדה לקובץ PDF, ראשית יש להוסיף סימניה הורה:

1. פתח מסמך.
1. הוסף סימניה ל-[OutlineItemCollection](https://reference.aspose.com/pdf/net/aspose.pdf/outlineitemcollection), תוך הגדרת המאפיינים שלה.
1. הוסף את OutlineItemCollection לאוסף [OutlineCollection](https://reference.aspose.com/pdf/net/aspose.pdf/outlinecollection) של אובייקט המסמך.

הסימניה הילדה נוצרת באותה הדרך כמו הסימניה ההורה, כפי שהוסבר לעיל, אך מתווספת לאוסף ה-Outlines של הסימניה ההורה.

הקטעי קוד הבאים מראים איך להוסיף סימניה ילדה למסמך PDF.

```csharp
// לדוגמאות מלאות וקבצי נתונים, אנא בקר ב https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לספריית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_Bookmarks();

// פתיחת מסמך
Document pdfDocument = new Document(dataDir + "AddChildBookmark.pdf");

// יצירת אובייקט סימניה הורה
OutlineItemCollection pdfOutline = new OutlineItemCollection(pdfDocument.Outlines);
pdfOutline.Title = "Parent Outline";
pdfOutline.Italic = true;
pdfOutline.Bold = true;

// יצירת אובייקט סימניה ילדה
OutlineItemCollection pdfChildOutline = new OutlineItemCollection(pdfDocument.Outlines);
pdfChildOutline.Title = "Child Outline";
pdfChildOutline.Italic = true;
pdfChildOutline.Bold = true;

// הוספת סימניה ילדה לאוסף הסימניות של ההורה
pdfOutline.Add(pdfChildOutline);
// הוספת סימניה הורה לאוסף הסימניות של המסמך.
pdfDocument.Outlines.Add(pdfOutline);

dataDir = dataDir + "AddChildBookmark_out.pdf";
// שמירת הפלט
pdfDocument.Save(dataDir);
```
## מחק את כל הסימניות ממסמך PDF

כל הסימניות במסמך PDF נמצאות באוסף [OutlineCollection](https://reference.aspose.com/pdf/net/aspose.pdf/outlinecollection). המאמר הזה מסביר איך למחוק את כל הסימניות מקובץ PDF.

כדי למחוק את כל הסימניות מקובץ PDF:

1. קרא לשיטת Delete של אוסף [OutlineCollection](https://reference.aspose.com/pdf/net/aspose.pdf/outlinecollection).
1. שמור את הקובץ המעודכן באמצעות שיטת [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4) של אובייקט [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).

הקטעי קוד הבאים מראים איך למחוק את כל הסימניות ממסמך PDF.

```csharp
// לדוגמאות מלאות וקבצי נתונים, אנא עבור ל https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לתיקיית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_Bookmarks();

// פתח מסמך
Document pdfDocument = new Document(dataDir + "DeleteAllBookmarks.pdf");

// מחק את כל הסימניות
pdfDocument.Outlines.Delete();

dataDir = dataDir + "DeleteAllBookmarks_out.pdf";
// שמור את הקובץ המעודכן
pdfDocument.Save(dataDir);
```
## מחיקת סימניה מסוימת ממסמך PDF

כדי למחוק סימניה מסוימת מקובץ PDF:

1. העבר את כותרת הסימניה כפרמטר למתודת Delete של אוסף [OutlineCollection](https://reference.aspose.com/pdf/net/aspose.pdf/outlinecollection).
1. לאחר מכן שמור את הקובץ המעודכן באמצעות מתודת Save של אובייקט המסמך.

המחלקה [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) מספקת את אוסף [OutlineCollection](https://reference.aspose.com/pdf/net/aspose.pdf/outlinecollection). המתודה [Delete](https://reference.aspose.com/pdf/net/aspose.pdf/outlinecollection/methods/delete) מסירה כל סימניה עם הכותרת שהועברה למתודה.

הדוגמאות הבאות בקוד מראות כיצד למחוק סימניה מסוימת ממסמך ה-PDF.

```csharp
// לדוגמאות מלאות וקבצי נתונים, אנא עבורו ל https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לתיקיית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_Bookmarks();

// פתח מסמך
Document pdfDocument = new Document(dataDir + "DeleteParticularBookmark.pdf");

// מחק סימניה מסוימת לפי כותרת
pdfDocument.Outlines.Delete("Child Outline");

// שמור את הקובץ המעודכן
pdfDocument.Save(dataDir + "DeleteParticularBookmark_out.pdf");
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "ספריית Aspose.PDF ל-.NET",
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
    "applicationCategory": "ספרייה לעיבוד PDF ל-.NET",
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

