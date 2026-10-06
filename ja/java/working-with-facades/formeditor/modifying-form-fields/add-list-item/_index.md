---
title: "リスト項目の追加"
linktitle: "リスト項目の追加"
type: docs
weight: 10
url: /ja/java/add-list-item/
description: "Aspose.PDF の FormEditor ファサードを使用して、Java で PDF ドキュメントのリスト フィールドに項目を追加する方法を学びます。"
lastmod: "2026-10-06"
TechArticle: true
AlternativeHeadline: "Java での PDF フォーム フィールドへのリスト項目の追加"
Abstract: "この記事では、既存の PDF をバインドし、リスト フィールドに新しい項目を追加し、Aspose.PDF for Java の FormEditor ファサードを使用して更新されたドキュメントを保存する方法を示します。"
---
## リスト フィールドへの項目の追加

1. ソース PDF を `FormEditor` ファサードにバインドしてください。
2. 対象フィールドおよび新しい表示/値ペアに対して `addListItem(...)` を呼び出してください。
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
