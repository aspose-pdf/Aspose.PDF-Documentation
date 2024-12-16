---
title: ASP - JScript via COM Interop
type: docs
weight: 40
url: /ar/net/asp-jscript-via-com-interop/
---
{{% alert color="primary" %}}

هذا تطبيق ASP بسيط يُظهر لك كيفية إضافة نص بسيط إلى ملف PDF باستخدام [Aspose.PDF لـ .NET](/pdf/ar/net/) و JScript عبر COM Interop.

{{% /alert %}}

مثال:

{{% alert color="primary" %}}

```javascript
<%@ LANGUAGE = JScript %>
<html>
    <head>
        <title> استخدام Aspose.PDF لـ .NET في مثال ASP التقليدي</title>
    </head>
    <body>
        <h3>إنشاء مستند PDF عينة باستخدام Aspose.PDF لـ .NET مع ASP التقليدي وJScript</h3>
<%
// تعيين الترخيص
var lic = Server.CreateObject("Aspose.PDF.License");
lic.SetLicense("D:\\ASPOSE\\Aspose.Total.lic");

// تكوين نموذج Pdf عن طريق استدعاء مُنشئه الفارغ
var pdf = Server.CreateObject("Aspose.PDF.Document");

// إنشاء صفحة جديدة في كائن PDF
var pdfpage = pdf.Pages.Add();

// إنشاء كائن Fragment النصي
var sampleText = Server.CreateObject("Aspose.Pdf.Text.TextFragment");

// تعيين بعض المحتوى للFragment
sampleText.Text = "HelloWorld باستخدام ASP وJScript";

// إضافة فقرة نصية إلى مجموعة فقرات القسم
pdfpage.Paragraphs.Add(sampleText);

// حفظ مستند PDF
pdf.Save("d:\\pdftest\\HelloWorldinASP.pdf");

%>
    </body>
</html>
```
{{% /alert %}}
