---
title: Optimizer 
type: docs
weight: 80
url: /net/plugins/optimizer/
description: איך למטב ולשנות קבצי PDF עם Aspose.PDF Optimizer
lastmod: "2024-01-24"
---

בפרק זה, נחקור איך להשתמש ב-[Aspose.PDF Optimizer](https://products.aspose.org/pdf/net/optimizer/) כדי למטב, לשנות גודל ולסובב קבצי PDF ביישומי C# שלך.
בואו נצלול פנימה ונלמד איך לבצע את המשימות הללו צעד אחר צעד.

## דרישות מוקדמות

תצטרך את הדברים הבאים:

* Visual Studio 2019 או מאוחר יותר
* Aspose.PDF ל-.NET 24.1 או מאוחר יותר
* קובץ PDF לדוגמה שמכיל שדות טופס מסוימים

## מיטוב קבצי PDF

מיטוב קובץ PDF כולל הקטנת גודלו ושיפור הביצועים. הקטעים הבאים מראים איך להשיג מטרה זו. הנה איך אתה יכול למטב קובץ PDF:

* צור מקור נתונים חדש לקובץ PDF הקלט.
* צור מקור נתונים חדש לקובץ ה-PDF הממוטב הפלט.
* צור מופע של `OptimizeOptions`.
* הוסף את מקורות הנתונים של הקלט והפלט לאפשרויות המיטוב.
* הוסף את מקורות הנתונים לקלט ולפלט לאפשרויות האופטימיזציה.
* צור מופע של `Optimizer` ובצע את האופטימיזציה באמצעות אפשרויות האופטימיזציה.

```cs
// צור מקור נתונים חדש לקובץ PDF הקלט.
var inputDataSource = new FileDataSource(inputPath);

// צור מקור נתונים חדש לקובץ PDF הממוטב לפלט.
var outputDataSource = new FileDataSource("sample_optimized.pdf");

// צור מופע חדש של OptimizeOptions.
var options = new OptimizeOptions();

// הוסף את מקורות הנתונים לקלט ולפלט לאפשרויות האופטימיזציה.
options.AddInput(inputDataSource);
options.AddOutput(outputDataSource);


// צור מופע חדש של Optimizer.
var optimizer = new Optimizer();

// בצע את האופטימיזציה באמצעות אפשרויות האופטימיזציה.
optimizer.Process(options);
```

## שינוי גודל קבצי PDF

שינוי גודל קובץ PDF כולל שינוי גודל הדף שלו. הקוד הבא מראה איך לבצע זאת. עקוב אחר השלבים הללו כדי לשנות את גודל קובץ PDF:

* צור מקור נתונים חדש לקובץ PDF הקלט.
* צור מקור קובץ חדש עבור קובץ ה-PDF הקלט.
* צור מקור קובץ חדש עבור קובץ ה-PDF המותאם.
* צור מופע של `ResizeOptions` וקבע את גודל הדף הרצוי.
* הוסף את מקורות הנתונים של הקלט והפלט לאפשרויות השינוי.
* צור מופע של `Optimizer` ובצע את תהליך השינוי באמצעות אפשרויות השינוי.

```cs
// צור מקור קובץ חדש עבור קובץ ה-PDF הקלט.
var inputDataSource = new FileDataSource("sample.pdf");

// צור מקור קובץ חדש עבור קובץ ה-PDF המותאם.
var outputDataSource = new FileDataSource("sample_resized.pdf");

// צור מופע חדש של ResizeOptions וקבע את גודל הדף הרצוי.
var opt = new ResizeOptions
{
    PageSize = PageSize.PageLetter
};

// הוסף את מקורות הנתונים של הקלט והפלט לאפשרויות השינוי.
opt.AddInput(inputDataSource);
opt.AddOutput(outputDataSource);

// צור מופע חדש של Optimizer.
var optimizer = new Optimizer();

// בצע את תהליך השינוי באמצעות אפשרויות השינוי.
optimizer.Process(opt);
```

## סיבוב דפי PDF
## סיבוב דפי PDF

סיבוב דפי PDF מאפשר לך לשנות את האוריינטציה של דפים בתוך מסמך PDF. הנה איך ניתן לסובב דפי PDF:

* צור מקור קובץ חדש עבור קובץ ה-PDF הקלט.
* צור מקור קובץ חדש עבור קובץ ה-PDF הפלט.
* יצירת מופע של `RotateOptions` והגדרת ערך הסיבוב.
* הוסף את מקורות הנתונים של הקלט והפלט לאפשרויות הסיבוב.
* יצירת מופע של `Optimizer` ועיבוד הסיבוב באמצעות אפשרויות הסיבוב.

```cs
// צור מקור קובץ חדש עבור קובץ ה-PDF הקלט.
var inputDataSource = new FileDataSource(inputPath);

// צור מקור קובץ חדש עבור קובץ ה-PDF הממוטב.
var outputDataSource = new FileDataSource("sample_optimized.pdf");

// יצירת מופע חדש של RotateOptions.
var opt = new RotateOptions();

// הוסף את מקורות הנתונים של הקלט והפלט לאפשרויות הסיבוב.
opt.AddInput(inputDataSource);
opt.AddOutput(outputDataSource);

// הגדרת ערך הסיבוב
opt.Rotation = Rotation.on180;

// יצירת מופע חדש של Optimizer.
var optimizer = new Optimizer();

// עיבוד האופטימיזציה באמצעות אפשרויות האופטימיזציה.
optimizer.Process(opt)
```
## סיכום

למדתם כיצד לייעל, לשנות את גודלם ולסובב קבצי PDF באמצעות התוסף Aspose.PDF Optimizer ב-C#. הטמיעו את הטכניקות הללו באפליקציות שלכם כדי לתפעל קבצי PDF ביעילות לפי הדרישות שלכם.
