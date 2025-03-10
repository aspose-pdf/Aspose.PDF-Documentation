---
title: Aspose.PDF DOM API 基础
linktitle: DOM API 基础
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 130
url: /zh/net/basics-of-dom-api/
description: Aspose.PDF for .NET 还使用 DOM 的概念来表示 PDF 文档的结构。
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Basics of Aspose.PDF DOM API",
    "alternativeHeadline": "Enhanced PDF Manipulation with Aspose.PDF DOM API in C#",
    "abstract": "新的 Aspose.PDF for .NET DOM API 提供了一种强大的面向对象的方法来操作 PDF 文档，通过将其结构表示为层次树。这一特性使开发人员能够轻松访问、更新和导出 PDF 元素，同时通过直观的编程接口增强文档操作的灵活性和控制力。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "891",
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
    "url": "/net/basics-of-dom-api/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/basics-of-dom-api/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF 不仅可以执行简单和容易的任务，还可以应对更复杂的目标。请查看下一部分以获取高级用户和开发人员的信息。"
}
</script>

## DOM API 介绍

文档对象模型（DOM）是一种将结构化文档表示为面向对象模型的形式。DOM 是万维网联盟（W3C）官方标准，用于以平台和语言中立的方式表示结构化文档。

简单来说，DOM 是一个对象树，表示某些文档的结构。Aspose.PDF for .NET 也使用 DOM 的概念来表示 PDF 文档的结构。然而，DOM 的各个方面（例如其元素）是在所使用的编程语言的语法中进行操作的。DOM 的公共接口在其应用程序编程接口（API）中进行了规定。

### PDF 文档介绍

可移植文档格式（PDF）是文档交换的开放标准。PDF 文档是文本和二进制数据的组合。如果您在文本编辑器中打开它，您将看到定义文档结构和内容的原始对象。

PDF 文件的逻辑结构是层次性的，并决定了查看应用程序绘制文档页面及其内容的顺序。PDF 由四个组件组成：对象、文件结构、文档结构和内容流。

### PDF 文档结构

由于 PDF 文件的结构是层次性的，Aspose.PDF for .NET 也以相同的方式访问元素。以下层次结构向您展示了 PDF 文档的逻辑结构以及 Aspose.PDF for .NET DOM API 如何构建它。

![PDF 文档结构](../images/structure.png)

### 访问 PDF 文档元素

文档对象位于对象模型的根级别。Aspose.PDF for .NET DOM API 允许您创建一个文档对象，然后访问层次结构中的所有其他对象。您可以访问页面等集合或单个元素。DOM API 提供了单一的入口和出口点来操作 PDF 文档，如下所示：

- 打开 PDF 文档。
- 以 DOM 风格访问 PDF 文档结构。
- 更新 PDF 文档中的数据。
- 验证 PDF 文档。
- 将 PDF 文档导出为不同格式。
- 最后，保存更新后的 PDF 文档。

## 如何使用新的 Aspose.PDF for .NET API

本主题将解释新的 Aspose.PDF for .NET API，并指导您快速轻松地入门。请注意，关于特定功能使用的详细信息不在本文的范围内。

Aspose.PDF for .NET 由两部分组成：

- Aspose.PDF for .NET DOM API。
- Aspose.Pdf.Facades（旧的 Aspose.PDF.Kit for .NET）。

您将在下面找到每个领域的详细信息。

### Aspose.PDF for .NET DOM API

Aspose.PDF for .NET DOM API 对应于 PDF 文档结构，帮助您不仅在文件和文档级别上处理 PDF 文档，还在对象级别上处理。我们为开发人员提供了更多的灵活性，以访问 PDF 文档的所有元素和对象。使用 Aspose.PDF DOM API 的类，您可以以编程方式访问文档元素和格式。这个新的 DOM API 由以下各个命名空间组成：

### Aspose.PDF

此命名空间提供 Document 类，允许您打开和保存 PDF 文档。License 类也是此命名空间的一部分。它还提供与 PDF 页面、附件和书签相关的类，如 Page、PageCollection、FileSpecification、EmbeddedFileCollection、OutlineItemCollection 和 OutlineCollection 等。

#### Aspose.Text

此命名空间提供帮助您处理文本及其各个方面的类，例如 Font、FontCollection、FontRepository、FontStyles、TextAbsorber、TextFragment、TextFragmentAbsorber、TextFragmentCollection、TextFragmentState、TextSegment 和 TextSegmentCollection 等。

#### Aspose.Text.TextOptions

此命名空间提供允许您设置搜索、编辑或替换文本的不同选项的类，例如 TextEditOptions、TextReplaceOptions 和 TextSearchOptions。

#### Aspose.InteractiveFeatures

此命名空间包含帮助您处理 PDF 文档交互功能的类，例如处理文档和其他操作。此命名空间包含类，如 GoToAction、GoToRemoteAction 和 GoToURIAction 等。

#### Aspose.InteractiveFeatures.Annotations

注释是 PDF 文档交互功能的一部分。我们为注释专门设置了一个命名空间。此命名空间包含帮助您处理注释的类，例如 Annotation、AnnotationCollection、CircleAnnotation 和 LinkAnnotation 等。

#### Aspose.InteractiveFeatures.Forms

此命名空间包含帮助您处理 PDF 表单和表单字段的类，例如 Form、Field、TextBoxField 和 OptionCollection 等。

#### Aspose.Pdf.Devices

我们可以对 PDF 文档执行各种操作，例如将 PDF 文档转换为各种图像格式。然而，这些操作不属于 Document 对象，我们无法扩展 Document 类以进行此类操作。因此，我们在新的 DOM API 中引入了设备的概念。

#### Aspose.Pdf.Facades

在 Aspose.PDF for .NET 之前，您需要 Aspose.PDF.Kit for .NET 来操作现有的 PDF 文件。要执行旧的 Aspose.PDF.Kit 代码，可以使用 Aspose.PDF.Facades 命名空间。