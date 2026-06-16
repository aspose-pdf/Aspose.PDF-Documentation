---
title: Buat Tautan PDF di Python
linktitle: Buat Tautan
type: docs
weight: 10
url: /id/python-net/create-links/
description: Pelajari cara membuat tautan PDF internal, eksternal, dan remote di Python.
lastmod: "2026-06-12"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cara membuat Tautan di PDF
Abstract: Panduan Aspose.PDF for Python via .NET tentang pembuatan tautan memberikan pengembang instruksi praktis untuk menambahkan hyperlink interaktif ke dokumen PDF menggunakan Python. Panduan ini mencakup cara membuat berbagai jenis tautan, termasuk yang meluncurkan aplikasi eksternal, menavigasi ke halaman tertentu dalam dokumen yang sama, atau membuka file PDF lainnya. Dokumentasi menjelaskan cara menggunakan objek LinkAnnotation, mendefinisikan area yang dapat diklik dengan Rectangle, dan menetapkan tindakan seperti LaunchAction atau GoToRemoteAction. Dengan contoh kode yang jelas dan panduan langkah demi langkah, sumber daya ini membantu pengembang meningkatkan navigasi dan interaktivitas PDF dalam aplikasi Python mereka.
---

## Tautan dalam Dokumen PDF

Menurut spesifikasi PDF 1.7 (ISO 32000-1:2008), sebuah **Link annotation** dapat memicu beberapa jenis aksi yang menentukan apa yang terjadi ketika anotasi tersebut diaktifkan. Berikut adalah aksi utama yang didukung:

1. **GoTo** – Menavigasi ke tujuan dalam dokumen yang sama.
1. **GoToR** – Melompat ke tujuan di file PDF lain (go-to remote).
1. **URI** – Membuka uniform resource identifier, biasanya sebuah tautan web.
1. **Launch** – Meluncurkan aplikasi atau membuka file (tergantung platform dan sering dibatasi untuk keamanan).
1. **Named** – Menjalankan aksi yang telah ditentukan, seperti pergi ke halaman berikutnya atau mencetak dokumen.
1. **JavaScript** – Menjalankan kode JavaScript yang tertanam (digunakan dengan hati-hati karena masalah keamanan).
1. **SubmitForm** – Mengirim data formulir ke URL yang ditentukan.
1. **ResetForm** – Mengatur ulang bidang formulir ke nilai defaultnya.
1. **ImportData** – Mengimpor data ke dalam dokumen dari file eksternal.

Dengan menambahkan tautan ke aplikasi ke dalam dokumen, dimungkinkan untuk menautkan ke aplikasi dari sebuah dokumen. Ini berguna ketika Anda ingin pembaca melakukan tindakan tertentu pada titik tertentu dalam tutorial, misalnya, atau untuk membuat dokumen yang kaya fitur.

Untuk membuat tautan aplikasi dengan ‘LaunchAction’:

```python
import aspose.pdf as ap
from os import path
import sys

def create_link_annotation_launch_action(infile, outfile):
    document = ap.Document(infile)
    page = document.pages[1]

    link = ap.annotations.LinkAnnotation(page, ap.Rectangle(10, 580, 120, 600, True))
    border = ap.annotations.Border(link)
    border.width = 5
    border.dash = ap.annotations.Dash(1, 1)
    link.color = ap.Color.green
    link.action = ap.annotations.LaunchAction(document, "sample.pdf")
    page.annotations.append(link)
    document.save(outfile)
```

## Buat Tautan Dokumen PDF dalam File PDF

### Menggunakan GoToRemoteAction

Potongan kode ini menunjukkan cara menambahkan anotasi tautan ke halaman tertentu dari dokumen PDF menggunakan perpustakaan Python PDF.

1. Buka dokumen PDF
1. Pilih halaman kedua dari dokumen (indeks 1)
1. Buat anotasi tautan:
1. Diposisikan pada koordinat (10, 580, 120, 600)
1. Berwarna hijau
1. Tautan ke 'sample.pdf' pada halaman pertamanya
1. Tambahkan anotasi tautan ke halaman
1. Simpan dokumen yang dimodifikasi ke jalur file output

