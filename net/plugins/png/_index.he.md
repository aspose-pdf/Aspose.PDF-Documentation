---
title: ממיר PNG
type: docs
weight: 110
url: /net/plugins/png/
description: המרת מסמכי PDF לתמונות PNG באמצעות תוסף Aspose.PDF PNG
lastmod: "2024-01-24"
---

אם אתה מחפש ל[המיר מסמכי PDF לתמונות PNG](https://products.aspose.org/pdf/net/png-converter/) באמצעות .NET, Aspose.PDF עבור .NET מספק פתרון חזק. במאמר זה נעבור על השלבים החיוניים ליצירת אובייקט, הוספת מקור נתונים והפעלת השיטה process באמצעות ספריית Aspose.PDF.

## דרישות מוקדמות

תצטרך את הדברים הבאים:

* Visual Studio 2019 או מאוחר יותר
* Aspose.PDF עבור .NET 24.1 או מאוחר יותר
* קובץ PDF לדוגמא

## סקירת קוד

הקוד להלן מדגים דוגמא להמרת PNG באמצעות תוסף Aspose.PDF PNG:

```csharp
using Aspose.Pdf.Plugins;

//....

// צור מופע חדש של המחלקה PngOptions.
var convertorOptions = new PngOptions();

// הוסף את נתיבי הקלט והפלט ל-PngOptions.
convertorOptions.AddInput(new FileDataSource(Path.Combine(@"C:\Samples\", "sample.pdf")));
convertorOptions.AddOutput(new FileDataSource(Path.Combine(@"C:\Samples\", "images")));

// הגדר את רזולוציית הפלט ל-300 DPI.
convertorOptions.OutputResolution = 300;

// צור מופע חדש של המחלקה Png.
Png converter = new ();

// תהליך המרת ה-PNG וקבל את תוצאות המיכל.
ResultContainer resultContainer = converter.Process(convertorOptions);

// הדפס את התוצאה לקונסול.
foreach (FileResult operationResult in resultContainer.ResultCollection.Cast<FileResult>())
{
      Console.WriteLine(operationResult.Data.ToString());
}
```
בואו נפרט את השלבים המרכזיים:

1. **יצירת אובייקט (PngOptions ו-Png)**

   הקוד מתחיל ביצירת מופע של המחלקה `PngOptions` כדי להגדיר את המרת ה-PNG. בנוסף, מופע של המחלקה `Png` נוצר לעיבוד נוסף.

2. **הוספת מקור נתונים**

   נתיב קובץ PDF קלט מתווסף ל-`PngOptions` באמצעות השיטה `AddInput`. באופן דומה, נתיב הפלט עבור תמונות PNG מתווסף באמצעות השיטה `AddOutput`.

3. **הגדרת רזולוציית פלט**

   הקוד מגדיר את רזולוציית הפלט ל-300 DPI באמצעות התכונה `OutputResolution` של המחלקה `PngOptions`.

4. **הפעלת שיטת Process**

   המרת ה-PNG מתחילה על ידי קריאה לשיטה `Process` במחלקה `Png`, עם ה-`PngOptions` שהוגדרו. התוצאה נשמרת ב-`resultContainer`.

5. **טיפול בתוצאה**

   הקוד מדפיס את התוצאה לקונסולה, מציג את נתיב(י) הקובץ שהומר.
