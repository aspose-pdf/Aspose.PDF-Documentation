---
title: テキストフィールドを埋める
linktitle: テキストフィールドを埋める
type: docs
weight: 10
url: /ja/java/fill-text-fields/
description: Aspose.PDF の Form facade を使用して、Java で PDF フォームのテキストフィールドを埋める方法を学びます。
lastmod: "2026-10-05"
TechArticle: true
AlternativeHeadline: Java で PDF のテキスト Form フィールドを埋める
Abstract: この記事では、PDF フォームをバインドし、名前でテキストフィールドの値を設定し、Aspose.PDF for Java の Form facade を使用して更新されたドキュメントを保存する方法を示します。
---
使用する `FormExamples.fillTextFields(...)` テキストベースのフォームフィールドに入力するために。

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
