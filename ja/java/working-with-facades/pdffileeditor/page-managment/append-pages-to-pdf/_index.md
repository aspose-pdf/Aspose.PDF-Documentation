---
title: "PDF にページの追加"
linktitle: "PDF にページの追加"
type: docs
weight: 10
url: /ja/java/append-pages-to-pdf/
description: Java の PdfFileEditor ファサードを使用して、ある PDF から別の PDF にページを追加します。
lastmod: "2026-10-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java を使用して、ある PDF 文書から別の PDF にページ範囲を追加する
Abstract: Aspose.PDF for Java を使用して PDF にページを追加する方法を学びます。Java のサンプルでは PdfFileEditor を使用して、別の文書から選択したページ範囲を現在の PDF の末尾に追加します。
---
## PDF にページの追加

Java のサンプルは、2 番目の PDF のページ 1 を最初のドキュメントの末尾に追加します。

### 手順

1. 作成 `PdfFileEditor` インスタンス。
2. パスを渡してメイン入力PDFをバインドします `append`。
3. 二次ソースファイルリストと追加するページ範囲を指定します。
4. 結合結果を出力ファイルに保存してください。

### Java の例

```java
public static void appendPagesToPdf(Path inputFile, Path sampleFile, Path outputFile) {
    PdfFileEditor pdfEditor = new PdfFileEditor();
    pdfEditor.append(inputFile.toString(), new String[] {sampleFile.toString()}, 1, 1, outputFile.toString());
}
```
