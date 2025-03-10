---
title: تحويل PDF إلى PowerPoint في .NET
linktitle: تحويل PDF إلى PowerPoint
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 30
url: /ar/net/convert-pdf-to-powerpoint/
lastmod: "2021-11-01"
description: يسمح Aspose.PDF لك بتحويل PDF إلى تنسيق PPT (PowerPoint) باستخدام .NET. إحدى الطرق هي إمكانية تحويل PDF إلى PPTX مع الشرائح كصور.
lastmod: "2021-10-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Convert PDF to PowerPoint in .NET",
    "alternativeHeadline": "Convert PDF Documents to PowerPoint Presentations Efficiently in C#",
    "abstract": "Aspose.PDF for .NET يقدم ميزة قوية تتيح التحويل السلس لمستندات PDF إلى تنسيق PowerPoint (PPTX)، مما يسمح لكل صفحة PDF بالتحول إلى شريحة مميزة. مع خيار عرض النص كقابل للاختيار أو كصور، يمكن للمستخدمين تخصيص عروضهم التقديمية بسهولة مع تتبع تقدم التحويل بكفاءة. قم بتحسين سير عمل مستنداتك من خلال الاستفادة من هذه الوظيفة المبتكرة لزيادة الإنتاجية",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1174",
    "proficiencyLevel": "Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF for .NET",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "sales",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "sales",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "sales",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/net/convert-pdf-to-powerpoint/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/convert-pdf-to-powerpoint/"
    },
    "dateModified": "2024-11-25",
    "description": "يمكن لـ Aspose.PDF أداء المهام البسيطة والسريعة وكذلك التعامل مع الأهداف الأكثر تعقيدًا. تحقق من القسم التالي للمستخدمين المتقدمين والمطورين."
}
</script>

## نظرة عامة

تشرح هذه المقالة كيفية **تحويل PDF إلى PowerPoint باستخدام C#**. تغطي هذه المواضيع.

