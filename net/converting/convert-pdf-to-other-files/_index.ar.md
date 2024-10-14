---
title: تحويل PDF إلى EPUB، LaTeX، نص، XPS في C#
linktitle: تحويل PDF إلى صيغ أخرى
type: docs
weight: 90
url: /net/convert-pdf-to-other-files/
lastmod: "2021-11-01"
keywords: convert, PDF, EPUB, LaText, Text, XPS, C#
description: يوضح لك هذا الموضوع كيفية تحويل ملف PDF إلى صيغ ملفات أخرى مثل EPUB، LaTeX، النص، XPS إلخ باستخدام C# أو .NET.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## تحويل PDF إلى EPUB

{{% alert color="success" %}}
**جرب تحويل PDF إلى EPUB عبر الإنترنت**

يقدم لك Aspose.PDF لـ .NET تطبيقًا مجانيًا عبر الإنترنت ["PDF إلى EPUB"](https://products.aspose.app/pdf/conversion/pdf-to-epub)، حيث يمكنك تجربة استكشاف الوظائف والجودة التي يعمل بها.

[![تحويل Aspose.PDF PDF إلى EPUB بواسطة تطبيق مجاني](pdf_to_epub.png)](https://products.aspose.app/pdf/conversion/pdf-to-epub)
{{% /alert %}}

**<abbr title="النشر الإلكتروني">EPUB</abbr>** هو معيار كتاب إلكتروني مجاني ومفتوح من منتدى النشر الرقمي الدولي (IDPF).
**<abbr title="النشر الإلكتروني">EPUB</abbr>** هو معيار مجاني ومفتوح للكتب الإلكترونية من منتدى النشر الرقمي الدولي (IDPF).
تم تصميم EPUB للمحتوى القابل لإعادة التدفق، مما يعني أن قارئ EPUB يمكنه تحسين النص لجهاز عرض معين. كما يدعم EPUB المحتوى ذو التخطيط الثابت. يُعتبر الشكل كشكل واحد يمكن للناشرين وبيوت التحويل استخدامه داخليًا، بالإضافة إلى الاستخدام في التوزيع والبيع. يحل محل معيار الكتاب الإلكتروني المفتوح.

الكود التالي يعمل أيضًا مع مكتبة [Aspose.PDF.Drawing](/pdf/net/drawing/).

يدعم Aspose.PDF لـ .NET أيضًا ميزة تحويل مستندات PDF إلى تنسيق EPUB. يحتوي Aspose.PDF لـ .NET على فئة تُسمى EpubSaveOptions والتي يمكن استخدامها كالوسيط الثاني في طريقة [`Document.Save(..)`](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save/index)، لتوليد ملف EPUB.
يرجى محاولة استخدام الكود التالي لتحقيق هذا المطلب باستخدام C#.

```csharp
// للأمثلة الكاملة وملفات البيانات، يرجى زيارة https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// مسار دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();
// تحميل مستند PDF
Document pdfDocument = new Document(dataDir + "PDFToEPUB.pdf");
// إنشاء خيارات حفظ Epub
EpubSaveOptions options = new EpubSaveOptions();
// تحديد التخطيط للمحتويات
options.ContentRecognitionMode = EpubSaveOptions.RecognitionMode.Flow;
// حفظ مستند ePUB
pdfDocument.Save(dataDir + "PDFToEPUB_out.epub", options);
```
## تحويل PDF إلى LaTeX/TeX

**Aspose.PDF لـ .NET** يدعم تحويل PDF إلى LaTeX/TeX.
صيغة ملف LaTeX هي صيغة ملف نصي مع وسم خاص وتُستخدم في نظام إعداد الوثائق المعتمد على TeX للتنضيد عالي الجودة.

{{% alert color="success" %}}
**جرب تحويل PDF إلى LaTeX/TeX عبر الإنترنت**

يقدم Aspose.PDF لـ .NET تطبيقًا مجانيًا عبر الإنترنت ["PDF إلى LaTeX"](https://products.aspose.app/pdf/conversion/pdf-to-tex)، حيث يمكنك التحقق من الوظائف وجودة عمله.

[![تحويل Aspose.PDF لملف PDF إلى LaTeX/TeX بتطبيق مجاني](pdf_to_latex.png)](https://products.aspose.app/pdf/conversion/pdf-to-tex)
{{% /alert %}}

لتحويل ملفات PDF إلى TeX، يحتوي Aspose.PDF على الفئة [LaTeXSaveOptions](https://reference.aspose.com/pdf/net/aspose.pdf/latexsaveoptions) التي توفر خاصية OutDirectoryPath لحفظ الصور المؤقتة أثناء عملية التحويل.

يوضح الكود التالي عملية تحويل ملفات PDF إلى صيغة TEX باستخدام C#.

```csharp
// للأمثلة الكاملة وملفات البيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// المسار إلى دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

// إنشاء كائن Document
Aspose.Pdf.Document doc = new Aspose.Pdf.Document(dataDir + "PDFToTeX.pdf");

// توثيق خيار حفظ LaTex          
LaTeXSaveOptions saveOptions = new LaTeXSaveOptions();

// تحديد دليل الإخراج
string pathToOutputDirectory = dataDir;

// تعيين مسار دليل الإخراج لكائن خيار الحفظ
saveOptions.OutDirectoryPath = pathToOutputDirectory;

// حفظ ملف PDF في صيغة LaTex           
doc.Save(dataDir + "PDFToTeX_out.tex", saveOptions);
```
## تحويل PDF إلى نص

**Aspose.PDF لـ .NET** يدعم تحويل كامل مستند PDF وصفحة واحدة إلى ملف نصي.

### تحويل كامل مستند PDF إلى ملف نصي

يمكنك تحويل مستند PDF إلى ملف TXT باستخدام طريقة [Visit](https://reference.aspose.com/pdf/net/aspose.pdf.text/textabsorber/methods/visit/index) لفئة [TextAbsorber](https://reference.aspose.com/pdf/net/aspose.pdf.text/textabsorber).

الشفرة التالية تشرح كيفية استخراج النصوص من جميع الصفحات.

```csharp
public static void ConvertPDFDocToTXT()
{
    // فتح المستند
    Document pdfDocument = new Document(_dataDir + "demo.pdf");
    TextAbsorber ta = new TextAbsorber();
    ta.Visit(pdfDocument);
    // حفظ النص المستخرج في ملف نصي
    File.WriteAllText(_dataDir + "input_Text_Extracted_out.txt",ta.Text);
}
```

{{% alert color="success" %}}
**جرب تحويل PDF إلى نص عبر الإنترنت**

Aspose.PDF لـ .NET يقدم لك تطبيق مجاني عبر الإنترنت ["PDF to Text"](https://products.aspose.app/pdf/conversion/pdf-to-txt)، حيث يمكنك تجربة استكشاف الوظائف والجودة التي يعمل بها.
Aspose.PDF لـ .NET يقدم لك تطبيقًا مجانيًا عبر الإنترنت ["PDF إلى نص"](https://products.aspose.app/pdf/conversion/pdf-to-txt)، حيث يمكنك تجربة استكشاف الوظائف والجودة التي يعمل بها.

[![Aspose.PDF تحويل PDF إلى نص بواسطة التطبيق المجاني](pdf_to_text.png)](https://products.aspose.app/pdf/conversion/pdf-to-txt)
{{% /alert %}}

### تحويل صفحة PDF إلى ملف نصي

يمكنك تحويل مستند PDF إلى ملف TXT باستخدام Aspose.PDF لـ .NET. يجب عليك استخدام طريقة `Visit` لفئة `TextAbsorber` لحل هذه المهمة.

يشرح الكود التالي كيفية استخراج النصوص من الصفحات المحددة.

```csharp
public static void ConvertPDFPagestoTXT()
{
    Document pdfDocument = new Document(System.IO.Path.Combine(_dataDir, "demo.pdf"));
    TextAbsorber ta = new TextAbsorber();
    var pages = new [] {1, 3, 4};
    foreach (var page in pages)
    {
        ta.Visit(pdfDocument.Pages[page]);
    }
   
    // حفظ النص المستخرج في ملف نصي
    File.WriteAllText(System.IO.Path.Combine(_dataDir, "input_Text_Extracted_out.txt"), ta.Text);
}
```
## تحويل PDF إلى XPS

**Aspose.PDF لـ .NET** يُتيح إمكانية تحويل ملفات PDF إلى تنسيق <abbr title="مواصفات الورق XML">XPS</abbr>. دعونا نجرب استخدام قطعة الكود المعروضة لتحويل ملفات PDF إلى تنسيق XPS باستخدام C#.

{{% alert color="success" %}}
**جرب تحويل PDF إلى XPS عبر الإنترنت**

يقدم Aspose.PDF لـ .NET تطبيقًا مجانيًا عبر الإنترنت ["PDF إلى XPS"](https://products.aspose.app/pdf/conversion/pdf-to-xps)، حيث يمكنك تجربة استكشاف الوظائف والجودة التي يعمل بها.

[![Aspose.PDF تحويل PDF إلى XPS بتطبيق مجاني](pdf_to_xps.png)](https://products.aspose.app/pdf/conversion/pdf-to-xps)
{{% /alert %}}

نوع ملف XPS مرتبط أساسًا بمواصفات الورق XML التي تقدمها Microsoft Corporation. مواصفات الورق XML (XPS)، التي كانت تُعرف سابقًا بالاسم الرمزي Metro وتضم مفهوم التسويق لمسار الطباعة الجيل القادم (NGPP)، هي مبادرة من Microsoft لدمج إنشاء وعرض المستندات في نظام التشغيل Windows.

لتحويل ملفات PDF إلى XPS، يحتوي Aspose.PDF على الفئة [XpsSaveOptions](https://reference.aspose.com/net/pdf/aspose.pdf/xpssaveoptions) التي تُستخدم كالوسيط الثاني للدالة [Document.Save(..)](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save/index) لتوليد ملف XPS.
لتحويل ملفات PDF إلى XPS، تستخدم Aspose.PDF الفئة [XpsSaveOptions](https://reference.aspose.com/net/pdf/aspose.pdf/xpssaveoptions) التي تستخدم كالوسيطة الثانية للطريقة [Document.Save(..)](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save/index) لتوليد ملف XPS.

يوضح الجزء التالي من الشيفرة عملية تحويل ملف PDF إلى صيغة XPS.

```csharp
// للحصول على أمثلة كاملة وملفات بيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// المسار إلى مجلد الوثائق.
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

// تحميل مستند PDF
Document pdfDocument = new Document(dataDir + "input.pdf");

// إنشاء خيارات حفظ XPS
Aspose.Pdf.XpsSaveOptions saveOptions = new Aspose.Pdf.XpsSaveOptions();
// حفظ المستند XPS
pdfDocument.Save("PDFToXPS_out.xps", saveOptions)
```
