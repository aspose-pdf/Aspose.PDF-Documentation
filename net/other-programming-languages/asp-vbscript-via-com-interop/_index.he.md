---
title: ASP - VBScript דרך COM Interop
type: docs
weight: 30
url: /net/asp-vbscript-via-com-interop/
---

## דרישות מוקדמות

{{% alert color="primary" %}}

    אנא בדוק את המאמר בשם שימוש ב-Aspose.pdf עבור .NET דרך COM Interop.

{{% /alert %}}

## דוגמת Hello World! ב- VB Script

{{% alert color="primary" %}}

זוהי יישום ASP פשוט המראה כיצד ליצור קובץ PDF עם טקסט לדוגמה באמצעות [Aspose.PDF עבור .NET](/pdf/net/) ו- VBScript דרך COM Interop.

{{% /alert %}}

```vb

<%@ LANGUAGE = VBScript %>
<% Option Explicit %>
<html>
    <head>
        <title> שימוש ב-Aspose.PDF עבור .NET בדוגמת ASP קלאסית</title>
    </head>
<body>

<h3>יצירת מסמך PDF לדוגמה בעת שימוש ב-Aspose.PDF עבור .NET עם ASP קלאסי ו-VBScript</h3>

<%

'הגדרת רישיון
Dim lic
Set lic = CreateObject("Aspose.PDF.License")
lic.SetLicense("D:\ASPOSE\Licences\Aspose.Total licenses\Aspose.Total.lic")

'יצירת מופע Pdf על ידי קריאה לבנאי הריק שלו
Dim pdf
Set pdf = CreateObject("Aspose.PDF.Generator.Pdf")

'יצירת סעיף חדש באובייקט Pdf
Dim pdfsection
Set pdfsection = CreateObject("Aspose.PDF.Generator.Section")

'הוספת הסעיף לאובייקט Pdf
pdf.Sections.Add(pdfsection)

'יצירת אובייקט טקסט
Dim SampleText
Set SampleText = CreateObject("Aspose.PDF.Generator.Text")

'הוספת קטע טקסט לאובייקט הטקסט
Dim seg1
Set seg1 = CreateObject("Aspose.PDF.Generator.Segment")

'הקצאת תוכן לקטע
seg1.Content = "HelloWorld באמצעות ASP ו-VBScript"

'הוספת הקטע (עם צבע טקסט אדום) לפסקה
SampleText.Segments.Add(seg1)

'הוספת פסקת טקסט לאוסף הפסקאות של סעיף
pdfsection.Paragraphs.Add(SampleText)

'שמירת מסמך ה-PDF
pdf.Save("d:\pdftest\HelloWorldinASP.pdf")

%>

    </body>
</html>
```
## חילוץ טקסט באמצעות VBScript

{{% alert color="primary" %}}
    דוגמת VBScript זו מחלצת טקסט ממסמך PDF קיים באמצעות COM Interop.
    שגיאה בעת עיבוד המאקרו 'code' : ערך לא תקין שצוין עבור פרמטר lang
{{% /alert %}}
