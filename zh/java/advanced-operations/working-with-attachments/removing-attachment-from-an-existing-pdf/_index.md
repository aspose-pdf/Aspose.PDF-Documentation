---
title: 从现有PDF中移除附件
linktitle: 从现有PDF中移除附件
type: docs
weight: 30
url: zh/java/removing-attachment-from-an-existing-pdf/
description: Aspose.PDF可以从您的PDF文档中移除附件。使用Java PDF API通过Aspose.PDF库移除PDF文件中的附件。
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Aspose.PDF可以从PDF文件中移除附件。PDF文档的附件保存在Document对象的EmbeddedFiles集合中。

PDF文档的附件保存在[Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document)对象的[EmbeddedFiles](https://reference.aspose.com/pdf/java/com.aspose.pdf/EmbeddedFileCollection)集合中。

要删除与PDF文件关联的所有附件：

1. 调用[EmbeddedFiles](https://reference.aspose.com/pdf/java/com.aspose.pdf/EmbeddedFileCollection)集合的delete(..)方法。

1. 使用 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 对象的 save 方法保存更新后的文件。

以下代码片段展示了如何从 PDF 文档中删除所有附件。

```java
   public static void DeleteAllAttachmentsFromPDF(){
  // 打开文档
  Document pdfDocument = new Document(_dataDir+"input.pdf");
  // 删除所有附件
  pdfDocument.getEmbeddedFiles().delete();
  // 保存更新后的文件
  pdfDocument.save("output.pdf");

    }
```