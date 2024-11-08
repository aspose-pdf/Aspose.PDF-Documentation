---
title: ASP - VBScript عبر COM Interop
type: docs
weight: 30
url: /ar/net/asp-vbscript-via-com-interop/
---

## المتطلبات الأساسية

{{% alert color="primary" %}}

    يرجى التحقق من المقالة بعنوان استخدام Aspose.pdf لـ .NET عبر COM Interop.

{{% /alert %}}

## مثال "Hello World!" باستخدام VB Script

{{% alert color="primary" %}}

هذا تطبيق ASP بسيط يوضح كيفية إنشاء ملف PDF بنص عينة باستخدام [Aspose.PDF for .NET](/pdf/ar/net/) وVBScript عبر COM Interop.

{{% /alert %}}

```vb

<%@ LANGUAGE = VBScript %>
<% Option Explicit %>
<html>
    <head>
        <title> استخدام Aspose.PDF لـ .NET في نموذج ASP التقليدي</title>
    </head>
<body>

<h3>إنشاء مستند PDF عينة باستخدام Aspose.PDF لـ .NET مع ASP التقليدي وVBScript</h3>

<%

'تعيين الترخيص
Dim lic
Set lic = CreateObject("Aspose.PDF.License")
lic.SetLicense("D:\ASPOSE\Licences\Aspose.Total licenses\Aspose.Total.lic")

'إنشاء مثيل Pdf عن طريق استدعاء مُنشئه الفارغ
Dim pdf
Set pdf = CreateObject("Aspose.PDF.Generator.Pdf")

'إنشاء قسم جديد في كائن Pdf
Dim pdfsection
Set pdfsection = CreateObject("Aspose.PDF.Generator.Section")

'إضافة القسم إلى كائن Pdf
pdf.Sections.Add(pdfsection)

'إنشاء كائن نص
Dim SampleText
Set SampleText = CreateObject("Aspose.PDF.Generator.Text")

'إضافة جزء نصي إلى كائن النص
Dim seg1
Set seg1 = CreateObject("Aspose.PDF.Generator.Segment")

'تعيين بعض المحتوى للجزء
seg1.Content = "HelloWorld باستخدام ASP وVBScript"

'إضافة الجزء (بلون نص أحمر) إلى الفقرة
SampleText.Segments.Add(seg1)

'إضافة فقرة النص إلى مجموعة الفقرات لقسم
pdfsection.Paragraphs.Add(SampleText)

'حفظ مستند PDF
pdf.Save("d:\pdftest\HelloWorldinASP.pdf")

%>

    </body>
</html>
```
## استخراج النص باستخدام VBScript

{{% alert color="primary" %}}
    يقوم هذا النموذج من VBScript باستخراج النص من مستند PDF موجود عبر COM Interop.
    خطأ في تقديم ماكرو 'code' : تم تحديد قيمة غير صالحة لمعامل lang
{{% /alert %}}
