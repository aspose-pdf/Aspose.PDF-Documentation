---
title: العمل مع طبقات PDF باستخدام C#
linktitle: العمل مع طبقات PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 50
url: /ar/net/work-with-pdf-layers/
description: تشرح المهمة التالية كيفية قفل طبقة PDF، استخراج عناصر طبقة PDF، تسطيح PDF متعدد الطبقات، ودمج جميع الطبقات داخل PDF في واحدة.
lastmod: "2024-09-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Work with PDF layers using C#",
    "alternativeHeadline": "Manage PDF layers effortlessly with C#",
    "abstract": "اختبر إدارة مستندات PDF المحسنة مع الميزة الجديدة Aspose.PDF for .NET التي تتيح للمستخدمين العمل بفعالية مع طبقات PDF. تتيح هذه الوظيفة قفل وفتح الطبقات، استخراج العناصر إلى ملفات منفصلة، تسطيح المحتوى متعدد الطبقات، ودمج طبقات متعددة في واحدة، مما يوفر تحكمًا أكبر في رؤية المستند وتنظيمه. افتح إمكانيات مستندات PDF الخاصة بك وسهل سير العمل الخاص بك مع هذه الأدوات القوية.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "PDF layers, lock PDF layer, extract PDF layer elements, flatten layered PDF, merge PDF layers, Aspose.PDF for .NET, layer.Lock(), layer.Flatten(), layer.Save()",
    "wordcount": "501",
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
    "url": "/net/work-with-pdf-layers/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/work-with-pdf-layers/"
    },
    "dateModified": "2024-11-25",
    "description": "يمكن لـ Aspose.PDF أداء المهام البسيطة والسريعة، ولكن أيضًا التعامل مع الأهداف الأكثر تعقيدًا. تحقق من القسم التالي للمستخدمين المتقدمين والمطورين."
}
</script>

تسمح طبقات PDF لمستند PDF باحتواء مجموعات مختلفة من المحتوى يمكن عرضها أو إخفاؤها بشكل انتقائي. قد تتضمن كل طبقة في PDF نصوصًا أو صورًا أو رسومات، ويمكن للمستخدمين تبديل هذه الطبقات تشغيلًا أو إيقافًا، اعتمادًا على احتياجاتهم. غالبًا ما تستخدم الطبقات في المستندات المعقدة حيث يحتاج المحتوى المختلف إلى التنظيم أو الفصل.

## قفل طبقة PDF

مع Aspose.PDF for .NET يمكنك فتح PDF، قفل طبقة معينة في الصفحة الأولى، وحفظ المستند مع التغييرات.

منذ إصدار 24.5، تم تنفيذ هذه الميزة.

تمت إضافة طريقتين جديدتين وخصيصة واحدة:

- Layer.Lock(); - يقفل الطبقة.
- Layer.Unlock(); - يفتح الطبقة.
- Layer.Locked; - خاصية، تشير إلى حالة قفل الطبقة.

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void LockLayerInPDF()
{
	// The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Layers();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Get the first page and the first layer
        var page = document.Pages[1];
        var layer = page.Layers[0];

        // Lock the layer
        layer.Lock();

        // Save PDF document
        document.Save(dataDir + "LockLayerInPDF_out.pdf");
    }
}
```

## استخراج عناصر طبقة PDF

تسمح مكتبة Aspose.PDF for .NET باستخراج كل طبقة من الصفحة الأولى وحفظ كل طبقة في ملف منفصل.

لإنشاء PDF جديد من طبقة، يمكن استخدام مقتطف الشيفرة التالي:

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SaveLayersFromPdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Get layers from the first page
        var layers = document.Pages[1].Layers;

        // Save each layer to the output path
        foreach (var layer in layers)
        {
            layer.Save(dataDir + "Layers_out.pdf");
        }
    }
}
```

أدى إصدار 24.9 إلى تحديث لهذه الميزة.

من الممكن استخراج عناصر طبقة PDF وحفظها في تدفق ملف PDF جديد:

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SaveLayersToOutputStream(Stream outputStream)
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();
	
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Get layers from the first page
        var layers = document.Pages[1].Layers;

        // Save each layer to the output stream
        foreach (var layer in layers)
        {
            layer.Save(outputStream);
        }
    }
}
```

## تسطيح PDF متعدد الطبقات

تفتح مكتبة Aspose.PDF for .NET PDF، وتقوم بالتكرار عبر كل طبقة في الصفحة الأولى، وتسطيح كل طبقة، مما يجعلها دائمة على الصفحة.

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void FlattenLayersInPdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Get the first page
        var page = document.Pages[1];

        // Flatten each layer on the page
        foreach (var layer in page.Layers)
        {
            layer.Flatten(true);
        }
    }
}
```

تقبل طريقة 'Layer.Flatten(bool cleanupContentStream)' المعامل البولياني الذي يحدد ما إذا كان يجب إزالة علامات مجموعة المحتوى الاختيارية من تدفق المحتوى. يؤدي تعيين معامل cleanupContentStream إلى false إلى تسريع عملية التسطيح.

## دمج جميع الطبقات داخل PDF في واحدة

تسمح مكتبة Aspose.PDF for .NET بدمج جميع طبقات PDF أو طبقة معينة في الصفحة الأولى في طبقة جديدة وحفظ المستند المحدث.

تمت إضافة طريقتين لدمج جميع الطبقات في الصفحة:

- void MergeLayers(string newLayerName).
- void MergeLayers(string newLayerName, string newOptionalContentGroupId).

يسمح المعامل الثاني بإعادة تسمية علامة مجموعة المحتوى الاختيارية. القيمة الافتراضية هي "oc1" (/OC /oc1 BDC).

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MergeLayersInPdf(string newLayerName, string optionalLayerName = null)
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Get the first page
        var page = document.Pages[1];

        // Merge layers with a new layer name
        if (optionalLayerName != null)
        {
            page.MergeLayers(newLayerName, optionalLayerName);
        }
        else
        {
            page.MergeLayers(newLayerName);
        }

        // Save PDF document
        document.Save(dataDir + "MergeLayersInPdf_out.pdf");
    }
}
```