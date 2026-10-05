---
title: フィールド アクションの削除
linktitle: フィールド アクションの削除
type: docs
weight: 50
url: /ja/java/remove-field-action/
description: Java で Aspose.PDF の FormEditor ファサードを使用して PDF フィールドからフィールド アクションを削除する方法を学びます。
lastmod: "2026-10-05"
TechArticle: true
AlternativeHeadline: Java で PDF フィールド アクションを削除
Abstract: この記事では、既存の PDF をバインドし、特定のフィールドに関連付けられたアクションを削除し、Aspose.PDF for Java の FormEditor ファサードを使用して更新されたドキュメントを保存する方法を示します。
---
## フィールド アクションの削除

1. ソースPDFをバインドする `FormEditor` ファサード。
2. 呼び出し `removeFieldAction(...)` 対象フィールド用に。
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
