---
title: تحويل تنسيقات الصور المختلفة إلى PDF في .NET
linktitle: تحويل الصور إلى PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 60
url: /ar/net/convert-images-format-to-pdf/
lastmod: "2021-11-01"
description: تحويل تنسيقات الصور المختلفة مثل CDR و DJVU و BMP و CGM و JPEG و DICOM و PNG و TIFF و EMF و SVG إلى PDF باستخدام C# .NET.
sitemap:
    changefreq: "monthly"
    priority: 0.5
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Convert various Images formats to PDF in .NET",
    "alternativeHeadline": "Convert Multiple Image Formats to PDF with C#",
    "abstract": "تقديم ميزة قوية في Aspose.PDF for .NET التي تمكن من تحويل سلس لتنسيقات الصور المختلفة بما في ذلك BMP و CGM و DICOM و EMF و JPG و PNG و SVG و TIFF و CDR و DJVU إلى مستندات PDF عالية الجودة. توفر هذه الوظيفة طريقة مباشرة لدمج تحويلات الصور إلى PDF داخل تطبيقات .NET الخاصة بك، مما يضمن التعامل الفعال مع محتوى الرسوم المتنوعة.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "4587",
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
    "url": "/net/convert-images-format-to-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/convert-images-format-to-pdf/"
    },
    "dateModified": "2025-04-04",
    "description": "يمكن لـ Aspose.PDF أداء المهام البسيطة والسريعة وكذلك التعامل مع الأهداف الأكثر تعقيدًا. تحقق من القسم التالي للمستخدمين المتقدمين والمطورين."
}
</script>

## نظرة عامة

تشرح هذه المقالة كيفية تحويل تنسيقات الصور المختلفة إلى PDF باستخدام C#. تغطي هذه المواضيع.

تعمل مقتطفات الشيفرة التالية أيضًا مع مكتبة [Aspose.PDF.Drawing](/pdf/ar/net/drawing/).

