---
title: "複数の PDF ファイルの連結"
linktitle: "複数の PDF ファイルの連結"
type: docs
weight: 20
url: /ja/java/concatenate-pdf-files/
description: "配列ベースの PdfFileEditor concatenate ワークフローを使用して、Java で PDF ファイルを結合します。"
lastmod: "2026-10-06"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: "Java を使用した複数の PDF ファイルの 1 つのドキュメントへの結合"
Abstract: "Aspose.PDF for Java を使用して PDF ファイルを連結する方法を学びます。リポジトリのサンプルでは、2 つの入力を扱う配列ベースの `concatenate` オーバーロードが使用されており、このワークフローはメソッドが文字列配列としてソースパスを受け取るため、より長いファイルリストにも拡張可能です。"
---
## PDF ファイルの連結

Java サンプルでは、配列ベースの `concatenate` オーバーロードに渡すことで 2 つのファイルをマージします。

### 手順

1. `PdfFileEditor` インスタンスを作成してください。
2. 入力 PDF パスで文字列配列を構築してください。
3. 入力配列と出力ファイルパスを指定して `concatenate` を呼び出してください。
4. マージされたドキュメントを保存してください。

```java
public static void mergePdfDocuments(Path firstInputFile, Path secondInputFile, Path outputFile) {
    PdfFileEditor pdfEditor = new PdfFileEditor();
    pdfEditor.concatenate(new String[] {firstInputFile.toString(), secondInputFile.toString()}, outputFile.toString());
}
```

2つ以上のファイルを結合するには、`concatenate` に渡される文字列配列を拡張してください。
