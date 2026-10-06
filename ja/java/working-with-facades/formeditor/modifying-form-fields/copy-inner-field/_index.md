---
title: "内部フィールドのコピー"
linktitle: "内部フィールドのコピー"
type: docs
weight: 70
url: /ja/java/copy-inner-field/
description: Aspose.PDF の FormEditor ファサードを使用して、Java で同じ PDF ドキュメント内のフォームフィールドを新しい位置にコピーする方法を学びます。
lastmod: "2026-10-06"
TechArticle: true
AlternativeHeadline: Java で同じドキュメント内の PDF フォームフィールドをコピー
Abstract: この記事では、既存の PDF をバインドし、フィールドを別のページと位置に複製し、Aspose.PDF for Java の FormEditor ファサードを使用して更新されたドキュメントを保存する方法を示します。
---
## 同じ PDF 内のフィールドのコピー

1. ソース PDF を `FormEditor` ファサードにバインドしてください。
2. ソースフィールド名、新しいフィールド名、ページ、座標を指定して `copyInnerField(...)` を呼び出してください。
3. 更新されたドキュメントを保存してください。

```java
public static void copyInnerField(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.copyInnerField("First Name", "First Name Copy", 2, 200, 600);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
