---
title: "ComboBox フィールドの作成"
linktitle: "ComboBox フィールドの作成"
type: docs
weight: 30
url: /ja/java/create-combobox-field/
description: Aspose.PDF の FormEditor ファサードを使用して、Java で PDF ドキュメントにコンボ ボックス フィールドを追加する方法を学びます。
lastmod: "2026-10-06"
TechArticle: true
AlternativeHeadline: "Java を使用した PDF へのコンボ ボックス フィールドの作成"
Abstract: この記事では、既存の PDF をバインドし、コンボ ボックス フィールドを追加し、項目で埋め込み、Aspose.PDF for Java の FormEditor ファサードを使用して修正されたドキュメントを保存する方法を示します。
---
`FormEditorExamples.createComboBoxField(...)` を使用してコンボボックスを作成し、選択可能な項目を追加してください。

## コンボ ボックス フィールドの作成

1. ソース PDF を `FormEditor` ファサードにバインドしてください。
2. デフォルト値と対象矩形を持つコンボボックスフィールドを追加してください。
3. 選択可能なコンボボックス項目を追加してください。
4. 更新された文書を保存してください。

```java
public static void createComboBoxField(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.addField(FieldType.ComboBox, "combobox1", "Australia", 1, 230, 498, 350, 514);
        editor.addListItem("combobox1", new String[] {"Australia", "Australia"});
        editor.addListItem("combobox1", new String[] {"New Zealand", "New Zealand"});
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
