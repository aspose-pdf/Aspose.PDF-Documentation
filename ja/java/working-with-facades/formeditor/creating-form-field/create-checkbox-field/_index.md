---
title: チェックボックス フィールドの作成
linktitle: チェックボックス フィールドの作成
type: docs
weight: 20
url: /ja/java/create-checkbox-field/
description: "Aspose.PDF の FormEditor ファサードを使用して、Java で PDF ドキュメントにチェックボックスフォームフィールドを追加する方法を学びます。"
lastmod: "2026-10-06"
TechArticle: true
AlternativeHeadline: "Java での PDF へのチェックボックスフィールド作成"
Abstract: "この記事では、既存の PDF をバインドし、指定された位置にチェックボックスフィールドを追加し、Aspose.PDF for Java の FormEditor ファサードを使用して変更されたドキュメントを保存する方法を示します。"
---
PDF フォームにチェックボックスフィールドを追加するには、`FormEditorExamples.createCheckBoxField(...)` を使用してください。

## チェックボックス フィールドの作成

1. ソース PDF を `FormEditor` ファサードにバインドしてください。
2. チェックボックスフィールドを追加するには、`FieldType.CheckBox`、フィールド名、キャプション、ページ、および矩形を指定してください。
3. 更新されたドキュメントを保存してください。

```java
public static void createCheckBoxField(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.addField(FieldType.CheckBox, "checkbox1", "Check Box 1", 1, 240, 498, 256, 514);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
