---
title: "XFDF へのエクスポート"
linktitle: "XFDF へのエクスポート"
type: docs
weight: 20
url: /ja/java/export-to-xfdf/
description: "Aspose.PDF の Form ファサードを使用して、Java で PDF フォーム フィールド データを XFDF にエクスポートする方法を学習してください。"
lastmod: "2026-10-06"
TechArticle: true
AlternativeHeadline: "Java での AcroForm データの XFDF へのエクスポート"
Abstract: この記事では、PDF フォームをバインドし、Aspose.PDF for Java の Form ファサードを使用してフィールド値を XFDF ストリームにエクスポートする方法を示します。
---
`FormExamples.exportXfdf(...)` を使用して、フォーム フィールド データを XFDF として書き込んでください。

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
