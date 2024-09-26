---
title: עיצוב מסמך PDF באמצעות C#
linktitle: עיצוב מסמך PDF
type: docs
weight: 11
url: /net/formatting-pdf-document/
description: צור ועצב מסמך PDF באמצעות Aspose.PDF עבור .NET. השתמש בקטע הקוד הבא כדי לפתור את המשימות שלך.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "עיצוב מסמך PDF באמצעות C#",
    "alternativeHeadline": "איך לעצב מסמך PDF ב-.NET",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "יצירת מסמכי PDF",
    "keywords": "pdf, dotnet, עיצוב מסמך pdf",
    "wordcount": "302",
    "proficiencyLevel":"מתחיל",
    "publisher": {
        "@type": "Organization",
        "name": "צוות Aspose.PDF Doc",
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
    "url": "/net/formatting-pdf-document/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/formatting-pdf-document/"
    },
    "dateModified": "2022-02-04",
    "description": "צור ועצב מסמך PDF באמצעות Aspose.PDF עבור .NET. השתמש בקטע הקוד הבא כדי לפתור את המשימות שלך."
}
</script>
## עיצוב מסמך PDF

### קבלת הגדרות חלון המסמך ותצוגת דף

נושא זה עוזר לך להבין איך לקבל הגדרות של חלון המסמך, אפליקציית הצפייה ואיך הדפים מוצגים. כדי להגדיר את ההגדרות האלה:

פתח את קובץ ה-PDF באמצעות המחלקה [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document). כעת, תוכל להגדיר את התכונות של אובייקט המסמך, כמו

- CenterWindow – מרכז את חלון המסמך במרכז המסך. ברירת מחדל: false.
- Direction – סדר קריאה. זה קובע איך הדפים מסודרים כאשר הם מוצגים זה לצד זה. ברירת מחדל: משמאל לימין.
- DisplayDocTitle – מציג את כותרת המסמך בשורת כותרת חלון המסמך. ברירת מחדל: false (הכותרת מוצגת).
- HideMenuBar – מסתיר או מציג את סרגל התפריט של חלון המסמך. ברירת מחדל: false (סרגל התפריט מוצג).
- HideToolBar – מסתיר או מציג את סרגל הכלים של חלון המסמך. ברירת מחדל: false (סרגל הכלים מוצג).
- HideWindowUI – מסתיר או מציג אלמנטים בחלון המסמך כמו סרגלי גלילה.
- HideWindowUI – הסתר או הצג רכיבי חלון המסמך כמו פסי גלילה.
- NonFullScreenPageMode – איך המסמך מוצג כשהוא לא במצב מסך מלא.
- PageLayout – פריסת העמוד.
- PageMode – איך המסמך מוצג בפתיחה הראשונה. האפשרויות הן הצגת ממוזערים, מסך מלא, הצגת חלונית צירופים.

הקטע הבא עובד גם עם ספריית [Aspose.PDF.Drawing](/pdf/net/drawing/).

הקטע הבא מראה איך לקבל את המאפיינים באמצעות מחלקת [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).

```csharp
// לדוגמאות מלאות וקבצי נתונים, אנא עבור ל https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לתיקיית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// פתח מסמך
Document pdfDocument = new Document(dataDir + "GetDocumentWindow.pdf");

// קבל מאפיינים שונים של המסמך
// מיקום חלון המסמך - ברירת מחדל: false
Console.WriteLine("CenterWindow : {0}", pdfDocument.CenterWindow);
  
// סדר קריאה עיקרי; קובע את מיקום העמוד
// כשמוצגים זה לצד זה - ברירת מחדל: L2R
Console.WriteLine("Direction : {0}", pdfDocument.Direction);

// האם להציג בשורת הכותרת של החלון את כותרת המסמך
// אם לא, שורת הכותרת מציגה את שם קובץ ה-PDF - ברירת מחדל: false
Console.WriteLine("DisplayDocTitle : {0}", pdfDocument.DisplayDocTitle);

// האם לשנות את גודל חלון המסמך כך שיתאים לגודל
// העמוד הראשון שמוצג - ברירת מחדל: false
Console.WriteLine("FitWindow : {0}", pdfDocument.FitWindow);

// האם להסתיר את שורת התפריט של יישום הצפייה - ברירת מחדל: false
Console.WriteLine("HideMenuBar : {0}", pdfDocument.HideMenubar);

// האם להסתיר את סרגל הכלים של יישום הצפייה - ברירת מחדל: false
Console.WriteLine("HideToolBar : {0}", pdfDocument.HideToolBar);

// האם להסתיר אלמנטים כמו פסי גלילה
// ולהשאיר רק את תוכן העמודים מוצג - ברירת מחדל: false
Console.WriteLine("HideWindowUI : {0}", pdfDocument.HideWindowUI);

// מצב עמוד המסמך. איך להציג מסמך ביציאה ממצב מסך מלא.
Console.WriteLine("NonFullScreenPageMode : {0}", pdfDocument.NonFullScreenPageMode);

// פריסת העמוד, למשל עמוד יחיד, עמודה אחת
Console.WriteLine("PageLayout : {0}", pdfDocument.PageLayout);

// איך המסמך אמור להופיע בפתיחה
// למשל הצגת ממוזערים, מסך מלא, הצגת חלונית צירופים
Console.WriteLine("pageMode : {0}", pdfDocument.PageMode);
```
### הגדרת תכונות חלון המסמך ותצוגת הדף

