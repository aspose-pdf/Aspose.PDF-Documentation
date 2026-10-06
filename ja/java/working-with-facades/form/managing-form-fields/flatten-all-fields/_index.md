---
title: すべてのフィールドをフラット化
linktitle: すべてのフィールドをフラット化
type: docs
weight: 10
url: /ja/java/flatten-all-fields/
description: "Aspose.PDF の Form ファサードを使用して、Java で PDF フォームフィールドをすべてフラット化する方法を学習してください。"
lastmod: "2026-10-06"
TechArticle: true
AlternativeHeadline: "Java での インタラクティブなフォームフィールドのすべて静的コンテンツへの変換"
Abstract: "この記事では、PDF フォームをバインドし、すべてのフォームフィールドをフラット化し、Aspose.PDF for Java の Form ファサードを使用して更新されたドキュメントを保存する方法を示します。"
---
インタラクティブなフィールドをすべて静的なページコンテンツに変換する必要がある場合は、`FormExamples.flattenAllFields(...)` を使用してください。

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
