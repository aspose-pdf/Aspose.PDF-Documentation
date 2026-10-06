---
title: 删除附件
linktitle: 删除附件
type: docs
weight: 50
url: /zh/java/remove-attachments/
description: 了解如何在 Java 中使用 Aspose.PDF 的 PdfContentEditor 外观从 PDF 中删除所有文档附件。
lastmod: "2026-10-06"
TechArticle: true
AlternativeHeadline: 在 Java 中删除所有 PDF 附件
Abstract: 本文展示了如何绑定 PDF、删除所有文档附件，并使用 Aspose.PDF for Java 中的 PdfContentEditor 外观保存更新后的文件。
---
## 删除所有附件

1. 将源 PDF 绑定到 `PdfContentEditor` 外观。
2. 调用 `deleteAttachments()` 删除所有嵌入的附件。
3. 保存更新后的 PDF 文档。

```java
public static void removeAttachments(Path inputFile, Path outputFile) {
    PdfContentEditor editor = new PdfContentEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.deleteAttachments();
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
