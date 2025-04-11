---
title: كيفية إنشاء PDF باستخدام C#
linktitle: إنشاء مستند PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /ar/net/create-pdf-document/
description: إنشاء وتنسيق مستند PDF مع Aspose.PDF for .NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "How to Create PDF using C#",
    "alternativeHeadline": "Create and Format PDFs Effortlessly with C#",
    "abstract": "تتيح الوظيفة الجديدة في Aspose.PDF for .NET للمطورين إنشاء وتنسيق مستندات PDF بسهولة باستخدام C#. مع هذه الواجهة البرمجية البديهية، يمكن للمستخدمين إنشاء PDFs قابلة للبحث، والتلاعب بالمحتوى المعنون للوصول، ودمج إنشاء PDF بسلاسة في تطبيقات .NET المختلفة، مما يعزز الإنتاجية ويسهل سير العمل.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "PDF creation, C# PDF generation, Aspose.PDF for .NET, searchable PDF, accessible PDF, Document class, TextFragment, PDF document manipulation, .NET applications, BDC operations",
    "wordcount": "871",
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
    "url": "/net/create-pdf-document/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/create-pdf-document/"
    },
    "dateModified": "2024-11-25",
    "description": "إنشاء وتنسيق مستند PDF مع Aspose.PDF for .NET."
}
</script>

نحن دائمًا نبحث عن طريقة لإنشاء مستندات PDF والعمل معها في مشاريع C# بدقة وفعالية أكبر. توفر الوظائف السهلة الاستخدام من مكتبة ما إمكانية تتبع المزيد من العمل، وتقليل الوقت المستغرق في التفاصيل الثقيلة لمحاولة إنشاء PDFs، سواء في .NET.

تعمل مقتطفات الكود التالية أيضًا مع مكتبة [Aspose.PDF.Drawing](/pdf/ar/net/drawing/).

## إنشاء (أو توليد) مستند PDF باستخدام لغة C#

تتيح لك واجهة برمجة التطبيقات Aspose.PDF for .NET إنشاء وقراءة ملفات PDF باستخدام C# و VB.NET. يمكن استخدام واجهة برمجة التطبيقات في مجموعة متنوعة من تطبيقات .NET بما في ذلك WinForms و ASP.NET والعديد من التطبيقات الأخرى. في هذه المقالة، سنوضح كيفية استخدام واجهة برمجة التطبيقات Aspose.PDF for .NET لتوليد وقراءة ملفات PDF بسهولة في تطبيقات .NET.

### كيفية إنشاء ملف PDF بسيط

لإنشاء ملف PDF باستخدام C#، يمكن استخدام الخطوات التالية.

