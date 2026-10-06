---
title: "フィールドの削除"
linktitle: "フィールドの削除"
type: docs
weight: 40
url: /ja/java/remove-field/
description: "Java で Aspose.PDF の FormEditor ファサードを使用して、PDF ドキュメントから既存のフォームフィールドを削除する方法を学びます。"
lastmod: "2026-10-06"
TechArticle: true
AlternativeHeadline: "Java での PDF フォームフィールドの削除"
Abstract: "この記事では、既存の PDF をバインドし、指定されたフィールドを削除し、Aspose.PDF for Java の FormEditor ファサードを使用して更新されたドキュメントを保存する方法を示します。"
---
## フィールドの削除

1. ソース PDF を `FormEditor` ファサードにバインドしてください。
2. `removeField(...)` を対象フィールド名で呼び出してください。
3. 更新されたドキュメントを保存してください。

```java
public static void removeField(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.removeField("Country");
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
