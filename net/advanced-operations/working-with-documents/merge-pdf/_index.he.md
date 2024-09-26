---
title: איך למזג מסמכי PDF באמצעות C#
linktitle: מיזוג קבצי PDF
type: docs
weight: 50
url: /net/merge-pdf-documents/
keywords: "merge multiple pdf into single pdf c#, combine multiple pdf into one c#, merge multiple pdf into one c#"
description: דף זה מסביר כיצד למזג מסמכי PDF לקובץ PDF יחיד עם C# או VB.NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "איך למזג PDF באמצעות C#",
    "alternativeHeadline": "מיזוג מסמכי PDF",
    "author": {
        "@type": "Person",
        "name":"אנסטסיה הולוב",
        "givenName": "אנסטסיה",
        "familyName": "הולוב",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "מניפולציה של מסמכי PDF",
    "keywords": "pdf, c#, מיזוג pdf, חיבור, שילוב pdf",
    "wordcount": "212",
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
    "url": "https://docs.aspose.com/pdf/net/merge-pdf-documents/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "https://docs.aspose.com/pdf/net/merge-pdf-documents/"
    },
    "dateModified": "2022-02-04",
    "description": "דף זה מסביר כיצד למזג מסמכי PDF לקובץ PDF יחיד עם C# או VB.NET."
}
</script>
## מיזוג או שילוב מספר קבצי PDF לקובץ PDF יחיד ב-C#

מיזוג PDF ב-C# אינו משימה פשוטה ללא שימוש בספרייה של צד שלישי.
המאמר הזה מראה איך למזג מספר קבצי PDF למסמך PDF יחיד באמצעות Aspose.PDF ל-.NET. הדוגמא כתובה ב-C# אך ה-API יכול להשתמש גם בשפות תכנות .NET אחרות כמו VB.NET. קבצי ה-PDF ממוזגים כך שהראשון מתווסף בסוף המסמך האחר.

הקטע קוד הבא גם עובד עם ספריית [Aspose.PDF.Drawing](/pdf/net/drawing/).

## מיזוג קבצי PDF באמצעות C# ו-DOM

לשרשור שני קבצי PDF:

1. צור שני אובייקטים [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document), כל אחד מכיל אחד מקבצי ה-PDF הקלט.
1. לאחר מכן קרא לשיטת Add של אוסף [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection) עבור אובייקט ה-Document שברצונך להוסיף אליו את קובץ ה-PDF האחר.
1.
1.
1. לבסוף, שמור את קובץ PDF הסופי באמצעות השיטה [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4).

הקטע הבא מציג איך לשרשר קבצי PDF.

```csharp
// הנתיב לתיקייה של המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_Pages();

// פתח מסמך ראשון
Document pdfDocument1 = new Document(dataDir + "Concat1.pdf");
// פתח מסמך שני
Document pdfDocument2 = new Document(dataDir + "Concat2.pdf");

// הוסף עמודים מהמסמך השני לראשון
pdfDocument1.Pages.Add(pdfDocument2.Pages);

dataDir = dataDir + "ConcatenatePdfFiles_out.pdf";
// שמור את קובץ הפלט המשורשר
pdfDocument1.Save(dataDir);
```

## דוגמה חיה

[Aspose.PDF Merger](https://products.aspose.app/pdf/merger) הוא אפליקציית ווב חינמית באינטרנט שמאפשרת לך לבחון איך פונקציונליות מיזוג המצגות עובדת.

[![Aspose.PDF Merger](merger.png)](https://products.aspose.app/pdf/merger)

## ראה גם

- [פיצול PDF באמצעות DOM](https://docs.aspose.com/pdf/net/split-pdf-document/)
- [פיצול PDF באמצעות DOM](https://docs.aspose.com/pdf/net/split-pdf-document/)
- [הצמדת מסמכי PDF באמצעות Facades](https://docs.aspose.com/pdf/net/concatenate-pdf-documents/)
- [פיצול PDF באמצעות Facades](https://docs.aspose.com/pdf/net/split-pdf-pages/)

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

