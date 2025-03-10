---
title: 使用 AcroForms
linktitle: AcroForms
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /zh/net/acroforms/
description: 使用 Aspose.PDF for .NET，您可以从头开始创建表单，在 PDF 文档中填写表单字段，提取表单数据等。
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Working with AcroForms",
    "alternativeHeadline": "Enhance PDF forms with flexible AcroForms functionality",
    "abstract": "Aspose.PDF for .NET 引入了增强的 AcroForms 功能，使用户能够高效地从头创建表单、填写 PDF 字段并无缝提取数据。此强大功能支持多个数据库记录的集成，允许动态表单管理和简化的用户体验",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "AcroForms, PDF forms technology, create a form, fill form fields, extract data, database records, Templates, modify AcroForms, posting AcroForm data, import and export data",
    "wordcount": "484",
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
    "url": "/net/acroforms/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/acroforms/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF 不仅可以执行简单和容易的任务，还可以应对更复杂的目标。请查看下一部分以获取高级用户和开发人员的信息。"
}
</script>

## AcroForms 基础知识

**AcroForms** 是原始的 PDF 表单技术。AcroForms 是面向页面的表单。它们首次引入于 1998 年。它们接受表单数据格式（FDF）和 XML 表单数据格式（xFDF）的输入。第三方供应商支持 AcroForms。当 Adobe 引入 AcroForms 时，他们将其称为“使用 Adobe Acrobat Pro/Standard 创建的 PDF 表单，而不是特殊类型的静态或动态 XFA 表单。AcroForms 是可移植的，并且可以在所有平台上工作。

您可以使用 AcroForms 向 PDF 表单文档添加额外页面。由于模板的概念，您可以使用 AcroForms 支持用多个数据库记录填充表单。

PDF 1.7 支持两种不同的方法来集成数据和 PDF 表单。

*AcroForms（也称为 Acrobat 表单）*，在 PDF 1.2 格式规范中引入并包含。

*Adobe XML 表单架构（XFA）表单*，在 PDF 1.5 格式规范中作为可选功能引入（XFA 规范未包含在 PDF 规范中，仅作参考）。

为了理解 **Acroforms** 与 **XFA** 表单之间的区别，我们需要先了解基础知识。首先，两者都是您可以使用的 PDF 表单。Acroforms 是较旧的，创建于 1998 年，仍被称为经典 PDF 表单。XFA 表单是您可以保存为 PDF 的网页，出现在 2003 年。PDF 开始接受 XFA 表单花了一些时间。

AcroForms 具有 XFA 中没有的功能，反之亦然，XFA 也具有 AcroForms 中没有的一些功能。例如：

- AcroForms 支持“模板”的概念，允许向 PDF 表单文档添加额外页面，以支持用多个数据库记录填充表单。
- XFA 支持文档重排的概念，允许字段在需要时调整大小以适应数据。

有关 Java 库功能的更详细学习，请参阅以下文章：

- [创建 AcroForm](/pdf/zh/net/create-form) - 使用 C# 从头创建表单。
- [填写 AcroForm](/pdf/zh/net/fill-form) - 在您的 PDF 文档中填写表单字段。
- [提取 AcroForm](/pdf/zh/net/extract-form) - 从 PDF 文档的所有或单个字段获取值。
- [修改 AcroForm](/pdf/zh/net/modifing-form) - 获取或设置 FieldLimit，设置表单字段字体等。
- [发布 AcroForm 数据](/pdf/zh/net/posting-acroform-data/) - 将表单数据导入和导出到 XML 文件。
- [导入和导出数据](/pdf/zh/net/import-and-export-data/) - 使用表单类导入和导出数据。
- [从 PDF 中删除表单](/pdf/zh/net/remove-form/) - 根据子类型/表单删除文本，删除所有表单。
- [以 JSON 导入和导出数据](/pdf/zh/net/import-export-json/) - 使用 JSON 导入和导出数据。

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