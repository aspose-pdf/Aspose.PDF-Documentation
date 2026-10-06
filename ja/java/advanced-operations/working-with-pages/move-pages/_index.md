---
title: "Java での PDF ページの移動"
linktitle: "PDF ページの移動"
type: docs
weight: 100
url: /ja/java/move-pages/
description: "Java でドキュメント内またはドキュメント間で PDF ページを移動する方法を学びます。"
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: "Java での ドキュメント間の PDF ページの移動"
Abstract: この記事では、Aspose.PDF for Java を使用して PDF のページを移動する方法を説明します。単一ページまたは複数ページを別のドキュメントに移動すること、および同じ PDF 内でページの位置を変更することについて取り上げます。
---
Aspose.PDF for Java を使用すると、ドキュメント間でページを移動したり、同じ PDF 内でページの位置を変更したりできます。

## ページの別のドキュメントへの移動

単一ページを元の PDF から削除し、別のドキュメントに保存する場合にこの例を使用します。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開き、宛先ドキュメントを作成してください。
1. 対象ページを宛先に追加し、ソースから削除してください。
1. 両方のドキュメントを保存してください。

```java
public static void movePageFromOneDocumentToAnother(Path inputFile, Path sourceOutputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString());
         Document anotherDocument = new Document()) {
        anotherDocument.getPages().add(document.getPages().get_Item(2));
        document.getPages().delete(2);
        document.save(sourceOutputFile.toString());
        anotherDocument.save(outputFile.toString());
    }
}
```

## 複数のページの別のドキュメントへの移動

ソース PDF から新しいドキュメントに複数のページを転送する必要がある場合は、この例を使用します。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開き、宛先ドキュメントを作成してください。
1. 選択したページを宛先ドキュメントにコピーしてください。
1. ソースから移動したページを削除し、両方のファイルを保存してください。

```java
public static void moveBunchPagesFromOneDocumentToAnother(Path inputFile, Path sourceOutputFile, Path outputFile) {
    try (Document srcDocument = new Document(inputFile.toString());
         Document dstDocument = new Document()) {
        Integer[] pages = {1, 2};
        for (Integer pageIndex : pages) {
            dstDocument.getPages().add(srcDocument.getPages().get_Item(pageIndex));
        }
        dstDocument.save(outputFile.toString());
        srcDocument.getPages().delete(pages);
        srcDocument.save(sourceOutputFile.toString());
    }
}
```

## 同じドキュメント内でのページの移動

同じ PDF 内でページを新しい位置に再配置する必要がある場合は、この例を使用してください。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. 対象ページを新しい位置に複製し、元のページエントリを削除してください。
1. 再配置されたドキュメントを保存してください。

```java
public static void movePageInNewLocationInSameDocument(Path inputFile, Path outputFile) {
    try (Document srcDocument = new Document(inputFile.toString())) {
        srcDocument.getPages().add(srcDocument.getPages().get_Item(2));
        srcDocument.getPages().delete(2);
        srcDocument.save(outputFile.toString());
    }
}
```