- [تحويل BMP إلى PDF](#csharp-bmp-to-pdf)
- [تحويل CGM إلى PDF](#csharp-cgm-to-pdf)
- [تحويل DICOM إلى PDF](#csharp-dicom-to-pdf)
- [تحويل EMF إلى PDF](#csharp-emf-to-pdf)
- [تحويل GIF إلى PDF](#csharp-gif-to-pdf)
- [تحويل JPG إلى PDF](#csharp-jpg-to-pdf)
- [تحويل PNG إلى PDF](#csharp-png-to-pdf)
- [تحويل SVG إلى PDF](#csharp-svg-to-pdf)
- [تحويل TIFF إلى PDF](#csharp-tiff-to-pdf)
- [تحويل CDR إلى PDF](#csharp-cdr-to-pdf)
- [تحويل DJVU إلى PDF](#csharp-djvu-to-pdf)
- [تحويل HEIC إلى PDF](#csharp-heic-to-pdf)

## تحويل الصور إلى PDF باستخدام C#

**Aspose.PDF for .NET** يتيح لك تحويل تنسيقات مختلفة من الصور إلى ملفات PDF. توضح مكتبتنا مقتطفات الشيفرة لتحويل أكثر تنسيقات الصور شيوعًا، مثل - BMP و CGM و DICOM و EMF و JPG و PNG و SVG و CDR و HEIC و TIFF.

## تحويل BMP إلى PDF

قم بتحويل ملفات BMP إلى مستند PDF باستخدام مكتبة **Aspose.PDF for .NET**.

تعتبر صور <abbr title="Bitmap Image File">BMP</abbr> ملفات تحمل الامتداد. تمثل BMP ملفات الصور النقطية التي تُستخدم لتخزين الصور الرقمية النقطية. هذه الصور مستقلة عن محول الرسوميات وتسمى أيضًا تنسيق ملف bitmap المستقل عن الجهاز (DIB).
يمكنك تحويل BMP إلى ملفات PDF باستخدام واجهة برمجة التطبيقات Aspose.PDF for .NET. لذلك، يمكنك اتباع الخطوات التالية لتحويل صور BMP:

<a name="csharp-bmp-to-pdf" id="csharp-bmp-to-pdf"><strong>تحويل BMP إلى PDF</strong></a>

1. قم بتهيئة كائن جديد من فئة [Document](https://reference.aspose.com/pdf/ar/net/aspose.pdf/document).
2. قم بتحميل صورة **BMP** المدخلة.
3. أخيرًا، احفظ ملف PDF الناتج.

لذا فإن مقتطف الشيفرة التالي يتبع هذه الخطوات ويظهر كيفية تحويل BMP إلى PDF باستخدام C#:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertBMPtoPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();
        var image = new Aspose.Pdf.Image();
        
        // Load BMP file
        image.File = dataDir + "BMPtoPDF.bmp";
        page.Paragraphs.Add(image);
        
        // Save PDF document
        document.Save(dataDir + "BMPtoPDF_out.pdf");
    }
}
```

{{% alert color="success" %}}
**حاول تحويل BMP إلى PDF عبر الإنترنت**

تقدم Aspose لك تطبيقًا مجانيًا عبر الإنترنت ["BMP إلى PDF"](https://products.aspose.app/pdf/conversion/bmp-to-pdf/)، حيث يمكنك محاولة استكشاف الوظائف وجودة العمل.

[![تحويل Aspose.PDF BMP إلى PDF باستخدام تطبيق مجاني](bmp_to_pdf.png)](https://products.aspose.app/pdf/conversion/bmp-to-pdf/)
{{% /alert %}}

## تحويل CGM إلى PDF

<abbr title="Computer Graphics Metafile">CGM</abbr> هو امتداد ملف لتنسيق ملف رسومات الكمبيوتر المستخدم عادة في تطبيقات CAD (التصميم بمساعدة الكمبيوتر) وعرض الرسومات. CGM هو تنسيق رسومات متجهة يدعم ثلاث طرق ترميز مختلفة: ثنائي (الأفضل لسرعة قراءة البرنامج)، قائم على الأحرف (ينتج أصغر حجم ملف ويسمح بنقل البيانات بشكل أسرع) أو ترميز نص واضح (يسمح للمستخدمين بقراءة وتعديل الملف باستخدام محرر نصوص).

تحقق من مقتطف الشيفرة التالي لتحويل ملفات CGM إلى تنسيق PDF.

<a name="csharp-cgm-to-pdf" id="csharp-cgm-to-pdf"><strong>تحويل CGM إلى PDF</strong></a>

1. أنشئ مثيلًا من فئة [CgmLoadOptions](https://reference.aspose.com/pdf/ar/net/aspose.pdf/cgmloadoptions).
2. أنشئ مثيلًا من فئة [Document](https://reference.aspose.com/pdf/ar/net/aspose.pdf/document) مع ذكر اسم الملف المصدر والخيارات.
3. احفظ المستند بالاسم المطلوب.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertCGMtoPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    var option = new Aspose.Pdf.CgmLoadOptions();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "CGMtoPDF.cgm", option))
    {
        // Save PDF document
        document.Save(dataDir + "CGMtoPDF_out.pdf");
    }
}
```

## تحويل DICOM إلى PDF

<abbr title="Digital Imaging and Communications in Medicine">DICOM</abbr> هو تنسيق معيار الصناعة الطبية لإنشاء وتخزين ونقل وعرض الصور الطبية الرقمية والمستندات للمرضى الذين تم فحصهم.

**Aspose.PDF لـ .NET** يتيح لك تحويل صور DICOM و SVG، ولكن لأسباب تقنية لإضافة الصور تحتاج إلى تحديد نوع الملف الذي سيتم إضافته إلى PDF:

<a name="csharp-dicom-to-pdf" id="csharp-dicom-to-pdf"><strong>تحويل DICOM إلى PDF</strong></a>

1. أنشئ كائنًا من فئة Image.
2. أضف الصورة إلى مجموعة الفقرات في الصفحة.
3. حدد خاصية [FileType](https://reference.aspose.com/pdf/ar/net/aspose.pdf/image/properties/filetype).
4. حدد مسار الملف أو المصدر.
    - إذا كانت الصورة في موقع على القرص الصلب، حدد موقع المسار باستخدام خاصية Image.File.
    - إذا كانت الصورة موجودة في MemoryStream، مرر الكائن الذي يحمل الصورة إلى خاصية Image.ImageStream.

يظهر مقتطف الشيفرة التالي كيفية تحويل ملفات DICOM إلى تنسيق PDF باستخدام Aspose.PDF. يجب عليك تحميل صورة DICOM، وضع الصورة على صفحة في ملف PDF وحفظ الناتج كـ PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertDICOMtoPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create PDF document 
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();
        
        var image = new Aspose.Pdf.Image
        {
            FileType = ImageFileType.Dicom,
            File = dataDir + "DICOMtoPDF.dcm"
        };
        page.Paragraphs.Add(image);

        // Save PDF document
        document.Save(dataDir + "DICOMtoPDF_out.pdf");
    }
}
```

{{% alert color="success" %}}
**حاول تحويل DICOM إلى PDF عبر الإنترنت**

تقدم Aspose لك تطبيقًا مجانيًا عبر الإنترنت ["DICOM إلى PDF"](https://products.aspose.app/pdf/conversion/dicom-to-pdf/)، حيث يمكنك محاولة استكشاف الوظائف وجودة العمل.

[![تحويل Aspose.PDF DICOM إلى PDF باستخدام تطبيق مجاني](dicom_to_pdf.png)](https://products.aspose.app/pdf/conversion/dicom-to-pdf/)
{{% /alert %}}

## تحويل EMF إلى PDF

<abbr title="Enhanced metafile format">EMF</abbr> يخزن الصور الرسومية بشكل مستقل عن الجهاز. تتكون ملفات EMF من سجلات ذات أطوال متغيرة بترتيب زمني يمكن أن تعرض الصورة المخزنة بعد التحليل على أي جهاز إخراج. علاوة على ذلك، يمكنك تحويل EMF إلى صورة PDF باستخدام الخطوات أدناه:

<a name="csharp-emf-to-pdf" id="csharp-emf-to-pdf"><strong>تحويل EMF إلى PDF</strong></a>

1. أولاً، قم بتهيئة كائن من فئة [Document](https://reference.aspose.com/pdf/ar/net/aspose.pdf/document).
2. قم بتحميل ملف صورة **EMF**.
3. أضف صورة EMF المحملة إلى صفحة.
4. احفظ مستند PDF.

علاوة على ذلك، يظهر مقتطف الشيفرة التالي كيفية تحويل EMF إلى PDF باستخدام C# في مقتطف الشيفرة الخاص بك:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertEMFtoPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create PDF document 
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();
        var image = new Aspose.Pdf.Image();
        // Load EMF file
        image.File = dataDir + "EMFtoPDF.emf";

        // Specify page dimension properties
        page.PageInfo.Margin.Bottom = 0;
        page.PageInfo.Margin.Top = 0;
        page.PageInfo.Margin.Left = 0;
        page.PageInfo.Margin.Right = 0;
        page.PageInfo.Width = image.BitmapSize.Width;
        page.PageInfo.Height = image.BitmapSize.Height;

        page.Paragraphs.Add(image);

        // Save PDF document
        document.Save(dataDir + "EMFtoPDF_out.pdf");
    }
}
```

{{% alert color="success" %}}
**حاول تحويل EMF إلى PDF عبر الإنترنت**

تقدم Aspose لك تطبيقًا مجانيًا عبر الإنترنت ["EMF إلى PDF"](https://products.aspose.app/pdf/conversion/emf-to-pdf/)، حيث يمكنك محاولة استكشاف الوظائف وجودة العمل.

[![تحويل Aspose.PDF EMF إلى PDF باستخدام تطبيق مجاني](emf_to_pdf.png)](https://products.aspose.app/pdf/conversion/emf-to-pdf/)
{{% /alert %}}

## تحويل GIF إلى PDF

قم بتحويل ملفات GIF إلى مستند PDF باستخدام مكتبة **Aspose.PDF for .NET**.

<abbr title="Graphics Interchange Format">GIF</abbr> قادر على تخزين بيانات مضغوطة دون فقدان الجودة في تنسيق لا يزيد عن 256 لونًا. تم تطوير تنسيق GIF المستقل عن الأجهزة في عام 1987 (GIF87a) بواسطة CompuServe لنقل الصور النقطية عبر الشبكات.
يمكنك تحويل GIF إلى ملفات PDF باستخدام واجهة برمجة التطبيقات Aspose.PDF for .NET. لذلك، يمكنك اتباع الخطوات التالية لتحويل صور GIF:

<a name="csharp-gif-to-pdf" id="csharp-gif-to-pdf"><strong>تحويل GIF إلى PDF</strong></a>

1. قم بتهيئة كائن جديد من فئة [Document](https://reference.aspose.com/pdf/ar/net/aspose.pdf/document).
2. قم بتحميل صورة **GIF** المدخلة.
3. أخيرًا، احفظ ملف PDF الناتج.

لذا فإن مقتطف الشيفرة التالي يتبع هذه الخطوات ويظهر كيفية تحويل BMP إلى PDF باستخدام C#:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertGIFtoPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();
        var image = new Aspose.Pdf.Image();
        
        // Load sample GIF image file
        image.File = dataDir + "GIFtoPDF.gif";
        page.Paragraphs.Add(image);

        // Save PDF document
        document.Save(dataDir + "GIFtoPDF_out.pdf");
    }
}
```

{{% alert color="success" %}}
**حاول تحويل GIF إلى PDF عبر الإنترنت**

تقدم Aspose لك تطبيقًا مجانيًا عبر الإنترنت ["GIF إلى PDF"](https://products.aspose.app/pdf/conversion/gif-to-pdf/)، حيث يمكنك محاولة استكشاف الوظائف وجودة العمل.

[![تحويل Aspose.PDF GIF إلى PDF باستخدام تطبيق مجاني](bmp_to_pdf.png)](https://products.aspose.app/pdf/conversion/gif-to-pdf/)
{{% /alert %}}

## تحويل JPG إلى PDF

لا داعي للتساؤل عن كيفية تحويل JPG إلى PDF، لأن مكتبة **Apose.PDF لـ .NET** لديها أفضل حل.

يمكنك بسهولة تحويل صور JPG إلى PDF باستخدام Aspose.PDF for .NET من خلال اتباع الخطوات:

<a name="csharp-jpg-to-pdf" id="csharp-jpg-to-pdf"><strong>تحويل JPG إلى PDF</strong></a>

1. قم بتهيئة كائن من فئة [Document](https://reference.aspose.com/page/net/aspose.page/document).
2. أضف صفحة جديدة إلى مستند PDF.
3. قم بتحميل صورة **JPG** وأضفها إلى الفقرة.
4. احفظ الناتج كـ PDF.

يظهر مقتطف الشيفرة أدناه كيفية تحويل صورة JPG إلى PDF باستخدام C#:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertJPGtoPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create PDF document 
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();
        var image = new Aspose.Pdf.Image();
        // Load input JPG file
        image.File = dataDir + "JPGtoPDF.jpg";
        
        // Add image on a page
        page.Paragraphs.Add(image);
        
        // Save PDF document
        document.Save(dataDir + "JPGtoPDF_out.pdf");
    }
}
```

ثم يمكنك رؤية كيفية تحويل صورة إلى PDF بنفس ارتفاع وعرض الصفحة. سنقوم بالحصول على أبعاد الصورة وضبط أبعاد صفحة مستند PDF وفقًا لذلك باستخدام الخطوات أدناه:

1. قم بتحميل ملف الصورة المدخلة.
1. قم بتعيين الارتفاع والعرض والهوامش للصفحة.
1. احفظ ملف PDF الناتج.

يظهر مقتطف الشيفرة التالي كيفية تحويل صورة إلى PDF بنفس ارتفاع وعرض الصفحة باستخدام C#:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertJPGtoPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();
        var image = new Aspose.Pdf.Image();
        // Load JPEG file
        image.File = dataDir + "JPGtoPDF.jpg";
        
        // Read Height of input image
        page.PageInfo.Height = image.BitmapSize.Height;
        // Read Width of input image
        page.PageInfo.Width = image.BitmapSize.Width;
        page.PageInfo.Margin.Bottom = 0;
        page.PageInfo.Margin.Top = 0;
        page.PageInfo.Margin.Right = 0;
        page.PageInfo.Margin.Left = 0;
        page.Paragraphs.Add(image);
        
        // Save PDF document
        document.Save(dataDir + "JPGtoPDF_out.pdf");
    }
}
```

{{% alert color="success" %}}
**حاول تحويل JPG إلى PDF عبر الإنترنت**

تقدم Aspose لك تطبيقًا مجانيًا عبر الإنترنت ["JPG إلى PDF"](https://products.aspose.app/pdf/conversion/jpg-to-pdf/)، حيث يمكنك محاولة استكشاف الوظائف وجودة العمل.

[![تحويل Aspose.PDF JPG إلى PDF باستخدام تطبيق مجاني](jpg_to_pdf.png)](https://products.aspose.app/pdf/conversion/jpg-to-pdf/)
{{% /alert %}}

## تحويل PNG إلى PDF

**Aspose.PDF for .NET** يدعم ميزة تحويل صور PNG إلى تنسيق PDF. تحقق من مقتطف الشيفرة التالي لتحقيق مهمتك.

<abbr title="Portable Network Graphics">PNG</abbr> تشير إلى نوع من تنسيق ملفات الصور النقطية التي تستخدم الضغط بدون فقد، مما يجعلها شائعة بين مستخدميها.

يمكنك تحويل PNG إلى صورة PDF باستخدام الخطوات أدناه:

<a name="csharp-png-to-pdf" id="csharp-png-to-pdf"><strong>تحويل PNG إلى PDF</strong></a>

1. قم بتحميل صورة **PNG** المدخلة.
2. اقرأ قيم الارتفاع والعرض.
3. أنشئ كائن جديد من فئة [Document](https://reference.aspose.com/page/net/aspose.page/document) وأضف صفحة.
4. قم بتعيين أبعاد الصفحة.
5. احفظ الملف الناتج.

علاوة على ذلك، يظهر مقتطف الشيفرة أدناه كيفية تحويل PNG إلى PDF باستخدام C# في تطبيقات .NET الخاصة بك:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPNGtoPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();
        var image = new Aspose.Pdf.Image();
        // Load PNG file
        image.File = dataDir + "PNGtoPDF.png";
        
        // Read Height of input image
        page.PageInfo.Height = image.BitmapSize.Height;
        // Read Width of input image
        page.PageInfo.Width = image.BitmapSize.Width;
        page.PageInfo.Margin.Bottom = 0;
        page.PageInfo.Margin.Top = 0;
        page.PageInfo.Margin.Right = 0;
        page.PageInfo.Margin.Left = 0;
        page.Paragraphs.Add(image);
        
        // Save PDF document
        document.Save(dataDir + "PNGtoPDF_out.pdf");
    }
}
```

{{% alert color="success" %}}
**حاول تحويل PNG إلى PDF عبر الإنترنت**

تقدم Aspose لك تطبيقًا مجانيًا عبر الإنترنت ["PNG إلى PDF"](https://products.aspose.app/pdf/conversion/png-to-pdf/)، حيث يمكنك محاولة استكشاف الوظائف وجودة العمل.

[![تحويل Aspose.PDF PNG إلى PDF باستخدام تطبيق مجاني](png_to_pdf.png)](https://products.aspose.app/pdf/conversion/png-to-pdf/)
{{% /alert %}}

## تحويل SVG إلى PDF

**Aspose.PDF for .NET** يوضح كيفية تحويل صور SVG إلى تنسيق PDF وكيفية الحصول على أبعاد ملف <abbr title="Scalable Vector Graphics">SVG</abbr> المصدر.

تعتبر الرسومات المتجهة القابلة للتطوير (SVG) مجموعة من المواصفات لتنسيق ملف قائم على XML للرسومات المتجهة ثنائية الأبعاد، سواء كانت ثابتة أو ديناميكية (تفاعلية أو متحركة). تعتبر مواصفة SVG معيارًا مفتوحًا تم تطويره بواسطة اتحاد الويب العالمي (W3C) منذ عام 1999.

تُعرف صور SVG وسلوكياتها في ملفات نصية XML. وهذا يعني أنه يمكن البحث عنها وفهرستها وبرمجتها، وإذا لزم الأمر، ضغطها. كملفات XML، يمكن إنشاء وتحرير صور SVG باستخدام أي محرر نصوص، ولكن من الأكثر ملاءمة غالبًا إنشاؤها باستخدام برامج الرسم مثل Inkscape.

{{% alert color="success" %}}
**حاول تحويل تنسيق SVG إلى PDF عبر الإنترنت**

تقدم Aspose.PDF for .NET لك تطبيقًا مجانيًا عبر الإنترنت ["SVG إلى PDF"](https://products.aspose.app/pdf/conversion/svg-to-pdf)، حيث يمكنك محاولة استكشاف الوظائف وجودة العمل.

[![تحويل Aspose.PDF SVG إلى PDF باستخدام تطبيق مجاني](svg_to_pdf.png)](https://products.aspose.app/pdf/conversion/svg-to-pdf)
{{% /alert %}}

لتحويل ملفات SVG إلى PDF، استخدم الفئة المسماة [SvgLoadOptions](https://reference.aspose.com/pdf/ar/net/aspose.pdf/svgloadoptions) التي تُستخدم لتهيئة كائن [`LoadOptions`](https://reference.aspose.com/pdf/ar/net/aspose.pdf/loadoptions). لاحقًا، يتم تمرير هذا الكائن كوسيط أثناء تهيئة كائن Document ويساعد محرك عرض PDF في تحديد تنسيق الإدخال للمستند المصدر.

<a name="csharp-svg-to-pdf" id="csharp-svg-to-pdf"><strong>تحويل SVG إلى PDF</strong></a>

1. أنشئ مثيلًا من فئة [`SvgLoadOptions`](https://reference.aspose.com/pdf/ar/net/aspose.pdf/loadoptions).
2. أنشئ مثيلًا من فئة [`Document`](https://reference.aspose.com/pdf/ar/net/aspose.pdf/document) مع ذكر اسم الملف المصدر والخيارات.
3. احفظ المستند بالاسم المطلوب.

يظهر مقتطف الشيفرة التالي عملية تحويل ملف SVG إلى تنسيق PDF باستخدام Aspose.PDF for .NET.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertSVGtoPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    var option = new Aspose.Pdf.SvgLoadOptions();
    // Open SVG file 
    using (var document = new Aspose.Pdf.Document(dataDir + "SVGtoPDF.svg", option))
    {
        // Save PDF document
        document.Save(dataDir + "SVGtoPDF_out.pdf");
    }
}
```

## الحصول على أبعاد SVG

من الممكن أيضًا الحصول على أبعاد ملف SVG المصدر. يمكن أن تكون هذه المعلومات مفيدة إذا أردنا أن تغطي SVG الصفحة بالكامل من ملف PDF الناتج. تلبي خاصية AdjustPageSize في فئة SvgLoadOption هذا المتطلب. القيمة الافتراضية لهذه الخاصية هي false. إذا تم تعيين القيمة على true، سيكون لملف PDF الناتج نفس الحجم (الأبعاد) مثل SVG المصدر.

يظهر مقتطف الشيفرة التالي عملية الحصول على أبعاد ملف SVG المصدر وتوليد ملف PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertSVGtoPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

    var loadopt = new Aspose.Pdf.SvgLoadOptions();
    loadopt.AdjustPageSize = true;
    // Open SVG file
    using (var document = new Aspose.Pdf.Document(dataDir + "SVGtoPDF.svg", loadopt))
    {
        document.Pages[1].PageInfo.Margin.Top = 0;
        document.Pages[1].PageInfo.Margin.Left = 0;
        document.Pages[1].PageInfo.Margin.Bottom = 0;
        document.Pages[1].PageInfo.Margin.Right = 0;

        // Save PDF document
        document.Save(dataDir + "SVGtoPDF_out.pdf");
    }
    
}
```

### الميزات المدعومة لـ SVG

<table>
    <thead>
        <tr>
            <th>
                <p>علامة SVG</p>
            </th>
            <th>
                <p>استخدام عينة</p>
            </th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>
                <p>circle</p>
            </td>
            <td>
                <code><pre>&lt circle id="r2" cx="10" cy="10" r="10" stroke="blue" stroke-width="2"&gt </pre></code>
            </td>
        </tr>
        <tr>
            <td>
                <p>defs</p>
            </td>
            <td>
                <code>&lt;defs&gt;&nbsp; <br> &lt;rect id="r1" width="15" height="15"
                    stroke="blue" stroke-width="2" /&gt;&nbsp; <br> &lt;circle id="r2"
                    cx="10" cy="10" r="10" stroke="blue" stroke-width="2"/&gt;&nbsp; <br>
                    &lt;circle id="r3" cx="10" cy="10" r="10" stroke="blue" stroke-width="3"/&gt;&nbsp; <br> &lt;/defs&gt;&nbsp; <br> &lt;use
                    x="25" y="40" xlink:href="#r1" fill="red"/&gt;&nbsp; <br> &lt;use
                    x="35" y="15" xlink:href="#r2" fill="green"/&gt;&nbsp; <br> &lt;use
                    x="58" y="50" xlink:href="#r3" fill="blue"/&gt;</code>
            </td>
        </tr>
        <tr>
            <td>
                <p>tref</p>
            </td>
            <td>
                <p>&lt;defs&gt;&nbsp; <br> &nbsp;&nbsp;&nbsp; &lt;text
                    id="ReferencedText"&gt;&nbsp; <br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                    بيانات الحرف المرجعية&nbsp; <br> &nbsp;&nbsp;&nbsp;
                    &lt;/text&gt;&nbsp; <br> &lt;/defs&gt;&nbsp; <br
                        class="atl-forced-newline"> &lt;text x="10" y="100" font-size="15" fill="red" &gt;&nbsp; <br
                        class="atl-forced-newline"> &nbsp;&nbsp;&nbsp; &lt;tref
                    xlink:href="#ReferencedText"/&gt;&nbsp; <br> &lt;/text&gt;</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>use</p>
            </td>
            <td>
                <p>&lt;defs&gt;&nbsp; <br> &nbsp;&nbsp;&nbsp; &lt;text id="Text" x="400"
                    y="200"&nbsp; <br>
                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; font-family="Verdana" font-size="100"
                    text-anchor="middle" &gt;&nbsp; <br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                    نص مقنع&nbsp; <br> &nbsp;&nbsp;&nbsp; &lt;/text&gt;&nbsp; <br
                        class="atl-forced-newline"> &lt;use xlink:href="#Text" fill="blue"&nbsp; /&gt;</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>ellipse&nbsp;</p>
            </td>
            <td>
                <p>&lt;ellipse cx="2.5" cy="1.5" rx="2" ry="1" fill="red" /&gt;</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>g&nbsp;</p>
            </td>
            <td>
                <p>&lt;g fill="none" stroke="dimgray" stroke-width="1.5" &gt;&nbsp; <br>
                    &nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;&lt;line x1="-7"
                    y1="-7" x2="-3" y2="-3"/&gt;&nbsp; <br> &nbsp;&nbsp;
                    &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;&lt;line x1="7" y1="7" x2="3"
                    y2="3"/&gt;&nbsp; <br> &nbsp;&nbsp; &nbsp;&nbsp;&nbsp;
                    &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;&lt;line x1="-7" y1="7" x2="-3" y2="3"/&gt;&nbsp;
                    <br> &nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;
                    &nbsp;&nbsp;&nbsp; &nbsp;&lt;line x1="7" y1="-7" x2="3" y2="-3"/&gt;&nbsp; <br
                        class="atl-forced-newline"> &lt;/g&gt;&nbsp;</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>image</p>
            </td>
            <td>
                <p>&lt;image id="ShadedRelief" x="24" y="4" width="64" height="82" xlink:href="relief.jpg"
                    /&gt;&nbsp;</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>line</p>
            </td>
            <td>
                <p>&lt;line style="stroke:#eea;stroke-width:8" x1="10" y1="30" x2="260" y2="100"/&gt;&nbsp;</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>path</p>
            </td>
            <td>
                <p>&lt;path style="fill:#daa;fill-rule:evenodd;stroke:red" d="M 230,150 C 290,30 10,255 110,140 z
                    "/&gt;&nbsp;</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>style</p>
            </td>
            <td>
                <p>&lt;path style="fill:#daa;fill-rule:evenodd;stroke:red" d="M 230,150 C 290,30 10,255 110,140 z
                    "/&gt;</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>polygon</p>
            </td>
            <td>
                <p>&lt;polygon style="stroke:#24a;stroke-width:1.5;fill:#eefefe" points="10,10 180,10 10,250 10,10"
                    /&gt;</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>polyline</p>
            </td>
            <td>
                <p>&lt;polyline fill="none" stroke="dimgray" stroke-width="1" points="-3,-6 3,-6 3,1 5,1 0,7 -5,1
                    -3,1 -3,-5"/&gt;</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>rect&nbsp;</p>
            </td>
            <td>
                <p>&lt;rect x="0" y="0" width="400" height="600" stroke="none" fill="aliceblue" /&gt;</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>svg</p>
            </td>
            <td>
                <p>&lt;svg xmlns="http://www.w3.org/2000/svg" version="1.1" width="10cm" height="5cm" &gt;</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>text</p>
            </td>
            <td>
                <p>&lt;text font-family="sans-serif" fill="dimgray" font-size="22px" font-weight="bold" x="58"
                    y="30" pointer-events="none"&gt;عنوان الخريطة&lt;/text&gt;</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>font</p>
            </td>
            <td>
                <p>&lt;text x="10" y="100" font-size="15" fill="red" &gt;&nbsp; <br>
                    &nbsp;&nbsp;&nbsp; نص عينة&nbsp; <br> &lt;/text&gt;</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>tspan</p>
            </td>
            <td>
                <p>&lt;tspan dy="25" x="25"&gt;ستة قيم إدخال لون الحبر. هنا سيكون &lt;/tspan&gt;</p>
            </td>
        </tr>
    </tbody>
</table>

## تحويل TIFF إلى PDF

يدعم **Aspose.PDF** تنسيق ملف، سواء كان صورة TIFF أحادية الإطار أو متعددة الإطارات <abbr title="Tag Image File Format">TIFF</abbr>. وهذا يعني أنه يمكنك تحويل صورة TIFF إلى PDF في تطبيقات .NET الخاصة بك.

يمثل TIFF أو TIF، تنسيق ملف الصورة المسمى، الصور النقطية التي تهدف للاستخدام على مجموعة متنوعة من الأجهزة التي تتوافق مع معيار تنسيق الملف هذا. يمكن أن تحتوي صورة TIFF على عدة إطارات مع صور مختلفة. كما أن تنسيق ملف Aspose.PDF مدعوم، سواء كان صورة TIFF أحادية الإطار أو متعددة الإطارات.

يمكنك تحويل TIFF إلى PDF بنفس الطريقة التي يتم بها تحويل باقي تنسيقات ملفات الرسوم النقطية:

<a name="csharp-tiff-to-pdf" id="csharp-tiff-to-pdf"><strong>تحويل TIFF إلى PDF</strong></a>

1. أنشئ كائن جديد من فئة [Document](https://reference.aspose.com/pdf/ar/net/aspose.pdf/document) وأضف صفحة.
2. قم بتحميل صورة **TIFF** المدخلة.
3. احفظ مستند PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertTIFFtoPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        document.Pages.Add();
        var image = new Aspose.Pdf.Image();
        
        // Load sample Tiff image file
        image.File = dataDir + "TIFFtoPDF.tiff";
        document.Pages[1].Paragraphs.Add(image);
        
        // Save PDF document
        document.Save(dataDir + "TIFFtoPDF_out.pdf");
    }
}
```

في حال كنت بحاجة إلى تحويل صورة TIFF متعددة الصفحات إلى مستند PDF متعدد الصفحات والتحكم في بعض المعلمات، مثل العرض أو نسبة العرض إلى الارتفاع، يرجى اتباع الخطوات التالية:

1. أنشئ مثيلًا من فئة Document.
1. قم بتحميل صورة TIFF المدخلة.
1. احصل على FrameDimension للإطارات.
1. أضف صفحة جديدة لكل إطار.
1. أخيرًا، احفظ الصور في صفحات PDF.

يظهر مقتطف الشيفرة التالي كيفية تحويل صورة TIFF متعددة الصفحات أو متعددة الإطارات إلى PDF باستخدام C#:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertTIFFtoPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        using (var bitmap = new System.Drawing.Bitmap(File.OpenRead(dataDir + "TIFFtoPDF.tif")))
        {
            // Convert multi page or multi frame TIFF to PDF
            var dimension = new FrameDimension(bitmap.FrameDimensionsList[0]);
            var frameCount = bitmap.GetFrameCount(dimension);

            // Iterate through each frame
            for (int frameIdx = 0; frameIdx <= frameCount - 1; frameIdx++)
            {
                var page = document.Pages.Add();

                bitmap.SelectActiveFrame(dimension, frameIdx);

                using (var currentImage = new MemoryStream())
                {
                    bitmap.Save(currentImage, ImageFormat.Tiff);

                    var imageht = new Aspose.Pdf.Image
                    {
                        ImageStream = currentImage,
                        //Apply some other options
                        //ImageScale = 0.5
                    };
                    page.Paragraphs.Add(imageht);
                }
            }
        }

        // Save PDF document
        document.Save(dataDir + "TIFFtoPDF_out.pdf");
    }
}
```

## تحويل CDR إلى PDF

<abbr title="CDR">CDR</abbr> هو تنسيق ملف تم تطويره بواسطة شركة Corel ويستخدم بشكل رئيسي للصور والرسومات المتجهة. يتم التعرف على تنسيق ملف CDR من قبل معظم برامج تحرير الصور. تنسيق CDR هو التنسيق الافتراضي لتطبيقات Corel Draw.

تحقق من مقتطف الشيفرة التالي لتحويل ملفات CDR إلى تنسيق PDF.

<a name="csharp-cdr-to-pdf" id="csharp-cdr-to-pdf"><strong>تحويل CDR إلى PDF</strong></a>

1. أنشئ مثيلًا من فئة [CdrLoadOptions](https://reference.aspose.com/pdf/ar/net/aspose.pdf/cdrloadoptions/).
2. أنشئ مثيلًا من فئة [Document](https://reference.aspose.com/pdf/ar/net/aspose.pdf/document) مع ذكر اسم الملف المصدر والخيارات.
3. احفظ المستند بالاسم المطلوب.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertCDRtoPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open CDR file
    using (var document = new Aspose.Pdf.Document(dataDir + "CDRtoPDF.cdr", new CdrLoadOptions()))
    {
        // Save PDF document
        document.Save(dataDir + "CDRtoPDF_out.pdf");
    }
}
```

## تحويل DJVU إلى PDF

<abbr title="DJVU">DjVu</abbr> هو تنسيق صورة مضغوط تم تطويره بواسطة LizardTech. تم تصميم هذا التنسيق بشكل أساسي لتخزين أنواع مختلفة من المستندات الممسوحة ضوئيًا؛ خاصة المستندات التي تحتوي على مزيج من النصوص والصور وصور الألوان المفهرسة والرسومات الخطية.

تحقق من مقتطف الشيفرة التالي لتحويل ملفات DJVU إلى تنسيق PDF.

<a name="csharp-djvu-to-pdf" id="csharp-djvu-to-pdf"><strong>تحويل DJVU إلى PDF</strong></a>

1. أنشئ مثيلًا من فئة [DjvuLoadOptions](https://reference.aspose.com/pdf/ar/net/aspose.pdf/djvuloadoptions/).
2. أنشئ مثيلًا من فئة [Document](https://reference.aspose.com/pdf/ar/net/aspose.pdf/document) مع ذكر اسم الملف المصدر والخيارات.
3. احفظ المستند بالاسم المطلوب.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertDJVUtoPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
    
    // Open DJVU file
    using (var document = new Aspose.Pdf.Document(dataDir + "CDRtoPDF.djvu", new DjvuLoadOptions()))
    {
        // Save PDF document
        document.Save(dataDir + "CDRtoPDF_out.pdf");
    }
}
```

## تحويل HEIC إلى PDF

<a name="csharp-heic-to-pdf" id="csharp-heic-to-pdf"><strong>تحويل HEIC إلى PDF</strong></a>

ملف HEIC هو تنسيق ملف صورة حاوية عالية الكفاءة يمكن أن تخزن صورًا متعددة كمجموعة في ملف واحد.
لتحميل صور HEIC، تحتاج إلى إضافة مرجع إلى حزمة https://www.nuget.org/packages/FileFormat.Heic/.
قم بتحويل صور HEIC إلى PDF باستخدام Aspose.PDF:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertHEICtoPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open HEIC file
    using (var fs = new FileStream(dataDir + "HEICtoPDF.heic", FileMode.Open))
    {
        var image = FileFormat.Heic.Decoder.HeicImage.Load(fs);
        var pixels = image.GetByteArray(PixelFormat.Rgb24);
        var width = (int)image.Width;
        var height = (int)image.Height;

        using (var document = new Aspose.Pdf.Document())
        {
            var page = document.Pages.Add();
            var asposeImage = new Aspose.Pdf.Image();
            asposeImage.BitmapInfo = new Aspose.Pdf.BitmapInfo(pixels, width, height, Aspose.Pdf.BitmapInfo.PixelFormat.Rgb24);
            page.PageInfo.Height = height;
            page.PageInfo.Width = width;
            page.PageInfo.Margin.Bottom = 0;
            page.PageInfo.Margin.Top = 0;
            page.PageInfo.Margin.Right = 0;
            page.PageInfo.Margin.Left = 0;

            page.Paragraphs.Add(asposeImage);

            // Save PDF document
            document.Save(dataDir + "HEICtoPDF_out.pdf");
        }
    }
}
```