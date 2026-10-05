---
title: チェックボックス フィールドの作成
linktitle: チェックボックス フィールドの作成
type: docs
weight: 20
url: /ja/java/create-checkbox-field/
description: Aspose.PDF の FormEditor ファサードを使用して、Java で PDF ドキュメントにチェックボックス フォーム フィールドを追加する方法を学びます。
lastmod: "2026-10-05"
TechArticle: true
AlternativeHeadline: Java で PDF にチェックボックス フィールドを作成する
Abstract: この記事では、既存の PDF をバインドし、指定された位置にチェックボックス フィールドを追加し、Aspose.PDF for Java の FormEditor ファサードを使用して変更されたドキュメントを保存する方法を示します。
---
使用 `FormEditorExamples.createCheckBoxField(...)` PDFフォームにチェックボックスフィールドを追加するには。

## チェックボックス フィールドの作成

1. ソースPDFをバインドする `FormEditor` ファサード。
2. チェックボックスフィールドを追加 `FieldType.CheckBox`, フィールド名、キャプション、ページ、そして矩形。
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
