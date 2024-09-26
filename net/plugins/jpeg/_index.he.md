---
title: ממיר JPEG
type: docs
weight: 90
url: /net/plugins/jpeg/
description: איך להמיר דפי PDF לתמונות JPEG באמצעות ממיר JPEG של Aspose.PDF
lastmod: "2024-01-24"
draft: false
---

במאמר זה נראה לכם איך להשתמש ב[ממיר JPEG](https://products.aspose.org/pdf/net/jpeg-converter/), שיכול להמיר דפי PDF לתמונות JPEG ולשמור אותם כקבצים נפרדים.

## דרישות מוקדמות

תצטרכו את הדברים הבאים:

* Visual Studio 2019 או גרסה מאוחרת יותר
* Aspose.PDF עבור .NET 24.1 או גרסה מאוחרת יותר
* קובץ PDF לדוגמא שמכיל כמה דפים

ניתן להוריד את ספריית Aspose.PDF עבור .NET מהאתר הרשמי או להתקין אותה באמצעות מנהל חבילות NuGet ב-Visual Studio.

## שלבים

השלבים הבסיסיים להמרת דפי PDF לתמונות JPEG באמצעות ממיר ה-JPEG הם:

1. יצירת אובייקט של המחלקה Jpeg
1. יצירת אובייקט של המחלקה JpegOptions והוספת נתיבי הקלט והפלט
1. הפעלת המתודה Process של אובייקט ה-Jpeg וקבלת תוכן התוצאה
1.
1.

בואו נראה איך לממש את השלבים האלה בקוד C#.

### שלב 1: יצירת אובייקט של המחלקה Jpeg

מחלקת Jpeg היא המחלקה העיקרית שמספקת את הפונקציונליות של המרת דפי PDF לתמונות JPEG. כדי להשתמש בה, עליך ליצור מופע שלה באמצעות הבנאי המוגדר כברירת מחדל:

```cs
// יצירת מופע חדש של Jpeg
var converter = new Jpeg();
```

### שלב 2: יצירת אובייקט של המחלקה JpegOptions והוספת נתיבי הקבצים לקלט ולפלט

מחלקת JpegOptions היא מחלקת עזר שמאפשרת לך לציין אופציות ופרמטרים שונים עבור תהליך ההמרה, כגון רזולוציית הפלט, טווח הדפים, איכות התמונה וכו'.
מחלקת JpegOptions היא מחלקת עזר שמאפשרת לך לציין אפשרויות ופרמטרים שונים עבור תהליך ההמרה, כגון רזולוציית הפלט, טווח הדפים, איכות התמונה וכו'.

```cs
// ציון נתיבי הקלט והפלט
var inputPath = Path.Combine(@"C:\Samples\", "sample.pdf");
var outputPath = Path.Combine(@"C:\Samples\", "images");

// יצירת מופע של מחלקת JpegOptions
var converterOptions = new JpegOptions();

// הוספת נתיבי הקלט והפלט לאפשרויות
converterOptions.AddInput(new FileDataSource(inputPath));
converterOptions.AddOutput(new FileDataSource(outputPath));
```

ניתן גם להגדיר אפשרויות נוספות, כמו רזולוציית הפלט, טווח הדפים, איכות התמונה וכו' באמצעות התכונות של מחלקת JpegOptions. לדוגמה, כדי להמיר רק את הדף הראשון של קובץ ה-PDF לתמונת JPEG עם רזולוציה של 300 dpi, ניתן להשתמש בקוד הבא:

```cs
// הגדרת רזולוציית הפלט ל-300 dpi
converterOptions.OutputResolution = 300;

// הגדרת טווח הדפים לדף הראשון
converterOptions.PageRange = new PageRange(1);
```
### שלב 3: הפעל את שיטת ה-Process של אובייקט ה-Jpeg וקבל את מיכל התוצאות

השלב האחרון הוא להפעיל את שיטת ה-Process של אובייקט ה-Jpeg, תוך העברת אובייקט converterOptions כפרמטר. שיטה זו תבצע את ההמרה ותחזיר אובייקט ResultContainer, שמכיל את תוצאות ההמרה, כגון הסטטוס, ההודעות, נתיבי הקבצים המוצאים וכו'. ניתן לגשת לתוצאות באמצעות התכונות והשיטות של מחלקת ResultContainer. לדוגמה, כדי לקבל את מיכל התוצאות ולהדפיס את מצב ההמרה, ניתן להשתמש בקוד הבא:

```cs
// תהליך ההמרה וקבלת מיכל התוצאות
ResultContainer resultContainer = converter.Process(converterOptions);

// הדפסת מצב ההמרה
Console.WriteLine(resultContainer.Status);
```

המצב של ההמרה יכול להיות הצלחה או כישלון, תלוי אם ההמרה הושלמה בהצלחה או לא.

### שלב 4: הדפס את נתיבי התמונות ה-JPEG שהומרו

מיכל התוצאות מכיל אוסף של תוצאות, כל אחת עבור נתיב קובץ פלט.
תוכן התוצאות כולל אוסף של תוצאות, אחת לכל נתיב קובץ פלט.

```cs
// הדפס את נתיבי התמונות JPEG שהומרו
foreach (FileResult operationResult in resultContainer.ResultCollection.Cast<FileResult>())
{
  Console.WriteLine(operationResult.Data.ToString());
}
```

נתיבי הקבצים המוצא יהיו בפורמט של {outputPath}{pageNumber}.jpg, כאשר {outputPath} הוא ספריית הפלט ו-{pageNumber} הוא מספר העמוד בקובץ PDF. לדוגמה, אם ספריית הפלט היא C:\Samples\images ולקובץ PDF יש שלושה עמודים, נתיבי הקבצים המוצא יהיו:

```text
C:\Samples\images\1.jpg
C:\Samples\images\2.jpg
C:\Samples\images\3.jpg
```
