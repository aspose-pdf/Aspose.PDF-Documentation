---
title: すべてのページのブックマークを作成する（ファサード）
type: docs
weight: 10
url: ja/java/create-bookmark/
description: このセクションでは、PdfBookmarEditor クラスを使用して Aspose.PDF ファサードでブックマークを作成する方法を説明します。
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## すべてのページのブックマークを作成する（ファサード）

すべてのページのブックマークを作成するには、パラメーターなしで createBookmarks メソッドを使用する必要があります。PdfBookmarEditor クラスを使用すると、PDF ファイルのすべてのページのブックマークを作成できます。まず、PdfBookmarkEditor クラスのオブジェクトを作成し、bindPdf メソッドを使用して入力 PDF をバインドする必要があります。その後、createBookmarks メソッドを呼び出し、save メソッドを使用して出力 PDF ファイルを保存します。

次のコードスニペットは次のことを示しています:

{{< gist "aspose-pdf" "474c352a71ac9477aa0d604fd32e1c6a" "Examples-src-main-java-com-aspose-pdf-examples-facades-Bookmarks-CreateBookmarksOfAllPages-.java" >}}

## プロパティを指定してすべてのページのブックマークを作成する（ファサード）

PdfBookmarEditor クラスを使用すると、PDF ファイルのすべてのページのブックマークを作成し、プロパティ（色、太字、斜体）を指定できます。
 あなたは、createBookmarksメソッドを使用してそれを行うことができます。まず、PdfBookmarkEditorクラスのオブジェクトを作成し、bindPdfメソッドを使用して入力PDFをバインドする必要があります。次に、createBookmarksメソッドを呼び出し、saveメソッドを使用して出力PDFファイルを保存します。

次のコードスニペットは、プロパティを持つすべてのページのブックマークを作成する方法を示しています。

{{< gist "aspose-pdf" "474c352a71ac9477aa0d604fd32e1c6a" "Examples-src-main-java-com-aspose-pdf-examples-facades-Bookmarks-CreateBookmarksOfAllPagesWithProperties-.java" >}}