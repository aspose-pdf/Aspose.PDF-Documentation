---
title: تحقق من حدود الشكل في مجموعة الأشكال
type: docs
weight: 70
url: /ar/net/aspose-pdf-drawing-graph-shapes-bounds-check/
description: تعرف على كيفية التحقق من حدود الشكل عند إدخاله في مجموعة الأشكال لضمان ملاءمته داخل الحاوية الأم.
lastmod: "2025-02-28"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Checking Element Bounds in Shapes Collection",
    "alternativeHeadline": "Configurable Bounds Checking for Aspose.PDF Shapes with Exception Mode",
    "abstract": "تتميز ميزة التحقق من الحدود الجديدة في `Drawing.Graph.Shapes` بالتحقق تلقائيًا من أبعاد العناصر مقابل الحاويات الأم، مما يمنع تجاوز التخطيط. يتم تشغيل الاستثناءات عندما تتجاوز العناصر حدود الحاوية، مما يفرض قيودًا صارمة على الحجم أثناء الإدراج لضمان تنسيق PDF دقيق وتبسيط دقة التصميم.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "751",
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
    "url": "/net/aspose-pdf-drawing-graph-shapes-bounds-check/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/aspose-pdf-drawing-graph-shapes-bounds-check/"
    },
    "dateModified": "2025-03-17",
    "description": ""
}
</script>

## المقدمة
يوفر هذا المستند دليلًا مفصلًا حول استخدام ميزة التحقق من الحدود في مجموعة الأشكال. تضمن هذه الميزة أن العناصر تناسب داخل الحاوية الأم ويمكن تكوينها لرمي استثناء إذا لم يتناسب المكون. سنستعرض الخطوات لتنفيذ هذه الوظيفة ونقدم مثالًا كاملاً.

## المتطلبات الأساسية
ستحتاج إلى ما يلي:
* Visual Studio 2019 أو أحدث
* Aspose.PDF for .NET 25.3 أو أحدث
* ملف PDF عينة يحتوي على بعض الصفحات

يمكنك تنزيل مكتبة Aspose.PDF for .NET من الموقع الرسمي أو تثبيتها باستخدام مدير حزم NuGet في Visual Studio.

## الخطوات
إليك الخطوات لإكمال المهمة:
1. إنشاء مستند جديد وإضافة صفحة.
2. إنشاء كائن `Graph` بأبعاد محددة.
3. إنشاء كائن `Shape` بأبعاد محددة.
4. تعيين `BoundsCheckMode` إلى `ThrowExceptionIfDoesNotFit`.
5. محاولة إضافة الشكل إلى الرسم البياني.

دعنا نرى كيفية تنفيذ هذه الخطوات في كود C#.

### الخطوة 1: إنشاء مستند جديد وإضافة صفحة
أولاً، قم بإنشاء مستند PDF جديد وأضف صفحة إليه.

```csharp
using (var doc = new Aspose.Pdf.Document())
{
    Aspose.Pdf.Page page = doc.Pages.Add();
}
```

### الخطوة 2: إنشاء كائن Graph بأبعاد محددة
بعد ذلك، قم بإنشاء كائن `Graph` بعرض وارتفاع 100 وحدة. ضع الرسم البياني على بعد 10 وحدات من الأعلى و15 وحدة من اليسار من الصفحة. أضف حدودًا سوداء للرسم البياني.

```csharp
var graph = new Aspose.Pdf.Drawing.Graph(100d, 100d)
{
    Top = 10,
    Left = 15,
    Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.Box, 1F, Aspose.Pdf.Color.Black)
};
page.Paragraphs.Add(graph);
```

### الخطوة 3: إنشاء كائن Shape (على سبيل المثال، مستطيل) بأبعاد محددة
قم بإنشاء كائن مستطيل بعرض وارتفاع 50 وحدة. ضع المستطيل في (-1، 0)، وهو خارج حدود الرسم البياني.

```csharp
var rect = new Aspose.Pdf.Drawing.Rectangle(-1, 0, 50, 50)
{
    GraphInfo =
    {
        FillColor = Aspose.Pdf.Color.Tomato
    }
};
```

### الخطوة 4: تعيين BoundsCheckMode إلى ThrowExceptionIfDoesNotFit
قم بتعيين `BoundsCheckMode` إلى `ThrowExceptionIfDoesNotFit` لضمان أنه يتم رمي استثناء إذا لم يتناسب المستطيل داخل الرسم البياني.

