---
title: フィールド スクリプトの設定
linktitle: フィールド スクリプトの設定
type: docs
weight: 20
url: /ja/java/set-field-script/
description: "Aspose.PDF の FormEditor ファサードを使用して、Java で PDF フォームフィールドに JavaScript アクションを割り当てまたは更新する方法を学習します。"
lastmod: "2026-10-06"
TechArticle: true
AlternativeHeadline: "Java での PDF フォームフィールドへの JavaScript アクションの設定"
Abstract: "この記事では、既存の PDF をバインドし、初期スクリプトを追加してから更新されたスクリプトに置き換え、Aspose.PDF for Java の FormEditor ファサードを使用して変更されたドキュメントを保存する方法を示します。"
---
## フィールド スクリプトの設定

1. ソース PDF を `FormEditor` ファサードにバインドしてください。
2. フィールドに初期の JavaScript アクションを追加してください。
3. それを更新されたスクリプト テキストに置き換えてください。
4. 更新されたドキュメントを保存してください。

```java
public static void setFieldScript(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.addFieldScript("Script_Demo_Button", "app.alert('Script 1 has been executed');");
        editor.setFieldScript("Script_Demo_Button", "app.alert('Script 2 has been executed');");
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
