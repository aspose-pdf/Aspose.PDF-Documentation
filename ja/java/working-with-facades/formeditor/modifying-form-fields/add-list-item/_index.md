---
title: "リスト項目の追加"
linktitle: "リスト項目の追加"
type: docs
weight: 10
url: /ja/java/add-list-item/
description: Aspose.PDF の FormEditor ファサードを使用して、Java で PDF ドキュメントのリストフィールドに項目を追加する方法を学びます。
lastmod: "2026-10-05"
TechArticle: true
AlternativeHeadline: Java で PDF フォームフィールドにリスト項目を追加
Abstract: この記事では、既存の PDF をバインドし、リストフィールドに新しい項目を追加し、Aspose.PDF for Java の FormEditor ファサードを使用して更新されたドキュメントを保存する方法を示します。
---
## リストフィールドに項目の追加

1. ソースPDFをバインドする `FormEditor` ファサード。
2. 呼び出す `addListItem(...)` 対象フィールドおよび新しい表示/値ペア用に。
3. 更新されたドキュメントを保存してください。

```java
public static void addListItem(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.addListItem("Country", new String[] {"New Zealand", "New Zealand"});
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
