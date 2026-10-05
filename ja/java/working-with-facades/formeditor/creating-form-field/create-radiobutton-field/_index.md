---
title: "RadioButton フィールドの作成"
linktitle: "RadioButton フィールドの作成"
type: docs
weight: 50
url: /ja/java/create-radiobutton-field/
description: Aspose.PDF の FormEditor ファサードを使用して、Java で PDF ドキュメントにラジオボタン フィールドを追加する方法を学びます。
lastmod: "2026-10-05"
TechArticle: true
AlternativeHeadline: Java で PDF に radio button フィールドを作成する
Abstract: この記事では、既存の PDF をバインドし、ラジオボタンのレイアウト設定を構成し、ラジオボタン フィールドを作成し、Aspose.PDF for Java の FormEditor ファサードを使用して変更されたドキュメントを保存する方法を示します。
---
使用 `FormEditorExamples.createRadioButtonField(...)` 事前に定義されたオプションを持つラジオボタンフィールドを作成する

## ラジオボタン フィールドの作成

1. ソースPDFをバインドする `FormEditor` ファサード。
2. ラジオボタンの間隔、向き、および項目サイズを設定してください。
3. ラジオボタン項目を定義してください。
4. デフォルト選択と矩形を持つラジオボタンフィールドを追加してください。
5. 更新されたドキュメントを保存してください。

```java
public static void createRadioButtonField(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.setRadioGap(4);
        editor.setRadioHoriz(false);
        editor.setRadioButtonItemSize(20);
        editor.setItems(new String[] {"Australia", "New Zealand", "Malaysia"});
        editor.addField(FieldType.Radio, "radiobutton1", "Malaysia", 1, 240, 498, 256, 514);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
