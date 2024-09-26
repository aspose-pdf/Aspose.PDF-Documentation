---
title: מחולל תוכן עניינים
type: docs
weight: 150
url: /net/plugins/tocgenerator/
description: יוצר תוכן עניינים עם מחולל תוכן עניינים של Aspose.PDF עבור .NET 
lastmod: "2024-01-24"
draft: false
---

האם אתה רוצה לשפר את מסמכי ה-PDF שלך על ידי [הוספת תוכן עניינים (TOC)](https://products.aspose.org/pdf/net/toc-generator/) באופן דינמי? Aspose.PDF עבור .NET מספק מחלקת `TocGenerator` חזקה שמאפשרת לך ליצור TOCs בקלות. במדריך זה, נעבור על השלבים הבסיסיים ליצירת TOC במסמך PDF באמצעות Aspose.PDF, כולל יצירת אובייקט `TocGenerator`, הוספת נתיבי קלט/פלט, והפעלת תהליך יצירת ה-TOC.

## דרישות מוקדמות

תזדקק לדברים הבאים:

* Visual Studio 2019 או מאוחר יותר
* Aspose.PDF עבור .NET 24.1 או מאוחר יותר
* קובץ PDF לדוגמה

בנוסף, התמצא במחלקת `TocOptions` ובפונקציונליות שלה. ניתן למצוא מידע מפורט ב-[מרכז המידע של Aspose.PDF API](https://reference.aspose.com/pdf/net/aspose.pdf/TocOptions/).

עכשיו, בוא נצלול לקוד ונחקור איך ליצור תוכן עניינים למסמך PDF שלך.
עכשיו, בואו נצלול לתוך הקוד ונבחן איך ליצור תוכן עניינים למסמך PDF שלכם.

## הדרכה על הקוד

נשתמש במחלקה `TocGeneratorDemo` עם מתודת `Run` כדי להדגים איך ליצור תוכן עניינים. בואו נפרט את השלבים המרכזיים:

```csharp
using Aspose.Pdf.Plugins;

namespace AsposePluginsNet8.Documentation
{
    internal static class TocGeneratorDemo
    {
        private const string PathForSamples = @"C:\Samples\";

        // מריץ את הדגמת יצירת תוכן העניינים.
        internal static void Run()
        {
            // יוצר מופע חדש של המחלקה TocGenerator.
            TocGenerator generator = new();

            // יוצר מופע חדש של המחלקה TocOptions.
            TocOptions options = new();
            // מוסיף את נתיבי הקלט והפלט ל-TocOptions.
            options.AddInput(new FileDataSource(Path.Combine(PathForSamples, "sample.pdf")));
            options.AddOutput(new FileDataSource(Path.Combine(PathForSamples, "sample_toc.pdf")));

            // מעבד את יצירת תוכן העניינים ומקבל את תיבת התוצאות.
            var resultContainer = generator.Process(options);

            // מקבל את התוצאה מתיבת התוצאות.
            var result = resultContainer.ResultCollection[0];

            // מדפיס את התוצאה לקונסול.
            Console.WriteLine(result);
        }
    }
}
```
### 1. יצירת אובייקט TocGenerator

הקוד מתחיל ביצירת מופע חדש של המחלקה `TocGenerator`. מחלקה זו מספקת שיטות ליצירת תוכן עניינים עבור מסמכי PDF.

```csharp
TocGenerator generator = new();
```

### 2. יצירת TocOptions

לאחר מכן, נוצר מופע חדש של המחלקה `TocOptions` כדי להגדיר את תהליך יצירת תוכן העניינים. נתיבי קבצים לקלט ולפלט מתווספים לאפשרויות.

```csharp
TocOptions options = new();
options.AddInput(new FileDataSource(Path.Combine(PathForSamples, "sample.pdf")));
options.AddOutput(new FileDataSource(Path.Combine(PathForSamples, "sample_toc.pdf")));
```

### 3. הפעלת תהליך יצירת תוכן עניינים

המתודה `Process` נקראת על אובייקט ה-`TocGenerator`, תוך העברת האפשרויות שהוגדרו. תיבת התוצאות מכילה את תוכן העניינים שנוצר, והיא מודפסת לקונסול.

```csharp
var resultContainer = generator.Process(options);
var result = resultContainer.ResultCollection[0];
Console.WriteLine(result);
```
