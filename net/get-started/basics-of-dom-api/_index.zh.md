---
title: Aspose.PDF DOM API 基础
linktitle: DOM API 基础
type: docs
weight: 140
url: /net/basics-of-dom-api/
description: Aspose.PDF for .NET 也使用 DOM 的概念来表示 PDF 文档的结构。
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## DOM API 简介

文档对象模型（DOM）是一种以对象导向模型表示结构化文档的形式。DOM 是官方的万维网联盟（W3C）标准，用于以平台和语言中立的方式表示结构化文档。

简单来说，DOM 是一个对象树，代表某个文档的结构。
简而言之，DOM 是一种对象树，代表某个文档的结构。

### PDF 文档简介

可移植文档格式（PDF）是文档交换的开放标准。PDF 文档是文本和二进制数据的组合。如果您在文本编辑器中打开它，您将看到定义文档结构和内容的原始对象。

PDF 文件的逻辑结构是层次性的，决定了查看应用程序绘制文档页面及其内容的顺序。PDF 由四个组成部分构成：对象、文件结构、文档结构和内容流。

### PDF 文档结构

由于 PDF 文件的结构是层次性的，Aspose.PDF for .NET 也以相同的方式访问元素。以下层次结构向您展示了 PDF 文档的逻辑结构以及 Aspose.PDF for .NET DOM API 是如何构建它的。

![PDF 文档结构](../images/structure.png)

### 访问 PDF 文档元素

Document 对象位于对象模型的根级别。
文档对象位于对象模型的根级别。

- 打开 PDF 文档
- 以 DOM 风格访问 PDF 文档结构
- 更新 PDF 文档中的数据
- 验证 PDF 文档
- 将 PDF 文档导出为不同格式
- 最后，保存更新后的 PDF 文档

## 如何使用新的 Aspose.PDF for .NET API

本主题将解释新的 Aspose.PDF for .NET API 并指导您快速轻松地开始使用。请注意，关于使用特定功能的详细信息不是本文的一部分。

Aspose.PDF for .NET 由两部分组成：

- Aspose.PDF for .NET DOM API
- Aspose.PDF.Facades（旧 Aspose.PDF.Kit for .NET）
您将在下面找到每个区域的详细信息。

### Aspose.PDF for .NET DOM API

Aspose.PDF for .NET DOM API 对应于 PDF 文档结构，这有助于您不仅在文件和文档级别上，还在对象级别上处理 PDF 文档。
### Aspose.PDF

此命名空间提供了 Document 类，允许您打开和保存 PDF 文档。License 类也是这个命名空间的一部分。它还提供了与 PDF 页面、附件和书签相关的类，如 Page、PageCollection、FileSpecification、EmbeddedFileCollection、OutlineItemCollection 和 OutlineCollection 等。

#### Aspose.Text

此命名空间提供了帮助您处理文本及其各个方面的类，例如 Font、FontCollection、FontRepository、FontStyles、TextAbsorber、TextFragment、TextFragmentAbsorber、TextFragmentCollection、TextFragmentState、TextSegment 和 TextSegmentCollection 等。

#### Aspose.Text.TextOptions

此命名空间提供了允许您为搜索、编辑或替换文本设置不同选项的类，例如 TextEditOptions、TextReplaceOptions 和 TextSearchOptions。
#### Aspose.InteractiveFeatures

此命名空间包含的类可以帮助您处理PDF文档的交互功能，例如处理文档和其他操作。此命名空间包含类似GoToAction、GoToRemoteAction和GoToURIAction等类。

#### Aspose.InteractiveFeatures.Annotations

注释是PDF文档交互功能的一部分。我们为注释专门设立了一个命名空间。该命名空间包含了一些帮助您处理注释的类，例如Annotation、AnnotationCollection、CircleAnnotation和LinkAnnotation等。

#### Aspose.InteractiveFeatures.Forms

此命名空间包含的类可以帮助您处理PDF表单和表单字段，例如Form、Field、TextBoxField和OptionCollection等。

#### Aspose.PDF.Devices

我们可以对PDF文档执行各种操作，例如将PDF文档转换为各种图像格式。
我们可以对PDF文档执行各种操作，例如将PDF文档转换为各种图像格式。

##### Aspose.PDF.Facades

在Aspose.PDF for .NET之前，您需要Aspose.PDF.Kit for .NET来操作现有的PDF文件。要执行旧的Aspose.PDF.Kit代码，可以使用Aspose.PDF.Facades命名空间。
