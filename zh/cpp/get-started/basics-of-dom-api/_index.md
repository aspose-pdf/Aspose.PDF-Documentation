---
title: Aspose.PDF DOM API 基础
linktitle: DOM API 基础
type: docs
weight: 120
url: zh/cpp/basics-of-dom-api/
description: Aspose.PDF for C++ 也使用 DOM 的概念来表示 PDF 文档的结构。您可以在此处阅读该结构的描述。
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## DOM API 简介

文档对象模型 (DOM) 是一种将结构化文档表示为面向对象模型的形式。DOM 是万维网联盟 (W3C) 的官方标准，用于以平台和语言中立的方式表示结构化文档。

简单来说，DOM 是一个对象树，表示某个文档的结构。 Aspose.PDF for C++ 也使用 DOM 的概念来表示 PDF 文档的结构。DOM 的各个方面（例如其元素）在所使用的编程语言的语法中进行操作。DOM 的公共接口在其应用程序编程接口（API）中指定。

### PDF 文档简介

便携式文档格式（PDF）是一种用于文档交换的开放标准。PDF 文档是文本和二进制数据的组合。如果您在文本编辑器中打开它，您将看到定义文档结构和内容的原始对象。

PDF 文件的逻辑结构是分层的，并确定查看应用程序绘制文档页面及其内容的顺序。PDF 由四个组件组成：对象、文件结构、文档结构和内容流。

### PDF 文档结构

由于 PDF 文件的结构是分层的，Aspose.PDF for C++ 也以相同的方式访问这些元素。 以下层次结构显示了PDF文档的逻辑结构以及Aspose.PDF for C++ DOM API如何构建它。

![PDF Document Structure](../images/structure.png)

### 访问PDF文档元素

Document对象位于对象模型的根级别。Aspose.PDF for C++ DOM API允许您创建一个Document对象，然后访问层次结构中的所有其他对象。您可以访问任何集合，例如Pages或单个元素，例如Page等。DOM API提供了单一的入口和出口点来操作PDF文档，如下所示：

- 打开PDF文档
- 以DOM风格访问PDF文档结构
- 更新PDF文档中的数据
- 验证PDF文档
- 将PDF文档导出为不同格式
- 最后，保存更新后的PDF文档

## 如何使用新的Aspose.PDF for C++ API

本主题将解释新的Aspose.PDF for C++ API，并指导您快速轻松地入门。 请注意，有关特定功能使用的详细信息不属于本文的一部分。

Aspose.PDF for C++ 由两个部分组成：

- Aspose.PDF for C++ DOM API
- Aspose.PDF.Facades

您将在下面找到这些领域的详细信息。

### Aspose.PDF for C++ DOM API

Aspose.PDF for C++ DOM API 对应于 PDF 文档结构，它帮助您不仅在文件和文档级别，而且在对象级别处理 PDF 文档。我们为开发人员提供了更大的灵活性，以访问 PDF 文档的所有元素和对象。使用 Aspose.PDF DOM API 的类，您可以以编程方式访问文档元素和格式。这个新的 DOM API 由各种命名空间组成，如下所示：

### Aspose::Pdf 命名空间参考

此命名空间提供 Document 类，使您可以打开和保存 PDF 文档。

#### Aspose::Pdf::Text 命名空间参考

此命名空间提供类，帮助您处理文本及其各个方面，例如 Font、FontCollection、FontRepository、FontSource、TextAbsorber、TextFragment、TextFragmentAbsorber、TextFragmentCollection、TextFragmentState、TextSegment 和 TextSegmentCollection 等。
#### Aspose::Pdf::Collections Namespace Reference

此命名空间提供类 AsposeHashDictionary。

#### Aspose::Pdf::CommonData Namespace Reference

#### Aspose::Pdf::Diagnostics Namespace Reference

#### Aspose::Pdf::Drawing Namespace Reference

此命名空间提供类：Curve, Circle, Arc, Rectangle, Graph 等，用于向 PDF 文件添加图形元素。

