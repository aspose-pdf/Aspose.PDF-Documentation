---
title: マルチメディア
linktitle: マルチメディア
type: docs
weight: 70
url: /ja/java/pdfcontenteditor-multimedia/
description: Aspose.PDF の Java PdfContentEditor ファサードで利用可能な現在のマルチメディア機能について学びます。
lastmod: "2026-10-05"
TechArticle: true
AlternativeHeadline: PdfContentEditor を使用した Java のマルチメディア注釈ワークフロー
Abstract: このセクションでは、Java PdfContentEditor のサンプルセットで現在サポートされているマルチメディア関連のワークフローについて説明します。リポジトリには直接的な映画注釈の例が含まれており、サポートされていない音声トピックは明示的なスコープノートとして保持されています。
---
現在の Java `PdfContentEditorExamples` クラスは直接サポートします `addMovieAnnotation(...)`.

## 映画注釈の追加

1. ソース PDF をバインドする `PdfContentEditor` ファサード。
2. 呼び出し `createMovie(...)` アノテーション矩形、動画ファイルのパス、およびページ番号とともに。
3. 更新された PDF ドキュメントを保存してください。

```java
public static void addMovieAnnotation(Path inputFile, Path movieFile, Path outputFile) {
    PdfContentEditor editor = new PdfContentEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.createMovie(new Rectangle(80, 500, 220, 120), movieFile.toString(), 1);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
