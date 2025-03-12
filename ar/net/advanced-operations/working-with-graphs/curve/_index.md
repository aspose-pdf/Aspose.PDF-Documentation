---
title: إضافة كائن منحنى إلى ملف PDF
linktitle: إضافة منحنى
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 30
url: /ar/net/add-curve/
description: يشرح هذا المقال كيفية إنشاء كائن منحنى في ملف PDF باستخدام Aspose.PDF for .NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Add Curve Object to PDF file",
    "alternativeHeadline": "Create Curves in PDFs",
    "abstract": "تتيح الميزة الجديدة في Aspose.PDF for .NET للمطورين إنشاء والتلاعب بكائنات المنحنى داخل مستندات PDF، باستخدام منحنيات بيزير للحصول على رسومات سلسة. تسهل هذه الإضافة تصميم منحنيات بسيطة ومملوءة، مما يوفر أداة قوية لإنشاء تمثيلات بصرية معقدة في ملفات PDF مع الحفاظ على التحكم في الأبعاد والتصميم.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Add Curve, Curve object, Bezier curves, Aspose.PDF for .NET, PDF document generation, Drawing object, Filled Curve, Graph object, PDF manipulation, ASP.NET PDF",
    "wordcount": "500",
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
    "url": "/net/add-curve/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-curve/"
    },
    "dateModified": "2024-11-25",
    "description": "يشرح هذا المقال كيفية إنشاء كائن منحنى في ملف PDF باستخدام Aspose.PDF for .NET."
}
</script>

تعمل مقتطفات الشيفرة التالية أيضًا مع مكتبة [Aspose.PDF.Drawing](/pdf/ar/net/drawing/) .

## إضافة كائن منحنى

المنحنى [Curve](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/curve) هو اتحاد متصل من الخطوط الإسقاطية، حيث يلتقي كل خط بثلاثة خطوط أخرى في نقاط مزدوجة عادية.

يوضح Aspose.PDF for .NET كيفية استخدام منحنيات بيزير في الرسوم البيانية الخاصة بك.
تستخدم منحنيات بيزير على نطاق واسع في الرسوميات الحاسوبية لنمذجة المنحنيات السلسة. يتم احتواء المنحنى بالكامل في الغلاف المحدب لنقاط التحكم الخاصة به، ويمكن عرض النقاط رسوميًا واستخدامها للتلاعب بالمنحنى بشكل بديهي.
يتم احتواء المنحنى بالكامل في الرباعي الذي تكون زواياه هي النقاط الأربعة المعطاة (غلافها المحدب).

في هذا المقال، سنستكشف منحنيات الرسوم البيانية البسيطة، والمنحنيات المملوءة، التي يمكنك إنشاؤها في مستند PDF الخاص بك.

اتبع الخطوات أدناه:

1. إنشاء مثيل [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) .
1. إنشاء [كائن رسم](https://reference.aspose.com/pdf/net/aspose.pdf.drawing) بأبعاد معينة.
1. تعيين [حدود](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/graph/properties/border) لكائن الرسم.
1. إضافة [كائن رسم بياني](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/graph) إلى مجموعة الفقرات في الصفحة.
1. حفظ ملف PDF الخاص بنا.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExampleCurve()
{
    // The path to the document directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();

        // Create Drawing object with certain dimensions
        var graph = new Aspose.Pdf.Drawing.Graph(400, 200);

        // Set border for Drawing object
        var borderInfo = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, Aspose.Pdf.Color.Green);
        graph.Border = borderInfo;

        // Create a curve and set its properties
        var curve1 = new Aspose.Pdf.Drawing.Curve(new float[] { 10, 10, 50, 60, 70, 10, 100, 120 })
        {
            GraphInfo = 
            { 
                Color = Aspose.Pdf.Color.GreenYellow 
            }
        };

        // Add the curve to the graph shapes
        graph.Shapes.Add(curve1);

        // Add Graph object to paragraphs collection of page
        page.Paragraphs.Add(graph);

        // Save PDF document
        document.Save(dataDir + "DrawingCurve1_out.pdf");
    }
}

```

تظهر الصورة التالية النتيجة الناتجة عن تنفيذ مقتطف الشيفرة الخاص بنا:

![رسم منحنى](drawing_curve.png)

## إنشاء كائن منحنى مملوء

يوضح هذا المثال كيفية إضافة كائن منحنى مملوء باللون.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CurveFilled()
{
    // The path to the document directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();

        // Create Drawing object with certain dimensions
        var graph = new Aspose.Pdf.Drawing.Graph(400, 200);

        // Set border for Drawing object
        var borderInfo = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, Aspose.Pdf.Color.Green);
        graph.Border = borderInfo;

        // Create a curve and set fill color
        var curve1 = new Aspose.Pdf.Drawing.Curve(new float[] { 10, 10, 50, 60, 70, 10, 100, 120 })
        {
            GraphInfo = 
            { 
                FillColor = Aspose.Pdf.Color.GreenYellow 
            }
        };

        // Add the curve to the graph shapes
        graph.Shapes.Add(curve1);

        // Add Graph object to paragraphs collection of page
        page.Paragraphs.Add(graph);

        // Save PDF document
        document.Save(dataDir + "DrawingCurve2_out.pdf");
    }
}
```

انظر إلى نتيجة إضافة منحنى مملوء:

![منحنى مملوء](filled_curve.png)

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