#### Aspose::Pdf::Engine Namespace Reference

此命名空间提供 Addressing, Interactive, Security, CommonData, IO, Presentation 类。

#### Aspose::Pdf::GroupProcessor Namespace Reference

此命名空间提供类：ExtractorFactory - 代表用于创建 IPdfTypeExtractor 对象的工厂，IDocumentPageTextExtractor, IDocumentTextExtractor, IPdfTypeExtractor 类 - 代表与提取器交互的接口。

#### Aspose::Pdf::Interchange Namespace Reference

#### Aspose::Pdf::LogicalStructure Namespace Reference

此命名空间提供类：AnnotationElement, AttributeOwnerStandard, CaptionElement, DocumentElement, FormElement, GroupingElement, ILSTextElement, PrivateElement, WarichuWTElement 等。

#### Aspose::Pdf::Operators Namespace Reference

此命名空间提供以下操作符的类：BasicSetColorAndPatternOperator、BlockTextOperator、SetCharWidthBoundingBox、SetColorStroke、SetHorizontalTextScaling、SetTextRenderingMode、TextShowOperator 等。

#### Aspose::Pdf::Optimization Namespace Reference

此命名空间提供两个类 - ImageCompressionOptions 和 OptimizationOptions。

#### Aspose::Pdf::PageModel Namespace Reference

#### Aspose::Pdf::PdfAOptionClasses Namespace Reference

此命名空间提供两个类：FontEmbeddingOptions - PDF/A 标准要求，所有字体必须嵌入到文档中。该类包括在目标电脑上缺少某些字体时无法嵌入的情况标志。ToUnicodeProcessingRules - 此类描述了解决 Adobe Preflight 错误“文本无法映射到 Unicode”的规则。

#### Aspose::Pdf::Sanitization Namespace Reference

此命名空间提供两个类：Details_SanitizationException 和 IRecovery。

#### Aspose::Pdf::Tagged Namespace Reference

此命名空间提供类 Details_TaggedException - 表示文档的TaggedPDF内容的异常。ITaggedContent - 表示用于处理文档的TaggedPdf内容的接口？和TaggedPdfExceptionCode。

#### Aspose::Pdf::Validation Namespace Reference

#### Aspose::Pdf::XfaConverter Namespace Reference

此命名空间提供类 XfaParserOptions - 处理相关数据封装的类。

#### Aspose::Pdf::Annotations Namespace Reference

注释是PDF文档交互功能的一部分。我们为注释专门设立了一个命名空间。此命名空间包含帮助您处理注释的类，例如Annotation, AnnotationCollection, CircleAnnotation 和 LinkAnnotation等。

#### Aspose::Pdf::Forms Namespace Reference

此命名空间包含帮助您处理PDF表单和表单字段的类，例如Form, Field, TextBoxField 和 OptionCollection等。

#### Aspose::Pdf::Devices Namespace Reference

We can perform various operations on the PDF documents such as converting PDF document to various image formats. However, such operations do not belong to the Document object and we cannot extend the Document class for such operations. That's why we have introduced the concept of the Device in the new DOM API.

我们可以对 PDF 文档执行各种操作，例如将 PDF 文档转换为各种图像格式。然而，此类操作不属于 Document 对象，我们无法为此类操作扩展 Document 类。这就是为什么我们在新的 DOM API 中引入了 Device 的概念。

##### Aspose::Pdf::Facades Namespace Reference

##### Aspose::Pdf::Facades 命名空间参考

You can use Aspose.PDF.Facades namespace. This Namespace provides classes AutoFiller - represents a class to receive data from database or other datasource. Bookmark, Form, Stamp, PdfConverter anr more classes.

您可以使用 Aspose.PDF.Facades 命名空间。这个命名空间提供了类 AutoFiller - 表示一个从数据库或其他数据源接收数据的类。还有 Bookmark、Form、Stamp、PdfConverter 等多个类。