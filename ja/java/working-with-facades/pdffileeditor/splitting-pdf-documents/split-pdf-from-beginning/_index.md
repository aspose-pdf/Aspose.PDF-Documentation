---
title: "PDF を先頭から分割"
linktitle: "PDF を先頭から分割"
type: docs
weight: 10
url: /ja/java/split-pdf-from-beginning/
description: "Java で PdfFileEditor ファサードを使用して、PDF を先頭から分割します。"
lastmod: "2026-10-06"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: "Java での PDF の最初のページの新しいドキュメントへの抽出"
Abstract: "Aspose.PDF for Java を使用して、PDF を先頭から分割する方法を学びましょう。Java のサンプルでは PdfFileEditor を使用して、ドキュメントの最初の 3 ページを取得し、別々の PDF として保存します。"
---
## PDF を先頭から分割

Java のサンプルは、ソースドキュメントから最初の 3 ページを抽出します。

### 手順

1. `PdfFileEditor` インスタンスを作成してください。
2. `splitFromFirst` を呼び出し、ソースファイル、保持するページ数、出力ファイルを引数として渡してください。
3. 新しい PDF ドキュメントを保存してください。

```java
public static void splitPdfFromBeginning(Path inputFile, Path outputFile) {
    PdfFileEditor pdfFileEditor = new PdfFileEditor();
    pdfFileEditor.splitFromFirst(inputFile.toString(), 3, outputFile.toString());
}
```
