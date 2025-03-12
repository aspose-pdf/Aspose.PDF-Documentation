---
title: 使用 OneClick PDF 文档生成器
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /zh/net/using-oneclick-pdf-document-generator/
description: 了解如何在 Microsoft Dynamics 中使用 Aspose.PDF OneClick PDF 文档生成器
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.5
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Using OneClick PDF Document Generator",
    "alternativeHeadline": "Streamlined PDF Generation in Microsoft Dynamics",
    "abstract": "通过 Aspose.PDF OneClick PDF 文档生成器解锁 Microsoft Dynamics 中无缝的文档生成。此创新功能允许用户直接在 CRM 中创建可自定义的 PDF 模板，单击一下即可高效生成文档，并轻松将 OneClick 按钮集成到表单中以实现简化访问。利用此强大工具增强您的数据管理能力，提高生产力。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "313",
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
    "url": "/net/using-oneclick-pdf-document-generator/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/using-oneclick-pdf-document-generator/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF 不仅可以执行简单和容易的任务，还可以应对更复杂的目标。请查看下一部分以获取高级用户和开发人员的信息。"
}
</script>

## 创建模板并添加到 CRM

- 打开 Word 并创建一个模板。
- 插入来自 CRM 的数据的 MailMerge 字段。

![插入 MailMerge 字段](using-oneclick-pdf-document-generator_1.png)

- 确保字段名称与 CRM 字段完全匹配。
- 模板是特定于单个实体使用的。

![演示模板](using-oneclick-pdf-document-generator_2.png)

- 创建模板后，在 CRM 中打开 OneClick PDF 配置实体并创建新记录。
- 输入模板名称，选择模板定义的实体，并将创建的文档附加到附件中。

![选择模板](using-oneclick-pdf-document-generator_3.png)

## 从功能区按钮生成文档

- 打开要生成文档的记录。（确保该实体的配置中已附加模板）
- 从功能区点击 OneClick PDF 按钮。

![点击 OneClick PDF](using-oneclick-pdf-document-generator_4.png)

- 在弹出窗口中：选择模板、文件名和操作，然后点击生成。
- 根据选择检查下载的文件或备注。

## 配置 OneClick 按钮并使用它们

- 为了直接从表单使用 OneClick 按钮，打开表单自定义。
- 在要添加 OneClick 按钮的位置插入 WebResource。
- 在 WebResource 中选择 OpenButtonPage 并给它一个名称。
- 在数据字段中配置按钮，使用以下示例。

![WebResource 属性](using-oneclick-pdf-document-generator_5.png)

- 每个按钮使用单独的行，并使用以下语法：
  - 语法：模板名称 |<Action: Download/Note>|输出文件名
  - 示例：Demo|Download|我的下载文件
- 保存并发布自定义。
- 按钮在表单上可用。

![按钮在表单上可用](using-oneclick-pdf-document-generator_6.png)