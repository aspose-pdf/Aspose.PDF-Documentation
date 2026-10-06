---
title: 画像操作
linktitle: 画像操作
type: docs
weight: 50
url: /ja/java/pdfcontenteditor-image-operations/
description: "Aspose.PDF の PdfContentEditor ファサードで利用可能な現在の Java 画像操作の機能について学びます。"
lastmod: "2026-10-06"
TechArticle: true
AlternativeHeadline: Java における PdfContentEditor を使用した画像編集ワークフロー
Abstract: "このセクションでは、Java PdfContentEditor のサンプルセットで現在サポートされている画像関連のワークフローを説明します。リポジトリには画像の置換の直接的な例が含まれていますが、サポートされていない画像削除のトピックは明示的なスコープノートとして残されています。"
---
現在の Java `PdfContentEditorExamples` クラスは `replaceImage(...)` を直接サポートしています。

## 画像の置換

1. ソース PDF を `PdfContentEditor` ファサードにバインドしてください。
2. ページ番号、画像インデックス、および置換画像のパスを指定して `replaceImage(...)` を呼び出してください。
3. 更新された PDF ドキュメントを保存してください。

```java
public static void replaceImage(Path inputFile, Path imageFile, Path outputFile) {
    PdfContentEditor editor = new PdfContentEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.replaceImage(1, 1, imageFile.toString());
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
