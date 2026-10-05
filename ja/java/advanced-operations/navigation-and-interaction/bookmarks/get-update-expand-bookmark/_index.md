---
title: JavaでPDFブックマークを取得、更新、展開する
linktitle: ブックマークを取得、更新、展開する
type: docs
weight: 20
url: /ja/java/get-update-and-expand-bookmark/
description: Javaを使用してPDFドキュメント内のブックマークを取得、更新、展開する方法を学びます。
lastmod: "2026-10-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: JavaでPDFファイルのブックマークプロパティを検査し、アウトラインを展開する
Abstract: この記事では、Aspose.PDF for Java を使用してブックマークを読み取り、更新し、展開する方法を説明します。アウトライン項目を反復処理し、PdfBookmarkEditor でブックマークのページ番号を抽出し、子ブックマークを読み取り、ブックマークのタイトルとスタイルを更新し、文書が表示されるときにアウトラインが開くように強制する方法をカバーしています。
---
Aspose.PDF for Java は、ブックマークをドキュメントアウトラインモデルと `PdfBookmarkEditor` ファサード。

## ブックマークのプロパティの取得

ドキュメントのアウトラインでトップレベルのブックマークリストを調査する必要がある場合にこの例を使用してください。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. アウトライン コレクションを反復処理してください。
1. ブックマークのタイトル、スタイル、色の値を読み取り、出力してください。

```java
public static void getBookmarks(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (int i = 1; i <= document.getOutlines().size(); i++) {
            OutlineItemCollection outlineItem = document.getOutlines().get_Item(i);
            System.out.println(outlineItem.getTitle());
            System.out.println(outlineItem.getItalic());
            System.out.println(outlineItem.getBold());
            System.out.println(outlineItem.getColor());
        }
    }
}
```

## ブックマークのページ番号の取得

この例では使用します `PdfBookmarkEditor` ブックマークのタイトル、レベル、ページ番号、アクションを抽出するために。

1. ソース PDF をバインドする [PdfBookmarkEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdfbookmarkeditor/)。
1. ブックマークコレクションを抽出し、それをイテレートしてください。
1. 各ブックマークのレベル、タイトル、ページ番号、およびアクション情報を出力してください。

```java
public static void getBookmarkPageNumber(Path inputFile) {
    PdfBookmarkEditor bookmarkEditor = new PdfBookmarkEditor();
    try {
        bookmarkEditor.bindPdf(inputFile.toString());
        for (Bookmark bookmark : bookmarkEditor.extractBookmarks()) {
            String levelSeparator = "";
            for (int i = 0; i < bookmark.getLevel(); i++) {
                levelSeparator += "----";
            }

            System.out.println(levelSeparator + " Title: " + bookmark.getTitle());
            System.out.println(levelSeparator + " Page Number: " + bookmark.getPageNumber());
            System.out.println(levelSeparator + " Page Action: " + bookmark.getAction());
        }
    } finally {
        bookmarkEditor.close();
    }
}
```

## 子ブックマークの取得

トップレベルとネストされたアウトライン項目の両方を検査する必要がある場合は、この例を使用してください。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. トップレベルのアウトラインを反復処理し、そのプロパティを出力してください。
1. 子ブックマークを検出し、次にそれらを反復処理してプロパティを出力します。

```java
public static void getChildBookmarks(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (int i = 1; i <= document.getOutlines().size(); i++) {
            OutlineItemCollection outlineItem = document.getOutlines().get_Item(i);
            System.out.println(outlineItem.getTitle());
            System.out.println(outlineItem.getItalic());
            System.out.println(outlineItem.getBold());
            System.out.println(outlineItem.getColor());
            int count = outlineItem.size();
            if (count > 0) {
                System.out.println("Child Bookmarks");
                for (int j = 1; j <= outlineItem.size(); j++) {
                    OutlineItemCollection childOutlineItem = outlineItem.get_Item(j);
                    System.out.println(childOutlineItem.getTitle());
                    System.out.println(childOutlineItem.getItalic());
                    System.out.println(childOutlineItem.getBold());
                    System.out.println(childOutlineItem.getColor());
                }
            }
        }
    }
}
```

## ブックマークの更新

既存のブックマークタイトルとスタイルを変更する必要がある場合は、この例を使用します。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. ターゲットのアウトライン項目とその子ブックマークにアクセスします。
1. ブックマークのプロパティを更新し、ドキュメントを保存してください。

```java
public static void updateBookmarks(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        OutlineItemCollection outline = document.getOutlines().get_Item(1);
        OutlineItemCollection childOutline = outline.get_Item(1);
        childOutline.setTitle("Updated Outline");
        childOutline.setItalic(true);
        childOutline.setBold(true);

        document.save(outputFile.toString());
    }
}
```

## ブックマークをデフォルトで展開する

ドキュメントが表示されたときにブックマークパネルが開き、アウトライン項目が展開された状態で表示されるべき場合に、この例を使用します。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. ページモードをアウトライン使用に設定し、各アウトライン項目を開いた状態にマークしてください。
1. 更新されたドキュメントを保存してください。

```java
public static void expandedBookmarks(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.setPageMode(PageMode.UseOutlines);
        for (int i = 1; i <= document.getOutlines().size(); i++) {
            OutlineItemCollection item = document.getOutlines().get_Item(i);
            item.setOpen(true);
        }
        document.save(outputFile.toString());
    }
}
```
