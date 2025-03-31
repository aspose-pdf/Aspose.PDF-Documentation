---
title: تحسين، ضغط أو تقليل حجم PDF في C#
linktitle: تحسين PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 40
url: /ar/net/optimize-pdf/
description: تحسين ملف PDF، تقليل حجم جميع الصور، تقليل حجم PDF، إزالة الخطوط المدمجة، إزالة الكائنات غير المستخدمة باستخدام C#.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Optimize, Compress or Reduce PDF Size in C#",
    "alternativeHeadline": "Optimize PDF Files Efficiently with C#",
    "abstract": "تتيح ميزة تحسين PDF الجديدة في C# للمطورين تقليل أحجام ملفات PDF بشكل كبير من خلال استخدام استراتيجيات متعددة، مثل ضغط الصور، وإزالة الخطوط المدمجة، وإزالة الكائنات غير المستخدمة. تعمل هذه التحسينات على تحسين الكفاءة للنشر على الويب، ومشاركة البريد الإلكتروني، والتخزين، مما يوفر حلاً فعالاً لإدارة مستندات PDF الكبيرة.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "optimize pdf, compress pdf size, reduce pdf size, optimize pdf c#, unembed fonts, remove unused objects, shrink images, optimization methods, pdf document generation, Aspose.PDF",
    "wordcount": "2282",
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
    "url": "/net/optimize-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/optimize-pdf/"
    },
    "dateModified": "2024-11-25",
    "description": "تحسين ملف PDF، تقليل حجم جميع الصور، تقليل حجم PDF، إزالة الخطوط المدمجة، إزالة الكائنات غير المستخدمة باستخدام C#."
}
</script>

قد يحتوي مستند PDF أحيانًا على بيانات إضافية. سيساعد تقليل حجم ملف PDF في تحسين نقل الشبكة والتخزين. هذا مفيد بشكل خاص للنشر على صفحات الويب، والمشاركة على الشبكات الاجتماعية، والإرسال عبر البريد الإلكتروني، أو الأرشفة في التخزين. يمكننا استخدام عدة تقنيات لتحسين PDF:

- تحسين محتوى الصفحة لتصفح الإنترنت.
- تقليل أو ضغط جميع الصور.
- تمكين إعادة استخدام محتوى الصفحة.
- دمج التدفقات المكررة.
- إزالة الخطوط المدمجة.
- إزالة الكائنات غير المستخدمة.
- إزالة أو تسطيح حقول النماذج.
- إزالة أو تسطيح التعليقات.

{{% alert color="primary" %}}

يمكن العثور على شرح مفصل لطرق التحسين في صفحة نظرة عامة على طرق التحسين.

{{% /alert %}}

## تحسين مستند PDF للويب

تشير عملية التحسين، أو الترتيب للويب، إلى جعل ملف PDF مناسبًا للتصفح عبر الإنترنت باستخدام متصفح الويب. لتحسين ملف للعرض على الويب:

1. افتح المستند المدخل في كائن [Document](https://reference.aspose.com/pdf/ar/net/aspose.pdf/document).
1. استخدم طريقة [Optimize](https://reference.aspose.com/pdf/ar/net/aspose.pdf/document/methods/optimize).
1. احفظ المستند المحسن باستخدام طريقة [Save](https://reference.aspose.com/pdf/ar/net/aspose.pdf/document/methods/save).

تعمل مقتطفات الكود التالية أيضًا مع مكتبة [Aspose.PDF.Drawing](/pdf/ar/net/drawing/).

تظهر مقتطفات الكود التالية كيفية تحسين مستند PDF للويب.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void OptimizeDocument()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "OptimizeDocument.pdf"))
    {
        // Optimize for web
        document.Optimize();

        // Save PDF document
        document.Save(dataDir + "OptimizeDocument_out.pdf");
    }
}
```

## تقليل حجم PDF

تسمح لك طريقة [OptimizeResources()](https://reference.aspose.com/pdf/ar/net/aspose.pdf/document/methods/optimizeresources) بتقليل حجم المستند عن طريق التخلص من المعلومات غير الضرورية. بشكل افتراضي، تعمل هذه الطريقة كما يلي:

- يتم إزالة الموارد التي لا تستخدم في صفحات المستند.
- يتم دمج الموارد المتساوية في كائن واحد.
- يتم حذف الكائنات غير المستخدمة.

المقتطف أدناه هو مثال. لاحظ، مع ذلك، أن هذه الطريقة لا يمكن أن تضمن تقليل حجم المستند.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ShrinkDocument()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ShrinkDocument.pdf"))
    {
        // Optimize PDF document. Note, though, that this method cannot guarantee document shrinking
        document.OptimizeResources();

        // Save PDF document
        document.Save(dataDir + "ShrinkDocument_out.pdf");
    }
}
```

