---
title: אינטגרציה של טבלה עם מקורות נתונים PDF
linktitle: אינטגרציה של טבלה
type: docs
weight: 30
url: /net/integrate-table/
description: כתבה זו מציגה כיצד לאחד טבלאות PDF. איחוד טבלה עם מסד נתונים וקביעה האם הטבלה תתפצל בעמוד הנוכחי.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "אינטגרציה של טבלה עם מקורות נתונים PDF",
    "alternativeHeadline": "כיצד לאחד טבלה עם מקורות נתונים PDF",
    "author": {
        "@type": "Person",
        "name":"אנסטסיה הולוב",
        "givenName": "אנסטסיה",
        "familyName": "הולוב",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "יצירת מסמכי PDF",
    "keywords": "pdf, c#, איחוד טבלה",
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
    "url": "/net/integrate-table/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/integrate-table/"
    },
    "dateModified": "2022-02-04",
    "description": "כתבה זו מציגה כיצד לאחד טבלאות PDF. איחוד טבלה עם מסד נתונים וקביעה האם הטבלה תתפצל בעמוד הנוכחי."
}
</script>
הקטע הבא בקוד עובד גם עם ספריית [Aspose.PDF.Drawing](/pdf/net/drawing/).

## אינטגרציה של טבלה עם מסד נתונים

