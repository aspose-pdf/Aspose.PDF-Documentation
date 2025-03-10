---
title: تحويل HTML إلى PDF في .NET
linktitle: تحويل HTML إلى ملف PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 40
url: /ar/net/convert-html-to-pdf/
lastmod: "2021-11-01"
description: يوضح هذا الموضوع كيفية تحويل HTML إلى PDF و MHTML إلى PDF باستخدام Aspose.PDF.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Convert HTML to PDF in .NET",
    "alternativeHeadline": "Convert HTML and MHTML to PDF with C#",
    "abstract": "تتيح ميزة التحويل في Aspose.PDF for .NET التحويل السلس لمستندات HTML و MHTML إلى ملفات PDF عالية الجودة. مع خيارات التخصيص المتقدمة، يمكن للمستخدمين التحكم في تضمين الخطوط، واستعلامات الوسائط، وإدارة الموارد الخارجية مع ضمان عرض صفحات الويب أو ملفات HTML المحلية بدقة في تنسيق PDF مع مرونة مصممة لتلبية احتياجاتهم المحددة.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1889",
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
    "url": "/net/convert-html-to-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/convert-html-to-pdf/"
    },
    "dateModified": "2024-11-25",
    "description": "يمكن لـ Aspose.PDF أداء المهام البسيطة والسلسة ولكن أيضًا التعامل مع الأهداف الأكثر تعقيدًا. تحقق من القسم التالي للمستخدمين المتقدمين والمطورين."
}
</script>

## نظرة عامة 

تشرح هذه المقالة كيفية **تحويل HTML إلى PDF باستخدام C#**. تغطي المواضيع التالية.

يعمل مقتطف الكود التالي أيضًا مع مكتبة [Aspose.PDF.Drawing](/pdf/ar/net/drawing/) .

