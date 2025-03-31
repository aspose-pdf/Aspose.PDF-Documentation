---
title: إضافة رأس وتذييل إلى PDF
linktitle: إضافة رأس وتذييل إلى PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 70
url: /ar/net/add-headers-and-footers-of-pdf-file/
description: Aspose.PDF for .NET يتيح لك إضافة رؤوس وتذييلات إلى ملف PDF الخاص بك باستخدام فئة TextStamp.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Add Header and Footer to PDF",
    "alternativeHeadline": "Add Custom Headers and Footers to PDF Files",
    "abstract": "Aspose.PDF for .NET يقدم ميزة قوية تتيح للمستخدمين إثراء مستندات PDF الخاصة بهم من خلال إضافة رؤوس وتذييلات قابلة للتخصيص. باستخدام فئات TextStamp و ImageStamp، يمكن للمطورين دمج النصوص والصور بسهولة، وتخصيص موضعها ومظهرها لتناسب تنسيقات وأنماط المستندات المختلفة. هذا يعزز من احترافية المستند وقابليته للقراءة، مما يجعله مثاليًا للتقارير والفواتير وغيرها من الاتصالات الرسمية.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1549",
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
    "url": "/net/add-headers-and-footers-of-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-headers-and-footers-of-pdf-file/"
    },
    "dateModified": "2024-11-26",
    "description": "Aspose.PDF for .NET يتيح لك إضافة رؤوس وتذييلات إلى ملف PDF الخاص بك باستخدام فئة TextStamp."
}
</script>

**Aspose.PDF for .NET** يتيح لك إضافة رأس وتذييل في ملف PDF الحالي الخاص بك. يمكنك إضافة صور أو نص إلى مستند PDF. أيضًا، حاول إضافة رؤوس مختلفة في ملف PDF واحد باستخدام C#.

تعمل مقتطفات الشيفرة التالية أيضًا مع مكتبة [Aspose.PDF.Drawing](/pdf/ar/net/drawing/) .

## إضافة نص في رأس ملف PDF

يمكنك استخدام فئة [TextStamp](https://reference.aspose.com/pdf/ar/net/aspose.pdf/textstamp) لإضافة نص في رأس ملف PDF. توفر فئة TextStamp الخصائص اللازمة لإنشاء ختم نصي مثل حجم الخط، نمط الخط، ولون الخط، إلخ. لإضافة نص في الرأس، تحتاج إلى إنشاء كائن Document وكائن TextStamp باستخدام الخصائص المطلوبة. بعد ذلك، يمكنك استدعاء طريقة AddStamp من الصفحة لإضافة النص في رأس PDF.

تحتاج إلى تعيين خاصية TopMargin بطريقة تضبط النص في منطقة الرأس من PDF الخاص بك. تحتاج أيضًا إلى تعيين HorizontalAlignment إلى Center و VerticalAlignment إلى Top.

تظهر مقتطفات الشيفرة التالية كيفية إضافة نص في رأس ملف PDF باستخدام C#.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddHeaderText()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "TextinHeader.pdf"))
    {
        // Create header as a TextStamp
        var textStamp = new Aspose.Pdf.TextStamp("Header Text")
        {
            TopMargin = 10,
            HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Center,
            VerticalAlignment = Aspose.Pdf.VerticalAlignment.Top
        };

        // Add header on all pages
        foreach (var page in document.Pages)
        {
            page.AddStamp(textStamp);
        }

        // Save PDF document
        document.Save(dataDir + "TextinHeader_out.pdf");
    }
}
```

## إضافة نص في تذييل ملف PDF

يمكنك استخدام فئة TextStamp لإضافة نص في تذييل ملف PDF. توفر فئة TextStamp الخصائص اللازمة لإنشاء ختم نصي مثل حجم الخط، نمط الخط، ولون الخط، إلخ. لإضافة نص في التذييل، تحتاج إلى إنشاء كائن Document وكائن TextStamp باستخدام الخصائص المطلوبة. بعد ذلك، يمكنك استدعاء طريقة AddStamp من الصفحة لإضافة النص في تذييل PDF.

{{% alert color="primary" %}}

تحتاج إلى تعيين خاصية Bottom Margin بطريقة تضبط النص في منطقة التذييل من PDF الخاص بك. تحتاج أيضًا إلى تعيين HorizontalAlignment إلى Center و VerticalAlignment إلى Bottom

{{% /alert %}}

تظهر مقتطفات الشيفرة التالية كيفية إضافة نص في تذييل ملف PDF باستخدام C#.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddFooterText()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "TextinFooter.pdf"))
    {
        // Create footer as a TextStamp
        var textStamp = new Aspose.Pdf.TextStamp("Footer Text")
        {
            BottomMargin = 10,
            HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Center,
            VerticalAlignment = Aspose.Pdf.VerticalAlignment.Bottom
        };

        // Add footer on all pages
        foreach (var page in document.Pages)
        {
            page.AddStamp(textStamp);
        }

        // Save PDF document
        document.Save(dataDir + "TextinFooter_out.pdf");
    }
}
```

