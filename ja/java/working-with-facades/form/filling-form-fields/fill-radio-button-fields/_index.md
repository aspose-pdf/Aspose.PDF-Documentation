---
title: ラジオボタン フィールドを入力
linktitle: ラジオボタン フィールドを入力
type: docs
weight: 30
url: /ja/java/fill-radio-button-fields/
description: Aspose.PDF の Form ファサードを使用して、Java で PDF フォームのラジオボタンの値を選択する方法を学びます。
lastmod: "2026-10-05"
TechArticle: true
AlternativeHeadline: Java でラジオボタン フィールドのオプションを選択
Abstract: この記事では、PDF フォームをバインドし、インデックスでラジオボタンのオプションを選択し、Aspose.PDF for Java の Form ファサードを使用して更新されたドキュメントを保存する方法を示します。
---
使用 `FormExamples.fillRadioButtonFields(...)` ラジオボタンのオプションを選択する。

```java
public static void fillRadioButtonFields(Path inputFile, Path outputFile) {
    Form form = new Form();
    try {
        form.bindPdf(inputFile.toString());
        form.fillField("gender", 0);
        form.save(outputFile.toString());
    } finally {
        form.close();
    }
}
```