_التنسيق_: **HTML**
- [C# HTML إلى PDF](#csharp-html-to-pdf)
- [C# تحويل HTML إلى PDF](#csharp-html-to-pdf)
- [C# كيفية تحويل HTML إلى PDF](#csharp-html-to-pdf)

_التنسيق_: **MHTML**
- [C# MHTML إلى PDF](#csharp-mhtml-to-pdf)
- [C# تحويل MHTML إلى PDF](#csharp-mhtml-to-pdf)
- [C# كيفية تحويل MHTML إلى PDF](#csharp-mhtml-to-pdf)

_التنسيق_: **WebPage**
- [C# WebPage إلى PDF](#csharp-webpage-to-pdf)
- [C# تحويل WebPage إلى PDF](#csharp-webpage-to-pdf)
- [C# كيفية تحويل WebPage إلى PDF](#csharp-webpage-to-pdf)

## تحويل C# HTML إلى PDF

**Aspose.PDF for .NET** هو واجهة برمجة تطبيقات معالجة PDF تتيح لك تحويل أي مستندات HTML موجودة إلى PDF بسلاسة. يمكن تخصيص عملية تحويل HTML إلى PDF بشكل مرن.

## تحويل HTML إلى PDF

يظهر نموذج كود C# التالي كيفية تحويل مستند HTML إلى PDF.

<a name="csharp-html-to-pdf"><strong>الخطوات: تحويل HTML إلى PDF في C#</strong></a>

1. إنشاء مثيل من فئة [HtmlLoadOptions](https://reference.aspose.com/pdf/net/aspose.pdf/htmlloadoptions/) .
2. تهيئة كائن [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document/) .
3. حفظ مستند PDF الناتج عن طريق استدعاء **Document.Save()** .

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertHTMLtoPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Load the HTML file into a document using HtmlLoadOptions
    var options = new Aspose.Pdf.HtmlLoadOptions();

    // Open HTML document
    using (var document = new Aspose.Pdf.Document(dataDir + "test.html", options))
    {
        // Save PDF document
        document.Save(dataDir + "ConvertHTMLtoPDF_out.pdf");
    }
}
```

{{% alert color="success" %}}
**حاول تحويل HTML إلى PDF عبر الإنترنت**

تقدم Aspose لك تطبيقًا مجانيًا عبر الإنترنت ["HTML إلى PDF"](https://products.aspose.app/html/en/conversion/html-to-pdf) ، حيث يمكنك تجربة الوظائف والجودة التي يعمل بها.

[![تحويل Aspose.PDF HTML إلى PDF باستخدام تطبيق مجاني](html.png)](https://products.aspose.app/html/en/conversion/html-to-pdf)
{{% /alert %}}

## التحويل المتقدم من HTML إلى PDF

يمتلك محرك تحويل HTML عدة خيارات تتيح لنا التحكم في عملية التحويل.

### دعم استعلامات الوسائط

استعلامات الوسائط هي تقنية شائعة لتقديم ورقة أنماط مخصصة لأجهزة مختلفة. يمكننا تعيين نوع الجهاز باستخدام خاصية [`HtmlMediaType`](https://reference.aspose.com/pdf/net/aspose.pdf/htmlloadoptions/properties/htmlmediatype) .

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertHTMLtoPDFAdvancedMediaType()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Load the HTML file into a document using HtmlLoadOptions with Print media type
    var options = new HtmlLoadOptions
    {
        // Set Print or Screen mode
        HtmlMediaType = Aspose.Pdf.HtmlMediaType.Print
    };

    // Open HTML document
    using (var document = new Aspose.Pdf.Document(dataDir + "test.html", options))
    {
        // Save PDF document
        document.Save(dataDir + "ConvertHTMLtoPDFAdvancedMediaType_out.pdf");
    }
}
```

### تمكين (تعطيل) تضمين الخطوط

تستخدم صفحات HTML غالبًا خطوطًا (مثل الخطوط من المجلد المحلي، خطوط Google، إلخ). يمكننا أيضًا التحكم في تضمين الخطوط في مستند باستخدام خاصية [`IsEmbedFonts`](https://reference.aspose.com/pdf/net/aspose.pdf/htmlloadoptions/properties/isembedfonts) .

```csharp
 // For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
 private static void ConvertHTMLtoPDFAdvancedEmbedFonts()
 {
     // The path to the documents directory
     var dataDir = RunExamples.GetDataDir_AsposePdf();

     // Load the HTML file into a document using HtmlLoadOptions with the font embedding option set
     var options = new Aspose.Pdf.HtmlLoadOptions
     {
         // Disable font embedding
         IsEmbedFonts = false
     };

     // Open HTML document
     using (var document = new Aspose.Pdf.Document(dataDir + "test_fonts.html", options))
     {
         // Save PDF document
         document.Save(dataDir + "ConvertHTMLtoPDFAdvanced_EmbedFonts_out.pdf");
     }
 }
```

### إدارة تحميل الموارد الخارجية

يوفر محرك التحويل آلية تتيح لك التحكم في تحميل بعض الموارد المرتبطة بمستند HTML.
تحتوي فئة [`HtmlLoadOptions`](https://reference.aspose.com/pdf/net/aspose.pdf/htmlloadoptions) على خاصية [`CustomLoaderOfExternalResources`](https://reference.aspose.com/pdf/net/aspose.pdf/htmlloadoptions/fields/customloaderofexternalresources) التي يمكننا من خلالها تحديد سلوك محمل الموارد.
افترض أننا بحاجة إلى استبدال جميع صور PNG بصورة واحدة `test.jpg` واستبدال عنوان URL الخارجي إلى داخلي للموارد الأخرى.
للقيام بذلك، يمكننا تعريف محمل مخصص `SamePictureLoader` ونشير إلى [`CustomLoaderOfExternalResources`](https://reference.aspose.com/pdf/net/aspose.pdf/htmlloadoptions/fields/customloaderofexternalresources) بهذا الاسم.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertHTMLtoPDFAdvanced_DummyImage()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Load the HTML file into a document with a custom resource loader for external images
    var options = new Aspose.Pdf.HtmlLoadOptions
    {
        CustomLoaderOfExternalResources = SamePictureLoader
    };

    // Open HTML document
    using (var document = new Aspose.Pdf.Document(dataDir + "test.html", options))
    {
        // Save PDF document
        document.Save(dataDir + "html_test.pdf");
    }
}

private static Aspose.Pdf.LoadOptions.ResourceLoadingResult SamePictureLoader(string resourceURI)
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();
    Aspose.Pdf.LoadOptions.ResourceLoadingResult result;

    if (resourceURI.EndsWith(".png"))
    {
        byte[] resultBytes = File.ReadAllBytes(dataDir + "test.jpg");
        result = new Aspose.Pdf.LoadOptions.ResourceLoadingResult(resultBytes)
        {
            // Set MIME Type
            MIMETypeIfKnown = "image/jpeg"
        };
    }
    else
    {
        result = new Aspose.Pdf.LoadOptions.ResourceLoadingResult(GetContentFromUrl(resourceURI));
    }
    return result;
}

private static byte[] GetContentFromUrl(string url)
{
    var httpClient = new System.Net.Http.HttpClient();
    return httpClient.GetByteArrayAsync(url).GetAwaiter().GetResult();
}
```

## تحويل صفحة الويب إلى PDF

يختلف تحويل صفحة الويب قليلاً عن تحويل مستند HTML المحلي. من أجل تحويل محتويات صفحة الويب إلى تنسيق PDF، يمكننا أولاً جلب محتويات صفحة HTML باستخدام مثيل HttpClient، وإنشاء كائن Stream، وتمرير المحتويات إلى كائن Document وعرض الناتج في تنسيق PDF.

عند تحويل صفحة ويب مستضافة على خادم ويب إلى PDF:

<a name="csharp-webpage-to-pdf"><strong>الخطوات: تحويل WebPage إلى PDF في C#</strong></a>

1. قراءة محتويات الصفحة باستخدام كائن HttpClient.
1. إنشاء كائن [HtmlLoadOptions](https://reference.aspose.com/pdf/net/aspose.pdf/htmlloadoptions) وتعيين عنوان URL الأساسي.
1. تهيئة كائن Document مع تمرير كائن stream.
1. اختياريًا، تعيين حجم الصفحة و/أو الاتجاه.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertHTMLtoPDFAdvanced_WebPage()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    const string url = "https://en.wikipedia.org/wiki/Aspose_API";

    // Set page size A3 and Landscape orientation;   
    var options = new Aspose.Pdf.HtmlLoadOptions(url)
    {
        PageInfo =
        {
            Width = 842,
            Height = 1191,
            IsLandscape = true
        }
    };

    // Load the web page content as a stream and create a PDF document
    using (var document = new Aspose.Pdf.Document(GetContentFromUrlAsStream(url), options))
    {
        // Save PDF document
        document.Save(dataDir + "html_test.pdf");
    }
}

private static Stream GetContentFromUrlAsStream(string url, System.Net.ICredentials credentials = null)
{
    using (var handler = new System.Net.Http.HttpClientHandler { Credentials = credentials })
    using (var httpClient = new System.Net.Http.HttpClient(handler))
    {
        return httpClient.GetStreamAsync(url).GetAwaiter().GetResult();
    }
}
```

### توفير بيانات الاعتماد لتحويل صفحة الويب إلى PDF

أحيانًا نحتاج إلى إجراء تحويل لملفات HTML التي تتطلب مصادقة وامتيازات وصول، بحيث يمكن فقط للمستخدمين المصرح لهم جلب محتويات الصفحة. يشمل ذلك أيضًا السيناريو الذي يتم فيه جلب بعض الموارد/البيانات المشار إليها داخل HTML من خادم خارجي يتطلب مصادقة، ومن أجل تلبية هذا المتطلب، تمت إضافة خاصية [`ExternalResourcesCredentials`](https://reference.aspose.com/pdf/net/aspose.pdf/htmlloadoptions/fields/externalresourcescredentials) إلى فئة [`HtmlLoadOptions`](https://reference.aspose.com/pdf/net/aspose.pdf/htmlloadoptions) . يظهر مقتطف الكود التالي الخطوات اللازمة لتمرير بيانات الاعتماد لطلب HTML وموارده المعنية أثناء تحويل ملف HTML إلى PDF.

```csharp
 // For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
 private static void ConvertHTMLtoPDFAdvancedAuthorized()
 {
     // The path to the documents directory
     var dataDir = RunExamples.GetDataDir_AsposePdf();

     const string url = "http://httpbin.org/basic-auth/user1/password1";
     var credentials = new System.Net.NetworkCredential("user1", "password1");

     var options = new Aspose.Pdf.HtmlLoadOptions(url)
     {
         ExternalResourcesCredentials = credentials
     };

     using (var document = new Aspose.Pdf.Document(GetContentFromUrlAsStream(url, credentials), options))
     {
         // Save PDF document
         document.Save(dataDir + "HtmlTest_out.pdf");
     }
 }

private static Stream GetContentFromUrlAsStream(string url, System.Net.ICredentials credentials = null)
{
    using (var handler = new System.Net.Http.HttpClientHandler { Credentials = credentials })
    using (var httpClient = new System.Net.Http.HttpClient(handler))
    {
        return httpClient.GetStreamAsync(url).GetAwaiter().GetResult();
    }
}
```

### عرض جميع محتويات HTML في صفحة واحدة

توفر Aspose.PDF for .NET القدرة على عرض جميع المحتويات في صفحة واحدة أثناء تحويل ملف HTML إلى تنسيق PDF. على سبيل المثال، إذا كان لديك بعض محتويات HTML التي يكون حجم الناتج أكبر من صفحة واحدة، يمكنك استخدام خيار عرض بيانات الناتج في صفحة PDF واحدة. لاستخدام هذا الخيار، تم توسيع فئة HtmlLoadOptions بواسطة علامة IsRenderToSinglePage. يظهر مقتطف الكود أدناه كيفية استخدام هذه الوظيفة.

```csharp
 // For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
 private static void ConvertHTMLtoPDFAdvancedSinglePageRendering()
 {
     // The path to the documents directory
     var dataDir = RunExamples.GetDataDir_AsposePdf();

     // Initialize HtmlLoadOptions
     var options = new Aspose.Pdf.HtmlLoadOptions
     {
         // Set Render to single page property
         IsRenderToSinglePage = true
     };

     // Open PDF document
     using (var document = new Aspose.Pdf.Document(dataDir + "HTMLToPDF.html", options))
     {
         // Save PDF document
         document.Save(dataDir + "RenderContentToSamePage_out.pdf");
     }
 }
```

### عرض HTML مع بيانات SVG

توفر Aspose.PDF for .NET القدرة على تحويل صفحة HTML إلى مستند PDF. نظرًا لأن HTML يسمح بإضافة عنصر رسومي SVG كعلامة في الصفحة، فإن Aspose.PDF تدعم أيضًا تحويل مثل هذه البيانات إلى ملف PDF الناتج. يظهر مقتطف الكود التالي كيفية تحويل ملفات HTML مع علامات رسومية SVG إلى مستندات PDF معلمة.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertHTMLtoPDFWithSVG()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Initialize HtmlLoadOptions
    var options = new Aspose.Pdf.HtmlLoadOptions(Path.GetDirectoryName(dataDir + "HTMLSVG.html"));

    // Initialize Document object
    using (var document = new Aspose.Pdf.Document(dataDir + "HTMLSVG.html", options))
    {
        // Save PDF document
        document.Save(dataDir + "RenderHTMLwithSVGData_out.pdf");
    }
}
```

## تحويل MHTML إلى PDF 

{{% alert color="success" %}}
**حاول تحويل MHTML إلى PDF عبر الإنترنت**

تقدم Aspose.PDF for .NET لك تطبيقًا مجانيًا عبر الإنترنت ["MHTML إلى PDF"](https://products.aspose.app/pdf/conversion/mhtml-to-pdf) ، حيث يمكنك تجربة الوظائف والجودة التي يعمل بها.

[![تحويل Aspose.PDF MHTML إلى PDF باستخدام تطبيق مجاني](mhtml.png)](https://products.aspose.app/pdf/conversion/mhtml-to-pdf)
{{% /alert %}}

<abbr title="MIME encapsulation of aggregate HTML documents">MHTML</abbr>، اختصار لـ MIME HTML، هو تنسيق أرشيف صفحة ويب يستخدم لدمج الموارد التي يتم تمثيلها عادةً بواسطة روابط خارجية (مثل الصور، الرسوم المتحركة Flash، تطبيقات Java، وملفات الصوت) مع كود HTML في ملف واحد. يتم ترميز محتوى ملف MHTML كما لو كان رسالة بريد إلكتروني HTML، باستخدام نوع MIME multipart/related. يمكن لـ Aspose.PDF for .NET تحويل ملفات HTML إلى تنسيق PDF ومع إصدار Aspose.PDF for .NET 9.0.0، قدمنا ميزة جديدة تتيح لك تحويل ملفات MHTML إلى تنسيق PDF. يظهر مقتطف الكود التالي كيفية تحويل ملفات MHTML إلى تنسيق PDF باستخدام C#:

<a name="csharp-mhtml-to-pdf"><strong>الخطوات: تحويل MHTML إلى PDF في C#</strong></a>

1. إنشاء مثيل من فئة [MhtLoadOptions](https://reference.aspose.com/pdf/net/aspose.pdf/mhtloadoptions/) .
2. تهيئة كائن [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document/) .
3. حفظ مستند PDF الناتج عن طريق استدعاء **Document.Save()** .

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertMHTtoPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Initialize MhtLoadOptions with page setup
    var options = new Aspose.Pdf.MhtLoadOptions()
    {
        PageInfo = { Width = 842, Height = 1191, IsLandscape = true }
    };

    // Initialize Document object using the MHT file and options
    using (var document = new Aspose.Pdf.Document(dataDir + "fileformatinfo.mht", options))
    {
        // Save PDF document
        document.Save(dataDir + "MhtmlTest_out.pdf");
    }
}
```

## انظر أيضًا 

تغطي هذه المقالة أيضًا هذه المواضيع. الأكواد هي نفسها كما في الأعلى.

_التنسيق_: **HTML**
- [C# كود HTML إلى PDF](#csharp-html-to-pdf)
- [C# واجهة برمجة تطبيقات HTML إلى PDF](#csharp-html-to-pdf)
- [C# HTML إلى PDF برمجيًا](#csharp-html-to-pdf)
- [C# مكتبة HTML إلى PDF](#csharp-html-to-pdf)
- [C# حفظ HTML كـ PDF](#csharp-html-to-pdf)
- [C# توليد PDF من HTML](#csharp-html-to-pdf)
- [C# إنشاء PDF من HTML](#csharp-html-to-pdf)
- [C# محول HTML إلى PDF](#csharp-html-to-pdf)

_التنسيق_: **MHTML**
- [C# كود MHTML إلى PDF](#csharp-mhtml-to-pdf)
- [C# واجهة برمجة تطبيقات MHTML إلى PDF](#csharp-mhtml-to-pdf)
- [C# MHTML إلى PDF برمجيًا](#csharp-mhtml-to-pdf)
- [C# مكتبة MHTML إلى PDF](#csharp-mhtml-to-pdf)
- [C# حفظ MHTML كـ PDF](#csharp-mhtml-to-pdf)
- [C# توليد PDF من MHTML](#csharp-mhtml-to-pdf)
- [C# إنشاء PDF من MHTML](#csharp-mhtml-to-pdf)
- [C# محول MHTML إلى PDF](#csharp-mhtml-to-pdf)

_التنسيق_: **WebPage**
- [C# كود WebPage إلى PDF](#csharp-webpage-to-pdf)
- [C# واجهة برمجة تطبيقات WebPage إلى PDF](#csharp-webpage-to-pdf)
- [C# WebPage إلى PDF برمجيًا](#csharp-webpage-to-pdf)
- [C# مكتبة WebPage إلى PDF](#csharp-webpage-to-pdf)
- [C# حفظ WebPage كـ PDF](#csharp-webpage-to-pdf)
- [C# توليد PDF من WebPage](#csharp-webpage-to-pdf)
- [C# إنشاء PDF من WebPage](#csharp-webpage-to-pdf)
- [C# محول WebPage إلى PDF](#csharp-webpage-to-pdf)