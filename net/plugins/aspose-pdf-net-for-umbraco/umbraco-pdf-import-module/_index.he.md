---
title: מודול ייבוא PDF של Umbraco
type: docs
weight: 10
url: /net/umbraco-pdf-import-module/
description: למד כיצד להתקין ולהשתמש במודול ייבוא PDF של Umbraco
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

## הקדמה

**Aspose.PDF for .NET** הוא רכיב יצירה וניהול מסמכי PDF שמאפשר ליישומי .NET שלך לקרוא, לכתוב ולנהל מסמכי PDF קיימים ללא שימוש ב-Adobe Acrobat. הוא גם מאפשר לך ליצור טפסים ולנהל שדות טופס המוטמעים במסמך PDF.

**Aspose.PDF for .NET** זמין ומציע שפע של תכונות כולל אפשרויות דחיסת PDF; יצירה וניהול של טבלאות; תמיכה באובייקטי גרפיקה; פונקציונליות קישורים היפר-טקסטואלית מורחבת; בקרות אבטחה מתקדמות; טיפול בגופנים מותאמים אישית; אינטגרציה עם מקורות נתונים; הוספה או הסרה של סימניות; יצירת תוכן עניינים; הוספה, עדכון, מחיקת קבצים מצורפים והערות; ייבוא או ייצוא נתוני טופס PDF; הוספה, החלפה או הסרה של טקסט ותמונות; פיצול, שרשור, חילוץ או הכנסת דפים; המרת דפים לתמונה; הדפסת מסמכי PDF ועוד הרבה יותר
**Aspose.PDF עבור .NET** הוא זול ומציע מגוון עצום של תכונות כולל אפשרויות דחיסת PDF; יצירה וניהול של טבלאות; תמיכה באובייקטים גרפיים; פונקציונליות קישורים היפרטקסט מרחיבה; שליטה מורחבת באבטחה; טיפול בגופנים מותאמים אישית; אינטגרציה עם מקורות נתונים; הוספה או הסרה של סימניות; יצירת תוכן עניינים; הוספה, עדכון, מחיקה של קבצים מצורפים והערות; ייבוא או ייצוא של נתוני טופס PDF; הוספה, החלפה או הסרה של טקסט ותמונות; פיצול, שרשור, חילוץ או הוספת דפים; המרת דפים לתמונה; הדפסת מסמכי PDF ועוד הרבה יותר

### **תכונות המודול**

