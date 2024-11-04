---
title: Impor Penanda Buku dari XML ke File PDF yang Ada (facades)
type: docs
weight: 30
url: /java/import-bookmark/
description: Bagian ini menjelaskan cara mengimpor penanda buku dengan Aspose.PDF Facades menggunakan Kelas PdfBookmarEditor.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Metode importBookmarksWithXml memungkinkan Anda untuk mengimpor penanda buku ke dalam file PDF dari file XML.

Untuk mengimpor penanda buku:

1. Buat objek PdfBookmarkEditor dan ikat file PDF menggunakan metode bindPdf.
1. Panggil metode importBookmarksWithXml.
1. Simpan file PDF yang telah diperbarui menggunakan metode save.

Cuplikan kode berikut menunjukkan cara mengimpor penanda buku dari file XML.

{{< gist "aspose-pdf" "474c352a71ac9477aa0d604fd32e1c6a" "Examples-src-main-java-com-aspose-pdf-examples-facades-Bookmarks-ImportBookmarksFromXMLToAnExistingPDFFile-ToImportBookmarks.java" >}}

From Aspose.PDF for Java 9.0.0, kelas PdfBookmarkEditor mengimplementasikan metode exportBookmarksToXML dan importBookmarksWithXML dengan argumen Stream. Akibatnya, bookmark yang diekstrak dapat diimpor dari objek stream.

{{< gist "aspose-pdf" "474c352a71ac9477aa0d604fd32e1c6a" "Examples-src-main-java-com-aspose-pdf-examples-facades-Bookmarks-ImportBookmarksFromXMLToAnExistingPDFFile-ImportBookmarksWithXML.java" >}}