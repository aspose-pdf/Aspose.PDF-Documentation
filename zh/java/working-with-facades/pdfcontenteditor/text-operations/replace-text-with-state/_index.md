---
title: 使用状态替换文本
linktitle: 使用状态替换文本
type: docs
weight: 20
url: /zh/java/replace-text-with-state/
description: 了解如何在 Java 中使用 Aspose.PDF 的 `PdfContentEditor` 外观（facade）以自定义格式替换文本。
lastmod: "2026-10-06"
TechArticle: true
AlternativeHeadline: 在 Java 中使用自定义格式替换 PDF 文本。
Abstract: 本文展示了如何绑定 PDF、配置自定义 TextState、替换所有匹配的文本出现位置，并使用 Aspose.PDF for Java 中的 `PdfContentEditor` 外观保存更新后的文档。
---
## 使用自定义文本状态替换文本。

1. 将源 PDF 绑定到 `PdfContentEditor` 外观。
2. 创建并配置一个 `TextState` 使用所需的颜色和字体大小。
3. 将 replace-text 范围设置为 `ReplaceAll`.
4. 调用 `replaceText(...)` 使用搜索文本、替换文本和已配置的 `TextState`.
5. 保存更新后的 PDF 文档。

```java
public static void replaceTextWithState(Path inputFile, Path outputFile) {
    PdfContentEditor editor = new PdfContentEditor();
    try {
        editor.bindPdf(inputFile.toString());
        TextState textState = new TextState();
        textState.setForegroundColor(com.aspose.pdf.Color.getBlue());
        textState.setFontSize(14);
        editor.getReplaceTextStrategy().setReplaceScope(ReplaceTextStrategy.Scope.ReplaceAll);
        editor.replaceText("software", "SOFTWARE", textState);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
