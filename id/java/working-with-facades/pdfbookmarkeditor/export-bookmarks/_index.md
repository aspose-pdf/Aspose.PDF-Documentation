---
title: Ekspor Bookmark ke XML dari File PDF yang Ada (facades)
type: docs
weight: 20
url: id/java/export-bookmark/
description: Bagian ini menjelaskan cara mengekspor bookmark dengan Aspose.PDF Facades menggunakan Kelas PdfBookmarEditor.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

{{% alert %}}

Metode exportBookmarksToXml memungkinkan Anda untuk mengekspor bookmark dari file PDF ke file XML.

{{% /alert %}}

Untuk mengekspor bookmark:

1. Buat objek PdfBookmarkEditor dan ikat file PDF menggunakan metode bindPdf.
1. Panggil metode exportBookmarksToXml.

Cuplikan kode berikut menunjukkan kepada Anda cara mengekspor bookmark ke file XML.

{{< gist "aspose-pdf" "474c352a71ac9477aa0d604fd32e1c6a" "Examples-src-main-java-com-aspose-pdf-examples-facades-Bookmarks-ExportBookmarksToXMLFromAnExistingPDFFile-ToExportBookmarks.java" >}}

Dari Aspose.PDF untuk Java 9.0.0, kelas PdfBookmarkEditor mengimplementasikan metode exportBookmarksToXML dan importBookmarksWithXML dengan argumen Stream. Akibatnya, penanda buku yang diekstraksi dapat disimpan ke objek stream.

{{< gist "aspose-pdf" "474c352a71ac9477aa0d604fd32e1c6a" "Examples-src-main-java-com-aspose-pdf-examples-facades-Bookmarks-ExportBookmarksToXMLFromAnExistingPDFFile-ExportBookmarksToXML.java" >}}