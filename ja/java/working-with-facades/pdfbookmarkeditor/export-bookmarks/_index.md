---
title: 既存のPDFファイルからブックマークをXMLにエクスポートする(facades)
type: docs
weight: 20
url: ja/java/export-bookmark/
description: このセクションでは、PdfBookmarEditorクラスを使用してAspose.PDF Facadesでブックマークをエクスポートする方法を説明します。
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

{{% alert %}}

exportBookmarksToXmlメソッドは、PDFファイルからXMLファイルにブックマークをエクスポートすることができます。

{{% /alert %}}

ブックマークをエクスポートするには:

1. PdfBookmarkEditorオブジェクトを作成し、bindPdfメソッドを使用してPDFファイルをバインドします。
1. exportBookmarksToXmlメソッドを呼び出します。

次のコードスニペットは、ブックマークをXMLファイルにエクスポートする方法を示しています。

{{< gist "aspose-pdf" "474c352a71ac9477aa0d604fd32e1c6a" "Examples-src-main-java-com-aspose-pdf-examples-facades-Bookmarks-ExportBookmarksToXMLFromAnExistingPDFFile-ToExportBookmarks.java" >}}

From Aspose.PDF for Java 9.0.0、PdfBookmarkEditor クラスは Stream 引数を使用して exportBookmarksToXML および importBookmarksWithXML メソッドを実装します。その結果、抽出されたブックマークをストリーム オブジェクトに保存できます。

{{< gist "aspose-pdf" "474c352a71ac9477aa0d604fd32e1c6a" "Examples-src-main-java-com-aspose-pdf-examples-facades-Bookmarks-ExportBookmarksToXMLFromAnExistingPDFFile-ExportBookmarksToXML.java" >}}