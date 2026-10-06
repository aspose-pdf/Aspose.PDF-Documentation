---
title: "PDF ページへの余白の追加"
linktitle: "PDF ページへの余白の追加"
type: docs
weight: 10
url: /ja/java/add-margins-to-pdf-pages/
description: "PdfFileEditor ファサードを使用して、Java で選択した PDF ページに余白を追加します。"
lastmod: "2026-10-06"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: "Java での PDF ドキュメントの特定のページに余白の追加"
Abstract: "Aspose.PDF for Java を使用して選択したページに余白を追加する方法を学習してください。Java のサンプルでは、PdfFileEditor を使用して個々のページ番号を指定し、上下左右の余白を等しく適用します。"
---
## PDF ページへの余白の追加

この Java サンプルは、ソース文書の 1 ページ目と 3 ページ目に 36 ポイントの余白を追加します。

### 手順

1. `PdfFileEditor` インスタンスを作成してください。
2. 新しい余白を設定するページ番号を選択してください。
3. 入力ファイル、出力ファイル、ページリスト、および余白の値を指定して `addMargins` を呼び出してください。
4. 更新された PDF を保存してください。

### Java の例

```java
public static void addMarginsToPdfPages(Path inputFile, Path outputFile) {
    PdfFileEditor pdfEditor = new PdfFileEditor();
    pdfEditor.addMargins(inputFile.toString(), outputFile.toString(), new int[] {1, 3}, 36, 36, 36, 36);
}
```
