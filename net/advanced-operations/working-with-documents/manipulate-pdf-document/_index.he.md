---
title: לשלוט במסמך PDF ב-C#
linktitle: לשלוט במסמך PDF
type: docs
weight: 20
url: /net/manipulate-pdf-document/
description: המאמר הזה מכיל מידע על איך לאמת מסמך PDF לתקן PDF A, איך לעבוד עם תוכן עניינים, איך להגדיר תאריך תפוגה ל-PDF, וכו'.
keywords: "manipulate pdf c#"
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "לשלוט במסמך PDF",
    "alternativeHeadline": "איך לשלוט בקובץ PDF",
    "author": {
        "@type": "Person",
        "name":"אנסטסיה הולוב",
        "givenName": "אנסטסיה",
        "familyName": "הולוב",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "יצירת מסמכי PDF",
    "keywords": "pdf, dotnet, manipulate pdf file",
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
    "url": "/net/manipulate-pdf-document/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/manipulate-pdf-document/"
    },
    "dateModified": "2022-02-04",
    "description": "המאמר הזה מכיל מידע על איך לאמת מסמך PDF לתקן PDF A, איך לעבוד עם תוכן עניינים, איך להגדיר תאריך תפוגה ל-PDF, וכו'."
}
</script>

## **ניהול מסמך PDF ב-C#**

## אימות מסמך PDF לתקן PDF A (A 1A ו-A 1B)

