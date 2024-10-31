---
title: Aspose.PDF DOM API 基础
linktitle: DOM API 基础
type: docs
weight: 10
url: /androidjava/basics-of-dom-api/
description: Aspose.PDF for Android via Java 也使用 DOM 的概念来表示 PDF 文档的结构。这里您可以阅读对此结构的描述。
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## DOM API 简介

文档对象模型（DOM）是一种将结构化文档表示为面向对象模型的表示形式。DOM 是代表结构化文档的官方万维网联盟 (W3C) 标准，以平台和语言无关的方式。

简单来说，DOM 是一个对象树，代表某个文档的结构。
 Aspose.PDF for Android via Java 也使用 DOM 的概念来表示 PDF 文档的结构。DOM 的各个方面（例如其元素）在所使用的编程语言的语法中进行操作。DOM 的公共接口在其应用程序编程接口（API）中指定。

### PDF 文档介绍

可移植文档格式 (PDF) 是用于文档交换的开放标准。PDF 文档是文本和二进制数据的组合。如果在文本编辑器中打开它，您将看到定义文档结构和内容的原始对象。

PDF 文件的逻辑结构是分层的，并决定查看应用程序绘制文档页面及其内容的顺序。PDF 由四个组件组成：对象、文件结构、文档结构和内容流。

### PDF 文档结构

由于 PDF 文件的结构是分层的，Aspose.PDF for Java 也以相同的方式访问这些元素。 以下层次结构显示了PDF文档的逻辑结构以及Aspose.PDF for Java DOM API如何构建它。

![PDF文档结构](https://docs.aspose.com/pdf/java/images/structure.png)

### 访问PDF文档元素

Document对象位于对象模型的根级别。Aspose.PDF通过Java DOM API为Android提供了创建Document对象的功能，然后可以访问层次结构中的所有其他对象。您可以访问任何集合，如Pages或单个元素，如Page等。DOM API提供了单一的入口和出口点来操作PDF文档，如下所示：

- 打开PDF文档
- 以DOM风格访问PDF文档结构
- 更新PDF文档中的数据
- 验证PDF文档
- 将PDF文档导出为不同格式
- 最后，保存更新后的PDF文档

## 如何使用新的Aspose.PDF通过Java API为Android

本主题将解释新的Aspose.PDF通过Java API为Android，并指导您快速轻松地入门。 请注意，关于使用特定功能的详细信息不属于本文的一部分。

Aspose.PDF for Android via Java 由两部分组成：

- Aspose.PDF for Android via Java DOM API
- Aspose.PDF.Facades

你将在下面找到每个领域的详细信息。

### Aspose.PDF for Android via Java DOM API

新的 Aspose.PDF for Android via Java DOM API 对应于 PDF 文档结构，这帮助你不仅在文件和文档级别上工作，还可以在对象级别上操作 PDF 文档。我们为开发人员提供了更大的灵活性，以访问 PDF 文档的所有元素和对象。使用 Aspose.PDF DOM API 的类，你可以以编程方式访问文档元素和格式。这个新的 DOM API 由以下各种命名空间组成：

### com.aspose.pdf

这个命名空间提供了 Document 类，允许你打开和保存 PDF 文档。 The License 类也是该命名空间的一部分。它还提供了与 PDF 页面、附件和书签相关的类，例如 com.aspose.pdf.Page、com.aspose.pdf.PageCollection、com.aspose.pdf.FileSpecification、com.aspose.pdf.EmbeddedFileCollection、com.aspose.pdf.OutlineItemCollection 和 com.aspose.pdf.OutlineCollection 等。

#### com.aspose.pdf.text

此命名空间提供的类帮助您处理文本及其各个方面，例如 com.aspose.pdf.Font、com.aspose.pdf.FontCollection、com.aspose.pdf.FontRepository、com.aspose.pdf.FontStyles、com.aspose.pdf.TextAbsorber、com.aspose.pdf.TextFragment、com.aspose.pdf.TextFragmentAbsorber、com.aspose.pdf.TextFragmentCollection、com.aspose.pdf.TextFragmentState、com.aspose.pdf.TextSegment 和 com.aspose.pdf.TextSegmentCollection 等。

#### com.aspose.pdf.TextOptions

此命名空间提供的类允许您设置不同的选项以搜索、编辑或替换文本，例如 com.aspose.pdf.TextEditOptions、com.aspose.pdf.TextReplaceOptions 和 com.aspose.pdf.TextSearchOptions。
#### com.aspose.pdf.PdfAction

此命名空间包含帮助您处理PDF文档交互功能的类，例如处理文档和其他操作。此命名空间包含的类有 com.aspose.pdf.GoToAction、com.aspose.pdf.GoToRemoteAction 和 com.aspose.pdf.GoToURIAction 等。

#### com.aspose.pdf.Annotation

注释是PDF文档交互功能的一部分。我们为注释专门提供了一个命名空间。此命名空间包含帮助您处理注释的类，例如 com.aspose.pdf.Annotation、com.aspose.pdf.AnnotationCollection、com.aspose.pdf.CircleAnnotation 和 com.aspose.pdf.LinkAnnotation 等。

#### com.aspose.pdf.Form

此命名空间包含帮助您处理PDF表单和表单字段的类，例如 com.aspose.pdf.Form、com.aspose.pdf.Field、com.aspose.pdf.TextBoxField 和 com.aspose.pdf.OptionCollection 等。

#### com.aspose.pdf.devices

我们可以对PDF文档执行各种操作，例如将PDF文档转换为各种图像格式。
 然而，此类操作不属于 Document 对象，我们无法为此类操作扩展 Document 类。这就是为什么我们在新的 DOM API 中引入了 Device 概念。

##### com.aspose.pdf.facades

在 Aspose.PDF for Java 之前，你需要使用 Aspose.PDF.Kit for Java 来操作现有的 PDF 文件。要执行旧的 Aspose.PDF.Kit 代码，可以使用 com.aspose.pdf.facades 命名空间。