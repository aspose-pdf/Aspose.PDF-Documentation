---
title: تحويل ملفات PDF إلى صيغ PDF/A
linktitle: تحويل ملفات PDF إلى صيغ PDF/A
type: docs
weight: 100
url: /net/convert-pdf-to-pdfa/
lastmod: "2021-11-01"
description: هذا الموضوع يوضح كيف يتيح Aspose.PDF تحويل ملف PDF إلى ملف PDF متوافق مع PDF/A.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

**Aspose.PDF لـ .NET** يتيح لك تحويل ملف PDF إلى ملف PDF متوافق مع <abbr title="Portable Document Format / A">PDF/A</abbr>. قبل القيام بذلك، يجب التحقق من صحة الملف. هذا الموضوع يشرح كيفية ذلك.

{{% alert color="primary" %}}

يرجى ملاحظة أننا نتبع Adobe Preflight للتحقق من مطابقة PDF/A. جميع الأدوات في السوق لها تمثيلها الخاص لمطابقة PDF/A. يرجى مراجعة هذا المقال عن أدوات التحقق من PDF/A للرجوع إليها. لقد اخترنا منتجات Adobe للتحقق من كيفية إنتاج Aspose.PDF لملفات PDF لأن Adobe تقع في مركز كل ما يتعلق بـ PDF.

{{% /alert %}}

قم بتحويل الملف باستخدام طريقة Convert للفئة Document.
{{% alert color="success" %}}
**جرب تحويل PDF إلى PDF/A عبر الإنترنت**

Aspose.PDF لـ .NET يقدم لك تطبيقًا مجانيًا عبر الإنترنت ["PDF to PDF/A-1A"](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a)، حيث يمكنك تجربة استكشاف الوظائف والجودة التي يعمل بها.

[![Aspose.PDF تحويل PDF إلى PDF/A بواسطة التطبيق المجاني](pdf_to_pdfa.png)](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a)
{{% /alert %}}

الشفرة التالية تعمل أيضًا مع مكتبة [Aspose.PDF.Drawing](/pdf/net/drawing/).

## تحويل ملف PDF إلى PDF/A-1b

الشفرة التالية توضح كيفية تحويل ملفات PDF إلى PDF متوافق مع PDF/A-1b.

```csharp
// للحصول على أمثلة كاملة وملفات بيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// المسار إلى دليل الوثائق.
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

// فتح المستند
Document pdfDocument = new Document(dataDir + "PDFToPDFA.pdf");
           
// تحويل إلى مستند متوافق مع PDF/A
// خلال عملية التحويل، يتم أيضًا أداء التحقق
pdfDocument.Convert(dataDir + "log.xml", PdfFormat.PDF_A_1B, ConvertErrorAction.Delete);

dataDir = dataDir + "PDFToPDFA_out.pdf";
// حفظ المستند الناتج
pdfDocument.Save(dataDir);
```
لأداء التحقق فقط، استخدم السطر التالي من الشفرة:

```csharp
// للأمثلة الكاملة وملفات البيانات، يرجى زيارة https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// مسار الدليل الخاص بالوثائق.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// فتح الوثيقة
Document pdfDocument = new Document(dataDir + "ValidatePDFAStandard.pdf");

// التحقق من صحة PDF لمعيار PDF/A-1a
pdfDocument.Validate(dataDir + "validation-result-A1A.xml", PdfFormat.PDF_A_1B);
```

## تحويل ملف PDF إلى PDF/A-3b

Aspose.PDF for .NET يدعم أيضًا خاصية تحويل ملف PDF إلى تنسيق PDF/A-3b.

```csharp
// للأمثلة الكاملة وملفات البيانات، يرجى زيارة https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// مسار الدليل الخاص بالوثائق.
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

// فتح الوثيقة
Document pdfDocument = new Document(dataDir + "input.pdf");           

pdfDocument.Convert(new MemoryStream(), PdfFormat.PDF_A_3B, ConvertErrorAction.Delete);

dataDir = dataDir + "PDFToPDFA3b_out.pdf";
// حفظ الوثيقة الناتجة
pdfDocument.Save(dataDir);
```
## تحويل ملف PDF إلى PDF/A-2u

يدعم Aspose.PDF لـ .NET أيضًا خاصية تحويل ملف PDF إلى تنسيق PDF/A-2u.

```csharp
string inFile = "input.pdf";
string outFile = "output.pdf";
Aspose.PDF.Document doc = new Aspose.PDF.Document(inFile);
doc.Convert(new MemoryStream(), PdfFormat.PDF_A_2U, ConvertErrorAction.Delete);
doc.Save(outFile);
```

## تحويل ملف PDF إلى PDF/A-3u

يدعم Aspose.PDF لـ .NET أيضًا خاصية تحويل ملف PDF إلى تنسيق PDF/A-3u.

```csharp
string inFile = "input.pdf";
string outFile = "output.pdf";
Aspose.PDF.Document doc = new Aspose.PDF.Document(inFile);
doc.Convert(new MemoryStream(), PdfFormat.PDF_A_3U, ConvertErrorAction.Delete);
doc.Save(outFile);
```

## إضافة مرفق إلى ملف PDF/A

في حال كان لديك متطلب لإرفاق ملفات إلى تنسيق PDF/A المتوافق، نوصي باستخدام قيمة PDF_A_3A من تعداد Aspose.PDF.PdfFormat.
PDF/A_3a هو التنسيق الذي يوفر خاصية إرفاق أي نوع ملف كمرفق لملف PDF/A المتوافق.

```csharp
```csharp
// للحصول على أمثلة كاملة وملفات بيانات، يرجى زيارة https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// مسار إلى مجلد الوثائق.
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

// توثيق مثيل Document لتحميل ملف موجود
Aspose.Pdf.Document doc = new Document(dataDir + "input.pdf");
// إعداد ملف جديد ليتم إضافته كمرفق
FileSpecification fileSpecification = new FileSpecification(dataDir + "aspose-logo.jpg", "ملف صورة كبير");
// إضافة المرفق إلى مجموعة مرفقات الوثيقة
doc.EmbeddedFiles.Add(fileSpecification);
// تنفيذ التحويل إلى PDF/A_3a حتى يتم تضمين المرفق في الملف الناتج
doc.Convert(dataDir + "log.txt", Aspose.Pdf.PdfFormat.PDF_A_3A, ConvertErrorAction.Delete);
// حفظ الملف الناتج
doc.Save(dataDir + "AddAttachmentToPDFA_out.pdf");
```

## استبدال الخطوط المفقودة بخطوط بديلة

وفقًا لمعايير PDFA، يجب تضمين الخطوط في مستند PDFA.
وفقًا لمعايير PDFA، يجب تضمين الخطوط في مستند PDFA.

```csharp
// للحصول على أمثلة كاملة وملفات البيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// المسار إلى دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

Aspose.Pdf.Text.Font originalFont = null;
try
{
    originalFont = FontRepository.FindFont("AgencyFB");
}
catch (Exception)
{
    // الخط مفقود على جهاز الوجهة
    FontRepository.Substitutions.Add(new SimpleFontSubstitution("AgencyFB", "Arial"));
}
var fileNew = new FileInfo(dataDir + "newfile_out.pdf");
var pdf = new Document(dataDir + "input.pdf");
pdf.Convert( dataDir +  "log.xml", PdfFormat.PDF_A_1B, ConvertErrorAction.Delete);
pdf.Save(fileNew.FullName);
```
