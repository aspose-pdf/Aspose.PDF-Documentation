---
title: すべてのフィールドをフラット化
linktitle: すべてのフィールドをフラット化
type: docs
weight: 10
url: /ja/java/flatten-all-fields/
description: Aspose.PDF の Form facade を使用して、Java で PDF フォームフィールドをすべてフラット化する方法を学びます。
lastmod: "2026-10-05"
TechArticle: true
AlternativeHeadline: Java でインタラクティブなフォームフィールドをすべて静的コンテンツに変換します。
Abstract: この記事では、PDF フォームをバインドし、すべてのフォームフィールドをフラット化し、Aspose.PDF for Java の Form facade を使用して更新されたドキュメントを保存する方法を示します。
---
使用 `FormExamples.flattenAllFields(...)` インタラクティブなフィールドをすべて静的なページコンテンツに変換する必要があるとき。

```java
public static void flattenAllFields(Path inputFile, Path outputFile) {
    Form form = new Form();
    try {
        form.bindPdf(inputFile.toString());
        form.flattenAllFields();
        form.save(outputFile.toString());
    } finally {
        form.close();
    }
}
```
