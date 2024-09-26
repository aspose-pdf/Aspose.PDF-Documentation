---
title: הוספת טקסט ל-PDF באמצעות C#
linktitle: הוספת טקסט ל-PDF
type: docs
weight: 10
url: /net/add-text-to-pdf-file/
description: מאמר זה מתאר מגוון היבטים של עבודה עם טקסט ב-Aspose.PDF. למד כיצד להוסיף טקסט ל-PDF, להוסיף קטעי HTML או להשתמש בגופנים OTF מותאמים אישית.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
aliases:
    - /net/add-text-to-a-pdf-file/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "הוספת טקסט ל-PDF באמצעות C#",
    "alternativeHeadline": "כיצד להוסיף טקסט ל-PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "יצירת מסמכי PDF",
    "keywords": "pdf, c#, הוספת טקסט ל-pdf",
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
    "url": "/net/add-text-to-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-text-to-pdf-file/"
    },
    "dateModified": "2022-02-04",
    "description": "מאמר זה מתאר מגוון היבטים של עבודה עם טקסט ב-Aspose.PDF. למד כיצד להוסיף טקסט ל-PDF, להוסיף קטעי HTML או להשתמש בגופנים OTF מותאמים אישית."
}
</script>
הקטע הבא עובד גם עם ספריית [Aspose.PDF.Drawing](/pdf/net/drawing/).

להוסיף טקסט לקובץ PDF קיים:

1. פתח את קובץ ה-PDF הקיים באמצעות אובייקט Document.
2. קבל את העמוד הספציפי שאליו אתה מעוניין להוסיף את הטקסט.
3. צור אובייקט TextFragment עם הטקסט הנכנס יחד עם תכונות טקסט נוספות. האובייקט TextBuilder שנוצר מאותו עמוד – אליו אתה מעוניין להוסיף את הטקסט – מאפשר לך להוסיף את אובייקט TextFragment לעמוד באמצעות השיטה AppendText.
4. קרא לשיטת Save של אובייקט Document ושמור את קובץ ה-PDF הפלט.

## הוספת טקסט

הקטע הבא מראה כיצד להוסיף טקסט בקובץ PDF קיים.

```csharp
// לדוגמאות מלאות וקבצי נתונים, אנא עבור אל https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לתיקיית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// פתח מסמך
Document pdfDocument = new Document(dataDir + "input.pdf");

// קבל עמוד מסוים
Page pdfPage = (Page)pdfDocument.Pages[1];

// צור קטע טקסט
TextFragment textFragment = new TextFragment("main text");
textFragment.Position = new Position(100, 600);

// הגדר תכונות טקסט
textFragment.TextState.FontSize = 12;
textFragment.TextState.Font = FontRepository.FindFont("TimesNewRoman");
textFragment.TextState.BackgroundColor = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.LightGray);
textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.Red);

// צור אובייקט TextBuilder
TextBuilder textBuilder = new TextBuilder(pdfPage);

// הוסף את קטע הטקסט לעמוד PDF
textBuilder.AppendText(textFragment);

dataDir = dataDir + "AddText_out.pdf";

// שמור את מסמך PDF המתקבל.
pdfDocument.Save(dataDir);
```
## טעינת גופן מתוך זרם

הקטע קוד הבא מראה כיצד לטעון גופן מאובייקט זרם בעת הוספת טקסט למסמך PDF.

```csharp
// לדוגמאות מלאות וקבצי נתונים, נא לבקר ב https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לספריית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
string fontFile = "";

// טען קובץ PDF קלט
Document doc = new Document(dataDir + "input.pdf");
// צור אובייקט בונה טקסט לעמוד הראשון של המסמך
TextBuilder textBuilder = new TextBuilder(doc.Pages[1]);
// צור קטע טקסט עם מחרוזת לדוגמא
TextFragment textFragment = new TextFragment("Hello world");

if (fontFile != "")
{
    // טען את הגופן TrueType לתוך אובייקט זרם
    using (FileStream fontStream = File.OpenRead(fontFile))
    {
        // הגדר את שם הגופן למחרוזת הטקסט
        textFragment.TextState.Font = FontRepository.OpenFont(fontStream, FontTypes.TTF);
        // ציין את המיקום לקטע הטקסט
        textFragment.Position = new Position(10, 10);
        // הוסף את הטקסט ל-TextBuilder כך שניתן יהיה למקם אותו מעל קובץ ה-PDF
        textBuilder.AppendText(textFragment);
    }

    dataDir = dataDir + "LoadingFontFromStream_out.pdf";

    // שמור את מסמך PDF המתקבל.
    doc.Save(dataDir);
}
```

## הוספת טקסט באמצעות TextParagraph