מסדי נתונים נועדו לאחסון וניהול של נתונים. נהוג בקרב מתכנתים למלא אובייקטים שונים בנתונים ממסדי נתונים. המאמר הזה עוסק בהוספת נתונים ממסד נתונים לתוך טבלה. ניתן למלא את אובייקט [Table](https://reference.aspose.com/pdf/net/aspose.pdf/table) בנתונים מכל מקור נתונים באמצעות Aspose.PDF ל-.NET. זה לא רק אפשרי, אלא גם קל מאוד.

[Aspose.PDF ל-.NET](https://docs.aspose.com/pdf/net/) מאפשר למפתחים לייבא נתונים מ:

- מערך אובייקטים
- DataTable
- DataView

נושא זה מספק מידע על איסוף נתונים מ-DataTable או DataView.

כל המפתחים הפועלים תחת פלטפורמת .NET חייבים להיות מכירים במושגי ADO.NET הבסיסיים שהוצגו על ידי מסגרת .NET.
כל המפתחים העובדים תחת פלטפורמת .NET חייבים להיות מכירים במושגי ה-ADO.NET הבסיסיים שהוצגו על ידי מסגרת ה-.NET.

המתודות ImportDataTable(..) ו-ImportDataView(..) של מחלקת ה-Table משמשות לייבוא נתונים ממסדי נתונים.

הדוגמה להלן מדגימה את השימוש במתודת ImportDataTable. בדוגמה זו, אובייקט ה-DataTable נוצר מחדש ורשומות מתווספות באופן תכנותי במקום למלא את ה-DataTable בנתונים ממסדי נתונים. מפתחים יכולים למלא DataTable מהמסד הנתונים גם כן לפי רצונם.

```csharp
// לדוגמאות מלאות וקבצי נתונים, נא לעבור ל https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// נתיב לספריית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

DataTable dt = new DataTable("Employee");
dt.Columns.Add("Employee_ID", typeof(Int32));
dt.Columns.Add("Employee_Name", typeof(string));
dt.Columns.Add("Gender", typeof(string));
// הוספת 2 שורות לאובייקט DataTable באופן תכנותי
DataRow dr = dt.NewRow();
dr[0] = 1;
dr[1] = "John Smith";
dr[2] = "Male";
dt.Rows.Add(dr);
dr = dt.NewRow();
dr[0] = 2;
dr[1] = "Mary Miller";
dr[2] = "Female";
dt.Rows.Add(dr);
// יצירת מופע של מסמך
Document doc = new Document();
doc.Pages.Add();
// אתחול מופע חדש של הטבלה
Aspose.Pdf.Table table = new Aspose.Pdf.Table();
// הגדרת רוחב העמודות של הטבלה
table.ColumnWidths = "40 100 100 100";
// הגדרת צבע הגבול של הטבלה כאפור בהיר
table.Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, .5f, Aspose.Pdf.Color.FromRgb(System.Drawing.Color.LightGray));
// הגדרת הגבול לתאי הטבלה
table.DefaultCellBorder = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, .5f, Aspose.Pdf.Color.FromRgb(System.Drawing.Color.LightGray));
table.ImportDataTable(dt, true, 0, 1, 3, 3);

// הוספת אובייקט הטבלה לעמוד הראשון של המסמך הנכנס
doc.Pages[1].Paragraphs.Add(table);
dataDir = dataDir + "DataIntegrated_out.pdf";
// שמירת המסמך המעודכן המכיל את אובייקט הטבלה
doc.Save(dataDir);
```
## כיצד לקבוע האם טבלה תשבר בדף הנוכחי

טבלאות מתווספות כברירת מחדל מהפינה השמאלית העליונה ואם הטבלה מגיעה לקצה הדף, היא נשברת באופן אוטומטי. ניתן לקבל באופן תכנותי את המידע האם הטבלה תוכל להיכלל בדף הנוכחי או שהיא תישבר בתחתית הדף. לשם כך, ראשית עליך לקבל את מידע גודל המסמך, לאחר מכן עליך לקבל מידע על שולי הדף העליונים והתחתונים, מידע על שולי הטבלה העליונים וגובה הטבלה. אם תוסיף שולי דף עליונים + שולי דף תחתונים + שולי טבלה עליונים + גובה הטבלה ותחסיר מגובה המסמך, תוכל לקבל את כמות המקום הנותר מעל המסמך. בהתאם לגובה שורה מסוים (שציינת), תוכל לחשב האם כל השורות של הטבלה יכולות להתאכלס במרחב הנותר מעל דף או לא. נא להביט על קטע הקוד הבא. בקוד הבא, גובה השורה הממוצע הוא 23.002 נקודות.

```csharp
// לדוגמאות מלאות וקבצי נתונים, אנא עבור ל https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לספריית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

// יצירת מופע של מחלקת PDF
Document pdf = new Document();
// הוספת הסעיף לאוסף סעיפים של מסמך PDF
Aspose.Pdf.Page page = pdf.Pages.Add();
// יצירת מופע של אובייקט טבלה
Aspose.Pdf.Table table1 = new Aspose.Pdf.Table();
table1.Margin.Top = 300;
// הוספת הטבלה לאוסף הפסקאות של הסעיף הרצוי
page.Paragraphs.Add(table1);
// קביעת רוחב העמודות של הטבלה
table1.ColumnWidths = "100 100 100";
// קביעת גבול ברירת מחדל של תא באמצעות אובייקט BorderInfo
table1.DefaultCellBorder = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, 0.1F);
// קביעת גבול הטבלה באמצעות אובייקט BorderInfo מותאם אישית
table1.Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, 1F);
// יצירת אובייקט MarginInfo וקביעת שוליו השמאליים, התחתונים, הימניים והעליונים
Aspose.Pdf.MarginInfo margin = new Aspose.Pdf.MarginInfo();
margin.Top = 5f;
margin.Left = 5f;
margin.Right = 5f;
margin.Bottom = 5f;
// קביעת הריפוד המוגדר כברירת מחדל לאובייקט MarginInfo
table1.DefaultCellPadding = margin;
// אם תגדיל את המונה ל-17, הטבלה תישבר
// מכיוון שלא ניתן להכילה יותר בדף זה
for (int RowCounter = 0; RowCounter <= 16; RowCounter++)
{
    // יצירת שורות בטבלה ולאחר מכן תאים בשורות
    Aspose.Pdf.Row row1 = table1.Rows.Add();
    row1.Cells.Add("col " + RowCounter.ToString() + ", 1");
    row1.Cells.Add("col " + RowCounter.ToString() + ", 2");
    row1.Cells.Add("col " + RowCounter.ToString() + ", 3");
}
// קבלת מידע על גובה הדף
float PageHeight = (float)pdf.PageInfo.Height;
// קבלת מידע על גובה האובייקטים הכולל של שולי הדף העליונים והתחתונים,
// שולי הטבלה העליונים וגובה הטבלה.
float TotalObjectsHeight = (float)page.PageInfo.Margin.Top + (float)page.PageInfo.Margin.Bottom + (float)table1.Margin.Top + (float)table1.GetHeight();

// הצגת מידע על גובה המסמך PDF, גובה הטבלה, מידע על שולי הטבלה העליונים ומידע על שולי הדף העליונים
// והתחתונים
Console.WriteLine("גובה מסמך PDF = " + pdf.PageInfo.Height.ToString() + "\nמידע על שולי עליון = " + page.PageInfo.Margin.Top.ToString() + "\nמידע על שולי תחתון = " + page.PageInfo.Margin.Bottom.ToString() + "\n\nמידע על שולי טבלה עליון = " + table1.Margin.Top.ToString() + "\nגובה שורה ממוצע = " + table1.Rows[0].MinRowHeight.ToString() + " \nגובה טבלה " + table1.GetHeight().ToString() + "\n ----------------------------------------" + "\nגובה דף כולל =" + PageHeight.ToString() + "\nגובה מצטבר כולל טבלה =" + TotalObjectsHeight.ToString());

// בדיקה אם נחסיר את סכום שולי הדף העליונים + שולי הדף התחתונים
// + שולי הטבלה העליונים וגובה הטבלה מגובה הדף וזה פחות
// מ-10 (שורה ממוצעת יכולה להיות גדולה מ-10)
if ((PageHeight - TotalObjectsHeight) <= 10)
    // אם הערך פחות מ-10, אז להציג הודעה.
    // שמראה שלא ניתן למקם שורה נוספת ואם נוסיף
    // שורה חדשה, הטבלה תישבר. זה תלוי בערך גובה השורה.
    Console.WriteLine("גובה דף - גובה אובייקטים < 10, אז הטבלה תישבר");


dataDir = dataDir + "DetermineTableBreak_out.pdf";
// שמירת מסמך ה-pdf
pdf.Save(dataDir);
```
## הוספת עמודה חוזרת בטבלה

במחלקת Aspose.Pdf.Table, ניתן להגדיר RepeatingRowsCount שיחזור שורות אם הטבלה ארוכה מדי באופן אנכי ויוצאת לעמוד הבא. עם זאת, במקרים מסוימים, הטבלאות רחבות מדי כדי להתאים לעמוד בודד וצריכות להמשיך לעמוד הבא. כדי לשרת את המטרה הזו, הטמענו את התכונה RepeatingColumnsCount במחלקת Aspose.Pdf.Table. הגדרת תכונה זו תגרום לטבלה להישבר לכיוון העמוד הבא על פי עמודות ולחזור על מספר העמודות הנתון בתחילת העמוד הבא. קטע הקוד הבא מראה את שימוש בתכונת RepeatingColumnsCount:

```csharp
// לדוגמאות מלאות וקבצי נתונים, בבקשה לגשת ל https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לספריית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

string outFile = dataDir + "AddRepeatingColumn_out.pdf";
// יצירת מסמך חדש
Document doc = new Document();
Aspose.Pdf.Page page = doc.Pages.Add();

// יצירת טבלה חיצונית שתתפוס את כל העמוד
Aspose.Pdf.Table outerTable = new Aspose.Pdf.Table();
outerTable.ColumnWidths = "100%";
outerTable.HorizontalAlignment = HorizontalAlignment.Left;

// יצירת אובייקט טבלה שישבר בתוך העמוד הזהה
Aspose.Pdf.Table mytable = new Aspose.Pdf.Table();
mytable.Broken = TableBroken.VerticalInSamePage;
mytable.ColumnAdjustment = ColumnAdjustment.AutoFitToContent;

// הוספת הטבלה החיצונית לפסקאות העמוד
// הוספת mytable ל-outerTable
page.Paragraphs.Add(outerTable);
var bodyRow = outerTable.Rows.Add();
var bodyCell = bodyRow.Cells.Add();
bodyCell.Paragraphs.Add(mytable);
mytable.RepeatingColumnsCount = 5;
page.Paragraphs.Add(mytable);

// הוספת שורת כותרת
Aspose.Pdf.Row row = mytable.Rows.Add();
row.Cells.Add("header 1");
row.Cells.Add("header 2");
row.Cells.Add("header 3");
row.Cells.Add("header 4");
row.Cells.Add("header 5");
row.Cells.Add("header 6");
row.Cells.Add("header 7");
row.Cells.Add("header 11");
row.Cells.Add("header 12");
row.Cells.Add("header 13");
row.Cells.Add("header 14");
row.Cells.Add("header 15");
row.Cells.Add("header 16");
row.Cells.Add("header 17");

for (int RowCounter = 0; RowCounter <= 5; RowCounter++)

{
    // יצירת שורות בטבלה ולאחר מכן תאים בשורות
    Aspose.Pdf.Row row1 = mytable.Rows.Add();
    row1.Cells.Add("col " + RowCounter.ToString() + ", 1");
    row1.Cells.Add("col " + RowCounter.ToString() + ", 2");
    row1.Cells.Add("col " + RowCounter.ToString() + ", 3");
    row1.Cells.Add("col " + RowCounter.ToString() + ", 4");
    row1.Cells.Add("col " + RowCounter.ToString() + ", 5");
    row1.Cells.Add("col " + RowCounter.ToString() + ", 6");
    row1.Cells.Add("col " + RowCounter.ToString() + ", 7");
    row1.Cells.Add("col " + RowCounter.ToString() + ", 11");
    row1.Cells.Add("col " + RowCounter.ToString() + ", 12");
    row1.Cells.Add("col " + RowCounter.ToString() + ", 13");
    row1.Cells.Add("col " + RowCounter.ToString() + ", 14");
    row1.Cells.Add("col " + RowCounter.ToString() + ", 15");
    row1.Cells.Add("col " + RowCounter.ToString() + ", 16");
    row1.Cells.Add("col " + RowCounter.ToString() + ", 17");
}
doc.Save(outFile);
```
## שילוב טבלה עם מקור Entity Framework

יותר רלוונטי ל-.NET המודרני הוא ייבוא נתונים ממסגרות ORM. במקרה זה, רעיון טוב להרחיב את מחלקת הטבלה עם שיטות הרחבה לייבוא נתונים מרשימה פשוטה או מנתונים מקובצים. בואו ניתן דוגמה לאחת ממסגרות ה-ORM הפופולריות - Entity Framework.

```csharp
public static class PdfHelper
    {
        public static void ImportEntityList<TSource>(this Pdf.Table table, IList<TSource> data)
        {
            var headRow = table.Rows.Add();

            var props = typeof(TSource).GetProperties(BindingFlags.Public | BindingFlags.Instance);
            foreach (var prop in props)
            {
                headRow.Cells.Add(prop.GetCustomAttribute(typeof(DisplayAttribute)) is DisplayAttribute dd ? dd.Name : prop.Name);
            }

            foreach (var item in data)
            {
                // הוסף שורה לטבלה
                var row = table.Rows.Add();
                // הוסף תאים לטבלה
                foreach (var t in props)
                {
                    var dataItem = t.GetValue(item, null);
                    if (t.GetCustomAttribute(typeof(DataTypeAttribute)) is DataTypeAttribute dataType)
                        switch (dataType.DataType)
                        {

                            case DataType.Currency:
                                row.Cells.Add(string.Format("{0:C}", dataItem));
                                break;
                            case DataType.Date:
                                var dateTime = (DateTime)dataItem;
                                if (t.GetCustomAttribute(typeof(DisplayFormatAttribute)) is DisplayFormatAttribute df)
                                {
                                    row.Cells.Add(string.IsNullOrEmpty(df.DataFormatString)
                                        ? dateTime.ToShortDateString()
                                        : string.Format(df.DataFormatString, dateTime));
                                }
                                break;
                            default:
                                row.Cells.Add(dataItem.ToString());
                                break;
                        }
                    else
                    {
                        row.Cells.Add(dataItem.ToString());
                    }
                }
            }
        }
        public static void ImportGroupedData<TKey,TValue>(this Pdf.Table table, IEnumerable<Models.GroupViewModel<TKey, TValue>> groupedData)
        {
            var headRow = table.Rows.Add();           
            var props = typeof(TValue).GetProperties(BindingFlags.Public | BindingFlags.Instance);
            foreach (var prop in props)
            {
               headRow.Cells.Add(prop.GetCustomAttribute(typeof(DisplayAttribute)) is DisplayAttribute dd ? dd.Name : prop.Name);               
            }

            foreach (var group in groupedData)
            {
                // הוסף שורת קבוצה לטבלה
                var row = table.Rows.Add();
                var cell = row.Cells.Add(group.Key.ToString());
                cell.ColSpan = props.Length;
                cell.BackgroundColor = Pdf.Color.DarkGray;
                cell.DefaultCellTextState.ForegroundColor = Pdf.Color.White;

                foreach (var item in group.Values)
                {
                    // הוסף שורת נתונים לטבלה
                    var dataRow = table.Rows.Add();
                    // הוסף תאים
                    foreach (var t in props)
                    {
                        var dataItem = t.GetValue(item, null);

                        if (t.GetCustomAttribute(typeof(DataTypeAttribute)) is DataTypeAttribute dataType)
                            switch (dataType.DataType)
                            {
                                case DataType.Currency:
                                    dataRow.Cells.Add(string.Format("{0:C}", dataItem));
                                    break;
                                case DataType.Date:
                                    var dateTime = (DateTime)dataItem;
                                    if (t.GetCustomAttribute(typeof(DisplayFormatAttribute)) is DisplayFormatAttribute df)
                                    {
                                        dataRow.Cells.Add(string.IsNullOrEmpty(df.DataFormatString)
                                            ? dateTime.ToShortDateString()
                                            : string.Format(df.DataFormatString, dateTime));
                                    }
                                    break;
                                default:
                                    dataRow.Cells.Add(dataItem.ToString());
                                    break;
                            }
                        else
                        {
                            dataRow.Cells.Add(dataItem.ToString());
                        }
                    }
                }
            }
        }
    }
```
תכונות Data Annotations נמצאות לעיתים קרובות בשימוש לתיאור מודלים ועוזרות לנו ליצור את הטבלה. לכן, האלגוריתם הבא ליצירת טבלה נבחר עבור ImportEntityList:

- שורות 12-18: בניית שורת כותרת והוספת תאי כותרת לפי הכלל "אם תכונת DisplayAttribute נמצאת, אז לקחת את ערכה, אחרת לקחת את שם המאפיין"
- שורות 50-53: בניית שורות נתונים והוספת תאים לשורה לפי הכלל "אם תכונת DataTypeAttribute מוגדרת, אז בודקים האם יש צורך לבצע הגדרות עיצוב נוספות עבורה, ואחרת פשוט להמיר נתונים למחרוזת ולהוסיף לתא;"

בדוגמה זו, בוצעו התאמות מותאמות אישית עבור DataType.Currency (שורות 32-34) ו-DataType.Date (שורות 35-43), אך ניתן להוסיף אחרות לפי צורך.
האלגוריתם של המתודה ImportGroupedData דומה כמעט לקודם. מחלקת GroupViewModel נוספת משמשת, לאחסון הנתונים המקובצים.

```csharp
.using System.Collections.Generic;
    public class GroupViewModel<K,T>
    {
        public K Key;
        public IEnumerable<T> Values;
    }
```
מכיוון שאנו מעבדים קבוצות, תחילה אנו מייצרים שורה עבור הערך המפתח (שורות 66-71), ולאחר מכן - את השורות של קבוצה זו.

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