## إضافة صورة في رأس ملف PDF

يمكنك استخدام فئة [ImageStamp](https://reference.aspose.com/pdf/ar/net/aspose.pdf/ImageStamp) لإضافة صورة في رأس ملف PDF. توفر فئة Image Stamp الخصائص اللازمة لإنشاء ختم قائم على الصورة مثل حجم الخط، نمط الخط، ولون الخط، إلخ. لإضافة صورة في الرأس، تحتاج إلى إنشاء كائن Document وكائن Image Stamp باستخدام الخصائص المطلوبة. بعد ذلك، يمكنك استدعاء طريقة [AddStamp](https://reference.aspose.com/pdf/ar/net/aspose.pdf/page/methods/addstamp) من الصفحة لإضافة الصورة في رأس PDF.

{{% alert color="primary" %}}

تحتاج إلى تعيين خاصية TopMargin بطريقة تضبط الصورة في منطقة الرأس من PDF الخاص بك. تحتاج أيضًا إلى تعيين HorizontalAlignment إلى Center و VerticalAlignment إلى Top .

{{% /alert %}}

تظهر مقتطفات الشيفرة التالية كيفية إضافة صورة في رأس ملف PDF باستخدام C#.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddImageHeader()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ImageinHeader.pdf"))
    {
        // Create header as an ImageStamp
        var imageStamp = new Aspose.Pdf.ImageStamp(dataDir + "aspose-logo.jpg")
        {
            TopMargin = 10,
            HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Center,
            VerticalAlignment = Aspose.Pdf.VerticalAlignment.Top
        };

        // Add image header on all pages
        foreach (var page in document.Pages)
        {
            page.AddStamp(imageStamp);
        }

        // Save PDF document
        document.Save(dataDir + "ImageinHeader_out.pdf");
    }
}
```

## إضافة صورة في تذييل ملف PDF

يمكنك استخدام فئة Image Stamp لإضافة صورة في تذييل ملف PDF. توفر فئة Image Stamp الخصائص اللازمة لإنشاء ختم قائم على الصورة مثل حجم الخط، نمط الخط، ولون الخط، إلخ. لإضافة صورة في التذييل، تحتاج إلى إنشاء كائن Document وكائن Image Stamp باستخدام الخصائص المطلوبة. بعد ذلك، يمكنك استدعاء طريقة AddStamp من الصفحة لإضافة الصورة في تذييل PDF.

{{% alert color="primary" %}}

تحتاج إلى تعيين خاصية [BottomMargin](https://reference.aspose.com/pdf/ar/net/aspose.pdf/stamp/properties/bottommargin) بطريقة تضبط الصورة في منطقة التذييل من PDF الخاص بك. تحتاج أيضًا إلى تعيين [HorizontalAlignment](https://reference.aspose.com/pdf/ar/net/aspose.pdf/stamp/properties/horizontalalignment) إلى `Center` و [VerticalAlignment](https://reference.aspose.com/pdf/ar/net/aspose.pdf/stamp/properties/verticalalignment) إلى `Bottom`.

{{% /alert %}}

تظهر مقتطفات الشيفرة التالية كيفية إضافة صورة في تذييل ملف PDF باستخدام C#.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddImageFooter()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ImageInFooter.pdf"))
    {
        // Create footer as an ImageStamp
        var imageStamp = new Aspose.Pdf.ImageStamp(dataDir + "aspose-logo.jpg")
        {
            BottomMargin = 10,
            HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Center,
            VerticalAlignment = Aspose.Pdf.VerticalAlignment.Bottom
        };

        // Add image footer on all pages
        foreach (var page in document.Pages)
        {
            page.AddStamp(imageStamp);
        }

        // Save PDF document
        document.Save(dataDir + "ImageInFooter_out.pdf");
    }
}
```

