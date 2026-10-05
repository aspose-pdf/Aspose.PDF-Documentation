---
title: XFDFへエクスポート
linktitle: XFDFへエクスポート
type: docs
weight: 20
url: /ja/java/export-to-xfdf/
description: Aspose.PDF の Form ファサードを使用して、Java で PDF フォーム フィールド データを XFDF にエクスポートする方法を学びます。
lastmod: "2026-10-05"
TechArticle: true
AlternativeHeadline: Java で AcroForm データを XFDF にエクスポート
Abstract: この記事では、PDF フォームをバインドし、Aspose.PDF for Java の Form ファサードを使用してフィールド値を XFDF ストリームにエクスポートする方法を示します。
---
使用 `FormExamples.exportXfdf(...)` XFDFとしてフォームフィールドデータを書き込む。

```java
public static void exportXfdf(Path inputFile, Path outputFile) throws Exception {
    Form form = new Form();
    try (OutputStream outputStream = Files.newOutputStream(outputFile)) {
        form.bindPdf(inputFile.toString());
        form.exportXfdf(outputStream);
    } finally {
        form.close();
    }
}
```
