---
title: סובב טקסט בתוך PDF באמצעות C#
linktitle: סובב טקסט בתוך PDF
type: docs
weight: 50
url: /net/rotate-text-inside-pdf/
description: למד שיטות שונות לסובב טקסט ל-PDF. Aspose.PDF מאפשר לך לסובב טקסט לכל זווית, לסובב קטע טקסט או פסקה שלמה.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "סובב טקסט בתוך PDF באמצעות C#",
    "alternativeHeadline": "איך לסובב טקסט בקובץ PDF",
    "author": {
        "@type": "Person",
        "name":"אנסטסיה הולוב",
        "givenName": "אנסטסיה",
        "familyName": "הולוב",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "יצירת מסמך PDF",
    "keywords": "pdf, c#, יצירת מסמכים",
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
    "url": "/net/rotate-text-inside-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/rotate-text-inside-pdf/"
    },
    "dateModified": "2022-02-04",
    "description": "למד שיטות שונות לסובב טקסט ל-PDF. Aspose.PDF מאפשר לך לסובב טקסט לכל זווית, לסובב קטע טקסט או פסקה שלמה."
}
</script>
הקטע הבא עובד גם עם ספריית [Aspose.PDF.Drawing](/pdf/net/drawing/).

## סיבוב טקסט בתוך PDF באמצעות התכונה Rotation

