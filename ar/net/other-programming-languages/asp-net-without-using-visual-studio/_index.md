---
title: ASP.NET بدون استخدام Visual Studio
type: docs
weight: 60
url: ar/net/asp-net-without-using-visual-studio/
---

{{% alert color="primary" %}}

[Aspose.PDF for .NET](/pdf/net/) يمكن استخدامه لتطوير صفحات أو تطبيقات ASP.NET بدون استخدام Visual Studio. في هذا المثال، سنكتب HTML وكود C# أو VB.NET في ملف .aspx واحد؛ وهذا ما يعرف عادة بـ ASP.NET الفوري.

{{% /alert %}}

## تفاصيل التنفيذ

{{% alert color="primary" %}}

قم بإنشاء تطبيق ويب نموذجي وانسخ Aspose.PDF.dll إلى دليل يسمى "Bin" في دليل موقع الويب الخاص بك ( *إذا لم يكن هناك مجلد bin، قم بإنشاء واحد* ). ثم قم بإنشاء صفحة .aspx الخاصة بك وانسخ الكود التالي فيها.
هذا المثال يوضح كيفية استخدام [Aspose.PDF for .NET](/pdf/net/) مع كود مضمن في صفحة ASP.NET من أجل إنشاء مستند PDF بسيط يحتوي على بعض النصوص النموذجية داخله.
{{% /alert %}}

```cs

<%@ Page Language ="C#" %>
<%@ Import Namespace="System" %>
<%@ Import Namespace="System.IO" %>
<%@ Import Namespace="System.Data" %>
<%@ Import Namespace="Aspose.PDF" %>

<html>
    <head>
        <title> باستخدام Aspose.PDF for .NET مع ASP.NET المضمن</title>
    </head>
    <body>
        <h3>إنشاء مستند PDF بسيط باستخدام Aspose.PDF for .NET مع ASP.NET المضمن</h3>
<%
    // تعيين الترخيص
    Aspose.PDF.License lic = new Aspose.PDF.License();
    lic.SetLicense("D:\\ASPOSE\\Licences\\Aspose.Total licenses\\Aspose.Total.lic");

    // تهيئة كائن المستند
    Document document = new Document();
    // إضافة صفحة
    Page page = document.Pages.Add();
    // إضافة نص إلى الصفحة الجديدة
    page.Paragraphs.Add(new Aspose.Pdf.Text.TextFragment("مرحباً بالعالم!"));
    // حفظ PDF المحدث
    var outputFileName = Path.Combine(_dataDir, "HelloWorld_out.pdf");
    document.Save( outputFileName );
%>

    </body>
</html>
```

