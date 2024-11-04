---
title: 设置现有PDF的XMP元数据 - 外观
type: docs
weight: 20
url: /java/set-xmp-metadata/
description: 本节说明如何使用PdfXmpMetadata类通过Aspose.PDF Facades设置XMP元数据。
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

为了在PDF文件中设置XMP元数据，您需要创建[PdfXmpMetadata](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfXmpMetadata)对象，并使用[bindPdf(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Facade#bindPdf-com.aspose.pdf.IDocument-)方法绑定PDF文件。
 你可以使用 [PdfXmpMetadata](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfXmpMetadata) 类的 setByDefaultMetadataProperties(..) 方法来添加不同的属性。最后，调用 [PdfXmpMetadata](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/SaveableFacade#save-java.io.OutputStream-) 类的 [save(...)](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/SaveableFacade#save-java.io.OutputStream-) 方法。

以下代码片段向您展示了如何在 PDF 文件中添加 XMP 元数据。

{{< gist "aspose-pdf" "474c352a71ac9477aa0d604fd32e1c6a" "Examples-src-main-java-com-aspose-pdf-examples-facades-Document-SetXMPMetadataOfAnExistingPDF-.java" >}}