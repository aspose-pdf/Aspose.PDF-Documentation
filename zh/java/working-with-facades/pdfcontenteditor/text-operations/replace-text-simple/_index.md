---
title: 简易文本替换
linktitle: 简易文本替换
type: docs
weight: 10
url: /zh/java/replace-text-simple/
description: 了解如何在 Java 中使用 Aspose.PDF 的 PdfContentEditor 门面替换 PDF 文档中的全部文本。
lastmod: "2026-10-06"
TechArticle: true
AlternativeHeadline: 在 Java 中替换 PDF 文本
Abstract: 本文展示了如何绑定 PDF、配置 replace-text 范围、替换所有匹配的文本出现位置，并使用 Aspose.PDF for Java 中的 PdfContentEditor 门面保存更新后的文档。
---
## 在整个文档中替换文本

1. 将源 PDF 绑定到 `PdfContentEditor` 外观.
2. 将 replace-text 范围设置为 `ReplaceAll`.
3. 呼叫 `replaceText(...)` 使用搜索文本和替换文本。
4. 保存更新后的 PDF 文档。

```java
public static void replaceTextSimple(Path inputFile, Path outputFile) {
    PdfContentEditor editor = new PdfContentEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.getReplaceTextStrategy().setReplaceScope(ReplaceTextStrategy.Scope.ReplaceAll);
        editor.replaceText("33", "XXXIII ");
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