Untuk membuat tautan dokumen PDF menggunakan 'GoToRemoteAction':

```python
import aspose.pdf as ap
from os import path
import sys

def create_link_annotation_go_to_remote_action(infile, outfile):
    document = ap.Document(infile)
    page = document.pages[1]

    link = ap.annotations.LinkAnnotation(page, ap.Rectangle(10, 580, 120, 600, True))
    link.color = ap.Color.green
    link.action = ap.annotations.GoToRemoteAction("sample.pdf", 1)
    page.annotations.append(link)
    document.save(outfile)
```

### Menggunakan GoToAction

Kode ini menunjukkan cara menambahkan anotasi tautan ke halaman tertentu dari dokumen PDF menggunakan Aspose.PDF untuk Python. Tautan muncul sebagai persegi panjang berwarna hijau dengan batas garis putus-putus dan memungkinkan pengguna untuk menavigasi ke halaman lain dalam PDF yang sama. Untuk membuat tautan dokumen PDF menggunakan 'GoToAction':

```python
import aspose.pdf as ap
from os import path
import sys

def create_link_annotation_go_to_action(infile, outfile):
    document = ap.Document(infile)
    page = document.pages[1]

    link = ap.annotations.LinkAnnotation(page, ap.Rectangle(10, 580, 120, 600, True))
    border = ap.annotations.Border(link)
    border.width = 5
    border.dash = ap.annotations.Dash(1, 1)
    link.color = ap.Color.green
    if document.pages.length >= 4:
        link.action = ap.annotations.GoToAction(document.pages[4])
    else:
        link.action = ap.annotations.GoToAction(document.pages[document.pages.length])
    page.annotations.append(link)
    document.save(outfile)
```

### Menerapkan GoToURIAction

Contoh berikut menunjukkan cara menambahkan anotasi tautan ke dokumen PDF menggunakan Aspose.PDF for Python. Tautan tersebut muncul sebagai area berwarna hijau yang dapat diklik pada halaman pertama, dan ketika diklik, itu membuka dokumentasi Aspose.PDF for Python di peramban web melalui GoToURIAction.

Fungsionalitas ini berguna untuk menyematkan referensi eksternal yang membantu, dokumentasi, atau tautan dukungan secara langsung di dalam PDF Anda.

1. Muat Dokumen PDF. Buka file PDF yang ada menggunakan ap.Document.
1. Akses Halaman Pertama. Gunakan document.pages[1] untuk mengakses halaman pertama (Aspose menggunakan indeks berbasis 1).
1. Buat Anotasi Tautan. Buat objek LinkAnnotation dan tentukan area persegi panjang yang dapat diklik menggunakan ap.Rectangle.
1. Atur Penampilan Anotasi. Atur warna anotasi menjadi hijau menggunakan link.color = ap.Color.green.
1. Tetapkan Tindakan URI. Gunakan GoToURIAction untuk menautkan anotasi ke URL eksternal.
1. Tambahkan Anotasi ke Halaman. Tambahkan anotasi tautan yang telah dikonfigurasi ke koleksi anotasi halaman pertama.
1. Simpan Dokumen yang Dimodifikasi. Simpan dokumen PDF yang diperbarui ke jalur keluaran yang ditentukan.

```python
import aspose.pdf as ap
from os import path
import sys
    
def create_link_annotation_go_to_URI_action(infile, outfile):
    document = ap.Document(infile)
    page = document.pages[1]

    link = ap.annotations.LinkAnnotation(page, ap.Rectangle(10, 580, 120, 600, True))
    link.color = ap.Color.green
    link.action = ap.annotations.GoToURIAction("https://docs.aspose.com/pdf/python")
    page.annotations.append(link)
    document.save(outfile)
```

## Topik Tautan Terkait

- [Bekerja dengan tautan PDF di Python](/pdf/id/python-net/links/)
- [Ekstrak tautan dari PDF di Python](/pdf/id/python-net/extract-links/)
- [Perbarui tautan dalam PDF menggunakan Python](/pdf/id/python-net/update-links/)