---
title: "Java での PDFファイルの分割"
linktitle: "PDFファイルの分割"
type: docs
weight: 60
url: /ja/java/split-pdf/
description: Aspose.PDFを使用して、JavaでPDFを単一ページのPDFファイルに分割する方法を学びます。
lastmod: "2026-10-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Javaを使用したPDFページの分割
Abstract: この記事では、Aspose.PDFを使用してJavaでPDFドキュメントを個別の単一ページPDFファイルに分割する方法を示します。サンプルではソースドキュメントを開き、ページを順に処理し、各ページごとに新しいドキュメントを作成し、各ページを個別のPDFファイルとして保存します。
---
PDFを個別のファイルに分割することは、各ページをレビュー、保存、または下流処理のためにエクスポートする必要がある場合に便利です。

## ライブ例

[Aspose.PDF Splitter](https://products.aspose.app/pdf/splitter) ブラウザで PDF の分割をテストするための無料オンラインアプリケーションです。

[![Aspose Split PDF](splitter.png)](https://products.aspose.app/pdf/splitter)

この例では [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) PDF ファイルを開き、そのページを反復処理するクラス。各 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/)、新しいドキュメントを作成し、ページを追加して、結果を別々の PDF ファイルとして保存します。

Java で PDF を個々のページファイルに分割するには:

1. ソース PDF を次の方法で開く [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) コンストラクタ。
1. 繰り返し処理する [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) 返されるオブジェクト `document.getPages()`。
1. 新しい空の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 各ページについて。
1. 現在のものを追加 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) 新しいものへ [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 新しいものを保存 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 一意のファイル名で。
1. 両方を閉じる [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 処理が完了したらオブジェクト。

## PDF を単一ページのファイルに分割

以下の Java の例は `SplitDocumentExamples.java` そしてページを保存します `Page_1.pdf`, `Page_2.pdf`、その他。

```java
public static void splitDocument(Path inputFile, Path outputDir) {
    Document document = new Document(inputFile.toString());
    try {
        int pageCount = 1;
        for (Page page : document.getPages()) {
            Document newDocument = new Document();
            try {
                newDocument.getPages().add(page);
                newDocument.save(outputDir.resolve("Page_" + pageCount + ".pdf").toString());
            } finally {
                newDocument.close();
            }
            pageCount++;
        }
    } finally {
        document.close();
    }
}
```
