---
title: XFDF データのインポート
linktitle: XFDF データのインポート
type: docs
weight: 20
url: /ja/java/import-xfdf-data/
description: Aspose.PDF の Form ファサードを使用して、Java で XFDF フォーム データを PDF フォームにインポートする方法を学びます。
lastmod: "2026-10-05"
TechArticle: true
AlternativeHeadline: Java で XFDF から AcroForm データをインポートする
Abstract: この記事では、PDF フォームをバインドし、XFDF ストリームからフィールド値をインポートし、Aspose.PDF for Java の Form ファサードで更新されたドキュメントを保存する方法を示します。
---
使用 `FormExamples.importXfdf(...)` XFDF データからフォームに入力する。

```java
public static void importXfdf(Path inputFile, Path dataFile, Path outputFile) throws Exception {
    Form form = new Form();
    try (InputStream inputStream = Files.newInputStream(dataFile)) {
        form.bindPdf(inputFile.toString());
        form.importXfdf(inputStream);
        form.save(outputFile.toString());
    } finally {
        form.close();
    }
}
```
