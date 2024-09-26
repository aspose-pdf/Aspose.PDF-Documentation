---
title: מחולל טבלאות
type: docs
weight: 130
url: /net/plugins/tablegenerator/
description: מאפשר הוספה/הכנסה של טבלה במספר עמוד מצוין במסמך PDF.
lastmod: "2024-01-24"
draft: false
---

האם אתה צריך ליצור טבלאות דינמיות ומושכות במסמכי PDF שלך באמצעות .NET? Aspose.PDF עבור .NET מספק מחלקת TableGenerator עוצמתית שמפשטת את התהליך. בפרק זה, נעבור על השלבים ליצירת טבלאות במסמך PDF באמצעות [Aspose.PDF Table Generator](https://products.aspose.org/pdf/net/table-generator/), מיצירת מסמך דגמה ועד יצירת טבלאות עם מחלקת TableGenerator.
בואו נצלול פנימה ונלמד כיצד ליצור טבלאות שלב אחר שלב.

## דרישות מוקדמות

תזדקק לדברים הבאים:

* Visual Studio 2019 או מאוחר יותר
* Aspose.PDF עבור .NET 24.3 או מאוחר יותר
* קובץ PDF לדוגמא

## יצירת מסמך דגמה

לפני שנתחיל ביצירת טבלאות, בואו ניצור מסמך דגמה עם עמודים ריקים שבהם יוכנסו הטבלאות שלנו.
לפני שנתחיל ביצירת טבלאות, בואו ניצור מסמך דמו עם דפים ריקים שבהם יוכנסו הטבלאות שלנו.

* צור מסמך PDF חדש.
* הוסף דפים ריקים למסמך.
* שמור את המסמך לקובץ המוגדר.

```cs
// <summary>
// יוצר מסמך דמו עם דפים ריקים.
//
// פרמטרים:
// - fileName: הנתיב ושם הקובץ המוצא.
// </summary>
internal static void CreateDemoDocument(string fileName)
{
    // צור מסמך PDF חדש.
    var document = new Aspose.Pdf.Document();

    // הוסף ארבעה דפים ריקים למסמך.
    for (int i = 0; i < 2; i++)
    {
        document.Pages.Add();
    }

    // שמור את המסמך לקובץ המוגדר.
    document.Save(fileName);
}
```

## יצירת טבלאות

לאחר שהמסמך הדמו שלנו מוכן, אנו יכולים להתחיל לייצר טבלאות באמצעות המחלקה `TableGenerator`. הקטע הבא מדגים כיצד לייצר טבלאות עם סוגי תוכן ואופציות עיצוב שונות. הנה איך לייצר טבלאות:

* צור מופע חדש של המחלקה `TableGenerator`.
* צור מופע חדש של המחלקה `TableGenerator`.
* צור אפשרויות טבלה וציין מקורות קלט ופלט לקבצים.
* הוסף טבלאות עם שורות ותאים לאפשרויות, תוך ציון תוכן ועיצוב.
* בצע את יצירת הטבלה באמצעות השיטה `Process` וקבל את מיכל התוצאות.

### יצירת טבלאות

כדי ליצור טבלה באמצעות Aspose.PDF, עקוב אחר השלבים הבאים:

```cs
// צור מופע חדש של המחלקה TableGenerator.
var generator = new TableGenerator();

// צור אפשרויות טבלה והוסף טבלאות לדוגמה.
var options = new TableOptions();

// הוסף מקורות קובץ קלט ופלט לאפשרויות.
options.AddInput(new FileDataSource(@"C:\Samples\Results\table-generator-demo.pdf"));
options.AddOutput(new FileDataSource(@"C:\Samples\Results\table-generator-demo.pdf"));

// הוסף את הטבלה הראשונה לאפשרויות.
options
    .InsertPageAfter(1)
    .AddTable()
```

בקוד לעיל, אנו יוצרים מופע של `TableOptions` ומציינים מקורות קלט ופלט למסמך PDF.
בקוד שלעיל, אנו יוצרים מופע של `TableOptions` ומציינים מקורות קלט ופלט לנתוני הקובץ של מסמך PDF.

### הוספת תוכן לטבלאות

לאחר שהטבלה נוצרה, ניתן למלא אותה בשורות ותאים המכילים סוגים שונים של תוכן, כמו טקסט, HTML, תמונות וכו'. כך תוכל להוסיף תוכן לטבלה:

```csharp
options
    .AddTable()
        .AddRow()
            .AddCell()
                .AddParagraph(new HtmlFragment("<h1>כותרת 1</h1>")) // הוספת תוכן HTML לתא.
            .AddCell()
                .AddParagraph(new HtmlFragment("<h2>כותרת 2</h2>"))
            .AddCell()
                .AddParagraph(new HtmlFragment("<h3>כותרת 3</h3>"));
```

בדוגמא זו, אנו מוסיפים שורה לטבלה וממלאים אותה בתאים המכילים קטעי HTML המייצגים כותרות.

שיטות שימושיות:

* **InsertPageAfter**: מוסיף דף לאחר מספר הדף המצוין.
* **InsertPageBefore**: מוסיף דף לפני מספר הדף המצוין.
* **AddTable**: מוסיף טבלה למסמך.
* **AddTable**: הוספת טבלה למסמך.
* **AddRow**: הוספת שורה לטבלה.
* **AddCell**: הוספת תאים לשורה.
* **AddParagraph**: הוספת תוכן לתא.

ניתן להוסיף את סוגי התוכן הבאים כפסקה:

* **HtmlFragment** - תוכן המבוסס על סימון HTML
* **TeXFragment** - תוכן המבוסס על סימון TeX/LaTeX
* **TextFragment** - תוכן טקסט פשוט
* **Image** - גרפיקה

## ביצוע יצירת טבלה

לאחר הוספת התוכן, נוכל להתחיל ביצירת הטבלה.

```cs
// תהליך יצירת הטבלה וקבלת המיכל לתוצאות.
var resultContainer = generator.Process(options);

// הדפסת מספר התוצאות באוסף התוצאות.            
Console.WriteLine(resultContainer.ResultCollection.Count);
```

המתודה `Process` מבצעת יצירת טבלה. ניתן גם להקיף את המתודה זו ב-try-catch כדי לטפל בשגיאות.

להלן הקוד המלא של הדוגמה:

```cs
using Aspose.Pdf;
using Aspose.Pdf.Plugins;
using Aspose.Pdf.Text;

namespace AsposePluginsNet8.Documentation
{
    // <summary>
    // מייצג מחלקה המדגימה שימוש ביצירת טבלה ב-Aspose.Pdf.
    // </summary>
    internal static class TableDemo
    {
        // <summary>
        // מפעיל את דוגמת יצירת הטבלה.
        // </summary>
        internal static void Run()
        {
            // יצירת מסמך דוגמה ויצירת טבלאות.
            CreateDemoDocument(@"C:\Samples\Results\table-generator-demo.pdf");
            CreateDemoTable();
        }

        // <summary>
        // יוצר מסמך דוגמה עם ארבע דפים ריקים.
        //
        // פרמטרים:
        // - fileName: הנתיב ושם קובץ הפלט.
        // </summary>
        internal static void CreateDemoDocument(string fileName)
        {
            // יצירת מסמך PDF חדש.
            var document = new Aspose.Pdf.Document();

            // הוספת ארבעה דפים ריקים למסמך.
            for (int i = 0; i < 2; i++)
            {
                document.Pages.Add();
            }

            // שמירת המסמך בקובץ המצוין.
            document.Save(fileName);
        }

        // <summary>
        // יוצר טבלאות באמצעות מחלקת TableGenerator.
        // </summary>
        internal static void CreateDemoTable()
        {
            // יצירת מופע חדש של מחלקת TableGenerator.
            var generator = new TableGenerator();

            // יצירת אפשרויות טבלה והוספת טבלאות דוגמה.
            var options = new TableOptions();

            // הוספת מקורות נתונים של קובץ קלט וקובץ פלט לאפשרויות.
            options.AddInput(new FileDataSource(@"C:\Samples\Results\table-generator-demo.pdf"));
            options.AddOutput(new FileDataSource(@"C:\Samples\Results\table-generator-demo.pdf"));

            // הוספת הטבלה הראשונה לאפשרויות.
            options
                .InsertPageAfter(1)
                .AddTable()
                    .AddRow()
                        .AddCell()
                            .AddParagraph(new HtmlFragment("<h1>Header 1</h1>"))
                        .AddCell()
                            .AddParagraph(new HtmlFragment("<h2>Header 2</h2>"))
                        .AddCell()
                            .AddParagraph(new HtmlFragment("<h3>Header 3</h3>"))
                    .AddRow()
                        .AddCell()
                            .AddParagraph(new TeXFragment("{\\small The equation $E=mc^2$, discovered in 1905 by Albert Einstein.}", true))
                        .AddCell()
                            .AddParagraph(new TextFragment("Cell 2 2"))
                        .AddCell()
                            .AddParagraph(new TextFragment("Cell 2 3"))
                    .AddRow()
                        .AddCell()
                            .AddParagraph(new TextFragment("Cell 3 1a"))
                            .AddParagraph(new TextFragment("Cell 3 1b"))
                        .AddCell()
                            .AddParagraph(new TextFragment("Cell 3 2"))
                        .AddCell()
                            .AddParagraph(new TextFragment("Cell 3 3"));

            // הוספת הטבלה השנייה לאפשרויות.
            options
                .InsertPageBefore(2)
                .AddTable()
                    .AddRow()
                        .AddCell()
                            .AddParagraph(new TextFragment("Header 1 1"))
                        .AddCell()
                            .AddParagraph(new TextFragment("Header 1 2"))
                        .AddCell()
                            .AddParagraph(new TextFragment("Header 1 3"))
                    .AddRow()
                        .AddCell()
                            .AddParagraph(new Image()
                            {
                                File = @"C:\Samples\logo.png",
                                FixWidth = 75,
                                FixHeight = 75,
                            })
                        .AddCell()
                            .AddParagraph(new Image()
                            {
                                File = @"C:\Samples\sample.svg",
                                FileType = ImageFileType.Svg,
                                FixWidth = 75,
                                FixHeight = 75
                            })
                        .AddCell()
                            .AddParagraph(new Image()
                            {
                                ImageStream = File.OpenRead(@"C:\Samples\Conversion\Demo.dcm"),
                                FileType = ImageFileType.Dicom,
                                FixWidth = 75,
                                FixHeight = 75
                            });

            // תהליך יצירת הטבלה וקבלת המיכל לתוצאות.
            var resultContainer = generator.Process(options);

            // הדפסת מספר התוצאות באוסף התוצאות.
            Console.WriteLine(resultContainer.ResultCollection.Count);
        }
    }
}
```