## إدارة استراتيجية التحسين

يمكننا أيضًا تخصيص استراتيجية التحسين. حاليًا، تستخدم طريقة [OptimizeResources()](https://reference.aspose.com/pdf/ar/net/aspose.pdf.document/optimizeresources/methods/1) 5 تقنيات. يمكن تطبيق هذه التقنيات باستخدام طريقة OptimizeResources() مع معلمة [OptimizationOptions](https://reference.aspose.com/pdf/ar/net/aspose.pdf.optimization/optimizationoptions).

### تقليل أو ضغط جميع الصور

لدينا طريقتان للعمل مع الصور: تقليل جودة الصورة و/أو تغيير دقتها. في أي حال، يجب تطبيق [ImageCompressionOptions](https://reference.aspose.com/pdf/ar/net/aspose.pdf.optimization/imagecompressionoptions). في المثال التالي، نقوم بتقليل الصور عن طريق تقليل [ImageQuality](https://reference.aspose.com/pdf/ar/net/aspose.pdf.optimization/imagecompressionoptions/properties/imagequality) إلى 50.

`ImageQuality` يعمل بشكل مشابه لجودة JPEG، حيث القيمة 0 هي الأدنى والقيمة 100 هي الأعلى.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ShrinkImage()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "Shrinkimage.pdf"))
    {
        // Initialize OptimizationOptions
        var optimizeOptions = new Aspose.Pdf.Optimization.OptimizationOptions();

        // Set CompressImages option
        optimizeOptions.ImageCompressionOptions.CompressImages = true;

        // Set ImageQuality option
        optimizeOptions.ImageCompressionOptions.ImageQuality = 50;

        // Optimize PDF document using OptimizationOptions
        document.OptimizeResources(optimizeOptions);

        // Save PDF document
        document.Save(dataDir + "Shrinkimage_out.pdf");
    }
}
```

طريقة أخرى هي تغيير حجم الصور بدقة أقل. في هذه الحالة، يجب علينا تعيين ResizeImages إلى true و MaxResolution إلى القيمة المناسبة.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ResizeImages()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ResizeImage.pdf"))
    {
        // Initialize OptimizationOptions
        var optimizeOptions = new Aspose.Pdf.Optimization.OptimizationOptions();

        // Set CompressImages option
        optimizeOptions.ImageCompressionOptions.CompressImages = true;

        // Set ImageQuality option
        optimizeOptions.ImageCompressionOptions.ImageQuality = 75;

        // Set ResizeImage option
        optimizeOptions.ImageCompressionOptions.ResizeImages = true;

        // Set MaxResolution option
        optimizeOptions.ImageCompressionOptions.MaxResolution = 300;

        // Optimize PDF document using OptimizationOptions
        document.OptimizeResources(optimizeOptions);

        // Save PDF document
        document.Save(dataDir + "ResizeImages_out.pdf");
    }
}
```

