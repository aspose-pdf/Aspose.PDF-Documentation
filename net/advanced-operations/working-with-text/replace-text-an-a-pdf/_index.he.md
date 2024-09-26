---
title: החלפת טקסט ב-PDF
linktitle: החלפת טקסט ב-PDF
type: docs
weight: 40
url: /net/replace-text-in-pdf/
description: למד עוד על הדרכים השונות להחליף ולהסיר טקסט מתוך ספריית Aspose.PDF עבור .NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
aliases:
    - /net/replace-text-in-a-pdf-document/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "החלפת טקסט ב-PDF",
    "alternativeHeadline": "החלפה והסרת טקסט בקובץ PDF",
    "author": {
        "@type": "Person",
        "name":"אנסטסיה חולוב",
        "givenName": "אנסטסיה",
        "familyName": "חולוב",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "יצירת מסמך PDF",
    "keywords": "pdf, c#, החלפת טקסט, הסרת טקסט",
    "wordcount": "302",
    "proficiencyLevel": "מתחיל",
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
                "areaServed": "ארה\"ב",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "מכירות",
                "areaServed": "בריטניה",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "מכירות",
                "areaServed": "אוסטרליה",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/net/replace-text-in-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/replace-text-in-pdf/"
    },
    "dateModified": "2022-02-04",
    "description": "למד עוד על הדרכים השונות להחליף ולהסיר טקסט מתוך ספריית Aspose.PDF עבור .NET."
}
</script>
הקוד הבא עובד גם עם ספריית [Aspose.PDF.Drawing](/pdf/net/drawing/).

## החלפת טקסט בכל דפי מסמך PDF

{{% alert color="primary" %}}

