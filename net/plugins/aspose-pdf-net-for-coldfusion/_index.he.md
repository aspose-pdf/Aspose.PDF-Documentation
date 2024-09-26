---
title: שימוש ב-Aspose.Pdf עבור .NET עם Coldfusion
type: docs
weight: 300
url: /net/using-aspose-pdf-for-net-with-coldfusion/
description: עליך לעבוד עם Aspose.Pdf עבור .NET עם Coldfusion באמצעות מחלקת PdfFileInfo
lastmod: "2021-07-14"
draft: false
---

{{% alert color="primary" %}}

במאמר זה נסביר איך להשתמש ב-Aspose.PDF עבור .NET עם Coldfusion. זה יעזור לך להבין את פרטי השילוב של Aspose.PDF עבור .Net ו-Coldfusion. בעזרת דוגמה פשוטה, אראה לך את התהליך של כללת פונקציונליות של Aspose.PDF עבור .Net באפליקציות Coldfusion שלך.

{{% /alert %}}

## רקע

Aspose.PDF עבור .NET הוא רכיב שגם מספק את היכולת לערוך ולשנות קבצי PDF קיימים.
Aspose.PDF for .NET הוא רכיב שמספק גם את היכולת לערוך ולשנות קבצי PDF קיימים.

## דרישות מוקדמות

כדי להפעיל את Aspose.PDF עבור .Net עם Coldfusion, תצטרך IIS, .Net 2.0, ו-Coldfusion. בדקתי את הרכיב באמצעות IIS 5, .Net 2.0, ו-Coldfusion 8. ישנם שני דברים נוספים שעליך לוודא בעת התקנת Coldfusion. ראשית, עליך לציין איזה אתרים תחת IIS יריצו את Coldfusion. שנית, תצטרך לבחור ב-'שירותי אינטגרציה של .Net' ממתקין Coldfusion. שירותי האינטגרציה של .Net מאפשרים לך לגשת להרכבת רכיבי .Net ביישומי Coldfusion; במקרה זה הרכיב יהיה Aspose.PDF עבור .NET.

## הסבר

ראשית כל, עליך להעתיק את ה-DLL (Aspose.PDF.dll) למיקום ממנו תגיש לו לשימוש מאוחר יותר; זה יוגדר כנתיב ויוקצה לתכונת ה-assembly של תג cfobject כפי שמוצג למטה:

```html
<cfobject type = ".NET" name = "fileinfo" 
        class = "Aspose.PDF.Facades.PdfFileInfo" 
        assembly = "C:/Aspose/Net/Assembly/Aspose.PDF.dll">
```
מאפיין ה-class בתג המופיע לעיל מצביע על המחלקה Aspose.PDF. Facades, שבמקרה זה היא PdfFileInfo. מאפיין ה-name הוא שם המופע של המחלקה וישמש בהמשך בקוד לגישה לשיטות או לתכונות של המחלקה. מאפיין ה-type מציין את סוג הרכיב - במקרה שלנו זה .Net.

נקודה חשובה שיש לזכור בעת שימוש ברכיב .Net ב-Coldfusion היא, שכאשר אתה מקבל או מגדיר כל תכונה של אובייקט המחלקה, עליך לעקוב אחר מבנה מסוים. להגדרת תכונה תשתמש בתחביר Set_propertyname, ולקבלת ערך תכונה תשתמש בתחביר Get_propertyname.

לדוגמה

הגדר ערך תכונה:

```html
<cfset FilePath = ExpandPath("guide.pdf")>
```

קבל ערך תכונה:

```html
<cfoutput>#fileinfo.Get_title()#</cfoutput>
```

דוגמה בסיסית אך מלאה לסייע לך להבין את התהליך של שימוש ב-Aspose.PDF עבור .NET ב-Coldfusion מוצגת להלן.

### בואו נציג מידע על קובץ PDF

```html
<!--- יצירת מופע של מחלקת PdfFileInfo --->

<cfobject type = ".NET" name = "fileinfo" class = "Aspose.PDF.Facades.PdfFileInfo"

assembly = "C:/Aspose/Net/Assembly/Aspose.PDF.dll">

<!--- קבלת נתיב קובץ ה-pdf --->

<cfset FilePath = ExpandPath("guide.pdf")>

<!--- הקצאת נתיב קובץ ה-pdf לאובייקט המחלקה על ידי הגדרת התכונה inputfile--->

<cfset fileinfo.Set_inputfile(FilePath)>

<!--- הצגת מידע על הקובץ --->

<cfoutput><b>כותרת:</b>#fileinfo.Get_title()#</cfoutput><br/>
<cfoutput><b>נושא:</b>#fileinfo.Get_subject()#</cfoutput><br/>
<cfoutput><b>מחבר:</b>#fileinfo.Get_author()#</cfoutput><br/>
<cfoutput><b>יוצר:</b>#fileinfo.Get_Creator()#</cfoutput><br/>

```
## סיכום

{{% alert color="primary" %}}
במאמר זה ראינו שאם אנו עוקבים אחר כמה כללים בסיסיים של אינטגרציה בין Coldfusion ל-.Net, נוכל לשלב הרבה פונקציונליות וגמישות בנוגע לניהול מסמכי PDF, באמצעות Aspose.PDF ל-.NET באפליקציות Coldfusion שלנו.
{{% /alert %}}
