---
title: "Java での PDF ページの削除"
linktitle: "PDF ページの削除"
type: docs
weight: 80
url: /ja/java/delete-pages/
description: "Java で PDF ファイルからページを削除する方法を学びます。"
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: "Java での 1 つまたは複数の PDF ページの削除"
Abstract: この記事では、Aspose.PDF for Java を使用して PDF ファイルからページを削除する方法を説明します。単一ページの削除と、ページコレクション API を使った複数ページの一括削除について取り上げます。
---
PDF から 1 つまたは複数のページを削除する必要がある場合は、ドキュメントのページコレクションを使用してください。

## 単一ページの削除

インデックスで 1 ページを削除する必要がある場合は、この例を使用してください。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. ページコレクションから対象ページを削除してください。
1. 更新されたドキュメントを保存してください。

```java
public static void deletePage(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getPages().delete(2);
        document.save(outputFile.toString());
    }
}
```

## 複数ページの削除

この例は、複数のページを一度の操作で削除する必要がある場合に使用します。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. ページコレクションから削除するページインデックスを渡してください。
1. 変更された PDF を保存してください。

```java
public static void deleteBunchPages(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getPages().delete(new Integer[]{2, 3, 4});
        document.save(outputFile.toString());
    }
}
```
