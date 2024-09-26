---
title: Merger
type: docs
weight: 100
url: /net/plugins/merger/
description: כיצד למזג מספר קבצי PDF לקובץ אחד באמצעות תוסף המיזוג של Aspose.PDF
lastmod: "2024-01-24"
---

במאמר זה, נראה לך כיצד להשתמש ב[תוסף המיזוג](https://products.aspose.org/pdf/net/merger/), שיכול למזג מספר קבצי PDF לקובץ אחד ולשמור אותו כקובץ חדש.

## דרישות מוקדמות

תזדקק לדברים הבאים:

* Visual Studio 2019 או מאוחר יותר
* Aspose.PDF עבור .NET 21.1 או מאוחר יותר
* שלושה קבצי PDF לדוגמה שברצונך למזג

ניתן להוריד את ספריית Aspose.PDF עבור .NET מהאתר הרשמי או להתקין אותם באמצעות מנהל החבילות NuGet ב-Visual Studio.

## שלבים

השלבים הבסיסיים למיזוג מספר קבצי PDF לקובץ אחד באמצעות תוסף המיזוג הם:

1. יצירת אובייקט של מחלקת Merger
2. יצירת אובייקט של מחלקת MergeOptions והוספת נתיבי הקבצים לקלט ולפלט
3. הפעלת המתודה Process של אובייקט ה-Merger

בואו נראה כיצד ליישם את השלבים הללו בקוד C#.

### שלב 1: יצירת אובייקט של מחלקת Merger
### שלב 1: יצירת אובייקט של מחלקת Merger

מחלקת Merger היא המחלקה העיקרית שמספקת את הפונקציונליות של מיזוג קבצי PDF רבים לקובץ אחד. כדי להשתמש בה, עליך ליצור מופע שלה באמצעות הבנאי המוגדר כברירת מחדל:

```cs
// יצירת מופע חדש של Merger
var pdfMerger = new Merger();
```

### שלב 2: יצירת אובייקט של מחלקת MergeOptions והוספת נתיבי הקבצים לקלט ולפלט

מחלקת MergeOptions היא מחלקת עזר שמאפשרת לך לציין אפשרויות ופרמטרים שונים לתהליך המיזוג, כגון טווח הדפים, הסדר, האבטחה וכו'.
כיתת MergeOptions היא כיתת עזר שמאפשרת לך לציין אופציות ופרמטרים שונים עבור תהליך המיזוג, כגון טווח הדפים, הסדר, האבטחה וכו'.

```cs
// ציין את נתיבי הקלט והפלט
string inputFilePath1 = Path.Combine(@"C:\Samples\", "sample1.pdf");
string inputFilePath2 = Path.Combine(@"C:\Samples\", "sample2.pdf");
string inputFilePath3 = Path.Combine(@"C:\Samples\", "sample3.pdf");
var outputFilePath = "TestMerge.pdf";

// צור מופע של כיתת MergeOptions
var mergeOptions = new MergeOptions();

// הוסף את נתיבי הקלט והפלט לאופציות
mergeOptions.Inputs.Add(new FileDataSource(inputFilePath1));
mergeOptions.Inputs.Add(new FileDataSource(inputFilePath2));
mergeOptions.Inputs.Add(new FileDataSource(inputFilePath3));
mergeOptions.AddOutput(new FileDataSource(outputFilePath));
```

### שלב 3: הפעל את המתודה Process של אובייקט Merger

השלב הסופי הוא להפעיל את המתודה Process של אובייקט ה-Merger, תוך העברת אובייקט mergeOptions כפרמטר.
השלב הסופי הוא להפעיל את המתודה Process של אובייקט Merger, תוך מעבר האובייקט mergeOptions כפרמטר.

```cs
// עיבוד המיזוג ושמירת הקובץ הממוזג
pdfMerger.Process(mergeOptions);

// הדפסת הודעת אישור
Console.WriteLine("קבצי ה-PDF נמזגו בהצלחה.");
```
