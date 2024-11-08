---
title: تحويل PDF إلى HTML في .NET
linktitle: تحويل PDF إلى تنسيق HTML
type: docs
weight: 50
url: /ar/net/convert-pdf-to-html/
lastmod: "2021-11-01"
description: يوضح هذا الموضوع كيفية تحويل ملف PDF إلى تنسيق HTML باستخدام مكتبة Aspose.PDF للغة C#.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## نظرة عامة

يشرح هذا المقال كيفية **تحويل PDF إلى HTML باستخدام C#**. يغطي الموضوعات التالية.

_التنسيق_: **HTML**
- [C# PDF إلى HTML](#csharp-pdf-to-html)
- [C# تحويل PDF إلى HTML](#csharp-pdf-to-html)
- [C# كيفية تحويل ملف PDF إلى HTML](#csharp-pdf-to-html)

يعمل الكود التالي أيضًا مع مكتبة [Aspose.PDF.Drawing](/pdf/ar/net/drawing/).

## تحويل PDF إلى HTML

**Aspose.PDF لـ .NET** يوفر العديد من الميزات لتحويل صيغ ملفات مختلفة إلى مستندات PDF وتحويل ملفات PDF إلى صيغ ناتجة مختلفة.
**Aspose.PDF لـ .NET** يوفر العديد من الميزات لتحويل مختلف صيغ الملفات إلى مستندات PDF وتحويل ملفات PDF إلى صيغ مخرجات متنوعة.

**Aspose.PDF لـ .NET** يدعم الميزات لتحويل ملف PDF إلى HTML. المهام الرئيسية التي يمكنك إنجازها باستخدام مكتبة Aspose.PDF مذكورة:

- تحويل PDF إلى HTML؛
- تقسيم الناتج إلى HTML متعدد الصفحات؛
- تحديد مجلد لتخزين ملفات SVG؛
- ضغط صور SVG أثناء التحويل؛
- تحديد مجلد الصور؛
- إنشاء ملفات لاحقة بمحتويات الجسم فقط؛
- عرض النصوص الشفافة؛
- عرض طبقات مستند PDF.

{{% alert color="success" %}}
**جرب تحويل PDF إلى HTML عبر الإنترنت**

يقدم Aspose.PDF لـ .NET تطبيقًا مجانيًا عبر الإنترنت ["PDF to HTML"](https://products.aspose.app/pdf/conversion/pdf-to-html)، حيث يمكنك تجربة استكشاف الوظائف وجودة عمله.

[![تحويل Aspose.PDF PDF إلى HTML بتطبيق مجاني](pdf_to_html.png)](https://products.aspose.app/pdf/conversion/pdf-to-html)
{{% /alert %}}

يوفر Aspose.PDF لـ .NET كود من سطرين لتحويل ملف PDF مصدر إلى HTML.
Aspose.PDF لـ .NET يوفر كود من سطرين لتحويل ملف PDF مصدر إلى HTML.

<a name="csharp-pdf-to-html"><strong>الخطوات: تحويل PDF إلى HTML في C#</strong></a>

1. إنشاء نموذج من الكائن [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document/) مع مستند PDF المصدر.
2. حفظه إلى صيغة **SaveFormat.Html** من خلال استدعاء طريقة **Document.Save()**.

```csharp
// للأمثلة الكاملة وملفات البيانات، يرجى زيارة https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// المسار إلى دليل الوثائق.
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

// فتح مستند PDF المصدر
Document pdfDocument = new Document(dataDir + "PDFToHTML.pdf");

// حفظ الملف بتنسيق مستند MS
pdfDocument.Save(dataDir + "output_out.html", SaveFormat.Html);
```

### تقسيم الناتج إلى HTML متعدد الصفحات

عند تحويل ملف PDF كبير يحتوي على عدة صفحات إلى تنسيق HTML، يظهر الناتج كصفحة HTML واحدة.
عند تحويل ملف PDF كبير الحجم ذو عدة صفحات إلى تنسيق HTML، تظهر النتيجة على شكل صفحة HTML واحدة.

```csharp
// للحصول على أمثلة كاملة وملفات البيانات، يرجى زيارة https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// المسار إلى دليل الوثائق.
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

// فتح مستند PDF المصدر
Document pdfDocument = new Document(dataDir + "PDFToHTML.pdf");

// إنشاء كائن خيارات حفظ HTML
HtmlSaveOptions htmlOptions = new HtmlSaveOptions();

// تحديد تقسيم الناتج إلى صفحات متعددة
htmlOptions.SplitIntoPages = true;

// حفظ المستند
pdfDocument.Save(@"MultiPageHTML_out.html", htmlOptions);
```

### حدد مجلد لتخزين ملفات SVG

أثناء تحويل PDF إلى HTML، من الممكن تحديد المجلد الذي يجب حفظ صور SVG فيه.
خلال تحويل PDF إلى HTML، من الممكن تحديد المجلد الذي يجب حفظ صور SVG فيه.

```csharp
// تحميل ملف PDF
Document doc = new Document(dataDir + "PDFToHTML.pdf");

// إنشاء كائن خيارات حفظ HTML
HtmlSaveOptions newOptions = new HtmlSaveOptions();

// تحديد المجلد حيث يتم حفظ صور SVG أثناء تحويل PDF إلى HTML
newOptions.SpecialFolderForSvgImages = dataDir;

// حفظ الملف الناتج
doc.Save(dataDir + "SaveSVGFiles_out.html", newOptions);
```

### ضغط صور SVG أثناء التحويل

لضغط صور SVG أثناء تحويل PDF إلى HTML، يرجى استخدام الكود التالي:

```csharp
// للحصول على أمثلة كاملة وملفات البيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// إنشاء HtmlSaveOption مع الميزة المختبرة
HtmlSaveOptions newOptions = new HtmlSaveOptions();

// ضغط صور SVG إذا كانت موجودة
newOptions.CompressSvgGraphicsIfAny = true;
```

### تحديد مجلد الصور

يمكننا أيضًا تحديد المجلد الذي سيتم حفظ الصور فيه أثناء تحويل PDF إلى HTML:
يمكننا أيضًا تحديد المجلد الذي سيتم حفظ الصور فيه أثناء تحويل PDF إلى HTML:

```csharp
// للحصول على أمثلة كاملة وملفات البيانات، يرجى زيارة https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// إنشاء HtmlSaveOptions مع الميزة المجربة
HtmlSaveOptions newOptions = new HtmlSaveOptions();

// تحديد المجلد المنفصل لحفظ الصور
newOptions.SpecialFolderForAllImages = dataDir;
```

### إنشاء ملفات لاحقة بمحتويات الجسم فقط

مؤخرًا، طُلب منا تقديم ميزة حيث يتم تحويل ملفات PDF إلى HTML ويمكن للمستخدم الحصول على محتويات وسم `<body>` لكل صفحة فقط. سينتج ذلك ملفًا واحدًا مع CSS، وتفاصيل `<html>`, `<head>` وجميع الصفحات في ملفات أخرى فقط مع محتويات `<body>`.

لتلبية هذا المتطلب، تم تقديم خاصية جديدة، HtmlMarkupGenerationMode، إلى فئة HtmlSaveOptions.

مع الشفرة البسيطة التالية، يمكنك تقسيم HTML الناتج إلى صفحات.
مع الشفرة البسيطة التالية، يمكنك تقسيم الـ HTML الناتج إلى صفحات.

```csharp
// مسار إلى دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

Document doc = new Document(dataDir + "PDFToHTML.pdf");
           
HtmlSaveOptions options = new HtmlSaveOptions();
// هذه هي الإعدادات المجربة
options.HtmlMarkupGenerationMode = HtmlSaveOptions.HtmlMarkupGenerationModes.WriteOnlyBodyContent;
options.SplitIntoPages = true;

doc.Save(dataDir + "CreateSubsequentFiles_out.html", options);
```

### تصيير النصوص الشفافة

في حالة إذا كان ملف PDF المصدر/الإدخال يحتوي على نصوص شفافة تحت ظلال الصور الأمامية، قد تواجه مشكلات في تصيير النصوص. لذلك من أجل التعامل مع مثل هذه السيناريوهات، يمكن استخدام خصائص SaveShadowedTextsAsTransparentTexts و SaveTransparentTexts.

```csharp
// لأمثلة كاملة وملفات البيانات، يرجى زيارة https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// مسار إلى دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

Document doc = new Document(dataDir + "PDFToHTML.pdf");
HtmlSaveOptions htmlOptions = new HtmlSaveOptions();
htmlOptions.SaveShadowedTextsAsTransparentTexts = true;
htmlOptions.SaveTransparentTexts = true;
doc.Save(dataDir + "TransparentTextRendering_out.html", htmlOptions);
```
### تصيير طبقات مستند PDF

يمكننا تصيير طبقات مستند PDF في عنصر نوع طبقة منفصل أثناء تحويل PDF إلى HTML:

```csharp
// للحصول على أمثلة كاملة وملفات بيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// المسار إلى دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

Document doc = new Document(dataDir + "PDFToHTML.pdf");
// إنشاء كائن خيارات حفظ HTML
HtmlSaveOptions htmlOptions = new HtmlSaveOptions();

// تحديد تصيير طبقات مستند PDF بشكل منفصل في HTML الناتج
htmlOptions.ConvertMarkedContentToLayers = true;

// حفظ المستند
doc.Save(dataDir + "LayersRendering_out.html", htmlOptions);
```

## انظر أيضا

هذه المقالة تغطي أيضا هذه المواضيع. الأكواد هي نفسها كما هو موضح أعلاه.

_التنسيق_: **HTML**
- [كود C# لتحويل PDF إلى HTML](#csharp-pdf-to-html)
- [واجهة برمجة تطبيقات C# لتحويل PDF إلى HTML](#csharp-pdf-to-html)
- [تحويل PDF إلى HTML برمجياً بلغة C#](#csharp-pdf-to-html)
- [مكتبة C# لتحويل PDF إلى HTML](#csharp-pdf-to-html)
- [حفظ PDF كـ HTML بلغة C#](#csharp-pdf-to-html)
- [C# حفظ PDF كـ HTML](#csharp-pdf-to-html)
- [C# إنشاء HTML من PDF](#csharp-pdf-to-html)
- [C# إنشاء HTML من PDF](#csharp-pdf-to-html)
- [C# تحويل PDF إلى HTML](#csharp-pdf-to-html)
