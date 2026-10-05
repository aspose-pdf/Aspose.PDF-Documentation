---
title: "プログラムで PDF ドキュメントの作成"
linktitle: "PDF の作成"
type: docs
weight: 10
url: /ja/java/create-document/
description: Aspose.PDF を使用して Java で最初から PDF ドキュメントを作成する方法を学びます。
lastmod: "2026-10-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Aspose.PDF for Java を使用した PDF ファイルの生成
Abstract: この記事では、Aspose.PDF を使用して Java で PDF ファイルを作成する方法を示します。サンプルでは新しい Document オブジェクトを作成し、ページを追加し、サンプルテキストを含む TextFragment を挿入し、結果を PDF ファイルとして保存します。
---
コードで PDF ファイルを作成することは、レポート、請求書、生成されたビジネス文書に対する一般的な要件です。Aspose.PDF for Java は、最初からドキュメントを構築する直接的な方法を提供します。

## JavaでPDFファイルを作成する方法

PDFドキュメントをプログラムで作成するには:

1. [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) オブジェクトを作成してください。
1. 追加する [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) ドキュメントへ。
1. 追加する [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/) ページの段落へ。
1. 保存する [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 出力ファイルへ。

## シンプルな PDF ドキュメントの作成

以下のJava例は基づいています `CreatePdfDocumentExamples.java`.

```java
public static void createNewDocument(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        page.getParagraphs().add(new TextFragment("Hello World!"));
        document.save(outputFile.toString());
    }
}
```
