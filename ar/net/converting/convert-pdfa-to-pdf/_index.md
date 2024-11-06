---
title: تحويل من تنسيق PDF/A إلى تنسيق PDF
linktitle: تحويل من تنسيق PDF/A إلى تنسيق PDF
type: docs
weight: 110
url: ar/net/convert-pdfa-to-pdf/
lastmod: "2021-11-01"
description: يوضح هذا الموضوع كيفية السماح Aspose.PDF بتحويل ملف PDF/A إلى مستند PDF باستخدام مكتبة .NET.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

الشفرة التالية تعمل أيضًا مع مكتبة [Aspose.PDF.Drawing](/pdf/net/drawing/).

## تحويل مستند PDF/A إلى PDF

تحويل مستند PDF/A إلى PDF يعني إزالة قيود <abbr title="Portable Document Format Archive">PDF/A</abbr> من المستند الأصلي.
الفئة [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) تحتوي على طريقة [RemovePdfaCompliance(..)](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/removepdfacompliance) لإزالة معلومات الالتزام بـ PDF من ملف المصدر.

```csharp
public static void ConvertPDFAtoPDF()
{
    // للأمثلة الكاملة وملفات البيانات، يرجى زيارة https://github.com/aspose-pdf/Aspose.PDF-for-.NET
    Document pdfDocument = new Document(_dataDir + "PDFAToPDF.pdf");
    // إزالة معلومات الالتزام بـ PDF/A
    pdfDocument.RemovePdfaCompliance();
    // حفظ المستند المحدث
    pdfDocument.Save(_dataDir + "PDFAToPDF_out.pdf");
}
```
هذه المعلومات تُزال أيضًا إذا أجريت أي تغييرات في المستند (مثل إضافة صفحات). في المثال التالي، يفقد المستند الناتج المطابقة لمعيار PDF/A بعد إضافة صفحة.

```csharp
public static void ConvertPDFAtoPDFAdvanced()
{
    // للحصول على أمثلة كاملة وملفات بيانات، يرجى زيارة https://github.com/aspose-pdf/Aspose.PDF-for-.NET
    Document pdfDocument = new Document(_dataDir + "PDFAToPDF.pdf");
    // إضافة صفحة جديدة (فارغة) تزيل معلومات مطابقة PDF/A.
    pdfDocument.Pages.Add();
    // حفظ المستند المحدث
    pdfDocument.Save(_dataDir + "PDFAToPDF_out.pdf");
}
```
