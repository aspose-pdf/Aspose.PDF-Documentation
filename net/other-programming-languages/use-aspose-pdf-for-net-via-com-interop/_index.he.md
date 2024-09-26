---
title: Aspose.PDF עבור .NET באמצעות COM Interop
type: docs
weight: 20
url: /net/use-aspose-pdf-for-net-via-com-interop/
---

{{% alert color="primary" %}}

המידע בנושא זה חל על תרחישים בהם תרצה להשתמש ב- [Aspose.PDF עבור .NET](/pdf/net/) באמצעות COM Interop באחת משפות התכנות הבאות:

- ASP
- Delphi
- JScript
- Perl
- PHP
- PowerBuilder
- Python
- VBScript
- Visual Basic
- C++

{{% /alert %}}

## עבודה עם COM Interop

Aspose.PDF עבור .NET מתבצע תחת שליטת מסגרת ה-.NET וזה נקרא קוד מנוהל. קוד שנכתב בכל השפות המוזכרות לעיל פועל מחוץ למסגרת ה-.NET והוא נקרא קוד לא מנוהל. האינטראקציה בין קוד לא מנוהל ל-Aspose.PDF מתרחשת באמצעות המתקן של .NET הנקרא COM Interop.

אובייקטים של Aspose.PDF הם אובייקטים של .NET, אך כאשר משתמשים בהם באמצעות COM Interop, הם מופיעים כאובייקטים של COM בשפת התכנות שלך.
Aspose.PDF אובייקטים הם אובייקטים של .NET, אך כשמשתמשים בהם דרך COM Interop, הם נראים כאובייקטים של COM בשפת התכנות שלך.

{{% alert color="primary" %}}

