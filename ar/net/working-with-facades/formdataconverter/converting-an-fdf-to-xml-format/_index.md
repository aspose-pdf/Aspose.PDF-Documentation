---
title: تحويل FDF إلى تنسيق XML
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /ar/net/converting-an-fdf-to-xml-format/
description: يشرح هذا القسم كيفية تحويل FDF إلى تنسيق XML باستخدام فئة FormDataConverter.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Converting an FDF to XML format",
    "alternativeHeadline": "Convert FDF Files to XML Easily",
    "abstract": "اكتشف كيفية تحويل ملفات FDF بكفاءة إلى تنسيق XML باستخدام فئة FormDataConverter في Aspose.PDF for .NET. تعمل هذه الوظيفة على تبسيط معالجة البيانات من خلال تحويل أزواج المفتاح/القيمة من FDF إلى هيكل XML سهل القراءة، مما يعزز التوافق وإدارة البيانات في تطبيقاتك.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "288",
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
    "url": "/net/converting-an-fdf-to-xml-format/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/converting-an-fdf-to-xml-format/"
    },
    "dateModified": "2024-11-25",
    "description": "يمكن لـ Aspose.PDF أداء المهام البسيطة والسريعة وكذلك التعامل مع الأهداف الأكثر تعقيدًا. تحقق من القسم التالي للمستخدمين المتقدمين والمطورين."
}
</script>

{{% alert color="primary" %}}

تدعم مساحة [Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) في [Aspose.PDF for .NET](/pdf/net/) نماذج AcroForms بشكل جيد. كما أنها تدعم استيراد وتصدير بيانات النماذج إلى تنسيقات ملفات مختلفة مثل FDF و XFDF و XML. ومع ذلك، قد يحتاج المطورون أحيانًا إلى تحويل تنسيق إلى آخر. تتناول هذه المقالة الميزة التي تحول FDF إلى XML.

{{% /alert %}}

## تفاصيل التنفيذ

FDF تعني تنسيق بيانات النماذج، وملف FDF يحتوي على قيم النموذج في زوج مفتاح/قيمة. نحن نعلم أيضًا أن ملف XML يحتوي على القيم كعلامات. حيث يتم تمثيل المفتاح غالبًا كاسم العلامة ويتم تمثيل القيمة كالقيمة داخل تلك العلامة. الآن، توفر لنا [Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) المرونة لتحويل تنسيق ملف FDF إلى تنسيق XML.

يمكننا استخدام فئة [FormDataConverter](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formdataconverter) لهذا الغرض. توفر لنا هذه الفئة طرقًا مختلفة لتحويل تنسيق بيانات إلى آخر. في هذه المقالة، سنستخدم فقط طريقة واحدة تسمى [ConvertFdfToXml](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formdataconverter/methods/convertfdftoxml). تأخذ هذه الطريقة ملف FDF كمدخل أو تدفق مصدر وتقوم بحفظه في تنسيق XML.

تظهر الشيفرة البرمجية التالية كيفية تحويل ملف FDF إلى ملف XML:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
private static void ConvertFdftoXml()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_TechnicalArticles();

    // Create a file stream for FDF file - input file
    using (var fdfInputStream = new FileStream(dataDir + "input.fdf", FileMode.Open))
    {
        // Create a file stream for XML file - output file
        using (var xmlOutputStream = new FileStream(dataDir + "ConvertFdfToXML_out.xml", FileMode.Create))
        {
            FormDataConverter.ConvertFdfToXml(fdfInputStream, xmlOutputStream);
        }
    }
}
```