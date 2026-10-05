---
title: 単一から複数へ
linktitle: 単一から複数へ
type: docs
weight: 60
url: /ja/java/single-to-multiple/
description: Java で Aspose.PDF の FormEditor ファサードを使用して、PDF ドキュメント内の単一行テキスト フィールドを複数行フィールドに変換する方法を学びます。
lastmod: "2026-10-06"
TechArticle: true
AlternativeHeadline: "Java での 単一行 PDF フィールドの複数行への変換"
Abstract: この記事では、既存の PDF をバインドし、単一行フィールドを複数行フィールドに変換し、Aspose.PDF for Java の FormEditor ファサードを使用して更新されたドキュメントを保存する方法を示します。
---
## 単一行フィールドの複数行への変換

1. ソース PDF を `FormEditor` ファサードにバインドしてください。
2. `single2Multiple(...)` を対象フィールド名で呼び出してください。
3. 更新されたドキュメントを保存してください。

```java
public static void singleToMultiple(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.single2Multiple("City");
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
