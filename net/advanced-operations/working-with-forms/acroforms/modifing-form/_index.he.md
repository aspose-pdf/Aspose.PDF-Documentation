---
title: שינוי AcroForm
linktitle: שינוי AcroForm
type: docs
weight: 40
url: /net/modifing-form/
description: שינוי טופס בקובץ PDF שלך עם ספריית Aspose.PDF ל-.NET. תוכל להוסיף או להסיר שדות בטופס קיים, לקבל ולהגדיר מגבלת שדה וכו'.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "שינוי AcroForm",
    "alternativeHeadline": "כיצד לשנות AcroForm",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "יצירת מסמכי PDF",
    "keywords": "pdf, c#, שינוי acroform",
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
    "url": "/net/modifing-form/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/modifing-form/"
    },
    "dateModified": "2022-02-04",
    "description": "שינוי טופס בקובץ PDF שלך עם ספריית Aspose.PDF ל-.NET. תוכל להוסיף או להסיר שדות בטופס קיים, לקבל ולהגדיר מגבלת שדה וכו'."
}
</script>
הקוד הבא עובד גם עם ספריית [Aspose.PDF.Drawing](/pdf/net/drawing/).

## קבלה או הגדרה של הגבלת שדה

מחלקת FormEditor והמתודה SetFieldLimit(field, limit) מאפשרת לך להגדיר הגבלת שדה, מספר התווים המרבי שניתן להזין לשדה.

```csharp
// לדוגמאות מלאות וקבצי נתונים, בבקשה עבור אל https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// נתיב לתיקיית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

// הוספת שדה עם הגבלה
FormEditor form = new FormEditor();

form.BindPdf( dataDir + "input.pdf");
form.SetFieldLimit("textbox1", 15);
dataDir = dataDir + "SetFieldLimit_out.pdf";
form.Save(dataDir);
```

בדומה, ל-Aspose.PDF יש מתודה שמקבלת את הגבלת השדה באמצעות שיטת ה-DOM. קטע הקוד הבא מראה את השלבים.

```csharp
// לדוגמאות מלאות וקבצי נתונים, בבקשה עבור אל https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// נתיב לתיקיית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();
// קבלת מקסימום הגבלת שדה באמצעות DOM
Document doc = new Document(dataDir + "FieldLimit.pdf");
Console.WriteLine("Limit: " + (doc.Form["textbox1"] as TextBoxField).MaxLen);
```
ניתן לקבל את אותו הערך באמצעות מרחב השמות *Aspose.PDF.Facades* באמצעות קטע הקוד הבא.

```csharp
// לדוגמאות מלאות וקבצי נתונים, נא לעבור ל https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לספריית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();
// קבלת הגבלת שדה מרבית באמצעות Facades
Aspose.Pdf.Facades.Form form = new Aspose.Pdf.Facades.Form();
form.BindPdf(dataDir + "FieldLimit.pdf");
Console.WriteLine("Limit: " + form.GetFieldLimit("textbox1"));
```

## הגדרת גופן מותאם אישית לשדה הטופס

שדות טופס בקבצי PDF של Adobe ניתנים להגדרה לשימוש בגופנים ברירת מחדל מסוימים.
שדות טופס בקובצי Adobe PDF ניתן להגדירם לשימוש בגופנים ברירת מחדל מסוימים.

הקטע קוד הבא מראה איך להגדיר את גופן ברירת המחדל עבור שדות טופס PDF.

```csharp
// לדוגמאות מלאות וקבצי נתונים, אנא עבורו ל https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לתיקיית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

// פתח מסמך
Document pdfDocument = new Document(dataDir + "FormFieldFont14.pdf");

// קבל שדה טופס מסוים מהמסמך
Aspose.Pdf.Forms.Field field = pdfDocument.Form["textbox1"] as Aspose.Pdf.Forms.Field;

// צור אובייקט גופן
Aspose.Pdf.Text.Font font = FontRepository.FindFont("ComicSansMS");

// הגדר את מידע הגופן עבור שדה הטופס
// Field.DefaultAppearance = new Aspose.Pdf.Forms.in.DefaultAppearance(font, 10, System.Drawing.Color.Black);

dataDir = dataDir + "FormFieldFont14_out.pdf";
// שמור את המסמך שעודכן
pdfDocument.Save(dataDir);
```

## הוספה/הסרה של שדות בטופס קיים

כל שדות הטופס נמצאים באוסף Form של אובייקט ה-Document.
כל שדות הטופס מכילים באובייקט המסמך באוסף הטופס.

```csharp
// לדוגמאות מלאות וקבצי נתונים, אנא עבורו ל https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לספריית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

// פתח מסמך
Document pdfDocument = new Document(dataDir + "DeleteFormField.pdf");

// מחק שדה מסוים לפי שם
pdfDocument.Form.Delete("textbox1");
dataDir = dataDir + "DeleteFormField_out.pdf";
// שמור מסמך שהשתנה
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


