---
title: עורך טפסים
type: docs
weight: 40
url: /net/plugins/formeditor/
description: איך להוסיף, לעדכן, ולהסיר שדות טופס בקבצי PDF באמצעות תוספי Aspose.PDF
lastmod: "2024-01-24"
draft: false
---

במאמר זה, נראה לך איך להשתמש ב[תוסף עורך הטפסים](https://products.aspose.org/pdf/net/form-editor/), שיכול להוסיף, לעדכן, ולהסיר שדות טופס בקבצי PDF.

## דרישות מוקדמות

תזדקק לדברים הבאים:

* Visual Studio 2019 או מאוחר יותר
* Aspose.PDF עבור .NET 24.1 או מאוחר יותר
* קובץ PDF לדוגמה שמכיל כמה שדות טופס

ניתן להוריד את ספריית Aspose.PDF עבור .NET מהאתר הרשמי או להתקין אותה באמצעות מנהל חבילות NuGet ב-Visual Studio.

## שלבים

השלבים הבסיסיים להוספה, עדכון, והסרת שדות טופס בקבצי PDF באמצעות תוסף FormEditor הם:

1. צור אובייקט של מחלקת FormEditor
1. צור אובייקט של מחלקת FormEditorAddOptions, FormEditorSetOptions, או FormRemoveSelectedFieldsOptions, תלוי בפעולה שברצונך לבצע
1.
1.
1. הרץ את שיטת ה-Process של אובייקט FormEditor

בואו נראה איך לממש את השלבים הללו בקוד C# עבור כל פעולה.

### שלב 1: צור אובייקט של המחלקה FormEditor

מחלקת FormEditor היא המחלקה הראשית המספקת את הפונקציונליות של הוספה, עדכון, והסרת שדות טופס בקבצי PDF. כדי להשתמש בה, עליך ליצור מופע שלה באמצעות הבנאי המוגדר כברירת מחדל:

```cs
// צור מופע של התוסף FormEditor
var plugin = new FormEditor();
```

### שלב 2: צור אובייקט של המחלקה FormEditorAddOptions, FormEditorSetOptions, או FormRemoveSelectedFieldsOptions, בהתאם לפעולה שברצונך לבצע

המחלקות `FormEditorAddOptions`, `FormEditorSetOptions`, ו-`FormRemoveSelectedFieldsOptions` הן מחלקות עזר המאפשרות לך לציין אפשרויות ופרמטרים שונים עבור פעולות עריכת הטופס, כגון סוגי שדות הטופס, ערכים, תכונות, פרדיקטים ועוד.
המחלקות `FormEditorAddOptions`, `FormEditorSetOptions`, ו-`FormRemoveSelectedFieldsOptions` הן מחלקות עזר שמאפשרות לך לציין אפשרויות ופרמטרים שונים עבור פעולות עריכת טופס, כגון סוגי שדות הטופס, ערכים, תכונות, פרדיקטים וכו'.

```cs
    // יצירת אפשרויות להוספת שדות טופס.
    var options = new FormEditorAddOptions(
        [
            // יצירת שדה טופס מסוג תיבת סימון.
            new FormCheckBoxFieldCreateOptions(1, new Rectangle(110, 700, 125, 715))
            {
                Value = "CheckBoxField 1",
                PartialName = "CheckBoxField_1",
                Color = Color.Blue,
            },
            // יצירת שדה טופס מסוג תיבת רשימה.
            new FormComboBoxFieldCreateOptions(1, new Rectangle(310, 600, 350, 615))
            {
                Color = Color.Red,
                Editable = true,
                DefaultAppearance = new DefaultAppearance("Arial Bold", 12, System.Drawing.Color.DarkGreen),
                Options = ["option1", "option2", "option3"],
                Selected = 2
            },
            // יצירת שדה טופס מסוג תיבת טקסט.
            new FormTextBoxFieldCreateOptions(1, new Rectangle(10, 700, 90, 715))
            {
                MaxLen = 10,
                Value = "Some text",
                Color = Color.Chocolate
            }
        ]);
```
### שלב 3: הוספת מקורות הנתונים לקלט ולפלט לאובייקט האופציות

מקורות הנתונים לקלט ולפלט הם קבצי ה-PDF שברצונך לערוך ולשמור.

כדי לעדכן את ערכי שדות הטופס שערכם הוא "ערך אחד" או "ערך נוסף" ל"ערך חדש", ניתן להשתמש בקוד הבא:

```cs
    var options = new FormEditorSetOptions(
    (field) => { return field.Value == "ערך אחד" || field.Value == "ערך נוסף"; },
    new FormFieldSetOptions()
    {
        Value = "ערך חדש"
    });
```

כדי להסיר שדות טופס שהקואורדינטה התחתונה-שמאלית שלהם גדולה מ-300, ניתן להשתמש בקוד הבא:

```cs
// יצירת אופציות להסרת שדות טופס
var options = new FormRemoveSelectedFieldsOptions((field) => field.Rect.LLX > 300);
```
מקורות הנתונים הכניסה והפלט הם קבצי PDF שברצונך לערוך ולשמור.

```cs
// ציין את נתיבי הקבצים לכניסה ולפלט
string inputPath = $@"C:\Samples\Output\sample_forms.pdf";
string outputPath = $@"C:\Samples\Output\sample_forms2.pdf";

// צור מופע חדש של המחלקה FileDataSource עבור קבצי הכניסה והפלט
FileDataSource inputData = new(inputPath);
FileDataSource outputData = new(outputPath);

// הוסף את מקורות הנתונים לכניסה ולפלט לאפשרויות
options.AddInput(inputData);
options.AddOutput(outputData);
```

### שלב 4: הפעל את המתודה Process של אובייקט FormEditor

השלב הסופי הוא להפעיל את המתודה Process של אובייקט FormEditor, תוך העברת אובייקט האפשרויות כפרמטר.
השלב הסופי הוא להריץ את שיטת Process של אובייקט FormEditor, תוך העברת אובייקט האפשרויות כפרמטר.

```cs
// עיבוד פעולת עריכת הטופס באמצעות התוסף והאפשרויות
ResultContainer result = plugin.Process(options);

// קבלת התוצאה הראשונה מאוסף התוצאות
var result = resultContainer.ResultCollection[0];

// הדפסת התוצאה
Console.WriteLine(result);
```

התוצאה תכיל מידע כגון נתיבי קבצים פלט.