_التنسيق_: **PPTX**
- [C# PDF إلى PPTX](#csharp-pdf-to-pptx)
- [C# تحويل PDF إلى PPTX](#csharp-pdf-to-pptx)
- [C# كيفية تحويل ملف PDF إلى PPTX](#csharp-pdf-to-pptx)

_التنسيق_: **PowerPoint**
- [C# PDF إلى PowerPoint](#csharp-pdf-to-powerpoint)
- [C# تحويل PDF إلى PowerPoint](#csharp-pdf-to-powerpoint)
- [C# كيفية تحويل ملف PDF إلى PowerPoint](#csharp-pdf-to-powerpoint)

تعمل مقتطفات الكود التالية أيضًا مع مكتبة [Aspose.PDF.Drawing](/pdf/net/drawing/) .

## تحويل C# PDF إلى PowerPoint و PPTX

**Aspose.PDF for .NET** يتيح لك تتبع تقدم تحويل PDF إلى PPTX.

لدينا واجهة برمجة تطبيقات تسمى Aspose.Slides التي تقدم ميزة إنشاء وتعديل عروض PPT/PPTX. توفر هذه الواجهة أيضًا ميزة تحويل ملفات PPT/PPTX إلى تنسيق PDF. مؤخرًا، تلقينا متطلبات من العديد من عملائنا لدعم القدرة على تحويل PDF إلى تنسيق PPTX. بدءًا من إصدار Aspose.PDF for .NET 10.3.0، قدمنا ميزة لتحويل مستندات PDF إلى تنسيق PPTX. خلال هذا التحويل، يتم تحويل الصفحات الفردية من ملف PDF إلى شرائح منفصلة في ملف PPTX.

أثناء تحويل PDF إلى <abbr title="Microsoft PowerPoint 2007 XML Presentation">PPTX</abbr>، يتم عرض النص كنص حيث يمكنك تحديده/تحديثه. يرجى ملاحظة أنه من أجل تحويل ملفات PDF إلى تنسيق PPTX، يوفر Aspose.PDF فئة تسمى [`PptxSaveOptions`](https://reference.aspose.com/pdf/net/aspose.pdf/pptxsaveoptions). يتم تمرير كائن من فئة PptxSaveOptions كوسيط ثانٍ إلى [`Document.Save(..) method`](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save). توضح مقتطفات الكود التالية العملية لتحويل ملفات PDF إلى تنسيق PPTX.

## تحويل بسيط PDF إلى PowerPoint باستخدام C# و Aspose.PDF .NET

من أجل تحويل PDF إلى PPTX، ينصح Aspose.PDF for .NET باستخدام خطوات الكود التالية.

<a name="csharp-pdf-to-powerpoint"><strong>الخطوات: تحويل PDF إلى PowerPoint في C#</strong></a> | <a name="csharp-pdf-to-pptx"><strong>الخطوات: تحويل PDF إلى PPTX في C#</strong></a>

1. إنشاء مثيل من فئة [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) .
2. إنشاء مثيل من فئة [PptxSaveOptions](https://reference.aspose.com/pdf/net/aspose.pdf/pptxsaveoptions) .
3. استخدم طريقة **Save** لكائن **Document** لحفظ PDF كـ PPTX.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFToPPTX()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Instantiate PptxSaveOptions object
        var saveOptions = new Aspose.Pdf.PptxSaveOptions();

        // Save the file in PPTX format
        document.Save(dataDir + "PDFToPPT_out.pptx", saveOptions);
    }
}
```

## تحويل PDF إلى PPTX مع الشرائح كصور

{{% alert color="success" %}}
**حاول تحويل PDF إلى PowerPoint عبر الإنترنت**

يقدم لك Aspose.PDF for .NET تطبيقًا مجانيًا عبر الإنترنت ["PDF إلى PPTX"](https://products.aspose.app/pdf/conversion/pdf-to-pptx)، حيث يمكنك محاولة استكشاف الوظائف والجودة التي يعمل بها.

[![تحويل Aspose.PDF PDF إلى PPTX مع تطبيق مجاني](pdf_to_pptx.png)](https://products.aspose.app/pdf/conversion/pdf-to-pptx)
{{% /alert %}}

في حالة احتياجك لتحويل PDF قابل للبحث إلى PPTX كصور بدلاً من نص قابل للاختيار، يوفر Aspose.PDF مثل هذه الميزة عبر فئة [Aspose.Pdf.PptxSaveOptions](https://reference.aspose.com/pdf/net/aspose.pdf/pptxsaveoptions) . لتحقيق ذلك، قم بتعيين خاصية [SlidesAsImages](https://reference.aspose.com/pdf/net/aspose.pdf/pptxsaveoptions/properties/slidesasimages) من فئة [PptxSaveOptios](https://reference.aspose.com/pdf/net/aspose.pdf/pptxsaveoptions) إلى 'true' كما هو موضح في عينة الكود التالية.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFToPPTWithSlidesAsImages()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Instantiate PptxSaveOptions object
        var saveOptions = new Aspose.Pdf.PptxSaveOptions
        {
            SlidesAsImages = true
        };

        // Save the file in PPTX format with slides as images
        document.Save(dataDir + "PDFToPPT_out.pptx", saveOptions);
    }
}
```

## تفاصيل تقدم تحويل PPTX

يتيح لك Aspose.PDF for .NET تتبع تقدم تحويل PDF إلى PPTX. توفر فئة [Aspose.Pdf.PptxSaveOptions](https://reference.aspose.com/pdf/net/aspose.pdf/pptxsaveoptions) خاصية [CustomProgressHandler](https://reference.aspose.com/pdf/net/aspose.pdf/pptxsaveoptions/properties/customprogresshandler) التي يمكن تحديدها لطريقة مخصصة لتتبع تقدم التحويل كما هو موضح في عينة الكود التالية.

```csharp
 // For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFToPPTWithCustomProgressHandler()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {

        // Instantiate PptxSaveOptions object
        var saveOptions = new Aspose.Pdf.PptxSaveOptions();

        // Specify custom progress handler
        saveOptions.CustomProgressHandler = ShowProgressOnConsole;

        // Save the file in PPTX format with progress tracking
        document.Save(dataDir + "PDFToPPTWithProgressTracking_out.pptx", saveOptions);
    }
}

 // Define the method to handle progress events and display them on the console
private static void ShowProgressOnConsole(Aspose.Pdf.UnifiedSaveOptions.ProgressEventHandlerInfo eventInfo)
{
    switch (eventInfo.EventType)
    {
        case Aspose.Pdf.ProgressEventType.TotalProgress:
            // Display overall progress of the conversion
            Console.WriteLine($"{DateTime.Now.TimeOfDay}  - Conversion progress: {eventInfo.Value}%.");
            break;

        case Aspose.Pdf.ProgressEventType.ResultPageCreated:
            // Display progress of the page layout creation
            Console.WriteLine($"{DateTime.Now.TimeOfDay}  - Result page {eventInfo.Value} of {eventInfo.MaxValue} layout created.");
            break;

        case Aspose.Pdf.ProgressEventType.ResultPageSaved:
            // Display progress of the page being exported
            Console.WriteLine($"{DateTime.Now.TimeOfDay}  - Result page {eventInfo.Value} of {eventInfo.MaxValue} exported.");
            break;

        case Aspose.Pdf.ProgressEventType.SourcePageAnalysed:
            // Display progress of the source page analysis
            Console.WriteLine($"{DateTime.Now.TimeOfDay}  - Source page {eventInfo.Value} of {eventInfo.MaxValue} analyzed.");
            break;

        default:
            break;
    }
}
```

## انظر أيضًا 

تغطي هذه المقالة أيضًا هذه المواضيع. الأكواد هي نفسها كما هو مذكور أعلاه.

_التنسيق_: **PowerPoint**
- [C# كود PDF إلى PowerPoint](#csharp-pdf-to-powerpoint)
- [C# واجهة برمجة تطبيقات PDF إلى PowerPoint](#csharp-pdf-to-powerpoint)
- [C# PDF إلى PowerPoint برمجيًا](#csharp-pdf-to-powerpoint)
- [C# مكتبة PDF إلى PowerPoint](#csharp-pdf-to-powerpoint)
- [C# حفظ PDF كـ PowerPoint](#csharp-pdf-to-powerpoint)
- [C# توليد PowerPoint من PDF](#csharp-pdf-to-powerpoint)
- [C# إنشاء PowerPoint من PDF](#csharp-pdf-to-powerpoint)
- [C# محول PDF إلى PowerPoint](#csharp-pdf-to-powerpoint)

_التنسيق_: **PPTX**
- [C# كود PDF إلى PPTX](#csharp-pdf-to-pptx)
- [C# واجهة برمجة تطبيقات PDF إلى PPTX](#csharp-pdf-to-pptx)
- [C# PDF إلى PPTX برمجيًا](#csharp-pdf-to-pptx)
- [C# مكتبة PDF إلى PPTX](#csharp-pdf-to-pptx)
- [C# حفظ PDF كـ PPTX](#csharp-pdf-to-pptx)
- [C# توليد PPTX من PDF](#csharp-pdf-to-pptx)
- [C# إنشاء PPTX من PDF](#csharp-pdf-to-pptx)
- [C# محول PDF إلى PPTX](#csharp-pdf-to-pptx)