---
title: "Java での PDF ファイルの分割"
linktitle: "PDF ファイルの分割"
type: docs
weight: 60
url: /ja/java/split-pdf/
description: "Aspose.PDF を使用して、Java で PDF を単一ページの PDF ファイルに分割する方法を学びます。"
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: "Java を使用した PDF ページの分割"
Abstract: "この記事では、Aspose.PDF を使用して Java で PDF ドキュメントを個別の単一ページ PDF ファイルに分割する方法を示します。サンプルでは、ソースドキュメントを開き、ページを順に処理して各ページごとに新しいドキュメントを作成し、各ページを個別の PDF ファイルとして保存します。"
---
PDF を個別のファイルに分割することは、各ページをレビュー、保存、または下流処理のためにエクスポートする必要がある場合に便利です。

## ライブ例

[Aspose.PDF Splitter](https://products.aspose.app/pdf/splitter) は、ブラウザで PDF の分割をテストするための無料オンラインアプリケーションです。

[![Aspose Split PDF](splitter.png)](https://products.aspose.app/pdf/splitter)

この例では [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) クラスを使用して PDF ファイルを開き、そのページを反復処理します。各 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) に対して、新しいドキュメントを作成し、ページを追加して、結果を別々の PDF ファイルとして保存します。

Java で PDF を個々のページファイルに分割する手順は以下の通りです。

1. ソース PDF を [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) コンストラクタで開いてください。
1. `document.getPages()` で返される [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) オブジェクトを繰り返し処理してください。
1. 各ページについて、新しい空の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を作成してください。
1. 現在の [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) を新しい [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) に追加してください。
1. 新しい [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を一意のファイル名で保存してください。
1. 処理が完了したら、両方の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) オブジェクトを閉じてください。

## PDF を単一ページのファイルに分割

以下の Java の例は `SplitDocumentExamples.java` に基づいており、ページを `Page_1.pdf`、`Page_2.pdf` などとして保存します。

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
