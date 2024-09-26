---
title: יצירה או הוספת טבלה ב-PDF באמצעות C#
linktitle: יצירה או הוספת טבלה
type: docs
weight: 10
url: /net/add-table-in-existing-pdf-document/
description: Aspose.PDF עבור .NET היא ספרייה המשמשת ליצירה, קריאה ועריכת טבלאות PDF. בדוק פונקציות מתקדמות נוספות בנושא זה.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
aliases:
    - /net/add-and-extract-a-table/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "יצירה או הוספת טבלה ב-PDF באמצעות C#",
    "alternativeHeadline": "כיצד להוסיף טבלה ב-PDF עם .NET",
    "author": {
        "@type": "Person",
        "name":"אנסטסיה הולוב",
        "givenName": "אנסטסיה",
        "familyName": "הולוב",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "יצירת מסמכי PDF",
    "keywords": "pdf, c#, יצירת טבלה ב-pdf, הוספת טבלה",
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
    "url": "/net/add-table-in-existing-pdf-document/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-table-in-existing-pdf-document/"
    },
    "dateModified": "2022-02-04",
    "description": "Aspose.PDF עבור .NET היא ספרייה המשמשת ליצירה, קריאה ועריכת טבלאות PDF. בדוק פונקציות מתקדמות נוספות בנושא זה."
}
</script>
## יצירת טבלה באמצעות C\#

