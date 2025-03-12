---
title: إضافة كائن مستطيل إلى ملف PDF
linktitle: إضافة مستطيل
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 50
url: /ar/net/add-rectangle/
description: يشرح هذا المقال كيفية إنشاء كائن مستطيل في ملف PDF باستخدام Aspose.PDF for .NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Add Rectangle Object to PDF file",
    "alternativeHeadline": "Add Rectangle to PDF file",
    "abstract": "تتيح الميزة الجديدة في Aspose.PDF for .NET للمستخدمين إضافة كائنات مستطيلة بسلاسة إلى مستندات PDF. تشمل هذه الوظيفة خيارات لتخصيص المستطيلات بألوان صلبة، وتدرجات لونية، وشفافية، مما يوفر تخصيصًا بصريًا محسّنًا وتحكمًا في ترتيب الطبقات لمحتوى PDF.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Add Rectangle, PDF document generation, Aspose.PDF for .NET, Rectangle object, fill rectangle, gradient color fill, Z-Order control, alpha channel color, graph objects in PDF, create filled rectangle",
    "wordcount": "1263",
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
    "url": "/net/add-rectangle/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-rectangle/"
    },
    "dateModified": "2024-11-25",
    "description": "يشرح هذا المقال كيفية إنشاء كائن مستطيل في ملف PDF باستخدام Aspose.PDF for .NET."
}
</script>

تعمل مقتطفات الكود التالية أيضًا مع مكتبة [Aspose.PDF.Drawing](/pdf/ar/net/drawing/) .

## إضافة كائن مستطيل

يدعم Aspose.PDF for .NET ميزة إضافة كائنات الرسم (مثل الرسم، الخط، المستطيل، إلخ) إلى مستندات PDF. يمكنك أيضًا الاستفادة من إضافة كائن [Rectangle](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/rectangle) حيث تقدم أيضًا ميزة ملء كائن المستطيل بلون معين، والتحكم في ترتيب Z، وإضافة ملء تدرج لوني، وما إلى ذلك.

أولاً، دعنا نلقي نظرة على إمكانية إنشاء كائن مستطيل.

اتبع الخطوات أدناه:

