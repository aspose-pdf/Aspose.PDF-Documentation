---
title: "バーコード フィールドの入力"
linktitle: "バーコード フィールドの入力"
type: docs
weight: 50
url: /ja/java/fill-barcode-fields/
description: "Aspose.PDF の Form ファサードを使用して、Java でバーコード フォーム フィールドを入力する方法を学習します。"
lastmod: "2026-10-06"
TechArticle: true
AlternativeHeadline: "Java を使用した PDF フォームのバーコード フィールドへの値の設定"
Abstract: この記事では、PDF フォームをバインドし、バーコード フィールドの値を設定し、Aspose.PDF for Java の Form ファサードを使用して更新されたドキュメントを保存する方法を示します。
---
PDF フォームのバーコード フィールドに入力するには、`FormExamples.fillBarcodeFields(...)` を使用してください。

```java
public static void fillBarcodeFields(Path inputFile, Path outputFile) {
    Form form = new Form();
    try {
        form.bindPdf(inputFile.toString());
        form.fillBarcodeField("product_barcode", "123456789012");
        form.save(outputFile.toString());
    } finally {
        form.close();
    }
}
```