נושא זה מסביר איך להגדיר את תכונות חלון המסמך, אפליקציית הצפייה ותצוגת הדף. להגדרת התכונות השונות:

1. פתח את קובץ ה-PDF באמצעות המחלקה [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).
1. הגדר את תכונות אובייקט המסמך.
1. שמור את קובץ ה-PDF שעודכן באמצעות המתודה Save.

התכונות הזמינות הן:

- CenterWindow
- Direction
- DisplayDocTitle
- FitWindow
- HideMenuBar
- HideToolBar
- HideWindowUI
- NonFullScreenPageMode
- PageLayout
- PageMode

כל אחת מוסברת ומתוארת בקטע הקוד להלן. קטע הקוד הבא מראה לך איך להגדיר את התכונות באמצעות המחלקה [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).

```csharp
// לדוגמאות מלאות וקבצי נתונים, נא לעבור ל https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לתיקיית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// פתיחת מסמך
Document pdfDocument = new Document(dataDir + "SetDocumentWindow.pdf");

// הגדרת תכונות שונות של המסמך
// ציון מיקום חלון המסמך - ברירת מחדל: false
pdfDocument.CenterWindow = true;

// סדר קריאה דומיננטי; קובע את מיקום הדף
// כאשר מוצג זה לצד זה - ברירת מחדל: L2R
pdfDocument.Direction = Direction.R2L;

// ציון אם שורת הכותרת של החלון צריכה להציג את כותרת המסמך
// אם לא, שורת הכותרת מציגה את שם קובץ ה-PDF - ברירת מחדל: false
pdfDocument.DisplayDocTitle = true;

// ציון האם לשנות את גודל חלון המסמך כדי להתאים לגודל
// הדף הראשון שמוצג - ברירת מחדל: false
pdfDocument.FitWindow = true;

// ציון האם להסתיר את שורת התפריט של אפליקציית הצפייה - ברירת מחדל: false
pdfDocument.HideMenubar = true;

// ציון האם להסתיר את סרגל הכלים של אפליקציית הצפייה - ברירת מחדל: false
pdfDocument.HideToolBar = true;

// ציון האם להסתיר את אלמנטי ממשק המשתמש כמו פסי גלילה
// ולהשאיר רק את תוכן הדף מוצג - ברירת מחדל: false
pdfDocument.HideWindowUI = true;

// מצב דף המסמך. ציון איך להציג מסמך ביציאה ממצב מסך מלא.
pdfDocument.NonFullScreenPageMode = PageMode.UseOC;

// ציון פריסת הדף, כלומר דף יחיד, עמודה אחת
pdfDocument.PageLayout = PageLayout.TwoColumnLeft;

// ציון איך המסמך צריך להציג כאשר נפתח
// למשל הצגת תמונות ממוזערות, מסך מלא, הצגת חלונית הקבצים המצורפים
pdfDocument.PageMode = PageMode.UseThumbs;

dataDir = dataDir + "SetDocumentWindow_out.pdf";
// שמירת קובץ ה-PDF שעודכן
pdfDocument.Save(dataDir);
```
### הטמעת גופנים בקובץ PDF קיים

