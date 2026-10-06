---
title: XFDF データのインポート
linktitle: XFDF データのインポート
type: docs
weight: 20
url: /ja/java/import-xfdf-data/
description: "Aspose.PDF の Form ファサードを使用して、Java で XFDF フォームデータを PDF フォームにインポートする方法を学びます。"
lastmod: "2026-10-06"
TechArticle: true
AlternativeHeadline: "Java での XFDF から AcroForm データのインポート"
Abstract: この記事では、PDF フォームをバインドし、XFDF ストリームからフィールド値をインポートし、Aspose.PDF for Java の Form ファサードで更新されたドキュメントを保存する方法を示します。
---
`FormExamples.importXfdf(...)` を使用して、XFDF データからフォームに入力してください。

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