1. إنشاء كائن من فئة [Document](https://reference.aspose.com/pdf/ar/net/aspose.pdf/document).
1. إضافة كائن [Page](https://reference.aspose.com/pdf/ar/net/aspose.pdf/page) إلى مجموعة [Pages](https://reference.aspose.com/pdf/ar/net/aspose.pdf/document/properties/pages) لكائن Document.
1. إضافة [TextFragment](https://reference.aspose.com/pdf/ar/net/aspose.pdf.text/textfragment) إلى مجموعة [Paragraphs](https://reference.aspose.com/pdf/ar/net/aspose.pdf/page/properties/paragraphs) للصفحة.
1. حفظ مستند PDF الناتج.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CreateHelloWorldDocument()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_QuickStart();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();
        // Add text to new page
        page.Paragraphs.Add(new Aspose.Pdf.Text.TextFragment("Hello World!"));
        // Save PDF document
        document.Save(dataDir + "HelloWorld_out.pdf");
    }
}
```

### كيفية إنشاء مستند PDF قابل للبحث

يوفر Aspose.PDF for .NET ميزة إنشاء وتعديل مستندات PDF الموجودة. عند إضافة عناصر نصية داخل ملف PDF، يصبح PDF الناتج قابلاً للبحث. ومع ذلك، إذا كنا نقوم بتحويل صورة تحتوي على نص إلى ملف PDF، فإن المحتويات داخل PDF لن تكون قابلة للبحث. ومع ذلك، كحل بديل، يمكننا استخدام OCR على الملف الناتج، بحيث يصبح قابلاً للبحث.

تحدد هذه المنطق أدناه التعرف على النص لصور PDF. يمكنك استخدام دعم OCR الخارجي لمعيار HOCR. لأغراض الاختبار، استخدمنا OCR مجاني من Google tesseract. لذلك، تحتاج أولاً إلى تثبيت Tesseract-OCR على نظامك، وستكون لديك تطبيق وحدة التحكم tesseract.

فيما يلي الكود الكامل لتحقيق هذا المتطلب:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CreateSearchableDocument()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_QuickStart();
    
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SearchableDocument.pdf"))
    {
        document.Convert(CallBackGetHocr);

        // Save PDF document
        document.Save(dataDir + "SearchableDocument_out.pdf");
    }
}

private static string CallBackGetHocr(System.Drawing.Image img)
{
    var tmpFile = Path.GetTempFileName();
    try
    {
        using (var bmp = new System.Drawing.Bitmap(img))
        {
            bmp.Save(tmpFile, System.Drawing.Imaging.ImageFormat.Bmp);
        }

        var inputFile = string.Concat('"', tmpFile, '"');
        var outputFile = string.Concat('"', tmpFile, '"');
        var arguments = string.Concat(inputFile, " ", outputFile, " -l eng hocr");
        var tesseractProcessName = RunExamples.GetTesseractExePath();

        var psi = new System.Diagnostics.ProcessStartInfo(tesseractProcessName, arguments)
        {
            UseShellExecute = true,
            CreateNoWindow = true,
            WindowStyle = System.Diagnostics.ProcessWindowStyle.Hidden,
            WorkingDirectory = Path.GetDirectoryName(tesseractProcessName)
        };

        var p = new System.Diagnostics.Process
        {
            StartInfo = psi
        };
        p.Start();
        p.WaitForExit();

        using (var streamReader = new StreamReader(tmpFile + ".hocr"))
        {
            string text = streamReader.ReadToEnd();
            return text;
        }
    }
    finally
    {
        if (File.Exists(tmpFile))
        {
            File.Delete(tmpFile);
        }
        if (File.Exists(tmpFile + ".hocr"))
        {
            File.Delete(tmpFile + ".hocr");
        }
    }
}
```

### كيفية إنشاء PDF قابل للوصول باستخدام وظائف منخفضة المستوى

يعمل مقتطف الكود هذا مع مستند PDF ومحتواه المعنون، باستخدام مكتبة Aspose.PDF لمعالجته.

يخلق المثال عنصر span جديد في المحتوى المعنون للصفحة الأولى من PDF، ويجد جميع عناصر BDC، ويربطها بالـ span. ثم يتم حفظ المستند المعدل.

يمكنك إنشاء بيان bdc يحدد mcid و lang ونص التوسيع باستخدام كائن BDCProperties:

```cs
var bdc = new Aspose.Pdf.Operators.BDC("P", new Aspose.Pdf.Facades.BDCProperties(1, "de", "Hallo, welt!"));
```

بعد إنشاء شجرة الهيكل، من الممكن ربط عامل BDC بالعنصر المحدد من الهيكل باستخدام طريقة Tag على كائن العنصر:

```cs
Aspose.Pdf.LogicalStructure.SpanElement span = content.CreateSpanElement();
span.Tag(bdc);
```

خطوات إنشاء PDF قابل للوصول:

1. تحميل مستند PDF.
1. الوصول إلى المحتوى المعنون.
1. إنشاء عنصر Span.
1. إضافة Span إلى العنصر الجذري.
1. التكرار على محتويات الصفحة.
1. التحقق من عناصر BDC ووضع علامة عليها.
1. حفظ المستند المعدل.

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CreateAnAccessibleDocument()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_QuickStart();
    
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "tourguidev2_gb_tags.pdf"))
    {
        // Access tagged content
        Aspose.Pdf.Tagged.ITaggedContent content = document.TaggedContent;
        // Create a span element
        Aspose.Pdf.LogicalStructure.SpanElement span = content.CreateSpanElement();
        // Append span to root element
        content.RootElement.AppendChild(span);
        // Iterate over page contents
        foreach (var op in document.Pages[1].Contents)
        {
            var bdc = op as Aspose.Pdf.Operators.BDC;
            if (bdc != null)
            {
                span.Tag(bdc);
            }
        }
        // Save PDF document
        document.Save(dataDir + "AccessibleDocument_out.pdf");
    }
}
```

يعدل هذا الكود PDF عن طريق إنشاء عنصر span داخل المحتوى المعنون للمستند ووضع علامة على محتوى معين (عمليات BDC) من الصفحة الأولى بهذا span. ثم يتم حفظ PDF المعدل في ملف جديد.

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