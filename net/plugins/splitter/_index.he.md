---
title: Splitter
type: docs
weight: 120
url: /net/plugins/splitter/
description: מחלק מסמך PDF לעמודים נפרדים
lastmod: "2024-01-24"
draft: false
---

יש לך מסמך PDF גדול שתרצה לפרק לקבצים קטנים יותר וניהוליים יותר? עם [Aspose.PDF Splitter for .NET](https://products.aspose.org/pdf/net/splitter/), תוכל להשיג זאת בקלות. במאמר זה, נחקור את התהליך של פיצול מסמך PDF לקבצים מרובים באמצעות תוסף Aspose.PDF. בואו נצלול לקוד ונעבור על השלבים.

## דרישות מוקדמות

תזדקק לדברים הבאים:

* Visual Studio 2019 או מאוחר יותר
* Aspose.PDF עבור .NET 24.1 או מאוחר יותר
* קובץ PDF לדוגמא

בנוסף, התרגל עם המחלקה `SplitOptions` והתכונות שלה. תוכל למצוא מידע מפורט על המחלקה הזו ב[מקור המידע API](https://reference.aspose.com/pdf/net/aspose.pdf/SplitOptions/). שים לב שכל `FileDataSource` בפלט מייצג עמוד בודד בקבצי ה-PDF המפוצלים.

עכשיו, בואו נחקור את הקוד שניתן ונבין איך לפצל מסמך PDF.
עכשיו, בואו נחקור את הקוד שסופק ונבין איך לפצל מסמך PDF.

## הסבר הקוד

הקוד להלן מדגים הדגמה של פיצול PDF באמצעות Aspose.PDF.Plugins:

```csharp
using Aspose.Pdf.Plugins;
// ...........

// הגדר את נתיב הקלט של מסמך ה-PDF שיופצל.
using var inputStream = File.OpenRead(Path.Combine(@"C:\Samples\", "sample.pdf"));

// צור מופע חדש של Splitter.
var splitter = new Splitter();

// צור אפשרויות לפיצול המסמך.
var options = new SplitOptions();

// הוסף מקורות קלט ופלט לאפשרויות.
options.AddInput(new StreamDataSource(inputStream));

var document = new Aspose.Pdf.Document(inputStream);

for (int i = 1; i <= document.Pages.Count; i++)
{
   var pageNum = string.Format("{0,3}", i.ToString("D3"));
   options.AddOutput(new FileDataSource(Path.Combine(@"C:\Samples\", $"splitter_{pageNum}.pdf")));
}

// עבד את האפשרויות כדי לפצל את המסמך.
var result = splitter.Process(options);
Console.WriteLine(result);
```

בואו נפרט את השלבים המרכזיים:
בואו נפרט את השלבים המרכזיים:

1. **הגדרת קובץ PDF קלט**

   הקוד מתחיל בציון נתיב המסמך PDF שיש לפצל. זה נעשה באמצעות השיטה `File.OpenRead`.

2. **יצירת אובייקט (מפצל ואפשרויות פיצול)**

   הקוד יוצר מופע של המחלקה `Splitter` כדי לטפל בתהליך הפיצול. בנוסף, נוצר מופע של המחלקה `SplitOptions` כדי להגדיר את פעולת הפיצול.

3. **הוספת מקור נתונים (קלט ופלט)**

   מסמך ה-PDF הנכנס מתווסף ל-`SplitOptions` כמקור נתונים קלט באמצעות השיטה `AddInput`. עבור כל עמוד במסמך, נתיב קובץ פלט מתווסף כמקור נתונים פלט באמצעות השיטה `AddOutput`.

4. **הרצת שיטת תהליך**

   תהליך הפיצול מופעל על ידי קריאה לשיטה `Process` על המחלקה `Splitter`, עם ההגדרות שנקבעו ב-`SplitOptions`. תוצאת הפעולה נשמרת במשתנה `result`.

5. **טיפול בתוצאה**

   הקוד מדפיס את התוצאה לקונסול, ומספק מידע על תהליך הפיצול.
הקוד מדפיס את התוצאה לקונסול, ומספק מידע על תהליך הפיצול.
