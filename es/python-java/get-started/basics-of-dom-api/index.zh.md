---
title: Aspose.PDF DOM API 的基础
linktitle: DOM API 的基础
type: docs
weight: 110
url: /es/python-java/basics-of-dom-api/
description: Aspose.PDF for Java 也使用 DOM 的概念来表示 PDF 文档的结构。在这里，您可以阅读此结构的描述。
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## DOM API 简介

文档对象模型 (DOM) 是一种将结构化文档表示为面向对象模型的形式。DOM 是万维网联盟 (W3C) 官方标准，用于以平台和语言中立的方式表示结构化文档。

简单来说，DOM 是一个对象树，它表示某个文档的结构。
 Aspose.PDF for Java 也使用 DOM 的概念来表示 PDF 文档的结构。DOM 的各个方面（例如其元素）在所使用的编程语言的语法中进行操作。DOM 的公共接口在其应用程序编程接口（API）中指定。

### PDF 文档简介

可移植文档格式（PDF）是一种用于文档交换的开放标准。 PDF 文档是文本和二进制数据的组合。如果您在文本编辑器中打开它，您将看到定义文档结构和内容的原始对象。

PDF 文件的逻辑结构是分层的，并决定了查看应用程序绘制文档页面及其内容的顺序。PDF 由四个组件组成：对象、文件结构、文档结构和内容流。

### PDF 文档结构

由于 PDF 文件的结构是分层的，Aspose.PDF for Java 也以相同的方式访问元素。 以下层次结构向您展示了 PDF 文档的逻辑结构以及 Aspose.PDF for Java DOM API 如何构建它。

![PDF 文档结构](../images/structure.png)

### 访问 PDF 文档元素

Document 对象位于对象模型的根级别。Aspose.PDF for Java DOM API 允许您创建 Document 对象，然后访问层次结构中的所有其他对象。您可以访问诸如 Pages 之类的集合或诸如 Page 之类的单个元素。DOM API 提供了单一的入口和出口点来操作 PDF 文档，如下所示：

- 打开 PDF 文档
- 以 DOM 风格访问 PDF 文档结构
- 更新 PDF 文档中的数据
- 验证 PDF 文档
- 将 PDF 文档导出为不同格式
- 最后，保存更新后的 PDF 文档

## 如何使用新的 Aspose.PDF for Java API

本主题将解释新的 Aspose.PDF for Java API，并指导您快速轻松地入门。 请注意，有关使用特定功能的详细信息不属于本文的一部分。

Aspose.PDF for Java 由两个部分组成：

- Aspose.PDF for Java DOM API
- Aspose.PDF.Facades

您可以在下面找到这些领域的详细信息。

### Aspose.PDF for Java DOM API

新的 Aspose.PDF for Java DOM API 对应于 PDF 文档结构，这有助于您不仅在文件和文档级别上，还在对象级别上处理 PDF 文档。我们为开发人员提供了更多的灵活性，以访问 PDF 文档的所有元素和对象。使用 Aspose.PDF DOM API 的类，您可以以编程方式访问文档元素和格式。这个新的 DOM API 由以下各种命名空间组成：

### com.aspose.pdf

此命名空间提供 Document 类，允许您打开和保存 PDF 文档。 The License 类也是该命名空间的一部分。它还提供与 PDF 页面、附件和书签相关的类，如 com.aspose.pdf.Page、com.aspose.pdf.PageCollection、com.aspose.pdf.FileSpecification、com.aspose.pdf.EmbeddedFileCollection、com.aspose.pdf.OutlineItemCollection 和 com.aspose.pdf.OutlineCollection 等。

#### com.aspose.pdf.text

该命名空间提供的类帮助您处理文本及其各个方面，例如 com.aspose.pdf.Font、com.aspose.pdf.FontCollection、com.aspose.pdf.FontRepository、com.aspose.pdf.FontStyles、com.aspose.pdf.TextAbsorber、com.aspose.pdf.TextFragment、com.aspose.pdf.TextFragmentAbsorber、com.aspose.pdf.TextFragmentCollection、com.aspose.pdf.TextFragmentState、com.aspose.pdf.TextSegment 和 com.aspose.pdf.TextSegmentCollection 等。

#### com.aspose.pdf.TextOptions

该命名空间提供的类允许您设置用于搜索、编辑或替换文本的不同选项，例如 com.aspose.pdf.TextEditOptions、com.aspose.pdf.TextReplaceOptions 和 com.aspose.pdf.TextSearchOptions。
#### com.aspose.pdf.PdfAction

此命名空间包含帮助您处理PDF文档交互功能的类，例如处理文档和其他操作。此命名空间包含的类如com.aspose.pdf.GoToAction, com.aspose.pdf.GoToRemoteAction和com.aspose.pdf.GoToURIAction等。

#### com.aspose.pdf.Annotation

注释是PDF文档交互功能的一部分。我们为注释专门提供了一个命名空间。此命名空间包含帮助您处理注释的类，例如com.aspose.pdf.Annotation, com.aspose.pdf.AnnotationCollection, com.aspose.pdf.CircleAnnotation和com.aspose.pdf.LinkAnnotation等。

#### com.aspose.pdf.Form

此命名空间包含帮助您处理PDF表单和表单字段的类，例如com.aspose.pdf.Form, com.aspose.pdf.Field, com.aspose.pdf.TextBoxField和com.aspose.pdf.OptionCollection等。

#### com.aspose.pdf.devices

我们可以对PDF文档执行各种操作，例如将PDF文档转换为各种图像格式。
 However, such operations do not belong to the Document object and we cannot extend the Document class for such operations. That's why we have introduced the concept of the Device in the new DOM API.

##### com.aspose.pdf.facades

在以前的 Aspose.PDF for Java 中，你需要 Aspose.PDF.Kit for Java 来操作现有的 PDF 文件。要执行旧的 Aspose.PDF.Kit 代码，可以使用 com.aspose.pdf.facades 命名空间。