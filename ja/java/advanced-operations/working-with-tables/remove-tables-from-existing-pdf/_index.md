---
title: "既存の PDF ドキュメントからテーブルの削除"
linktitle: "テーブルの削除"
description: "Java を使用して、既存の PDF ドキュメントから 1 つまたは複数のテーブルを削除する方法を学習します。"
lastmod: "2026-10-06"
type: docs
weight: 50
url: /ja/java/removing-tables/
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: "Java を使用した PDF ファイルからの 1 つまたは複数のテーブルの削除"
Abstract: この記事では、Aspose.PDF for Java を使用して既存の PDF ドキュメントからテーブルを削除する方法を説明します。テーブルの位置を特定するための TableAbsorber を紹介し、単一のテーブルを削除する方法と、ページ上で検出されたすべてのテーブルを削除する方法を示します。
---
既存の PDF から検出されたテーブルを 1 つまたは複数削除する必要がある場合は、`TableAbsorber` を使用してください。

## 検出されたテーブルを 1 つ削除

ページ上で一致した最初のテーブルのみを削除する場合は、この例を使用してください。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. [TableAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/tableabsorber/) を使用して対象ページにアクセスしてください。
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

ページ上のすべての一致するテーブルを削除する必要がある場合に、この例を使用してください。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. 対象ページに [TableAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/tableabsorber/) を適用し、検出されたテーブルをリストにコピーしてください。
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
