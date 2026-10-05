---
title: FDFへのエクスポート
linktitle: FDFへのエクスポート
type: docs
weight: 10
url: /ja/java/export-to-fdf/
description: Aspose.PDF の Form ファサードを使用して、Java で PDF フォーム フィールドの値を FDF にエクスポートする方法を学びます。
lastmod: "2026-10-05"
TechArticle: true
AlternativeHeadline: Java で AcroForm データを FDF にエクスポート
Abstract: この記事では、PDF フォームをバインドし、Aspose.PDF for Java の Form ファサードを使用してフィールド データを FDF ストリームにエクスポートする方法を示します。
---
使用 `FormExamples.exportFdf(...)` AcroForm フィールドデータを FDF としてシリアライズする必要がある場合。

```java
public static void exportFdf(Path inputFile, Path outputFile) throws Exception {
    Form form = new Form();
    try (OutputStream outputStream = Files.newOutputStream(outputFile)) {
        form.bindPdf(inputFile.toString());
        form.exportFdf(outputStream);
    } finally {
        form.close();
    }
}
```
