---
title: ייצוא טופס
type: docs
weight: 60
url: /net/plugins/formflattener/
description: כיצד להשטיח שדות טופס בקבצי PDF באמצעות תוסף FormFlattener של Aspose.PDF
lastmod: "2024-01-24"
---

במאמר זה, נראה לכם כיצד להשתמש ב-[תוסף FormFlattener](https://products.aspose.org/pdf/net/form-flattener/), שיכול להשטיח שדות טופס בקבצי PDF.

## דרישות מוקדמות

תזדקקו לדברים הבאים:

* Visual Studio 2019 או גרסה מאוחרת יותר
* Aspose.PDF עבור .NET 21.1 או גרסה מאוחרת יותר
* קובץ PDF לדוגמא המכיל כמה שדות טופס

ניתן להוריד את ספריית Aspose.PDF עבור .NET מהאתר הרשמי או להתקין אותם באמצעות מנהל החבילות NuGet ב-Visual Studio.

## שלבים

השלבים הבסיסיים להשטחת שדות טופס בקבצי PDF באמצעות תוסף FormFlattener הם:

1. צור אובייקט של המחלקה FormFlattener
1. צור אובייקט של המחלקה FormFlattenAllFieldsOptions או FormFlattenSelectedFieldsOptions, תלוי אם ברצונך להשטיח את כל השדות או חלק מהם
1.
1. הרץ את שיטת Process של אובייקט FormFlattener

בואו נראה כיצד לממש את השלבים הללו בקוד C#.

### שלב 1: צור אובייקט של הכיתה FormFlattener

הכיתה FormFlattener היא הכיתה העיקרית המספקת את הפונקציונליות של החלקת שדות טופס בקבצי PDF. כדי להשתמש בה, עליך ליצור מופע שלה באמצעות הבנאי המוגדר כברירת מחדל:

```cs
// צור מופע של התוסף FormFlattener
var plugin = new FormFlattener();
```

### שלב 2: צור אובייקט של הכיתה FormFlattenAllFieldsOptions או FormFlattenSelectedFieldsOptions, תלוי אם ברצונך להחליק את כל השדות או חלק מהם

הכיתות FormFlattenAllFieldsOptions ו-FormFlattenSelectedFieldsOptions הן כיתות עזר המאפשרות לך לציין אפשרויות ופרמטרים שונים עבור תהליך ההחלקה.
מחלקות FormFlattenAllFieldsOptions ו-FormFlattenSelectedFieldsOptions הן מחלקות עזר שמאפשרות לך לציין אפשרויות ופרמטרים שונים עבור תהליך ההחלקה.

```cs
// יצירת אפשרויות להחלקת כל השדות
var options = new FormFlattenAllFieldsOptions();
```

כדי להחליק רק את שדות הטופס שהקואורדינטה התחתית-שמאלית x שלהם גדולה מ-300, ניתן להשתמש בקוד הבא:

```cs
// יצירת אפשרויות להחלקת שדות נבחרים
var options = new FormFlattenSelectedFieldsOptions((field) => field.Rect.LLX > 300);
```

### שלב 3: הוספת מקורות הנתונים הקלט והפלט לאובייקט האפשרויות

מקורות הנתונים הקלט והפלט הם קבצי PDF שברצונך להחליק ולשמור.
מקורות הנתונים הקלט והפלט הם קובצי PDF שברצונך להחליק ולשמור.

```cs
// הוספת מקורות נתוני קלט ופלט לאפשרויות
options.Inputs.Add(new FileDataSource("sample.pdf"));
options.Outputs.Add(new FileDataSource("sample-flat.pdf"));
```

### שלב 4: הרצת שיטת ה-Process של אובייקט FormFlattener

השלב הסופי הוא להריץ את שיטת ה-Process של אובייקט ה-FormFlattener, תוך העברת אובייקט האפשרויות כפרמטר. שיטה זו תבצע את תהליך ההחלקה ותחזיר אובייקט ResultContainer, המכיל את תוצאות התהליך, כגון הסטטוס, ההודעות, מקורות הנתונים הפלט וכו'. ניתן לגשת לתוצאות באמצעות התכונות והשיטות של מחלקת ResultContainer. לדוגמה, כדי לקבל את התוצאה הראשונה מאוסף התוצאות ולהדפיס אותה לקונסול, ניתן להשתמש בקוד הבא:

```cs
// עיבוד האפשרויות וקבלת המיכל תוצאה
var resultContainer = plugin.Process(options);

// קבלת התוצאה הראשונה ממיכל התוצאה
var result = resultContainer.ResultCollection[0];

// הדפסת התוצאה
Console.WriteLine(result);
```
```
התוצאה תכיל מידע כגון נתיבי קבצים פלט.
```
