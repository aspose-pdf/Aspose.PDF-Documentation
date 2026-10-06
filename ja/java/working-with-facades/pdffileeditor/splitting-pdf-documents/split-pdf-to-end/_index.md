---
title: PDF を末尾まで分割
linktitle: PDF を末尾まで分割
type: docs
weight: 40
url: /ja/java/split-pdf-to-end/
description: PdfFileEditor ファサードを使用して、Java で選択したページから末尾まで PDF を分割します。
lastmod: "2026-10-06"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: "Java を使用して開始位置から PDF の末尾までページを抽出"
Abstract: "Aspose.PDF for Java を使用して、PDF を末尾まで分割する方法を学習します。Java の例では PdfFileEditor を使用し、ページ 2 からソースドキュメントの末尾までのすべてのページを抽出します。"
---
## PDF を末尾まで分割

この Java サンプルは、ページ 2 からすべてのページを抽出します。

### 手順

1. `PdfFileEditor` インスタンスを作成してください。
2. ソースファイル、開始ページ番号、および出力ファイルを指定して `splitToEnd` を呼び出してください。
3. 結果として得られた PDF ドキュメントを保存してください。

```java
public static void splitPdfToEnd(Path inputFile, Path outputFile) {
    PdfFileEditor pdfFileEditor = new PdfFileEditor();
    pdfFileEditor.splitToEnd(inputFile.toString(), 2, outputFile.toString());
}
```
