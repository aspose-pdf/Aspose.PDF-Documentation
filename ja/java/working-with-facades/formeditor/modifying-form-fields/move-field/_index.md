---
title: "フィールドの移動"
linktitle: "フィールドの移動"
type: docs
weight: 30
url: /ja/java/move-field/
description: Aspose.PDF の FormEditor ファサードを使用して、Java で PDF ドキュメント内の既存のフォームフィールドを移動する方法を学びます。
lastmod: "2026-10-06"
TechArticle: true
AlternativeHeadline: "Java での PDF フォームフィールドの新しい位置への移動"
Abstract: "この記事では、既存の PDF をバインドし、フィールドを新しい座標に移動し、Aspose.PDF for Java の FormEditor ファサードを使用して更新されたドキュメントを保存する方法を示します。"
---
## フィールドの移動

1. ソース PDF を `FormEditor` ファサードにバインドしてください。
2. 対象フィールド名と新しい矩形座標を使用して `moveField(...)` を呼び出してください。
3. 更新されたドキュメントを保存してください。

```java
public static void moveField(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.moveField("Country", 200, 600, 280, 620);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