לאימות מסמך PDF לתאימות PDF/A-1a או PDF/A-1b, השתמש במחלקת [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) ובשיטת Validate. שיטה זו מאפשרת לך לציין את שם הקובץ בו תישמר התוצאה ואת סוג האימות הנדרש [PdfFormat](https://reference.aspose.com/pdf/net/aspose.pdf/pdfformat) אנומרציה: PDF_A_1A או PDF_A_1B.

{{% alert color="primary" %}}

פורמט ה-XML המוצא הוא פורמט מותאם אישי של Aspose. ה-XML מכיל אוסף של תגיות עם שם Problem; כל תגית מכילה את פרטי בעיה מסוימת. מאפיין ObjectID של תגית Problem מייצג את מזהה האובייקט שהבעיה קשורה אליו. מאפיין ה-Clause מייצג כלל תואם במפרט ה-PDF.

{{% /alert %}}

הקטע קוד הבא עובד גם עם ספריית [Aspose.PDF.Drawing](/pdf/net/drawing/).

הקטע קוד הבא מראה לך כיצד לאמת מסמך PDF ל-PDF/A-1A.
הקטע הבא מראה כיצד לאמת מסמך PDF עבור PDF/A-1A.

```csharp
// לדוגמאות מלאות וקבצי נתונים, אנא בקר ב https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לספריית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// פתח מסמך
Document pdfDocument = new Document(dataDir + "ValidatePDFAStandard.pdf");

// אמת PDF עבור PDF/A-1a
pdfDocument.Validate(dataDir + "validation-result-A1A.xml", PdfFormat.PDF_A_1A);
```

הקטע הבא מראה כיצד לאמת מסמך PDF עבור PDF/A-1B.

```csharp
// לדוגמאות מלאות וקבצי נתונים, אנא בקר ב https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לספריית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// פתח מסמך
Document pdfDocument = new Document(dataDir + "ValidatePDFAStandard.pdf");

// אמת PDF עבור PDF/A-1b
pdfDocument.Validate(dataDir + "validation-result-A1A.xml", PdfFormat.PDF_A_1B);
```
{{% alert color="primary" %}}

Aspose.PDF עבור .NET יכול לשמש לקבוע אם המסמך שנטען הוא PDF תקף וגם [אם הוא מוצפן או לא](https://docs.aspose.com/pdf/net/set-privileges-encrypt-and-decrypt-pdf-file/). כדי להרחיב עוד את יכולות המחלקה Document, נוספה תכונה בשם *IsPdfaCompliant* לקביעה אם קובץ הקלט תואם PDF/A ותכונה בשם *PdfaFormat* לזיהוי פורמט ה-PDF/A.

{{% /alert %}}

## עבודה עם תוכן עניינים

### הוספת תוכן עניינים ל-PDF קיים

ממשק Aspose.PDF מאפשר לך להוסיף תוכן עניינים בין אם בעת יצירת PDF חדש, או לקובץ קיים. המחלקה ListSection במרחב השמות Aspose.Pdf.Generator מאפשרת לך ליצור תוכן עניינים בעת יצירת PDF מאפס. להוספת כותרות, שהן אלמנטים של תוכן העניינים, השתמש במחלקה Aspose.Pdf.Generator.Heading.

להוספת תוכן עניינים לקובץ PDF קיים, השתמש במחלקה Heading במרחב השמות Aspose.Pdf.
כדי להוסיף תוכן עניינים לקובץ PDF קיים, השתמש במחלקה Heading במרחב השמות Aspose.Pdf.

```csharp
// לדוגמאות מלאות וקבצי נתונים, אנא עבור ל https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לתיקיית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// טען קבצי PDF קיימים
Document doc = new Document(dataDir + "AddTOC.pdf");

// קבל גישה לעמוד הראשון של קובץ PDF
Page tocPage = doc.Pages.Insert(1);

// צור אובייקט לייצוג מידע TOC
TocInfo tocInfo = new TocInfo();
TextFragment title = new TextFragment("תוכן העניינים");
title.TextState.FontSize = 20;
title.TextState.FontStyle = FontStyles.Bold;

// הגדר את הכותרת ל-TOC
tocInfo.Title = title;
tocPage.TocInfo = tocInfo;

// צור אובייקטי מחרוזת שישמשו כאלמנטים של TOC
string[] titles = new string[4];
titles[0] = "עמוד ראשון";
titles[1] = "עמוד שני";
titles[2] = "עמוד שלישי";
titles[3] = "עמוד רביעי";
for (int i = 0; i < 2; i++)
{
    // צור אובייקט Heading
    Aspose.Pdf.Heading heading2 = new Aspose.Pdf.Heading(1);
    TextSegment segment2 = new TextSegment();
    heading2.TocPage = tocPage;
    heading2.Segments.Add(segment2);

    // ציין את עמוד היעד לאובייקט הכותרת
    heading2.DestinationPage = doc.Pages[i + 2];

    // עמוד יעד
    heading2.Top = doc.Pages[i + 2].Rect.Height;

    // קואורדינטת יעד
    segment2.Text = titles[i];

    // הוסף כותרת לעמוד המכיל TOC
    tocPage.Paragraphs.Add(heading2);
}
dataDir = dataDir + "TOC_out.pdf";
// שמור את המסמך המעודכן
doc.Save(dataDir);
```
### הגדר סוג TabLeaderType שונה לרמות TOC שונות

Aspose.PDF מאפשרת גם הגדרת סוג TabLeaderType שונה לרמות TOC שונות. עליך להגדיר את התכונה LineDash של FormatArray עם הערך המתאים של אימום TabLeaderType כדלהלן.

```csharp
 string outFile = "TOC.pdf";

Aspose.Pdf.Document doc = new Aspose.Pdf.Document();
Page tocPage = doc.Pages.Add();
TocInfo tocInfo = new TocInfo();

//הגדרת סוג המנהיג
tocInfo.LineDash = TabLeaderType.Solid;
TextFragment title = new TextFragment("תוכן העניינים");
title.TextState.FontSize = 30;
tocInfo.Title = title;

//הוסף את קטע הרשימה לאוסף הפרקים של מסמך ה-PDF
tocPage.TocInfo = tocInfo;
//הגדר את פורמט של ארבע רמות הרשימה על ידי הגדרת השוליים השמאליים
//והגדרות פורמט הטקסט של כל רמה

tocInfo.FormatArrayLength = 4;
tocInfo.FormatArray[0].Margin.Left = 0;
tocInfo.FormatArray[0].Margin.Right = 30;
tocInfo.FormatArray[0].LineDash = TabLeaderType.Dot;
tocInfo.FormatArray[0].TextState.FontStyle = FontStyles.Bold | FontStyles.Italic;
tocInfo.FormatArray[1].Margin.Left = 10;
tocInfo.FormatArray[1].Margin.Right = 30;
tocInfo.FormatArray[1].LineDash = TabLeaderType.None;
tocInfo.FormatArray[1].TextState.FontSize = 10;
tocInfo.FormatArray[2].Margin.Left = 20;
tocInfo.FormatArray[2].Margin.Right = 30;
tocInfo.FormatArray[2].TextState.FontStyle = FontStyles.Bold;
tocInfo.FormatArray[3].LineDash = TabLeaderType.Solid;
tocInfo.FormatArray[3].Margin.Left = 30;
tocInfo.FormatArray[3].Margin.Right = 30;
tocInfo.FormatArray[3].TextState.FontStyle = FontStyles.Bold;

//צור פרק במסמך ה-PDF
Page page = doc.Pages.Add();

//הוסף ארבעה כותרות בפרק
for (int Level = 1; Level <= 4; Level++)
{

    Aspose.Pdf.Heading heading2 = new Aspose.Pdf.Heading(Level);
    TextSegment segment2 = new TextSegment();
    heading2.Segments.Add(segment2);
    heading2.IsAutoSequence = true;
    heading2.TocPage = tocPage;
    segment2.Text = "כותרת לדוגמא" + Level;
    heading2.TextState.Font = FontRepository.FindFont("Arial Unicode MS");

    //הוסף את הכותרת לתוכן העניינים.
    heading2.IsInList = true;
    page.Paragraphs.Add(heading2);
}

// שמור את ה-PDF

doc.Save(outFile);
```
### הסתר מספרי עמודים בתוכן העניינים

במקרה שאתה לא רוצה להציג מספרי עמודים, יחד עם הכותרות בתוכן העניינים, תוכל להשתמש בתכונה [IsShowPageNumbers](https://reference.aspose.com/pdf/net/aspose.pdf/tocinfo/properties/isshowpagenumbers) של מחלקת [TOCInfo](https://reference.aspose.com/pdf/net/aspose.pdf/tocinfo) כשקר false. אנא בדוק את קטע הקוד הבא להסתרת מספרי העמודים בתוכן העניינים:

```csharp
// לדוגמאות מלאות וקבצי נתונים, אנא עבור אל https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לספריית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
string outFile = dataDir + "HiddenPageNumbers_out.pdf";
Document doc = new Document();
Page tocPage = doc.Pages.Add();
TocInfo tocInfo = new TocInfo();
TextFragment title = new TextFragment("תוכן העניינים");
title.TextState.FontSize = 20;
title.TextState.FontStyle = FontStyles.Bold;
tocInfo.Title = title;
//הוסף את חלק הרשימה לאוסף החלקים של מסמך ה-Pdf
tocPage.TocInfo = tocInfo;
//הגדר את פורמט הרמות הארבע ברשימה על ידי הגדרת שוליים שמאליים ו
//הגדרות פורמט הטקסט של כל רמה

tocInfo.IsShowPageNumbers = false;
tocInfo.FormatArrayLength = 4;
tocInfo.FormatArray[0].Margin.Right = 0;
tocInfo.FormatArray[0].TextState.FontStyle = FontStyles.Bold | FontStyles.Italic;
tocInfo.FormatArray[1].Margin.Left = 30;
tocInfo.FormatArray[1].TextState.Underline = true;
tocInfo.FormatArray[1].TextState.FontSize = 10;
tocInfo.FormatArray[2].TextState.FontStyle = FontStyles.Bold;
tocInfo.FormatArray[3].TextState.FontStyle = FontStyles.Bold;
Page page = doc.Pages.Add();
//הוסף ארבעה כותרות בחלק
for (int Level = 1; Level != 5; Level++)

{ Heading heading2 = new Heading(Level); TextSegment segment2 = new TextSegment(); heading2.TocPage = tocPage; heading2.Segments.Add(segment2); heading2.IsAutoSequence = true; segment2.Text = "זהו כותרת של רמה " + Level; heading2.IsInList = true; page.Paragraphs.Add(heading2); }
doc.Save(outFile);
```
### התאמת מספרי עמודים בעת הוספת תוכן עניינים

נפוץ להתאים אישית את מספור העמודים בתוכן העניינים בעת הוספת תוכן עניינים במסמך PDF. לדוגמה, ייתכן שנצטרך להוסיף קידומת מסוימת לפני מספר העמוד כמו P1, P2, P3 וכדומה. במקרה כזה, Aspose.PDF עבור .NET מספק את התכונה PageNumbersPrefix של המחלקה TocInfo שניתן להשתמש בה להתאמת מספרי העמודים כפי שמוצג בדוגמת הקוד הבאה.

```csharp
// לדוגמאות מלאות וקבצי נתונים, נא לעבור ל https://github.com/aspose-pdf/Aspose.PDF-for-.NET
string inFile = RunExamples.GetDataDir_AsposePdf_WorkingDocuments() + "42824.pdf";
string outFile = RunExamples.GetDataDir_AsposePdf_WorkingDocuments() + "42824_out.pdf";
// טען קובץ PDF קיים
Document doc = new Document(inFile);
// קבל גישה לעמוד הראשון של קובץ PDF
Aspose.Pdf.Page tocPage = doc.Pages.Insert(1);
// צור אובייקט לייצוג מידע TOC
TocInfo tocInfo = new TocInfo();
TextFragment title = new TextFragment("תוכן העניינים");
title.TextState.FontSize = 20;
title.TextState.FontStyle = FontStyles.Bold;
// קבע את הכותרת לתוכן העניינים
tocInfo.Title = title;
tocInfo.PageNumbersPrefix = "P";
tocPage.TocInfo = tocInfo;
for (int i = 1; i<doc.Pages.Count; i++)
{
    // צור אובייקט Heading
    Aspose.Pdf.Heading heading2 = new Aspose.Pdf.Heading(1);
    TextSegment segment2 = new TextSegment();
    heading2.TocPage = tocPage;
    heading2.Segments.Add(segment2);
    // ציין את העמוד היעד לאובייקט הכותרת
    heading2.DestinationPage = doc.Pages[i + 1];
    // עמוד יעד
    heading2.Top = doc.Pages[i + 1].Rect.Height;
    // קואורדינטה יעד
    segment2.Text = "עמוד " + i.ToString();
    // הוסף כותרת לעמוד המכיל תוכן עניינים
    tocPage.Paragraphs.Add(heading2);
}

// שמור את המסמך המעודכן
doc.Save(outFile);
```
## איך לקבוע תאריך תפוגה לקובץ PDF

אנו מחילים הרשאות גישה על קבצי PDF כך שקבוצה מסוימת של משתמשים תוכל לגשת לתכונות/אובייקטים מסוימים במסמכי PDF. כדי להגביל את הגישה לקובץ PDF, אנו מחילים הצפנה ולעיתים יש לנו דרישה לקבוע תאריך תפוגה לקובץ PDF, כך שהמשתמש שגולש/צופה במסמך יקבל התראה תקפה לגבי תפוגת הקובץ.

כדי להשיג את הדרישה שצוינה לעיל, אנו יכולים להשתמש באובייקט *JavascriptAction*. אנא הסתכלו על קטע הקוד הבא.

```csharp
// לדוגמאות מלאות וקבצי נתונים, אנא עברו ל https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לתיקיית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// יצירת אובייקט מסמך
Aspose.Pdf.Document doc = new Aspose.Pdf.Document();
// הוספת דף לאוסף הדפים של קובץ PDF
doc.Pages.Add();
// הוספת קטע טקסט לאוסף הפסקאות של אובייקט הדף
doc.Pages[1].Paragraphs.Add(new TextFragment("שלום עולם..."));
// יצירת אובייקט JavaScript כדי לקבוע תאריך תפוגה ל-PDF
JavascriptAction javaScript = new JavascriptAction(
"var year=2017;"
+ "var month=5;"
+ "today = new Date(); today = new Date(today.getFullYear(), today.getMonth());"
+ "expiry = new Date(year, month);"
+ "if (today.getTime() > expiry.getTime())"
+ "app.alert('הקובץ פג תוקף. נדרש קובץ חדש.');");
// קביעת JavaScript כפעולת פתיחת PDF
doc.OpenAction = javaScript;

dataDir = dataDir + "SetExpiryDate_out.pdf";
// שמירת מסמך PDF
doc.Save(dataDir);
```
## קביעת התקדמות יצירת קובץ PDF

לקוח ביקש מאיתנו להוסיף תכונה שמאפשרת למפתחים לקבוע את התקדמות יצירת קובץ PDF. הנה התגובה לבקשה זו.

השדה [CustomerProgressHandler](https://reference.aspose.com/pdf/net/aspose.pdf/docsaveoptions/fields/customprogresshandler) של מחלקת [DocSaveOptions](https://reference.aspose.com/pdf/net/aspose.pdf/docsaveoptions) מאפשר לך לקבוע איך הולכת יצירת ה-PDF. למטפל יש את הסוגים הבאים:

- DocSaveOptions.ConversionProgessEventHandler
- DocSaveOptions.ProgressEventHandlerInfo
- DocSaveOptions.ProgressEventType

הדוגמאות לקוד למטה מראות איך להשתמש ב-CustomerProgressHandler.

```csharp
// לדוגמאות מלאות וקבצי נתונים, בבקשה עבורו ל https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לתיקיית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// פתח מסמך
Document pdfDocument = new Document(dataDir + "AddTOC.pdf");
DocSaveOptions saveOptions = new DocSaveOptions();
saveOptions.CustomProgressHandler = new UnifiedSaveOptions.ConversionProgressEventHandler(ShowProgressOnConsole);

dataDir = dataDir + "DetermineProgress_out.pdf";
pdfDocument.Save(dataDir, saveOptions);
Console.ReadLine();
```
```csharp
// לדוגמאות מלאות וקבצי נתונים, אנא בקרו ב https://github.com/aspose-pdf/Aspose.PDF-for-.NET
public static void ShowProgressOnConsole(DocSaveOptions.ProgressEventHandlerInfo eventInfo)
{
    switch (eventInfo.EventType)
    {
        case DocSaveOptions.ProgressEventType.TotalProgress:
            Console.WriteLine(String.Format("{0}  - התקדמות ההמרה : {1}% .", DateTime.Now.ToLongTimeString(), eventInfo.Value.ToString()));
            break;
        case DocSaveOptions.ProgressEventType.SourcePageAnalized:
            Console.WriteLine(String.Format("{0}  - דף מקור {1} מתוך {2} נבדק.", DateTime.Now.ToLongTimeString(), eventInfo.Value.ToString(), eventInfo.MaxValue.ToString()));
            break;
        case DocSaveOptions.ProgressEventType.ResultPageCreated:
            Console.WriteLine(String.Format("{0}  - פריסת דף התוצאה {1} מתוך {2} נוצרה.", DateTime.Now.ToLongTimeString(), eventInfo.Value.ToString(), eventInfo.MaxValue.ToString()));
            break;
        case DocSaveOptions.ProgressEventType.ResultPageSaved:
            Console.WriteLine(String.Format("{0}  - דף התוצאה {1} מתוך {2} יוצא.", DateTime.Now.ToLongTimeString(), eventInfo.Value.ToString(), eventInfo.MaxValue.ToString()));
            break;
        default:
            break;
    }

}
```
## החלקת מסמך PDF מילוי ב-C#

מסמכי PDF לעיתים כוללים טפסים עם ווידג'טים מילויים אינטרקטיביים כגון כפתורי רדיו, תיבות סימון, תיבות טקסט, רשימות וכו'. כדי להפוך אותו ללא ניתן לעריכה למטרות שונות, אנו צריכים להחליק את קובץ ה-PDF.
Aspose.PDF מספקת את הפונקציה להחלקת ה-PDF שלך ב-C# בקוד קצר:

```csharp
// טעינת טופס PDF מקורי
Document doc = new Document(dataDir + "input.pdf");

// החלקת טופס PDF מילוי
if (doc.Form.Fields.Count() > 0)
{
    foreach (var item in doc.Form.Fields)
    {
        item.Flatten();
    }
}

dataDir = dataDir + "FlattenForms_out.pdf";
// שמירת המסמך המעודכן
doc.Save(dataDir);
```