مسألة أخرى مهمة هي وقت التنفيذ. ولكن مرة أخرى، يمكننا إدارة هذا الإعداد أيضًا. حاليًا، يمكننا استخدام خوارزميتين - القياسية والسريعة. للتحكم في وقت التنفيذ، يجب علينا تعيين خاصية [Version](https://reference.aspose.com/pdf/ar/net/aspose.pdf.optimization/imagecompressionoptions/properties/version). توضح المقتطفات التالية خوارزمية السريعة:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void FastShrinkImages()
{
    // Initialize Time
    var time = DateTime.Now.Ticks;

    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "Shrinkimage.pdf"))
    {
        // Initialize OptimizationOptions
        var optimizeOptions = new Aspose.Pdf.Optimization.OptimizationOptions();

        // Set CompressImages option
        optimizeOptions.ImageCompressionOptions.CompressImages = true;

        // Set ImageQuality option
        optimizeOptions.ImageCompressionOptions.ImageQuality = 75;

        // Set Image Compression Version to fast
        optimizeOptions.ImageCompressionOptions.Version = Aspose.Pdf.Optimization.ImageCompressionVersion.Fast;

        // Optimize PDF document using OptimizationOptions
        document.OptimizeResources(optimizeOptions);

        // Save PDF document
        document.Save(dataDir + "FastShrinkImages_out.pdf");
    }

    // Output the time taken for the operation
    Console.WriteLine("Ticks: {0}", DateTime.Now.Ticks - time);
}
```

### إزالة الكائنات غير المستخدمة

قد يحتوي مستند PDF أحيانًا على كائنات PDF التي لا يتم الإشارة إليها من أي كائن آخر في المستند. قد يحدث هذا، على سبيل المثال، عندما تتم إزالة صفحة من شجرة صفحات المستند ولكن كائن الصفحة نفسه لم يتم إزالته. إزالة هذه الكائنات لا تجعل المستند غير صالح بل تقلل حجمه.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void OptimizeDocument()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "OptimizeDocument.pdf"))
    {
        // Set RemoveUsedObject option
        var optimizeOptions = new Aspose.Pdf.Optimization.OptimizationOptions
        {
            RemoveUnusedObjects = true
        };
        
        // Optimize PDF document using OptimizationOptions
        document.OptimizeResources(optimizeOptions);

        // Save PDF document
        document.Save(dataDir + "OptimizeDocument_out.pdf");
    }
}
```

### إزالة التدفقات غير المستخدمة

أحيانًا يحتوي المستند على تدفقات موارد غير مستخدمة. هذه التدفقات ليست "كائنات غير مستخدمة" لأنها تشير من قاموس موارد الصفحة. وبالتالي، لا تتم إزالتها باستخدام طريقة "إزالة الكائنات غير المستخدمة". ولكن هذه التدفقات لا تستخدم أبدًا مع محتويات الصفحة. قد يحدث هذا في الحالات التي تمت فيها إزالة صورة من الصفحة ولكن ليس من موارد الصفحة. أيضًا، تحدث هذه الحالة غالبًا عندما يتم استخراج الصفحات من المستند وتكون صفحات المستند تحتوي على موارد "شائعة"، أي نفس كائن Resources. يتم تحليل محتويات الصفحة لتحديد ما إذا كانت تدفق مورد مستخدم أم لا. يتم إزالة التدفقات غير المستخدمة. أحيانًا يقلل ذلك من حجم المستند. استخدام هذه التقنية مشابه للخطوة السابقة:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void OptimizePdfDocument()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "OptimizeDocument.pdf"))
    {
        // Set RemoveUsedStreams option
        var optimizeOptions = new Aspose.Pdf.Optimization.OptimizationOptions
        {
            RemoveUnusedStreams = true
        };

        // Optimize PDF document using OptimizationOptions
        document.OptimizeResources(optimizeOptions);

        // Save PDF document
        document.Save(dataDir + "OptimizeDocument_out.pdf");
    }
}
```

### ربط التدفقات المكررة

يمكن أن تحتوي بعض المستندات على عدة تدفقات موارد متطابقة (مثل الصور، على سبيل المثال). قد يحدث هذا، على سبيل المثال، عندما يتم دمج مستند مع نفسه. يحتوي المستند الناتج على نسختين مستقلتين من نفس تدفق المورد. نقوم بتحليل جميع تدفقات الموارد ومقارنتها. إذا كانت التدفقات مكررة، يتم دمجها، أي تبقى نسخة واحدة فقط. يتم تغيير المراجع بشكل مناسب، ويتم إزالة نسخ الكائن. في بعض الحالات، يساعد ذلك في تقليل حجم المستند.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void OptimizePdfDocumentWithLinkDuplicateStreams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "OptimizeDocument.pdf"))
    {
        // Set LinkDuplicateStreams option
        var optimizeOptions = new Aspose.Pdf.Optimization.OptimizationOptions
        {
            LinkDuplicateStreams = true
        };

        // Optimize PDF document using OptimizationOptions
        document.OptimizeResources(optimizeOptions);

        // Save PDF document
        document.Save(dataDir + "OptimizeDocument_out.pdf");
    }
}
```

