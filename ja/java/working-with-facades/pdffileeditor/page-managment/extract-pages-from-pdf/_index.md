---
title: "PDFからページの抽出"
linktitle: "PDFからページの抽出"
type: docs
weight: 30
url: /ja/java/extract-pages-from-pdf/
description: Java の PdfFileEditor ファサードを使用して、PDF から選択したページを抽出します。
lastmod: "2026-10-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java を使用して、選択した PDF ページを新しいドキュメントに抽出
Abstract: Aspose.PDF for Java を使用して PDF からページを抽出する方法を学びます。Java のサンプルでは PdfFileEditor を使用して特定のページ番号を収集し、別の出力 PDF に書き込みます。
---
## PDFからページの抽出

Java のサンプルは、ページ 1、4、3 を新しい PDF ドキュメントに抽出します。

### 手順

1. 作成 `PdfFileEditor` インスタンス。
2. 抽出するページ番号を定義してください。
3. 呼び出す `extract` ソースファイル、ページ配列、および出力ファイルとともに。
4. 抽出したページを新しい PDF として保存してください。

### Java の例

```java
public static void extractPagesFromPdf(Path inputFile, Path outputFile) {
    PdfFileEditor pdfEditor = new PdfFileEditor();
    pdfEditor.extract(inputFile.toString(), new int[] {1, 4, 3}, outputFile.toString());
}
```