טבלאות חשובות בעבודה עם מסמכי PDF. הן מספקות תכונות נהדרות להצגת מידע בצורה מסודרת. מרחב השמות Aspose.PDF מכיל מחלקות בשם [Table](https://reference.aspose.com/pdf/net/aspose.pdf/table), [Cell](https://reference.aspose.com/pdf/net/aspose.pdf/cell), ו-[Row](https://reference.aspose.com/pdf/net/aspose.pdf/row) אשר מספקות פונקציונליות ליצירת טבלאות בעת יצירת מסמכי PDF מאפס.

הקטע הקוד הבא עובד גם עם ספריית [Aspose.PDF.Drawing](/pdf/net/drawing/).

ניתן ליצור טבלה על ידי יצירת אובייקט של מחלקת Table.

```csharp
Aspose.Pdf.Table table = new Aspose.Pdf.Table();
```

### הוספת טבלה למסמך PDF קיים

כדי להוסיף טבלה לקובץ PDF קיים באמצעות Aspose.PDF ל-.NET, עקוב אחר השלבים הבאים:

1. טען את קובץ המקור.
1. אתחל טבלה והגדר את העמודות והשורות שלה.
1. הגדר הגדרות טבלה (הגדרנו את הגבולות).
1. מלא את הטבלה.
1. הוסף את הטבלה לדף.
1.
1.

הדוגמאות הבאות מראות איך להוסיף טקסט בקובץ PDF קיים.

```csharp
// לדוגמאות מלאות וקבצי נתונים, אנא עבורו ל https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לספריית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

// טעינת מסמך PDF מקורי
Aspose.Pdf.Document doc = new Aspose.Pdf.Document(dataDir+ "AddTable.pdf");
// אתחול מופע חדש של הטבלה
Aspose.Pdf.Table table = new Aspose.Pdf.Table();
// הגדרת צבע הגבול של הטבלה כאפור בהיר
table.Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, .5f, Aspose.Pdf.Color.FromRgb(System.Drawing.Color.LightGray));
// הגדרת הגבול לתאי הטבלה
table.DefaultCellBorder = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, .5f, Aspose.Pdf.Color.FromRgb(System.Drawing.Color.LightGray));
// יצירת לולאה להוספת 10 שורות
for (int row_count = 1; row_count < 10; row_count++)
{
    // הוספת שורה לטבלה
    Aspose.Pdf.Row row = table.Rows.Add();
    // הוספת תאים לטבלה
    row.Cells.Add("עמודה (" + row_count + ", 1)");
    row.Cells.Add("עמודה (" + row_count + ", 2)");
    row.Cells.Add("עמודה (" + row_count + ", 3)");
}
// הוספת אובייקט הטבלה לעמוד הראשון של המסמך הקלט
doc.Pages[1].Paragraphs.Add(table);
dataDir = dataDir + "document_with_table_out.pdf";
// שמירת המסמך המעודכן המכיל את אובייקט הטבלה
doc.Save(dataDir);
```
### ColSpan ו-RowSpan בטבלאות

Aspose.PDF עבור .NET מספק את התכונה [ColSpan](https://reference.aspose.com/pdf/net/aspose.pdf/cell/properties/colspan) כדי למזג עמודות בטבלה ואת התכונה [RowSpan](https://reference.aspose.com/pdf/net/aspose.pdf/cell/properties/rowspan) כדי למזג שורות.

אנו משתמשים בתכונה `ColSpan` או `RowSpan` על אובייקט ה-`Cell` שיוצר את תא הטבלה. לאחר החלת התכונות הנדרשות ניתן להוסיף את התא שנוצר לטבלה.

```csharp
public static void AddTable_RowColSpan()
{
    // טען מסמך PDF מקורי
    Aspose.Pdf.Document pdfDocument = new Aspose.Pdf.Document();
    pdfDocument.Pages.Add();

    // מאתחל מופע חדש של טבלה
    Aspose.Pdf.Table table = new Aspose.Pdf.Table
    {
        // הגדר את צבע הגבול של הטבלה כאפור בהיר
        Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, .5f, Color.Black),
        // הגדר את הגבול לתאי הטבלה
        DefaultCellBorder = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, .5f, Color.Black)
    };

    // הוסף שורה ראשונה לטבלה
    Aspose.Pdf.Row row1 = table.Rows.Add();
    for (int cellCount = 1; cellCount <5; cellCount++)
    {
        // הוסף תאים לטבלה
        row1.Cells.Add($"Test 1 {cellCount}");
    }

    // הוסף שורה שנייה לטבלה
    Aspose.Pdf.Row row2 = table.Rows.Add();
    row2.Cells.Add($"Test 2 1");
    var cell = row2.Cells.Add($"Test 2 2");
    cell.ColSpan = 2;
    row2.Cells.Add($"Test 2 4");

    // הוסף שורה שלישית לטבלה
    Aspose.Pdf.Row row3 = table.Rows.Add();
    row3.Cells.Add("Test 3 1");
    row3.Cells.Add("Test 3 2");
    row3.Cells.Add("Test 3 3");
    row3.Cells.Add("Test 3 4");

    // הוסף שורה רביעית לטבלה
    Aspose.Pdf.Row row4 = table.Rows.Add();
    row4.Cells.Add("Test 4 1");
    cell = row4.Cells.Add("Test 4 2");
    cell.RowSpan = 2;
    row4.Cells.Add("Test 4 3");
    row4.Cells.Add("Test 4 4");

    // הוסף שורה חמישית לטבלה
    row4 = table.Rows.Add();
    row4.Cells.Add("Test 5 1");
    row4.Cells.Add("Test 5 3");
    row4.Cells.Add("Test 5 4");

    // הוסף את אובייקט הטבלה לעמוד הראשון של המסמך הכניסה
    pdfDocument.Pages[1].Paragraphs.Add(table);

    // שמור את המסמך המעודכן המכיל את אובייקט הטבלה
    doc.Save(Path.Combine(_dataDir, "document_with_table_out.pdf"));
}
```
תוצאת הרצת הקוד להלן היא הטבלה המוצגת בתמונה הבאה:

![ColSpan and RowSpan demo](colspan_rowspan.png)

## עבודה עם גבולות, שוליים וריפוד

יש לשים לב כי יש תמיכה גם בתכונה להגדרת סגנון גבול, שוליים וריפוד תאים לטבלאות. לפני כניסה לפרטים טכניים נוספים, חשוב להבין את המושגים של גבול, שוליים וריפוד שמוצגים להלן בדיאגרמה:

![Borders, margins and padding](set-border-style-margins-and-padding-of-table_1.png)

בתרשים לעיל, ניתן לראות כי גבולות הטבלה, השורה והתא נפגשים. באמצעות Aspose.PDF, ניתן להגדיר שוליים לטבלה וריפוד לתאים. על מנת להגדיר שוליים לתא, עלינו להגדיר ריפוד לתא.

### גבולות

להגדרת גבולות של אובייקטים של טבלה, [שורה](https://reference.aspose.com/pdf/net/aspose.pdf/row) ו[תא](https://reference.aspose.com/pdf/net/aspose.pdf/cell), יש להשתמש במאפיינים Table.Border, Row.Border ו-Cell.Border.
כדי להגדיר את גבולות הטבלה, [שורה](https://reference.aspose.com/pdf/net/aspose.pdf/row) ו[תא](https://reference.aspose.com/pdf/net/aspose.pdf/cell), השתמש בתכונות Table.Border, Row.Border ו-Cell.Border.

### שוליים או ריווח פנימי

ניתן לנהל ריווח פנימי של תאים באמצעות תכונת [DefaultCellPadding](https://reference.aspose.com/pdf/net/aspose.pdf/table/properties/defaultcellpadding) של מחלקת הטבלה. כל תכונות הריווח הקשורות מוקצות למופע של מחלקת [MarginInfo](https://reference.aspose.com/pdf/net/aspose.pdf/margininfo) שמקבלת מידע על הפרמטרים `שמאל`, `ימין`, `למעלה` ו`למטה` כדי ליצור שוליים מותאמים אישית.

בדוגמה הבאה, רוחב גבול התא נקבע ל-0.1 נקודה, רוחב גבול הטבלה נקבע לנקודה 1 וריווח התא נקבע ל-5 נקודות.

![שוליים וגבול בטבלת PDF](margin-border.png)

```csharp
// לדוגמאות מלאות וקבצי נתונים, נא לעבור ל https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לספריית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

// צור מופע של אובייקט המסמך על ידי קריאה לבנאי הריק שלו
Document doc = new Document();
Page page = doc.Pages.Add();
// צור מופע של אובייקט טבלה
Aspose.Pdf.Table tab1 = new Aspose.Pdf.Table();
// הוסף את הטבלה לאוסף הפסקאות של הקטע הרצוי
page.Paragraphs.Add(tab1);
// הגדר את רוחבי העמודות של הטבלה
tab1.ColumnWidths = "50 50 50";
// הגדר גבול ברירת מחדל לתא באמצעות אובייקט BorderInfo
tab1.DefaultCellBorder = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, 0.1F);
// הגדר גבול לטבלה באמצעות אובייקט BorderInfo מותאם אישית
tab1.Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, 1F);
// צור אובייקט MarginInfo והגדר את השוליים השמאלי, התחתון, הימני והעליון שלו
Aspose.Pdf.MarginInfo margin = new Aspose.Pdf.MarginInfo();
margin.Top = 5f;
margin.Left = 5f;
margin.Right = 5f;
margin.Bottom = 5f;
// הגדר את ריווח התא המוגדר כברירת מחדל לאובייקט MarginInfo
tab1.DefaultCellPadding = margin;
// צור שורות בטבלה ולאחר מכן תאים בשורות
Aspose.Pdf.Row row1 = tab1.Rows.Add();
row1.Cells.Add("col1");
row1.Cells.Add("col2");
row1.Cells.Add();
TextFragment mytext = new TextFragment("col3 with large text string");
// row1.Cells.Add("col3 with large text string to be placed inside cell");
row1.Cells[2].Paragraphs.Add(mytext);
row1.Cells[2].IsWordWrapped = false;
// row1.Cells[2].Paragraphs[0].FixedWidth= 80;
Aspose.Pdf.Row row2 = tab1.Rows.Add();
row2.Cells.Add("item1");
row2.Cells.Add("item2");
row2.Cells.Add("item3");
dataDir = dataDir + "MarginsOrPadding_out.pdf";
// שמור את ה-PDF
doc.Save(dataDir);
```
כדי ליצור טבלה עם פינות מעוגלות, השתמש בערך `RoundedBorderRadius` של המחלקה BorderInfo והגדר את סגנון פינות הטבלה למעוגל.

```csharp
// לדוגמאות מלאות וקבצי נתונים, אנא עבור ל https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לספריית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_Tables();
Aspose.Pdf.Table tab1 = new Aspose.Pdf.Table();

GraphInfo graph = new GraphInfo();
graph.Color = Aspose.Pdf.Color.Red;
// יצירת אובייקט BorderInfo ריק
BorderInfo bInfo = new BorderInfo(BorderSide.All, graph);
// הגדרת הגבול לגבול מעוגל שרדיוס העיגול הוא 15
bInfo.RoundedBorderRadius = 15;
// הגדרת סגנון פינות השולחן כמעוגל.
tab1.CornerStyle = Aspose.Pdf.BorderCornerStyle.Round;
// הגדרת מידע גבול של השולחן
tab1.Border = bInfo;
```

## החלת הגדרות AutoFit שונות על טבלה

כאשר יוצרים טבלה באמצעות סוכן חזותי כמו Microsoft Word, תמצא לעיתים קרובות את עצמך משתמש באחת מאפשרויות ה-AutoFit כדי להתאים את גודל הטבלה לרוחב הרצוי.
כאשר יוצרים טבלה באמצעות סוכן חזותי כמו Microsoft Word, תמצאו את עצמכם לעיתים קרובות משתמשים באחת מאפשרויות ה-AutoFit כדי להתאים את גודל הטבלה לרוחב הרצוי.

כברירת מחדל Aspose.Pdf מוסיפה טבלה חדשה באמצעות `ColumnAdjustment` עם ערך `Customized`. הטבלה תתאים את גודלה לרוחב הזמין בדף. כדי לשנות את התנהגות הגודל בטבלה כזו או בטבלה קיימת ניתן לקרוא לשיטת Table.autoFit(int). שיטה זו מקבלת אנומרציה של AutoFitBehavior שמגדירה איזה סוג של התאמה אוטומטית מוחלת על הטבלה.

כמו ב-Microsoft Word, שיטת autofit היא למעשה קיצור דרך שמחיל תכונות שונות על הטבלה בבת אחת. תכונות אלו הן למעשה אלו שנותנות לטבלה את ההתנהגות הנצפית. נדון בתכונות אלו לכל אופציית autofit. נשתמש בטבלה הבאה ונחיל הגדרות autofit שונות כהדגמה:

```csharp
// לדוגמאות מלאות וקבצי נתונים, אנא עברו ל https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לתיקיית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

// יצירת אובייקט Pdf על ידי קריאה לבנאי הריק שלו
Document doc = new Document();
// יצירת הפרק באובייקט Pdf
Page sec1 = doc.Pages.Add();

// יצירת אובייקט טבלה
Aspose.Pdf.Table tab1 = new Aspose.Pdf.Table();
// הוספת הטבלה לאוסף הפסקאות של הפרק הרצוי
sec1.Paragraphs.Add(tab1);

// הגדרת רוחבי העמודות של הטבלה
tab1.ColumnWidths = "50 50 50";
tab1.ColumnAdjustment = ColumnAdjustment.AutoFitToWindow;

// הגדרת גבול ברירת המחדל של התא באמצעות אובייקט BorderInfo
tab1.DefaultCellBorder = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, 0.1F);

// הגדרת גבול הטבלה באמצעות אובייקט BorderInfo מותאם אישית
tab1.Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, 1F);
// יצירת אובייקט MarginInfo והגדרת שוליו השמאלי, התחתון, הימני והעליון
Aspose.Pdf.MarginInfo margin = new Aspose.Pdf.MarginInfo();
margin.Top = 5f;
margin.Left = 5f;
margin.Right = 5f;
margin.Bottom = 5f;

// הגדרת הריפוד ברירת המחדל של התא לאובייקט MarginInfo
tab1.DefaultCellPadding = margin;

// יצירת שורות בטבלה ולאחר מכן תאים בשורות
Aspose.Pdf.Row row1 = tab1.Rows.Add();
row1.Cells.Add("col1");
row1.Cells.Add("col2");
row1.Cells.Add("col3");
Aspose.Pdf.Row row2 = tab1.Rows.Add();
row2.Cells.Add("item1");
row2.Cells.Add("item2");
row2.Cells.Add("item3");

dataDir = dataDir + "AutoFitToWindow_out.pdf";
// שמירת המסמך המעודכן המכיל אובייקט טבלה
doc.Save(dataDir);
```
### קבלת רוחב הטבלה

לעיתים נדרש לקבל את רוחב הטבלה באופן דינמי. למחלקה Aspose.PDF.Table יש שיטה [GetWidth](https://reference.aspose.com/pdf/net/aspose.pdf/table/methods/getwidth) למטרה זו. לדוגמה, אם לא הגדרת את רוחבי עמודות הטבלה במפורש והגדרת [ColumnAdjustment](https://reference.aspose.com/pdf/net/aspose.pdf/table/properties/columnadjustment) לAutoFitToContent. במקרה זה תוכל לקבל את רוחב הטבלה כך.

```csharp
// לדוגמאות מלאות וקבצי נתונים, אנא בקר ב https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// יצירת מסמך חדש
Document doc = new Document();
// הוספת דף למסמך
Page page = doc.Pages.Add();
// אתחול טבלה חדשה
Table table = new Table
{
    ColumnAdjustment = ColumnAdjustment.AutoFitToContent
};
// הוספת שורה לטבלה
Row row = table.Rows.Add();
// הוספת תא לטבלה
Cell cell = row.Cells.Add("טקסט תא 1");
cell = row.Cells.Add("טקסט תא 2");
// קבלת רוחב הטבלה
Console.WriteLine(table.GetWidth());
```

## הוספת תמונת SVG לתא בטבלה
## הוספת תמונת SVG לתא בטבלה

Aspose.PDF עבור .NET תומך בתכונה להוספת תא לטבלה בקובץ PDF. בעת יצירת טבלה, ניתן להוסיף טקסט או תמונות לתאים. יתר על כן, ה-API גם מציע את התכונה להמיר קבצי SVG לפורמט PDF. באמצעות שילוב של תכונות אלו, ניתן לטעון תמונת SVG ולהוסיפה לתא בטבלה.

הקטע קוד הבא מראה את השלבים ליצירת מופע של טבלה והוספת תמונת SVG לתוך תא בטבלה.

```csharp
// לדוגמאות מלאות וקבצי נתונים, אנא בקרו ב https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לספריית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

// יצירת אובייקט מסמך
Document doc = new Document();
// יצירת מופע של תמונה
Aspose.Pdf.Image img = new Aspose.Pdf.Image();
// הגדרת סוג התמונה כ-SVG
img.FileType = Aspose.Pdf.ImageFileType.Svg;
// נתיב לקובץ המקורי
img.File = dataDir + "SVGToPDF.svg";
// הגדרת רוחב למופע התמונה
img.FixWidth = 50;
// הגדרת גובה למופע התמונה
img.FixHeight = 50;
// יצירת מופע של טבלה
Aspose.Pdf.Table table = new Aspose.Pdf.Table();
// הגדרת רוחב לתאים בטבלה
table.ColumnWidths = "100 100";
// יצירת אובייקט שורה והוספתו למופע הטבלה
Aspose.Pdf.Row row = table.Rows.Add();
// יצירת אובייקט תא והוספתו למופע השורה
Aspose.Pdf.Cell cell = row.Cells.Add();
// הוספת קטע טקסט לאוסף הפסקאות של אובייקט התא
cell.Paragraphs.Add(new TextFragment("תא ראשון"));
// הוספת תא נוסף לאובייקט השורה
cell = row.Cells.Add();
// הוספת תמונת SVG לאוסף הפסקאות של התא שנוסף לאחרונה
cell.Paragraphs.Add(img);
// יצירת אובייקט עמוד והוספתו לאוסף העמודים של אובייקט המסמך
Page page = doc.Pages.Add();
// הוספת הטבלה לאוסף הפסקאות של אובייקט העמוד
page.Paragraphs.Add(table);

dataDir = dataDir + "AddSVGObject_out.pdf";
// שמירת הקובץ PDF
doc.Save(dataDir);
```
## שימוש בתגי HTML בתוך טבלה

לעיתים קרובות אתה יכול להיתקל בדרישה לייבא תוכן ממסד נתונים שמכיל תגי HTML ולאחר מכן לייבא את התוכן לאובייקט הטבלה. בעת ייבוא התוכן, יש לטפל בתגי ה-HTML בהתאם בתוך מסמך PDF. שיפרנו את השיטה ImprotDataTable(), על מנת לעמוד בדרישה זו כדלהלן:

{{% alert color="primary" %}}
אנא שים לב ששימוש בתגי HTML בתוך אלמנט הטבלה מגדיל את זמן יצירת המסמך, מכיוון שה-API צריך לעבד את תגי ה-HTML בהתאם ולהציג אותם במסמך PDF הפלט.
{{% /alert %}}

```csharp
// לדוגמאות מלאות וקבצי נתונים, אנא עבור ל- https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לספריית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

DataTable dt = new DataTable("Employee");
dt.Columns.Add("data", System.Type.GetType("System.String"));

DataRow dr = dt.NewRow();
dr[0] = "<li>מחלקת רפואת חירום: רחוב ספרוס 3400 קומת קרקע בניין סילברשטיין פילדלפיה PA 19104-4206</li>";
dt.Rows.Add(dr);
dr = dt.NewRow();
dr[0] = "<li>שירות תצפית רפואי של פן: רחוב ספרוס 3400 קומת קרקע דונר פילדלפיה PA 19104-4206</li>";
dt.Rows.Add(dr);
dr = dt.NewRow();
dr[0] = "<li>UPHS/Presbyterian - מחלקת רפואת חירום: רחוב 39 צפון 51 . פילדלפיה PA 19104-2640</li>";
dt.Rows.Add(dr);

Document doc = new Document();
doc.Pages.Add();
// מאתחל מופע חדש של הטבלה
Aspose.Pdf.Table tableProvider = new Aspose.Pdf.Table();
//קובע את רוחבי העמודות של הטבלה
tableProvider.ColumnWidths = "400 50 ";
// קובע את צבע הגבול של הטבלה לאפור בהיר
tableProvider.Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, 0.5F, Aspose.Pdf.Color.FromRgb(System.Drawing.Color.LightGray));
// קובע את הגבול לתאי הטבלה
tableProvider.DefaultCellBorder = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, 0.5F, Aspose.Pdf.Color.FromRgb(System.Drawing.Color.LightGray));
Aspose.Pdf.MarginInfo margin = new Aspose.Pdf.MarginInfo();
margin.Top = 2.5F;
margin.Left = 2.5F;
margin.Bottom = 1.0F;
tableProvider.DefaultCellPadding = margin;

tableProvider.ImportDataTable(dt, false, 0, 0, 3, 1, true);

doc.Pages[1].Paragraphs.Add(tableProvider);
doc.Save(dataDir + "HTMLInsideTableCell_out.pdf");
```
## הוספת שבירת עמוד בין שורות של טבלה

כברירת מחדל, כאשר יוצרים טבלה בתוך קובץ PDF, הטבלה זורמת לעמודים הבאים כאשר היא מגיעה לשולי התחתית של הטבלה. עם זאת, יתכן שיש לנו דרישה להכניס באופן כפוי שבירת עמוד כאשר מוסיפים מספר מסוים של שורות לטבלה. קטע הקוד הבא מציג את השלבים להוספת שבירת עמוד כאשר מתווספות 10 שורות לטבלה.

```csharp
// לדוגמאות מלאות וקבצי נתונים, אנא עבורו ל https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לספריית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

// יצירת מופע מסמך
Document doc = new Document();
// הוספת עמוד לאוסף העמודים של קובץ PDF
doc.Pages.Add();
// יצירת מופע טבלה
Aspose.Pdf.Table tab = new Aspose.Pdf.Table();
// הגדרת סגנון גבול לטבלה
tab.Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, Aspose.Pdf.Color.Red);
// הגדרת סגנון גבול ברירת מחדל לטבלה עם צבע גבול אדום
tab.DefaultCellBorder = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, Aspose.Pdf.Color.Red);
// ציון רוחב עמודות הטבלה
tab.ColumnWidths = "100 100";
// יצירת לולאה להוספת 200 שורות לטבלה
for (int counter = 0; counter <= 200; counter++)
{
    Aspose.Pdf.Row row = new Aspose.Pdf.Row();
    tab.Rows.Add(row);
    Aspose.Pdf.Cell cell1 = new Aspose.Pdf.Cell();
    cell1.Paragraphs.Add(new TextFragment("תא " + counter + ", 0"));
    row.Cells.Add(cell1); Aspose.Pdf.Cell cell2 = new Aspose.Pdf.Cell();
    cell2.Paragraphs.Add(new TextFragment("תא " + counter + ", 1"));
    row.Cells.Add(cell2);
    // כאשר מתווספות 10 שורות, להציג שורה חדשה בעמוד חדש
    if (counter % 10 == 0 && counter != 0) row.IsInNewPage = true;
}
// הוספת הטבלה לאוסף הפסקאות של קובץ PDF
doc.Pages[1].Paragraphs.Add(tab);

dataDir = dataDir + "InsertPageBreak_out.pdf";
// שמירת מסמך PDF
doc.Save(dataDir);
```
## להציג טבלה בעמוד חדש

כברירת מחדל, פסקאות מתווספות לאוסף Paragraphs של אובייקט Page. עם זאת, ניתן להציג טבלה בעמוד חדש במקום לאחר האובייקט ברמת הפסקה שנוסף לעמוד באופן ישיר.

### דוגמה: איך להציג טבלה בעמוד חדש באמצעות C\#

כדי להציג טבלה בעמוד חדש, השתמש בתכונה [IsInNewPage](https://reference.aspose.com/pdf/net/aspose.pdf/baseparagraph/properties/isinnewpage) במחלקת BaseParagraph. קטע הקוד הבא מראה איך לעשות זאת.

```csharp
// לדוגמאות מלאות וקבצי נתונים, אנא עבור ל https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לתיקיית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

Document doc = new Document();
PageInfo pageInfo = doc.PageInfo;
Aspose.Pdf.MarginInfo marginInfo = pageInfo.Margin;

marginInfo.Left = 37;
marginInfo.Right = 37;
marginInfo.Top = 37;
marginInfo.Bottom = 37;

pageInfo.IsLandscape = true;

Aspose.Pdf.Table table = new Aspose.Pdf.Table();
table.ColumnWidths = "50 100";
// עמוד שנוסף.
Page curPage = doc.Pages.Add();
for (int i = 1; i <= 120; i++)
{
    Aspose.Pdf.Row row = table.Rows.Add();
    row.FixedRowHeight = 15;
    Aspose.Pdf.Cell cell1 = row.Cells.Add();
    cell1.Paragraphs.Add(new TextFragment("תוכן 1"));
    Aspose.Pdf.Cell cell2 = row.Cells.Add();
    cell2.Paragraphs.Add(new TextFragment("HHHHH"));
}
Aspose.Pdf.Paragraphs paragraphs = curPage.Paragraphs;
paragraphs.Add(table);
/********************************************/
Aspose.Pdf.Table table1 = new Aspose.Pdf.Table();
table.ColumnWidths = "100 100";
for (int i = 1; i <= 10; i++)
{
    Aspose.Pdf.Row row = table1.Rows.Add();
    Aspose.Pdf.Cell cell1 = row.Cells.Add();
    cell1.Paragraphs.Add(new TextFragment("LAAAAAAA"));
    Aspose.Pdf.Cell cell2 = row.Cells.Add();
    cell2.Paragraphs.Add(new TextFragment("LAAGGGGGG"));
}
table1.IsInNewPage = true;
// אני רוצה לשמור את הטבלה 1 לעמוד הבא בבקשה...
paragraphs.Add(table1);
dataDir = dataDir + "IsNewPageProperty_Test_out.pdf";
doc.Save(dataDir);
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

