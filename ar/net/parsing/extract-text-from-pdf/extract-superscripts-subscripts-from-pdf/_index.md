---
title: استخراج نصوص SuperScripts و SubScripts من PDF
linktitle: استخراج SuperScripts و SubScripts
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 30
url: /ar/net/extract-superscripts-subscripts-from-pdf/
description: تصف هذه المقالة طرقًا مختلفة لاستخراج نصوص SuperScripts و SubScripts من PDF باستخدام Aspose.PDF في C#.
lastmod: "2022-10-07"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Extract SuperScripts and SubScripts text from PDF",
    "alternativeHeadline": "Extract SuperScripts and SubScripts from PDF Documents",
    "abstract": "تتيح الميزة الجديدة لاستخراج نصوص SuperScripts و SubScripts من مستندات PDF باستخدام مكتبة Aspose.PDF for .NET للمستخدمين استرجاع تنسيق النص المتخصص بدقة الموجود في المستندات التقنية. تبسط هذه الإضافة عملية التعامل مع التعبيرات الرياضية والمواصفات الكيميائية من خلال تزويد المطورين بالأدوات اللازمة للتلاعب بهذه العناصر النصية بسهولة.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "323",
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
    "url": "/net/extract-superscripts-subscripts-from-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/extract-superscripts-subscripts-from-pdf/"
    },
    "dateModified": "2024-11-25",
    "description": "يمكن لـ Aspose.PDF أداء المهام البسيطة والسلسة وكذلك التعامل مع الأهداف الأكثر تعقيدًا. تحقق من القسم التالي للمستخدمين المتقدمين والمطورين."
}
</script>

## استخراج نصوص SuperScripts و SubScripts

استخراج النص من مستند PDF هو أمر شائع. ومع ذلك، في مثل هذا النص، عند استخراجه، قد لا يتم عرض **SuperScripts و SubScripts** الموجودة فيه، والتي تعتبر نموذجية للمستندات التقنية والمقالات. الـ SubScript أو SuperScript هو حرف أو رقم أو حرف موضوع أسفل أو فوق خط النص العادي. عادة ما يكون أصغر من بقية النص.

تستخدم **SubScripts و SuperScripts** غالبًا في الصيغ والتعبيرات الرياضية ومواصفات المركبات الكيميائية. من الصعب تعديلها عندما يمكن أن يكون هناك العديد منها في نفس فقرة النص.
في أحد الإصدارات الأخيرة، أضافت مكتبة **Aspose.PDF for .NET** دعمًا لاستخراج نصوص SuperScripts و SubScripts من PDF.

استخدم فئة **TextFragmentAbsorber** ويمكنك بالفعل القيام بأي شيء بالنص الموجود، أي يمكنك ببساطة استخدام النص بالكامل. جرب مقتطف الكود التالي:

مقتطف الكود التالي يعمل أيضًا مع مكتبة [Aspose.PDF.Drawing](/pdf/net/drawing/).

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractSuperScriptsAndSubScripts()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SuperScriptExample.pdf"))
    {
        // Create an absorber
        var absorber = new Aspose.Pdf.Text.TextFragmentAbsorber();
        document.Pages[1].Accept(absorber);
        using (StreamWriter writer = new StreamWriter(dataDir + "SuperScriptExample_out.txt"))
        {
            // Write the extracted text in text file
            writer.WriteLine(absorber.Text);
        }
    }
}
```

أو استخدم **TextFragments** بشكل منفصل وقم بجميع أنواع التلاعب بها، على سبيل المثال، فرزها حسب الإحداثيات أو حسب الحجم.

مقتطف الكود التالي يعمل أيضًا مع مكتبة [Aspose.PDF.Drawing](/pdf/net/drawing/).

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractSuperScriptsAndSubScriptsWithTextFragments()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SuperScriptExample.pdf"))
    {
        // Create an absorber
        var absorber = new Aspose.Pdf.Text.TextFragmentAbsorber();
        document.Pages[1].Accept(absorber);
        using (StreamWriter writer = new StreamWriter(dataDir + "SuperScriptExample_out.txt"))
        {
            foreach (var textFragment in absorber.TextFragments)
            {
                // Write the extracted text in text file
                writer.Write(textFragment.Text);
            }

        }
    }
}
```