```csharp
graph.Shapes.UpdateBoundsCheckMode(Aspose.Pdf.BoundsCheckMode.ThrowExceptionIfDoesNotFit);
```

### الخطوة 5: محاولة إضافة المستطيل إلى الرسم البياني
حاول إضافة المستطيل إلى الرسم البياني. سيؤدي ذلك إلى رمي استثناء `Aspose.Pdf.BoundsOutOfRangeException` لأن المستطيل لا يتناسب مع أبعاد الرسم البياني.

```csharp
graph.Shapes.Add(rect);
```

## المخرجات
بعد تنفيذ الكود، ستكون المخرجات المتوقعة هي استثناء `Aspose.Pdf.BoundsOutOfRangeException` مع الرسالة:

```
Bounds not fit. Container dimensions: 100x100
```

## استكشاف الأخطاء وإصلاحها
في حالة حدوث مشكلات، إليك بعض النصائح:
* تأكد من تعيين `BoundsCheckMode` بشكل صحيح.
* تحقق من أن أبعاد العنصر والحاوية دقيقة.
* تحقق من موضع العنصر داخل الحاوية.

## مثال كامل
فيما يلي مثال كامل يوضح جميع الخطوات مجتمعة:

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CheckShapeBounds()
{
    // Create a new document and add a page
    using (var doc = new Aspose.Pdf.Document())
    {
        var page = doc.Pages.Add();
        
        // Create a Graph Object with Specified Dimensions
        var graph = new Aspose.Pdf.Drawing.Graph(100d, 100d)
        {
            Top = 10,
            Left = 15,
            Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.Box, 1F, Aspose.Pdf.Color.Black)
        };
        page.Paragraphs.Add(graph);
        
        // Create a Shape object (for example, Rectangle) with specified dimensions
        var rect = new Aspose.Pdf.Drawing.Rectangle(-1, 0, 50, 50)
        {
            GraphInfo =
            {
                FillColor = Aspose.Pdf.Color.Tomato
            }
        };
        
        // Set the BoundsCheckMode to ThrowExceptionIfDoesNotFit
        graph.Shapes.UpdateBoundsCheckMode(Aspose.Pdf.BoundsCheckMode.ThrowExceptionIfDoesNotFit);
        
        // Attempt to add the rectangle to the graph
        graph.Shapes.Add(rect);
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CheckShapeBounds()
{
    // Create a new document and add a page
    using var doc = new Aspose.Pdf.Document();
    var page = doc.Pages.Add();

    // Create a Graph Object with Specified Dimensions
    var graph = new Aspose.Pdf.Drawing.Graph(100d, 100d)
    {
        Top = 10,
        Left = 15,
        Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.Box, 1F, Aspose.Pdf.Color.Black)
    };
    page.Paragraphs.Add(graph);

    // Create a Aspose.Pdf.Drawing.Shape object (for example, Aspose.Pdf.Drawing.Rectangle) with specified dimensions
    var rect = new Aspose.Pdf.Drawing.Rectangle(-1, 0, 50, 50)
    {
        GraphInfo =
        {
            FillColor = Aspose.Pdf.Color.Tomato
        }
    };

    // Set the BoundsCheckMode to ThrowExceptionIfDoesNotFit
    graph.Shapes.UpdateBoundsCheckMode(Aspose.Pdf.BoundsCheckMode.ThrowExceptionIfDoesNotFit);

    // Attempt to add the rectangle to the graph
    graph.Shapes.Add(rect);
}
```
{{< /tab >}}
{{< /tabs >}}

## الخاتمة
تعد ميزة التحقق من الحدود في مجموعة الأشكال أداة قوية لضمان تناسب العناصر داخل الحاويات الأم. يمكنك منع مشكلات التخطيط في مستندات PDF الخاصة بك عن طريق تعيين BoundsCheckMode إلى ThrowExceptionIfDoesNotFit. هذه الميزة مفيدة بشكل خاص في السيناريوهات التي يكون فيها تحديد موضع العناصر وحجمها بدقة أمرًا حاسمًا. لمزيد من التفاصيل، قم بزيارة [الوثائق الرسمية](https://docs.aspose.com/pdf/net/).