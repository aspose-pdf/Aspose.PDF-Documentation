---
title: "既存のPDFドキュメントからテーブルの削除"
linktitle: "テーブルの削除"
description: Javaで既存のPDFドキュメントから1つまたは複数のテーブルを削除する方法を学びます。
lastmod: "2026-10-05"
type: docs
weight: 50
url: /ja/java/removing-tables/
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Javaを使用してPDFファイルから1つまたは複数のテーブルを削除する
Abstract: この記事では、Aspose.PDF for Java を使用して既存の PDF ドキュメントからテーブルを削除する方法を説明します。テーブルの位置を特定するための TableAbsorber を紹介し、単一のテーブルを削除する方法と、ページ上で検出されたすべてのテーブルを削除する方法を示します。
---
使用 `TableAbsorber` 既存のPDFから検出されたテーブルを1つまたは複数削除する必要がある場合。

## 検出されたテーブルを1つ削除する

ページ上で一致した最初のテーブルのみを削除する場合は、この例を使用します。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. 次の方法で対象ページにアクセス [TableAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/tableabsorber/).
1. 検出された最初のテーブルを削除し、ドキュメントを保存してください。

```java
public static void removeOneTable(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TableAbsorber absorber = new TableAbsorber();
        absorber.visit(document.getPages().get_Item(1));
        absorber.remove(absorber.getTableList().get(0));
        document.save(outputFile.toString());
    }
}
```

## ページから検出されたすべてのテーブルの削除

ページ上のすべての一致するテーブルを削除する必要がある場合にこの例を使用します。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. 次の方法で対象ページにアクセス [TableAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/tableabsorber/) 検出されたテーブルをリストにコピーします。
1. 検出された各テーブルを削除し、更新された PDF を保存してください。

```java
public static void removeAllTables(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TableAbsorber absorber = new TableAbsorber();
        absorber.visit(document.getPages().get_Item(1));
        List<AbsorbedTable> tables = new ArrayList<>(absorber.getTableList());
        for (AbsorbedTable table : tables) {
            absorber.remove(table);
        }
        document.save(outputFile.toString());
    }
}
```
