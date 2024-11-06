---
title: 将附件添加到 PDF 文档
linktitle: 将附件添加到 PDF 文档
type: docs
weight: 10
url: zh/java/add-attachment-to-pdf-document/
description: 本页面描述了如何使用 Java 将附件添加到 PDF 文件。
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

附件可以包含各种信息，并且可以是多种文件类型。本文解释了如何向 PDF 文件添加附件。

1. 创建一个包含要附加文件和文件描述的 [FileSpecification](https://reference.aspose.com/pdf/java/com.aspose.pdf/FileSpecification) 对象。

1. 使用 [add(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf/FileSpecification) 方法将 [FileSpecification](https://reference.aspose.com/pdf/java/com.aspose.pdf/FileSpecification) 对象添加到 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 对象的 [EmbeddedFiles](https://reference.aspose.com/pdf/java/com.aspose.pdf/EmbeddedFileCollection) 集合中。[EmbeddedFiles](https://reference.aspose.com/pdf/java/com.aspose.pdf/EmbeddedFileCollection) 集合包含添加到 PDF 文件的所有附件。

以下代码片段向您展示了如何在 PDF 文档中添加附件。

```java
public class ExampleAttachments {
    
    private static String _dataDir = "/home/aspose/pdf-examples/Samples/Attachments/";

    public static void AddingAttachment() {
        // 打开一个文档
  Document pdfDocument = new Document(_dataDir+"input.pdf");
  // 设置一个新的文件作为附件添加
  FileSpecification fileSpecification = new FileSpecification("sample.txt", "示例文本文件");
  // 将附件添加到文档的附件集合中
  pdfDocument.getEmbeddedFiles().add(fileSpecification);
  // 保存更新后的文档
  pdfDocument.save("output.pdf");
    }
}
```