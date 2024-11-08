---
title: ブックマークの取得、更新、および展開 
linktitle: ブックマークの取得、更新、および展開
type: docs
weight: 20
url: /ja/java/get-update-and-expand-bookmark/
description: この記事では、PDFファイルでブックマークを使用する方法について説明します。Javaライブラリを使用して、PDFファイルからブックマークを取得し、ブックマークのページ番号を取得し、PDFドキュメント内のブックマークを更新し、ドキュメントを表示するときにブックマークを展開することができます。
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## ブックマークを取得する

[Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) オブジェクトの [OutlineCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/OutlineCollection) コレクションには、PDFファイルのすべてのブックマークが含まれています。この記事では、PDFファイルからブックマークを取得する方法と、特定のブックマークがどのページにあるかを取得する方法について説明します。

ブックマークを取得するには、[OutlineCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/OutlineCollection) コレクションをループして、OutlineItemCollection内の各ブックマークを取得します。
 The OutlineItemCollectionは、すべてのブックマークの属性へのアクセスを提供します。次のコードスニペットは、PDFファイルからブックマークを取得する方法を示しています。

```java
    public static void GettingBookmarks() {
        // ドキュメントを開く
        Document pdfDocument = new Document(GetDataDir() + "UpdateBookmarks.pdf");
        // すべてのブックマークをループする
        for (OutlineItemCollection outlineItem : (Iterable<OutlineItemCollection>) pdfDocument.getOutlines()) {
            System.out.println("タイトル :- " + outlineItem.getTitle());
            System.out.println("イタリックか :- " + outlineItem.getItalic());
            System.out.println("ボールドか :- " + outlineItem.getBold());
            System.out.println("色 :- " + outlineItem.getColor());
        }
    }
```

## ブックマークのページ番号を取得する

ブックマークを追加した後に、Bookmarkオブジェクトに関連付けられた目的地のPageNumberを取得することで、それがどのページにあるかを知ることができます。

```java
    public static void GettingBookmarksPageNumber() {
        // PdfBookmarkEditorを作成
        PdfBookmarkEditor bookmarkEditor = new PdfBookmarkEditor();
        // PDFファイルを開く
        bookmarkEditor.bindPdf(GetDataDir() + "UpdateBookmarks.pdf");
        // ブックマークを抽出
        Bookmarks bookmarks = bookmarkEditor.extractBookmarks();
        for (Bookmark bookmark : (Iterable<Bookmark>) bookmarks) {
            String strLevelSeprator = "";
            for (int i = 1; i < bookmark.getLevel(); i++) {
                strLevelSeprator += "---- ";
            }
            System.out.println("タイトル :- " + strLevelSeprator + bookmark.getTitle());
            System.out.println("ページ番号 :- " + strLevelSeprator + bookmark.getPageNumber());
            System.out.println("ページアクション :- " + strLevelSeprator + bookmark.getAction());
        }
    }
```

## PDFドキュメントのブックマークを更新する

PDFファイルのブックマークを更新するには、まずDocumentオブジェクトのOutlineColletionコレクションからブックマークのインデックスを指定して特定のブックマークを取得します。一度ブックマークを[OutlineItemCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/OutlineCollection)オブジェクトに取得したら、そのプロパティを更新し、Saveメソッドを使用して更新されたPDFファイルを保存できます。以下のコードスニペットは、PDFドキュメントのブックマークを更新する方法を示しています。

```java
    public static void UpdateBookmarksInPDFDocument() {
        // ドキュメントを開く
        Document pdfDocument = new Document(GetDataDir() + "UpdateBookmarks.pdf");
        // ブックマークオブジェクトを取得する
        OutlineItemCollection pdfOutline = pdfDocument.getOutlines().get_Item(1);

        // ブックマークオブジェクトを更新する
        pdfOutline.setTitle("Updated Outline");
        pdfOutline.setItalic(true);
        pdfOutline.setBold(true);
        // ターゲットページを2に設定
        pdfOutline.setDestination(new GoToAction(pdfDocument.getPages().get_Item(2)));

        // 出力を保存
        pdfDocument.save(GetDataDir() + "Bookmarkupdated_output.pdf");
    }
```


## PDFドキュメント内の子ブックマークを更新する

子ブックマークを更新するには：

1. 最初に親ブックマークを取得し、適切なインデックス値を使用して子ブックマークを取得することにより、更新したい子ブックマークをPDFファイルから取得します。
1. Saveメソッドを使用して更新されたPDFファイルを保存します。

{{% alert color="primary" %}}

ブックマークのインデックスを指定してDocumentオブジェクトのOutlineCollectionコレクションからブックマークを取得し、この親ブックマークのインデックスを指定して子ブックマークを取得します。

{{% /alert %}}

以下のコードスニペットは、PDFドキュメント内の子ブックマークを更新する方法を示しています。

```java
    public static void UpdateChildBookmarksInPDFDocument() {
        // ドキュメントを開く
        Document pdfDocument = new Document(GetDataDir() + "UpdateBookmarks.pdf");
        // ブックマークオブジェクトを取得
        OutlineItemCollection pdfOutline = pdfDocument.getOutlines().get_Item(1);
        // 子ブックマークオブジェクトを取得
        OutlineItemCollection childOutline = pdfOutline.get_Item(1);

        // ブックマークオブジェクトを更新
        childOutline.setTitle("Updated Outline");
        childOutline.setItalic(true);
        childOutline.setBold(true);
        // ターゲットページを2に設定
        childOutline.setDestination(new GoToAction(pdfDocument.getPages().get_Item(2)));

        // 出力を保存
        pdfDocument.save(GetDataDir() + "Bookmarkupdated_output.pdf");
    }
```


## ドキュメントを表示する際のブックマークの展開

ブックマークは、ドキュメントオブジェクトの [OutlineItemCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/OutlineItemCollection) コレクションに保持されており、これは [OutlineCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/OutlineCollection) コレクション内にあります。しかし、PDFファイルを表示する際にすべてのブックマークを展開した状態にする必要があるかもしれません。

この要件を達成するために、各アウトライン/ブックマーク項目のオープンステータスをオープンとして設定することができます。以下のコードスニペットは、PDFドキュメント内の各ブックマークのオープンステータスを展開として設定する方法を示しています。

```java
    public static void ExpandedBookmarks() {    
        Document doc = new Document(GetDataDir()+"UpdateBookmarks.pdf");
        // ページ表示モードを設定、例えばサムネイルの表示、全画面表示、添付ファイルパネルの表示
        doc.setPageMode(PageMode.UseOutlines);
        // PDFファイル内のブックマークの総数を出力
        System.out.println(doc.getOutlines().size());
        // PDFファイルのアウトラインコレクション内の各アウトライン項目を通過
        for (int counter = 1; counter <= doc.getOutlines().size(); counter++) {
            // アウトライン項目のオープンステータスを設定
            doc.getOutlines().get_Item(counter).setOpen(true);
        }
        // PDFファイルを保存
        doc.save(_dataDir+"Bookmarks_Expanded.pdf");
    }
```