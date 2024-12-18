---
title: 既存のPDFファイルにブックマークアクションを追加する
type: docs
weight: 20
url: /ja/java/adding-bookmark-actions/
description: このセクションでは、Aspose.PDF Facadesを使用して既存のPDFファイルにブックマークアクションを追加する方法について説明します。
lastmod: "2021-06-30"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

com.aspose.pdf.facadesパッケージに含まれる[PdfContentEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor)クラスは、PDFファイルにブックマークアクションを追加する柔軟性を提供します。このクラスを使用すると、PDFビューアでメニュー項目を実行するためのシリアルアクションと対応するリンクを作成できます。また、このクラスはドキュメントイベントのための追加アクションを作成する機能も提供します。

次のコード例は、PDFドキュメントにブックマークアクションを追加する方法を示しています。
 If you click on this tab, the desired action is performed. With the help of a Bookmark, clicking on it, we perform the desired action. Then create an [CreateBookmarkAction](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor#createBookmarksAction-java.lang.String-java.awt.Color-boolean-boolean-java.lang.String-java.lang.String-java.lang.String-), set the parameters of the text, colors, indicate the name of the bookmark, and also indicate the page number. The last action is done with "GoTo", it allows you to go from anywhere to the page we need.

このタブをクリックすると、希望のアクションが実行されます。ブックマークを使用して、それをクリックすると、希望のアクションを実行します。それから、[CreateBookmarkAction](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor#createBookmarksAction-java.lang.String-java.awt.Color-boolean-boolean-java.lang.String-java.lang.String-java.lang.String-)を作成し、テキストのパラメータ、色、ブックマークの名前を設定し、ページ番号も指定します。最後のアクションは「GoTo」で行われ、必要なページにどこからでも移動できます。

```java
public static void AddBookmarksAction()
        {
            var document = new Document(_dataDir + "Sample.pdf");
            PdfContentEditor editor = new PdfContentEditor(document);
            editor.createBookmarksAction("Bookmark 1", java.awt.Color.GREEN, true, false, "", "GoTo", "2");

            // 結果のPDFをファイルに保存します
            editor.save(_dataDir + "PdfContentEditorDemo_Bookmark.pdf");
        }
```