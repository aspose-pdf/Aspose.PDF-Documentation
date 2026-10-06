---
title: チェックボックス フィールドの入力
linktitle: チェックボックス フィールドの入力
type: docs
weight: 20
url: /ja/java/fill-check-box-fields/
description: "Aspose.PDF の Form ファサードを使用して、Java で PDF フォームのチェックボックス フィールドを入力する方法を学習します。"
lastmod: "2026-10-06"
TechArticle: true
AlternativeHeadline: "Java による PDF フォームのチェックボックス フィールド値の設定"
Abstract: この記事では、PDF フォームをバインドし、名前でチェックボックス フィールドを設定し、Aspose.PDF for Java の Form ファサードを使用して更新されたドキュメントを保存する方法を示します。
---
`FormExamples.fillCheckBoxFields(...)` を使用して、フォームのチェックボックスの値を設定してください。

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
