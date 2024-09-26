---
title: מחלץ תמונות
type: docs
weight: 80
url: /net/plugins/imageextractor/
description: חילוץ תמונות מקבצי PDF בקלות עם תוסף ImageExtractor
lastmod: "2024-01-24"
draft: false
---

אם אי פעם הייתה לך הצורך לחלץ תמונות מקובץ PDF באמצעות .NET, Aspose.PDF עבור .NET מספק פתרון חזק ופשוט לשימוש. במדריך זה נעבור על השלבים הבסיסיים ליצירת אובייקט, הוספת מקור נתונים והפעלת השיטה process באמצעות [Aspose.PDF Image Extractor](https://products.aspose.org/pdf/net/image-extractor/).

## דרישות מוקדמות

תזדקק לדברים הבאים:

* Visual Studio 2019 או מאוחר יותר
* Aspose.PDF עבור .NET 21.1 או מאוחר יותר
* קובץ PDF לדוגמה

ניתן להוריד את ספריית Aspose.PDF עבור .NET מהאתר הרשמי או להתקינה באמצעות מנהל החבילות NuGet ב-Visual Studio.
כעת, בואו נצלול לקוד ונלמד כיצד להשתמש בתוסף ImageExtractor.

## שלבים

הקוד שסופק מדגים את השימוש בתוסף `ImageExtractor` לחילוץ תמונות מקובץ PDF.
 הקוד המוצג מדגים את השימוש בתוסף `ImageExtractor` לחילוץ תמונות מקובץ PDF.

### 1. יצירת אובייקט (ImageExtractor)

השלב הראשון כולל יצירת מופע של תוסף `ImageExtractor`. זה מתבצע באמצעות הקוד הבא:

```csharp
using var plugin = new ImageExtractor();
```

כאן, המשפט `using` מבטיח טיפול נכון במשאבים כאשר הפעולה מסתיימת.

### 2. הוספת מקור נתונים

לאחר מכן, נוצר מופע של המחלקה `ImageExtractorOptions` כדי להגדיר את תהליך חילוץ התמונות. נתיב קובץ הקלט מתווסף לאפשרויות באמצעות השיטה `AddInput`:

```csharp
var imageExtractorOptions = new ImageExtractorOptions();
imageExtractorOptions.AddInput(new FileDataSource(Path.Combine(@"C:\Samples\", "sample.pdf")));
```

ודא להחליף את `"C:\Samples\"` ו-`"sample.pdf"` בנתיב ושם הקובץ המתאימים של קובץ ה-PDF שלך.

### 3. הרצת שיטת הפעלה

השלב הסופי הוא לעבד את חילוץ התמונות באמצעות התוסף והאפשרויות:

```csharp

```csharp
var resultContainer = plugin.Process(imageExtractorOptions);
```

התוצאה מאוחסנת ב-`resultContainer`, שמכיל את התמונה(ות) שנלקחו.

### 4. טיפול בתמונה(ות) שנלקחו

לאחר הרצת התהליך, אתה יכול לאחזר את התמונה(ות) שנלקחו מהמכולה של התוצאות. הקוד למטה מדגים שמירת התמונה הראשונה שנלקחה במקום זמני:

```csharp
var imageExtracted = resultContainer.ResultCollection[0].ToStream();
var someTemporaryPlace = File.OpenWrite("C:\\tmp\\tmp.jpg");
imageExtracted.CopyTo(someTemporaryPlace);
```

ודא שאתה מותאם את נתיב היעד ושם הקובץ לפי העדפותיך.

אתה יכול להעתיק את הדוגמה המלאה למטה:

```cs
using Aspose.Pdf.Plugins;

namespace AsposePluginsNet8.Documentation;

internal static class ImageExtractorDemo
{
    // <summary>
    // מדגים את השימוש בתוסף ImageExtractor לחלץ תמונות מקובץ PDF.
    // </summary>
    internal static void Run()
    {
        // יצירת מופע של התוסף ImageExtractor.
        using var plugin = new ImageExtractor();

        // יצירת מופע של הכיתה ImageExtractorOptions.
        var imageExtractorOptions = new ImageExtractorOptions();

        // הוספת נתיב קובץ הקלט לאפשרויות.
        imageExtractorOptions.AddInput(new FileDataSource(Path.Combine(@"C:\Samples\", "sample.pdf")));

        // עיבוד חילוץ התמונה באמצעות התוסף והאפשרויות.
        var resultContainer = plugin.Process(imageExtractorOptions);

        // קבלת התמונה שנלקחה מהמכולה של התוצאות.
        var imageExtracted = resultContainer.ResultCollection[0].ToStream();
        var someTemporaryPlace = File.OpenWrite(Path.Combine(@"C:\Samples\","tmp.jpg"));
        imageExtracted.CopyTo(someTemporaryPlace);
    }
}
```

