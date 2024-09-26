---
title: הוספת כותרת עליונה ותחתונה לקובץ PDF
linktitle: הוספת כותרת עליונה ותחתונה לקובץ PDF
type: docs
weight: 70
url: /net/add-headers-and-footers-of-pdf-file/
description: Aspose.PDF עבור .NET מאפשר לך להוסיף כותרות עליונות ותחתונות לקובץ PDF שלך באמצעות מחלקת TextStamp.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
aliases:
    - /net/manage-header-and-footer-of-pdf-file/
    - /net/manage-header-and-footer/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "הוספת כותרת עליונה ותחתונה לקובץ PDF",
    "alternativeHeadline": "איך להוסיף כותרת עליונה ותחתונה לקובץ PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "יצירת מסמכי PDF",
    "keywords": "pdf, c#, הוספת כותרת עליונה, הוספת כותרת תחתונה ב-pdf",
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
    "url": "/net/add-headers-and-footers-of-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-headers-and-footers-of-pdf-file/"
    },
    "dateModified": "2022-02-04",
    "description": "Aspose.PDF עבור .NET מאפשר לך להוסיף כותרות עליונות ותחתונות לקובץ PDF שלך באמצעות מחלקת TextStamp."
}
</script>
**Aspose.PDF for .NET** מאפשר לך להוסיף כותרת עליונה ותחתונה בקובץ PDF קיים. תוכל להוסיף תמונות או טקסט למסמך PDF. נסה גם להוסיף כותרות שונות בקובץ PDF אחד עם C#.

הקטע קוד הבא עובד גם עם ספריית [Aspose.PDF.Drawing](/pdf/net/drawing/).

## הוספת טקסט בכותרת העליונה של קובץ PDF

