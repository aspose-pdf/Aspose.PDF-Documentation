---
title: PDF ファイルを 2 つ連結する
linktitle: PDF ファイルを 2 つ連結する
type: docs
weight: 60
url: /ja/java/concatenate-two-files/
description: PdfFileEditor ファサードを使用して、Java で 2 つの PDF ファイルを 1 つのドキュメントにマージします。
lastmod: "2026-10-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java を使用して 2 つの PDF ファイルを単一の出力ドキュメントに連結する
Abstract: Aspose.PDF for Java を使用して 2 つの PDF ファイルを連結する方法を学びます。Java の例では PdfFileEditor と配列ベースの `concatenate` オーバーロードを使用して、2 つのソース文書を 1 つの出力 PDF に結合します。
---
## 2 つの PDF ファイルを連結する

この記事は直接...にマッピングされます `mergePdfDocuments` 例として `PdfFileEditorExamples.java`.

### 手順

1. 作成する `PdfFileEditor` インスタンス。
2. 2つの入力ファイルパスを文字列配列として渡してください。
3. 呼び出す `concatenate` 配列と出力ファイルパスを使用して。
4. 結合された PDF を保存してください。

```java
public static void mergePdfDocuments(Path firstInputFile, Path secondInputFile, Path outputFile) {
    PdfFileEditor pdfEditor = new PdfFileEditor();
    pdfEditor.concatenate(new String[] {firstInputFile.toString(), secondInputFile.toString()}, outputFile.toString());
}
```
