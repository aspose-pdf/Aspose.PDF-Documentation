---
title: Form Exporter
type: docs
weight: 50
url: /net/plugins/formexpoter/
description: כיצד לייצא ערכי שדות טופס לקבצי CSV באמצעות תוסף Aspose.PDF Form Exporter
lastmod: "2024-01-24"
draft: false
---

במאמר זה נראה לכם כיצד להשתמש ב[תוסף Form Exporter](https://products.aspose.org/pdf/net/form-exporter/), המאפשר ייצוא ערכי שדות טופס מקבצי PDF לקבצי CSV.

## דרישות מוקדמות

תזדקק לפריטים הבאים:

* Visual Studio 2019 או מאוחר יותר
* Aspose.PDF עבור .NET 21.1 או מאוחר יותר
* קובץ PDF לדוגמה המכיל כמה שדות טופס

ניתן להוריד את ספריית Aspose.PDF עבור .NET מהאתר הרשמי או להתקינה באמצעות מנהל חבילות NuGet ב-Visual Studio.

## שלבים

השלבים הבסיסיים לייצוא ערכי שדות טופס לקבצי CSV באמצעות התוסף FormExporter הם:

1. יצירת אובייקט מסוג `FormExporter`
1. יצירת אובייקט מסוג `FormExporterValuesToCsvOptions` והגדרת הפרדיקט והמפריד
1.
1.
1. הפעל את המתודה `Process` של אובייקט `FormExporter`

בואו נראה איך לממש את השלבים האלה בקוד C#.

### שלב 1: יצירת אובייקט של המחלקה FormExporter

מחלקת FormExporter היא המחלקה הראשית שמספקת את הפונקציונליות של ייצוא ערכי שדות טופס לקבצי CSV. כדי להשתמש בה, עליך ליצור מופע שלה באמצעות הבנאי המוגדר כברירת מחדל:

```cs
// יצירת מופע של תוסף FormExporter
var plugin = new FormExporter();
```

### שלב 2: יצירת אובייקט של המחלקה FormExporterValuesToCsvOptions וציון הפרדיקט והמפריד

מחלקת FormExporterValuesToCsvOptions היא מחלקת עזר שמאפשרת לך לציין אפשרויות ופרמטרים שונים לתהליך הייצוא, כמו הפרדיקט והמפריד.
מחלקת FormExporterValuesToCsvOptions היא מחלקת עזר שמאפשרת לך לציין אפשרויות ופרמטרים שונים לתהליך הייצוא, כמו הפרדיקט והמפריד.

```cs
// יצירת אפשרויות לייצוא ערכי שדות טופס ל-CSV
var options = new FormExporterValuesToCsvOptions(
(field) => { return field is TextBoxField && field.PageIndex == 2; }, ';');
```

### שלב 3: הוסף את מקורות הנתונים הקלט והפלט לאובייקט האפשרויות

מקורות הנתונים הקלט והפלט הם קבצי ה-PDF שברצונך לייצא מהם וקובץ ה-CSV שברצונך לשמור.
מקורות הנתונים לקלט ולפלט הם קבצי PDF שברצונך לייצא מהם וקובץ CSV שברצונך לשמור.

```cs
// הוספת קבצי הקלט והפלט לאפשרויות
options.AddInput(new FileDataSource("inputFileNameWithFields-1.pdf"));
options.AddInput(new FileDataSource("inputFileNameWithFields-2.pdf"));
options.AddInput(new FileDataSource("inputFileNameWithFields-3.pdf"));
options.AddInput(new FileDataSource("inputFileNameWithFields-4.pdf"));
options.AddOutput(new FileDataSource("outputFileName.csv"));

```

### שלב 4: הפעלת המתודה Process של אובייקט FormExporter

השלב הסופי הוא להפעיל את המתודה Process של אובייקט FormExporter, תוך העברת אובייקט האפשרויות כפרמטר.
השלב הסופי הוא להריץ את שיטת Process של אובייקט FormExporter, תוך העברת אובייקט האפשרויות כפרמטר.

```cs
// עיבוד ערכי השדות בטופס באמצעות התוסף
var resultContainer = plugin.Process(options);
var result = resultContainer.ResultCollection[0];
Console.WriteLine(result);

```

התוצאה תכיל מידע כמו נתיבי הקובץ לקלט ולפלט.