באמצעות התכונה Rotation של מחלקת [TextFragment](https://reference.aspose.com/pdf/net/aspose.pdf.text/textfragment), ניתן לסובב טקסט בזוויות שונות. סיבוב הטקסט יכול להיות שימושי בתרחישים שונים של יצירת מסמכים. ניתן לציין את זווית הסיבוב במעלות על מנת לסובב את הטקסט לפי הדרישה שלך. אנא בדוק את התרחישים השונים הבאים, בהם תוכל ליישם סיבוב טקסט.

## יישום סיבוב באמצעות TextFragment ו-TextBuilder

```csharp
// לדוגמאות מלאות וקבצי נתונים, אנא עבור ל https://github.com/aspose-pdf/Aspose.PDF-for-.NET
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// אתחול אובייקט מסמך
Document pdfDocument = new Document();
// קבלת עמוד מסוים
Page pdfPage = (Page)pdfDocument.Pages.Add();
// יצירת פרגמנט טקסט
TextFragment textFragment1 = new TextFragment("main text");
textFragment1.Position = new Position(100, 600);
// הגדרת תכונות טקסט
textFragment1.TextState.FontSize = 12;
textFragment1.TextState.Font = FontRepository.FindFont("TimesNewRoman");
// יצירת פרגמנט טקסט מסובב
TextFragment textFragment2 = new TextFragment("rotated text");
textFragment2.Position = new Position(200, 600);
// הגדרת תכונות טקסט
textFragment2.TextState.FontSize = 12;
textFragment2.TextState.Font = FontRepository.FindFont("TimesNewRoman");
textFragment2.TextState.Rotation = 45;
// יצירת פרגמנט טקסט מסובב
TextFragment textFragment3 = new TextFragment("rotated text");
textFragment3.Position = new Position(300, 600);
// הגדרת תכונות טקסט
textFragment3.TextState.FontSize = 12;
textFragment3.TextState.Font = FontRepository.FindFont("TimesNewRoman");
textFragment3.TextState.Rotation = 90;
// יצירת אובייקט TextBuilder
TextBuilder textBuilder = new TextBuilder(pdfPage);
// הוספת פרגמנט הטקסט לעמוד PDF
textBuilder.AppendText(textFragment1);
textBuilder.AppendText(textFragment2);
textBuilder.AppendText(textFragment3);
// שמירת המסמך
pdfDocument.Save(dataDir + "TextFragmentTests_Rotated1_out.pdf");
```
## יישום סיבוב באמצעות TextParagraph ו-TextBuilder (קטעים מסובבים)

```csharp
// לדוגמאות מלאות וקבצי נתונים, אנא עבורו ל https://github.com/aspose-pdf/Aspose.PDF-for-.NET
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// האתחול של אובייקט המסמך
Document pdfDocument = new Document();
// קבלת עמוד מסוים
Page pdfPage = (Page)pdfDocument.Pages.Add();
TextParagraph paragraph = new TextParagraph();
paragraph.Position = new Position(200, 600);
// יצירת קטע טקסט
TextFragment textFragment1 = new TextFragment("טקסט מסובב");
// הגדרת מאפייני הטקסט
textFragment1.TextState.FontSize = 12;
textFragment1.TextState.Font = FontRepository.FindFont("TimesNewRoman");
// הגדרת סיבוב
textFragment1.TextState.Rotation = 45;
// יצירת קטע טקסט
TextFragment textFragment2 = new TextFragment("טקסט ראשי");
// הגדרת מאפייני הטקסט
textFragment2.TextState.FontSize = 12;
textFragment2.TextState.Font = FontRepository.FindFont("TimesNewRoman");
// יצירת קטע טקסט
TextFragment textFragment3 = new TextFragment("טקסט מסובב נוסף");
// הגדרת מאפייני הטקסט
textFragment3.TextState.FontSize = 12;
textFragment3.TextState.Font = FontRepository.FindFont("TimesNewRoman");
// הגדרת סיבוב
textFragment3.TextState.Rotation = -45;
// הוספת קטעי הטקסט לפסקה
paragraph.AppendLine(textFragment1);
paragraph.AppendLine(textFragment2);
paragraph.AppendLine(textFragment3);
// יצירת אובייקט TextBuilder
TextBuilder textBuilder = new TextBuilder(pdfPage);
// הוספת הפסקה לעמוד ה-PDF
textBuilder.AppendParagraph(paragraph);
// שמירת המסמך
pdfDocument.Save(dataDir + "TextFragmentTests_Rotated2_out.pdf");
```
## יישום סיבוב באמצעות TextFragment ו-Page.Paragraphs

```csharp
// לדוגמאות מלאות וקבצי נתונים, אנא עבורו ל https://github.com/aspose-pdf/Aspose.PDF-for-.NET
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// אתחול אובייקט מסמך
Document pdfDocument = new Document();
// קבלת דף מסוים
Page pdfPage = (Page)pdfDocument.Pages.Add();
// יצירת קטע טקסט
TextFragment textFragment1 = new TextFragment("טקסט ראשי");
// הגדרת מאפייני הטקסט
textFragment1.TextState.FontSize = 12;
textFragment1.TextState.Font = FontRepository.FindFont("TimesNewRoman");
// יצירת קטע טקסט
TextFragment textFragment2 = new TextFragment("טקסט מסובב");
// הגדרת מאפייני הטקסט
textFragment2.TextState.FontSize = 12;
textFragment2.TextState.Font = FontRepository.FindFont("TimesNewRoman");
// הגדרת סיבוב
textFragment2.TextState.Rotation = 315;
// יצירת קטע טקסט
TextFragment textFragment3 = new TextFragment("טקסט מסובב");
// הגדרת מאפייני הטקסט
textFragment3.TextState.FontSize = 12;
textFragment3.TextState.Font = FontRepository.FindFont("TimesNewRoman");
// הגדרת סיבוב
textFragment3.TextState.Rotation = 270;
pdfPage.Paragraphs.Add(textFragment1);
pdfPage.Paragraphs.Add(textFragment2);
pdfPage.Paragraphs.Add(textFragment3);
// שמירת המסמך
pdfDocument.Save(dataDir + "TextFragmentTests_Rotated3_out.pdf");
```
## יישום סיבוב באמצעות TextParagraph ו-TextBuilder (פסקה שלמה מסתובבת)

```csharp
// לדוגמאות מלאות וקבצי נתונים, אנא בקרו ב https://github.com/aspose-pdf/Aspose.PDF-for-.NET
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// אתחול אובייקט מסמך
Document pdfDocument = new Document();
// קבלת עמוד מסוים
Page pdfPage = (Page)pdfDocument.Pages.Add();
for (int i = 0; i < 4; i++)
{
    TextParagraph paragraph = new TextParagraph();
    paragraph.Position = new Position(200, 600);
    // ציון סיבוב
    paragraph.Rotation = i * 90 + 45;
    // יצירת קטע טקסט
    TextFragment textFragment1 = new TextFragment("טקסט פסקה");
    // יצירת קטע טקסט
    textFragment1.TextState.FontSize = 12;
    textFragment1.TextState.Font = FontRepository.FindFont("TimesNewRoman");
    textFragment1.TextState.BackgroundColor = Aspose.Pdf.Color.LightGray;
    textFragment1.TextState.ForegroundColor = Aspose.Pdf.Color.Blue;
    // יצירת קטע טקסט
    TextFragment textFragment2 = new TextFragment("שורה שנייה של טקסט");
    // הגדרת מאפייני טקסט
    textFragment2.TextState.FontSize = 12;
    textFragment2.TextState.Font = FontRepository.FindFont("TimesNewRoman");
    textFragment2.TextState.BackgroundColor = Aspose.Pdf.Color.LightGray;
    textFragment2.TextState.ForegroundColor = Aspose.Pdf.Color.Blue;
    // יצירת קטע טקסט
    TextFragment textFragment3 = new TextFragment("ועוד טקסט...");
    // הגדרת מאפייני טקסט
    textFragment3.TextState.FontSize = 12;
    textFragment3.TextState.Font = FontRepository.FindFont("TimesNewRoman");
    textFragment3.TextState.BackgroundColor = Aspose.Pdf.Color.LightGray;
    textFragment3.TextState.ForegroundColor = Aspose.Pdf.Color.Blue;
    textFragment3.TextState.Underline = true;
    paragraph.AppendLine(textFragment1);
    paragraph.AppendLine(textFragment2);
    paragraph.AppendLine(textFragment3);
    // יצירת אובייקט TextBuilder
    TextBuilder textBuilder = new TextBuilder(pdfPage);
    // הוספת קטע הטקסט לעמוד PDF
    textBuilder.AppendParagraph(paragraph);
}
// שמירת המסמך
pdfDocument.Save(dataDir + "TextFragmentTests_Rotated4_out.pdf");
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
                "availableLanguage": "אנגלית"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "מכירות",
                "areaServed": "GB",
                "availableLanguage": "אנגלית"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "מכירות",
                "areaServed": "AU",
                "availableLanguage": "אנגלית"
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

