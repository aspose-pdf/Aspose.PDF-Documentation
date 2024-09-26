---
title: הוספת מספר עמוד ל-PDF באמצעות C#
linktitle: הוספת מספר עמוד
type: docs
weight: 100
url: /net/add-page-number/
description: Aspose.PDF עבור .NET מאפשר לך להוסיף חותמת מספר עמוד לקובץ PDF שלך באמצעות מחלקת PageNumber Stamp.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
aliases:
    - /net/get-and-set-page-properties/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "הוספת מספר עמוד ל-PDF באמצעות C#",
    "alternativeHeadline": "איך להוסיף חותמת מספר עמוד ל-PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "יצירת מסמכי PDF",
    "keywords": "pdf, c#, חותמת מספר עמוד",
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
    "url": "/net/add-page-number/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-page-number/"
    },
    "dateModified": "2022-02-04",
    "description": "Aspose.PDF עבור .NET מאפשר לך להוסיף חותמת מספר עמוד לקובץ PDF שלך באמצעות מחלקת PageNumber Stamp."
}
</script>
כל המסמכים חייבים לכלול מספרי עמודים בהם. מספר העמוד מקל על הקורא לאתר חלקים שונים של המסמך.
**Aspose.PDF for .NET** מאפשר לך להוסיף מספרי עמודים עם PageNumberStamp.

הקטע קוד הבא עובד גם עם ספריית [Aspose.PDF.Drawing](/pdf/net/drawing/).

ניתן להשתמש במחלקת [PageNumberStamp](https://reference.aspose.com/pdf/net/aspose.pdf/pagenumberstamp) כדי להוסיף חותמת מספר עמוד בקובץ PDF.
אתה יכול להשתמש במחלקה [PageNumberStamp](https://reference.aspose.com/pdf/net/aspose.pdf/pagenumberstamp) כדי להוסיף חותמת מספר עמוד בקובץ PDF.

```csharp
// לדוגמאות מלאות וקבצי נתונים, אנא עבור ל https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לספריית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

// פתח מסמך
Document pdfDocument = new Document(dataDir+ "PageNumberStamp.pdf");

// צור חותמת מספר עמוד
PageNumberStamp pageNumberStamp = new PageNumberStamp();
// האם החותמת היא רקע
pageNumberStamp.Background = false;
pageNumberStamp.Format = "עמוד # מתוך " + pdfDocument.Pages.Count;
pageNumberStamp.BottomMargin = 10;
pageNumberStamp.HorizontalAlignment = HorizontalAlignment.Center;
pageNumberStamp.StartingNumber = 1;
// הגדר תכונות טקסט
pageNumberStamp.TextState.Font = FontRepository.FindFont("Arial");
pageNumberStamp.TextState.FontSize = 14.0F;
pageNumberStamp.TextState.FontStyle = FontStyles.Bold;
pageNumberStamp.TextState.FontStyle = FontStyles.Italic;
pageNumberStamp.TextState.ForegroundColor = Color.Aqua;

// הוסף חותמת לעמוד מסוים
pdfDocument.Pages[1].AddStamp(pageNumberStamp);

dataDir = dataDir + "PageNumberStamp_out.pdf";
// שמור מסמך פלט
pdfDocument.Save(dataDir);
```
## דוגמה חיה

[הוספת מספרי עמודים ל-PDF](https://products.aspose.app/pdf/page-number) היא אפליקציה מקוונת חינמית שמאפשרת לך לחקור איך פועלת הפונקציונליות של הוספת מספרי עמודים.

[![איך להוסיף מספר עמוד ב-pdf באמצעות C#](page_number.png)](https://products.aspose.app/pdf/page-number)

## הוספה/הסרה של מספור בייטס

**מספור בייטס** (ידוע גם כחותמת בייטס) משמש בתחומים המשפטיים, הרפואיים והעסקיים לשים מספרים מזהים ו/או חותמות תאריך/שעה על תמונות ומסמכים ככל שהם נסרקים או מעובדים, לדוגמה, במהלך שלב הגילוי של הכנות למשפט או זיהוי קבלות עסקיות. תהליך זה מספק זיהוי, הגנה, ומספור עוקב אוטומטי של התמונות או המסמכים.

Aspose.PDF תומך באופן מוגבל במספור בייטס כרגע. פונקציונליות זו תעודכן על פי בקשות לקוחות.

### איך להסיר מספור בייטס

```csharp
static void Demo03()
{
    Document doc = new Document(@"C:\Samples\Sample-Document03.pdf");
    foreach (var page in doc.Pages)
    {
        var batesNum = page.Artifacts.First(ar => ar.CustomSubtype == "BatesN");
        page.Artifacts.Delete(batesNum);
    }
    doc.Save(@"C:\Samples\Sample-Document04.pdf");
}
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

