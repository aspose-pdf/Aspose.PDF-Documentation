---
title: Aspose.PDF DOM API 基础
linktitle: DOM API 基础
type: docs
weight: 10
url: /zh/androidjava/basics-of-dom-api/
description: Aspose.PDF for Android via Java 也使用 DOM 的概念以对象的形式表示 PDF 文档的结构。在此您可以阅读该结构的描述。
lastmod: "2026-07-01"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## DOM API 介绍

文档对象模型（DOM）是一种以面向对象模型表示结构化文档的形式。DOM 是世界万维网联盟（W3C）官方的用于以平台和语言无关方式表示结构化文档的标准。

简单来说，DOM 是一个对象树，用来表示某些文档的结构。Aspose.PDF for Android via Java 也使用 DOM 的概念以对象的形式表示 PDF 文档的结构。然而，DOM 的各个方面（例如其 Elements）在所使用的编程语言语法中进行操作。DOM 的公共接口在其应用程序编程接口（API）中定义。

### PDF 文档介绍

便携式文档格式（PDF）是一种用于文档交换的开放标准。PDF 文档由文本和二进制数据组合而成。如果在文本编辑器中打开它，您将看到定义文档结构和内容的原始对象。

PDF 文件的逻辑结构是层次化的，决定了查看应用程序绘制文档页面及其内容的顺序。PDF 由四个组件组成：对象、文件结构、文档结构和内容流。

### PDF 文档结构

由于 PDF 文件的结构是层次化的，Aspose.PDF for Java 也以相同的方式访问这些元素。以下层次结构展示了 PDF 文档的逻辑结构以及 Aspose.PDF for Java DOM API 如何构建它。

![PDF 文档结构](https://docs.aspose.com/pdf/java/images/structure.png)

### 访问 PDF 文档元素

Document 对象位于对象模型的根级别。Aspose.PDF for Android via Java DOM API 允许您创建一个 Document 对象，然后访问层次结构中的所有其他对象。您可以访问诸如 Pages 之类的集合或单个元素如 Page 等。DOM API 提供单一的入口和退出点来操作 PDF 文档，如下所示：

- 打开 PDF 文档
- 以 DOM 方式访问 PDF 文档结构
- 更新 PDF 文档中的数据
- 验证 PDF 文档
- 将 PDF 文档导出为不同格式
- 最后，保存更新后的 PDF 文档

## 如何使用全新的 Aspose.PDF for Android via Java API

本主题将解释全新的 Aspose.PDF for Android via Java API，并指导您快速轻松入门。请注意，关于特定功能使用的详细信息不在本文范围内。

Aspose.PDF for Android via Java 由两部分组成：

- Aspose.PDF for Android via Java DOM API
- Aspose.PDF.Facades 

您将在下方找到每个领域的详细信息。

### Aspose.PDF for Android via Java DOM API

全新的 Aspose.PDF for Android via Java DOM API 对应于 PDF 文档结构，这帮助您不仅在文件和文档层面上，而且在对象层面上处理 PDF 文档。我们为开发者提供了更大的灵活性，以访问 PDF 文档的所有元素和对象。使用 Aspose.PDF DOM API 的类，您可以以编程方式访问文档元素和格式化。这个新的 DOM API 由以下各命名空间组成：

### com.aspose.pdf

此命名空间提供 Document 类，允许您打开和保存 PDF 文档。License 类也是此命名空间的一部分。它还提供与 PDF 页面、附件和书签相关的类，如 com.aspose.pdf.Page、com.aspose.pdf.PageCollection、com.aspose.pdf.FileSpecification、com.aspose.pdf.EmbeddedFileCollection、com.aspose.pdf.OutlineItemCollection 和 com.aspose.pdf.OutlineCollection 等。

#### com.aspose.pdf.text

此命名空间提供帮助您处理文本及其各个方面的类，例如 com.aspose.pdf.Font、com.aspose.pdf.FontCollection、com.aspose.pdf.FontRepository、com.aspose.pdf.FontStyles、com.aspose.pdf.TextAbsorber、com.aspose.pdf.TextFragment、com.aspose.pdf.TextFragmentAbsorber、com.aspose.pdf.TextFragmentCollection、com.aspose.pdf.TextFragmentState、com.aspose.pdf.TextSegment 和 com.aspose.pdf.TextSegmentCollection 等。

#### com.aspose.pdf.TextOptions

此命名空间提供允许您设置搜索、编辑或替换文本的不同选项的类，例如 com.aspose.pdf.TextEditOptions、com.aspose.pdf.TextReplaceOptions 和 com.aspose.pdf.TextSearchOptions。

#### com.aspose.pdf.PdfAction

此命名空间包含帮助您使用 PDF 文档交互功能的类，例如处理文档及其他操作。此命名空间包含如 com.aspose.pdf.GoToAction、com.aspose.pdf.GoToRemoteAction 和 com.aspose.pdf.GoToURIAction 等类。

#### com.aspose.pdf.Annotation

Annotations 是 PDF 文档交互功能的一部分。我们专门为注释制定了一个命名空间。该命名空间包含帮助您使用注释的类，例如 com.aspose.pdf.Annotation、com.aspose.pdf.AnnotationCollection、com.aspose.pdf.CircleAnnotation 和 com.aspose.pdf.LinkAnnotation 等。

#### com.aspose.pdf.Form

该命名空间包含帮助您使用 PDF 表单和表单字段的类，例如 com.aspose.pdf.Form、com.aspose.pdf.Field、com.aspose.pdf.TextBoxField 和 com.aspose.pdf.OptionCollection 等。

#### com.aspose.pdf.devices 

我们可以对 PDF 文档执行各种操作，例如将 PDF 文档转换为多种图像格式。但是，这类操作不属于 Document 对象，且我们无法为这些操作扩展 Document 类。这就是我们在新的 DOM API 中引入 Device 概念的原因。

##### com.aspose.pdf.facades

在 Aspose.PDF for Java 之前，你需要使用 Aspose.PDF.Kit for Java 来操作现有的 PDF 文件。要执行旧的 Aspose.PDF.Kit 代码，可以使用 com.aspose.pdf.facades 命名空间。

