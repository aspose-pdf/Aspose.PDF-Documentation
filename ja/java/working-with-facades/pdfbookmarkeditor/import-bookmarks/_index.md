---
title: 既存のPDFファイルにXMLからブックマークをインポートする (facades)
type: docs
weight: 30
url: /ja/java/import-bookmark/
description: このセクションでは、Aspose.PDF Facadesを使用してPdfBookmarkEditorクラスでブックマークをインポートする方法を説明します。
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

importBookmarksWithXmlメソッドを使用すると、XMLファイルからPDFファイルにブックマークをインポートできます。

ブックマークをインポートするには:

1. PdfBookmarkEditorオブジェクトを作成し、bindPdfメソッドを使用してPDFファイルをバインドします。
1. importBookmarksWithXmlメソッドを呼び出します。
1. saveメソッドを使用して更新されたPDFファイルを保存します。

以下のコードスニペットは、XMLファイルからブックマークをインポートする方法を示しています。

{{< gist "aspose-pdf" "474c352a71ac9477aa0d604fd32e1c6a" "Examples-src-main-java-com-aspose-pdf-examples-facades-Bookmarks-ImportBookmarksFromXMLToAnExistingPDFFile-ToImportBookmarks.java" >}}

From Aspose.PDF for Java 9.0.0、PdfBookmarkEditorクラスは、Stream引数を使用してexportBookmarksToXMLおよびimportBookmarksWithXMLメソッドを実装しています。その結果、抽出されたブックマークはストリームオブジェクトからインポートすることができます。

{{< gist "aspose-pdf" "474c352a71ac9477aa0d604fd32e1c6a" "Examples-src-main-java-com-aspose-pdf-examples-facades-Bookmarks-ImportBookmarksFromXMLToAnExistingPDFFile-ImportBookmarksWithXML.java" >}}