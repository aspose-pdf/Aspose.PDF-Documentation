---
title: "Java での PDFポートフォリオの作成"
linktitle: ポートフォリオ
type: docs
weight: 20
url: /ja/java/portfolio/
description: Aspose.PDFを使用して、JavaでPDFポートフォリオを作成および管理する方法を学びます。
lastmod: "2026-10-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Javaで埋め込みファイル付きのPDFポートフォリオを構築および編集する
Abstract: この記事では、Aspose.PDF for Javaを使用してPDFポートフォリオを作成および管理する方法を説明します。ドキュメントでコレクションを有効にする方法、ポートフォリオに複数のファイルタイプを追加する方法、既存のPDFポートフォリオからすべてのコレクション項目を削除する方法を学びます。
---
PDFポートフォリオは、単一のPDFコンテナ内に複数のファイルをまとめることができ、各ファイルを元の形式のまま保持します。

## PDFポートフォリオの作成

複数のファイルをPDFポートフォリオコレクションにまとめる必要がある場合は、この例を使用してください。

1. 新しいPDFを作成する [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) それを有効にする [Collection](https://reference.aspose.com/pdf/java/com.aspose.pdf/collection/)。
1. 作成 [FileSpecification](https://reference.aspose.com/pdf/java/com.aspose.pdf/filespecification/) 各入力ファイルごとのオブジェクトを作成し、説明を設定してください。
1. ファイルをポートフォリオコレクションに追加し、出力ドキュメントを保存してください。

```java
public static void createPdfPortfolio(Path[] inputFiles, Path outputFile) {
    try (Document document = new Document()) {
        document.setCollection(new Collection());

        FileSpecification excel = new FileSpecification(inputFiles[0].toString());
        FileSpecification word = new FileSpecification(inputFiles[1].toString());
        FileSpecification image = new FileSpecification(inputFiles[2].toString());

        excel.setDescription("Excel File");
        word.setDescription("Word File");
        image.setDescription("Image File");

        document.getCollection().add(excel);
        document.getCollection().add(word);
        document.getCollection().add(image);

        document.save(outputFile.toString());
    }
}
```

## PDF ポートフォリオからファイルの削除

既存の PDF ポートフォリオ コレクションをクリアする必要がある場合に、この例を使用してください。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. ドキュメント コレクション エントリを削除してください。
1. クリーンアップされた出力ドキュメントを保存してください。

```java
public static void removeFilesFromPdfPortfolio(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getCollection().delete();
        document.save(outputFile.toString());
    }
}
```
