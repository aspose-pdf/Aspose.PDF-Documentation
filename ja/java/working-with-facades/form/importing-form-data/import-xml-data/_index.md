---
title: XML データのインポート
linktitle: XML データのインポート
type: docs
weight: 40
url: /ja/java/import-xml-data/
description: Java で Form ファサードを使用して、Aspose.PDF の PDF フォームに XML フォーム データをインポートする方法を学びます。
lastmod: "2026-10-06"
TechArticle: true
AlternativeHeadline: Java で XML から AcroForm データをインポート
Abstract: この記事では、PDF フォームをバインドし、XML ストリームからフィールド値をインポートし、Aspose.PDF for Java の Form ファサードを使用して更新されたドキュメントを保存する方法を示します。
---
`FormExamples.importXml(...)` を使用して、XML データからフォームに入力してください。

```java
public static void importXml(Path inputFile, Path dataFile, Path outputFile) throws Exception {
    Form form = new Form();
    try (InputStream inputStream = Files.newInputStream(dataFile)) {
        form.bindPdf(inputFile.toString());
        form.importXml(inputStream);
        form.save(outputFile.toString());
    } finally {
        form.close();
    }
}
```
