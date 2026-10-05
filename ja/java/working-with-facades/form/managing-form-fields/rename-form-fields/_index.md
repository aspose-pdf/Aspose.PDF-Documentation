---
title: "フォーム フィールドの名前の変更"
linktitle: "フォーム フィールドの名前の変更"
type: docs
weight: 30
url: /ja/java/rename-form-fields/
description: Aspose.PDF の Form ファサードを使用して、Java で PDF フォーム フィールドの名前を変更する方法を学びます。
lastmod: "2026-10-05"
TechArticle: true
AlternativeHeadline: Java で PDF ドキュメントのフォーム フィールドの名前を変更
Abstract: この記事では、PDF フォームをバインドし、既存のフィールドの名前を変更し、更新されたドキュメントを Aspose.PDF for Java の Form ファサードを使用して保存する方法を示します。
---
使用 `FormExamples.renameFormFields(...)` インタラクティブな PDF フォームのフィールド名を変更するには。

```java
public static void renameFormFields(Path inputFile, Path outputFile) {
    Form form = new Form();
    try {
        form.bindPdf(inputFile.toString());
        form.renameField("First Name", "NewFirstName");
        form.renameField("Last Name", "NewLastName");
        form.save(outputFile.toString());
    } finally {
        form.close();
    }
}
```
