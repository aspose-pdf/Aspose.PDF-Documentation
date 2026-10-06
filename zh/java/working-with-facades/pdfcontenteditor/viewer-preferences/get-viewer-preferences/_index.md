---
title: 获取查看器首选项
linktitle: 获取查看器首选项
type: docs
weight: 10
url: /zh/java/get-viewer-preferences/
description: 了解如何在 Java 中使用 Aspose.PDF 的 PdfContentEditor 类读取 PDF 文档的查看器首选项。
lastmod: "2026-10-06"
TechArticle: true
AlternativeHeadline: 在 Java 中读取 PDF 查看器首选项
Abstract: 本文展示了如何绑定 PDF 并使用 Aspose.PDF for Java 的 PdfContentEditor 类打印当前的查看器首选项值。
---
## 获取当前查看器首选项

1. 将源 PDF 绑定到 `PdfContentEditor` 立面。
2. 呼叫 `getViewerPreference()` 读取当前值。
3. 检查或打印返回的偏好标志。

```java
public static void getViewerPreferences(Path inputFile) {
    PdfContentEditor editor = new PdfContentEditor();
    try {
        editor.bindPdf(inputFile.toString());
        System.out.println("Current viewer preference: " + editor.getViewerPreference());
    } finally {
        editor.close();
    }
}
```
