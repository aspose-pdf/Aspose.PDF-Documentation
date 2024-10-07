---
title: Create Bookmarks
type: docs
weight: 10
url: /net/create-bookmarks/
description: Bagian ini menjelaskan cara membuat penanda buku ke file PDF Anda dengan Aspose.PDF Facades menggunakan Kelas PdfBookmarEditor.
lastmod: "2021-06-05"
draft: false
---

## Membuat Penanda Buku untuk Semua Halaman

Untuk membuat penanda buku dari semua halaman, Anda perlu menggunakan metode [CreateBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarks/methods/2) tanpa parameter apapun. Kelas [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) memungkinkan Anda membuat penanda buku untuk semua halaman dari file PDF. Pertama, Anda perlu membuat objek dari kelas [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) dan mengikat PDF input menggunakan metode [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3). Kemudian, Anda harus memanggil metode [CreateBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarks/methods/2) dan menyimpan file PDF output menggunakan metode [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save). Cuplikan kode berikut menunjukkan cara membuat Penanda Buku.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Bookmarks-CreateBookmarksAll-CreateBookmarksAll.cs" >}}

## Membuat Penanda Buku untuk Semua Halaman dengan Properti

Kelas [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) memungkinkan Anda untuk membuat penanda buku dari semua halaman file PDF dan menentukan propertinya (Warna, Tebal, Miring). Anda dapat melakukannya dengan bantuan metode [CreateBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarks/methods/2). Pertama, Anda perlu membuat objek dari kelas [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) dan mengikat PDF input menggunakan metode [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3). Kemudian, Anda harus memanggil metode [CreateBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarks/methods/2) dan menyimpan file PDF output menggunakan metode [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save). Cuplikan kode berikut menunjukkan kepada Anda cara membuat penanda buku untuk semua halaman dengan properti.



{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Bookmarks-CreateBookmarksPagesProperties-CreateBookmarksPagesProperties.cs" >}}

## Membuat Penanda Buku untuk Halaman Tertentu

Anda dapat membuat penanda buku untuk halaman tertentu dalam file PDF yang sudah ada menggunakan metode [CreateBookmarkOfPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarkofpage/methods/1). Metode ini mengambil dua argumen: judul bookmark dan nomor halaman. Pertama, Anda perlu membuat objek dari kelas [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) dan mengikat file PDF input menggunakan metode [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3). Kemudian, Anda harus memanggil metode [CreateBookmarkOfPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarkofpage/methods/1) dan menyimpan file PDF output menggunakan metode [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save). Cuplikan kode berikut menunjukkan cara membuat bookmark dari halaman tertentu.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Bookmarks-CreateBookmarkPage-CreateBookmarkPage.cs" >}}

## Membuat Bookmark untuk Rentang Halaman

Kelas [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) memungkinkan Anda membuat bookmark untuk rentang halaman. Anda dapat menggunakan metode [CreateBookmarkOfPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarkofpage/methods/1) dengan dua parameter: daftar bookmark (daftar judul bookmark) dan daftar halaman (daftar halaman yang akan diberi bookmark). Pertama, Anda perlu membuat objek dari kelas [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) dan mengikat file PDF input menggunakan metode [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3). Kemudian, Anda harus memanggil metode [CreateBookmarkOfPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarkofpage/methods/1) dan menyimpan output PDF menggunakan metode [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save). Cuplikan kode berikut menunjukkan kepada Anda bagaimana membuat bookmark dari rentang halaman.




{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Bookmarks-CreateBookmarkPageRange-CreateBookmarkPageRange.cs" >}}
## Tambahkan Penanda Buku di File PDF yang Ada

Anda dapat menambahkan penanda buku di file PDF yang ada menggunakan kelas [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor). Untuk membuat penanda buku, Anda perlu membuat objek [Bookmark](https://reference.aspose.com/pdf/net/aspose.pdf.facades/bookmark) dan mengatur atribut yang diperlukan dari penanda buku tersebut. Setelah itu, Anda perlu mengoper objek [Bookmark](https://reference.aspose.com/pdf/net/aspose.pdf.facades/bookmark) ke metode [CreateBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarks/methods/2) dari kelas [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor). Terakhir, Anda perlu menyimpan file PDF yang telah diperbarui menggunakan metode [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save). Cuplikan kode berikut menunjukkan cara menambahkan penanda buku di file PDF yang ada.




{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Bookmarks-AddBookmark-AddBookmark.cs" >}}

## Menambahkan Penanda Anak dalam File PDF yang Ada

Anda dapat menambahkan penanda anak dalam file PDF yang ada menggunakan kelas [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor). In order to add child bookmarks, Anda perlu membuat objek [Bookmark](https://reference.aspose.com/pdf/net/aspose.pdf.facades/bookmark). You can add individual [Penanda](https://reference.aspose.com/pdf/net/aspose.pdf.facades/bookmark) objects into [Penanda](https://reference.aspose.com/pdf/net/aspose.pdf.facades/bookmarks) object. Anda juga perlu membuat objek [Bookmark](https://reference.aspose.com/pdf/net/aspose.pdf.facades/bookmark) dan mengatur properti [ChildItem](https://reference.aspose.com/pdf/net/aspose.pdf.facades/bookmark/properties/childitem) ke objek [Bookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades/bookmarks). Kemudian Anda perlu meneruskan objek [Bookmark](https://reference.aspose.com/pdf/net/aspose.pdf.facades/bookmark) ini dengan [ChildItem](https://reference.aspose.com/pdf/net/aspose.pdf.facades/bookmark/properties/childitem) ke metode [CreateBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarks/methods/2). Akhirnya, Anda perlu menyimpan PDF yang diperbarui menggunakan metode [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) dari kelas [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor). Cuplikan kode berikut menunjukkan cara menambahkan bookmark anak dalam file PDF yang ada.




{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Bookmarks-AddChildBookmark-AddChildBookmark.cs" >}}
## Lihat juga

Cobalah untuk membandingkan dan menemukan cara bekerja dengan penanda halaman yang sesuai untuk Anda. Mari belajar bagian [Bekerja dengan Penanda Halaman di PDF](/pdf/net/bookmarks/).