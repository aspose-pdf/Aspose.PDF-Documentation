---
title: "プログラムによる PDF ドキュメントの作成"
linktitle: "PDF の作成"
type: docs
weight: 10
url: /ja/java/create-document/
description: Aspose.PDF を使用して Java で最初から PDF ドキュメントを作成する方法を学びます。
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Aspose.PDF for Java を使用した PDF ファイルの生成
Abstract: この記事では、Aspose.PDF を使用して Java で PDF ファイルを作成する方法を示します。サンプルでは新しい Document オブジェクトを作成し、ページを追加し、サンプルテキストを含む TextFragment を挿入し、結果を PDF ファイルとして保存します。
---
コードで PDF ファイルを作成することは、レポート、請求書、生成されたビジネス文書に対する一般的な要件です。Aspose.PDF for Java は、最初からドキュメントを構築する直接的な方法を提供します。

## Java で PDF ファイルを作成する方法

PDF ドキュメントをプログラムで作成するには、次の手順を実行してください。

1. [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) オブジェクトを作成してください。
1. [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) をドキュメントに追加してください。
1. ページの段落コレクションに [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/) を追加してください。
1. [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を出力ファイルに保存してください。

## シンプルな PDF ドキュメントの作成

以下の Java の例は `CreatePdfDocumentExamples.java` を基にしています。

```java
public static void createNewDocument(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        page.getParagraphs().add(new TextFragment("Hello World!"));
        document.save(outputFile.toString());
    }
}
```