ניתן לנסות למצוא ולהחליף את הטקסט במסמך באמצעות Aspose.PDF ולקבל את התוצאות באופן מקוון ב[קישור](https://products.aspose.app/pdf/redaction) הזה

{{% /alert %}}

כדי להחליף טקסט בכל הדפים של מסמך PDF, תחילה עליך להשתמש ב-TextFragmentAbsorber כדי למצוא את הביטוי המסוים שברצונך להחליף. לאחר מכן, עליך לעבור על כל ה-TextFragments כדי להחליף את הטקסט ולשנות כל תכונה אחרת. לאחר שעשית זאת, עליך רק לשמור את קובץ ה-PDF המוצא באמצעות המתודה Save של אובייקט המסמך. קטע הקוד הבא מראה לך כיצד להחליף טקסט בכל דפי מסמך PDF.

```csharp
// לדוגמאות מלאות וקבצי נתונים, נא ללכת ל https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לתיקיית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// פתיחת מסמך
Document pdfDocument = new Document(dataDir + "ReplaceTextAll.pdf");

// יצירת אובייקט TextAbsorber כדי למצוא את כל המופעים של ביטוי החיפוש הנכנס
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("text");

// קבלת ה-absorber לכל הדפים
pdfDocument.Pages.Accept(textFragmentAbsorber);

// קבלת קובצי טקסט שנאספו
TextFragmentCollection textFragmentCollection = textFragmentAbsorber.TextFragments;

// לולאה דרך הקטעים
foreach (TextFragment textFragment in textFragmentCollection)
{
    // עדכון טקסט ומאפיינים נוספים
    textFragment.Text = "TEXT";
    textFragment.TextState.Font = FontRepository.FindFont("Verdana");
    textFragment.TextState.FontSize = 22;
    textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.Blue);
    textFragment.TextState.BackgroundColor = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.Green);
}

dataDir = dataDir + "ReplaceTextAll_out.pdf";
// שמירת מסמך PDF התוצאתי.
pdfDocument.Save(dataDir);
```
## החלפת טקסט באזור מסוים של הדף

כדי להחליף טקסט באזור מסוים של הדף, ראשית עלינו ליצור מופע של אובייקט TextFragmentAbsorber, לציין את אזור הדף באמצעות התכונה TextSearchOptions.Rectangle ולאחר מכן לעבור על כל ה-TextFragments כדי להחליף את הטקסט. לאחר ביצוע הפעולות הללו, יש לשמור את ה-PDF המעודכן באמצעות שיטת ה-Save של אובייקט ה-Document. הדוגמה הבאה מראה איך להחליף טקסט בכל דפי מסמך PDF.

```csharp
// טעינת קובץ PDF
Aspose.PDF.Document pdf  = new Aspose.PDF.Document("c:/pdftest/programaticallyproducedpdf.pdf");

// יצירת מופע של אובייקט TextFragment Absorber
Aspose.PDF.Text.TextFragmentAbsorber TextFragmentAbsorberAddress = new Aspose.PDF.Text.TextFragmentAbsorber();

// חיפוש טקסט בתוך גבולות הדף
TextFragmentAbsorberAddress.TextSearchOptions.LimitToPageBounds = true;

// הגדרת אזור הדף לאפשרויות חיפוש טקסט
TextFragmentAbsorberAddress.TextSearchOptions.Rectangle = new Aspose.PDF.Rectangle(100, 100, 200, 200);

// חיפוש טקסט מהדף הראשון של קובץ ה-PDF
pdf.Pages[1].Accept(TextFragmentAbsorberAddress);

// עיבוד כל פרגמנט טקסט בנפרד
foreach( Aspose.PDF.Text.TextFragment tf in TextFragmentAbsorberAddress.TextFragments)
{
    // עדכון הטקסט לתווים ריקים
    tf.Text = "";
}

// שמירת קובץ ה-PDF לאחר החלפת הטקסט
pdf.Save("c:/pdftest/TextUpdated.pdf");
```
## החלפת טקסט בהתבסס על ביטוי רגולרי

אם אתה רוצה להחליף משפטים מסוימים בהתבסס על ביטוי רגולרי, תחילה עליך למצוא את כל המשפטים שתואמים את הביטוי הרגולרי באמצעות TextFragmentAbsorber. עליך להעביר את הביטוי הרגולרי כפרמטר לבנאי של TextFragmentAbsorber. עליך גם ליצור אובייקט TextSearchOptions שמציין האם משתמשים בביטוי רגולרי או לא. לאחר שתקבל את המשפטים התואמים ב-TextFragments, תצטרך לעבור על כולם ולעדכן כפי שנדרש. לבסוף, עליך לשמור את ה-PDF המעודכן באמצעות המתודה Save של אובייקט המסמך. קטע הקוד הבא מראה לך כיצד להחליף טקסט בהתבסס על ביטוי רגולרי.

```csharp
// לדוגמאות מלאות וקבצי נתונים, אנא עבור ל https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לספריית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// פתח מסמך
Document pdfDocument = new Document(dataDir + "SearchRegularExpressionPage.pdf");

// צור אובייקט TextAbsorber כדי למצוא את כל המשפטים שמתאימים לביטוי הרגולרי
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("\\d{4}-\\d{4}"); // כמו 1999-2000

// הגדר אופציית חיפוש טקסט כדי לציין שימוש בביטוי רגולרי
TextSearchOptions textSearchOptions = new TextSearchOptions(true);
textFragmentAbsorber.TextSearchOptions = textSearchOptions;

// קבל את ה-absorber לעמוד בודד
pdfDocument.Pages[1].Accept(textFragmentAbsorber);

// קבל את אוסף קטעי הטקסט שנלקחו
TextFragmentCollection textFragmentCollection = textFragmentAbsorber.TextFragments;

// עבור על הקטעים
foreach (TextFragment textFragment in textFragmentCollection)
{
    // עדכן טקסט ומאפיינים נוספים
    textFragment.Text = "ביטוי חדש";
    // הגדר למופע של אובייקט.
    textFragment.TextState.Font = FontRepository.FindFont("Verdana");
    textFragment.TextState.FontSize = 22;
    textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.Blue);
    textFragment.TextState.BackgroundColor = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.Green);
}
dataDir = dataDir + "ReplaceTextonRegularExpression_out.pdf";
pdfDocument.Save(dataDir);
```
## החלפת גופנים בקובץ PDF קיים

Aspose.PDF עבור .NET תומך ביכולת להחליף טקסט במסמך PDF. עם זאת, לפעמים יש דרישה להחליף רק את הגופן שמשמש במסמך PDF. לכן, במקום להחליף את הטקסט, מוחלף רק הגופן המשמש. אחת מהעומסים של בנאי המחלקה TextFragmentAbsorber מקבל אובייקט TextEditOptions כארגומנט ואנו יכולים להשתמש בערך RemoveUnusedFonts מתוך אנומרציה TextEditOptions.FontReplace כדי לעמוד בדרישות שלנו. קטע הקוד הבא מראה כיצד להחליף את הגופן במסמך PDF.

```csharp
// לדוגמאות מלאות וקבצי נתונים, אנא עבור ל https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לספריית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// טען קובץ PDF מקורי
Document pdfDocument = new Document(dataDir + "ReplaceTextPage.pdf");
// חפש קטעי טקסט והגדר אפשרות עריכה כהסרת גופנים שאינם בשימוש
TextFragmentAbsorber absorber = new TextFragmentAbsorber(new TextEditOptions(TextEditOptions.FontReplace.RemoveUnusedFonts));

// קבל את ה-absorber לכל הדפים
pdfDocument.Pages.Accept(absorber);
// עבור על כל קטעי הטקסט
foreach (TextFragment textFragment in absorber.TextFragments)
{
    // אם שם הגופן הוא ArialMT, החלף את שם הגופן ל-Arial
    if (textFragment.TextState.Font.FontName == "Arial,Bold")
    {
        textFragment.TextState.Font = FontRepository.FindFont("Arial");
    }

}

dataDir = dataDir + "ReplaceFonts_out.pdf";
// שמור את המסמך המעודכן
pdfDocument.Save(dataDir);
```
## החלפת טקסט צריכה לסדר מחדש את תוכן העמוד אוטומטית

Aspose.PDF עבור .NET תומך בתכונה לחיפוש והחלפת טקסט בתוך קובץ PDF. עם זאת, לאחרונה חלק מהלקוחות נתקלו בבעיות במהלך החלפת טקסט כאשר קטע טקסט מסוים מוחלף בתוכן קטן יותר ומוצגים רווחים נוספים ב-PDF המתקבל או במקרה שקטע הטקסט מוחלף במחרוזת ארוכה יותר, אז המילים חופפות תוכן קיים בעמוד. לכן, הדרישה הייתה להכניס מנגנון שברגע שהטקסט במסמך PDF מוחלף, התוכן יסודר מחדש.

כדי לענות על התרחישים שתוארו לעיל, Aspose.PDF עבור .NET שופר כך שבעיות אלו לא יופיעו בעת החלפת טקסט בקובץ PDF. קטע הקוד הבא מראה כיצד להחליף טקסט בקובץ PDF והתוכן של העמוד צריך להסדר מחדש אוטומטית.

```csharp
// לדוגמאות מלאות וקבצי נתונים, נא לעבור ל https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לתיקיית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// טעינת קובץ PDF מקורי
Document doc = new Document(dataDir + "ExtractTextPage.pdf");
// יצירת אובייקט TextFragment Absorber עם ביטוי רגולרי
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("[TextFragmentAbsorber,companyname,Textbox,50]");
doc.Pages.Accept(textFragmentAbsorber);
// החלפת כל קטע טקסט
foreach (TextFragment textFragment in textFragmentAbsorber.TextFragments)
{
    // הגדרת גופן של קטע הטקסט שמוחלף
    textFragment.TextState.Font = FontRepository.FindFont("Arial");
    // הגדרת גודל גופן
    textFragment.TextState.FontSize = 12;
    textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.Navy;
    // החלפת הטקסט במחרוזת ארוכה יותר ממקום השמירה
    textFragment.Text = "This is a Larger String for the Testing of this issue";
}
dataDir = dataDir + "RearrangeContentsUsingTextReplacement_out.pdf";
// שמירת ה-PDF המתקבל
doc.Save(dataDir);
```
## עיבוד סמלים ניתנים להחלפה בעת יצירת PDF

סמלים ניתנים להחלפה הם סמלים מיוחדים במחרוזת טקסט שניתן להחליפם בתוכן מתאים בזמן ריצה. סמלים ניתנים להחלפה שנתמכים כעת על ידי מודל אובייקט המסמכים החדש של מרחב השמות Aspose.PDF הם `$P`, `$p`, `\n`, `\r`. ה`$p` וה`$P` משמשים לטיפול במספור דפים בזמן ריצה. `$p` מוחלף במספר הדף שבו נמצאת המחלקה Paragraph הנוכחית. `$P` מוחלף במספר הכולל של דפים במסמך. בעת הוספת `TextFragment` לאוסף הפסקאות של מסמכי PDF, לא נתמך הזנת שורה חדשה בתוך הטקסט. עם זאת, כדי להוסיף טקסט עם הזנת שורה חדשה, יש להשתמש ב`TextFragment` עם `TextParagraph`:

- השתמש ב"\r\n" או Environment.NewLine בTextFragment במקום ב"\n" בודד;
- צור אובייקט TextParagraph. הוא יוסיף טקסט עם פיצול שורות;
- הוסף את הTextFragment עם TextParagraph.AppendLine;
- הוסף את הTextParagraph עם TextBuilder.AppendParagraph.

```csharp
// לדוגמאות מלאות וקבצי נתונים, אנא עבור ל https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לספריית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

Aspose.Pdf.Document pdfApplicationDoc = new Aspose.Pdf.Document();
Aspose.Pdf.Page applicationFirstPage = (Aspose.Pdf.Page)pdfApplicationDoc.Pages.Add();

// אתחול TextFragment חדש עם טקסט המכיל את סימני השורה החדשה הנדרשים
Aspose.Pdf.Text.TextFragment textFragment = new Aspose.Pdf.Text.TextFragment("Applicant Name: " + Environment.NewLine + " Joe Smoe");

// הגדרת תכונות הTextFragment במידת הצורך
textFragment.TextState.FontSize = 12;
textFragment.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("TimesNewRoman");
textFragment.TextState.BackgroundColor = Aspose.Pdf.Color.LightGray;
textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.Red;

// יצירת אובייקט TextParagraph
TextParagraph par = new TextParagraph();

// הוספת TextFragment חדש לפסקה
par.AppendLine(textFragment);

// הגדרת מיקום הפסקה
par.Position = new Aspose.Pdf.Text.Position(100, 600);

// יצירת אובייקט TextBuilder
TextBuilder textBuilder = new TextBuilder(applicationFirstPage);
// הוספת הTextParagraph באמצעות TextBuilder
textBuilder.AppendParagraph(par);

dataDir = dataDir + "RenderingReplaceableSymbols_out.pdf";
pdfApplicationDoc.Save(dataDir);
```
## סמלים ניתנים להחלפה באזור כותרת עליונה/תחתונה

ניתן להציב סמלים ניתנים להחלפה גם בתוך אזור הכותרת העליונה/התחתונה של קובץ PDF. אנא עיין בדוגמת הקוד הבאה לפרטים על כיצד להוסיף סמל ניתן להחלפה בחלק התחתון.

```csharp
// לדוגמאות מלאות וקבצי נתונים, אנא בקר ב https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לתיקיית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

Document doc = new Document();
Page page = doc.Pages.Add();

MarginInfo marginInfo = new MarginInfo();
marginInfo.Top = 90;
marginInfo.Bottom = 50;
marginInfo.Left = 50;
marginInfo.Right = 50;
// הקצאת מופע marginInfo לתכונת Margin של sec1.PageInfo
page.PageInfo.Margin = marginInfo;

HeaderFooter hfFirst = new HeaderFooter();
page.Header = hfFirst;
hfFirst.Margin.Left = 50;
hfFirst.Margin.Right = 50;

// יצירת פסקת טקסט שתאחסן את התוכן להצגה ככותרת עליונה
TextFragment t1 = new TextFragment("כותרת הדוח");
t1.TextState.Font = FontRepository.FindFont("Arial");
t1.TextState.FontSize = 16;
t1.TextState.ForegroundColor = Aspose.Pdf.Color.Black;
t1.TextState.FontStyle = FontStyles.Bold;
t1.TextState.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Center;
t1.TextState.LineSpacing = 5f;
hfFirst.Paragraphs.Add(t1);

TextFragment t2 = new TextFragment("שם_הדוח");
t2.TextState.Font = FontRepository.FindFont("Arial");
t2.TextState.ForegroundColor = Aspose.Pdf.Color.Black;
t2.TextState.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Center;
t2.TextState.LineSpacing = 5f;
t2.TextState.FontSize = 12;
hfFirst.Paragraphs.Add(t2);

// יצירת אובייקט HeaderFooter לסעיף
HeaderFooter hfFoot = new HeaderFooter();
// הגדרת אובייקט HeaderFooter לכותרת תחתונה לעמודים אי-זוגיים וזוגיים
page.Footer = hfFoot;
hfFoot.Margin.Left = 50;
hfFoot.Margin.Right = 50;

// הוספת פסקת טקסט המכילה את מספר העמוד הנוכחי מתוך מספר העמודים הכולל
TextFragment t3 = new TextFragment("נוצר בתאריך הבדיקה");
TextFragment t4 = new TextFragment("שם הדוח ");
TextFragment t5 = new TextFragment("עמוד $p מתוך $P");

// יצירת אובייקט שולחן
Table tab2 = new Table();

// הוספת השולחן לאוסף הפסקאות של החלק הרצוי
hfFoot.Paragraphs.Add(tab2);

// הגדרת רוחב העמודות בשולחן
tab2.ColumnWidths = "165 172 165";

// יצירת שורות בשולחן ולאחר מכן תאים בשורות
Row row3 = tab2.Rows.Add();

row3.Cells.Add();
row3.Cells.Add();
row3.Cells.Add();

// הגדרת היישור האנכי של הטקסט כממורכז
row3.Cells[0].Alignment = Aspose.Pdf.HorizontalAlignment.Left;
row3.Cells[1].Alignment = Aspose.Pdf.HorizontalAlignment.Center;
row3.Cells[2].Alignment = Aspose.Pdf.HorizontalAlignment.Right;

row3.Cells[0].Paragraphs.Add(t3);
row3.Cells[1].Paragraphs.Add(t4);
row3.Cells[2].Paragraphs.Add(t5);

Table table = new Table();

table.ColumnWidths = "33% 33% 34%";
table.DefaultCellPadding = new MarginInfo();
table.DefaultCellPadding.Top = 10;
table.DefaultCellPadding.Bottom = 10;

// הוספת השולחן לאוסף הפסקאות של החלק הרצוי
page.Paragraphs.Add(table);

// הגדרת גבול ברירת מחדל לתא באמצעות אובייקט BorderInfo
table.DefaultCellBorder = new BorderInfo(BorderSide.All, 0.1f);

// הגדרת גבול לשולחן באמצעות אובייקט BorderInfo מותאם אישית
table.Border = new BorderInfo(BorderSide.All, 1f);

table.RepeatingRowsCount = 1;

// יצירת שורות בשולחן ולאחר מכן תאים בשורות
Row row1 = table.Rows.Add();

row1.Cells.Add("col1");
row1.Cells.Add("col2");
row1.Cells.Add("col3");
const string CRLF = "\r\n";
for (int i = 0; i <= 10; i++)
{
    Row row = table.Rows.Add();
    row.IsRowBroken = true;
    for (int c = 0; c <= 2; c++)
    {
        Cell c1;
        if (c == 2)
            c1 = row.Cells.Add("Aspose.Total for Java היא אוסף של כל רכיב ה-Java המוצע על ידי Aspose. היא מורכבת באופן" + CRLF + "יומיומי כדי להבטיח שהיא מכילה את הגרסאות העדכניות ביותר של כל אחד מרכיבי ה-Java שלנו. " + CRLF + "יומיומי כדי להבטיח שהיא מכילה את הגרסאות העדכניות ביותר של כל אחד מרכיבי ה-Java שלנו. " + CRLF + "מאפשרת למפתחים ליצור מגוון רחב של יישומים.");
        else
            c1 = row.Cells.Add("item1" + c);
        c1.Margin = new MarginInfo();
        c1.Margin.Left = 30;
        c1.Margin.Top = 10;
        c1.Margin.Bottom = 10;
    }
}

dataDir = dataDir + "ReplaceableSymbolsInHeaderFooter_out.pdf";
doc.Save(dataDir);
```
## הסרת גופנים שלא בשימוש מקובץ PDF

Aspose.PDF for .NET תומכת בתכונה לשבץ גופנים בעת יצירת מסמך PDF, כמו גם ביכולת לשבץ גופנים בקבצי PDF קיימים. החל מגרסה 7.3.0 של Aspose.PDF for .NET, היא גם מאפשרת להסיר גופנים כפולים או שאינם בשימוש ממסמכי PDF.

להחלפת גופנים, השתמש בגישה הבאה:

1. קרא למחלקה [TextFragmentAbsorber](https://reference.aspose.com/pdf/net/aspose.pdf.text/textfragmentabsorber).
1. קרא לפרמטר TextFragmentAbsorber class’ TextEditOptions.FontReplace.RemoveUnusedFonts. (זה מסיר גופנים שהפכו ללא שימושיים במהלך החלפת גופן).
1. הגדר גופן באופן יחיד לכל קטע טקסט.

הקטע קוד הבא מחליף גופן לכל קטעי הטקסט של כל דפי המסמך ומסיר גופנים שאינם בשימוש.

```csharp
// לדוגמאות מלאות וקבצי נתונים, אנא עבור ל https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לתיקיית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// טען קובץ PDF מקורי
Document doc = new Document(dataDir + "ReplaceTextPage.pdf");
TextFragmentAbsorber absorber = new TextFragmentAbsorber(new TextEditOptions(TextEditOptions.FontReplace.RemoveUnusedFonts));
doc.Pages.Accept(absorber);

// עבור על כל קטעי הטקסט
foreach (TextFragment textFragment in absorber.TextFragments)
{
    textFragment.TextState.Font = FontRepository.FindFont("Arial, Bold");
}

dataDir = dataDir + "RemoveUnusedFonts_out.pdf";
// שמור את המסמך המעודכן
doc.Save(dataDir);
```
## הסר את כל הטקסט ממסמך PDF

### הסר את כל הטקסט באמצעות אופרטורים

בפעולה מסוימת של טקסט, אתה צריך להסיר את כל הטקסט ממסמך PDF ולשם כך אתה צריך להגדיר טקסט שנמצא כערך ריק בדרך כלל. הנקודה היא ששינוי הטקסט למספר רב של קטעי טקסט גורם למספר בדיקות ופעולות התאמת מיקום הטקסט. הן חיוניות בתרחישי עריכת טקסט. הקושי הוא שאתה לא יכול לקבוע כמה קטעי טקסט יוסרו בתרחיש שבו הם מעובדים בלולאה.

לכן, אנו ממליצים להשתמש בגישה אחרת לתרחיש של הסרת כל הטקסט מדפי PDF. אנא שקול את קטע הקוד הבא שעובד מאוד מהר.

```csharp
// לדוגמאות מלאות וקבצי נתונים, אנא עבור ל https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לספריית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// פתח מסמך
Document pdfDocument = new Document(dataDir + "RemoveAllText.pdf");
// עבור על כל הדפים של מסמך PDF
for (int i = 1; i <= pdfDocument.Pages.Count; i++)
{
    Page page = pdfDocument.Pages[i];
    OperatorSelector operatorSelector = new OperatorSelector(new Aspose.Pdf.Operators.TextShowOperator());
    // בחר את כל הטקסט בדף
    page.Contents.Accept(operatorSelector);
    // מחק את כל הטקסט
    page.Contents.Delete(operatorSelector.Selected);
}
// שמור את המסמך
pdfDocument.Save(dataDir + "RemoveAllText_out.pdf", Aspose.Pdf.SaveFormat.Pdf);
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

