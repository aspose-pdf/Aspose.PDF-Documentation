---
title: チェックボックス フィールドの入力
linktitle: チェックボックス フィールドの入力
type: docs
weight: 20
url: /ja/java/fill-check-box-fields/
description: Aspose.PDF の Form ファサードを使用して、Java で PDF フォームのチェックボックス フィールドを入力する方法を学びます。
lastmod: "2026-10-05"
TechArticle: true
AlternativeHeadline: Java で PDF フォームのチェックボックス フィールドの値を設定する
Abstract: この記事では、PDF フォームをバインドし、名前でチェックボックス フィールドを設定し、Aspose.PDF for Java の Form ファサードを使用して更新されたドキュメントを保存する方法を示します。
---
使用 `FormExamples.fillCheckBoxFields(...)` フォームのチェックボックスの値を設定する。

```java
public static void fillCheckBoxFields(Path inputFile, Path outputFile) {
    Form form = new Form();
    try {
        form.bindPdf(inputFile.toString());
        form.fillField("subscribe_newsletter", "Yes");
        form.fillField("accept_terms", "Yes");
        form.save(outputFile.toString());
    } finally {
        form.close();
    }
}
```
