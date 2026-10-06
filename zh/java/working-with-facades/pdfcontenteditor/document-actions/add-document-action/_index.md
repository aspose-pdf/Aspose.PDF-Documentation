---
title: 添加文档操作
linktitle: 添加文档操作
type: docs
weight: 10
url: /zh/java/add-document-action/
description: 了解如何在 Java 中使用 Aspose.PDF 的 PdfContentEditor 门面向 PDF 添加文档打开操作。
lastmod: "2026-10-06"
TechArticle: true
AlternativeHeadline: 在 Java 中向 PDF 添加文档打开操作
Abstract: 本文展示了如何绑定 PDF、将 JavaScript 操作附加到文档打开事件，并使用 Aspose.PDF for Java 中的 PdfContentEditor 门面保存更新后的文档。
---
## 添加文档打开操作

1. 将源 PDF 绑定到 `PdfContentEditor` 立面。
2. 调用 `addDocumentAdditionalAction(...)` 与 `DOCUMENT_OPEN` 事件和 JavaScript 操作文本。
3. 保存更新后的 PDF 文档。

```java
public static void addDocumentAction(Path inputFile, Path outputFile) {
    PdfContentEditor editor = new PdfContentEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.addDocumentAdditionalAction(PdfContentEditor.DOCUMENT_OPEN, "app.alert('Document opened with PdfContentEditor action');");
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
