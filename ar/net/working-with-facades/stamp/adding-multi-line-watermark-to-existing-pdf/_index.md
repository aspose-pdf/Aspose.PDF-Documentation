---
title: إضافة علامة مائية متعددة الأسطر
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /ar/net/adding-multi-line-watermark-to-existing-pdf/
description: يشرح هذا القسم كيفية إضافة علامة مائية متعددة الأسطر إلى ملف PDF موجود باستخدام فئة FormattedText.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Adding multi line watermark",
    "alternativeHeadline": "Enhance PDFs with Multi-Line Watermarks Easily",
    "abstract": "تقديم القدرة على إضافة علامات مائية متعددة الأسطر إلى ملفات PDF الموجودة باستخدام مساحة أسماء Aspose.Pdf.Facades. تسهل هذه الوظيفة الجديدة العملية، مما يسمح للمستخدمين بإدراج عدة أسطر من النص في مستنداتهم بسهولة باستخدام الطريقة الجديدة المطبقة AddNewLineText() في فئة FormattedText. عزز عروض PDF الخاصة بك بعلامات مائية متعددة الأسطر مخصصة بسهولة.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "188",
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
    "url": "/net/adding-multi-line-watermark-to-existing-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/adding-multi-line-watermark-to-existing-pdf/"
    },
    "dateModified": "2024-11-25",
    "description": "يمكن لـ Aspose.PDF أداء المهام البسيطة والسلسة وكذلك التعامل مع الأهداف الأكثر تعقيدًا. تحقق من القسم التالي للمستخدمين المتقدمين والمطورين."
}
</script>

{{% alert color="primary" %}}

يرغب الكثير من المستخدمين في ختم مستندات PDF الخاصة بهم بنص متعدد الأسطر. عادةً ما يحاولون استخدام `\n` و `<br>` ولكن هذه الأنواع من الأحرف غير مدعومة من قبل مساحة أسماء Aspose.Pdf.Facades. لذلك، لجعل ذلك ممكنًا، أضفنا طريقة أخرى تسمى [AddNewLineText()](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/formattedtext/methods/addnewlinetext/index) في فئة [FormattedText](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/formattedtext) من مساحة أسماء Aspose.Pdf.Facades.

{{% /alert %}}

## تفاصيل التنفيذ

يرجى الرجوع إلى كتلة التعليمات البرمجية التالية لإضافة علامة مائية متعددة الأسطر في ملف PDF موجود.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddTextStampToPdf()
{
    // Instantiate a stamp object
    var logoStamp = new Aspose.Pdf.Facades.Stamp();

    // Instantiate an object of FormattedText class
    var formatText = new Aspose.Pdf.Facades.FormattedText("Hello World!",
        System.Drawing.Color.FromArgb(180, 0, 0), 
        Aspose.Pdf.Facades.FontStyle.TimesItalic,
        Aspose.Pdf.Facades.EncodingType.Winansi, false, 50);

    // Add another line for Stamp
    formatText.AddNewLineText("Good Luck");
    // BindLogo to PDF
    logoStamp.BindLogo(formatText);
}
```