---
title: הוספת חותמות טקסט ב-PDF ב-C#
linktitle: חותמות טקסט בקובץ PDF
type: docs
weight: 20
url: /net/text-stamps-in-the-pdf-file/
description: הוספת חותמת טקסט למסמך PDF באמצעות המחלקה TextStamp עם ספריית Aspose.PDF עבור .NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "הוספת חותמות טקסט ב-PDF ב-C#",
    "alternativeHeadline": "הוספת חותמות טקסט ב-PDF ב-C#",
    "author": {
        "@type": "Person",
        "name":"אנדריי אנדרוחובסקי",
        "givenName": "אנדריי",
        "familyName": "אנדרוחובסקי",
        "url":"https://www.linkedin.com/in/andruhovski/"
    },
    "genre": "יצירת מסמכי PDF",
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
    "url": "/net/text-stamps-in-the-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/text-stamps-in-the-pdf-file/"
    },
    "dateModified": "2022-02-04",
    "description": "הוספת חותמת טקסט למסמך PDF באמצעות המחלקה TextStamp עם ספריית Aspose.PDF עבור .NET."
}
</script>
## הוספת חותמת טקסט ב-C#

ניתן להשתמש במחלקה [TextStamp](https://reference.aspose.com/pdf/net/aspose.pdf/TextStamp) כדי להוסיף חותמת טקסט בקובץ PDF. מחלקת TextStamp מספקת תכונות הדרושות ליצירת חותמת מבוססת טקסט כמו גודל גופן, סגנון גופן, וצבע הגופן וכו'. כדי להוסיף חותמת טקסט, עליך ליצור אובייקט Document ואובייקט TextStamp באמצעות התכונות הנדרשות. לאחר מכן, תוכל לקרוא לשיטת AddStamp של ה-Page כדי להוסיף את החותמת ב-PDF.

הקטע קוד הבא עובד גם עם ספריית [Aspose.PDF.Drawing](/pdf/net/drawing/).

הקטע קוד הבא מראה לך איך להוסיף חותמת טקסט בקובץ PDF.

```csharp
// לדוגמאות מלאות וקבצי נתונים, נא ללכת ל https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לתיקיית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

// פתח מסמך
Document pdfDocument = new Document(dataDir+ "AddTextStamp.pdf");

// צור חותמת טקסט
TextStamp textStamp = new TextStamp("Sample Stamp");
// הגדר האם החותמת היא רקע
textStamp.Background = true;
// הגדר מקור
textStamp.XIndent = 100;
textStamp.YIndent = 100;
// סובב חותמת
textStamp.Rotate = Rotation.on90;
// הגדר תכונות טקסט
textStamp.TextState.Font = FontRepository.FindFont("Arial");
textStamp.TextState.FontSize = 14.0F;
textStamp.TextState.FontStyle = FontStyles.Bold;
textStamp.TextState.FontStyle = FontStyles.Italic;
textStamp.TextState.ForegroundColor = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.Aqua);
// הוסף חותמת לדף מסוים
pdfDocument.Pages[1].AddStamp(textStamp);

dataDir = dataDir + "AddTextStamp_out.pdf";
// שמור מסמך פלט
pdfDocument.Save(dataDir);
```
## הגדרת יישור עבור אובייקט TextStamp

הוספת סימני מים למסמכי PDF היא אחת התכונות הנדרשות לעיתים קרובות ו-Aspose.PDF עבור .NET מסוגל להוסיף סימני מים בתמונה כמו גם בטקסט. יש לנו מחלקה בשם [TextStamp](https://reference.aspose.com/pdf/net/aspose.pdf/textstamp) שמספקת את היכולת להוסיף חותמות טקסט מעל קובץ PDF. לאחרונה הייתה דרישה לתמוך בתכונה לציין את יישור הטקסט בעת שימוש באובייקט TextStamp. כדי לעמוד בדרישה זו, הצגנו את המאפיין TextAlignment במחלקת TextStamp. באמצעות מאפיין זה, אנו יכולים לציין את יישור הטקסט האופקי.

הקטעי קוד הבאים מראים דוגמה על איך לטעון מסמך PDF קיים ולהוסיף מעליו TextStamp.

```csharp
// לדוגמאות מלאות וקבצי נתונים, אנא עבור ל https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לספריית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

// יצירת אובייקט מסמך עם קובץ קלט
Document doc = new Document(dataDir+ "DefineAlignment.pdf");
// יצירת אובייקט FormattedText עם מחרוזת לדוגמה
FormattedText text = new FormattedText("This");
// הוספת שורת טקסט חדשה ל-FormattedText
text.AddNewLineText("is sample");
text.AddNewLineText("Center Aligned");
text.AddNewLineText("TextStamp");
text.AddNewLineText("Object");
// יצירת אובייקט TextStamp באמצעות FormattedText
TextStamp stamp = new TextStamp(text);
// ציון יישור אופקי של חותמת הטקסט כממורכז
stamp.HorizontalAlignment = HorizontalAlignment.Center;
// ציון יישור אנכי של חותמת הטקסט כממורכז
stamp.VerticalAlignment = VerticalAlignment.Center;
// ציון יישור הטקסט האופקי של TextStamp כממורכז
stamp.TextAlignment = HorizontalAlignment.Center;
// הגדרת שולי עליון לאובייקט החותמת
stamp.TopMargin = 20;
// הוספת אובייקט החותמת מעל דף הראשון של המסמך
doc.Pages[1].AddStamp(stamp);

dataDir = dataDir + "StampedPDF_out.pdf";
// שמירת המסמך המעודכן
doc.Save(dataDir);
```
## מילוי טקסט מסוג קו כחותם בקובץ PDF

הטמענו הגדרה של מצב עיבוד טקסט לצורך הוספה ועריכה של טקסט. כדי לעבד טקסט מסוג קו, נא ליצור אובייקט TextState ולהגדיר את RenderingMode ל-TextRenderingMode.StrokeText וגם לבחור צבע עבור התכונה StrokingColor. לאחר מכן, יש לקשר את TextState לחותם באמצעות השיטה BindTextState().

הדוגמה הבאה מדגימה הוספת טקסט מסוג קו:

```csharp
// לדוגמאות מלאות וקבצי נתונים, נא לעבור ל https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לתיקיית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();
// יצירת אובייקט TextState להעברת תכונות מתקדמות
TextState ts = new TextState();
// הגדרת צבע לקו
ts.StrokingColor = Color.Gray;
// הגדרת מצב עיבוד טקסט
ts.RenderingMode = TextRenderingMode.StrokeText;
// טעינת מסמך PDF קלט
Facades.PdfFileStamp fileStamp = new Facades.PdfFileStamp(new Aspose.Pdf.Document(dataDir + "input.pdf"));

Aspose.Pdf.Facades.Stamp stamp = new Aspose.Pdf.Facades.Stamp();
stamp.BindLogo(new Facades.FormattedText("PAID IN FULL", System.Drawing.Color.Gray, "Arial", Facades.EncodingType.Winansi, true, 78));

// קישור TextState
stamp.BindTextState(ts);
// הגדרת מקור X,Y
stamp.SetOrigin(100, 100);
stamp.Opacity = 5;
stamp.BlendingSpace = Facades.BlendingColorSpace.DeviceRGB;
stamp.Rotation = 45.0F;
stamp.IsBackground = false;
// הוספת חותם
fileStamp.AddStamp(stamp);
fileStamp.Save(dataDir + "ouput_out.pdf");
fileStamp.Close();
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

