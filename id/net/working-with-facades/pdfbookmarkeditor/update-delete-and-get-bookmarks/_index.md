---
title: Update, Delete dan Dapatkan Bookmark
type: docs
weight: 30
url: /id/net/update-delete-and-get-bookmarks/
description: Bagian ini menjelaskan cara memperbarui, menghapus, dan mendapatkan Bookmark dengan Aspose.PDF Facades.
lastmod: "2021-06-05"
draft: false
---

## Memperbarui Bookmark yang Ada di File PDF

Untuk memperbarui bookmark yang ada di file PDF, Anda perlu menggunakan metode [ModifyBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor/methods/modifybookmarks). This method takes two arguments: source title (judul penanda buku yang akan diubah), destination title (judul yang akan diganti). Anda perlu membuat objek dari kelas [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) dan mengikat file PDF input menggunakan metode [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3). Setelah itu, Anda perlu memanggil metode [ModifyBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor/methods/modifybookmarks), dan kemudian menyimpan PDF yang diperbarui menggunakan metode [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save). Cuplikan kode berikut menunjukkan kepada Anda cara memodifikasi penanda buku yang ada dalam file PDF.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Bookmarks-UpdateBookmark-UpdateBookmark.cs" >}}

## Hapus Semua Penanda Buku dari File PDF

Anda dapat menghapus semua penanda buku dari file PDF menggunakan metode [DeleteBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor/methods/deletebookmarks) tanpa parameter apa pun. Pertama-tama, Anda perlu membuat objek dari kelas [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) dan mengikat file PDF input menggunakan metode [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3). Setelah itu, Anda perlu memanggil metode [DeleteBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor/methods/deletebookmarks) dan kemudian menyimpan file PDF yang diperbarui menggunakan metode [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save). Cuplikan kode berikut menunjukkan kepada Anda cara menghapus semua penanda buku dari file PDF.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Bookmarks-DeleteAllBookmarks-DeleteAllBookmarks.cs" >}}

## Hapus Penanda Buku Tertentu dari File PDF

Untuk menghapus penanda buku tertentu, Anda perlu memanggil metode [DeleteBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor/methods/deletebookmarks) dengan parameter string (judul). *Judul* di sini mewakili penanda buku yang akan dihapus dari PDF. Buat objek dari kelas [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) dan ikat file PDF input menggunakan metode [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3). Setelah itu, panggil metode [DeleteBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor/methods/deletebookmarks) dan kemudian simpan file PDF yang diperbarui menggunakan metode [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save). Cuplikan kode berikut menunjukkan cara menghapus penanda buku tertentu dari file PDF.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Bookmarks-DeleteABookmark-DeleteABookmark.cs" >}}

## Dapatkan Penanda Buku dari Dokumen PDF Facades

Kelas [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) menyediakan fitur untuk memanipulasi Penanda Buku dalam file PDF yang ada. Itu menyediakan berbagai properti untuk mendapatkan/mengatur informasi mengenai penanda buku. Cuplikan kode berikut menunjukkan cara mendapatkan informasi terkait setiap penanda buku dalam file PDF.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Bookmarks-GetFromPDF-GetFromPDF.cs" >}}

## Ekstrak Penanda Buku dari File PDF yang Ada

Metode [ExtractBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/extractbookmarks/methods/3) memungkinkan Anda mengekstrak penanda buku dari file PDF. Dalam rangka untuk mengekstrak penanda buku, Anda perlu membuat objek [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) dan mengikat file PDF menggunakan metode [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3). Setelah itu, Anda perlu memanggil metode [ExtractBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/extractbookmarks/methods/3). Metode [ExtractBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/extractbookmarks/methods/3) mengembalikan objek [Bookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades/bookmarks/methods/index). Anda kemudian dapat melakukan loop melalui bookmark ini dan mendapatkan objek [Bookmark](https://reference.aspose.com/pdf/net/aspose.pdf.facades/bookmark) individu. Terakhir, simpan file PDF yang diperbarui menggunakan metode [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save). Cuplikan kode berikut menunjukkan cara mengekspor bookmark ke file XML.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Bookmarks-ExtractBookmarks-ExtractBookmarks.cs" >}}