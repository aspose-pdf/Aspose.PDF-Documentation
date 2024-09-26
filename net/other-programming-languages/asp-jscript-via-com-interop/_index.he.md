---
title: ASP - JScript דרך COM Interop
type: docs
weight: 40
url: /net/asp-jscript-via-com-interop/
---
{{% alert color="primary" %}}

זוהי יישום ASP פשוט המראה איך להוסיף מחרוזת טקסט פשוטה לקובץ PDF באמצעות [Aspose.PDF ל-.NET](/pdf/net/) ו-JScript דרך COM Interop.

{{% /alert %}}

דוגמה:

{{% alert color="primary" %}}

```javascript
<%@ LANGUAGE = JScript %>
<html>
    <head>
        <title> שימוש ב-Aspose.PDF ל-.NET בדוגמת ASP קלאסית</title>
    </head>
    <body>
        <h3>יצירת מסמך PDF דוגמתי בעת שימוש ב-Aspose.PDF ל-.NET עם ASP קלאסי ו-JScript</h3>
<%
// הגדרת רישיון
var lic = Server.CreateObject("Aspose.PDF.License");
lic.SetLicense("D:\\ASPOSE\\Aspose.Total.lic");

// יצירת מופע Pdf על ידי קריאה לבנאי הריק שלו
var pdf = Server.CreateObject("Aspose.PDF.Document");

// יצירת דף חדש באובייקט PDF
var pdfpage = pdf.Pages.Add();

// יצירת אובייקט פרגמנט טקסט
var sampleText = Server.CreateObject("Aspose.Pdf.Text.TextFragment");

// הקצאת תוכן לפרגמנט
sampleText.Text = "HelloWorld בשימוש ב-ASP ו-JScript";

// הוספת פסקת טקסט לאוסף הפסקאות של סעיף
pdfpage.Paragraphs.Add(sampleText);

// שמירת מסמך ה-PDF
pdf.Save("d:\\pdftest\\HelloWorldinASP.pdf");

%>
    </body>
</html>
```
{{% /alert %}}
