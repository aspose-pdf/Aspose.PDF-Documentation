---
title: "Java での PDFページの追加"
linktitle: ページの追加
type: docs
weight: 10
url: /ja/java/add-pages/
description: JavaでPDFドキュメントにページを追加または挿入する方法を学びます。
lastmod: "2026-10-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: JavaでPDFページを追加または挿入する
Abstract: このドキュメントでは、Aspose.PDF for Java を使用して PDF ファイルにページを追加する方法を説明します。特定の位置に空白ページを挿入すること、ドキュメントの末尾にページを追加すること、別の PDF からページをインポートすることについて解説します。
---
Aspose.PDF for Java を使用すると、空白ページを挿入したり、別のドキュメントからページをインポートしたりできます。

## 特定の位置に空白ページの挿入

既存の PDF の途中に空白ページを追加する必要がある場合は、このサンプルをご利用ください。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. ページコレクション内の対象位置に新しいページを挿入してください。
1. 更新されたドキュメントを保存してください。

```java
public static void insertEmptyPage(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getPages().insert(2);
        document.save(outputFile.toString());
    }
}
```

## 末尾に空白ページの追加

ドキュメントを新しい空白の最終ページで拡張する必要がある場合は、この例を使用してください。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. ページコレクションの末尾に新しいページを追加してください。
1. 変更された PDF を保存してください。

```java
public static void addEmptyPageToEnd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getPages().add();
        document.save(outputFile.toString());
    }
}
```

## 別のドキュメントからページの追加

PDF を 1 つから別の PDF にページをインポートしたいときは、この例を使用してください。

1. 宛先を作成します [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) そして、ソースドキュメントを開いてください。
1. 必要な宛先コンテンツを追加し、ソース PDF から対象ページをインポートしてください。
1. 結果のドキュメントを保存してください。

```java
public static void addPageFromAnotherDocument(Path inputFile, Path outputFile) {
    try (Document document = new Document();
         Document anotherDocument = new Document(inputFile.toString())) {
        document.getPages().add().getParagraphs().add(new TextFragment("This is first page!"));
        document.getPages().add(anotherDocument.getPages().get_Item(1));
        document.save(outputFile.toString());
    }
}
```
