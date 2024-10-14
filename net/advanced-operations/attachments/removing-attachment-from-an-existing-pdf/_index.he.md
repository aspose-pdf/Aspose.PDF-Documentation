---
title: הסרת קובץ מצורף מ-PDF
linktitle: הסרת קובץ מצורף מ-PDF קיים
type: docs
weight: 30
url: /net/removing-attachment-from-an-existing-pdf/
description: Aspose.PDF יכול להסיר קבצים מצורפים מהמסמכים שלך ב-PDF. השתמש ב-API של C# PDF כדי להסיר קבצים מצורפים בקבצי PDF באמצעות ספריית Aspose.PDF.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "הסרת קובץ מצורף מ-PDF",
    "alternativeHeadline": "כיצד למחוק קבצים מצורפים מ-PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "יצירת מסמכי PDF",
    "keywords": "pdf, c#, מחיקת קבצים מצורפים",
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
    "url": "/net/removing-attachment-from-an-existing-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/removing-attachment-from-an-existing-pdf/"
    },
    "dateModified": "2022-02-04",
    "description": "Aspose.PDF יכול להסיר קבצים מצורפים מהמסמכים שלך ב-PDF. השתמש ב-API של C# PDF כדי להסיר קבצים מצורפים בקבצי PDF באמצעות ספריית Aspose.PDF."
}
</script>
Aspose.PDF יכול להסיר קבצים מצורפים מקבצי PDF. הקבצים המצורפים של מסמך PDF מאוחסנים באוסף EmbeddedFiles של אובייקט המסמך.

הקטע קוד הבא עובד גם עם ספריית [Aspose.PDF.Drawing](/pdf/net/drawing/).

כדי למחוק את כל הקבצים המצורפים הקשורים לקובץ PDF:

1. קרא לשיטת [Delete](https://reference.aspose.com/pdf/net/aspose.pdf/embeddedfilecollection/methods/delete) של אוסף [EmbeddedFiles](https://reference.aspose.com/pdf/net/aspose.pdf/embeddedfilecollection).
1. שמור את הקובץ המעודכן באמצעות שיטת [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4) של אובייקט [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).

הקטע קוד הבא מראה כיצד להסיר קבצים מצורפים ממסמך PDF.

```csharp
// לדוגמאות מלאות וקבצי נתונים, אנא עבור ל https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לתיקיית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_Attachments();

// פתח מסמך
Document pdfDocument = new Document(dataDir + "DeleteAllAttachments.pdf");

// מחק את כל הקבצים המצורפים
pdfDocument.EmbeddedFiles.Delete();

// שמור מסמך מעודכן
pdfDocument.Save(dataDir + "DeleteAllAnnotationsFromPage_out.pdf");
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
```

