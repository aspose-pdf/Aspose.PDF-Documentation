---
title: יצירת טבלה ממקור נתונים
linktitle: יצירת טבלה ממקור נתונים
type: docs
weight: 30
url: /net/render-table-from-the-data-source/
description: דף זה מסביר איך ניתן ליצור טבלה ממקור נתונים באמצעות ספריית Aspose.PDF.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Aspose.PDF מאפשר לך ליצור טבלה עם מקור נתונים מ-DataSet, DataTable, מערכים ואובייקטים המיישמים את הממשק IEnumerable באמצעות המחלקה PdfLightTable.

ה[מחלקה Table](https://reference.aspose.com/pdf/net/aspose.pdf/table) משמשת לעיבוד טבלאות. מחלקה זו נותנת לנו את היכולת ליצור טבלאות ולמקם אותן במסמך, באמצעות [שורות](https://reference.aspose.com/pdf/net/aspose.pdf/rows) ו[תאים](https://reference.aspose.com/pdf/net/aspose.pdf/cell). אז, כדי ליצור את הטבלה, עליך להוסיף את מספר השורות הנדרש ולמלא אותן במספר התאים המתאים.

הדוגמה הבאה יוצרת טבלה 4x10.

```csharp
var table = new Table
    {
        // הגדרת רוחב עמודות אוטומטית לטבלה
        ColumnWidths = "25% 25% 25% 25%",
        // הגדרת ריפוד לתא
        DefaultCellPadding = new MarginInfo(10, 5, 10, 5), // שמאל תחתון ימין עליון
        // הגדרת צבע גבול הטבלה לירוק
        Border = new BorderInfo(BorderSide.All, .5f, Color.Green),
        // הגדרת גבול לתאי הטבלה בצבע שחור
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
    // הוספת אובייקט הטבלה לעמוד הראשון של המסמך
    document.Pages[1].Paragraphs.Add(table);
```
בעת אתחול אובייקט הטבלה, נעשה שימוש בהגדרות עיצוב מינימליות:

* [ColumnWidths](https://reference.aspose.com/pdf/net/aspose.pdf/table/properties/columnwidths) - רוחב העמודות (כברירת מחדל);
* [DefaultCellPadding](https://reference.aspose.com/pdf/net/aspose.pdf/table/properties/defaultcellpadding) - השדות המוגדרים כברירת מחדל לתאי השולחן;
* [Border](https://reference.aspose.com/pdf/net/aspose.pdf/table/properties/border) - מאפייני מסגרת השולחן (סגנון, עובי, צבע);
* [DefaultCellBorder](https://reference.aspose.com/pdf/net/aspose.pdf/table/properties/defaultcellborder) - מאפייני מסגרת התא (סגנון, עובי, צבע).

## ייצוא נתונים ממערך של אובייקטים

המחלקה Table מספקת שיטות לאינטראקציה עם מקורות נתונים של ADO.NET - [ImportDataTable](https://reference.aspose.com/pdf/net/aspose.pdf.table/importdatatable/methods/1) ו-[ImportDataView](https://reference.aspose.com/pdf/net/aspose.pdf/table/methods/importdataview).

בהנחה שאובייקטים אלו אינם נוחים במיוחד לעבודה בתבנית MVC, נסתפק בדוגמה קצרה. בדוגמה זו (שורה 50), המתודה ImportDataTable נקראת ומקבלת כפרמטרים מופע של DataTable והגדרות נוספות כמו דגל כותרת ומיקום התחלתי (שורות/עמודות) לפלט הנתונים.

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
    // הגדרת ריפוד התאים
    DefaultCellPadding = new MarginInfo(10, 5, 10, 5), // שמאל תחתון ימין עליון
    // הגדרת צבע גבול הטבלה לירוק
    Border = new BorderInfo(BorderSide.All, .5f, Color.Green),
    // הגדרת הגבול לתאי הטבלה בשחור
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

