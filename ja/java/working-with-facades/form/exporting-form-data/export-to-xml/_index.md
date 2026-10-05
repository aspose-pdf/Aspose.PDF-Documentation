---
title: XML にエクスポート
linktitle: XML にエクスポート
type: docs
weight: 40
url: /ja/java/export-to-xml/
description: Java で Aspose.PDF の Form ファサードを使用して PDF フォーム データを XML にエクスポートする方法を学びます。
lastmod: "2026-10-05"
TechArticle: true
AlternativeHeadline: Java で AcroForm データを XML にエクスポート
Abstract: この記事では、PDF フォームをバインドし、Aspose.PDF for Java の Form ファサードを使用してフィールド値を XML ストリームにエクスポートする方法を示します。
---
使用 `FormExamples.exportXml(...)` フォームフィールドデータをXMLとして保存する。

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
