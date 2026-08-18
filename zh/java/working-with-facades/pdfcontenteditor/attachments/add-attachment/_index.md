---
title: 添加附件
linktitle: 添加附件
type: docs
weight: 10
url: /java/add-attachment/
description: 了解如何使用 Aspose.PDF 中的 PdfContentEditor 外观将外部文件附加到 Java 中的 PDF 文档。
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: 使用 Java 将文件附件添加到 PDF
Abstract: 本文介绍如何绑定 PDF、以流的形式打开附件、添加带有说明的文档附件以及使用 Aspose.PDF for Java 中的 PdfContentEditor 外观保存更新的文件。
---
## 添加文档附件

1. 将源 PDF 绑定到 `PdfContentEditor` 外观。
2. Open the attachment file as an input stream.
3. Call `addDocumentAttachment(...)` with the stream, file name, and description.
4. Save the updated PDF document.

```java
public static void addAttachment(Path inputFile, Path attachmentFile, Path outputFile) throws Exception {
    PdfContentEditor editor = new PdfContentEditor();
    try (InputStream attachmentStream = Files.newInputStream(attachmentFile)) {
        editor.bindPdf(inputFile.toString());
        editor.addDocumentAttachment(attachmentStream, attachmentFile.getFileName().toString(), "Sample attachment.");
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
