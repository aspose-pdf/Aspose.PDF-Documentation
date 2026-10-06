---
title: 添加附件
linktitle: 添加附件
type: docs
weight: 10
url: /zh/java/add-attachment/
description: 了解如何在 Java 中使用 Aspose.PDF 的 PdfContentEditor 门面将外部文件附加到 PDF 文档。
lastmod: "2026-10-06"
TechArticle: true
AlternativeHeadline: 在 Java 中向 PDF 添加文件附件
Abstract: 本文展示了如何绑定 PDF，打开附件为流，使用描述添加文档附件，并使用 Aspose.PDF for Java 中的 PdfContentEditor 门面保存更新后的文件。
---
## 添加文档附件

1. 将源 PDF 绑定到 `PdfContentEditor` 外观。
2. 将附件文件作为输入流打开。
3. 调用 `addDocumentAttachment(...)` 使用流、文件名和描述。
4. 保存更新后的 PDF 文档。

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
