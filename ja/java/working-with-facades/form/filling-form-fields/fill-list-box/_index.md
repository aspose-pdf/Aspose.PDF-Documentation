---
title: リスト ボックスに入力
linktitle: リスト ボックスに入力
type: docs
weight: 40
url: /ja/java/fill-list-box/
description: Aspose.PDF の Form ファサードを使用して、Java で PDF フォームのリスト ボックス フィールドに入力する方法を学びます。
lastmod: "2026-10-06"
TechArticle: true
AlternativeHeadline: "Java を使用して PDF フォームのリスト ボックス フィールドの値の設定"
Abstract: この記事では、PDF フォームをバインドし、リスト ボックス フィールドの値を設定し、Aspose.PDF for Java の Form ファサードを使用して更新されたドキュメントを保存する方法を示します。
---
`FormExamples.fillListBoxFields(...)` を使用してリスト ボックス フィールドを埋めてください。

```java
public static void fillListBoxFields(Path inputFile, Path outputFile) {
    Form form = new Form();
    try {
        form.bindPdf(inputFile.toString());
        form.fillField("favorite_colors", "Red");
        form.save(outputFile.toString());
    } finally {
        form.close();
    }
}
```
