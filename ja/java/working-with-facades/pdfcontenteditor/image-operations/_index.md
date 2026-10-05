---
title: 画像操作
linktitle: 画像操作
type: docs
weight: 50
url: /ja/java/pdfcontenteditor-image-operations/
description: Aspose.PDF の PdfContentEditor ファサードで利用可能な現在の Java 画像操作カバレッジを学びます。
lastmod: "2026-10-05"
TechArticle: true
AlternativeHeadline: Java における PdfContentEditor を使用した画像編集ワークフロー
Abstract: このセクションでは、Java PdfContentEditor のサンプルセットで現在サポートされている画像関連のワークフローを取り上げます。リポジトリには画像の置換の直接例が含まれており、サポートされていない画像削除のトピックは明示的なスコープノートとして残されています。
---
現在のJava `PdfContentEditorExamples` クラスは直接サポートします `replaceImage(...)`.

## 画像の置換

1. ソース PDF をバインドする `PdfContentEditor` ファサード。
2. 呼び出す `replaceImage(...)` ページ番号、画像インデックス、置換画像パスを使用して。
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
