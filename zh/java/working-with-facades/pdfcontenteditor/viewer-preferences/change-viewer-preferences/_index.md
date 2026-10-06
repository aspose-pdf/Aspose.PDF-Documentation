---
title: 更改查看器首选项
linktitle: 更改查看器首选项
type: docs
weight: 20
url: /zh/java/change-viewer-preferences/
description: 了解如何在 Java 中使用 Aspose.PDF 的 PdfContentEditor 类更改 PDF 文档的查看器首选项。
lastmod: "2026-10-06"
TechArticle: true
AlternativeHeadline: 在 Java 中更改 PDF 查看器首选项
Abstract: 本文展示了如何绑定 PDF，修改当前的查看器首选项值，并使用 Aspose.PDF for Java 中的 PdfContentEditor 类保存更新后的文档。
---
## 更改查看器首选项

1. 将源 PDF 绑定到 `PdfContentEditor` 对象。
2. 读取当前的查看器首选项值。
3. 将其与所需的附加标志组合起来，然后将结果传递给 `changeViewerPreference(...)`。
4. 保存更新后的 PDF 文档。

```java
public static void changeViewerPreferences(Path inputFile, Path outputFile) {
    PdfContentEditor editor = new PdfContentEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.changeViewerPreference(editor.getViewerPreference() | 1);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
