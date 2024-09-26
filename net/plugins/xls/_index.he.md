---
title: XLS Converter
type: docs
weight: 20
url: /net/plugins/xls/
description: כיצד להמיר קבצי PDF לגיליונות אקסל באמצעות תוספי Aspose.Pdf
lastmod: "2024-01-24"
---

{{% alert color="primary" %}}

במאמר זה, נראה לכם כיצד להשתמש בתוסף [PdfXls](https://products.aspose.org/pdf/net/xls-converter/), שיכול להמיר קבצי PDF לפורמט Excel עם נאמנות ודיוק גבוהים.

{{% /alert %}}

## דרישות מוקדמות

תזדקקו לדברים הבאים:

* Visual Studio 2019 או גרסה מאוחרת יותר
* Aspose.PDF עבור .NET 24.1 או גרסה מאוחרת יותר
* קובץ PDF לדוגמה שברצונכם להמיר לפורמט Excel

ניתן להוריד את ספריית Aspose.PDF עבור .NET מהאתר הרשמי או להתקין אותה באמצעות ניהול חבילות NuGet ב-Visual Studio.

## שלבים

השלבים הבסיסיים להמרת קובץ PDF לפורמט Excel באמצעות התוסף PdfXls הם:

1. יצירת אובייקט מסוג PdfXls
1. הוספת מקורות הנתונים הקלט והפלט לאובייקט PdfToXlsOptions
1. הפעלת השיטה Process של אובייקט ה-PdfXls

בואו נראה כיצד לממש את השלבים הללו בקוד C#.
בואו נראה איך ליישם את השלבים הללו בקוד C#.

### שלב 1: יצירת אובייקט של המחלקה PdfXls

מחלקת PdfXls היא המחלקה הראשית שמספקת את הפונקציונליות של המרת PDF ל-Excel. כדי להשתמש בה, עליך ליצור מופע שלה באמצעות הבנאי המוגדר כברירת מחדל:

```csharp
// יצירת מופע של התוסף PdfXls
var plugin = new PdfXls();
```

### שלב 2: הוספת מקורות הנתונים לקלט ולפלט לאובייקט PdfToXlsOptions

מחלקת PdfToXlsOptions היא מחלקת עזר שמאפשרת לך לציין אפשרויות ופרמטרים שונים עבור תהליך ההמרה. כדי להשתמש בה, עליך ליצור מופע שלה ולהוסיף את מקורות הנתונים לקלט ולפלט באמצעות השיטות `AddInput` ו-`AddOutput`. מקורות הנתונים יכולים להיות נתיבי קבצים או זרמים. לדוגמה, כדי להמיר קובץ PDF בשם `sample.pdf` בתיקיית `C:\Samples` לקובץ Excel בשם `sample.xlsx` באותה תיקייה, תוכל להשתמש בקוד הבא:

```csharp
// ציון נתיבי הקבצים לקלט ולפלט
var inputPath = Path.Combine(@"C:\Samples\", "sample.pdf");
var outputPath = Path.Combine(@"C:\Samples\", "sample.xlsx");

// יצירת מופע של מחלקת PdfToXlsOptions
var options = new PdfToXlsOptions();

// הוספת נתיבי הקבצים לקלט ולפלט לאופציות
options.AddInput(new FileDataSource(inputPath));
options.AddOutput(new FileDataSource(outputPath));
```
ניתן גם להגדיר אפשרויות נוספות, כגון פורמט הפלט, טווח הדפים, שם גיליון העבודה וכו' באמצעות מאפייני מחלקת PdfToXlsOptions. לדוגמה, כדי להמיר את קובץ ה-PDF לפורמט XLSX, להכניס עמודה ריקה במיקום הראשון ולתת לגיליון העבודה את השם "MySheet", ניתן להשתמש בקוד הבא:

```csharp
// הגדרת פורמט הפלט ל-XLSX
options.Format = PdfToXlsOptions.ExcelFormat.XLSX;

// הוספת עמודה ריקה במיקום הראשון
options.InsertBlankColumnAtFirst = true;
```

### שלב 3: הפעלת שיטת ה-Process של אובייקט PdfXls

השלב הסופי הוא להפעיל את שיטת ה-Process של אובייקט ה-PdfXls, תוך העברת אובייקט PdfToXlsOptions כפרמטר.
שלב הסיום הוא להריץ את המתודה Process של האובייקט PdfXls, כשמועבר אליה האובייקט PdfToXlsOptions כפרמטר.

```csharp
// עיבוד ההמרה מ-PDF ל-Excel באמצעות התוסף והאפשרויות
var resultContainer = plugin.Process(options);

// קבלת התוצאה הראשונה מאוסף התוצאות
var result = resultContainer.ResultCollection[0];

// הדפסת התוצאה
Console.WriteLine(result);
```

התוצאה תכיל מידע כגון נתיבי הקבצים המוצאיים.
