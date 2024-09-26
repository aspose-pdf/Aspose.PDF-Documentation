---
title: פיצול קובץ PDF באופן תכנותי
linktitle: פצל קבצי PDF
type: docs
weight: 60
url: /net/split-pdf-document/
keywords: פיצול pdf לכמה קבצים, פיצול pdf ל-pdf נפרדים, פיצול pdf c#
description: נושא זה מדגים כיצד לפצל דפי PDF לקבצי PDF נפרדים ביישומי .NET שלך באמצעות C#.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
aliases:
    - /net/split-document/
    - /net/split-pdf-pages/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "פיצול קובץ PDF באופן תכנותי",
    "alternativeHeadline": "כיצד לפצל PDF עם .NET",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "יצירת מסמכי PDF",
    "keywords": "pdf, c#, פיצול pdf",
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
    "url": "/net/split-pdf-document/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/split-pdf-document/"
    },
    "dateModified": "2022-02-04",
    "description": "נושא זה מדגים כיצד לפצל דפי PDF לקבצי PDF נפרדים ביישומי .NET שלך באמצעות C#."
}
</script>
## דוגמה חיה

[Aspose.PDF Splitter](https://products.aspose.app/pdf/splitter) הוא יישום אינטרנט חינמי שמאפשר לך לחקור איך פונקציונליות פיצול הצגות עובדת.

[![Aspose Split PDF](splitter.png)](https://products.aspose.app/pdf/splitter)

נושא זה מראה איך לפצל דפי PDF לקבצי PDF נפרדים ביישומי ה-.NET שלך. כדי לפצל דפי PDF לקבצי PDF בעמוד בודד באמצעות C#, ניתן לבצע את השלבים הבאים:

1. עבור בלולאה דרך דפי מסמך PDF דרך אוסף [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection) של אובייקט [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document)
1. בכל איטרציה, צור אובייקט מסמך חדש והוסף את אובייקט [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) הבודד למסמך הריק
1. שמור את ה-PDF החדש באמצעות שיטת [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4)

הקטע קוד הבא עובד גם עם ספריית [Aspose.PDF.Drawing](/pdf/net/drawing/).
קוד זה עובד גם עם הספרייה [Aspose.PDF.Drawing](/pdf/net/drawing/).

## לפצל מסמך PDF לקבצים מרובים או PDFs נפרדים ב-C#

הקטע הבא של קוד C# מדגים איך לפצל דפי PDF לקבצי PDF נפרדים.

```csharp
// לדוגמאות מלאות וקבצי נתונים, אנא בקרו ב https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לתיקיית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_Pages();

// פתח מסמך
Document pdfDocument = new Document(dataDir + "SplitToPages.pdf");

int pageCount = 1;

// עבור על כל הדפים
foreach (Page pdfPage in pdfDocument.Pages)
{
    Document newDocument = new Document();
    newDocument.Pages.Add(pdfPage);
    newDocument.Save(dataDir + "page_" + pageCount + "_out" + ".pdf");
    pageCount++;
}
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

