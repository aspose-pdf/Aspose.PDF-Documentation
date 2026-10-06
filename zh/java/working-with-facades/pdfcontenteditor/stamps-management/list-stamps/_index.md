---
title: 列出印章
linktitle: 列出印章
type: docs
weight: 20
url: /zh/java/list-stamps/
description: 了解如何在 Java 中使用 Aspose.PDF 的 PdfContentEditor 门面列出页面上的橡胶印章。
lastmod: "2026-10-06"
TechArticle: true
AlternativeHeadline: 在 Java 中列出 PDF 橡胶印章
Abstract: 本文展示了如何绑定 PDF，检索页面上的印章，并使用 Aspose.PDF for Java 中的 PdfContentEditor 门面检查生成的集合。
---
## 列出页面上的印章

1. 将源 PDF 绑定到 `PdfContentEditor` 外观。
2. 调用 `getStamps(pageNumber)` 检索目标页面上的印章。
3. 检查结果 `StampInfo[]` 集合。

```java
public static void listStamps(Path inputFile) {
    PdfContentEditor editor = new PdfContentEditor();
    try {
        editor.bindPdf(inputFile.toString());
        StampInfo[] stamps = editor.getStamps(1);
        System.out.println("Stamps on page 1: " + stamps.length);
    } finally {
        editor.close();
    }
}
```