بالإضافة إلى ذلك، يمكننا استخدام إعدادات [AllowReusePageContent](https://reference.aspose.com/pdf/ar/net/aspose.pdf.optimization/optimizationoptions/properties/allowreusepagecontent). إذا تم تعيين هذه الخاصية إلى true، سيتم إعادة استخدام محتوى الصفحة عند تحسين المستند للصفحات المتطابقة.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void OptimizePdfDocumentWithReusePageContent()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "OptimizeDocument.pdf"))
    {
        // Set AllowReusePageContent option
        var optimizeOptions = new Aspose.Pdf.Optimization.OptimizationOptions
        {
            AllowReusePageContent = true
        };

        Console.WriteLine("Start");

        // Optimize PDF document using OptimizationOptions
        document.OptimizeResources(optimizeOptions);

        // Save PDF document
        document.Save(dataDir + "OptimizeDocument_out.pdf");
    }

    Console.WriteLine("Finished");

    // Calculate and display file sizes
    var fi1 = new FileInfo(dataDir + "OptimizeDocument.pdf");
    var fi2 = new FileInfo(dataDir + "OptimizeDocument_out.pdf");
    Console.WriteLine("Original file size: {0}. Reduced file size: {1}", fi1.Length, fi2.Length);
}
```

### إزالة الخطوط المدمجة

إذا كان المستند يستخدم خطوطًا مدمجة، فهذا يعني أن جميع بيانات الخطوط مخزنة في المستند. الميزة هي أن المستند يمكن مشاهدته بغض النظر عما إذا كان الخط مثبتًا على جهاز المستخدم أم لا. ولكن يجعل تضمين الخطوط المستند أكبر. تقوم طريقة إزالة الخطوط المدمجة بإزالة جميع الخطوط المدمجة. وبالتالي، ينخفض حجم المستند ولكن قد يصبح المستند نفسه غير قابل للقراءة إذا لم يتم تثبيت الخط الصحيح.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void OptimizePdfDocumentWithUnembedFonts()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "OptimizeDocument.pdf"))
    {
        // Set UnembedFonts option
        var optimizeOptions = new Aspose.Pdf.Optimization.OptimizationOptions
        {
            UnembedFonts = true
        };

        Console.WriteLine("Start");

        // Optimize PDF document using OptimizationOptions
        document.OptimizeResources(optimizeOptions);

        // Save PDF document
        document.Save(dataDir + "OptimizeDocument_out.pdf");	
    }
	
    Console.WriteLine("Finished");

    // Calculate and display file sizes
    var fi1 = new FileInfo(dataDir + "OptimizeDocument.pdf");
    var fi2 = new FileInfo(dataDir + "OptimizeDocument_out.pdf");
    Console.WriteLine("Original file size: {0}. Reduced file size: {1}", fi1.Length, fi2.Length);
}
```

تطبق موارد التحسين هذه الطرق على المستند. إذا تم تطبيق أي من هذه الطرق، فمن المحتمل أن ينخفض حجم المستند. إذا لم يتم تطبيق أي من هذه الطرق، فلن يتغير حجم المستند وهو أمر واضح.

## طرق إضافية لتقليل حجم مستند PDF

### إزالة أو تسطيح التعليقات

يمكن حذف التعليقات عندما تكون غير ضرورية. عندما تكون مطلوبة ولكن لا تتطلب تحريرًا إضافيًا، يمكن تسطيحها. ستقلل كل من هاتين التقنيتين من حجم الملف.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void FlattenAnnotationsInPdfDocument()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "OptimizeDocument.pdf"))
    {
        // Flatten annotations
        foreach (var page in document.Pages)
        {
            foreach (var annotation in page.Annotations)
            {
                annotation.Flatten();
            }
        }

        // Save PDF document
        document.Save(dataDir + "OptimizeDocument_out.pdf");
    }
}
```

### إزالة حقول النماذج

إذا كان مستند PDF يحتوي على AcroForms، يمكننا محاولة تقليل حجم الملف عن طريق تسطيح حقول النماذج.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void FlattenPdfForms()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Load source PDF form
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Flatten Forms
        if (document.Form.Fields.Lenght > 0)
        {
            foreach (var item in document.Form.Fields)
            {
                item.Flatten();
            }
        }

        // Save PDF document
        document.Save(dataDir + "FlattenForms_out.pdf");
    }
}
```

### تحويل PDF من مساحة ألوان RGB إلى تدرج الرمادي

