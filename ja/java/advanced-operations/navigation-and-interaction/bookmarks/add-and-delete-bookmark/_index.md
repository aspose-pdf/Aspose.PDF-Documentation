---
title: JavaでPDFブックマークを追加および削除する
linktitle: ブックマークを追加および削除する
type: docs
weight: 10
url: /ja/java/add-and-delete-bookmark/
description: Javaを使用してPDFドキュメントでブックマークを追加および削除する方法を学びます。
lastmod: "2026-10-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: JavaでPDFドキュメントのブックマークを追加または削除する
Abstract: この記事では、Aspose.PDF for Java を使用してブックマークの作成と削除を行う方法を示します。例では、トップレベルのブックマークを追加し、子ブックマークの階層を作成し、すべてのブックマークを削除し、タイトルで特定のブックマークを削除する方法をデモしています。
---
ドキュメントアウトラインコレクションを使用して、ブックマークをプログラムで管理します。

## トップレベルのブックマークの追加

ドキュメントに単一のトップレベルアウトラインエントリを含める必要がある場合は、この例を使用します。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. [OutlineItemCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/outlineitemcollection/) を作成し、そのタイトル、スタイル、およびアクションを設定してください。
1. ブックマークをドキュメントのアウトラインに追加し、ファイルを保存してください。

```java
public static void addBookmark(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        OutlineItemCollection pdfOutline = new OutlineItemCollection(document.getOutlines());
        pdfOutline.setTitle("Test Outline");
        pdfOutline.setItalic(true);
        pdfOutline.setBold(true);
        pdfOutline.setAction(new GoToAction(document.getPages().get_Item(1)));

        document.getOutlines().add(pdfOutline);
        document.save(outputFile.toString());
    }
}
```

## 子ブックマークの追加

この例では、親ブックマークを作成し、その下に子ブックマークをネストします。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. 親と子を作成 [OutlineItemCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/outlineitemcollection/) オブジェクト。
1. 子を親に追加し、親をアウトラインコレクションに追加して、ドキュメントを保存してください。

```java
public static void addChildBookmark(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        OutlineItemCollection pdfOutline = new OutlineItemCollection(document.getOutlines());
        pdfOutline.setTitle("Parent Outline");
        pdfOutline.setItalic(true);
        pdfOutline.setBold(true);

        OutlineItemCollection pdfChildOutline = new OutlineItemCollection(document.getOutlines());
        pdfChildOutline.setTitle("Child Outline");
        pdfChildOutline.setItalic(true);
        pdfChildOutline.setBold(true);

        pdfOutline.add(pdfChildOutline);
        document.getOutlines().add(pdfOutline);
        document.save(outputFile.toString());
    }
}
```

## すべてのブックマークの削除

ドキュメントからアウトラインコレクション全体を削除する必要がある場合にこの方法を使用します。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. 完全なアウトラインコレクションを削除してください。
1. クリーンアップされた出力ファイルを保存してください。

```java
public static void deleteBookmarks(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getOutlines().delete();
        document.save(outputFile.toString());
    }
}
```

## 特定のブックマークの削除

名前付きブックマークが1つだけ削除したいが、アウトラインツリー全体をクリアしない場合にこの例を使用します。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. アウトライン コレクションからタイトルでブックマークを削除してください。
1. 更新されたドキュメントを保存してください。

```java
public static void deleteBookmark(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getOutlines().delete("Child Outline");
        document.save(outputFile.toString());
    }
}
```
