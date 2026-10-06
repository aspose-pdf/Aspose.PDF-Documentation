---
title: "XML へのエクスポート"
linktitle: "XML へのエクスポート"
type: docs
weight: 40
url: /ja/java/export-to-xml/
description: "Java で Aspose.PDF の Form ファサードを使用して、PDF フォーム データを XML にエクスポートする方法を学習してください。"
lastmod: "2026-10-06"
TechArticle: true
AlternativeHeadline: "Java での AcroForm データの XML へのエクスポート"
Abstract: この記事では、PDF フォームをバインドし、Aspose.PDF for Java の Form ファサードを使用してフィールド値を XML ストリームにエクスポートする方法を示します。
---
`FormExamples.exportXml(...)` を使用して、フォーム フィールド データを XML として保存してください。

```java
public static void exportXml(Path inputFile, Path outputFile) throws Exception {
    Form form = new Form();
    try (OutputStream outputStream = Files.newOutputStream(outputFile)) {
        form.bindPdf(inputFile.toString());
        form.exportXml(outputStream);
    } finally {
        form.close();
    }
}
```
