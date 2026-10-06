---
title: 在 Java 中创建符合 PDF/3-A 标准的 PDF 并附加 ZUGFeRD 发票。
linktitle: 将 ZUGFeRD 附加到 PDF。
type: docs
weight: 10
url: /zh/java/attach-zugferd/
description: 了解如何在 Java 中将 ZUGFeRD 发票 XML 附加到 PDF 并将其转换为 PDF/A-3A。
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Java 将 ZUGFeRD 发票 XML 附加到 PDF 文档。
Abstract: 本文说明了如何使用 Aspose.PDF for Java 创建符合 PDF/A-3A 标准的发票文档。内容包括将发票 XML 作为嵌入文件附加、设置 MIME 类型和 associated-file 关系、将 PDF 转换为 PDF/A-3A，以及保存最终的 ZUGFeRD 可用文档。
---
使用 `Document` 和 `FileSpecification` 在需要将发票 XML 打包到 PDF 中以用于 ZUGFeRD 风格工作流时的 API。

## 将 ZUGFeRD 发票 XML 附加到 PDF

1. 打开源 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 创建 [FileSpecification](https://reference.aspose.com/pdf/java/com.aspose.pdf/filespecification/) 用于 XML 发票文件。
1. 设置嵌入文件的元数据，包括 MIME 类型和 [AFRelationship](https://reference.aspose.com/pdf/java/com.aspose.pdf/afrelationship/)。
1. 添加 [FileSpecification](https://reference.aspose.com/pdf/java/com.aspose.pdf/filespecification/) 到文档嵌入文件集合。
1. 将文档转换为 [PdfFormat](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfformat/) `PDF_A_3A`。
1. 保存已更新的 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。

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
