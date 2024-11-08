---
title: Aspose.PDF DOM API 的基础
linktitle: DOM API 的基础
type: docs
weight: 110
url: /zh/java/basics-of-dom-api/
description: Aspose.PDF for Java 也使用 DOM 的概念来表示 PDF 文档的对象结构。在这里，您可以阅读这种结构的描述。
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## DOM API 简介

文档对象模型 (DOM) 是一种将结构化文档表示为面向对象模型的形式。DOM 是万维网联盟 (W3C) 的官方标准，用于以平台和语言中立的方式表示结构化文档。

简单来说，DOM 是代表某个文档结构的对象树。
 Aspose.PDF for Java 也使用 DOM 的概念来表示 PDF 文档的结构对象。然而，DOM 的各个方面（如其元素）是在所用编程语言的语法中进行操作的。DOM 的公共接口在其应用程序编程接口（API）中指定。

### PDF 文档简介

可移植文档格式 (PDF) 是一种用于文档交换的开放标准。PDF 文档是文本和二进制数据的组合。如果在文本编辑器中打开它，您将看到定义文档结构和内容的原始对象。

PDF 文件的逻辑结构是分层的，并确定查看应用程序绘制文档页面及其内容的顺序。PDF 由四个组件组成：对象、文件结构、文档结构和内容流。

### PDF 文档结构

由于 PDF 文件的结构是分层的，Aspose.PDF for Java 也以相同的方式访问元素。 以下层次结构展示了PDF文档的逻辑结构以及Aspose.PDF for Java DOM API如何构建它。

![PDF文档结构](../images/structure.png)

### 访问PDF文档元素

Document对象位于对象模型的根级别。Aspose.PDF for Java DOM API允许您创建一个Document对象，然后访问层次结构中的所有其他对象。您可以访问任何集合，如Pages或单个元素如Page等。DOM API提供单一的入口和出口点来操作PDF文档，如下所示：

- 打开PDF文档
- 以DOM风格访问PDF文档结构
- 更新PDF文档中的数据
- 验证PDF文档
- 将PDF文档导出为不同格式
- 最后，保存更新后的PDF文档

## 如何使用新的Aspose.PDF for Java API

本主题将解释新的Aspose.PDF for Java API，并指导您快速轻松地开始。 请注意，有关使用特定功能的详细信息不属于本文的一部分。

Aspose.PDF for Java由两部分组成：

- Aspose.PDF for Java DOM API
- Aspose.PDF.Facades

您将在下文中找到每个领域的详细信息。

### Aspose.PDF for Java DOM API

新的Aspose.PDF for Java DOM API对应于PDF文档结构，这有助于您不仅在文件和文档级别上工作，还在对象级别上处理PDF文档。我们为开发人员提供了更多的灵活性来访问PDF文档的所有元素和对象。使用Aspose.PDF DOM API的类，您可以以编程方式访问文档元素和格式。这个新的DOM API由各种命名空间组成，如下所示：

### com.aspose.pdf

这个命名空间提供了Document类，允许您打开和保存PDF文档。 The License 类也是此命名空间的一部分。它还提供与 PDF 页面、附件和书签相关的类，如 com.aspose.pdf.Page、com.aspose.pdf.PageCollection、com.aspose.pdf.FileSpecification、com.aspose.pdf.EmbeddedFileCollection、com.aspose.pdf.OutlineItemCollection 和 com.aspose.pdf.OutlineCollection 等。

#### com.aspose.pdf.text

此命名空间提供帮助您处理文本及其各个方面的类，例如 com.aspose.pdf.Font、com.aspose.pdf.FontCollection、com.aspose.pdf.FontRepository、com.aspose.pdf.FontStyles、com.aspose.pdf.TextAbsorber、com.aspose.pdf.TextFragment、com.aspose.pdf.TextFragmentAbsorber、com.aspose.pdf.TextFragmentCollection、com.aspose.pdf.TextFragmentState、com.aspose.pdf.TextSegment 和 com.aspose.pdf.TextSegmentCollection 等。

#### com.aspose.pdf.TextOptions

此命名空间提供允许您设置不同选项以搜索、编辑或替换文本的类，例如 com.aspose.pdf.TextEditOptions、com.aspose.pdf.TextReplaceOptions 和 com.aspose.pdf.TextSearchOptions。
#### com.aspose.pdf.PdfAction

此命名空间包含帮助您处理PDF文档的交互功能的类，例如处理文档和其他操作。此命名空间包含的类如 com.aspose.pdf.GoToAction、com.aspose.pdf.GoToRemoteAction 和 com.aspose.pdf.GoToURIAction 等。

#### com.aspose.pdf.Annotation

注释是PDF文档交互功能的一部分。我们专门为注释提供了一个命名空间。此命名空间包含帮助您处理注释的类，例如 com.aspose.pdf.Annotation、com.aspose.pdf.AnnotationCollection、com.aspose.pdf.CircleAnnotation 和 com.aspose.pdf.LinkAnnotation 等。

#### com.aspose.pdf.Form

此命名空间包含帮助您处理PDF表单和表单字段的类，例如 com.aspose.pdf.Form、com.aspose.pdf.Field、com.aspose.pdf.TextBoxField 和 com.aspose.pdf.OptionCollection 等。

#### com.aspose.pdf.devices

我们可以对PDF文档执行各种操作，例如将PDF文档转换为各种图像格式。
 然而，这些操作不属于 Document 对象，我们不能为这些操作扩展 Document 类。这就是为什么我们在新的 DOM API 中引入了 Device 的概念。

##### com.aspose.pdf.facades

在 Aspose.PDF for Java 之前，你需要 Aspose.PDF.Kit for Java 来操作现有的 PDF 文件。要执行旧的 Aspose.PDF.Kit 代码，可以使用 com.aspose.pdf.facades 命名空间。