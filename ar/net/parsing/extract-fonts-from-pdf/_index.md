---
title: استخراج الخطوط من PDF C#
linktitle: استخراج الخطوط من PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 30
url: /ar/net/extract-fonts-from-pdf/
description: استخدم مكتبة Aspose.PDF لـ .NET لاستخراج جميع الخطوط المدمجة من مستند PDF الخاص بك.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Extract Fonts from PDF C#",
    "alternativeHeadline": "Effortlessly Extract All Fonts from PDF Documents",
    "abstract": "افتح قوة مستندات PDF الخاصة بك مع وظيفة مكتبة Aspose.PDF for .NET التي تتيح لك استخراج جميع الخطوط المدمجة بسهولة. باستخدام طريقة FontUtilities.GetAllFonts()، يمكن للمطورين الوصول بسهولة إلى الخطوط وإدراجها داخل أي ملف PDF، مما يعزز تحليل المستندات وقدرات التخصيص.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "156",
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
    "url": "/net/extract-fonts-from-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/extract-fonts-from-pdf/"
    },
    "dateModified": "2024-11-25",
    "description": "يمكن لمكتبة Aspose.PDF أداء المهام البسيطة والسلسة، ولكنها أيضًا قادرة على التعامل مع الأهداف الأكثر تعقيدًا. تحقق من القسم التالي للمستخدمين المتقدمين والمطورين."
}
</script>

في حال كنت ترغب في الحصول على جميع الخطوط من مستند PDF، يمكنك استخدام طريقة FontUtilities.GetAllFonts() المقدمة في فئة Document. يرجى مراجعة مقتطف الكود التالي للحصول على جميع الخطوط من مستند PDF موجود:

مقتطف الكود التالي يعمل أيضًا مع مكتبة [Aspose.PDF.Drawing](/pdf/ar/net/drawing/).

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractFonts()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ExtractFonts.pdf"))
    {
        Aspose.Pdf.Text.Font[] fonts = document.FontUtilities.GetAllFonts();
        foreach (Aspose.Pdf.Text.Font font in fonts)
        {
            Console.WriteLine(font.FontName);
        }
    }
}
```