ניתן להשתמש במחלקת [TextStamp](https://reference.aspose.com/pdf/net/aspose.pdf/textstamp) כדי להוסיף טקסט בכותרת העליונה של קובץ PDF. מחלקת TextStamp מספקת תכונות הדרושות ליצירת חותמת מבוססת טקסט כמו גודל גופן, סגנון גופן וצבע גופן וכו'. על מנת להוסיף טקסט בכותרת העליונה, עליך ליצור אובייקט מסמך ואובייקט TextStamp באמצעות התכונות הנדרשות. לאחר מכן, תוכל לקרוא לשיטת AddStamp של הדף כדי להוסיף את הטקסט בכותרת העליונה של ה-PDF.

עליך להגדיר את תכונת TopMargin בצורה כזו שתתאים את הטקסט באזור הכותרת העליונה של ה-PDF שלך. תצטרך גם להגדיר HorizontalAlignment ל-Center ו-VerticalAlignment ל-Top.

הקטע קוד הבא מראה לך איך להוסיף טקסט בכותרת העליונה של קובץ PDF עם C#.
הקטע הבא מראה לך איך להוסיף טקסט בכותרת של קובץ PDF בשפת C#.

```csharp
// לדוגמאות מלאות וקבצי נתונים, אנא עבור ל https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לתיקיית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

// פתח מסמך
Document pdfDocument = new Document(dataDir+ "TextinHeader.pdf");

// צור כותרת
TextStamp textStamp = new TextStamp("טקסט הכותרת");
// הגדר תכונות של החותמת
textStamp.TopMargin = 10;
textStamp.HorizontalAlignment = HorizontalAlignment.Center;
textStamp.VerticalAlignment = VerticalAlignment.Top;
// הוסף כותרת לכל הדפים
foreach (Page page in pdfDocument.Pages)
{
    page.AddStamp(textStamp);
}
// שמור את המסמך המעודכן
pdfDocument.Save(dataDir+ "TextinHeader_out.pdf");
```

## הוספת טקסט בכותרת התחתונה של קובץ PDF

ניתן להשתמש במחלקת TextStamp כדי להוסיף טקסט בכותרת התחתונה של קובץ PDF.
ניתן להשתמש במחלקת TextStamp כדי להוסיף טקסט בכותרת התחתונה של קובץ PDF.

{{% alert color="primary" %}}

עליך להגדיר את תכונת השוליים התחתונים באופן שיאפשר להתאים את הטקסט באזור הכותרת התחתונה של ה-PDF שלך. כמו כן עליך להגדיר את HorizontalAlignment ל-Center ואת VerticalAlignment ל-Bottom

{{% /alert %}}

הקטע הבא מראה כיצד להוסיף טקסט בכותרת התחתונה של קובץ PDF באמצעות C#.

```csharp
// לדוגמאות מלאות וקבצי נתונים, אנא בקרו ב https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לספריית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

// פתח מסמך
Document pdfDocument = new Document(dataDir+ "TextinFooter.pdf");
// צור כותרת תחתונה
TextStamp textStamp = new TextStamp("טקסט כותרת תחתונה");
// הגדר תכונות החותמת
textStamp.BottomMargin = 10;
textStamp.HorizontalAlignment = HorizontalAlignment.Center;
textStamp.VerticalAlignment = VerticalAlignment.Bottom;
// הוסף כותרת תחתונה לכל העמודים
foreach (Page page in pdfDocument.Pages)
{
    page.AddStamp(textStamp);
}
// שמור קובץ פלט
doc.Save(dataDir + "TextinFooter_out.pdf");
```
## הוספת תמונה בכותרת של קובץ PDF

ניתן להשתמש במחלקה [ImageStamp](https://reference.aspose.com/pdf/net/aspose.pdf/ImageStamp) כדי להוסיף תמונה בכותרת של קובץ PDF. מחלקת חותמת התמונה מספקת תכונות הדרושות ליצירת חותמת מבוססת תמונה כמו גודל גופן, סגנון גופן וצבע גופן וכו'. על מנת להוסיף תמונה בכותרת, עליך ליצור אובייקט מסמך ואובייקט חותמת תמונה באמצעות התכונות הדרושות. לאחר מכן, תוכל לקרוא לשיטה [AddStamp](https://reference.aspose.com/pdf/net/aspose.pdf/page/methods/addstamp) של העמוד כדי להוסיף את התמונה בכותרת של ה-PDF.

{{% alert color="primary" %}}

עליך להגדיר את תכונת TopMargin בצורה שתתאים את התמונה באזור הכותרת של ה-PDF שלך. כמו כן עליך להגדיר את HorizontalAlignment ל-Center ואת VerticalAlignment ל-Top.

{{% /alert %}}

הקטע קוד הבא מראה לך איך להוסיף תמונה בכותרת של קובץ PDF ב-C#.

```csharp
// לדוגמאות מלאות וקבצי נתונים, אנא בקר ב https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לתיקיית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

// פתח מסמך
Document pdfDocument = new Document(dataDir+ "ImageinHeader.pdf");

// צור כותרת
ImageStamp imageStamp = new ImageStamp(dataDir+ "aspose-logo.jpg");
// הגדר תכונות של החותמת
imageStamp.TopMargin = 10;
imageStamp.HorizontalAlignment = HorizontalAlignment.Center;
imageStamp.VerticalAlignment = VerticalAlignment.Top;
// הוסף כותרת לכל העמודים
foreach (Page page in pdfDocument.Pages)
{
    page.AddStamp(imageStamp);
}
// שמור קובץ פלט
doc.Save(dataDir + "ImageinHeader_out.pdf");
```
## הוספת תמונה בכותרת התחתונה של קובץ PDF

ניתן להשתמש במחלקת Image Stamp כדי להוסיף תמונה בכותרת התחתונה של קובץ PDF. מחלקת Image Stamp מספקת מאפיינים הנדרשים ליצירת חותמת מבוססת תמונה כמו גודל גופן, סגנון גופן, וצבע גופן וכדומה. כדי להוסיף תמונה בכותרת התחתונה, עליך ליצור אובייקט מסמך ואובייקט Image Stamp באמצעות המאפיינים הנדרשים. לאחר מכן, תוכל לקרוא לשיטת AddStamp של העמוד כדי להוסיף את התמונה בכותרת התחתונה של ה-PDF.

{{% alert color="primary" %}}

עליך להגדיר את המאפיין [BottomMargin](https://reference.aspose.com/pdf/net/aspose.pdf/stamp/properties/bottommargin) בצורה שתתאים את התמונה לאזור הכותרת התחתונה של ה-PDF שלך. כמו כן עליך להגדיר את [HorizontalAlignment](https://reference.aspose.com/pdf/net/aspose.pdf/stamp/properties/horizontalalignment) ל-`Center` ואת [VerticalAlignment](https://reference.aspose.com/pdf/net/aspose.pdf/stamp/properties/verticalalignment) ל-`Bottom`.

{{% /alert %}}

הקטע הבא מראה איך להוסיף תמונה בכותרת התחתונה של קובץ PDF ב-C#.
הקטע הבא מדגים איך להוסיף תמונה בכותרת התחתונה של קובץ PDF בשפת C#.

```csharp
// לדוגמאות מלאות וקבצי נתונים, אנא בקרו ב https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לתיקיית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

// פתיחת מסמך
Document pdfDocument = new Document(dataDir+ "ImageInFooter.pdf");
// יצירת כותרת תחתונה
ImageStamp imageStamp = new ImageStamp(dataDir+ "aspose-logo.jpg");
// הגדרת מאפייני החותמת
imageStamp.BottomMargin = 10;
imageStamp.HorizontalAlignment = HorizontalAlignment.Center;
imageStamp.VerticalAlignment = VerticalAlignment.Bottom;
// הוספת כותרת תחתונה לכל הדפים
foreach (Page page in pdfDocument.Pages)
{
    page.AddStamp(imageStamp);
}
// שמירת קובץ הפלט
doc.Save(dataDir + "ImageInFooter_out.pdf");
```

## הוספת כותרות שונות בקובץ PDF אחד

אנו יודעים שאנו יכולים להוסיף TextStamp בקטע הכותרת/כותרת תחתונה של המסמך באמצעות המאפיינים TopMargin או Bottom Margin, אך לעיתים ייתכן שנדרש להוסיף מספר כותרות/כותרות תחתונות במסמך PDF יחיד.
אנו יודעים שאנו יכולים להוסיף חותמת טקסט בחלק העליון או התחתון של המסמך באמצעות התכונות TopMargin או Bottom Margin, אך לעיתים קרובות ייתכן שיהיה לנו דרישה להוסיף מספר כותרות/תחתיות במסמך PDF יחיד.

על מנת לעמוד בדרישה זו, ניצור אובייקטים נפרדים של TextStamp (מספר האובייקטים תלוי במספר הכותרות/תחתיות הנדרשות) ונוסיף אותם למסמך PDF. נוכל גם לציין מידע עיצוב שונה עבור כל אובייקט חותמת. בדוגמה הבאה, יצרנו אובייקט מסמך ושלושה אובייקטים של TextStamp ולאחר מכן השתמשנו בשיטת [AddStamp](https://reference.aspose.com/pdf/net/aspose.pdf/page/methods/addstamp) של העמוד כדי להוסיף את הטקסט בחלק העליון של ה- PDF. קטע הקוד הבא מראה לך כיצד להוסיף תמונה בחלק התחתון של קובץ PDF עם Aspose.PDF עבור .NET.

```csharp
// לדוגמאות מלאות וקבצי נתונים, אנא בקרו ב https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לתיקיית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

// פתיחת מסמך המקור
Aspose.Pdf.Document doc = new Aspose.Pdf.Document(dataDir+ "AddingDifferentHeaders.pdf");

// יצירת שלוש חותמות
Aspose.Pdf.TextStamp stamp1 = new Aspose.Pdf.TextStamp("כותרת 1");
Aspose.Pdf.TextStamp stamp2 = new Aspose.Pdf.TextStamp("כותרת 2");
Aspose.Pdf.TextStamp stamp3 = new Aspose.Pdf.TextStamp("כותרת 3");

// הגדרת יישור החותמת (מיקום החותמת בחלק העליון של העמוד, ממורכזת אופקית)
stamp1.VerticalAlignment = Aspose.Pdf.VerticalAlignment.Top;
stamp1.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Center;
// ציון סגנון הגופן כמודגש
stamp1.TextState.FontStyle = FontStyles.Bold;
// הגדרת מידע צבע הרקע של הטקסט כאדום
stamp1.TextState.ForegroundColor = Color.Red;
// ציון גודל הגופן כ-14
stamp1.TextState.FontSize = 14;

// כעת עלינו להגדיר את היישור האנכי של אובייקט החותמת השני כעליון
stamp2.VerticalAlignment = Aspose.Pdf.VerticalAlignment.Top;
// הגדרת מידע יישור אופקי לחותמת כממורכזת
stamp2.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Center;
// הגדרת גורם ההגדלה לאובייקט החותמת
stamp2.Zoom = 10;

// הגדרת עיצוב של אובייקט החותמת השלישי
// ציון מידע היישור האנכי לאובייקט החותמת כעליון
stamp3.VerticalAlignment = Aspose.Pdf.VerticalAlignment.Top;
// הגדרת מידע יישור אופקי לאובייקט החותמת כממורכז
stamp3.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Center;
// הגדרת זווית הסיבוב לאובייקט החותמת
stamp3.RotateAngle = 35;
// הגדרת ורוד כצבע רקע לחותמת
stamp3.TextState.BackgroundColor = Color.Pink;
// שינוי מידע פני הגופן לחותמת ל-Verdana
stamp3.TextState.Font = FontRepository.FindFont("Verdana");
// החותמת הראשונה מתווספת בעמוד הראשון;
doc.Pages[1].AddStamp(stamp1);
// החותמת השנייה מתווספת בעמוד השני;
doc.Pages[2].AddStamp(stamp2);
// החותמת השלישית מתווספת בעמוד השלישי.
doc.Pages[3].AddStamp(stamp3);
// שמירת המסמך המעודכן
doc.Save(dataDir + "MultiHeader_out.pdf");
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "ספריית Aspose.PDF ל-.NET",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "ארגון",
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
                "@type": "נקודת קשר",
                "telephone": "+1 903 306 1676",
                "contactType": "מכירות",
                "areaServed": "ארה\"ב",
                "availableLanguage": "אנגלית"
            },
            {
                "@type": "נקודת קשר",
                "telephone": "+44 141 628 8900",
                "contactType": "מכירות",
                "areaServed": "בריטניה",
                "availableLanguage": "אנגלית"
            },
            {
                "@type": "נקודת קשר",
                "telephone": "+61 2 8006 6987",
                "contactType": "מכירות",
                "areaServed": "אוסטרליה",
                "availableLanguage": "אנגלית"
            }
        ]
    },
    "offers": {
        "@type": "הצעה",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "ספריית עיבוד PDF ל-.NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/net/create-pdf-document/screenshot.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "דירוג מצטבר",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>
```