הקטע הבא מראה איך להוסיף טקסט במסמך PDF באמצעות המחלקה [TextParagraph](https://reference.aspose.com/pdf/net/aspose.pdf.text/textparagraph).

```csharp
// לדוגמאות מלאות וקבצי נתונים, אנא עבור ל https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לתיקיית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// פתיחת מסמך
Document doc = new Document();
// הוספת דף לאוסף הדפים של אובייקט המסמך
Page page = doc.Pages.Add();
TextBuilder builder = new TextBuilder(page);
// יצירת פסקת טקסט
TextParagraph paragraph = new TextParagraph();
// הגדרת הזחה לשורות הבאות
paragraph.SubsequentLinesIndent = 20;
// ציון המיקום להוספת TextParagraph
paragraph.Rectangle = new Aspose.Pdf.Rectangle(100, 300, 200, 700);
// ציון מצב גלילת המילים
paragraph.FormattingOptions.WrapMode = TextFormattingOptions.WordWrapMode.ByWords;
// יצירת קטע טקסט
TextFragment fragment1 = new TextFragment("the quick brown fox jumps over the lazy dog");
fragment1.TextState.Font = FontRepository.FindFont("Times New Roman");
fragment1.TextState.FontSize = 12;
// הוספת קטע לפסקה
paragraph.AppendLine(fragment1);
// הוספת פסקה
builder.AppendParagraph(paragraph);

dataDir = dataDir + "AddTextUsingTextParagraph_out.pdf";

// שמירת מסמך PDF המתקבל.
doc.Save(dataDir);
```
## הוספת קישור לקטע טקסט

דף PDF עשוי להכיל עצם אחד או יותר של TextFragment, כאשר לכל עצם TextFragment יכול להיות יותר ממופע אחד של TextSegment. כדי להגדיר קישור ל-TextSegment, ניתן להשתמש במאפיין Hyperlink של מחלקת [TextSegment](https://reference.aspose.com/pdf/net/aspose.pdf.text/textsegment) תוך ספק את המופע של מופע Aspose.Pdf.WebHyperlink. נסה להשתמש בקטע הקוד הבא כדי להשיג דרישה זו.

```csharp
// לדוגמאות מלאות וקבצי נתונים, אנא עבור ל https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לתיקיית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// צור מופע של מסמך
Document doc = new Document();
// הוסף דף לאוסף הדפים של קובץ PDF
Page page1 = doc.Pages.Add();
// צור מופע של TextFragment
TextFragment tf = new TextFragment("דוגמה לקטע טקסט");
// הגדר יישור אופקי ל-TextFragment
tf.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Right;
// צור textsegment עם טקסט לדוגמה
TextSegment segment = new TextSegment(" ... קטע טקסט 1...");
// הוסף קטע לאוסף הקטעים של TextFragment
tf.Segments.Add(segment);
// צור TextSegment חדש
segment = new TextSegment("קישור ל-Google");
// הוסף קטע לאוסף הקטעים של TextFragment
tf.Segments.Add(segment);
// הגדר קישור ל-TextSegment
segment.Hyperlink = new Aspose.Pdf.WebHyperlink("www.google.com");
// הגדר צבע קדמי לקטע טקסט
segment.TextState.ForegroundColor = Aspose.Pdf.Color.Blue;
// הגדר עיצוב טקסט כנטוי
segment.TextState.FontStyle = FontStyles.Italic;
// צור עצם TextSegment נוסף
segment = new TextSegment("TextSegment ללא קישור");
// הוסף קטע לאוסף הקטעים של TextFragment
tf.Segments.Add(segment);
// הוסף TextFragment לאוסף הפסקאות של אובייקט הדף
page1.Paragraphs.Add(tf);

dataDir = dataDir + "AddHyperlinkToTextSegment_out.pdf";

// שמור את מסמך PDF המתקבל.
doc.Save(dataDir);
```
## שימוש בגופן OTF

Aspose.PDF עבור .NET מציעה את התכונה להשתמש בגופנים מותאמים אישית/TrueType בעת יצירה/עריכה של תוכן קובץ PDF כך שתוכן הקובץ יוצג באמצעות תוכן שאינו גופני מערכת ברירת המחדל. החל משחרור Aspose.PDF עבור .NET 10.3.0, סיפקנו תמיכה בגופני פתוחים.

```csharp
// לדוגמאות מלאות וקבצי נתונים, אנא עבורו ל https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לספריית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// צור מופע מסמך חדש
Document pdfDocument = new Document();
// הוסף דף לאוסף הדפים של קובץ PDF
Aspose.Pdf.Page page = pdfDocument.Pages.Add();
// צור מופע TextFragment עם טקסט לדוגמה
TextFragment fragment = new TextFragment("Sample Text in OTF font");
// מצא גופן בתיקיית הגופנים של המערכת
// Fragment.TextState.Font = FontRepository.FindFont("HelveticaNeueLT Pro 45 Lt");
// או אפשר גם לציין את נתיב הגופן OTF בתיקיית המערכת
fragment.TextState.Font = FontRepository.OpenFont(dataDir + "space age.otf");
// ציין להטמיע גופן בתוך קובץ PDF, כך שיצוגו יהיה נכון,
// גם אם הגופן הספציפי אינו מותקן/נמצא על המכונה היעד
fragment.TextState.Font.IsEmbedded = true;
// הוסף TextFragment לאוסף הפסקאות של מופע הדף
page.Paragraphs.Add(fragment);

dataDir = dataDir + "OTFFont_out.pdf";

// שמור את מסמך PDF המתקבל.
pdfDocument.Save(dataDir);
```
## הוספת מחרוזת HTML באמצעות DOM

המחלקה Aspose.Pdf.Generator.Text מכילה תכונה בשם IsHtmlTagSupported שמאפשרת להוסיף תגי HTML/תוכן לקובצי PDF. התוכן שנוסף מוצג בתגי HTML ילידים במקום להופיע כמחרוזת טקסט פשוטה. כדי לתמוך בתכונה דומה במודל האובייקט החדש (DOM) של מרחב השמות Aspose.Pdf, הוצגה המחלקה HtmlFragment.

ניתן להשתמש במופע של [HtmlFragment](https://reference.aspose.com/pdf/net/aspose.pdf/htmlfragment) כדי לציין את תוכן ה-HTML שצריך להמקם בתוך קובץ ה-PDF. בדומה ל-TextFragment, HtmlFragment היא אובייקט ברמת פסקה וניתן להוסיפה לאוסף הפסקאות של אובייקט הדף. קטעי הקוד הבאים מראים את השלבים למיקום תוכן HTML בתוך קובץ PDF באמצעות גישת DOM.

```csharp
// לדוגמאות מלאות וקבצי נתונים, אנא עבור אל https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לתיקיית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// יצירת אובייקט מסמך
Document doc = new Document();
// הוספת דף לאוסף הדפים של קובץ ה-PDF
Page page = doc.Pages.Add();
// יצירת HtmlFragment עם תוכן HTML
HtmlFragment title = new HtmlFragment("<fontsize=10><b><i>שולחן</i></b></fontsize>");
// הגדרת מידע על שוליים תחתונים
title.Margin.Bottom = 10;
// הגדרת מידע על שוליים עליונים
title.Margin.Top = 200;
// הוספת קטע HTML לאוסף הפסקאות של הדף
page.Paragraphs.Add(title);

dataDir = dataDir + "AddHTMLUsingDOM_out.pdf";
// שמירת קובץ ה-PDF
doc.Save(dataDir);
```
הקטע הבא מדגים את השלבים להוספת רשימות מסודרות ב-HTML למסמך:

```csharp
// לדוגמאות מלאות וקבצי נתונים, אנא עברו ל https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לספריית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// הנתיב למסמך הפלט.
string outFile = dataDir + "AddHTMLOrderedListIntoDocuments_out.pdf";
// יצירת אובייקט מסמך
Document doc = new Document();
// יצירת אובייקט HtmlFragment עם קטע ה-HTML המתאים
HtmlFragment t = new HtmlFragment("`<body style='line-height: 100px;'><ul><li>ראשון</li><li>שני</li><li>שלישי</li><li>רביעי</li><li>חמישי</li></ul>טקסט אחרי הרשימה.<br/>שורה הבאה<br/>השורה האחרונה</body>`");
// הוספת דף לאוסף הדפים
Page page = doc.Pages.Add();
// הוספת HtmlFragment לתוך הדף
page.Paragraphs.Add(t);
// שמירת קובץ PDF המתקבל
doc.Save(outFile);
```

ניתן גם להגדיר עיצוב מחרוזת HTML באמצעות אובייקט TextState כך:

```csharp
// לדוגמאות מלאות וקבצי נתונים, אנא עברו ל https://github.com/aspose-pdf/Aspose.PDF-for-.NET
HtmlFragment html = new HtmlFragment("טקסט כלשהו");
html.TextState = new TextState();
html.TextState.Font = FontRepository.FindFont("Calibri");
```
במקרה שבו אתה מגדיר ערכי תכונות טקסט באמצעות סימון HTML ולאחר מכן מספק את אותם ערכים בתכונות TextState, הם ידרסו את פרמטרי ה-HTML על ידי תכונות ממופע TextState. קטעי הקוד הבאים מדגימים את ההתנהגות המתוארת.

```csharp
// עבור דוגמאות מלאות וקבצי נתונים, אנא בקר ב https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לספריית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// יצירת אובייקט מסמך
Document doc = new Document();
// הוספת דף לאוסף הדפים של קובץ PDF
Page page = doc.Pages.Add();
// יצירת HtmlFragment עם תוכן HTML
HtmlFragment title = new HtmlFragment("<p style='font-family: Verdana'><b><i>Table contains text</i></b></p>");
// גופן מ-'Verdana' יאופס ל-'Arial'
title.TextState = new TextState("Arial");
title.TextState.FontSize = 20;
// הגדרת מידע על שוליים תחתונים
title.Margin.Bottom = 10;
// הגדרת מידע על שוליים עליונים
title.Margin.Top = 400;
// הוספת קטע HTML לאוסף הפסקאות של הדף
page.Paragraphs.Add(title);
// שמירת קובץ PDF
dataDir = dataDir + "AddHTMLUsingDOMAndOverwrite_out.pdf";
// שמירת קובץ PDF
doc.Save(dataDir);
```
## הערות שוליים והערות סופיות (DOM)

הערות שוליים מציינות הערות בטקסט של המאמר שלך באמצעות מספרים עוקבים בכתב עילי. ההערה עצמה מוזחת ויכולה להופיע כהערת שוליים בתחתית הדף.

### הוספת הערת שוליים

במערכת הפנייה עם הערות שוליים, יש לציין הפניה על ידי:

- שים מספר קטן מעל קו הטיפוס באופן ישיר אחרי חומר המקור. מספר זה נקרא מזהה הערה. הוא ממוקם מעט מעל לשורת הטקסט.
- שים את אותו מספר, ולאחריו ציטוט של מקורך, בתחתית הדף. ההערת שוליים צריכה להיות מספרית ולפי סדר כרונולוגי: ההפניה הראשונה היא 1, השנייה היא 2, וכן הלאה.

היתרון של הערות שוליים הוא שהקורא יכול פשוט להוריד את עיניו לתחתית הדף כדי לגלות את מקור ההפניה שמעניינת אותו.

אנא עקוב אחר השלבים שצוינו להלן כדי ליצור הערת שוליים:

- צור מופע של מסמך
- צור אובייקט דף
- צור אובייקט קטע טקסט
- צור מופע של הערה והעבר את ערכה לתכונת TextFragment.FootNote
- צור מופע של Note והעבר את ערכו למאפיין TextFragment.FootNote
- הוסף TextFragment לאוסף הפסקאות של מופע דף

### סגנון קו מותאם אישית ל-FootNote

הדוגמה הבאה מדגימה כיצד להוסיף הערות שוליים בתחתית דף PDF ולהגדיר סגנון קו מותאם אישית.

```csharp
// לדוגמאות מלאות וקבצי נתונים, בבקשה לגשת ל https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לספריית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// צור מופע של מסמך
Document doc = new Document();
// הוסף דף לאוסף הדפים של PDF
Page page = doc.Pages.Add();
// צור מופע של GraphInfo
Aspose.Pdf.GraphInfo graph = new Aspose.Pdf.GraphInfo();
// הגדר רוחב קו ל-2
graph.LineWidth = 2;
// הגדר את צבע הגרף
graph.Color = Aspose.Pdf.Color.Red;
// הגדר ערך מערך המקטעים ל-3
graph.DashArray = new int[] { 3 };
// הגדר ערך שלב המקטע ל-1
graph.DashPhase = 1;
// הגדר את סגנון קו ההערה השולית לדף כגרף
page.NoteLineStyle = graph;
// צור מופע של TextFragment
TextFragment text = new TextFragment("Hello World");
// הגדר ערך FootNote ל-TextFragment
text.FootNote = new Note("foot note for test text 1");
// הוסף TextFragment לאוסף הפסקאות של דף ראשון של המסמך
page.Paragraphs.Add(text);
// צור TextFragment שני
text = new TextFragment("Aspose.Pdf for .NET");
// הגדר FootNote לקטע הטקסט השני
text.FootNote = new Note("foot note for test text 2");
// הוסף קטע טקסט שני לאוסף הפסקאות של קובץ PDF
page.Paragraphs.Add(text);

dataDir = dataDir + "CustomLineStyleForFootNote_out.pdf";

// שמור את מסמך PDF המתקבל.
doc.Save(dataDir);
```
ניתן להגדיר עיצוב של תווית הערת שוליים (מזהה הערה) באמצעות אובייקט TextState כדלקמן:

```csharp
TextFragment text = new TextFragment("test text 1");
text.FootNote = new Note("foot note for test text 1");
text.FootNote.Text = "21";
text.FootNote.TextState = new TextState();
text.FootNote.TextState.ForegroundColor = Aspose.Pdf.Color.Blue;
text.FootNote.TextState.FontStyle = FontStyles.Italic;
```

### התאמה אישית של תווית הערת שוליים

כברירת מחדל, מספר הערת השוליים עולה החל מ-1. עם זאת, ייתכן שיהיה לנו דרישה להגדיר תווית מותאמת אישית להערת שוליים. כדי לעמוד בדרישה זו, אנא נסה להשתמש בקטע הקוד הבא

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// Create Document instance
Document doc = new Document();
// Add page to pages collection of PDF
Page page = doc.Pages.Add();
// Create GraphInfo object
Aspose.Pdf.GraphInfo graph = new Aspose.Pdf.GraphInfo();
// Set line width as 2
graph.LineWidth = 2;
// Set the color for graph object
graph.Color = Aspose.Pdf.Color.Red;
// Set dash array value as 3
graph.DashArray = new int[] { 3 };
// Set dash phase value as 1
graph.DashPhase = 1;
// Set footnote line style for page as graph
page.NoteLineStyle = graph;
// Create TextFragment instance
TextFragment text = new TextFragment("Hello World");
// Set FootNote value for TextFragment
text.FootNote = new Note("foot note for test text 1");
// Specify custom label for FootNote
text.FootNote.Text = " Aspose(2015)";
// Add TextFragment to paragraphs collection of first page of document
page.Paragraphs.Add(text);

dataDir = dataDir + "CustomizeFootNoteLabel_out.pdf";
```
## הוספת תמונה וטבלה להערת שוליים

בגרסאות הקודמות, ניתן היה להוסיף תמיכה בהערות שוליים אך זה היה רלוונטי רק לאובייקט TextFragment. עם זאת, החל מגרסה Aspose.PDF for .NET 10.7.0, ניתן גם להוסיף הערת שוליים לאובייקטים נוספים במסמך PDF כמו טבלה, תאים וכו'. קטע הקוד הבא מראה את השלבים להוספת הערת שוליים לאובייקט TextFragment ולאחר מכן הוספת אובייקט תמונה וטבלה לאוסף הפסקאות של סעיף הערות השוליים.

```csharp
// לדוגמאות מלאות וקבצי נתונים, אנא בקרו ב https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לתיקיית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

Document doc = new Document();
Page page = doc.Pages.Add();
TextFragment text = new TextFragment("טקסט מסוים");
page.Paragraphs.Add(text);

text.FootNote = new Note();
Aspose.Pdf.Image image = new Aspose.Pdf.Image();
image.File = dataDir + "aspose-logo.jpg";
image.FixHeight = 20;
text.FootNote.Paragraphs.Add(image);
TextFragment footNote = new TextFragment("טקסט הערת שוליים");
footNote.TextState.FontSize = 20;
footNote.IsInLineParagraph = true;
text.FootNote.Paragraphs.Add(footNote);
Aspose.Pdf.Table table = new Aspose.Pdf.Table();
table.Rows.Add().Cells.Add().Paragraphs.Add(new TextFragment("שורה 1 תא 1"));
text.FootNote.Paragraphs.Add(table);

dataDir = dataDir + "AddImageAndTable_out.pdf";

// שמירת המסמך PDF המתקבל.
doc.Save(dataDir);
```
## כיצד ליצור הערות סוף

הערת סוף היא ציטוט מקור שמפנה את הקוראים למקום מסוים בסוף המאמר שבו הם יכולים למצוא את מקור המידע או המילים שנצטטו או שהוזכרו במאמר. כאשר משתמשים בהערות סוף, המשפט שצוטט או שנסקר או שנסכם מלווה במספר עילי.

הדוגמה הבאה מדגימה כיצד להוסיף הערת סוף בעמוד PDF.

```csharp
// לדוגמאות מלאות וקבצי נתונים, אנא בקרו ב https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לתיקיית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// צור מופע מסמך
Document doc = new Document();
// הוסף עמוד לאוסף העמודים של PDF
Page page = doc.Pages.Add();
// צור מופע של קטע טקסט
TextFragment text = new TextFragment("שלום עולם");
// הגדר ערך להערת סוף עבור קטע הטקסט
text.EndNote = new Note("הערת סוף לדוגמה");
// ציין תווית מותאמת אישית עבור הערת הסוף
text.EndNote.Text = " Aspose(2015)";
// הוסף קטע טקסט לאוסף הפסקאות של העמוד הראשון של המסמך
page.Paragraphs.Add(text);

dataDir = dataDir + "CreateEndNotes_out.pdf";
// שמור את מסמך PDF המתקבל.
doc.Save(dataDir);
```
## טקסט ותמונה כפסקה בשורה אחת

הפריסה המוגדרת כברירת מחדל של קובץ PDF היא פריסת זרימה (משמאל למעלה לימין למטה). לכן, כל אלמנט חדש שמתווסף לקובץ PDF מתווסף בזרימה התחתונה הימנית. עם זאת, ייתכן שיש לנו דרישה להציג אלמנטים שונים בעמוד, כגון תמונה וטקסט באותו הרמה (אחד אחרי השני). גישה אחת יכולה להיות ליצור מופע של Table ולהוסיף שני האלמנטים לתאים נפרדים. עם זאת, גישה נוספת יכולה להיות פסקה בשורה אחת. על ידי הגדרת התכונה IsInLineParagraph של תמונה וטקסט כ-true, פסקאות אלו יופיעו כפסקאות בשורה אחת לעומת אלמנטים אחרים בעמוד.

הקטע קוד הבא מראה לך כיצד להוסיף טקסט ותמונה כפסקאות בשורה אחת בקובץ PDF.

```csharp
// לדוגמאות מלאות וקבצי נתונים, נא ללכת ל https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לספריית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// יצירת מופע מסמך
Document doc = new Document();
// הוספת עמוד לאוסף העמודים של מופע המסמך
Page page = doc.Pages.Add();
// יצירת TextFragmnet
TextFragment text = new TextFragment("Hello World.. ");
// הוספת קטע טקסט לאוסף הפסקאות של אובייקט העמוד
page.Paragraphs.Add(text);
// יצירת מופע תמונה
Aspose.Pdf.Image image = new Aspose.Pdf.Image();
// הגדרת התמונה כפסקה בשורה אחת כך שתופיע מיד אחרי
// אובייקט הפסקה הקודם (TextFragment)
image.IsInLineParagraph = true;
// ציון נתיב קובץ התמונה
image.File = dataDir + "aspose-logo.jpg";
// הגדרת גובה התמונה (אופציונלי)
image.FixHeight = 30;
// הגדרת רוחב התמונה (אופציונלי)
image.FixWidth = 100;
// הוספת התמונה לאוסף הפסקאות של אובייקט העמוד
page.Paragraphs.Add(image);
// אתחול מחדש של אובייקט TextFragment עם תוכן שונה
text = new TextFragment(" Hello Again..");
// הגדרת TextFragment כפסקה בשורה אחת
text.IsInLineParagraph = true;
// הוספת קטע הטקסט החדש לאוסף הפסקאות של העמוד
page.Paragraphs.Add(text);

dataDir = dataDir + "TextAndImageAsParagraph_out.pdf";
doc.Save(dataDir);
```
## ציין ריווח תווים בעת הוספת טקסט

ניתן להוסיף טקסט בתוך אוסף פסקאות של קבצי PDF באמצעות מופע של TextFragment או באמצעות אובייקט TextParagraph ואפילו ניתן לחותם את הטקסט בתוך PDF באמצעות מחלקת TextStamp. בעת הוספת הטקסט, ייתכן שיהיה צורך לציין ריווח תווים עבור אובייקטי הטקסט. כדי לעמוד בדרישה זו, תכונה חדשה בשם תכונת CharacterSpacing הוצגה. אנא עיין בגישות הבאות כדי לעמוד בדרישה זו.

הגישות הבאות מציגות את השלבים לציון ריווח תווים בעת הוספת טקסט בתוך מסמך PDF.

### באמצעות TextBuilder ו-TextFragment

```csharp
// לדוגמאות מלאות וקבצי נתונים, אנא עבור אל https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לספריית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// צור מופע של מסמך
Document pdfDocument = new Document();
// הוסף עמוד לאוסף העמודים של המסמך
Page page = pdfDocument.Pages.Add();
// צור מופע של TextBuilder
TextBuilder builder = new TextBuilder(pdfDocument.Pages[1]);
// צור מופע של קטע טקסט עם תוכן דוגמא
TextFragment wideFragment = new TextFragment("Text with increased character spacing");
wideFragment.TextState.ApplyChangesFrom(new TextState("Arial", 12));
// ציין ריווח תווים עבור TextFragment
wideFragment.TextState.CharacterSpacing = 2.0f;
// ציין את מיקום קטע הטקסט
wideFragment.Position = new Position(100, 650);
// הוסף קטע טקסט למופע של TextBuilder
builder.AppendText(wideFragment);
dataDir = dataDir + "CharacterSpacingUsingTextBuilderAndFragment_out.pdf";
// שמור את המסמך PDF המתקבל.
pdfDocument.Save(dataDir);
```
### שימוש בTextParagraph

```csharp
// לדוגמאות מלאות וקבצי נתונים, אנא עבור ל https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לתיקיית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// יצירת מופע מסמך
Document pdfDocument = new Document();
// הוספת דף לאוסף הדפים של מסמך
Page page = pdfDocument.Pages.Add();
// יצירת מופע TextBuilder
TextBuilder builder = new TextBuilder(pdfDocument.Pages[1]);
// יצירת מופע TextParagraph
TextParagraph paragraph = new TextParagraph();
// יצירת מופע TextState כדי לציין שם גופן וגודל
TextState state = new TextState("Arial", 12);
// ציון הריווח בין תווים
state.CharacterSpacing = 1.5f;
// הוספת טקסט לאובייקט TextParagraph
paragraph.AppendLine("זהו פסקה עם ריווח תווים", state);
// ציון המיקום עבור TextParagraph
paragraph.Position = new Position(100, 550);
// הוספת TextParagraph למופע TextBuilder
builder.AppendParagraph(paragraph);

dataDir = dataDir + "CharacterSpacingUsingTextBuilderAndParagraph_out.pdf";
// שמירת מסמך PDF המתקבל.
pdfDocument.Save(dataDir);
```
### שימוש בTextStamp

```csharp
// לדוגמאות מלאות וקבצי נתונים, אנא עבור ל https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לתיקיית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// יצירת מופע מסמך
Document pdfDocument = new Document();
// הוספת דף לאוסף הדפים של המסמך
Page page = pdfDocument.Pages.Add();
// הקמת מופע של TextStamp עם טקסט לדוגמא
TextStamp stamp = new TextStamp("זהו חותמת טקסט עם מרווח תווים");
// ציון שם הגופן עבור אובייקט החותמת
stamp.TextState.Font = FontRepository.FindFont("Arial");
// ציון גודל הגופן עבור TextStamp
stamp.TextState.FontSize = 12;
// ציון מרווח התווים כ-1f
stamp.TextState.CharacterSpacing = 1f;
// הגדרת ה-XIndent עבור החותמת
stamp.XIndent = 100;
// הגדרת ה-YIndent עבור החותמת
stamp.YIndent = 500;
// הוספת חותמת טקסטית למופע הדף
stamp.Put(page);
dataDir = dataDir + "CharacterSpacingUsingTextStamp_out.pdf";
// שמירת מסמך PDF המתקבל.
pdfDocument.Save(dataDir);
```
## יצירת מסמך PDF רב-עמודות

במגזינים ועיתונים, אנו רואים לרוב שהחדשות מוצגות במספר עמודות על דף אחד במקום בספרים שבהם פסקאות הטקסט מודפסות בדרך כלל על פני כל העמוד מהצד השמאלי לצד הימני. רבות מיישומי עיבוד המסמכים כמו Microsoft Word ו-Adobe Acrobat Writer מאפשרים למשתמשים ליצור מספר עמודות על דף בודד ולאחר מכן להוסיף נתונים אליהן.

[Aspose.PDF for .NET](https://docs.aspose.com/pdf/net/) גם מציעה את התכונה ליצירת מספר עמודות בתוך דפי מסמכי PDF.
[Aspose.PDF for .NET](https://docs.aspose.com/pdf/net/) מציע גם את התכונה ליצור מספר עמודות בתוך עמודי מסמכי PDF.

ריווח עמודות משמעו המרחק בין העמודות והריווח המוגדר כברירת מחדל בין העמודות הוא 1.25 ס"מ. אם רוחב העמודה לא מצוין, אז [Aspose.PDF for .NET](https://docs.aspose.com/pdf/net/) מחשב את רוחב כל עמודה אוטומטית לפי גודל העמוד וריווח העמודות.

להלן דוגמה שמדגימה את יצירת שתי עמודות עם אובייקטים של גרפים (קו) והם מתווספים לאוסף הפסקאות של FloatingBox, שלאחר מכן מתווסף לאוסף הפסקאות של מופע העמוד.

```csharp
// לדוגמאות מלאות וקבצי נתונים, נא ללכת אל https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לספריית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

Document doc = new Document();
// ציין את מידע השולי השמאלי עבור קובץ ה-PDF
doc.PageInfo.Margin.Left = 40;
// ציין את מידע השולי הימני עבור קובץ ה-PDF
doc.PageInfo.Margin.Right = 40;
Page page = doc.Pages.Add();

Aspose.Pdf.Drawing.Graph graph1 = new Aspose.Pdf.Drawing.Graph(500, 2);
// הוסף את הקו לאוסף הפסקאות של אובייקט החלק
page.Paragraphs.Add(graph1);

// ציין את הקואורדינטות עבור הקו
float[] posArr = new float[] { 1, 2, 500, 2 };
Aspose.Pdf.Drawing.Line l1 = new Aspose.Pdf.Drawing.Line(posArr);
graph1.Shapes.Add(l1);
// צור משתני מחרוזות עם טקסט המכיל תגיות HTML

string s = "<font face=\"Times New Roman\" size=4>" +

"<strong> איך להימנע מהונאות כספיות</<strong> "
+ "</font>";
// צור פסקאות טקסט המכילות טקסט HTML

HtmlFragment heading_text = new HtmlFragment(s);
page.Paragraphs.Add(heading_text);

Aspose.Pdf.FloatingBox box = new Aspose.Pdf.FloatingBox();
// הוסף ארבע עמודות בחלק
box.ColumnInfo.ColumnCount = 2;
// הגדר את הריווח בין העמודות
box.ColumnInfo.ColumnSpacing = "5";

box.ColumnInfo.ColumnWidths = "105 105";
TextFragment text1 = new TextFragment("מאת גוגלר (הבלוג הרשמי של גוגל)");
text1.TextState.FontSize = 8;
text1.TextState.LineSpacing = 2;
box.Paragraphs.Add(text1);
text1.TextState.FontSize = 10;

text1.TextState.FontStyle = FontStyles.Italic;
// צור אובייקט גרפים לציור קו
Aspose.Pdf.Drawing.Graph graph2 = new Aspose.Pdf.Drawing.Graph(50, 10);
// ציין את הקואורדינטות עבור הקו
float[] posArr2 = new float[] { 1, 10, 100, 10 };
Aspose.Pdf.Drawing.Line l2 = new Aspose.Pdf.Drawing.Line(posArr2);
graph2.Shapes.Add(l2);

// הוסף את הקו לאוסף הפסקאות של אובייקט החלק
box.Paragraphs.Add(graph2);

TextFragment text2 = new TextFragment(@"Sed augue tortor, sodales id, luctus et, pulvinar ut, eros. Suspendisse vel dolor. Sed quam. Curabitur ut massa vitae eros euismod aliquam. Pellentesque sit amet elit. Vestibulum interdum pellentesque augue. Cras mollis arcu sit amet purus. Donec augue. Nam mollis tortor a elit. Nulla viverra nisl vel mauris. Vivamus sapien. nascetur ridiculus mus. Nam justo lorem, aliquam luctus, sodales et, semper sed, enim Nam justo lorem, aliquam luctus, sodales et, semper sed, enim Nam justo lorem, aliquam luctus, sodales et, semper sed, enim nAenean posuere ante ut neque. Morbi sollicitudin congue felis. Praesent turpis diam, iaculis sed, pharetra non, mollis ac, mauris. Phasellus nisi ipsum, pretium vitae, tempor sed, molestie eu, dui. Duis lacus purus, tristique ut, iaculis cursus, tincidunt vitae, risus. Sed commodo. *** sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Nam justo lorem, aliquam luctus, sodales et, semper sed, enim Nam justo lorem, aliquam luctus, sodales et, semper sed, enim Nam justo lorem, aliquam luctus, sodales et, semper sed, enim nAenean posuere ante ut neque. Morbi sollicitudin congue felis. Praesent turpis diam, iaculis sed, pharetra non, mollis ac, mauris. Phasellus nisi ipsum, pretium vitae, tempor sed, molestie eu, dui. Duis lacus purus, tristique ut, iaculis cursus, tincidunt vitae, risus. Sed commodo. *** sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Sed urna. . Duis convallis ultrices nisi. Maecenas non ligula. Nunc nibh est, tincidunt in, placerat sit amet, vestibulum a, nulla. Praesent porttitor turpis eleifend ante. Morbi sodales.nAenean posuere ante ut neque. Morbi sollicitudin congue felis. Praesent turpis diam, iaculis sed, pharetra non, mollis ac, mauris. Phasellus nisi ipsum, pretium vitae, tempor sed, molestie eu, dui. Duis lacus purus, tristique ut, iaculis cursus, tincidunt vitae, risus. Sed commodo. *** sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Sed urna. . Duis convallis ultrices nisi. Maecenas non ligula. Nunc nibh est, tincidunt in, placerat sit amet, vestibulum a, nulla. Praesent porttitor turpis eleifend ante. Morbi sodales.");
box.Paragraphs.Add(text2);

page.Paragraphs.Add(box);

dataDir = dataDir + "CreateMultiColumnPdf_out.pdf";
// שמור קובץ PDF
doc.Save(dataDir);
```
## עבודה עם נקודות עצירה מותאמות אישית

נקודת עצירה היא נקודת עצירה לטאבינג. בעיבוד תמלילים, כל שורה מכילה מספר נקודות עצירה הממוקמות במרווחים קבועים (לדוגמה, כל חצי אינץ'). ניתן לשנות את מיקומן, כאשר רוב תוכנות העיבוד מאפשרות לך להגדיר נקודות עצירה בכל מקום שתרצה. כאשר לוחצים על מקש הטאב, נקודת ההוספה או הסמן קופצים לנקודת העצירה הבאה, שהיא עצמה בלתי נראית. אף על פי שנקודות העצירה אינן קיימות בקובץ הטקסט, תוכנת העיבוד מתעדת אותן כדי שתוכל להגיב באופן נכון ללחיצה על מקש הטאב.

[Aspose.PDF for .NET](https://docs.aspose.com/pdf/net/) מאפשר למפתחים להשתמש בנקודות עצירה מותאמות אישית במסמכי PDF. המחלקה Aspose.Pdf.Text.TabStop משמשת להגדרת נקודות עצירה מותאמות אישית במחלקת [TextFragment](https://reference.aspose.com/pdf/net/aspose.pdf.text/textfragment).

[Aspose.PDF for .NET](https://docs.aspose.com/pdf/net/) גם מציע כמה סוגים מוגדרים מראש של סוגי ראשי טאב כאנומרציה בשם, TabLeaderType שערכיה המוגדרים מראש ותיאוריהם ניתנים למטה:
[Aspose.PDF for .NET](https://docs.aspose.com/pdf/net/) גם מציע כמה סוגי רמזורים מוגדרים מראש כספרות בשם, TabLeaderType שערכיהם המוגדרים מראש ותיאוריהם ניתנים להלן:

|**סוג רמזור**|**תיאור**|
| :- | :- |
|None|אין רמזור|
|Solid|רמזור מוצק|
|Dash|רמזור מקווקו|
|Dot|רמזור נקודה|

הנה דוגמה לכיצד להגדיר עצירות TAB מותאמות אישית.

```csharp
// לדוגמאות מלאות וקבצי נתונים, אנא עבור אל https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לספריית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

Document _pdfdocument = new Document();
Page page = _pdfdocument.Pages.Add();

Aspose.Pdf.Text.TabStops ts = new Aspose.Pdf.Text.TabStops();
Aspose.Pdf.Text.TabStop ts1 = ts.Add(100);
ts1.AlignmentType = TabAlignmentType.Right;
ts1.LeaderType = TabLeaderType.Solid;
Aspose.Pdf.Text.TabStop ts2 = ts.Add(200);
ts2.AlignmentType = TabAlignmentType.Center;
ts2.LeaderType = TabLeaderType.Dash;
Aspose.Pdf.Text.TabStop ts3 = ts.Add(300);
ts3.AlignmentType = TabAlignmentType.Left;
ts3.LeaderType = TabLeaderType.Dot;

TextFragment header = new TextFragment("זהו דוגמה ליצירת טבלה עם עצירות TAB", ts);
TextFragment text0 = new TextFragment("#$TABHead1 #$TABHead2 #$TABHead3", ts);

TextFragment text1 = new TextFragment("#$TABdata11 #$TABdata12 #$TABdata13", ts);
TextFragment text2 = new TextFragment("#$TABdata21 ", ts);
text2.Segments.Add(new TextSegment("#$TAB"));
text2.Segments.Add(new TextSegment("data22 "));
text2.Segments.Add(new TextSegment("#$TAB"));
text2.Segments.Add(new TextSegment("data23"));

page.Paragraphs.Add(header);
page.Paragraphs.Add(text0);
page.Paragraphs.Add(text1);
page.Paragraphs.Add(text2);

dataDir = dataDir + "CustomTabStops_out.pdf";
_pdfdocument.Save(dataDir);
```
## כיצד להוסיף טקסט שקוף בקובץ PDF

קובץ PDF מכיל תמונה, טקסט, גרף, קובץ מצורף, אובייקטים של הערות ובעת יצירת TextFragment, ניתן להגדיר מידע על צבע רקע וקדמי כמו גם עיצוב טקסט. Aspose.PDF עבור .NET תומך בתכונה להוספת טקסט עם ערוץ צבע אלפא. קטע הקוד הבא מראה כיצד להוסיף טקסט עם צבע שקוף.

```csharp
// לדוגמאות מלאות וקבצי נתונים, אנא עבור אל https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לספריית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// צור מופע של מסמך
Document doc = new Document();
// צור דף לאוסף הדפים של קובץ ה-PDF
Aspose.Pdf.Page page = doc.Pages.Add();

// צור אובייקט גרף
Aspose.Pdf.Drawing.Graph canvas = new Aspose.Pdf.Drawing.Graph(100, 400);
// צור מופע מלבן עם ממדים מסוימים
Aspose.Pdf.Drawing.Rectangle rect = new Aspose.Pdf.Drawing.Rectangle(100, 100, 400, 400);
// צור אובייקט צבע מערוץ צבע אלפא
rect.GraphInfo.FillColor = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.FromArgb(128, System.Drawing.Color.FromArgb(12957183)));
// הוסף מלבן לאוסף הצורות של אובייקט הגרף
canvas.Shapes.Add(rect);
// הוסף אובייקט הגרף לאוסף הפסקאות של אובייקט הדף
page.Paragraphs.Add(canvas);
// הגדר ערך כדי שלא לשנות מיקום עבור אובייקט הגרף
canvas.IsChangePosition = false;

// צור מופע של TextFragment עם ערך דוגמה
TextFragment text = new TextFragment("טקסט שקוף טקסט שקוף טקסט שקוף טקסט שקוף טקסט שקוף טקסט שקוף טקסט שקוף טקסט שקוף טקסט שקוף טקסט שקוף טקסט שקוף טקסט שקוף טקסט שקוף טקסט שקוף טקסט שקוף ");
// צור אובייקט צבע מערוץ אלפא
Aspose.Pdf.Color color = Aspose.Pdf.Color.FromArgb(30, 0, 255, 0);
// הגדר מידע צבע עבור מופע הטקסט
text.TextState.ForegroundColor = color;
// הוסף טקסט לאוסף הפסקאות של מופע הדף
page.Paragraphs.Add(text);

dataDir = dataDir + "AddTransparentText_out.pdf";
doc.Save(dataDir);
```
## ציון ריווח בין שורות עבור גופנים

לכל גופן יש ריבוע מופשט, שגובהו הוא המרחק המיועד בין שורות הטקסט באותו גודל גופן.
לכל גופן יש ריבוע מופשט, שגובהו הוא המרחק המיועד בין שורות של טקסט באותו גודל גופן.
## קבל את רוחב הטקסט באופן דינמי

לעיתים יש צורך לקבל את רוחב הטקסט באופן דינמי. Aspose.PDF עבור .NET כולל שתי שיטות למדידת רוחב מחרוזת. ניתן להפעיל את השיטה [MeasureString](https://reference.aspose.com/pdf/net/aspose.pdf.text/font/methods/measurestring) של מחלקות Aspose.Pdf.Text.Font או Aspose.Pdf.Text.TextState (או שתיהן). קטע הקוד להלן מראה כיצד להשתמש בפונקציונליות זו.

```csharp
// לדוגמאות מלאות וקבצי נתונים, אנא עבור ל https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לספריית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

Aspose.Pdf.Text.Font font = FontRepository.FindFont("Arial");
TextState ts = new TextState();
ts.Font = font;
ts.FontSize = 14;

if (Math.Abs(font.MeasureString("A", 14) - 9.337) > 0.001)
    Console.WriteLine("מדידת מחרוזת הגופן לא צפויה!");

if (Math.Abs(ts.MeasureString("z") - 7.0) > 0.001)
    Console.WriteLine("מדידת מחרוזת הגופן לא צפויה!");

for (char c = 'A'; c <= 'z'; c++)
{
    double fnMeasure = font.MeasureString(c.ToString(), 14);
    double tsMeasure = ts.MeasureString(c.ToString());

    if (Math.Abs(fnMeasure - tsMeasure) > 0.001)
        Console.WriteLine("מדידת מחרוזות הגופן והמצב לא תואמת!");
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
יישום דוגמא

# תיעוד ל-API

## פתיחה

ברוכים הבאים לתיעוד של ה-API שלנו. במסמך זה תמצאו הסברים על שימוש ב-API.

### מה זה API?

API (ממשק תכנות יישומים) הוא מערכת שמאפשרת לתוכנות שונות לתקשר זו עם זו.

## התקנה

השתמש בפקודה הבאה להתקנת ה-API:

```bash
npm install our-api
```

## שימוש בסיסי

כדי להשתמש ב-API, יש לייבא אותו תחילה לתוך הפרויקט שלכם:

```javascript
import { apiClient } from 'our-api';
```

לאחר מכן, ניתן לבצע קריאות ל-API כך:

```javascript
apiClient.getData().then(data => {
  console.log(data);
});
```

## פרמטרים

ה-API מקבל מספר פרמטרים, כולל:

- `userID`: מזהה של המשתמש
- `data`: המידע לשליחה

דוגמה לשימוש:

```javascript
apiClient.sendData({ userID: '12345', data: 'הנתונים שלך כאן' });
```

## תמיכה

אם נתקלת בבעיות, אנא צור קשר עם תמיכת הלקוחות שלנו בדוא"ל support@our-api.com.

## שאלות נפוצות

### איך אני מעדכן נתונים?

לעדכון נתונים, שלח בקשת PATCH ל-API עם הנתונים המעודכנים.

```javascript
apiClient.updateData({ userID: '12345', newData: 'הנתונים המעודכנים שלך כאן' });
```

### מה המשך התמיכה ב-API?

type: docs
changefreq: "monthly"

התמיכה ב-API נמשכת כל עוד יש מנוי פעיל.
