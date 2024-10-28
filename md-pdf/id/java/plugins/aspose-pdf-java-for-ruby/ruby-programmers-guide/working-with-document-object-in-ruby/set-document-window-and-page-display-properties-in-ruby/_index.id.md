---
title: Setel Properti Jendela Dokumen dan Tampilan Halaman di Ruby
type: docs
weight: 100
url: /java/set-document-window-and-page-display-properties-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - Setel Properti Jendela Dokumen dan Tampilan Halaman

Untuk Menyetel Properti Jendela Dokumen dan Tampilan Halaman dari dokumen Pdf menggunakan **Aspose.PDF Java untuk Ruby**, cukup panggil modul **SetDocumentWindow**.

Kode Ruby

```java
# Jalur ke direktori dokumen.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Buka dokumen pdf.

doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + "input1.pdf")

# Menyetel properti dokumen yang berbeda

# Posisi jendela dokumen - Default: false

doc.setCenterWindow(true)

# Urutan membaca yang dominan; menentukan posisi halaman

# ketika ditampilkan berdampingan - Default: L2R

#doc.setDirection(Rjb::import('com.aspose.pdf.Direction.L2R'))

# Apakah bilah judul jendela harus menampilkan judul dokumen.

# Jika false, bilah judul menampilkan nama file PDF - Default: false

doc.setDisplayDocTitle(true)

# Apakah mengubah ukuran jendela dokumen agar sesuai dengan ukuran

# halaman yang pertama ditampilkan - Default: false

doc.setFitWindow(true)

# Apakah menyembunyikan bilah menu dari aplikasi penampil - Default: false

doc.setHideMenubar(true)

# Apakah menyembunyikan bilah alat dari aplikasi penampil - Default: false

doc.setHideToolBar(true)

# Apakah menyembunyikan elemen UI seperti bilah gulir

# dan hanya menampilkan konten halaman - Default: false

doc.setHideWindowUI(true)

# Mode halaman dokumen. Cara menampilkan dokumen saat keluar dari mode layar penuh.

doc.setNonFullScreenPageMode(Rjb::import('com.aspose.pdf.PageMode.UseOC'))

# Tata letak halaman yaitu satu halaman, satu kolom

doc.setPageLayout(Rjb::import('com.aspose.pdf.PageLayout.TwoColumnLeft'))

# Bagaimana dokumen harus ditampilkan saat dibuka.

doc.setPageMode()

# Simpan file PDF yang telah diperbarui

doc.save(data_dir + "Set Document Window.pdf")
```


## Download Running Code

Unduh **Set Document Window and Page Display Properties (Aspose.PDF)** dari salah satu situs sosial coding yang disebutkan di bawah ini:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/setdocumentwindow.rb)