1. إنشاء مستند PDF جديد [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).
1. إضافة [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) إلى مجموعة الصفحات في ملف PDF.
1. إضافة [Text fragment](https://reference.aspose.com/pdf/net/aspose.pdf/texfragment) إلى مجموعة الفقرات في مثيل الصفحة.
1. إنشاء مثيل [Graph](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/graph) .
1. تعيين الحدود لكائن [Drawing object](https://reference.aspose.com/pdf/net/aspose.pdf.drawing) .
1. إنشاء مثيل مستطيل.

1. إضافة كائن [Rectangle](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/rectangle) إلى مجموعة الأشكال في كائن Graph.
1. إضافة كائن الرسم إلى مجموعة الفقرات في مثيل الصفحة.
1. إضافة [Text fragment](https://reference.aspose.com/pdf/net/aspose.pdf/texfragment) إلى مجموعة الفقرات في مثيل الصفحة.

1. وحفظ ملف PDF الخاص بك.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddRectangle(Aspose.Pdf.Page page, float x, float y, float width, float height, Aspose.Pdf.Color color, int zIndex)
{
    // Create a Graph object with dimensions matching the specified rectangle
    var graph = new Aspose.Pdf.Drawing.Graph(width, height)
    {
        // Prevent the graph from repositioning automatically
        IsChangePosition = false,
        // Set the Left coordinate position for the Graph instance
        Left = x,
        // Set the Top coordinate position for the Graph instance
        Top = y
    };

    // Create a Rectangle object inside the Graph
    var rect = new Aspose.Pdf.Drawing.Rectangle(0, 0, width, height)
    {
        // Set the fill color of the rectangle
        GraphInfo =
        {
            FillColor = color,
            // Set the border color of the rectangle
            Color = color
        }
    };

    // Add the rectangle to the Shapes collection of the Graph
    graph.Shapes.Add(rect);

    // Set the Z-Index for the Graph object to control layering
    graph.ZIndex = zIndex;

    // Add the Graph object to the Paragraphs collection of the page
    page.Paragraphs.Add(graph);
}
```

![إنشاء مستطيل](create_rectangle.png)

## إنشاء كائن مستطيل مملوء

يقدم Aspose.PDF for .NET أيضًا ميزة ملء كائن المستطيل بلون معين.

تظهر مقتطفات الكود التالية كيفية إضافة كائن [Rectangle](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/rectangle) مملوء بلون.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void RectangleFilled()
{
    // The path to the documents directory directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();

        // Create Graph instance
        var graph = new Aspose.Pdf.Drawing.Graph(100, 400);

        // Add graph object to paragraphs collection of page instance
        page.Paragraphs.Add(graph);

        // Create Rectangle instance with specified dimensions
        var rect = new Aspose.Pdf.Drawing.Rectangle(100, 100, 200, 120)
        {
            // Specify fill color for the Rectangle object
            GraphInfo = 
            { 
                FillColor = Aspose.Pdf.Color.Red 
            }
        };

        // Add rectangle object to shapes collection of Graph object
        graph.Shapes.Add(rect);

        // Save PDF document
        document.Save(dataDir + "CreateFilledRectangle_out.pdf");
    }
}
```

انظر إلى نتيجة المستطيل المملوء بلون صلب:

![مستطيل مملوء](fill_rectangle.png)

## إضافة رسم مع ملء تدرج

يدعم Aspose.PDF for .NET ميزة إضافة كائنات الرسم إلى مستندات PDF وأحيانًا يتطلب ملء كائنات الرسم بتدرج لوني. لملء كائنات الرسم بتدرج لوني، نحتاج إلى تعيين setPatterColorSpace مع كائن gradientAxialShading كما يلي.

تظهر مقتطفات الكود التالية كيفية إضافة كائن [Rectangle](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/rectangle) مملوء بتدرج لوني.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CreateFilledRectangleGradientFill()
{
    // The path to the documents directory directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();

        // Create Graph instance
        var graph = new Aspose.Pdf.Drawing.Graph(400, 400);

        // Add graph object to paragraphs collection of page instance
        page.Paragraphs.Add(graph);

        // Create Rectangle instance
        var rect = new Aspose.Pdf.Drawing.Rectangle(0, 0, 300, 300);

        // Create a gradient fill color
        var gradientColor = new Aspose.Pdf.Color();
        var gradientSettings = new Aspose.Pdf.Drawing.GradientAxialShading(Aspose.Pdf.Color.Red, Aspose.Pdf.Color.Blue)
        {
            Start = new Aspose.Pdf.Point(0, 0),
            End = new Aspose.Pdf.Point(350, 350)
        };
        gradientColor.PatternColorSpace = gradientSettings;

        // Apply gradient fill color to the rectangle
        rect.GraphInfo.FillColor = gradientColor;

        // Add rectangle object to shapes collection of Graph object
        graph.Shapes.Add(rect);

        // Save PDF document
        document.Save(dataDir + "CreateFilledRectangleGradient_out.pdf");
    }
}
```

![مستطيل بتدرج لوني](gradient.png)

## إنشاء مستطيل مع قناة لون ألفا

يدعم Aspose.PDF for .NET ملء كائن المستطيل بلون معين. يمكن أن يحتوي كائن المستطيل أيضًا على قناة لون ألفا لإعطاء مظهر شفاف. تظهر مقتطفات الكود التالية كيفية إضافة كائن [Rectangle](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/rectangle) مع قناة لون ألفا.

يمكن أن تخزن بكسلات الصورة معلومات حول شفافيتها جنبًا إلى جنب مع قيمة اللون. وهذا يسمح بإنشاء صور تحتوي على مناطق شفافة أو شبه شفافة.

بدلاً من جعل لون شفاف، يخزن كل بكسل معلومات حول مدى تعتيمه. تُسمى هذه البيانات الشفافية قناة ألفا وعادة ما يتم تخزينها بعد قنوات لون البكسل.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void RectangleFilled_AlphaChannel()
{
    // The path to the documents directory directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();

        // Create Graph instance
        var graph = new Aspose.Pdf.Drawing.Graph(100, 400);

        // Add graph object to paragraphs collection of page instance
        page.Paragraphs.Add(graph);

        // Create first rectangle with alpha channel fill color
        var rect = new Aspose.Pdf.Drawing.Rectangle(100, 100, 200, 120)
        {
            GraphInfo = 
            { 
                FillColor = Aspose.Pdf.Color.FromArgb(128, 244, 180, 0) 
            }
        };

        // Add the first rectangle to the shapes collection of the Graph object
        graph.Shapes.Add(rect);

        // Create second rectangle with different alpha channel fill color
        var rect1 = new Aspose.Pdf.Drawing.Rectangle(200, 150, 200, 100)
        {
            GraphInfo = 
            { 
                FillColor = Aspose.Pdf.Color.FromArgb(160, 120, 0, 120) 
            }
        };

        // Add the second rectangle to the shapes collection of the Graph object
        graph.Shapes.Add(rect1);

        // Save PDF document
        document.Save(dataDir + "CreateFilledRectangle_out.pdf");
    }
}
```

![مستطيل لون قناة ألفا](rectangle_color.png)

## التحكم في ترتيب Z للمستطيل

يدعم Aspose.PDF for .NET ميزة إضافة كائنات الرسم (مثل الرسم، الخط، المستطيل، إلخ) إلى مستندات PDF. عند إضافة أكثر من مثيل لنفس الكائن داخل ملف PDF، يمكننا التحكم في عرضها عن طريق تحديد ترتيب Z. يُستخدم ترتيب Z أيضًا عندما نحتاج إلى عرض الكائنات فوق بعضها البعض.

تظهر مقتطفات الكود التالية الخطوات اللازمة لعرض كائنات [Rectangle](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/rectangle) فوق بعضها البعض.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddRectangleZOrder()
{
    // The path to the documents directory directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();

        // Set size of PDF page
        page.SetPageSize(375, 300);

        // Set left and top margins for the page object as 0
        page.PageInfo.Margin.Left = 0;
        page.PageInfo.Margin.Top = 0;

        // Create rectangles with different colors and Z-Order values
        AddRectangle(page, 50, 40, 60, 40, Aspose.Pdf.Color.Red, 2);
        AddRectangle(page, 20, 20, 30, 30, Aspose.Pdf.Color.Blue, 1);
        AddRectangle(page, 40, 40, 60, 30, Aspose.Pdf.Color.Green, 0);

        // Save PDF document
        document.Save(dataDir + "ControlRectangleZOrder_out.pdf");
    }
}
```

![التحكم في ترتيب Z](control.png)

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