يتكون ملف PDF من نصوص وصور ومرفقات وتعليقات ورسوم بيانية وكائنات أخرى. قد تواجه متطلبات لتحويل PDF من مساحة ألوان RGB إلى تدرج الرمادي بحيث يكون أسرع عند طباعة تلك الملفات PDF. أيضًا، عندما يتم تحويل الملف إلى تدرج الرمادي، يتم تقليل حجم المستند أيضًا، ولكن يمكن أن يتسبب ذلك أيضًا في انخفاض جودة المستند. هذه الميزة مدعومة حاليًا من قبل ميزة Pre-Flight في Adobe Acrobat، ولكن عند الحديث عن أتمتة المكتب، تعتبر Aspose.PDF الحل النهائي لتوفير مثل هذه الميزات لتلاعب المستندات. لتحقيق هذا المتطلب، يمكن استخدام مقتطف الكود التالي.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertRgbToGrayScale()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Create RGB to DeviceGray conversion strategy
        var strategy = new Aspose.Pdf.RgbToDeviceGrayConversionStrategy();

        // Iterate through each page
        for (int idxPage = 1; idxPage <= document.Pages.Count; idxPage++)
        {
            // Get instance of particular page inside PDF
            var page = document.Pages[idxPage];

            // Convert the RGB colorspace image to GrayScale colorspace
            strategy.Convert(page);
        }

        // Save PDF document
        document.Save(dataDir + "TestGray_out.pdf");
    }
}
```

### ضغط FlateDecode

{{% alert color="primary" %}}

تدعم هذه الميزة الإصدار 18.12 أو أعلى.

{{% /alert %}}

Aspose.PDF for .NET يوفر دعم ضغط FlateDecode لوظيفة تحسين PDF. توضح مقتطفات الكود التالية كيفية استخدام الخيار في التحسين لتخزين الصور مع ضغط **FlateDecode**:

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void OptimizeDocumentImagesWithFlateCompression()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "AddImage.pdf"))
    {
        // Initialize OptimizationOptions
        var optimizationOptions = new Aspose.Pdf.Optimization.OptimizationOptions();

        // To optimize images using FlateDecode compression, set optimization options to Flate
        optimizationOptions.ImageCompressionOptions.Encoding = Aspose.Pdf.Optimization.ImageEncoding.Flate;

        // Set optimization options
        document.OptimizeResources(optimizationOptions);

        // Save PDF document
        document.Save(dataDir + "OptimizeDocumentImagesWithFlateCompression_out.pdf");
    }
}
```

### تخزين الصورة في XImageCollection

Aspose.PDF for .NET يوفر القدرة على تخزين صور جديدة في **XImageCollection** مع ضغط FlateDecode. لتمكين هذا الخيار يمكنك استخدام علامة **ImageFilterType.Flate**. توضح مقتطفات الكود التالية كيفية استخدام هذه الوظيفة:

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddImageToPdfWithFlateCompression()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();

        // Open the image file stream
        using (var imageStream = new FileStream(dataDir + "aspose-logo.jpg", FileMode.Open))
        {
            // Add the image to the page resources with Flate compression
            page.Resources.Images.Add(imageStream, Aspose.Pdf.ImageFilterType.Flate);
        }

        // Get the added image
        var ximage = page.Resources.Images[page.Resources.Images.Count];

        // Save the current graphics state
        page.Contents.Add(new Aspose.Pdf.Operators.GSave());

        // Set coordinates for the image placement
        int lowerLeftX = 0;
        int lowerLeftY = 0;
        int upperRightX = 600;
        int upperRightY = 600;

        var rectangle = new Aspose.Pdf.Rectangle(lowerLeftX, lowerLeftY, upperRightX, upperRightY);
        var matrix = new Aspose.Pdf.Matrix(new double[]
        {
            rectangle.URX - rectangle.LLX, 0, 0, rectangle.URY - rectangle.LLY, rectangle.LLX, rectangle.LLY
        });

        // Use ConcatenateMatrix operator to define how the image must be placed
        page.Contents.Add(new Aspose.Pdf.Operators.ConcatenateMatrix(matrix));
        page.Contents.Add(new Aspose.Pdf.Operators.Do(ximage.Name));

        // Restore the graphics state
        page.Contents.Add(new Aspose.Pdf.Operators.GRestore());

        // Save the document
        document.Save(dataDir + "AddImageToPdfWithFlateCompression_out.pdf");
    }
}
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for .NET Library",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
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
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "PDF Manipulation Library for .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/net/create-pdf-document/screenshot.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>