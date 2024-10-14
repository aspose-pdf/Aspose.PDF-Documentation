---
title: חלץ ושמור קובץ מצורף
linktitle: חלץ ושמור קובץ מצורף
type: docs
weight: 20
url: /net/extract-and-save-an-attachment/
description: Aspose.PDF עבור .NET מאפשר לך לקבל את כל הקבצים המצורפים ממסמך PDF. כמו כן, אתה יכול לקבל קובץ מצורף בודד מהמסמך שלך.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "חלץ ושמור קובץ מצורף",
    "alternativeHeadline": "איך לחלץ ולשמור קבצים מצורפים",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "יצירת מסמך PDF",
    "keywords": "pdf, c#, שמירת קבצים מצורפים, חילוץ קבצים מצורפים",
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
    "url": "/net/extract-and-save-an-attachment/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/extract-and-save-an-attachment/"
    },
    "dateModified": "2022-02-04",
    "description": "Aspose.PDF עבור .NET מאפשר לך לקבל את כל הקבצים המצורפים ממסמך PDF. כמו כן, אתה יכול לקבל קובץ מצורף בודד מהמסמך שלך."
}
</script>
## קבל את כל הקבצים המצורפים

עם Aspose.PDF, ניתן לקבל את כל הקבצים המצורפים ממסמך PDF. זה שימושי גם כאשר אתה רוצה לשמור את המסמכים בנפרד מה-PDF, או אם אתה צריך להסיר קבצים מצורפים מ-PDF.

כדי לקבל את כל הקבצים המצורפים מקובץ PDF:

1. עבור על אוסף [EmbeddedFiles](https://reference.aspose.com/pdf/net/aspose.pdf/embeddedfilecollection) של אובייקט [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document). האוסף [EmbeddedFiles](https://reference.aspose.com/pdf/net/aspose.pdf/embeddedfilecollection) מכיל את כל הקבצים המצורפים. כל אלמנט באוסף זה מייצג אובייקט [FileSpecification](https://reference.aspose.com/pdf/net/aspose.pdf/filespecification). כל איטרציה בלולאת foreach דרך אוסף [EmbeddedFiles](https://reference.aspose.com/pdf/net/aspose.pdf/embeddedfilecollection) מחזירה אובייקט [FileSpecification](https://reference.aspose.com/pdf/net/aspose.pdf/filespecification).
1.
1.

הקטעי קוד הבאים מראים כיצד לקבל את כל הקבצים המצורפים ממסמך PDF.

הקטע קוד הבא עובד גם עם ספריית [Aspose.PDF.Drawing](/pdf/net/drawing/).

```csharp
// לדוגמאות מלאות וקבצי נתונים, אנא בקרו ב https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לספריית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_Attachments();

// פתח מסמך
Document pdfDocument = new Document(dataDir + "GetAlltheAttachments.pdf");

// קבל את אוסף הקבצים המוטמעים
EmbeddedFileCollection embeddedFiles = pdfDocument.EmbeddedFiles;

// קבל את מספר הקבצים המוטמעים
Console.WriteLine("סך הכל קבצים : {0}", embeddedFiles.Count);

int count = 1;

// עבור על האוסף כדי לקבל את כל הקבצים המצורפים
foreach (FileSpecification fileSpecification in embeddedFiles)
{
    Console.WriteLine("שם: {0}", fileSpecification.Name);
    Console.WriteLine("תיאור: {0}",
    fileSpecification.Description);
    Console.WriteLine("סוג MIME: {0}", fileSpecification.MIMEType);

    // בדוק אם אובייקט הפרמטר מכיל את הפרמטרים
    if (fileSpecification.Params != null)
    {
        Console.WriteLine("סכום ביקורת: {0}",
        fileSpecification.Params.CheckSum);
        Console.WriteLine("תאריך יצירה: {0}",
        fileSpecification.Params.CreationDate);
        Console.WriteLine("תאריך שינוי: {0}",
        fileSpecification.Params.ModDate);
        Console.WriteLine("גודל: {0}", fileSpecification.Params.Size);
    }

    // קבל את הקובץ המצורף וכתוב לקובץ או לזרם
    byte[] fileContent = new byte[fileSpecification.Contents.Length];
    fileSpecification.Contents.Read(fileContent, 0,
    fileContent.Length);
    FileStream fileStream = new FileStream(dataDir + count + "_out" + ".txt",
    FileMode.Create);
    fileStream.Write(fileContent, 0, fileContent.Length);
    fileStream.Close();
    count+=1;
}
```
## קבל קובץ מצורף יחיד

כדי לקבל קובץ מצורף יחיד, ניתן לציין את האינדקס של הקובץ באובייקט `EmbeddedFiles` של מופע המסמך. אנא נסה להשתמש בקטע הקוד הבא.

```csharp
// לדוגמאות מלאות וקבצי נתונים, אנא עבור אל https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לתיקיית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_Attachments();

// פתח מסמך
Document pdfDocument = new Document(dataDir + "GetIndividualAttachment.pdf");

// קבל קובץ משובץ מסוים
FileSpecification fileSpecification = pdfDocument.EmbeddedFiles[1];

// קבל את תכונות הקובץ
Console.WriteLine("שם: {0}", fileSpecification.Name);
Console.WriteLine("תיאור: {0}", fileSpecification.Description);
Console.WriteLine("סוג MIME: {0}", fileSpecification.MIMEType);

// בדוק אם אובייקט הפרמטרים מכיל את הפרמטרים
if (fileSpecification.Params != null)
{
    Console.WriteLine("סכום ביקורת: {0}",
    fileSpecification.Params.CheckSum);
    Console.WriteLine("תאריך יצירה: {0}",
    fileSpecification.Params.CreationDate);
    Console.WriteLine("תאריך שינוי: {0}",
    fileSpecification.Params.ModDate);
    Console.WriteLine("גודל: {0}", fileSpecification.Params.Size);
}


// קבל את הקובץ וכתוב לקובץ או לזרם
byte[] fileContent = new byte[fileSpecification.Contents.Length];
fileSpecification.Contents.Read(fileContent, 0, fileContent.Length);

FileStream fileStream = new FileStream(dataDir + "test_out" + ".txt", FileMode.Create);
fileStream.Write(fileContent, 0, fileContent.Length);
fileStream.Close();
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

