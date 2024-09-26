---
title: PDF Tooltip באמצעות C#
linktitle: PDF Tooltip
type: docs
weight: 20
url: /net/pdf-tooltip/
description: למד כיצד להוסיף תיאור קצר לקטע טקסט ב-PDF באמצעות C# ו-Aspose.PDF
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "PDF Tooltip באמצעות C#",
    "alternativeHeadline": "הוספת תיאור קצר ל-PDF לטקסט",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "יצירת מסמך PDF",
    "keywords": "pdf, c#, הוספת תיאור קצר ל-pdf",
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
    "url": "/net/pdf-tooltip/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/pdf-tooltip/"
    },
    "dateModified": "2022-02-04",
    "description": "למד כיצד להוסיף תיאור קצר לקטע טקסט ב-PDF באמצעות C# ו-Aspose.PDF"
}
</script>
הקטע הבא של קוד עובד גם עם ספריית [Aspose.PDF.Drawing](/pdf/net/drawing/).

## הוספת תיאור כלי לטקסט שנמצא על ידי הוספת כפתור בלתי נראה

לעיתים נדרש להוסיף פרטים עבור ביטוי או מילה מסוימת כתיאור כלי במסמך PDF כך שיקפוץ כאשר המשתמש מרחף את סמן העכבר מעל הטקסט. Aspose.PDF for .NET מספקת תכונה זו ליצירת תיאורי כלי על ידי הוספת כפתור בלתי נראה מעל הטקסט שנמצא. הקטע הבא של קוד יראה לך את הדרך להשגת פונקציונליות זו:

```csharp
// לדוגמאות מלאות וקבצי נתונים, אנא בקר ב https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לספריית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
string outputFile = dataDir + "Tooltip_out.pdf";

// יצירת מסמך דוגמה עם טקסט
Document doc = new Document();
doc.Pages.Add().Paragraphs.Add(new TextFragment("הזז את סמן העכבר לכאן כדי להציג תיאור כלי"));
doc.Pages[1].Paragraphs.Add(new TextFragment("הזז את סמן העכבר לכאן כדי להציג תיאור כלי ארוך מאוד"));
doc.Save(outputFile);

// פתיחת מסמך עם טקסט
Document document = new Document(outputFile);
// יצירת אובייקט TextAbsorber כדי למצוא את כל הביטויים התואמים את הביטוי הרגולרי
TextFragmentAbsorber absorber = new TextFragmentAbsorber("הזז את סמן העכבר לכאן כדי להציג תיאור כלי");
// קבלת ה-absorber עבור דפי המסמך
document.Pages.Accept(absorber);
// קבלת קטעי הטקסט שנמצאו
TextFragmentCollection textFragments = absorber.TextFragments;

// לולאה דרך הקטעים
foreach (TextFragment fragment in textFragments)
{
    // יצירת כפתור בלתי נראה במיקום קטע הטקסט
    ButtonField field = new ButtonField(fragment.Page, fragment.Rectangle);
    // הערך AlternateName יוצג כתיאור כלי על ידי יישום הצופה
    field.AlternateName = "תיאור כלי לטקסט.";
    // הוספת שדה הכפתור למסמך
    document.Form.Add(field);
}

// הבא יהיה דוגמה של תיאור כלי ארוך מאוד
absorber = new TextFragmentAbsorber("הזז את סמן העכבר לכאן כדי להציג תיאור כלי ארוך מאוד");
document.Pages.Accept(absorber);
textFragments = absorber.TextFragments;

foreach (TextFragment fragment in textFragments)
{
    ButtonField field = new ButtonField(fragment.Page, fragment.Rectangle);
    // הגדרת טקסט ארוך מאוד
    field.AlternateName = "Lorem ipsum dolor sit amet, consectetur adipiscing elit," +
                            " sed do eiusmod tempor incididunt ut labore et dolore magna" +
                            " aliqua. Ut enim ad minim veniam, quis nostrud exercitation" +
                            " ullamco laboris nisi ut aliquip ex ea commodo consequat." +
                            " Duis aute irure dolor in reprehenderit in voluptate velit" +
                            " esse cillum dolore eu fugiat nulla pariatur. Excepteur sint" +
                            " occaecat cupidatat non proident, sunt in culpa qui officia" +
                            " deserunt mollit anim id est laborum.";
    document.Form.Add(field);
}

// שמירת המסמך
document.Save(outputFile);
```
{{% alert color="primary" %}}

לגבי אורך ההסבר המופיע בתיבת הכלים, טקסט תיבת הכלים מוכל במסמך PDF כסוג מחרוזת PDF, מחוץ לזרם התוכן. אין הגבלה מועילה על מחרוזות כאלה בקבצי PDF (ראה נספח C של מדריך PDF). עם זאת, קורא תואם (למשל Adobe Acrobat) הרץ על מעבד מסוים ובסביבת הפעלה מסוימת כן נתקל בהגבלה כזו. אנא פנה לתיעוד של אפליקציית קורא ה-PDF שלך.