- בעולם של COM אנו מבחינים בין שרת COM ללקוח COM. שרת COM מאחסן מחלקות COM בעוד שלקוח COM מבקש משרת COM מופעים של מחלקות, כלומר אובייקטים של COM.
- לקוח COM או בפשטות אפליקציית לקוח יכולה לדעת משהו על תוכן המחלקה של COM או להיות לגמרי בלתי מודע לשיטות ולתכונות שלה. לכן אפליקציית הלקוח יכולה לגלות את מבנה המחלקה של COM בעת קומפילציה/בנייה או רק במהלך הביצוע. תהליך זה של "גילוי" ידוע כקישור ולכן יש לנו **קישור מוקדם** ו**קישור מאוחר**.
- בקצרה מחלקת COM היא כמו קופסה שחורה וכדי לעבוד איתה נדרש ספריית סוגים, קובץ בינארי זה כולל תיאור של שיטות, תכונות של מחלקת COM וכל שפת תכנות ברמה גבוהה שתומכת בעבודה עם אובייקטים של COM לעיתים קרובות מכילה ביטוי תחבירי להוספת ספריית סוגים, למשל זהו [**#import**](http://msdn.microsoft.com/en-us/library/8etzzkb6.aspx) ב-C++.
- בקצרה, מחלקת COM היא כמו קופסה שחורה וכדי לעבוד איתה נדרש ספריית סוגים, קובץ בינארי זה מכיל תיאור של שיטות מחלקת COM, תכונות וכל שפה גבוהה שתומכת בעבודה עם אובייקטים של COM לעיתים קרובות מחזיקה בביטוי תחביר להוספת ספריית סוגים, לדוגמה זהו [**#import**](http://msdn.microsoft.com/en-us/library/8etzzkb6.aspx) ב-C++.
- ספריית הסוגים משמשת לקישור מוקדם.
- אובייקט COM יכול לחשוף את שיטותיו ותכונותיו בשתי דרכים: באמצעות **ממשק שליחה** (dispinterface) ובתוך **vtable** (טבלת פונקציות וירטואליות).
- בתוך **dispinterface**, כל שיטה ותכונה מזוהות על ידי חבר ייחודי; חבר זה הוא מזהה השליחה של הפונקציה (או **DispID**).
- **vtable** הוא רק סט של מצביעים לפונקציות שממשק המחלקה של COM תומך בהן.
- אובייקט שמחשף את שיטותיו דרך שני הממשקים תומך ב**ממשק כפול**.
- יש יתרונות לשני סוגי הקישור.
- יש יתרונות לשני סוגי הקישור.
- מנגנון קישור מאוחר יש יתרון גדול: אם יוצר ה- COM DLL מחליט לשחרר גרסה חדשה, עם ממשק פונקציה שונה, כל קוד שקורא לשיטות אלו לא ייפלט כל עוד השיטות זמינות; אפילו אם ה- **vtable** שונה מנגנון הקישור המאוחר מצליח לגלות את ה- DISPIDs החדשים ולקרוא לשיטות המתאימות.

הנה הנושאים שיהיה עליך לשלוט בהם בסופו של דבר:

- שימוש באובייקטים של COM בשפת התכנות שלך. ראה את תיעוד שפת התכנות שלך ואת הנושאים הספציפיים לשפה להמשך בתיעוד זה.

- עבודה עם אובייקטים של COM שחשופים על ידי .NET COM Interop. ראה [Interoperating With Unmanaged Code](http://msdn.microsoft.com/en-us/library/sd10k43k.aspx) ו-[Exposing .NET Framework Components to COM](http://msdn.microsoft.com/en-us/library/zsfww439%28v=vs.110%29.aspx) ב- MSDN.

- מודל אובייקט של מסמך Aspose.PDF.
- מודל האובייקטים של Aspose.PDF.

{{% /alert %}}

## רישום Aspose.PDF עבור .NET עם COM Interop

עליך להתקין את Aspose.PDF עבור .NET ולוודא שהוא רשום עם COM Interop (לוודא שניתן לקרוא אליו מקוד לא מנוהל).

{{% alert color="primary" %}}

כדי לרשום את Aspose.PDF עבור .NET ל-COM Interop באופן ידני:

1. מתפריט ה**התחל**, בחר **כל התוכניות**, אז **Microsoft Visual Studio**, **כלי Visual Studio** ולבסוף, **פקודת Visual Studio Command Prompt**.
1. הזן את הפקודה לרישום האסמבלי:
   1. .NET Framework 2.0
      regasm "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net2.0\Aspose.PDF.dll" /codebase
   1. .NET Framework 3.5
      regasm "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net3.5\Aspose.PDF.dll" /codebase
   1. .NET Framework 4.0
      regasm "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net4.0\Aspose.PDF.dll" /codebase

{{% /alert %}}

שים לב שהאפשרות /codebase נחוצה רק אם Aspose.PDF.dll אינו ב-GAC, שימוש באפשרות זו גורם ל-regasm לשים את הנתיב לאסמבלי ברישום.
{{% alert color="primary" %}}
regasm.exe הוא כלי הכלול ב-SDK של .NET Framework. כל כלי ה-SDK של .NET Framework נמצאים בתיקייה *\Microsoft .NET\Framework\<FrameworkVersion>*, לדוגמה *C:\Windows\Microsoft .NET\Framework\v4.0.30319*. אם אתה משתמש ב-Visual Studio .NET:
מתפריט **התחל**, בחר **תוכניות**, לאחר מכן **Microsoft Visual Studio .NET**, אז **כלי Visual Studio .NET** ולבסוף, **פקודת Visual Studio .NET 2003**.
הוא מפעיל חלון פקודה עם כל משתני הסביבה הנחוצים מוגדרים.

{{% /alert %}}

### ProgIDs

ProgID הוא ראשי תיבות של "מזהה תכנותי". זהו שם של מחלקת COM שמשמשת ליצירת אובייקט. ProgID מורכב משם הספרייה "Aspose.PDF" ושם המחלקה.

### ספריית סוגים

{{% alert color="primary" %}}

אם שפת התכנות שלך (למשל Visual Basic או Delphi) מאפשרת לך להתייחס לספריית סוגי COM, אז הוסף התייחסות ל-Aspose.PDF.tlb ותוכל לראות את כל מחלקות, שיטות, תכונות ומניות של Aspose.PDF ל-.NET בדפדפן האובייקטים שלך.
{{% /alert %}}
אם שפת התכנות שלך (לדוגמה Visual Basic או Delphi) מאפשרת לך להתייחס לספריית טיפוסי COM, הוסף הפניה ל-Aspose.PDF.tlb ולראות את כל מחלקות Aspose.PDF ל-.NET, שיטות, מאפיינים ומניות בדפדפן האובייקטים שלך.

ליצירת קובץ TLB:

- .NET Framework 2.0
  regasm "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net2.0\Aspose.PDF.dll" /tlb: "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net2.0\Aspose.PDF.tlb" /codebase
- .NET Framework 3.5
  regasm "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net3.5\Aspose.PDF.dll" /tlb: "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net3.5\Aspose.PDF.tlb" /codebase
- .NET Framework 4.0
  regasm "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net4.0\Aspose.PDF.dll" /tlb: "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net4.0\Aspose.PDF.tlb" /codebase

{{% /alert %}}

## יצירת אובייקטי COM

יצירת אובייקט COM דומה ליצירת אובייקט .NET רגיל:

```vb

'Instantiate Pdf instance by calling its empty constructor

Dim pdf
Set pdf = CreateObject("Aspose.PDF.Generator.Pdf")

```
כאשר נוצר, ניתן לגשת לשיטות ולתכונות של האובייקט, כאילו היה אובייקט COM:

```vb
'הוספת סעיף לאובייקט Pdf
pdf.Sections.Add(pdfsection)
```

חלק מהשיטות כוללות עומסים והן יוצגו על ידי COM Interop עם סיומת מספרית שתתווסף אליהן, למעט השיטה הראשונה שנשארת ללא שינוי. לדוגמה, עומסי השיטה Pdf.Save יהפכו ל- Pdf.Save, Pdf.Save_2 וכן הלאה.

למידע נוסף, ראה את המאמרים הספציפיים לשפה בהמשך התיעוד הזה.

## יצירת אסמבלי עטיפה

אם אתה זקוק לשימוש במספר רב של מחלקות, שיטות ותכונות של Aspose.PDF עבור .NET, שקול ליצור אסמבלי עטיפה (באמצעות C# או כל שפת תכנות .NET אחרת). אסמבליות עטיפה עוזרות להימנע משימוש ישיר ב-Aspose.PDF עבור .NET מקוד לא מנוהל.

גישה טובה היא לפתח אסמבלי .NET שמפנה ל-Aspose.PDF עבור .NET ועושה את כל העבודה איתו, וחושף רק מעט מחלקות ושיטות לקוד לא מנוהל.
גישה טובה היא לפתח Assembly ב-.NET שמפנה ל-Aspose.PDF עבור .NET ועושה את כל העבודה איתו, וחושף רק קבוצה מינימלית של מחלקות ושיטות לקוד לא מנוהל.

הפחתת מספר המחלקות והשיטות שאתה צריך לקרוא דרך COM Interop מפשטת את הפרויקט. שימוש במחלקות .NET דרך COM Interop לעיתים דורש כישורים מתקדמים.

