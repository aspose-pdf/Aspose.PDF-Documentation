---
title: "Java での PDF ブックマークの追加および削除"
linktitle: "ブックマークの追加と削除"
type: docs
weight: 10
url: /ja/java/add-and-delete-bookmark/
description: "Java を使用して PDF ドキュメントでブックマークを追加および削除する方法を学びます。"
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: "Java での PDF ドキュメントのブックマークを追加または削除"
Abstract: "この記事では、Aspose.PDF for Java を使用してブックマークの作成と削除を行う方法を示します。例では、トップレベルのブックマークの追加、子ブックマークの階層の作成、すべてのブックマークの削除、およびタイトルで特定のブックマークを削除する方法をデモしています。"
---
ドキュメントのアウトライン コレクションを使用して、ブックマークをプログラムで管理します。

## トップレベルのブックマークの追加

ドキュメントに単一のトップレベルアウトライン エントリを含める必要がある場合は、この例を使用してください。

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
1. 親と子の [OutlineItemCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/outlineitemcollection/) オブジェクトを作成してください。
1. 子を親に追加し、親をアウトライン コレクションに追加して、ドキュメントを保存してください。

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

ドキュメントからアウトライン コレクション全体を削除する必要がある場合にこの方法を使用します。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. 完全なアウトライン コレクションを削除してください。
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

名前付きブックマークを1つだけ削除し、アウトライン ツリー全体をクリアしない場合にこの例を使用します。

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