קוראי PDF תומכים [ב-14 גופנים עיקריים](https://en.wikipedia.org/wiki/PDF#Text) כדי שהמסמכים יוצגו באותה צורה ללא תלות בפלטפורמה שבה המסמך מוצג. כאשר קובץ PDF מכיל גופן שאינו אחד מ-14 הגופנים העיקריים, יש להטמיע את הגופן בקובץ PDF כדי למנוע החלפת גופנים.

Aspose.PDF עבור .NET תומך בהטמעת גופנים בקבצי PDF קיימים. ניתן להטמיע גופן שלם או תת-קבוצה של הגופן. כדי להטמיע את הגופן, פתח את קובץ ה-PDF באמצעות מחלקת [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document). לאחר מכן השתמש במחלקת [Aspose.Pdf.Text.Font](https://reference.aspose.com/pdf/net/aspose.pdf.text) כדי להטמיע את הגופן בקובץ ה-PDF. כדי להטמיע את הגופן המלא, השתמש בתכונת IsEmbeded של מחלקת Font; כדי להשתמש בתת-קבוצה של הגופן, השתמש בתכונת IsSubset.

{{% alert color="primary" %}}

תת-קבוצת גופן מטמיעה רק את התווים שבשימוש והיא שימושית כאשר משתמשים בגופנים למשפטים קצרים או סיסמאות, לדוגמה כאשר גופן תאגידי משמש ללוגו, אך לא לטקסט הראשי.
חלק מהגופנים משובצים רק בתווים שמשתמשים בהם והם שימושיים במקרים שבהם משתמשים בגופנים למשפטים קצרים או לסיסמאות, לדוגמה כאשר גופן חברתי משמש ללוגו, אך לא לטקסט הראשי.

{{% /alert %}}

הקטע הבא מראה איך לשבץ גופן בקובץ PDF.

### שיבוץ גופנים סטנדרטיים מסוג 1

חלק מהמסמכים ב-PDF מכילים גופנים מסט מיוחד של Adobe. גופנים מסט זה נקראים "גופנים סטנדרטיים מסוג 1". הסט כולל 14 גופנים ושיבוץ סוג זה של גופנים דורש שימוש בדגלים מיוחדים כלומר [Aspose.Pdf.Document.EmbedStandardFonts](https://reference.aspose.com/pdf/net/aspose.pdf/document/properties/embedstandardfonts). להלן קטע הקוד שניתן להשתמש בו כדי לקבל מסמך עם כל הגופנים משובצים כולל גופנים סטנדרטיים מסוג 1:

```csharp
// לדוגמאות מלאות וקבצי נתונים, אנא עבורו ל https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לתיקיית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// טעינת מסמך PDF קיים
Document pdfDocument = new Document(dataDir + "input.pdf");
// הגדרת הנכס EmbedStandardFonts של המסמך
pdfDocument.EmbedStandardFonts = true;
foreach (Aspose.Pdf.Page page in pdfDocument.Pages)
{
    if (page.Resources.Fonts != null)
    {
        foreach (Aspose.Pdf.Text.Font pageFont in page.Resources.Fonts)
        {
// בדיקה אם הגופן כבר משובץ
if (!pageFont.IsEmbedded)
{
    pageFont.IsEmbedded = true;
}
        }
    }
}
pdfDocument.Save(dataDir + "EmbeddedFonts-updated_out.pdf");
```
### שיבוץ גופנים בעת יצירת PDF

אם אתה צריך להשתמש בגופן שאינו אחד מ-14 הגופנים המרכזיים שתומכים ב-Adobe Reader, עליך לשבץ את תיאור הגופן בעת יצירת קובץ ה-Pdf. אם מידע הגופן אינו מושבץ, Adobe Reader ייקח אותו ממערכת ההפעלה אם הוא מותקן על המערכת, או שהוא יבנה גופן חלופי בהתאם לתיאור הגופן ב-Pdf.

>אנא שים לב שהגופן המושבץ חייב להיות מותקן על מכונת המארח כלומר במקרה של הקוד הבא גופן 'Univers Condensed' מותקן על המערכת.

אנו משתמשים בתכונה IsEmbedded של מחלקת Font כדי לשבץ את מידע הגופן לתוך קובץ ה-Pdf. הגדרת ערך תכונה זו ל-'True' תשבץ את קובץ הגופן המלא לתוך ה-Pdf, תוך ידיעת העובדה שזה יגדיל את גודל קובץ ה-Pdf. להלן קטע הקוד שניתן להשתמש בו כדי לשבץ את מידע הגופן לתוך Pdf.

```csharp
// לדוגמאות מלאות וקבצי נתונים, אנא עבור אל https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לספריית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// יישום אובייקט Pdf על ידי קריאה לבנאי הריק שלו
Aspose.Pdf.Document doc = new Aspose.Pdf.Document();

// יצירת סעיף באובייקט ה-Pdf
Aspose.Pdf.Page page = doc.Pages.Add();

Aspose.Pdf.Text.TextFragment fragment = new Aspose.Pdf.Text.TextFragment("");

Aspose.Pdf.Text.TextSegment segment = new Aspose.Pdf.Text.TextSegment(" זהו טקסט לדוגמא בשימוש בגופן מותאם אישית.");
Aspose.Pdf.Text.TextState ts = new Aspose.Pdf.Text.TextState();
ts.Font = FontRepository.FindFont("Arial");
ts.Font.IsEmbedded = true;
segment.TextState = ts;
fragment.Segments.Add(segment);
page.Paragraphs.Add(fragment);

dataDir = dataDir + "EmbedFontWhileDocCreation_out.pdf";
// שמירת מסמך PDF
doc.Save(dataDir);
```
### הגדרת שם גופן ברירת מחדל בעת שמירת PDF

כאשר מסמך PDF מכיל גופנים שאינם זמינים במסמך עצמו ועל המכשיר, ה-API מחליף את גופנים אלו בגופן ברירת המחדל. כאשר גופן זמין (מותקן על המכשיר או מוטמע במסמך), ה-PDF המופק צריך להכיל את אותו הגופן (לא להיות מוחלף בגופן ברירת המחדל). ערך גופן ברירת המחדל צריך להכיל את שם הגופן (לא את הנתיב לקבצי הגופן). יישמנו תכונה להגדרת שם גופן ברירת מחדל בעת שמירת מסמך כ-PDF. ניתן להשתמש בקטע הקוד הבא כדי להגדיר גופן ברירת מחדל:

```csharp
// לדוגמאות מלאות וקבצי נתונים, אנא עבורו ל https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לספריית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
// טען מסמך PDF קיים עם גופן חסר
string documentName = dataDir + "input.pdf";
string newName = "Arial";
using (System.IO.FileStream fs = new System.IO.FileStream(documentName, System.IO.FileMode.Open))
using (Document document = new Document(fs))
{
    PdfSaveOptions pdfSaveOptions = new PdfSaveOptions();
    // ציין שם גופן ברירת מחדל
    pdfSaveOptions.DefaultFontName = newName;
    document.Save(dataDir + "output_out.pdf", pdfSaveOptions);
}
```
### קבל את כל הגופנים ממסמך PDF

אם ברצונך לקבל את כל הגופנים ממסמך PDF, תוכל להשתמש בשיטת FontUtilities.GetAllFonts() המוצעת במחלקת [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document). אנא בדוק את קטע הקוד הבא כדי לקבל את כל הגופנים ממסמך PDF קיים:

```csharp
// לדוגמאות מלאות וקבצי נתונים, אנא עבור ל https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לתיקיית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
Document doc = new Document(dataDir + "input.pdf");
Aspose.Pdf.Text.Font[] fonts = doc.FontUtilities.GetAllFonts();
foreach (Aspose.Pdf.Text.Font font in fonts)
{
    Console.WriteLine(font.FontName);
}
```

### קבל אזהרות עבור החלפת גופן

Aspose.PDF for .NET מספק שיטות לקבלת הודעות על החלפת גופן לטיפול במקרי החלפת גופן. קטעי הקוד להלן מראים איך להשתמש בפונקציונליות המתאימה.

```csharp
// לדוגמאות מלאות וקבצי נתונים, אנא עבור ל https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לתיקיית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

Document doc = new Document(dataDir + "input.pdf");

doc.FontSubstitution += new Document.FontSubstitutionHandler(OnFontSubstitution);
```
השיטה **OnFontSubstitution** מופיעה להלן.

```csharp
// לדוגמאות מלאות וקבצי נתונים, אנא בקרו ב https://github.com/aspose-pdf/Aspose.PDF-for-.NET
Console.WriteLine(string.Format("הגופן '{0}' הוחלף בגופן אחר '{1}'",
oldFont.FontName, newFont.FontName));
```

### שיפור טמעת גופנים באמצעות FontSubsetStrategy

האפשרות לטמע גופנים כתת-קבוצה ניתן להשיג באמצעות המאפיין IsSubset, אך לעיתים תרצה להפחית קבוצת גופנים מוטמעת במלואה לתת-קבוצות שמשמשות במסמך בלבד. למחלקה Aspose.Pdf.Document יש מאפיין FontUtilities שכולל את השיטה SubsetFonts(FontSubsetStrategy subsetStrategy). בשיטה SubsetFonts(), הפרמטר subsetStrategy עוזר לכוון את אסטרטגיית התת-קבוצה. FontSubsetStrategy תומך בשתי האפשרויות הבאות לתת-קיבוץ גופנים.

- SubsetAllFonts - זה יעשה תת-קיבוץ לכל הגופנים המשמשים במסמך.
- SubsetEmbeddedFontsOnly - זה יעשה תת-קיבוץ רק לגופנים שטומעו במלואם במסמך.

הקטע הבא מראה איך להגדיר FontSubsetStrategy:
הקטע הבא ממחיש כיצד להגדיר אסטרטגיית חתך גופן:

```csharp
// לדוגמאות מלאות וקבצי נתונים, אנא עבורו ל https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לספריית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
Document doc = new Document(dataDir + "input.pdf");
// כל הגופנים ישובצו כתת-קבוצה במסמך במקרה של SubsetAllFonts.
doc.FontUtilities.SubsetFonts(FontSubsetStrategy.SubsetAllFonts);
// תת-קבוצה של גופן תשובץ לגופנים שהוטמעו במלואם אך גופנים שלא הוטמעו במסמך לא יושפעו.
doc.FontUtilities.SubsetFonts(FontSubsetStrategy.SubsetEmbeddedFontsOnly);
doc.Save(dataDir + "Output_out.pdf");
```

### קביעת וקבלת גורם הזום של קובץ PDF

לעיתים תרצה לקבוע מהו גורם הזום הנוכחי של מסמך PDF. באמצעות Aspose.Pdf, תוכל למצוא את הערך הנוכחי כמו גם להגדיר אחד.

מאפיין היעד של המחלקה [GoToAction](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/gotoaction) מאפשר לך לקבל את ערך הזום המשויך לקובץ PDF.
#### הגדר גורם זום

הקטע הבא מראה איך להגדיר גורם זום של קובץ PDF.

```csharp
// לדוגמאות מלאות וקבצי נתונים, אנא עבורו ל https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// נתיב לתיקיית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// יצירת אובייקט מסמך חדש
Document doc = new Document(dataDir + "SetZoomFactor.pdf");

GoToAction action = new GoToAction(new XYZExplicitDestination(1, 0, 0, .5));
doc.OpenAction = action;
dataDir = dataDir + "Zoomed_pdf_out.pdf";
// שמירת המסמך
doc.Save(dataDir);
```

#### קבל גורם זום

הקטע הבא מראה איך לקבל את גורם הזום של קובץ PDF.

```csharp
// לדוגמאות מלאות וקבצי נתונים, אנא עבורו ל https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// נתיב לתיקיית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// יצירת אובייקט מסמך חדש
Document doc = new Document(dataDir + "Zoomed_pdf.pdf");

// יצירת אובייקט GoToAction
GoToAction action = doc.OpenAction as GoToAction;

// קבלת גורם הזום של קובץ PDF
System.Console.WriteLine((action.Destination as XYZExplicitDestination).Zoom); // ערך הזום של המסמך;
```
### הגדרת תכונות Dialog Preset להדפסה

Aspoose.PDF מאפשר הגדרת תכונות Dialog Preset להדפסה של מסמך PDF. זה מאפשר לך לשנות את התכונה DuplexMode עבור מסמך PDF שמוגדר כברירת מחדל ל-simplex. ניתן להשיג זאת באמצעות שתי שיטות שונות כפי שמוצג למטה.

```csharp
// לדוגמאות מלאות וקבצי נתונים, אנא עבור אל https://github.com/aspose-pdf/Aspose.PDF-for-.NET
var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

using (Document doc = new Document())
{
    doc.Pages.Add();
    doc.Duplex = PrintDuplex.DuplexFlipLongEdge;
    doc.Save(dataDir + "35297_out.pdf", SaveFormat.Pdf);
}
```

### הגדרת תכונות Dialog Preset להדפסה באמצעות עורך תוכן PDF

```csharp
// לדוגמאות מלאות וקבצי נתונים, אנא עבור אל https://github.com/aspose-pdf/Aspose.PDF-for-.NET
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

string outputFile = dataDir + "input.pdf";
using (PdfContentEditor ed = new PdfContentEditor())
{
    ed.BindPdf(outputFile);
    if ((ed.GetViewerPreference() & ViewerPreference.DuplexFlipShortEdge) > 0)
    {
        Console.WriteLine("הקובץ מכיל הפוך קצר");
    }

    ed.ChangeViewerPreference(ViewerPreference.DuplexFlipShortEdge);
    ed.Save(dataDir + "SetPrintDlgPropertiesUsingPdfContentEditor_out.pdf");
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

