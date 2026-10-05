---
title: "テキストボックス フィールドの作成"
linktitle: "テキストボックス フィールドの作成"
type: docs
weight: 10
url: /ja/java/create-textbox-field/
description: Aspose.PDF の FormEditor ファサードを使用して、Java で PDF ドキュメントにテキストボックス フィールドを追加する方法を学びます。
lastmod: "2026-10-05"
TechArticle: true
AlternativeHeadline: Java を使用して PDF にテキスト フォーム フィールドを作成
Abstract: この記事では、既存の PDF をバインドし、デフォルト値付きのテキスト フィールドを追加し、Aspose.PDF for Java の FormEditor ファサードを使用して変更されたドキュメントを保存する方法を示します。
---
使用 `FormEditorExamples.createTextBoxField(...)` PDF フォームにテキスト フィールドを追加する。

## テキストボックス フィールドの作成

1. ソースPDFをバインドする `FormEditor` ファサード。
2. 各テキストフィールドを追加 `FieldType.Text`, フィールド名、デフォルト値、ページ番号、そして矩形。
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