{{% /alert %}}

## צור בלוק טקסט מוסתר והצג אותו כאשר העכבר עובר מעליו

ב-Aspose.PDF, מיושמת תכונה להסתרת פעולות בה ניתן להציג/להסתיר שדה תיבת טקסט (או כל סוג אחר של אנוטציה) בעת כניסת/יציאת עכבר מעל כפתור בלתי נראה. לשם כך משתמשים במחלקה Aspose.Pdf.Annotations.HideAction כדי להקצות את פעולת ההסתרה/הצגה לבלוק הטקסט. אנא השתמש בקטע הקוד הבא כדי להציג/להסתיר בלוק טקסט בעת כניסת/יציאת עכבר.

כמו כן, שים לב שפעולות PDF במסמכים פועלות כראוי בקוראים התואמים (למשל
כל היישומים של פעולת ההסתרה במסמכי PDF עובדים היטב ב-Internet Explorer גרסה 11.0.
כל היישומים של פעולת ההסתרה עובדים גם ב-Opera גרסה 12.14, אך נצפתה עיכוב בתגובה בפתיחה הראשונה של המסמך.
רק יישום שמשתמש בבנאי HideAction המקבל שם שדה עובד אם דפדפן Google Chrome גרסה 61.0 גולש במסמך; יש להשתמש בבנאים המתאימים אם גלישה ב-Google Chrome היא משמעותית:

```csharp
// לדוגמאות מלאות וקבצי נתונים, אנא עברו ל https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לתיקיית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

string outputFile = dataDir + "TextBlock_HideShow_MouseOverOut_out.pdf";

// צור מסמך דוגמא עם טקסט
Document doc = new Document();
doc.Pages.Add().Paragraphs.Add(new TextFragment("הזז את סמן העכבר לכאן כדי להציג טקסט צף"));
doc.Save(outputFile);

// פתח מסמך עם טקסט
Document document = new Document(outputFile);
// צור אובייקט TextAbsorber כדי למצוא את כל הביטויים התואמים לביטוי הרגולרי
TextFragmentAbsorber absorber = new TextFragmentAbsorber("הזז את סמן העכבר לכאן כדי להציג טקסט צף");
// הפעל את ה-absorber עבור דפי המסמך
document.Pages.Accept(absorber);
// קבל את הטקסט הראשון שהופק
TextFragmentCollection textFragments = absorber.TextFragments;
TextFragment fragment = textFragments[1];

// צור שדה טקסט נסתר לטקסט צף במלבן המצוין של הדף
TextBoxField floatingField = new TextBoxField(fragment.Page, new Rectangle(100, 700, 220, 740));
// הגדר טקסט להצגה כערך שדה
floatingField.Value = "זהו \"שדה טקסט צף\".";
// מומלץ להגדיר שדה כ'לקריאה בלבד' לתרחיש זה
floatingField.ReadOnly = true;
// הגדר את דגל 'נסתר' כדי להפוך את השדה לבלתי נראה בפתיחת המסמך
floatingField.Flags |= AnnotationFlags.Hidden;

// הגדרת שם שדה ייחודי אינה נדרשת אך מותרת
floatingField.PartialName = "FloatingField_1";

// הגדרת תכונות תצוגת שדה אינה נדרשת אך משפרת את המראה
floatingField.DefaultAppearance = new DefaultAppearance("Helv", 10, System.Drawing.Color.Blue);
floatingField.Characteristics.Background = System.Drawing.Color.LightBlue;
floatingField.Characteristics.Border = System.Drawing.Color.DarkBlue;
floatingField.Border = new Border(floatingField);
floatingField.Border.Width = 1;
floatingField.Multiline = true;

// הוסף שדה טקסט למסמך
document.Form.Add(floatingField);

// צור כפתור בלתי נראה במיקום קטע הטקסט
ButtonField buttonField = new ButtonField(fragment.Page, fragment.Rectangle);
// צור פעולת הסתרה חדשה לשדה נתון (הערה) ודגל בלתי נראה.
// (ניתן גם להתייחס לשדה הצף בשמו אם הגדרת אותו למעלה.)
// הוסף פעולות בכניסת/יציאת עכבר בשדה הכפתור הבלתי נראה
buttonField.Actions.OnEnter = new HideAction(floatingField, false);
buttonField.Actions.OnExit = new HideAction(floatingField);

// הוסף שדה כפתור למסמך
document.Form.Add(buttonField);

// שמור מסמך
document.Save(outputFile);
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
                "areaServed": "ארה\"ב",
                "availableLanguage": "אנגלית"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "מכירות",
                "areaServed": "בריטניה",
                "availableLanguage": "אנגלית"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "מכירות",
                "areaServed": "אוסטרליה",
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

