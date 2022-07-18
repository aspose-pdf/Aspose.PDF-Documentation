---
title: Set XMP Metadata of an existing PDF - facades
type: docs
weight: 20
url: /java/set-xmp-metadata/
description: This section explains how to set XMP metadata with Aspose.PDF Facades using PdfXmpMetadata Class.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

In order to set XMP metadata in a PDF file, you need to create [PdfXmpMetadata](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfXmpMetadata) object and bind the PDF file using [bindPdf(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Facade#bindPdf-com.aspose.pdf.IDocument-) method. You can use setByDefaultMetadataProperties(..) method of the [PdfXmpMetadata](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfXmpMetadata) class to add different properties. Finally, call the [save(...)](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/SaveableFacade#save-java.io.OutputStream-) method of [PdfXmpMetadata](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfXmpMetadata) class.

The following code snippet shows you how to add XMP metadata in a PDF file.

{{< gist "aspose-pdf" "474c352a71ac9477aa0d604fd32e1c6a" "Examples-src-main-java-com-aspose-pdf-examples-facades-Document-SetXMPMetadataOfAnExistingPDF-.java" >}}