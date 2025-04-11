---
title: 添加多行水印
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /zh/net/adding-multi-line-watermark-to-existing-pdf/
description: 本节解释如何使用 FormattedText 类向现有 PDF 添加多行水印。
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Adding multi line watermark",
    "alternativeHeadline": "Enhance PDFs with Multi-Line Watermarks Easily",
    "abstract": "介绍使用 Aspose.Pdf.Facades 命名空间向现有 PDF 添加多行水印的能力。此新功能简化了该过程，使用户能够轻松将多行文本纳入其文档中，使用在 FormattedText 类中新实现的 AddNewLineText() 方法。轻松用自定义的多行水印增强您的 PDF 演示文稿",
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
    "description": "Aspose.PDF 不仅可以执行简单和容易的任务，还可以应对更复杂的目标。请查看下一节以获取高级用户和开发人员的信息。"
}
</script>

{{% alert color="primary" %}}

许多用户希望在其 PDF 文档上盖上多行文本。他们通常尝试使用 `\n` 和 `<br>`，但这些类型的字符不被 Aspose.Pdf.Facades 命名空间支持。因此，为了使其成为可能，我们在 Aspose.Pdf.Facades 命名空间的 [FormattedText](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades/formattedtext) 类中添加了另一个名为 [AddNewLineText()](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades/formattedtext/methods/addnewlinetext/index) 的方法。

{{% /alert %}}

## 实现细节

请参考以下代码块以在现有 PDF 中添加多行水印。

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