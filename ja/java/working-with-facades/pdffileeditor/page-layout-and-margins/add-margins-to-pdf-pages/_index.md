---
title: "PDFページへの余白の追加"
linktitle: "PDFページへの余白の追加"
type: docs
weight: 10
url: /ja/java/add-margins-to-pdf-pages/
description: PdfFileEditorファサードを使用して、Javaで選択したPDFページに余白を追加します。
lastmod: "2026-10-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: JavaでPDFドキュメントの特定のページに余白を追加する
Abstract: Aspose.PDF for Javaを使用して選択ページに余白を追加する方法を学びます。JavaのサンプルはPdfFileEditorを使用して個々のページ番号を指定し、上下左右の余白を同等に適用します。
---
## PDFページへの余白の追加

このJavaサンプルは、ソース文書の1ページ目と3ページ目に36ポイントの余白を追加します。

### 手順

1. 作成する `PdfFileEditor` インスタンス。
2. 新しい余白を設定するページ番号を選択してください。
3. 呼び出す `addMargins` 入力ファイル、出力ファイル、ページリスト、および余白の値を使用して。
4. 更新された PDF を保存してください。

### Java の例

```java
public static void addMarginsToPdfPages(Path inputFile, Path outputFile) {
    PdfFileEditor pdfEditor = new PdfFileEditor();
    pdfEditor.addMargins(inputFile.toString(), outputFile.toString(), new int[] {1, 3}, 36, 36, 36, 36);
}
```