## إضافة رؤوس مختلفة في ملف PDF واحد

نعلم أنه يمكننا إضافة TextStamp في قسم الرأس/التذييل من المستند باستخدام خاصيتي TopMargin أو Bottom Margin، ولكن في بعض الأحيان قد نحتاج إلى إضافة رؤوس/تذييلات متعددة في مستند PDF واحد. **Aspose.PDF for .NET** يشرح كيفية القيام بذلك.

لتحقيق هذا المتطلب، سنقوم بإنشاء كائنات TextStamp فردية (عدد الكائنات يعتمد على عدد الرؤوس/التذييلات المطلوبة) وسنضيفها إلى مستند PDF. يمكننا أيضًا تحديد معلومات تنسيق مختلفة لكل كائن ختم فردي. في المثال التالي، أنشأنا كائن Document وثلاثة كائنات TextStamp ثم استخدمنا طريقة [AddStamp](https://reference.aspose.com/pdf/ar/net/aspose.pdf/page/methods/addstamp) من الصفحة لإضافة النص في قسم الرأس من PDF. تظهر مقتطفات الشيفرة التالية كيفية إضافة صورة في تذييل ملف PDF باستخدام Aspose.PDF for .NET.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddDifferentHeaders()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "AddingDifferentHeaders.pdf"))
    {
        // Create three stamps
        var stamp1 = new Aspose.Pdf.TextStamp("Header 1");
        var stamp2 = new Aspose.Pdf.TextStamp("Header 2");
        var stamp3 = new Aspose.Pdf.TextStamp("Header 3");

        // Set stamp1 properties (Header 1)
        stamp1.VerticalAlignment = Aspose.Pdf.VerticalAlignment.Top;
        stamp1.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Center;
        stamp1.TextState.FontStyle = Aspose.Pdf.Text.FontStyles.Bold;
        stamp1.TextState.ForegroundColor = Aspose.Pdf.Color.Red;
        stamp1.TextState.FontSize = 14;

        // Set stamp2 properties (Header 2)
        stamp2.VerticalAlignment = Aspose.Pdf.VerticalAlignment.Top;
        stamp2.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Center;
        stamp2.Zoom = 10;

        // Set stamp3 properties (Header 3)
        stamp3.VerticalAlignment = Aspose.Pdf.VerticalAlignment.Top;
        stamp3.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Center;
        stamp3.RotateAngle = 35;
        stamp3.TextState.BackgroundColor = Aspose.Pdf.Color.Pink;
        stamp3.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("Verdana");

        // Add the stamps to specific pages
        document.Pages[1].AddStamp(stamp1);
        document.Pages[2].AddStamp(stamp2);
        document.Pages[3].AddStamp(stamp3);

        // Save PDF document
        document.Save(dataDir + "MultiHeader_out.pdf");
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