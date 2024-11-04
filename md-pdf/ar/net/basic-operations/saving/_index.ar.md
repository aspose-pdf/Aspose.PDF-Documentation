---
title: حفظ مستند PDF برمجيًا
linktitle: حفظ PDF
type: docs
weight: 30
url: /net/save-pdf-document/
description: تعلم كيفية حفظ ملف PDF في مكتبة Aspose.PDF لـ .NET. حفظ مستند PDF إلى نظام الملفات، إلى تيار، وفي تطبيقات الويب.
aliases:
    - /net/saving/
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

الشفرة البرمجية التالية تعمل أيضًا مع واجهة [Aspose.Drawing](/pdf/net/drawing/) الرسومية الجديدة.

## حفظ مستند PDF إلى نظام الملفات

يمكنك حفظ المستند PDF المُنشأ أو المُعدل إلى نظام الملفات باستخدام طريقة `Save` من فئة `Document`.
عندما لا تقدم نوع الصيغة (الخيارات)، يتم حفظ المستند بصيغة Aspose.PDF الإصدار 1.7 (*.pdf).

```csharp
public static void SaveDocument()
{
    var originalFileName = Path.Combine(_dataDir, "SimpleResume.pdf");
    var modifiedFileName = Path.Combine(_dataDir, "SimpleResumeModified.pdf");

    var pdfDocument = new Aspose.Pdf.Document(originalFileName);
    // قم ببعض التلاعب، على سبيل المثال إضافة صفحة فارغة جديدة
    pdfDocument.Pages.Add();
    pdfDocument.Save(modifiedFileName);
}
```
## حفظ مستند PDF إلى تيار

يمكنك أيضاً حفظ المستند PDF الذي تم إنشاؤه أو تعديله إلى تيار باستخدام الأساليب المتعددة لطريقة `Save`.

```csharp
public static void SaveDocumentStream()
{
    var originalFileName = Path.Combine(_dataDir, "SimpleResume.pdf");
    var modifiedFileName = Path.Combine(_dataDir, "SimpleResumeModified.pdf");

    var pdfDocument = new Aspose.Pdf.Document(originalFileName);
    // إجراء بعض التعديلات، مثل إضافة صفحة فارغة جديدة
    pdfDocument.Pages.Add();
    pdfDocument.Save(System.IO.File.OpenWrite(modifiedFileName));
}
```

## حفظ مستند PDF في تطبيقات الويب

لحفظ المستندات في تطبيقات الويب، يمكنك استخدام الطرق المقترحة أعلاه. بالإضافة إلى ذلك، فإن فئة `Document` لديها طريقة محملة `Save` للاستخدام مع فئة [HttpResponse](https://docs.microsoft.com/en-us/dotnet/api/system.web.httpresponse?view=netframework-4.8).

```csharp
var originalFileName = Path.Combine(_dataDir, "SimpleResume.pdf");
var pdfDocument = new Aspose.Pdf.Document(originalFileName);
// إجراء بعض التعديلات، مثل إضافة صفحة فارغة جديدة
pdfDocument.Pages.Add();
pdfDocument.Save(Response, originalFileName, ContentDisposition.Attachment, new PdfSaveOptions());
```
لمزيد من التفاصيل يرجى متابعة قسم [العرض](/pdf/net/showcases/).

## حفظ بصيغة PDF/A أو PDF/X

PDF/A هي نسخة معيارية من ISO لصيغة مستندات PDF المحمولة المستخدمة في أرشفة وحفظ المستندات الإلكترونية لفترات طويلة.
تختلف PDF/A عن PDF في أنها تحظر ميزات غير مناسبة للأرشفة طويلة الأمد، مثل ربط الخطوط (بدلاً من تضمين الخطوط) والتشفير. تشتمل متطلبات ISO لمشاهدي PDF/A على إرشادات إدارة الألوان، ودعم الخطوط المضمنة، وواجهة مستخدم لقراءة التعليقات المضمنة.

PDF/X هو مجموعة فرعية من معيار PDF ISO. الغرض من PDF/X هو تسهيل تبادل الرسومات، ولذلك يحتوي على سلسلة من المتطلبات المتعلقة بالطباعة والتي لا تنطبق على ملفات PDF القياسية.

في كلا الحالتين، يتم استخدام طريقة `Save` لتخزين المستندات، بينما يجب تحضير المستندات باستخدام طريقة `Convert`.

```csharp
public static void SaveDocumentAsPDFx()
{
    var pdfDocument = new Aspose.Pdf.Document("..\\..\\..\\Samples\\SimpleResume.pdf");
    pdfDocument.Pages.Add();
    pdfDocument.Convert(new PdfFormatConversionOptions(PdfFormat.PDF_X_3));
    pdfDocument.Save("..\\..\\..\\Samples\\SimpleResume_X3.pdf");
}
```


