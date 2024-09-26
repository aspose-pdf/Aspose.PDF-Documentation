---
title: ממיר מסמכים
type: docs
weight: 10
url: /net/plugins/doc/
description: המרת PDF ל-Word בקלות עם התוסף PdfDoc
lastmod: "2024-01-24"
---

מאמר זה מדריך אותך בשימוש ב-[ממיר ה-DOC של Aspose.Pdf ל-.NET](https://products.aspose.org/pdf/net/doc-converter/) להמרת מסמך PDF לפורמט Microsoft Word (.doc / .docx).

## דרישות מוקדמות

תזדקק לדברים הבאים:

* Visual Studio 2019 או מאוחר יותר
* Aspose.PDF ל-.NET 24.1 או מאוחר יותר
* קובץ PDF לדוגמה המכיל שדות טופס מסוימים

ניתן להוריד את ספריית Aspose.PDF ל-.NET מהאתר הרשמי או להתקין אותה באמצעות מנהל חבילות NuGet ב-Visual Studio.

## שלבים

### 1. הכנת המרתך (תמונת מסך של מחלקת FileDataSource)

תהליך ההמרה כולל שלושה שלבים עיקריים: הגדרת קבצים קלט ופלט, יצירת אובייקט `PdfDoc`, וקביעת אפשרויות המרה.

#### 1.1. הגדרת מקורות נתונים

* **קובץ קלט:** נשתמש במחלקת `FileDataSource` כדי לציין את מיקום הקובץ PDF שברצונך להמיר.
* **קובץ קלט:** נשתמש במחלקה `FileDataSource` כדי לציין את מיקום הקובץ PDF שברצונך להמיר.

```csharp
  FileDataSource inputDataSource = new(Path.Combine(@"C:\Samples\", "sample.pdf"));
```

  * החלף את `"C:\Samples\sample.pdf"` בנתיב המדויק לקובץ ה-PDF שלך.

* **קובץ פלט:** באופן דומה, השתמש באובייקט `FileDataSource` נוסף כדי להגדיר את המיקום ושם הקובץ למסמך ה-Word המתקבל.

```csharp
  FileDataSource outputDataSource = new(Path.Combine(@"C:\Samples\", "sample.docx"));
```

* החלף את `"C:\Samples\sample.docx"` בנתיב ושם הקובץ שברצונך לפלט.

### 2. יצירת אובייקט התוסף PdfDoc (צילום מסך של מחלקת PdfDoc)

לאחר מכן, אנו יוצרים מופע של מחלקת ה-`PdfDoc` כדי לבצע את ההמרה.

```csharp
  var plugin = new PdfDoc();
```

אובייקט זה משמש כמנוע לתהליך ההמרה.

### 3. קביעת הגדרות המרה

מחלקת `PdfToDocOptions` מאפשרת לך לעדן את תהליך ההמרה.
### כיתה `PdfToDocOptions` מאפשרת לך לעדן את תהליך ההמרה.

* **פורמט שמירה:** ציין את פורמט הפלט הרצוי עבור מסמך ה-Word. במקרה זה, אנו משתמשים ב-`SaveFormat.DocX` כדי לייצר מסמך מיקרוסופט וורד 2007 או מאוחר יותר תואם (.docx).

* **מוד המרה:** הגדר כיצד התוסף מפרש את מבנה ה-PDF במהלך ההמרה. נשתמש ב-`ConversionMode.EnhancedFlow` כדי למטב את מסמך ה-Word המתקבל עבור פריסה ועיצוב.

הנה קטע הקוד להגדרת האפשרויות:

```csharp
  PdfToDocOptions options = new()
  {
      SaveFormat = SaveFormat.DocX,
      ConversionMode = ConversionMode.EnhancedFlow
  };
```

**הוספת קלט ופלט:**

לבסוף, אנו מקשרים את מקורות הנתונים שהוגדרו קודם לכן עם אפשרויות ההמרה באמצעות שיטות `AddInput` ו-`AddOutput`:

```csharp
  options.AddInput(inputDataSource);
  options.AddOutput(outputDataSource);
```

זה מקשר את קובץ ה-PDF הנכנס ומסמך ה-Word הרצוי לתהליך ההמרה.

### 4.
### 4.

עם הכל מוכן, בואו נתחיל את ההמרה על ידי קריאה למתודה `Process` של תוסף `PdfDoc` תוך העברת האפשרויות שהוגדרו:

```csharp
  var resultContainer = plugin.Process(options);
```

מתודה זו מבצעת את ההמרה ומחזירה אובייקט `ResultContainer` המכיל פרטים על התהליך.

**אחזור תוצאות:**

למרות שזה לא חיוני להמרה בסיסית, ניתן לגשת לתוצאות דרך המאפיין `ResultCollection` של אובייקט `ResultContainer`. זה עשוי להיות שימושי לצרכי דיבאגינג או מעקב אחר פרטי המרה ספציפיים.

```csharp
  var result = resultContainer.ResultCollection[0];

  // הדפסת התוצאה (אופציונלי לצורכי הדגמה)
  Console.WriteLine(result);
```

עם שלב זה הסופי, מסמך ה-PDF שלך יומר לפורמט Word המבוקש ויישמר במיקום הפלט שהוגדר.

