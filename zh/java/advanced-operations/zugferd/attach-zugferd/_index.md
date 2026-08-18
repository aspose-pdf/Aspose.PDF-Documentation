---
title: 使用 Java 创建 PDF/3-A 兼容的 PDF 并附加 ZUGFeRD 发票
linktitle: 将 ZUGFeRD 附加到 PDF
type: docs
weight: 10
url: /java/attach-zugferd/
description: 了解如何将 ZUGFeRD 发票 XML 附加到 PDF 并使用 Java 将其转换为 PDF/A-3A。
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Java 将 ZUGFeRD 发票 XML 附加到 PDF 文档
Abstract: 本文介绍如何使用 Aspose.PDF for Java 创建符合 PDF/A-3A 标准的发票文档。它包括将发票 XML 作为嵌入文件附加、设置 MIME 类型和关联文件关系、将 PDF 转换为 PDF/A-3A 以及保存最终的 ZUGFeRD 就绪文档。
---
当您需要将发票 XML 打包到 PDF 中以实现 ZUGFeRD 样式工作流程时，请使用 `Document` 和 `FileSpecification` API。

## 将 ZUGFeRD 发票 XML 附加到 PDF

1. 打开源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 为 XML 发票文件创建 [FileSpecification](https://reference.aspose.com/pdf/java/com.aspose.pdf/filespecification/)。
1. 设置嵌入文件元数据，包括 MIME 类型和 [AFRelationship](https://reference.aspose.com/pdf/java/com.aspose.pdf/afrelationship/)。
1. 将 [FileSpecification](https://reference.aspose.com/pdf/java/com.aspose.pdf/filespecification/) 添加到文档嵌入文件集合中。
1. 将文档转换为 [PdfFormat](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfformat/) `PDF_A_3A`。
1. 保存更新的 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。

```java
public static void attachInvoiceZugferdFormat(Path inputFile, Path invoiceFile, Path outputFile) {
        try (Document document = new Document(inputFile.toString())) {
            String description = "Invoice metadata conforming to ZUGFeRD standard";
            FileSpecification fileSpecification = new FileSpecification(invoiceFile.toString(), description);

            fileSpecification.setMIMEType("text/xml");
            fileSpecification.setAFRelationship(AFRelationship.Alternative);

            document.getEmbeddedFiles().add("factur", fileSpecification);

            String outputFileName = outputFile.toString();
            String logPath = outputFileName.replace(".pdf", "_log.xml");
            document.convert(logPath, PdfFormat.PDF_A_3A, ConvertErrorAction.Delete);
            document.save(outputFile.toString());
        }
        System.out.println("ZUGFeRD invoice attached to " + outputFile);
    }
```
