---
title: Dapatkan Properti Jendela Dokumen dan Tampilan Halaman dalam Python
type: docs
weight: 30
url: /id/java/get-document-window-and-page-display-properties-in-python/
lastmod: "2021-06-05"
---

Untuk Mendapatkan Properti Jendela Dokumen dan Tampilan Halaman dari dokumen Pdf menggunakan **Aspose.PDF Java untuk Python**, cukup panggil kelas **GetDocumentWindow**.

```python

doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# Dapatkan berbagai properti dokumen
# Posisi jendela dokumen - Default: false
print "CenterWindow :- " + str(doc.getCenterWindow())

# Urutan membaca yang dominan; menentukan posisi halaman
# saat ditampilkan berdampingan - Default: L2R
print "Direction :- " + str(doc.getDirection())

# Apakah bilah judul jendela harus menampilkan judul dokumen.
# Jika false, bilah judul menampilkan nama file PDF - Default: false
print "DisplayDocTitle :- " + str(doc.getDisplayDocTitle())

#Apakah untuk mengubah ukuran jendela dokumen agar sesuai dengan ukuran
#halaman pertama yang ditampilkan - Default: false
print "FitWindow :- " + str(doc.getFitWindow())

# Apakah untuk menyembunyikan bilah menu dari aplikasi penampil - Default: false
print "HideMenuBar :-" + str(doc.getHideMenubar())

# Apakah untuk menyembunyikan bilah alat dari aplikasi penampil - Default: false
print "HideToolBar :-" + str(doc.getHideToolBar())

# Apakah untuk menyembunyikan elemen UI seperti bilah gulir
# dan hanya menampilkan konten halaman - Default: false
print "HideWindowUI :-" + str(doc.getHideWindowUI())

# Mode halaman dokumen. Cara menampilkan dokumen saat keluar dari mode layar penuh.
print "NonFullScreenPageMode :-" + str(doc.getNonFullScreenPageMode())

# Tata letak halaman yaitu satu halaman, satu kolom
print "PageLayout :-" + str(doc.getPageLayout())

#Bagaimana dokumen harus ditampilkan saat dibuka.
print "pageMode :-" + str(doc.getPageMode())
```


**Unduh Kode yang Berjalan**

Unduh **Dapatkan Jendela Dokumen dan Properti Tampilan Halaman (Aspose.PDF)** dari salah satu situs pengkodean sosial yang disebutkan di bawah ini:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/GetDocumentWindow/GetDocumentWindow.py)