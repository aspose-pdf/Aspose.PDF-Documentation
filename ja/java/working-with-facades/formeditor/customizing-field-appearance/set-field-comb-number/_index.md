---
title: "フィールドのコンブ番号の設定"
linktitle: "フィールドのコンブ番号の設定"
type: docs
weight: 60
url: /ja/java/set-field-comb-number/
description: "Java で Aspose.PDF の FormEditor ファサードを使用して、PDF フォームフィールドのコンブ番号を設定する方法を学びます。"
lastmod: "2026-10-06"
TechArticle: true
AlternativeHeadline: "Java での PDF フォームフィールドのコンブ番号の設定"
Abstract: "この記事では、既存の PDF をバインドし、フィールドのコンブ番号を設定し、Aspose.PDF for Java の FormEditor ファサードを使用して更新されたドキュメントを保存する方法を示します。"
---
## フィールドのコンブ番号の設定

1. ソース PDF を `FormEditor` ファサードにバインドしてください。
2. `setFieldCombNumber(...)` を呼び出して、対象フィールドとコンブ値を設定してください。
3. 更新されたドキュメントを保存してください。

```java
public static void setFieldCombNumber(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.setFieldCombNumber("textCombField", 5);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
