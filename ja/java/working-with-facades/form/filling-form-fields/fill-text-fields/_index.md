---
title: テキストフィールドを埋める
linktitle: テキストフィールドを埋める
type: docs
weight: 10
url: /ja/java/fill-text-fields/
description: "Aspose.PDF の Form ファサードを使用して、Java で PDF フォームのテキストフィールドを埋める方法を学びます。"
lastmod: "2026-10-06"
TechArticle: true
AlternativeHeadline: Java で PDF のテキスト Form フィールドを埋める
Abstract: "この記事では、PDF フォームをバインドし、名前でテキストフィールドの値を設定し、Aspose.PDF for Java の Form ファサードを使用して更新されたドキュメントを保存する方法を示します。"
---
テキストベースのフォームフィールドに入力するには、`FormExamples.fillTextFields(...)` を使用してください。

```java
public static void fillTextFields(Path inputFile, Path outputFile) {
    Form form = new Form();
    try {
        form.bindPdf(inputFile.toString());
        form.fillField("name", "John Doe");
        form.fillField("address", "123 Main St, Anytown, USA");
        form.fillField("email", "john.doe@example.com");
        form.save(outputFile.toString());
    } finally {
        form.close();
    }
}
```
