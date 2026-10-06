---
title: "Java での PDF ページの抽出"
linktitle: PDF ページの抽出
type: docs
weight: 80
url: /ja/java/extract-pages/
description: "Java を使用して、単一または複数の PDF ページを新しいファイルに抽出する方法を学習します。"
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: "Java を使用した PDF ページの新しいドキュメントへの抽出"
Abstract: "このドキュメントでは、Aspose.PDF for Java を使用して PDF ファイルからページを抽出する方法を説明します。単一ページのコピーと、1-based page indexing を使用した複数ページの別ドキュメントへの抽出方法を扱います。"
---
Aspose.PDF for Java を使用すると、選択したページを新しい宛先ドキュメントにコピーできます。

## 単一ページの抽出

ソース PDF から 1 ページを別のドキュメントに保存する必要がある場合は、この例を使用してください。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開き、宛先ドキュメントを作成してください。
1. 対象ページを宛先ページコレクションにコピーしてください。
1. 新しい PDF を保存してください。

```java
public static void extractPage(Path inputFile, Path outputFile) {
    try (Document srcDocument = new Document(inputFile.toString());
         Document dstDocument = new Document()) {
        dstDocument.getPages().add(srcDocument.getPages().get_Item(2));
        dstDocument.save(outputFile.toString());
    }
}
```

## 複数ページの抽出

複数のページを別々の PDF にコピーする必要がある場合は、この例を使用してください。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開き、宛先ドキュメントを作成してください。
1. 選択されたページインデックスを反復処理し、宛先に追加してください。
1. 抽出されたページのドキュメントを保存してください。

```java
public static void extractBunchPages(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString());
         Document anotherDocument = new Document()) {
        Integer[] pages = {2, 3};
        for (Integer pageIndex : pages) {
            anotherDocument.getPages().add(document.getPages().get_Item(pageIndex));
        }
        anotherDocument.save(outputFile.toString());
    }
}
```
