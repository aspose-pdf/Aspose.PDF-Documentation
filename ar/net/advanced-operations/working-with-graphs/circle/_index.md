---
title: إضافة كائن دائرة إلى ملف PDF
linktitle: إضافة دائرة
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /ar/net/add-circle/
description: يشرح هذا المقال كيفية إنشاء كائن دائرة في ملف PDF باستخدام Aspose.PDF for .NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Add Circle Object to PDF file",
    "alternativeHeadline": "Add Interactive Circle Objects in PDFs with Ease",
    "abstract": "تتيح الوظيفة الجديدة في Aspose.PDF for .NET للمستخدمين إنشاء كائنات دائرة داخل ملفات PDF بسهولة. تعزز هذه الميزة تصور البيانات من خلال تمكين إضافة الرسوم البيانية الدائرية العادية والمملوءة، مما يوفر للمطورين طريقة بديهية لتمثيل المعلومات رسوميًا في مستنداتهم.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Add Circle Object, Circle in PDF, Aspose.PDF for .NET, PDF document generation, Create filled Circle, Graph object, PDF file manipulation, C# PDF library",
    "wordcount": "441",
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
    "url": "/net/add-circle/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-circle/"
    },
    "dateModified": "2024-11-25",
    "description": "يشرح هذا المقال كيفية إنشاء كائن دائرة في ملف PDF باستخدام Aspose.PDF for .NET."
}
</script>

تعمل مقتطفات الشيفرة التالية أيضًا مع مكتبة [Aspose.PDF.Drawing](/pdf/net/drawing/) .

## إضافة كائن دائرة

مثل الرسوم البيانية الشريطية، يمكن استخدام الرسوم البيانية الدائرية لعرض البيانات في عدد من الفئات المنفصلة. ومع ذلك، على عكس الرسوم البيانية الشريطية، يمكن استخدام الرسوم البيانية الدائرية فقط عندما يكون لديك بيانات لجميع الفئات التي تشكل الكل. لذا دعونا نلقي نظرة على إضافة كائن [دائرة](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/circle) باستخدام Aspose.PDF for .NET.

اتبع الخطوات أدناه:

1. إنشاء مثيل [مستند](https://reference.aspose.com/pdf/net/aspose.pdf/document) .
1. إنشاء [كائن رسم](https://reference.aspose.com/pdf/net/aspose.pdf.drawing) بأبعاد معينة.
1. تعيين [حدود](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/graph/properties/border) لكائن الرسم.
1. إضافة كائن [رسم](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/graph) إلى مجموعة الفقرات في الصفحة.
1. حفظ ملف PDF الخاص بنا.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void Circle()
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

        // Create a circle with the specified coordinates and radius
        var circle = new Aspose.Pdf.Drawing.Circle(100, 100, 40);

        // Set the circle's color
        circle.GraphInfo.Color = Aspose.Pdf.Color.GreenYellow;

        // Add the circle to the graph shapes
        graph.Shapes.Add(circle);

        // Add Graph object to paragraphs collection of page
        page.Paragraphs.Add(graph);

        // Save PDF document
        document.Save(dataDir + "DrawingCircle1_out.pdf");
    }
}
```

ستبدو دائرتنا المرسومة كما يلي:

![رسم دائرة](drawing_circle.png)

## إنشاء كائن دائرة مملوءة

تظهر هذه المثال كيفية إضافة كائن دائرة مملوءة باللون.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CircleFilled()
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

        // Create a filled circle
        var circle = new Aspose.Pdf.Drawing.Circle(100, 100, 40)
        {
            GraphInfo = 
            { 
                Color = Aspose.Pdf.Color.GreenYellow, 
                FillColor = Aspose.Pdf.Color.Green 
            },
            Text = new Aspose.Pdf.Text.TextFragment("Circle")
        };

        // Add the circle to the graph shapes
        graph.Shapes.Add(circle);

        // Add Graph object to paragraphs collection of page
        page.Paragraphs.Add(graph);

        // Save PDF document
        document.Save(dataDir + "DrawingCircle2_out.pdf");
    }
}
```

دعونا نرى نتيجة إضافة دائرة مملوءة:

![دائرة مملوءة](filled_circle.png)

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