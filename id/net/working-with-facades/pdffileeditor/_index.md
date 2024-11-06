---
title: PdfFileEditor Class
type: docs
weight: 10
url: id/net/pdffileeditor-class/
description: Bagian ini menjelaskan cara bekerja dengan Aspose.PDF Facades menggunakan kelas PdfFileEditor.
lastmod: "2021-06-05"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Bekerja dengan dokumen PDF mencakup berbagai fungsi. Mengelola halaman-halaman dari file PDF adalah bagian penting dari pekerjaan ini. Aspose.PDF.Facaded menyediakan kelas `PdfFileEditor` untuk tujuan ini.

Kelas PdfFileEditor berisi metode yang membantu memanipulasi halaman individu; kelas ini tidak mengedit atau memanipulasi isi dari halaman. Anda dapat menyisipkan halaman baru, menghapus halaman yang ada, membagi halaman atau Anda dapat menentukan penempatan halaman menggunakan PdfFileEditor.

Fitur yang disediakan oleh kelas ini dapat dibagi menjadi tiga kategori utama yaitu Pengeditan File, Penempatan PDF, dan Pemisahan. Kami akan membahas bagian-bagian ini secara detail di bawah ini:

## Pengeditan File

Fitur-fitur yang dapat kita masukkan dalam bagian ini adalah Sisipkan, Tambahkan, Hapus, Gabungkan, dan Ekstrak. Anda dapat menyisipkan halaman baru di lokasi tertentu menggunakan metode Insert, atau menambahkan halaman di akhir file. Anda juga dapat menghapus sejumlah halaman dari file menggunakan metode Delete, dengan menentukan array integer yang berisi nomor halaman yang akan dihapus. Metode Concatenate membantu Anda menyatukan halaman dari beberapa file PDF. Anda dapat mengekstrak sejumlah halaman menggunakan metode Extract, dan menyimpan halaman-halaman ini ke dalam file PDF lain atau aliran memori.

Bagian ini mengeksplorasi kemampuan kelas ini dan menjelaskan tujuan dari metodenya.

- [Gabungkan dokumen PDF](/pdf/net/concatenate-pdf-documents/)
- [Ekstrak halaman PDF](/pdf/net/extract-pdf-pages/)
- [Sisipkan halaman PDF](/pdf/net/insert-pdf-pages/)
- [Hapus halaman PDF](/pdf/net/delete-pdf-pages/)

## Menggunakan Page Brakes

Page Break adalah fitur khusus yang memungkinkan aliran dokumen kembali.

- [Page Break pada PDF yang ada](/pdf/net/page-break-in-existing-pdf/)

## Penyusunan PDF

Penyusunan adalah proses mengatur halaman dengan benar sebelum pencetakan. `PdfFileEditor` menyediakan dua metode untuk tujuan ini yaitu `MakeBooklet` dan `MakeNUp`. Metode MakeBooklet membantu mengatur halaman sehingga akan mudah untuk melipat atau menjilidnya setelah dicetak, namun, metode MakeNUp memungkinkan untuk mencetak beberapa halaman pada satu halaman file PDF.

- [Buat Booklet dari PDF](/pdf/net/make-booklet-of-pdf/)
- [Buat NUp dari file PDF](/pdf/net/make-nup-of-pdf-files/)

## Pemisahan

Fitur pemisahan memungkinkan Anda untuk membagi file PDF yang ada menjadi beberapa bagian. Anda dapat memisahkan bagian depan file PDF atau bagian belakang. Karena PdfFileEditor menyediakan berbagai metode untuk tujuan pemisahan, Anda juga dapat membagi file menjadi halaman individu atau banyak set dari beberapa halaman.

- [Pisah halaman PDF](/pdf/net/split-pdf-pages/)