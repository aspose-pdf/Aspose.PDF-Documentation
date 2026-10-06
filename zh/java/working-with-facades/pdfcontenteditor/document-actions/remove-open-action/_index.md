---
title: 删除打开操作
linktitle: 删除打开操作
type: docs
weight: 20
url: /zh/java/remove-open-action/
description: 了解如何在 Java 中使用 Aspose.PDF 的 PdfContentEditor 类从 PDF 中删除文档打开操作。
lastmod: "2026-10-06"
TechArticle: true
AlternativeHeadline: 在 Java 中删除 PDF 文档打开操作
Abstract: 本文展示了如何绑定 PDF，删除文档打开操作，并使用 Aspose.PDF for Java 中的 PdfContentEditor 类保存更新后的文档。
---
## 删除文档打开操作

1. 将源 PDF 绑定到 `PdfContentEditor` 对象。
2. 呼叫 `removeDocumentOpenAction()`。
3. 保存更新后的 PDF 文档。

```java
public static void removeOpenAction(Path inputFile, Path outputFile) {
    PdfContentEditor editor = new PdfContentEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.removeDocumentOpenAction();
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
