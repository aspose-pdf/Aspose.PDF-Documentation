---
title: تحويل XML إلى تنسيق FDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /ar/net/converting-an-xml-to-fdf-format/
description: يشرح هذا القسم كيفية تحويل XML إلى تنسيق FDF باستخدام FormDataConverter.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Converting an XML to FDF format",
    "alternativeHeadline": "Convert XML Files to FDF Format Easily",
    "abstract": "تتيح هذه الميزة للمطورين تحويل ملفات XML إلى تنسيق FDF بسلاسة باستخدام فئة FormDataConverter في Aspose.PDF for .NET. تعزز هذه الوظيفة تبادل البيانات بين تنسيقات الوثائق، مما يسهل إدارة بيانات النماذج بكفاءة في التطبيقات",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "274",
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
    "url": "/net/converting-an-xml-to-fdf-format/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/converting-an-xml-to-fdf-format/"
    },
    "dateModified": "2024-11-25",
    "description": "يمكن لـ Aspose.PDF أداء المهام البسيطة والسلسة ولكن أيضًا التعامل مع الأهداف الأكثر تعقيدًا. تحقق من القسم التالي للمستخدمين المتقدمين والمطورين."
}
</script>

{{% alert color="primary" %}}

تدعم مساحة [Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) في [Aspose.PDF for .NET](/pdf/net/) النماذج بشكل جيد. كما أنها تدعم استيراد وتصدير بيانات النماذج إلى تنسيقات ملفات مختلفة مثل FDF و XFDF و XML. ومع ذلك، يحتاج المطور أحيانًا إلى تحويل تنسيق إلى آخر. في هذه المقالة، سننظر في الميزة التي تتيح لنا تحويل تنسيق FDF إلى XML.

{{% /alert %}}

## تفاصيل التنفيذ

FDF هو اختصار لتنسيق بيانات النماذج، وملف FDF يحتوي على قيم النموذج في زوج مفتاح/قيمة. نعلم أيضًا أن ملف XML يحتوي على القيم كعلامات. حيث يتم تمثيل المفتاح غالبًا باسم العلامة ويتم تمثيل القيمة كالقيمة داخل تلك العلامة. الآن، توفر [Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) المرونة لتحويل تنسيق ملف XML إلى تنسيق FDF.

استخدم فئة [FormDataConverter](https://reference.aspose.com/pdf/net/aspose.pdf.facades/FormDataConverter) لهذا الغرض. توفر هذه الفئة طرقًا مختلفة لتحويل تنسيق بيانات إلى آخر. توضح هذه المقالة كيفية استخدام إحدى الطرق، ConvertXmlToFdf(..)، التي تأخذ ملف FDF كمدخل أو تدفق مصدر وتقوم بحفظه في تنسيق XML. يوضح مقتطف الشيفرة التالي كيفية تحويل ملف FDF إلى ملف XML.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
private static void ConvertXmlToFdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_TechnicalArticles();

    using (var src = new FileStream(dataDir + "log.xml", FileMode.Open, FileAccess.Read))
    {
        using (var dest = new FileStream(dataDir + "XMLToPdf_out.pdf", FileMode.Create, FileAccess.ReadWrite))
        {
            FormDataConverter.ConvertXmlToFdf(src, dest);
        }
    }
}
```