---
title: ブックマークの追加と削除
linktitle: ブックマークの追加と削除
type: docs
weight: 10
url: /java/add-and-delete-bookmark/
description: JavaでPDFドキュメントにブックマークを追加できます。PDFドキュメントからすべてまたは特定のブックマークを削除することが可能です。
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## PDFドキュメントにブックマークを追加する

ブックマークは、[OutlineItemCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/OutlineItemCollection)コレクション内のDocumentオブジェクトの中に保持されており、それ自体が[OutlineCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/OutlineCollection)コレクションの中にあります。

PDFにブックマークを追加するには:

1. [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document)オブジェクトを使用してPDFドキュメントを開きます。
1. ブックマークを作成し、そのプロパティを定義します。
1. [OutlineItemCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/OutlineItemCollection)コレクションをOutlinesコレクションに追加します。

次のコードスニペットは、PDFドキュメントにブックマークを追加する方法を示しています。

```java
package com.aspose.pdf.examples;

import java.io.IOException;

import com.aspose.pdf.*;
import com.aspose.pdf.facades.Bookmark;
import com.aspose.pdf.facades.Bookmarks;
import com.aspose.pdf.facades.PdfBookmarkEditor;

public class ExampleBookmarks {

    private static String _dataDir = "/home/aspose/pdf-examples/Samples/Bookmarks/";

    private static String GetDataDir() {
        String os = System.getProperty("os.name");
        if (os.startsWith("Windows"))
            _dataDir = "C:\\Samples\\Bookmarks\\";
        return _dataDir;
    }

    public static void AddBookmarks() throws IOException {

        Document pdfDocument = new Document(GetDataDir() + "AddBookmark.pdf");

        // ブックマークオブジェクトを作成する
        OutlineItemCollection pdfOutline = new OutlineItemCollection(pdfDocument.getOutlines());
        pdfOutline.setTitle("テストアウトライン");
        pdfOutline.setItalic(true);
        pdfOutline.setBold(true);

        // 目的のページ番号を設定する
        pdfOutline.setAction(new GoToAction(pdfDocument.getPages().get_Item(2)));

        // ドキュメントのアウトラインコレクションにブックマークを追加する
        pdfDocument.getOutlines().add(pdfOutline);

        // 更新されたドキュメントを保存する
        pdfDocument.save(_dataDir + "AddBookmark_out.pdf");
    }
```


## PDFドキュメントに子ブックマークを追加する

ブックマークはネストでき、親と子のブックマークとの階層的な関係を示します。この記事では、PDFに子ブックマーク、つまり第2レベルのブックマークを追加する方法を説明します。

PDFファイルに子ブックマークを追加するには、まず親ブックマークを追加します:

1. ドキュメントを開きます。
2. [OutlineItemCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/OutlineItemCollection) にブックマークを追加し、そのプロパティを定義します。
3. OutlineItemCollection を Document オブジェクトの [OutlineCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/OutlineCollection) コレクションに追加します。

子ブックマークは、上記で説明したように親ブックマークと同様に作成されますが、親ブックマークの Outlines コレクションに追加されます。

以下のコードスニペットは、PDFドキュメントに子ブックマークを追加する方法を示しています。

```java
    public static void AddChildBookmark() {
        // ドキュメントを開く
        Document pdfDocument = new Document(GetDataDir() + "AddChildBookmark.pdf");

        // 親ブックマークオブジェクトを作成する
        OutlineItemCollection pdfOutline = new OutlineItemCollection(pdfDocument.getOutlines());
        pdfOutline.setTitle("Parent Outline");
        pdfOutline.setItalic(true);
        pdfOutline.setBold(true);

        // 子ブックマークオブジェクトを作成する
        OutlineItemCollection pdfChildOutline = new OutlineItemCollection(pdfDocument.getOutlines());
        pdfChildOutline.setTitle("Child Outline");
        pdfChildOutline.setItalic(true);
        pdfChildOutline.setBold(true);

        // 親ブックマークのコレクションに子ブックマークを追加する
        pdfOutline.add(pdfChildOutline);
        // ドキュメントのアウトラインコレクションに親ブックマークを追加する
        pdfDocument.getOutlines().add(pdfOutline);

        // 出力を保存する
        pdfDocument.save(_dataDir + "AddChildBookmark_out.pdf");
    }
```


## PDFドキュメントからすべてのブックマークを削除する

PDF内のすべてのブックマークは、[OutlineCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/OutlineCollection) コレクションに保持されています。この記事では、PDFファイルからすべてのブックマークを削除する方法を説明します。

PDFファイルからすべてのブックマークを削除するには:

1. [OutlineCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/OutlineCollection) コレクションの Delete メソッドを呼び出します。
1. [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) オブジェクトの Save メソッドを使用して、変更されたファイルを保存します。

以下のコードスニペットは、PDFドキュメントからすべてのブックマークを削除する方法を示しています。

```java
    public static void DeleteAllBookmarksFromPDFDocument() {
        // ドキュメントを開く
        Document pdfDocument = new Document(GetDataDir() + "DeleteAllBookmarks.pdf");

        // すべてのブックマークを削除
        pdfDocument.getOutlines().delete();

        // 更新されたファイルを保存
        pdfDocument.save(_dataDir + "DeleteAllBookmarks_out.pdf");
    }
```

## PDFドキュメントから特定のブックマークを削除する

[PDFドキュメントからすべての添付ファイルを削除する](https://docs.aspose.com/pdf/java/working-with-attachments/)では、PDFファイルからすべての添付ファイルを削除する方法を示しました。特定の添付ファイルのみを削除することも可能です。

特定のブックマークをPDFファイルから削除するには:

1. ブックマークのタイトルを[OutlineCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/OutlineCollection)コレクションの[Delete](https://reference.aspose.com/pdf/java/com.aspose.pdf/OutlineCollection#delete--)メソッドにパラメータとして渡します。
1. 次に、DocumentオブジェクトのSaveメソッドを使用して更新されたファイルを保存します。

[Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document)クラスは、[OutlineCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/OutlineCollection)コレクションを提供します。[Delete](https://reference.aspose.com/pdf/java/com.aspose.pdf/OutlineCollection#delete--)メソッドは、メソッドに渡されたタイトルのブックマークを削除します。

次のコードスニペットは、PDFドキュメントから特定のブックマークを削除する方法を示しています。

```java
    public static void DeleteParticularBookmarkPDFDocument() {
        // ドキュメントを開く
        Document pdfDocument = new Document(GetDataDir() + "DeleteParticularBookmark.pdf");

        // タイトルで特定のアウトラインを削除
        pdfDocument.getOutlines().delete("Child Outline");

        // 更新されたファイルを保存
        pdfDocument.save(_dataDir + "DeleteParticularBookmark_out.pdf");
    }
```