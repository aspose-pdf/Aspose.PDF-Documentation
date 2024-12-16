---
title: Установить XMP Метаданные существующего PDF - фасады
type: docs
weight: 20
url: /ru/java/set-xmp-metadata/
description: Этот раздел объясняет, как установить XMP метаданные с использованием Aspose.PDF Facades через класс PdfXmpMetadata.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Для установки XMP метаданных в PDF файл, необходимо создать объект [PdfXmpMetadata](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfXmpMetadata) и привязать PDF файл, используя метод [bindPdf(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Facade#bindPdf-com.aspose.pdf.IDocument-).
 Вы можете использовать метод setByDefaultMetadataProperties(..) класса [PdfXmpMetadata](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfXmpMetadata), чтобы добавить различные свойства. В конце вызовите метод [save(...)](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/SaveableFacade#save-java.io.OutputStream-) класса [PdfXmpMetadata](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfXmpMetadata).

Следующий фрагмент кода показывает, как добавить XMP метаданные в PDF файл.

{{< gist "aspose-pdf" "474c352a71ac9477aa0d604fd32e1c6a" "Examples-src-main-java-com-aspose-pdf-examples-facades-Document-SetXMPMetadataOfAnExistingPDF-.java" >}}