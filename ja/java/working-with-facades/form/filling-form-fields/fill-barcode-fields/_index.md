---
title: バーコード フィールドを入力する
linktitle: バーコード フィールドを入力する
type: docs
weight: 50
url: /ja/java/fill-barcode-fields/
description: Aspose.PDF の Form ファサードを使用して、Java でバーコード フォーム フィールドを入力する方法を学びます。
lastmod: "2026-10-05"
TechArticle: true
AlternativeHeadline: Java を使用して PDF フォームのバーコード フィールドに値を設定する
Abstract: この記事では、PDF フォームをバインドし、バーコード フィールドの値を設定し、Aspose.PDF for Java の Form ファサードを使用して更新されたドキュメントを保存する方法を示します。
---
使用する `FormExamples.fillBarcodeFields(...)` PDF フォームのバーコード フィールドに入力するために

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
