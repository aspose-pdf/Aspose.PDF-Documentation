---
title: 创建符合 PDF/3-A 的 PDF 并在 Java 中附加 ZUGFeRD 发票
linktitle: 将 ZUGFeRD 附加到 PDF
type: docs
weight: 10
url: /java/attach-zugferd/
description: 了解如何在 Aspose.PDF for Java 中生成带有 ZUGFeRD 的 PDF 文档
lastmod: "2024-01-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 将 ZUGFeRD 附加到 PDF

我们建议按照以下步骤将 ZUGFeRD 附加到 PDF：

* 定义一个路径变量，该变量指向输入和输出 PDF 文件所在的文件夹。
* 定义一个字符串变量 `path`，用于存储将被处理的 PDF 文件的路径。使用 `Paths.get` 方法组合完整路径的各个部分。
* 创建一个 try-with-resources 语句，以确保从路径变量创建的 Document 对象在语句结束后自动关闭。Document 对象表示将被修改和保存的 PDF 文档。

* 通过提供另一个文件的路径和描述来创建 [FileSpecification](https://reference.aspose.com/pdf/java/com.aspose.pdf/filespecification/) 对象，该文件包含符合 ZUGFeRD 标准的发票元数据。
* 向文件规范对象添加属性，例如描述、MIME类型和AFrelationship。AFrelationship表示嵌入文件与PDF文档的关系。在这种情况下，它被设置为“Alternative”，这意味着嵌入文件是PDF内容的替代表示。
* 将文件规范对象添加到文档的嵌入文件集合中。文件名应指定为ZUGFeRD标准，例如“factor-x.xml”。
* 将文档转换为PDF/A-3U格式，这是PDF的一个子集，确保电子文档的长期保存。PDF/A-3U允许在PDF文档中嵌入任何格式的文件。
* 将转换后的文档保存为新的PDF文件（例如“ZUGFeRD-res.pdf”）。
* 关闭try-with-resources语句并释放Document对象。

```java
String _dataDir = "/home/aspose/pdf-examples/Samples/";
String path = Paths.get(_dataDir, "ZUGFeRD", "ZUGFeRD-test.pdf").toString();
try (Document document = new Document(path)) {
    String description = "符合ZUGFeRD标准的发票元数据";
    path = Paths.get(_dataDir, "ZUGFeRD", "factur-x.xml").toString();
    FileSpecification fileSpecification = new FileSpecification(path.toString(), description);
    fileSpecification.setMIMEType("text/xml");
    fileSpecification.setAFRelationship(com.aspose.pdf.AFRelationship.Alternative);

    // 将附件添加到文档的附件集合中
    document.getEmbeddedFiles().add(fileSpecification);
    path = Paths.get(_dataDir, "ZUGFeRD", "log.xml").toString();
    document.convert(path, PdfFormat.PDF_A_3A, ConvertErrorAction.Delete);
    path = Paths.get(_dataDir, "ZUGFeRD", "ZUGFeRD-res.pdf").toString();
    document.save(path);
}
```