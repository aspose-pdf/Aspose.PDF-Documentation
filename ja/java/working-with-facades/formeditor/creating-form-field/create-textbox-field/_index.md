---
title: "テキストボックスフィールドの作成"
linktitle: "テキストボックスフィールドの作成"
type: docs
weight: 10
url: /ja/java/create-textbox-field/
description: "Aspose.PDF の FormEditor ファサードを使用して、Java で PDF ドキュメントにテキスト ボックス フィールドを追加する方法を学習します。"
lastmod: "2026-10-06"
TechArticle: true
AlternativeHeadline: "Java を使用した PDF へのテキスト フォーム フィールドの作成"
Abstract: この記事では、既存の PDF をバインドし、デフォルト値付きのテキスト フィールドを追加し、Aspose.PDF for Java の FormEditor ファサードを使用して変更されたドキュメントを保存する方法を示します。
---
PDF フォームにテキスト フィールドを追加するには、`FormEditorExamples.createTextBoxField(...)` を使用してください。

## テキストボックスフィールドの作成

1. ソース PDF を `FormEditor` ファサードにバインドしてください。
2. 各テキスト フィールドを追加する際は、`FieldType.Text`、フィールド名、デフォルト値、ページ番号、および矩形を指定してください。
3. 更新されたドキュメントを保存してください。

```java
public static void createTextBoxField(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.addField(FieldType.Text, "first_name", "Alexander", 1, 50, 570, 150, 590);
        editor.addField(FieldType.Text, "last_name", "Smith", 1, 235, 570, 330, 590);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
