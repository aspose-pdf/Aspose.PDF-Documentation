---
title: הוספת קובץ מצורף למסמך PDF
linktitle: הוספת קובץ מצורף למסמך PDF
type: docs
weight: 10
url: /net/add-attachment-to-pdf-document/
description: דף זה מתאר איך להוסיף קובץ מצורף לקובץ PDF באמצעות הספרייה Aspose.PDF עבור .NET
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
aliases:
    - /net/adding-to-a-pdf-document/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "הוספת קובץ מצורף למסמך PDF",
    "alternativeHeadline": "איך להוסיף קבצים מצורפים ל-PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "יצירת מסמכי PDF",
    "keywords": "pdf, c#, קבצים מצורפים ב-pdf",
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
    "url": "/net/add-attachment-to-pdf-document/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-attachment-to-pdf-document/"
    },
    "dateModified": "2022-02-04",
    "description": "דף זה מתאר איך להוסיף קובץ מצורף לקובץ PDF באמצעות הספרייה Aspose.PDF עבור .NET"
}
</script>
נספחים יכולים להכיל מגוון רחב של מידע ויכולים להיות מסוגים שונים של קבצים. המאמר הזה מסביר איך להוסיף נספח לקובץ PDF.

הקטע קוד הבא עובד גם עם ממשק גרפי חדש של [Aspose.Drawing](/pdf/net/drawing/).

1. צור פרויקט C# חדש.
1. הוסף הפניה ל-DLL של Aspose.PDF.
1. צור אובייקט [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).
1. צור אובייקט [FileSpecification](https://reference.aspose.com/pdf/net/aspose.pdf/filespecification) עם הקובץ שאתה מוסיף, ותיאור הקובץ.
1. הוסף את אובייקט [FileSpecification](https://reference.aspose.com/pdf/net/aspose.pdf/filespecification) לאוסף [EmbeddedFiles](https://reference.aspose.com/pdf/net/aspose.pdf/embeddedfilecollection) של אובייקט [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document), באמצעות שיטת ה-Add של האוסף.

האוסף [EmbeddedFiles](https://reference.aspose.com/pdf/net/aspose.pdf/embeddedfilecollection) מכיל את כל הנספחים בקובץ PDF.
האוסף [EmbeddedFiles](https://reference.aspose.com/pdf/net/aspose.pdf/embeddedfilecollection) מכיל את כל הקבצים המצורפים בקובץ PDF.

```csharp
// לדוגמאות מלאות וקבצי נתונים, אנא בקר ב https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לתיקיית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_Attachments();

// פתיחת מסמך
Document pdfDocument = new Document(dataDir + "AddAttachment.pdf");

// הגדרת קובץ חדש להוספה כצירוף
FileSpecification fileSpecification = new FileSpecification(dataDir + "test.txt", "קובץ טקסט לדוגמה");

// הוספת צירוף לאוסף הצירופים של המסמך
pdfDocument.EmbeddedFiles.Add(fileSpecification);

// שמירת המסמך המעודכן
pdfDocument.Save(dataDir + "AddllAnnotations_out.pdf");
```

