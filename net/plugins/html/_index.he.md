---
title: ממיר HTML
type: docs
weight: 70
url: /net/plugins/html/
description: איך להמיר קבצי PDF ל-HTML ומ-HTML באמצעות תוסף PdfHtml של Aspose.PDF
lastmod: "2024-01-24"
draft: false
---

במאמר זה, נראה לכם איך להשתמש ב[תוסף PdfHtml](https://products.aspose.org/pdf/net/html-converter/), שיכול להמיר קבצי PDF ל-HTML ולהפך.

## דרישות מוקדמות

תזדקקו לדברים הבאים:

* Visual Studio 2019 או מאוחר יותר
* Aspose.PDF עבור .NET 21.1 או מאוחר יותר
* קובץ PDF לדוגמה וקובץ HTML לדוגמה

ניתן להוריד את ספריית Aspose.PDF עבור .NET מהאתר הרשמי או להתקין אותה באמצעות מנהל החבילות NuGet ב-Visual Studio.

## שלבים

השלבים הבסיסיים להמרת קבצי PDF ל-HTML ולהפך באמצעות תוסף PdfHtml הם:

1. יצירת אובייקט של המחלקה PdfHtml
2. יצירת אובייקט של המחלקה PdfToHtmlOptions או HtmlToPdfOptions, בהתאם לכיוון ההמרה
3. הוספת מקורות הנתונים לקלט ולפלט לאובייקט האופציות
4.
### שלב 1: יצירת אובייקט של הכיתה PdfHtml

הכיתה PdfHtml היא הכיתה המרכזית שמספקת את הפונקציונליות להמרת קבצי PDF ל-HTML ולהפך. כדי להשתמש בה, יש ליצור מופע שלה באמצעות הבנאי המוגדר כברירת מחדל:

```cs
// יצירת מופע של התוסף PdfHtml
var plugin = new PdfHtml();
```

### שלב 2: יצירת אובייקט של הכיתה PdfToHtmlOptions או HtmlToPdfOptions, תלוי בכיוון ההמרה

הכיתות PdfToHtmlOptions ו- HtmlToPdfOptions הן כיתות עוזרות המאפשרות לך לציין אופציות ופרמטרים שונים לתהליך ההמרה, כגון פורמט הפלט, טווח הדפים, הקידוד, הגופנים ועוד. כדי להשתמש בכיתות אלו, יש ליצור מופע של הכיתה המתאימה באמצעות הבנאי המוגדר כברירת מחדל או על ידי מעבר פרמטרים. לדוגמה, להמרת קובץ PDF לקובץ HTML עם משאבים מוטמעים, ניתן להשתמש בקוד הבא:

```cs
להמיר קובץ HTML לקובץ PDF עם הגדרות ברירת מחדל, תוכל להשתמש בקוד הבא:

```cs
// צור מופע חדש של מחלקת HtmlToPdfOptions
var options = new HtmlToPdfOptions();
```

ניתן גם להגדיר אפשרויות נוספות, כגון פורמט הפלט, טווח העמודים, הקידוד, הגופנים ועוד באמצעות המאפיינים של מחלקות האפשרויות. לדוגמה, להמיר קובץ PDF לקובץ HTML עם קידוד UTF-8 וגופן Arial, תוכל להשתמש בקוד הבא:

```cs
// צור מופע חדש של מחלקת PdfToHtmlOptions
var options = new PdfToHtmlOptions(PdfToHtmlOptions.SaveDataType.FileWithEmbeddedResources);

// הגדר את הקידוד ל-UTF-8
options.Encoding = Encoding.UTF8;

// הגדר את הגופן ל-Arial
options.Font = "Arial";
```

### שלב 3: הוסף את מקורות הנתונים לקלט ולפלט לאובייקט האפשרויות

מקורות הנתונים לקלט ולפלט הם קבצי ה-PDF או ה-HTML שברצונך להמיר ולשמור.
מקורות הקלט והפלט הם קבצי PDF או HTML שברצונך להמיר ולשמור.

```cs
// ציין את נתיבי הקלט והפלט
var inputPath = Path.Combine(@"C:\Samples\", "sample.pdf");
var outputPath = Path.Combine(@"C:\Samples\", "sample.html");

// הוסף את נתיבי הקלט והפלט לאפשרויות
options.AddInput(new FileDataSource(inputPath));
options.AddOutput(new FileDataSource(outputPath));
```

### שלב 4: הפעל את המתודה Process של האובייקט PdfHtml

השלב הסופי הוא להפעיל את המתודה Process של האובייקט PdfHtml, תוך העברת אובייקט האפשרויות כפרמטר. מתודה זו תבצע את ההמרה ותחזיר אובייקט ResultContainer, המכיל את תוצאות ההמרה, כגון הסטטוס, ההודעות, מקורות הנתונים הפלט ועוד. ניתן לגשת לתוצאות באמצעות התכונות והמתודות של מחלקת ResultContainer. לדוגמה, כדי לקבל את התוצאה הראשונה מאוסף התוצאות ולהדפיס אותה לקונסול, ניתן להשתמש בקוד הבא:

```cs
// תהליך ההמרה וקבלת קונטיינר התוצאות
var resultContainer = plugin.Process(options);

// קבל את התוצאה הראשונה מאוסף התוצאות
var result = resultContainer.ResultCollection[0];

// הדפס את התוצאה לקונסול
Console.WriteLine(result);
```
התוצאה תכיל מידע כגון נתיבי קבצים פלט.
