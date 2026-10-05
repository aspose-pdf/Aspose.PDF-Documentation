---
title: "ラバースタンプの追加"
linktitle: "ラバースタンプの追加"
type: docs
weight: 10
url: /ja/java/add-rubber-stamp/
description: Aspose.PDF の PdfContentEditor ファサードを使用して、Java で PDF ドキュメントにラバースタンプ アノテーションを追加する方法を学びます。
lastmod: "2026-10-05"
TechArticle: true
AlternativeHeadline: Java で PDF にラバースタンプを追加
Abstract: この記事では、PDF をバインドし、ラベル テキストとカラーを指定したラバースタンプ アノテーションを作成し、Aspose.PDF for Java の PdfContentEditor ファサードを使用して更新されたドキュメントを保存する方法を示します。
---
## ラバースタンプの追加

1. ソース PDF をバインドする `PdfContentEditor` ファサード。
2. 呼び出す `createRubberStamp(...)` ページ番号、矩形、タイトル、内容、そして色を使用して。
3. 更新された PDF ドキュメントを保存してください。

```java
public static void addRubberStamp(Path inputFile, Path outputFile) {
    PdfContentEditor editor = new PdfContentEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.createRubberStamp(1, new Rectangle(120, 450, 180, 60), "Approved", "Approved by reviewer", Color.GREEN);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
