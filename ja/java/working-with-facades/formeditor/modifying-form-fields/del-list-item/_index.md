---
title: "リスト項目の削除"
linktitle: "リスト項目の削除"
type: docs
weight: 20
url: /ja/java/del-list-item/
description: Aspose.PDF の FormEditor ファサードを使用して、Java で PDF ドキュメントのリストフィールドから項目を削除する方法を学びます。
lastmod: "2026-10-06"
TechArticle: true
AlternativeHeadline: "Java での PDF フォームフィールドのリスト項目の削除"
Abstract: この記事では、既存の PDF をバインドし、リストフィールドから特定の項目を削除し、Aspose.PDF for Java の FormEditor ファサードを使用して更新されたドキュメントを保存する方法を示します。
---
## リストフィールドから項目の削除

1. ソース PDF を `FormEditor` ファサードにバインドしてください。
2. 対象フィールドと削除する項目に対して `delListItem(...)` を呼び出してください。
3. 更新されたドキュメントを保存してください。

```java
public static void deleteListItem(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.delListItem("Country", "UK");
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
