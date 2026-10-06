---
title: 添加橡皮图章
linktitle: 添加橡皮图章
type: docs
weight: 10
url: /zh/java/add-rubber-stamp/
description: 了解如何在 Java 中使用 Aspose.PDF 的 PdfContentEditor 类向 PDF 文档添加橡皮图章注释。
lastmod: "2026-10-06"
TechArticle: true
AlternativeHeadline: 在 Java 中向 PDF 添加橡皮图章
Abstract: 本文展示了如何绑定 PDF、使用 Aspose.PDF for Java 中的 PdfContentEditor 类创建带有标签文本和颜色的橡皮图章注释，并保存更新后的文档。
---
## 添加橡皮图章

1. 将源 PDF 绑定到 `PdfContentEditor` 对象。
2. 调用 `createRubberStamp(...)` 包含页码、矩形、标题、内容和颜色。
3. 保存更新后的 PDF 文档。

```java
public static void addRubberStamp(Path inputFile, Path outputFile) {
    PdfContentEditor editor = new PdfContentEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.createRubberStamp(1, new Rectangle(120, 450, 180, 60), "Approved", "Approved by reviewer", Color.GREEN);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
