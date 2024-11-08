---
title: Dapatkan Jendela Dokumen dan Properti Tampilan Halaman di Ruby
type: docs
weight: 40
url: /id/java/get-document-window-and-page-display-properties-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - Dapatkan Jendela Dokumen dan Properti Tampilan Halaman

Untuk Mendapatkan Jendela Dokumen dan Properti Tampilan Halaman dari dokumen Pdf menggunakan **Aspose.PDF Java for Ruby**, cukup panggil modul **GetDocumentWindow**.

Kode Ruby

```java
# Jalur ke direktori dokumen.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Buka dokumen pdf.

doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + "input1.pdf")

# Dapatkan berbagai properti dokumen

# Posisi jendela dokumen - Default: false

puts "CenterWindow :- " + doc.getCenterWindow().to_s

# Urutan pembacaan yang dominan; tentukan posisi halaman

# ketika ditampilkan berdampingan - Default: L2R

puts "Direction :- " + doc.getDirection().to_s

# Apakah bilah judul jendela harus menampilkan judul dokumen.

# Jika false, bilah judul menampilkan nama file PDF - Default: false

puts "DisplayDocTitle :- " + doc.getDisplayDocTitle().to_s

# Apakah untuk mengubah ukuran jendela dokumen agar sesuai dengan ukuran

# halaman pertama yang ditampilkan - Default: false

puts "FitWindow :- " + doc.getFitWindow().to_s

# Apakah untuk menyembunyikan bilah menu dari aplikasi penampil - Default: false

puts "HideMenuBar :-" + doc.getHideMenubar().to_s

# Apakah untuk menyembunyikan bilah alat dari aplikasi penampil - Default: false

puts "HideToolBar :-" + doc.getHideToolBar().to_s

# Apakah untuk menyembunyikan elemen UI seperti bilah gulir

# dan hanya menampilkan konten halaman - Default: false

puts "HideWindowUI :-" + doc.getHideWindowUI().to_s

# Mode halaman dokumen. Bagaimana menampilkan dokumen saat keluar dari mode layar penuh.

puts "NonFullScreenPageMode :-" + doc.getNonFullScreenPageMode().to_s

# Tata letak halaman yaitu satu halaman, satu kolom

puts "PageLayout :-" + doc.getPageLayout().to_s

# Bagaimana dokumen harus ditampilkan saat dibuka.

puts "pageMode :-" + doc.getPageMode().to_s
```


## Download Running Code

Unduh **Dapatkan Properti Jendela Dokumen dan Tampilan Halaman (Aspose.PDF)** dari salah satu situs pengkodean sosial yang disebutkan di bawah ini:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/getdocumentwindow.rb)