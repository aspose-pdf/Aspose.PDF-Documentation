---
title: PDF を単一ページに分割する
linktitle: PDF を単一ページに分割する
type: docs
weight: 30
url: /ja/java/split-pdf-into-single-pages/
description: Java の PdfFileEditor ファサードで PDF を単一ページの出力ファイルに分割する。
lastmod: "2026-10-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java で PDF の各ページを個別のファイルにエクスポートする
Abstract: Aspose.PDF for Java を使用して PDF を単一ページのファイルに分割する方法を学びます。Java の例では PdfFileEditor を使用し、ファイル名パターンに基づいて各ページを個別の出力 PDF に書き込みます。
---
## PDF を単一ページに分割する

各ソースページをそれぞれ PDF ファイルにする必要がある場合は、この workflow を使用してください。

### 手順

1. 作成 `PdfFileEditor` インスタンス。
2. ページ プレースホルダー を含む 出力 ファイル パターン を 準備します `%NUM%`.
3. 呼び出し `splitToPages` ソースファイルと出力パターンで。
4. 生成された単一ページファイルを保存してください。

```java
public static void splitPdfIntoSinglePages(Path inputFile, Path outputFilePattern) {
    PdfFileEditor pdfFileEditor = new PdfFileEditor();
    pdfFileEditor.splitToPages(inputFile.toString(), outputFilePattern.toString());
}
```
