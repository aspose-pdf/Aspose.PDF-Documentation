---
title: ASP.NET ללא שימוש ב-Visual Studio
type: docs
weight: 60
url: /net/asp-net-without-using-visual-studio/
---

{{% alert color="primary" %}}

[Aspose.PDF for .NET](/pdf/net/) ניתן לשימוש עבור פיתוח דפי ASP.NET או אפליקציות ללא שימוש ב-Visual Studio. בדוגמה זו, נכתוב HTML וקוד C# או VB.NET בקובץ .aspx יחיד; זה ידוע בדרך כלל כ-Instant ASP.NET.

{{% /alert %}}

## פרטי היישום

{{% alert color="primary" %}}

צור אפליקציית ווב לדוגמה והעתק את Aspose.PDF.dll לתיקייה בשם "Bin" בתיקיית האתר שלך ( *אם תיקיית bin אינה קיימת, צור אחת* ). לאחר מכן צור את דף ה-.aspx שלך והעתק את הקוד הבא לתוכו.
הדוגמה מראה כיצד להשתמש ב-[Aspose.PDF for .NET](/pdf/net/) עם קוד מוטמע בדף ASP.NET על מנת ליצור מסמך PDF פשוט עם טקסט לדוגמה בתוכו.
{{% /alert %}}

```cs

<%@ Page Language ="C#" %>
<%@ Import Namespace="System" %>
<%@ Import Namespace="System.IO" %>
<%@ Import Namespace="System.Data" %>
<%@ Import Namespace="Aspose.PDF" %>

<html>
    <head>
        <title> שימוש ב-Aspose.PDF for .NET עם ASP.NET מוטמע</title>
    </head>
    <body>
        <h3>יצירת מסמך PDF פשוט בעת שימוש ב-Aspose.PDF for .NET עם ASP.NET מוטמע</h3>
<%
    // הגדר רישיון
    Aspose.PDF.License lic = new Aspose.PDF.License();
    lic.SetLicense("D:\\ASPOSE\\Licences\\Aspose.Total licenses\\Aspose.Total.lic");

    // אתחל אובייקט מסמך
    Document document = new Document();
    // הוסף עמוד
    Page page = document.Pages.Add();
    // הוסף טקסט לעמוד החדש
    page.Paragraphs.Add(new Aspose.Pdf.Text.TextFragment("שלום עולם!"));
    // שמור את ה-PDF המעודכן
    var outputFileName = Path.Combine(_dataDir, "HelloWorld_out.pdf");
    document.Save( outputFileName );
%>

    </body>
</html>
```

