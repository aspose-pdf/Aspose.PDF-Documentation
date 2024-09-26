---
title: חלץ טקסט
type: docs
weight: 140
url: /net/plugins/textextractor/
description: מחלץ תוכן טקסט ממסמך PDF.
lastmod: "2024-01-24"
---

יש לך מסמך PDF שממנו אתה צריך [לחלץ טקסט באופן תכנותי](https://products.aspose.org/pdf/net/text-extractor/)? עם Aspose.PDF עבור .NET, תוכל להשיג זאת בקלות באמצעות מחלקת TextExtractor. במאמר זה, נעבור על השלבים הבסיסיים ליצירת אפליקציה לחילוץ טקסט ב-.NET, כולל יצירת אובייקט TextExtractor, הוספת מקור נתונים, והרצת תהליך חילוץ הטקסט.

## דרישות מוקדמות

תצטרך את הבאים:

* Visual Studio 2019 או מאוחר יותר
* Aspose.PDF עבור .NET 24.1 או מאוחר יותר
* קובץ PDF לדוגמה

בנוסף, התמצא במחלקה `TextExtractorOptions` ובפונקציונליות שלה. ניתן למצוא מידע מפורט ב-[מרכז המידע של Aspose.PDF API](https://reference.aspose.com/pdf/net/aspose.pdf/TextExtractorOptions/).

עכשיו, בואו נעבור לקוד ונחקור כיצד לחלץ טקסט ממסמך PDF.
עכשיו, בואו נעמיק בקוד ונחקור איך לחלץ טקסט ממסמך PDF.

## סקירת קוד

הקוד הבא מדגים את יכולות חילוץ הטקסט. בואו נפרט את השלבים המרכזיים:

### 1. יצירת אובייקט TextExtractor

הקוד מתחיל ביצירת מופע חדש של המחלקה `TextExtractor`. מחלקה זו מספקת שיטות לחילוץ טקסט ממסמכי PDF.

```csharp
using TextExtractor extractor = new();
```

### 2. הוספת מקור נתונים

לאחר מכן נוצר `FileDataSource` עבור קובץ ה-PDF הקלט. זהו הקובץ ממנו יוחלץ הטקסט.

```csharp
FileDataSource fileSource = new(Path.Combine(@"C:\Samples\", "sample.pdf"));
```

### 3. יצירת TextExtractorOptions

נוצר אובייקט `TextExtractorOptions` כדי להגדיר את תהליך חילוץ הטקסט. מקור הקובץ הקלט מתווסף לאפשרויות.

```csharp
TextExtractorOptions textExtractorOptions = new();
textExtractorOptions.AddInput(fileSource);
```

### 4. הפעלת תהליך חילוץ הטקסט

השיטה `Process` נקראת על אובייקט ה-`TextExtractor`, עם האפשרויות שהוגדרו.
שיטת `Process` נקראת לאחר מכן על אובייקט `TextExtractor`, תוך מעבר של האפשרויות המוגדרות.

```csharp
var resultContainer = extractor.Process(textExtractorOptions);
var results = resultContainer.ResultCollection;
Console.WriteLine(results[0]);
```

ניתן לראות את הקוד המלא להלן:

``````cs
using Aspose.Pdf.Plugins;
// ...

// יצירת מופע חדש של TextExtractor.
using TextExtractor extractor = new();

// יצירת FileDataSource עבור קובץ PDF הקלט.
FileDataSource fileSource = new(Path.Combine(@"C:\Samples\", "sample.pdf"));

// יצירת TextExtractorOptions.
TextExtractorOptions textExtractorOptions = new();
textExtractorOptions.AddInput(fileSource);

// עיבוד חילוץ הטקסט.
var resultContainer = extractor.Process(textExtractorOptions);
var results = resultContainer.ResultCollection;

// הדפסת הטקסט שחולץ.
Console.WriteLine(results[0]);

```