Umbraco PDF Import הוא תוסף קוד פתוח מבית [Aspose](http://www.aspose.com/) המאפשר למפתחים לקרוא תוכן מכל מסמך PDF ללא צורך בתוכנה נוספת.
יבוא PDF של Umbraco הוא תוסף קוד פתוח מבית [Aspose](http://www.aspose.com/) שמאפשר למפתחים לקרוא תוכן מכל מסמך PDF ללא הצורך בתוכנה נוספת.

## דרישות מערכת ופלטפורמות נתמכות

### **דרישות מערכת**

כדי להתקין את מודול יבוא PDF של Aspose .NET ל-Umbraco עליך לעמוד בדרישות הבאות:

- Umbraco 6.0 +

אנא צרו קשר איתנו אם ברצונכם להתקין מודול זה על גרסאות אחרות של Umbraco.

### **פלטפורמות נתמכות**

המודול נתמך בכל הגרסאות של

- Umbraco הרץ על ASP.NET 4.0

## הורדה

ניתן להוריד את יבוא PDF של Aspose .NET ל-Umbraco מאחת מהמיקומים הבאים

- [CodePlex](https://asposeumbraco.codeplex.com/releases)
- [Github](https://github.com/asposemarketplace/Aspose_for_Umbraco/releases)
- [Sourceforge](https://sourceforge.net/projects/asposeumbraco/files/)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-umbraco/downloads)
- [Umbraco](https://our.umbraco.org/projects/developer-tools/import-from-pdf-using-aspose-pdf)
- [Umbraco](https://our.umbraco.org/projects/developer-tools/import-from-pdf-using-aspose-pdf)

## התקנה

לאחר ההורדה, נא לעקוב אחר השלבים הבאים כדי להתקין את החבילה באתר האומברקו שלך:

1. התחבר לאזור ה**מפתחים** של אומברקו, לדוגמה <http://www.myblog.com/umbraco/>
1. בתפריט העץ, הרחב את תיקיית **החבילות**.
   מכאן יש שתי דרכים להתקין חבילה: תבחר **התקן חבילה מקומית** או חפש ב**מאגר החבילות של Umbraco.**
1. אם אתה מתקין **חבילה מקומית**, אל תפתח את החבילה אלא טען את הזיפ לתוך אומברקו.
1. עקוב אחר ההוראות במסך.

**הערה:** ייתכן שתקבל שגיאת 'אורך הבקשה המרבי חרג' בעת ההתקנה. תוכל לתקן בקלות את בעיית זו על ידי עדכון הערך 'maxRequestLength' בקובץ ה-web.config של אומברקו.

```xml
  <httpRuntime requestValidationMode="2.0" enableVersionHeader="false" maxRequestLength="25000" />
```

## שימוש

לאחר שהתקנת את המקרו זה ממש פשוט להתחיל להשתמש בו באתר שלך:

1.
1. לחץ על **הגדרות** ברשימת הסעיפים בחלק התחתון השמאלי של המסך.
1. הרחב את צומת **תבניות** ובחר בתבנית שברצונך להוסיף אליה מאקרו, לדוגמה פוסט בבלוג.
1. בחר את המיקום בתבנית שנבחרה שבו אתה רוצה את הכפתור.
1. לחץ על **הוסף מאקרו** בסרגל העליון.
1. מתוך **בחר מאקרו**, בחר במאקרו המותקן ולחץ על **אישור**.

הוספת בהצלחה את התבנית. כעת מופיע כפתור בשם **ייבוא מ-Pdf** בכל הדפים שנוצרו באמצעות התבנית הזו. כל אחד יכול פשוט ללחוץ על הכפתור ולייבא את תוכן מסמך PDF.

## הדגמת וידאו

אנא צפה [בווידאו](https://www.youtube.com/watch?v=zmZTJ86B25E) למטה כדי לראות את המודול בפעולה.

## תמיכה, הרחבה ותרומה

### תמיכה

מהימים הראשונים של Aspose, ידענו שלא יהיה מספיק רק לתת ללקוחות שלנו מוצרים טובים.
מהימים הראשונים של Aspose, ידענו שלתת ללקוחות שלנו מוצרים טובים לא יהיה מספיק.

לכן אנו מציעים תמיכה חינם. כל מי שמשתמש במוצר שלנו, בין אם קנה אותו או שהוא משתמש בהערכה, ראוי לתשומת לב מלאה ולכבוד.

תוכלו לרשום כל בעיה או הצעה הקשורה ל-Aspose.PDF .NET עבור מודולים של Umbraco באחת מהפלטפורמות הבאות

- [CodePlex](https://asposeumbraco.codeplex.com/workitem/list/basic)
- [Github](https://github.com/asposemarketplace/Aspose_for_Umbraco/issues)
- [Sourceforge](https://sourceforge.net/p/asposeumbraco/tickets/?source=navbar)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-umbraco/issues?status=new&status=open)

#### ייבוא מ-Pdf

- [רשת המפתחים של מיקרוסופט - שאלות ותשובות](https://code.msdn.microsoft.com/Umbraco-Import-from-Pdf-d4659bc8/view/Discussions#content)

### הרחב ותרום

Aspose .NET PDF Import עבור Umbraco הוא קוד פתוח וקוד המקור שלו זמין באתרי הקוד החברתיים המובילים המפורטים למטה.
Aspose .NET PDF Import for Umbraco הוא קוד פתוח וקוד המקור שלו זמין באתרי הקוד החברתיים המובילים המפורטים למטה.

#### קוד מקור

ניתן לקבל את קוד המקור העדכני ביותר מאחת מהמיקומים הבאים

- [CodePlex](https://asposeumbraco.codeplex.com/SourceControl/latest)
- [Github](https://github.com/asposemarketplace/Aspose_for_Umbraco)
- [Sourceforge](https://sourceforge.net/p/asposeumbraco/code/ci/master/tree/)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-umbraco/src)

#### כיצד להגדיר את קוד המקור

עליך להתקין את התוכנות הבאות כדי לפתוח ולהרחיב את קוד המקור

- Visual Studio 2010 או גרסה גבוהה יותר

אנא עקוב אחר השלבים הפשוטים הבאים כדי להתחיל

1. הורד/שכפל את קוד המקור.
1. פתח את Visual Studio 2010 ובחר **File** > **Open Project**
1. עיין אל קוד המקור העדכני ביותר שהורדת ופתח את **Aspose.Import from PDF.sln**
