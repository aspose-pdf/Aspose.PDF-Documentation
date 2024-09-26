---
title: יצירת טבלה עם Entity Framework 
linktitle: יצירת טבלה עם Entity Framework
type: docs
weight: 40
url: /net/render-table-using-entity-framework-model-as-data-source/
description: המאמר הזה יראה לך איך ליצור טבלה באמצעות מודל Entity Framework כמקור נתונים באמצעות Aspose.PDF ל-.NET.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

ישנן מספר משימות שלעיתים קרובות יותר נוח לייצא נתונים ממסדי נתונים למסמך PDF ללא שימוש בתכנית המרת HTML ל-PDF שהפכה לפופולרית לאחרונה.

המאמר הזה יראה לך איך ליצור מסמך PDF באמצעות Aspose.PDF ל-.NET.

## יסודות יצירת PDF עם Aspose.PDF

אחת המחלקות החשובות ביותר ב-Aspose.PDF היא [מחלקת Document](https://reference.aspose.com/pdf/net/aspose.pdf/document). מחלקה זו היא מנוע לפלט PDF. כדי להציג מבנה PDF, ספריית Aspose.PDF משתמשת במודל Document-Page, שבו:

* Document - מכיל את תכונות המסמך PDF כולל אוסף הדפים;
* מסמך - מכיל את תכונות המסמך בפורמט PDF כולל אוסף דפים;
* דף - מכיל את תכונות של דף מסוים ואוספים שונים של אלמנטים הקשורים לדף זה.

לכן, כדי ליצור מסמך PDF עם Aspose.PDF, עליך לבצע את השלבים הבאים:

1. צור את אובייקט המסמך;
1. הוסף את הדף (אובייקט הדף) לאובייקט המסמך;
1. צור אובייקטים שמוצבים על הדף (לדוגמה, קטע טקסט, טבלה, וכו')
1. הוסף את הפריטים שנוצרו לאוסף המתאים על הדף (במקרה שלנו זה יהיה אוסף פסקאות);
1. שמור את המסמך כקובץ PDF.

```csharp
// שלב 1
var document = new Document
{
    PageInfo = new PageInfo { Margin = new MarginInfo(28, 28, 28, 42) }
};

// שלב 2
var pdfPage = document.Pages.Add();

// שלב 3
var textFragment = new TextFragment(reportTitle);
// ..........................................

var table = new Table
{
    // .................................
};

// שלב 4
pdfPage.Paragraphs.Add(textFragment);
pdfPage.Paragraphs.Add(table);

// שלב 5
using (var streamOut = new MemoryStream())
{
    document.Save(streamOut);
    return new FileContentResult(streamOut.ToArray(), "application/pdf")
    {
        FileDownloadName = "tenants.pdf"
    };
}
```
הבעיה הנפוצה ביותר היא הצגת נתונים בפורמט של טבלה. מחלקת [Table](https://reference.aspose.com/pdf/net/aspose.pdf/table) משמשת לעיבוד טבלאות. מחלקה זו נותנת לנו את היכולת ליצור טבלאות ולמקם אותם במסמך, באמצעות [Rows](https://reference.aspose.com/pdf/net/aspose.pdf/rows) ו-[Cells](https://reference.aspose.com/pdf/net/aspose.pdf/cell). לכן, כדי ליצור את הטבלה, יש להוסיף את מספר השורות הנדרש ולמלא אותם במספר התאים המתאים.

הדוגמה הבאה יוצרת טבלה בגודל 4x10.

```csharp
var table = new Table
    {
        // הגדרת רוחבי עמודות אוטומטיים של הטבלה
        ColumnWidths = "25% 25% 25% 25%",
        // הגדרת ריפוד לתא
        DefaultCellPadding = new MarginInfo(10, 5, 10, 5), // שמאל תחתון ימין עליון
        // הגדרת צבע הגבול של הטבלה לירוק
        Border = new BorderInfo(BorderSide.All, .5f, Color.Green),
        // הגדרת הגבול לתאי הטבלה כשחור
        DefaultCellBorder = new BorderInfo(BorderSide.All, .2f, Color.Green),
    };
    for (var rowCount = 0; rowCount < 10; rowCount++)
    {
        // הוספת שורה לטבלה
        var row = table.Rows.Add();
        // הוספת תאים לטבלה
        for (int i = 0; i < 4; i++)
        {
            row.Cells.Add($"Cell ({i+1}, {rowCount +1})");
        }
    }
    // הוספת אובייקט הטבלה לדף הראשון של המסמך
    document.Pages[1].Paragraphs.Add(table);
```
changefreq: "monthly"
type: docs
כאשר מאתחלים את אובייקט הטבלה, הופעלו ההגדרות המינימליות של המראה:

* [רוחב העמודות](https://reference.aspose.com/pdf/net/aspose.pdf/table/properties/columnwidths) - רוחב העמודות (כברירת מחדל);
* [ריפוד תא ברירת מחדל](https://reference.aspose.com/pdf/net/aspose.pdf/table/properties/defaultcellpadding) - שדות ברירת המחדל לתאי הטבלה;
* [מסגרת](https://reference.aspose.com/pdf/net/aspose.pdf/table/properties/border) - מאפייני מסגרת הטבלה (סגנון, עובי, צבע);
* [מסגרת תא ברירת מחדל](https://reference.aspose.com/pdf/net/aspose.pdf/table/properties/defaultcellborder) - מאפייני מסגרת התא (סגנון, עובי, צבע).

כתוצאה מכך, אנו מקבלים טבלה בגודל 4x10 עם עמודות ברוחב שווה.

![טבלה 4x10](http://aspose-html-doc.azurewebsites.net/docs/images/img001.jpg)

## ייצוא נתונים מאובייקטים של ADO.NET

מחלקת הטבלה מספקת שיטות לאינטראקציה עם מקורות נתונים של ADO.NET - [ייבוא טבלת נתונים](https://reference.aspose.com/pdf/net/aspose.pdf.table/importdatatable/methods/1) ו-[ייבוא תצוגת נתונים](https://reference.aspose.com/pdf/net/aspose.pdf/table/methods/importdataview).
מחלקת Table מספקת שיטות לאינטראקציה עם מקורות נתונים של ADO.NET - [ImportDataTable](https://reference.aspose.com/pdf/net/aspose.pdf.table/importdatatable/methods/1) ו-[ImportDataView](https://reference.aspose.com/pdf/net/aspose.pdf/table/methods/importdataview).
מתוך הבנה שאובייקטים אלו אינם נוחים במיוחד לעבודה בתבנית MVC, נסתפק בדוגמה קצרצרה. בדוגמה זו (שורה 50), השיטה ImportDataTable נקראת ומקבלת כפרמטרים מופע של DataTable והגדרות נוספות כמו דגל הכותרת והמיקום ההתחלתי (שורות/עמודות) לפלט הנתונים.

```csharp
// יצירת מסמך PDF חדש
var document = new Document
{
    PageInfo = new PageInfo { Margin = new MarginInfo(28, 28, 28, 42) }
};

var pdfPage = document.Pages.Add();

// אתחול מופע חדש של TextFragment לכותרת הדוח
var textFragment = new TextFragment(reportTitle1);
Table table = new Table
{
    // הגדרת רוחבי העמודות בטבלה
    ColumnWidths = "25% 25% 25% 25%",
    // הגדרת ריפוד לתאים
    DefaultCellPadding = new MarginInfo(10, 5, 10, 5), // שמאל תחתון ימין עליון
    // הגדרת צבע הגבול של הטבלה לירוק
    Border = new BorderInfo(BorderSide.All, .5f, Color.Green),
    // הגדרת הגבול לתאי הטבלה לשחור
    DefaultCellBorder = new BorderInfo(BorderSide.All, .2f, Color.Green),
};

var configuration = new ConfigurationBuilder()
    .SetBasePath(Directory.GetCurrentDirectory())
    .AddJsonFile("config.json", false)
    .Build();

var connectionString = configuration.GetSection("connectionString").Value;

if (string.IsNullOrEmpty(connectionString))
    throw new ArgumentException("אין מחרוזת חיבור ב-config.json");

var resultTable = new DataTable();

using (var conn = new SqlConnection(connectionString))
{
    const string sql = "SELECT * FROM Tennats";
    using (var cmd = new SqlCommand(sql, conn))
    {
        using (var adapter = new SqlDataAdapter(cmd))
        {
            adapter.Fill(resultTable);
        }
    }
}

table.ImportDataTable(resultTable,true,1,1);

// הוספת אובייקט הטבלה לעמוד הראשון של המסמך
document.Pages[1].Paragraphs.Add(table);
using (var streamOut = new MemoryStream())
{
    document.Save(streamOut);
    return new FileContentResult(streamOut.ToArray(), "application/pdf")
    {
        FileDownloadName = "demotable2.pdf"
    };
}
```
## ייצוא נתונים מ-Entity Framework

יותר רלוונטי ל-.NET המודרני הוא ייבוא נתונים ממסגרות ORM. במקרה זה, רעיון טוב הוא להרחיב את המחלקה Table עם שיטות הרחבה ליבוא נתונים מרשימה פשוטה או מנתונים מקובצים. בואו ניתן דוגמה לאחד ה-ORM הפופולריים ביותר - Entity Framework.

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
                // Add row to table
                var row = table.Rows.Add();
                // Add table cells
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
                // Add group row to table
                var row = table.Rows.Add();
                var cell = row.Cells.Add(group.Key.ToString());
                cell.ColSpan = props.Length;
                cell.BackgroundColor = Pdf.Color.DarkGray;
                cell.DefaultCellTextState.ForegroundColor = Pdf.Color.White;

                foreach (var item in group.Values)
                {
                    // Add data row to table
                    var dataRow = table.Rows.Add();
                    // Add cells
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
                            dataRow.Cells.Add(dataItem.toString());
                        }
                    }
                }
            }
        }
    }
```

מאפייני סימון הנתונים נמצאים בשימוש תכוף לתיאור מודלים ומסייעים לנו ליצור את הטבלה. לפיכך, אלגוריתם יצירת הטבלה הבא נבחר עבור ImportEntityList:

* שורות 12-18: בניית שורת כותרת והוספת תאי כותרת על פי הכלל "אם מופיע DisplayAttribute, אז לקחת את ערכו, אחרת לקחת את שם המאפיין"
* שורות 50-53: בניית שורות הנתונים והוספת תאי שורה על פי הכלל "אם מוגדר המאפיין DataTypeAttribute, אז בודקים האם נדרש לבצע הגדרות עיצוב נוספות עבורו, ואחרת פשוט להמיר נתונים למחרוזת ולהוסיף לתא;"

בדוגמה זו, בוצעו התאמות מותאמות אישית עבור DataType.Currency (שורות 32-34) ו-DataType.Date (שורות 35-43), אך ניתן להוסיף עוד לפי הצורך.
אלגוריתם של שיטת ImportGroupedData דומה כמעט לקודמת. משתמשים במחלקה GroupViewModel נוספת, לאחסון הנתונים המקובצים.

```csharp
using System.Collections.Generic;
    public class GroupViewModel<K,T>
    {
        public K Key;
        public IEnumerable<T> Values;
    }
```
מאז שאנו מעבדים קבוצות, תחילה אנו יוצרים שורה עבור ערך המפתח (שורות 66-71), ולאחר מכן - שורות של קבוצה זו.
