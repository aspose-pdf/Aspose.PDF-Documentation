---
title: تحويل PDF إلى PowerPoint في .NET
linktitle: تحويل PDF إلى PowerPoint
type: docs
weight: 30
url: ar/net/convert-pdf-to-powerpoint/
lastmod: "2021-11-01"
description: يتيح لك Aspose.PDF تحويل PDF إلى تنسيق PPT (PowerPoint) باستخدام .NET. هناك طريقة لتحويل PDF إلى PPTX مع الشرائح كصور.
lastmod: "2021-10-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
## نظرة عامة

يشرح هذا المقال كيفية **تحويل PDF إلى PowerPoint باستخدام C#**. يغطي الموضوعات التالية.

_التنسيق_: **PPTX**
- [C# PDF إلى PPTX](#csharp-pdf-to-pptx)
- [C# تحويل PDF إلى PPTX](#csharp-pdf-to-pptx)
- [C# كيفية تحويل ملف PDF إلى PPTX](#csharp-pdf-to-pptx)

_التنسيق_: **PowerPoint**
- [C# PDF إلى PowerPoint](#csharp-pdf-to-powerpoint)
- [C# تحويل PDF إلى PowerPoint](#csharp-pdf-to-powerpoint)
- [C# كيفية تحويل ملف PDF إلى PowerPoint](#csharp-pdf-to-powerpoint)

يعمل الكود التالي أيضًا مع مكتبة [Aspose.PDF.Drawing](/pdf/net/drawing/).

## تحويل PDF إلى PowerPoint و PPTX في C#
## تحويل PDF إلى PowerPoint وPPTX في C#

**Aspose.PDF لـ .NET** يتيح لك تتبع تقدم تحويل PDF إلى PPTX.

لدينا واجهة برمجة تطبيقات تُسمى Aspose.Slides والتي تقدم الميزة لإنشاء وكذلك التعديل على عروض PPT/PPTX. توفر هذه الواجهة أيضًا الميزة لتحويل ملفات PPT/PPTX إلى صيغة PDF. مؤخرًا، تلقينا متطلبات من العديد من عملائنا لدعم قدرة تحويل PDF إلى صيغة PPTX. بدءًا من إصدار Aspose.PDF لـ .NET 10.3.0، قدمنا ميزة لتحويل مستندات PDF إلى صيغة PPTX. خلال هذا التحويل، يتم تحويل الصفحات الفردية لملف PDF إلى شرائح منفصلة في ملف PPTX.

خلال تحويل PDF إلى <abbr title="عرض تقديمي بصيغة XML لـ Microsoft PowerPoint 2007">PPTX</abbr>، يتم عرض النص كنص حيث يمكنك تحديده أو تحديثه.
خلال تحويل PDF إلى <abbr title="Microsoft PowerPoint 2007 XML Presentation">PPTX</abbr>، يتم تقديم النص على أنه نص حيث يمكنك تحديده/تحديثه.

## تحويل بسيط من PDF إلى PowerPoint باستخدام C# و Aspose.PDF .NET

لتحويل PDF إلى PPTX، ينصح Aspose.PDF لـ .NET باستخدام الخطوات البرمجية التالية.

<a name="csharp-pdf-to-powerpoint"><strong>خطوات: تحويل PDF إلى PowerPoint في C#</strong></a> | <a name="csharp-pdf-to-pptx"><strong>خطوات: تحويل PDF إلى PPTX في C#</strong></a>

1. إنشاء نموذج من فئة [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document)
2. إنشاء نموذج من فئة [PptxSaveOptions](https://reference.aspose.com/pdf/net/aspose.pdf/pptxsaveoptions)
3. استخدم طريقة **Save** لكائن **Document** لحفظ PDF كـ PPTX

```csharp
// للحصول على أمثلة كاملة وملفات بيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// المسار إلى دليل الوثائق.
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();
// تحميل مستند PDF
Aspose.Pdf.Document doc = new Aspose.Pdf.Document(dataDir + "input.pdf");
// إنشاء نموذج من نوع PptxSaveOptions
Aspose.Pdf.PptxSaveOptions pptx_save = new Aspose.Pdf.PptxSaveOptions();
// حفظ الناتج بتنسيق PPTX
doc.Save(dataDir + "PDFToPPT_out.pptx", pptx_save);
```
## تحويل PDF إلى PPTX مع الشرائح كصور

{{% alert color="success" %}}
**جرب تحويل PDF إلى PowerPoint عبر الإنترنت**

يقدم لك Aspose.PDF لـ .NET تطبيق مجاني عبر الإنترنت ["PDF إلى PPTX"](https://products.aspose.app/pdf/conversion/pdf-to-pptx)، حيث يمكنك تجربة استكشاف الوظائف والجودة التي يعمل بها.

[![تحويل Aspose.PDF PDF إلى PPTX بتطبيق مجاني](pdf_to_pptx.png)](https://products.aspose.app/pdf/conversion/pdf-to-pptx)
{{% /alert %}}

في حالة إذا كنت بحاجة إلى تحويل PDF القابل للبحث إلى PPTX كصور بدلاً من نص قابل للتحديد، يوفر Aspose.PDF هذه الميزة عبر فئة [Aspose.Pdf.PptxSaveOptions](https://reference.aspose.com/pdf/net/aspose.pdf/pptxsaveoptions). لتحقيق ذلك، قم بتعيين خاصية [SlidesAsImages](https://reference.aspose.com/pdf/net/aspose.pdf/pptxsaveoptions/properties/slidesasimages) لفئة [PptxSaveOptions](https://reference.aspose.com/pdf/net/aspose.pdf/pptxsaveoptions) إلى 'true' كما هو موضح في مثال الكود التالي.

```csharp
// لأمثلة كاملة وملفات بيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// المسار إلى دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();
// تحميل مستند PDF
Aspose.Pdf.Document doc = new Aspose.Pdf.Document(dataDir + "input.pdf");
// توفير نموذج لخيارات حفظ Pptx
Aspose.Pdf.PptxSaveOptions pptx_save = new Aspose.Pdf.PptxSaveOptions();
// حفظ الناتج بتنسيق PPTX
pptx_save.SlidesAsImages = true;
doc.Save(dataDir + "PDFToPPT_out_.pptx", pptx_save);
```
## تفاصيل تقدم تحويل PPTX

يتيح لك Aspose.PDF لـ .NET تتبع تقدم تحويل PDF إلى PPTX. توفر الفئة [Aspose.Pdf.PptxSaveOptions](https://reference.aspose.com/pdf/net/aspose.pdf/pptxsaveoptions) خاصية [CustomProgressHandler](https://reference.aspose.com/pdf/net/aspose.pdf/pptxsaveoptions/properties/customprogresshandler) التي يمكن تحديدها لطريقة مخصصة لتتبع تقدم التحويل كما هو موضح في نموذج الكود التالي.

```csharp
// للحصول على أمثلة كاملة وملفات بيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// مسار إلى دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();
// تحميل مستند PDF
Aspose.Pdf.Document doc = new Aspose.Pdf.Document(dataDir + "input.pdf");
// إنشاء مثيل PptxSaveOptions
Aspose.Pdf.PptxSaveOptions pptx_save = new Aspose.Pdf.PptxSaveOptions();

//تحديد معالج تقدم مخصص
pptx_save.CustomProgressHandler = ShowProgressOnConsole;
// حفظ الناتج بتنسيق PPTX
doc.Save(dataDir + "PDFToPPTWithProgressTracking_out_.pptx", pptx_save);
```
تالياً هو الأسلوب المخصص لعرض تقدم التحويل.

```csharp
// للحصول على أمثلة كاملة وملفات البيانات، يرجى زيارة https://github.com/aspose-pdf/Aspose.PDF-for-.NET
switch (eventInfo.EventType)
{
    case ProgressEventType.TotalProgress:
        Console.WriteLine(String.Format("{0}  - تقدم التحويل : {1}% .", DateTime.Now.TimeOfDay, eventInfo.Value.ToString()));
        break;
    case ProgressEventType.ResultPageCreated:
        Console.WriteLine(String.Format("{0}  - تم إنشاء تخطيط الصفحة النتيجة {1} من {2}.", DateTime.Now.TimeOfDay, eventInfo.Value.ToString(), eventInfo.MaxValue.ToString()));
        break;
    case ProgressEventType.ResultPageSaved:
        Console.WriteLine(String.Format("{0}  - تم تصدير الصفحة النتيجة {1} من {2}.", DateTime.Now.TimeOfDay, eventInfo.Value.ToString(), eventInfo.MaxValue.ToString()));
        break;
    case ProgressEventType.SourcePageAnalysed:
        Console.WriteLine(String.Format("{0}  - تم تحليل الصفحة المصدر {1} من {2}.", DateTime.Now.TimeOfDay, eventInfo.Value.ToString(), eventInfo.MaxValue.ToString()));

        break;
    default:
        break;
}
```
## انظر أيضًا

هذه المقالة تغطي أيضًا هذه المواضيع. الأكواد هي نفسها كما هو مذكور أعلاه.

_التنسيق_: **PowerPoint**
- [كود C# لتحويل PDF إلى PowerPoint](#csharp-pdf-to-powerpoint)
- [API لتحويل PDF إلى PowerPoint بلغة C#](#csharp-pdf-to-powerpoint)
- [تحويل PDF إلى PowerPoint برمجيًا باستخدام C#](#csharp-pdf-to-powerpoint)
- [مكتبة C# لتحويل PDF إلى PowerPoint](#csharp-pdf-to-powerpoint)
- [حفظ PDF كـ PowerPoint باستخدام C#](#csharp-pdf-to-powerpoint)
- [إنشاء PowerPoint من PDF باستخدام C#](#csharp-pdf-to-powerpoint)
- [إنشاء PowerPoint من PDF باستخدام C#](#csharp-pdf-to-powerpoint)
- [محول PDF إلى PowerPoint بلغة C#](#csharp-pdf-to-powerpoint)

_التنسيق_: **PPTX**
- [كود C# لتحويل PDF إلى PPTX](#csharp-pdf-to-pptx)
- [API لتحويل PDF إلى PPTX بلغة C#](#csharp-pdf-to-pptx)
- [تحويل PDF إلى PPTX برمجيًا باستخدام C#](#csharp-pdf-to-pptx)
- [مكتبة C# لتحويل PDF إلى PPTX](#csharp-pdf-to-pptx)
- [حفظ PDF كـ PPTX باستخدام C#](#csharp-pdf-to-pptx)
- [إنشاء PPTX من PDF باستخدام C#](#csharp-pdf-to-pptx)
- [إنشاء PPTX من PDF باستخدام C#](#csharp-pdf-to-pptx)
- [محول PDF إلى PPTX بلغة C#](#csharp-pdf-to-pptx)
