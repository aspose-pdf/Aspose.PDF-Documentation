---
title: הוספת חותמות תמונה ב-PDF באמצעות C#
linktitle: חותמות תמונה בקובץ PDF
type: docs
weight: 10
url: /net/image-stamps-in-pdf-page/
description: הוספת חותמת תמונה במסמך PDF שלך באמצעות מחלקת ImageStamp עם ספריית Aspose.PDF.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "הוספת חותמות תמונה ב-PDF באמצעות C#",
    "alternativeHeadline": "הוספת חותמות תמונה ב-PDF באמצעות C#",
    "author": {
        "@type": "Person",
        "name":"Andriy Andrukhovskiy",
        "givenName": "Andriy",
        "familyName": "Andrukhovskiy",
        "url":"https://www.linkedin.com/in/andruhovski/"
    },
    "genre": "יצירת מסמכים ב-PDF",
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
    "url": "/net/image-stamps-in-pdf-page/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/image-stamps-in-pdf-page/"
    },
    "dateModified": "2022-02-04",
    "description": "הוספת חותמת תמונה במסמך PDF שלך באמצעות מחלקת ImageStamp עם ספריית Aspose.PDF."
}
</script>
## הוספת חותמת תמונה בקובץ PDF

ניתן להשתמש במחלקת ImageStamp כדי להוסיף חותמת תמונה לקובץ PDF. מחלקת ImageStamp מספקת את התכונות הנדרשות ליצירת חותמת מבוססת תמונה, כגון גובה, רוחב, שקיפות וכו'.

הדוגמא לקוד הבאה עובדת גם עם ספריית [Aspose.PDF.Drawing](/pdf/net/drawing/).

כדי להוסיף חותמת תמונה:

1. יצירת אובייקט מסמך ואובייקט ImageStamp באמצעות התכונות הנדרשות.
1. קריאה למתודת AddStamp של מחלקת Page כדי להוסיף את החותמת ל-PDF.

הדוגמא לקוד הבאה מראה איך להוסיף חותמת תמונה בקובץ PDF.

```csharp
// לדוגמאות מלאות וקבצי נתונים, אנא עבורו ל https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לתיקיית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

// פתיחת מסמך
Document pdfDocument = new Document(dataDir+ "AddImageStamp.pdf");

// יצירת חותמת תמונה
ImageStamp imageStamp = new ImageStamp(dataDir + "aspose-logo.jpg");
imageStamp.Background = true;
imageStamp.XIndent = 100;
imageStamp.YIndent = 100;
imageStamp.Height = 300;
imageStamp.Width = 300;
imageStamp.Rotate = Rotation.on270;
imageStamp.Opacity = 0.5;
// הוספת חותמת לדף מסוים
pdfDocument.Pages[1].AddStamp(imageStamp);

dataDir = dataDir + "AddImageStamp_out.pdf";
// שמירת מסמך הפלט
pdfDocument.Save(dataDir);
```
## שליטה באיכות תמונה בעת הוספת חותמת

כאשר מוסיפים תמונה כעצם חותמת, ניתן לשלוט באיכות התמונה. מאפיין האיכות של מחלקת ImageStamp משמש למטרה זו. הוא מציין את איכות התמונה באחוזים (ערכים חוקיים הם 0..100).

```csharp
// לדוגמאות מלאות וקבצי נתונים, אנא עבורו ל https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לתיקיית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

// פתיחת מסמך
Document pdfDocument = new Document(dataDir+ "AddImageStamp.pdf");

// יצירת חותמת תמונה
ImageStamp imageStamp = new ImageStamp(dataDir + "aspose-logo.jpg");

imageStamp.Quality = 10;
pdfDocument.Pages[1].AddStamp(imageStamp);
pdfDocument.Save(dataDir + "ControlImageQuality_out.pdf");
```

## חותמת תמונה כרקע בתיבה צפה

API של Aspose.PDF מאפשר להוסיף חותמת תמונה כרקע בתיבה צפה.
ממשק ה- API של Aspose.PDF מאפשר לך להוסיף חותמת תמונה כרקע בתיבה צפה.

```csharp
// לדוגמאות מלאות וקבצי נתונים, אנא בקר ב https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לספריית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

// יצירת אובייקט מסמך
Document doc = new Document();
// הוספת דף למסמך PDF
Page page = doc.Pages.Add();
// יצירת אובייקט FloatingBox
FloatingBox aBox = new FloatingBox(200, 100);
// הגדרת מיקום שמאלי ל-FloatingBox
aBox.Left = 40;
// הגדרת מיקום עליון ל-FloatingBox
aBox.Top = 80;
// הגדרת יישור אופקי ל-FloatingBox
aBox.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Center;
// הוספת קטע טקסט לאוסף הפסקאות של FloatingBox
aBox.Paragraphs.Add(new TextFragment("טקסט ראשי"));
// הגדרת גבול ל-FloatingBox
aBox.Border = new BorderInfo(BorderSide.All, Aspose.Pdf.Color.Red);
// הוספת תמונת רקע
aBox.BackgroundImage = new Image
{
    File = dataDir + "aspose-logo.jpg"
};
// הגדרת צבע רקע ל-FloatingBox
aBox.BackgroundColor = Aspose.Pdf.Color.Yellow;
// הוספת FloatingBox לאוסף הפסקאות של אובייקט הדף
page.Paragraphs.Add(aBox);
// שמירת מסמך ה-PDF
doc.Save(dataDir + "AddImageStampAsBackgroundInFloatingBox_out.pdf");
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

