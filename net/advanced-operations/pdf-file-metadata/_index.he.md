---
title: עבודה עם מטא-דאטה של קובץ PDF | C#
linktitle: מטא-דאטה של קובץ PDF
type: docs
weight: 140
url: /net/pdf-file-metadata/
description: מדור זה מסביר כיצד לקבל מידע על קובץ PDF, איך לקבל מטא-דאטה XMP מקובץ PDF, להגדיר מידע על קובץ PDF.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "עבודה עם מטא-דאטה של קובץ PDF | C#",
    "alternativeHeadline": "איך לקבל מטא-דאטה של קובץ PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "יצירת מסמכי PDF",
    "keywords": "pdf, c#, מטא-דאטה של קובץ pdf",
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
    "url": "/net/pdf-file-metadata/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/pdf-file-metadata/"
    },
    "dateModified": "2022-02-04",
    "description": "מדור זה מסביר כיצד לקבל מידע על קובץ PDF, איך לקבל מטא-דאטה XMP מקובץ PDF, להגדיר מידע על קובץ PDF."
}
</script>
הקטע הבא של קוד עובד גם עם ספריית [Aspose.PDF.Drawing](/pdf/net/drawing/).

## קבלת מידע על קובץ PDF

כדי לקבל מידע ספציפי על קובץ PDF, תחילה עליך לקבל את אובייקט [DocumentInfo](https://reference.aspose.com/pdf/net/aspose.pdf/documentinfo) באמצעות תכונת [Info](https://reference.aspose.com/pdf/net/aspose.pdf/document/properties/info) של אובייקט [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document). לאחר שמתקבל אובייקט [DocumentInfo](https://reference.aspose.com/pdf/net/aspose.pdf/documentinfo), ניתן לקבל את ערכי התכונות השונות. הקטע הבא של קוד מראה איך לקבל מידע על קובץ PDF.

```csharp
// לדוגמאות מלאות וקבצי נתונים, אנא עבור ל https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לתיקיית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// פתיחת מסמך
Document pdfDocument = new Document(dataDir + "GetFileInfo.pdf");
// קבלת מידע על המסמך
DocumentInfo docInfo = pdfDocument.Info;
// הצגת מידע על המסמך
Console.WriteLine("Author: {0}", docInfo.Author);
Console.WriteLine("Creation Date: {0}", docInfo.CreationDate);
Console.WriteLine("Keywords: {0}", docInfo.Keywords);
Console.WriteLine("Modify Date: {0}", docInfo.ModDate);
Console.WriteLine("Subject: {0}", docInfo.Subject);
Console.WriteLine("Title: {0}", docInfo.Title);
```
## הגדרת מידע בקובץ PDF

Aspose.PDF עבור .NET מאפשר לך להגדיר מידע ספציפי לקובץ עבור PDF, כמו מחבר, תאריך יצירה, נושא וכותרת. כדי להגדר את המידע הזה:

1. צור אובייקט [DocumentInfo](https://reference.aspose.com/pdf/net/aspose.pdf/documentinfo).
1. הגדר את ערכי התכונות.
1. שמור את המסמך המעודכן באמצעות שיטת Save של מחלקת המסמך.

{{% alert color="primary" %}}

שים לב שאתה לא יכול להגדיר ערכים נגד השדות *Application* ו-*Producer*, מכיוון ש-Aspose Ltd. ו-Aspose.PDF עבור .NET x.x.x יוצגו נגד שדות אלה.

{{% /alert %}}

הקטע קוד הבא מראה לך איך להגדיר מידע בקובץ PDF.

```csharp
// לדוגמאות מלאות וקבצי נתונים, בבקשה עבור ל https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לתיקיית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// פתח מסמך
Document pdfDocument = new Document(dataDir + "SetFileInfo.pdf");

// ציין מידע על המסמך
DocumentInfo docInfo = new DocumentInfo(pdfDocument);

docInfo.Author = "Aspose";
docInfo.CreationDate = DateTime.Now;
docInfo.Keywords = "Aspose.Pdf, DOM, API";
docInfo.ModDate = DateTime.Now;
docInfo.Subject = "מידע PDF";
docInfo.Title = "הגדרת מידע על מסמך PDF";

dataDir = dataDir + "SetFileInfo_out.pdf";
// שמור מסמך פלט
pdfDocument.Save(dataDir);
```
## קבל מטא-נתונים של XMP מקובץ PDF

Aspose.PDF מאפשר לך לגשת למטא-נתונים של XMP בקובץ PDF. כדי לקבל את המטא-נתונים של הקובץ:

1. צור אובייקט [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) ופתח את קובץ ה-PDF הקלט.
1. קבל את מטא-נתוני הקובץ באמצעות תכונת [Metadata](https://reference.aspose.com/pdf/net/aspose.pdf/document/properties/metadata).

הקטע קוד הבא מראה לך איך לקבל מטא-נתונים מקובץ ה-PDF.

```csharp
// לדוגמאות מלאות וקבצי נתונים, אנא עבור ל https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לתיקיית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// פתח מסמך
Document pdfDocument = new Document(dataDir + "GetXMPMetadata.pdf");

// קבל תכונות
Console.WriteLine(pdfDocument.Metadata["xmp:CreateDate"]);
Console.WriteLine(pdfDocument.Metadata["xmp:Nickname"]);
Console.WriteLine(pdfDocument.Metadata["xmp:CustomProperty"]);
```

## הגדר מטא-נתוני XMP בקובץ PDF

Aspose.PDF מאפשר לך להגדיר מטא-נתונים בקובץ PDF.
Aspose.PDF מאפשר לך להגדיר מטא-דאטה בקובץ PDF.

1. צור אובייקט [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).
1. הגדר ערכי מטא-דאטה באמצעות התכונה [Metadata](https://reference.aspose.com/pdf/net/aspose.pdf/document/properties/metadata).
1. שמור את המסמך המעודכן באמצעות שיטת [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) של אובייקט [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).

הקטע קוד הבא מראה לך איך להגדיר מטא-דאטה בקובץ PDF.

```csharp
// לדוגמאות מלאות וקבצי נתונים, אנא עבור ל https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// נתיב לתיקיית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// פתח מסמך
Document pdfDocument = new Document(dataDir + "SetXMPMetadata.pdf");

// הגדר תכונות
pdfDocument.Metadata["xmp:CreateDate"] = DateTime.Now;
pdfDocument.Metadata["xmp:Nickname"] = "Nickname";
pdfDocument.Metadata["xmp:CustomProperty"] = "ערך מותאם";

dataDir = dataDir + "SetXMPMetadata_out.pdf";
// שמור מסמך
pdfDocument.Save(dataDir);
```
## הוספת מטא-דאטה עם קידומת

חלק מהמפתחים צריכים ליצור מרחב שמות מטא-דאטה חדש עם קידומת. קטע הקוד הבא מראה איך להוסיף מטא-דאטה עם קידומת.

```csharp
// לדוגמאות מלאות וקבצי נתונים, אנא עברו לכתובת https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לתיקיית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// פתיחת מסמך
Document pdfDocument = new Document(dataDir + "SetXMPMetadata.pdf");
pdfDocument.Metadata.RegisterNamespaceUri("xmp", "http:// Ns.adobe.com/xap/1.0/"); // הוסר קידומת Xmlns
pdfDocument.Metadata["xmp:ModifyDate"] = DateTime.Now;

dataDir = dataDir + "SetPrefixMetadata_out.pdf";
// שמירת המסמך
pdfDocument.Save(dataDir);
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


