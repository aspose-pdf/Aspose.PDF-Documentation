---
title: FDF データのインポート
linktitle: FDF データのインポート
type: docs
weight: 10
url: /ja/java/import-fdf-data/
description: Aspose.PDF の Form ファサードを使用して、Java で PDF フォームに FDF フォームデータをインポートする方法を学びます。
lastmod: "2026-10-05"
TechArticle: true
AlternativeHeadline: Java で FDF から AcroForm データをインポートする
Abstract: この記事では、PDF フォームをバインドし、FDF ストリームからフィールド値をインポートし、Aspose.PDF for Java の Form ファサードを使用して更新されたドキュメントを保存する方法を示します。
---
使用 `FormExamples.importFdf(...)` FDF ファイルからフィールド値を適用するために。

```java
public static void importFdf(Path inputFile, Path dataFile, Path outputFile) throws Exception {
    Form form = new Form();
    try (InputStream inputStream = Files.newInputStream(dataFile)) {
        form.bindPdf(inputFile.toString());
        form.importFdf(inputStream);
        form.save(outputFile.toString());
    } finally {
        form.close();
    }
}
```
