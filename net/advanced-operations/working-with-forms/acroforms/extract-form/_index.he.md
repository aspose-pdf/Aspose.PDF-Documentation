---
title: חילוץ AcroForm - חילוץ נתוני טופס ממסמך PDF ב-C#
linktitle: חילוץ AcroForm
type: docs
weight: 30
url: /net/extract-form/
keywords: extract form data from pdf c#
description: חלץ טופס ממסמך ה-PDF שלך באמצעות ספריית Aspose.PDF עבור .NET. קבל ערך משדה יחיד בקובץ PDF.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "חילוץ AcroForm",
    "alternativeHeadline": "איך לחלץ AcroForm מ-PDF",
    "author": {
        "@type": "Person",
        "name":"אנסטסיה הולוב",
        "givenName": "אנסטסיה",
        "familyName": "הולוב",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "יצירת מסמכי PDF",
    "keywords": "pdf, c#, extract acroform",
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
    "url": "/net/extract-form/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/extract-form/"
    },
    "dateModified": "2022-02-04",
    "description": "חלץ טופס ממסמך ה-PDF שלך באמצעות ספריית Aspose.PDF עבור .NET. קבל ערך משדה יחיד בקובץ PDF."
}
</script>
הקוד הבא עובד גם עם ספריית [Aspose.PDF.Drawing](/pdf/net/drawing/).

## חילוץ נתונים מטופס

### קבלת ערכים מכל השדות של מסמך PDF

כדי לקבל ערכים מכל השדות במסמך PDF, עליך לנווט בכל שדות הטופס ולאחר מכן לקבל את הערך באמצעות התכונה Value. קבל כל שדה מאוסף הטופס, בסוג השדה הבסיסי הנקרא Field וגש לתכונת ה-Value שלו.

הקטעי קוד ב-C# הבאים מראים כיצד לקבל את ערכי כל השדות ממסמך PDF.

```csharp
// לדוגמאות מלאות וקבצי נתונים, אנא עבור אל https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לתיקיית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

// פתיחת מסמך
Document pdfDocument = new Document(dataDir + "GetValuesFromAllFields.pdf");

// קבלת ערכים מכל השדות
foreach (Field formField in pdfDocument.Form)
{
    Console.WriteLine("שם השדה : {0} ", formField.PartialName);
    Console.WriteLine("ערך : {0} ", formField.Value);
}
```
### קבלת ערך משדה יחיד במסמך PDF

נכס ה-Value של שדה הטופס מאפשר לך לקבל את ערך שדה מסוים. כדי לקבל את הערך, קבל את שדה הטופס מאוסף ה-Form של אובייקט ה-Document. דוגמה זו ב-C# בוחרת [TextBoxField](https://reference.aspose.com/pdf/net/aspose.pdf.forms/textboxfield) ומאחזרת את ערכו באמצעות נכס ה-Value.

```csharp
// לדוגמאות מלאות וקבצי נתונים, אנא עבור ל https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לספריית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

// פתיחת מסמך
Document pdfDocument = new Document(dataDir + "GetValueFromField.pdf");

// קבלת שדה
TextBoxField textBoxField = pdfDocument.Form["textbox1"] as TextBoxField;

// קבלת ערך השדה
Console.WriteLine("PartialName : {0} ", textBoxField.PartialName);
Console.WriteLine("Value : {0} ", textBoxField.Value);
```

כדי לקבל את כתובת ה-URL של כפתור השליחה, השתמש בשורות הקוד הבאות.

```csharp
// לדוגמאות מלאות וקבצי נתונים, אנא עבור ל https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לספריית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

// פתיחת מסמך
Document pdfDocument = new Document(dataDir + "GetValueFromField.pdf");
SubmitFormAction act = pdfDocument.Form[1].OnActivated as SubmitFormAction;
if(act != null)
Console.WriteLine(act.Url.Name);
```
### קבל שדות טופס מאזור מסוים בקובץ PDF

לפעמים, ייתכן שתדעו היכן במסמך נמצא שדה טופס, אך לא תדעו את שמו. לדוגמה, אם יש לכם רק תוכנית של טופס מודפס. עם Aspose.PDF עבור .NET, זה לא בעיה. תוכלו לגלות אילו שדות נמצאים באזור מסוים של קובץ PDF. כדי לקבל שדות טופס מאזור מסוים בקובץ PDF:

1. פתח את קובץ ה-PDF באמצעות אובייקט [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).
1. קבל את הטופס מאוסף הטפסים של המסמך.
1. ציין את האזור המלבני והעבר אותו לשיטת GetFieldsInRect של אובייקט הטופס. נחזיר אוסף שדות.
1. השתמש בזה כדי לתפעל את השדות.

הקטע קוד C# הבא מראה כיצד לקבל שדות טופס באזור מלבני מסוים של קובץ PDF.

```csharp
// לדוגמאות מלאות וקבצי נתונים, בקר נא ב https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לתיקיית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

// פתח קובץ pdf
Aspose.Pdf.Document doc = new Aspose.Pdf.Document(dataDir + "GetFieldsFromRegion.pdf");

// צור אובייקט מלבן כדי לקבל שדות באזור זה
Aspose.Pdf.Rectangle rectangle = new Aspose.Pdf.Rectangle(35, 30, 500, 500);

// קבל את טופס ה-PDF
Aspose.Pdf.Forms.Form form = doc.Form;

// קבל שדות באזור המלבני
Aspose.Pdf.Forms.Field[] fields = form.GetFieldsInRect(rectangle);

// הצג שמות וערכים של שדות
foreach (Field field in fields)
{
    // הצג תכונות הצבת תמונה עבור כל הצבות
    Console.Out.WriteLine("שם שדה: " + field.FullName + "-" + "ערך שדה: " + field.Value);
}
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

