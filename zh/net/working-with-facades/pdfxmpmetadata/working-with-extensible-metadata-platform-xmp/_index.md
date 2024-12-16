---
title: Extensible Metadata Platform - XMP
type: docs
weight: 10
url: /zh/net/working-with-extensible-metadata-platform-xmp/
description: 本节解释如何使用 PdfXmpMetadata 类处理可扩展元数据平台 - XMP。
lastmod: "2021-06-05"
draft: false
---

{{% alert color="primary" %}}

可扩展元数据平台（XMP）是由 Adobe Systems Inc. 创建的标准。此标准用于处理和存储标准化和专有的元数据。此元数据可以嵌入到不同的文件格式中，但在本文中我们将仅关注 PDF 文件格式。我们将看到如何使用 Aspose.PDF for .NET 中的 Aspose.Pdf.Facades 命名空间在 PDF 文件中嵌入元数据。我们将使用 [PdfXmpMetadata](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfxmpmetadata) 类来操作 PDF 文档中的 XMP。

{{% /alert %}}

## 背景

PDF 文件在其生命周期中经历多个阶段。 我们创建一个 PDF 文档，然后将其传递给其他人或部门进行进一步处理。然而，在此过程中，我们需要跟踪所做更改的不同方面。XMP 可以实现此目的，跟踪文件中的更改或其他信息。

## 解释

为了使用 Aspose.Pdf.Facades 操作 XMP，我们将使用 [PdfXmpMetadata](http://www.aspose.com/docs/display/pdfnet/PdfXmpMetadata+Class) 类。我们将使用此类操作预定义的元数据属性。[PdfXmpMetadata](http://www.aspose.com/docs/display/pdfnet/PdfXmpMetadata+Class) 类将这些属性添加到 PDF 文件中。它还帮助打开和保存我们添加元数据的 PDF 文件。因此，使用 [PdfXmpMetadata](http://www.aspose.com/docs/display/pdfnet/PdfXmpMetadata+Class) 类，我们可以轻松操作 PDF 文件中的 XMP。

以下代码片段将帮助您了解如何使用 [PdfXmpMetadata](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfxmpmetadata) 类处理 XMP：
{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-TechnicalArticles-ExtensibleMetadataPlatform-ExtensibleMetadataPlatform.cs" >}}

## 结论

{{% alert color="primary" %}}
在本文中，我们了解了如何使用 Aspose.Pdf.Facades 处理 XMP。本文中使用的 [PdfXmpMetadata](http://www.aspose.com/docs/display/pdfnet/PdfXmpMetadata+Class) 使用户可以非常轻松地操作 PDF 文档中的元数据。如果正确使用 [PdfXmpMetadata](http://www.aspose.com/docs/display/pdfnet/PdfXmpMetadata+Class) 类，将非常容易在 PDF 文件中融合智能，并使语义网的实现更进一步。
{{% /alert %}}