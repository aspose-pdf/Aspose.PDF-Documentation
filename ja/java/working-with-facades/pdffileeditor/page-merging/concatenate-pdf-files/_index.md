---
title: 複数の PDF ファイルを連結する
linktitle: 複数の PDF ファイルを連結する
type: docs
weight: 20
url: /ja/java/concatenate-pdf-files/
description: 配列ベースの PdfFileEditor concatenate ワークフローを使用して Java で PDF ファイルを結合します。
lastmod: "2026-10-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java を使用して複数の PDF ファイルを 1 つのドキュメントに結合する
Abstract: Aspose.PDF for Java を使用して PDF ファイルを連結する方法を学びます。リポジトリのサンプルは、2 つの入力を持つ配列ベースの `concatenate` オーバーロードを使用しており、同じワークフローはメソッドが文字列配列のソースパスを受け入れるため、より長いファイルリストにも拡張できます。
---
## PDF ファイルを連結する

Java のサンプルは、配列ベースに渡すことで 2 つのファイルをマージします。 `concatenate` オーバーロード。

### 手順

1. 作成 `PdfFileEditor` インスタンス。
2. 入力 PDF パスで文字列配列を構築してください。
3. 呼び出す `concatenate` 入力配列と出力ファイルパスで
4. マージされたドキュメントを保存してください。

```java
public static void mergePdfDocuments(Path firstInputFile, Path secondInputFile, Path outputFile) {
    PdfFileEditor pdfEditor = new PdfFileEditor();
    pdfEditor.concatenate(new String[] {firstInputFile.toString(), secondInputFile.toString()}, outputFile.toString());
}
```

2つ以上のファイルを結合するには、渡される文字列配列を拡張します `concatenate`.
