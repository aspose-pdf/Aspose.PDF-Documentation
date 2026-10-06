---
title: "PDF の単一ページへの分割"
linktitle: "PDF の単一ページへの分割"
type: docs
weight: 30
url: /ja/java/split-pdf-into-single-pages/
description: "Java の PdfFileEditor ファサードを使用して、PDF を単一ページの出力ファイルに分割します。"
lastmod: "2026-10-06"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: "Java での PDF の各ページの個別のファイルへのエクスポート"
Abstract: "Aspose.PDF for Java を使用して、PDF を単一ページのファイルに分割する方法を学びます。Java の例では PdfFileEditor を使用し、ファイル名パターンに基づいて各ページを個別の出力 PDF に書き込みます。"
---
## PDF の単一ページへの分割

各ソースページを個別の PDF ファイルに変換する必要がある場合は、このワークフローを使用してください。

### 手順

1. `PdfFileEditor` インスタンスを作成してください。
2. ページ番号プレースホルダー `%NUM%` を含む出力ファイルパターンを準備してください。
3. ソースファイルと出力パターンを指定して `splitToPages` を呼び出してください。
4. 生成された単一ページファイルを保存してください。

```java
public static void splitPdfIntoSinglePages(Path inputFile, Path outputFilePattern) {
    PdfFileEditor pdfFileEditor = new PdfFileEditor();
    pdfFileEditor.splitToPages(inputFile.toString(), outputFilePattern.toString());
}
```
