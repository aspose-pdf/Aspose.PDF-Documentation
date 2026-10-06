---
title: "ListBox フィールドの作成"
linktitle: "ListBox フィールドの作成"
type: docs
weight: 40
url: /ja/java/create-listbox-field/
description: Aspose.PDF の FormEditor ファサードを使用して、Java で PDF ドキュメントにリストボックス フィールドを追加する方法を学びます。
lastmod: "2026-10-06"
TechArticle: true
AlternativeHeadline: "Java を使用した PDF へのリストボックス フィールドの作成"
Abstract: "この記事では、既存の PDF をバインドし、リスト項目を定義し、リストボックスフィールドを追加し、Aspose.PDF for Java の FormEditor ファサードを使用して変更されたドキュメントを保存する方法を示します。"
---
`FormEditorExamples.createListBoxField(...)` を使用して、事前定義された項目を持つリストボックスを作成してください。

## リストボックス フィールドの作成

1. ソース PDF を `FormEditor` ファサードにバインドしてください。
2. 利用可能なリスト項目を `setItems(...)` で定義してください。
3. デフォルト値と矩形を指定してリストボックスフィールドを追加してください。
4. 更新されたドキュメントを保存してください。

```java
public static void createListBoxField(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.setItems(new String[] {"Australia", "New Zealand", "Malaysia"});
        editor.addField(FieldType.ListBox, "listbox1", "Australia", 1, 230, 398, 350, 514);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
