---
title: "FDF へのエクスポート"
linktitle: "FDF へのエクスポート"
type: docs
weight: 10
url: /ja/java/export-to-fdf/
description: "Aspose.PDF の Form ファサードを使用して、Java で PDF フォームフィールドの値を FDF にエクスポートする方法を学習してください。"
lastmod: "2026-10-06"
TechArticle: true
AlternativeHeadline: Java で AcroForm データを FDF にエクスポート
Abstract: "この記事では、PDF フォームをバインドし、Aspose.PDF for Java の Form ファサードを使用してフィールドデータを FDF ストリームにエクスポートする方法を説明します。"
---
AcroForm フィールドデータを FDF としてシリアライズする必要がある場合は、`FormExamples.exportFdf(...)` を使用してください。

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
