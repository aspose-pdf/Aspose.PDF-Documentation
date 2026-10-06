---
title: フィールド アクションの削除
linktitle: フィールド アクションの削除
type: docs
weight: 50
url: /ja/java/remove-field-action/
description: "Java で Aspose.PDF の FormEditor ファサードを使用して、PDF フォームフィールドからフィールド アクションを削除する方法を学習します。"
lastmod: "2026-10-06"
TechArticle: true
AlternativeHeadline: "Java での PDF フィールド アクションの削除"
Abstract: "この記事では、既存の PDF をバインドし、特定のフィールドに関連付けられたアクションを削除して、Aspose.PDF for Java の FormEditor ファサードを使用して更新されたドキュメントを保存する方法を示します。"
---
## フィールド アクションの削除

1. ソース PDF を `FormEditor` ファサードにバインドしてください。
2. 対象フィールドに対して `removeFieldAction(...)` を呼び出してください。
3. 更新されたドキュメントを保存してください。

```java
public static void removeFieldAction(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.removeFieldAction("Script_Demo_Button");
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
