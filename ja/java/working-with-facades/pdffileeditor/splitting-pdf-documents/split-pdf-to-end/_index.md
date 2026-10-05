---
title: PDF を末尾まで分割
linktitle: PDF を末尾まで分割
type: docs
weight: 40
url: /ja/java/split-pdf-to-end/
description: PdfFileEditor ファサードを使用して、Java で選択したページから末尾まで PDF を分割します。
lastmod: "2026-10-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java を使用して、開始位置から PDF の末尾までページを抽出します
Abstract: Aspose.PDF for Java を使用して、PDF を末尾まで分割する方法を学びます。Java の例では PdfFileEditor を使用し、ページ 2 からソース ドキュメントの末尾までのすべてのページを抽出します。
---
## PDF を末尾まで分割

この Java サンプルは、ページ 2 からすべてのページを抽出します。

### 手順

1. 作成 `PdfFileEditor` インスタンス。
2. 呼び出す `splitToEnd` ソースファイル、開始ページ番号、および出力ファイルと共に。
3. 結果として得られた PDF ドキュメントを保存してください。

```java
public static void splitPdfToEnd(Path inputFile, Path outputFile) {
    PdfFileEditor pdfFileEditor = new PdfFileEditor();
    pdfFileEditor.splitToEnd(inputFile.toString(), 2, outputFile.toString());
}
```
