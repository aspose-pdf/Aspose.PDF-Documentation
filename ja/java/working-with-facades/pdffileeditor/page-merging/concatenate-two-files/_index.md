---
title: "PDF ファイルを 2 つ連結"
linktitle: "PDF ファイルを 2 つ連結"
type: docs
weight: 60
url: /ja/java/concatenate-two-files/
description: PdfFileEditor ファサードを使用して、Java で 2 つの PDF ファイルを 1 つのドキュメントにマージします。
lastmod: "2026-10-06"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: "Java を使用して 2 つの PDF ファイルの単一の出力ドキュメントへの連結"
Abstract: Aspose.PDF for Java を使用して 2 つの PDF ファイルを連結する方法を学びます。Java の例では PdfFileEditor と配列ベースの `concatenate` オーバーロードを使用して、2 つのソース文書を 1 つの出力 PDF に結合します。
---
## 2 つの PDF ファイルの連結

この記事は、`PdfFileEditorExamples.java` 内の `mergePdfDocuments` 例に直接対応しています。

### 手順

1. `PdfFileEditor` インスタンスを作成してください。
2. 2つの入力ファイルパスを文字列配列として渡してください。
3. `concatenate` を配列と出力ファイルパスとともに呼び出してください。
4. 結合された PDF を保存してください。

```java
public static void mergePdfDocuments(Path firstInputFile, Path secondInputFile, Path outputFile) {
    PdfFileEditor pdfEditor = new PdfFileEditor();
    pdfEditor.concatenate(new String[] {firstInputFile.toString(), secondInputFile.toString()}, outputFile.toString());
}
```
