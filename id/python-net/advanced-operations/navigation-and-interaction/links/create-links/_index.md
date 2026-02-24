---
title: Buat Tautan di File PDF dengan Python
linktitle: Buat Tautan
type: docs
weight: 10
url: /id/python-net/create-links/
description: Bagian ini menjelaskan cara membuat tautan di dokumen PDF Anda dengan Python.
lastmod: "2025-07-17"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cara Membuat Tautan di PDF
Abstract: Panduan Aspose.PDF untuk Python via .NET tentang pembuatan tautan menyediakan pengembang dengan instruksi praktis untuk menambahkan hyperlink interaktif ke dokumen PDF menggunakan Python. Panduan ini mencakup cara membuat berbagai jenis tautan, termasuk yang meluncurkan aplikasi eksternal, menavigasi ke halaman tertentu dalam dokumen yang sama, atau membuka file PDF lain. Dokumentasi menjelaskan cara menggunakan objek LinkAnnotation, mendefinisikan area yang dapat diklik dengan Rectangle, dan menetapkan aksi seperti LaunchAction atau GoToRemoteAction. Dengan contoh kode yang jelas dan panduan langkah demi langkah, sumber daya ini membantu pengembang meningkatkan navigasi PDF dan interaktivitas dalam aplikasi Python mereka.
---

## Tautan dalam Dokumen PDF

Berdasarkan spesifikasi PDF 1.7 (ISO 32000-1:2008), sebuah **Link annotation** dapat memicu beberapa jenis aksi yang menentukan apa yang terjadi ketika anotasi diaktifkan. Berikut adalah aksi utama yang didukung:

1. **GoTo** – Menavigasi ke tujuan dalam dokumen yang sama.
1. **GoToR** – Melompat ke tujuan di file PDF lain (go-to remote).
1. **URI** – Membuka uniform resource identifier, biasanya sebuah tautan web.
1. **Launch** – Meluncurkan aplikasi atau membuka file (bergantung pada platform dan sering dibatasi demi keamanan).
1. **Named** – Menjalankan aksi yang telah ditentukan sebelumnya, seperti pindah ke halaman berikutnya atau mencetak dokumen.
1. **JavaScript** – Menjalankan kode JavaScript yang disematkan (digunakan dengan hati-hati karena masalah keamanan).
1. **SubmitForm** – Mengirim data formulir ke URL yang ditentukan.
1. **ResetForm** – Mengatur ulang bidang formulir ke nilai defaultnya.
1. **ImportData** – Mengimpor data ke dalam dokumen dari file eksternal.

Dengan menambahkan tautan ke aplikasi dalam sebuah dokumen, memungkinkan untuk menautkan ke aplikasi dari dokumen tersebut. Ini berguna ketika Anda ingin pembaca melakukan tindakan tertentu pada titik spesifik dalam tutorial, misalnya, atau untuk membuat dokumen yang kaya fitur.

Untuk membuat tautan aplikasi dengan 'LaunchAction':

```python

    import aspose.pdf as ap
    from os import path

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    # Open the input PDF document
    document = ap.Document(path_infile)

    # Select the second page (index 1)
    page = document.pages[1]

    # Create a link annotation with specific dimensions and position
    link = ap.annotations.LinkAnnotation(page, ap.Rectangle(10, 580, 120, 600, True))

    # Configure the link's border
    border = ap.annotations.Border(link)
    border.width = 5  # Border width of 5 units
    border.dash = ap.annotations.Dash(1, 1)  # Dashed border style

    # Set link appearance
    link.color = ap.Color.green  # Green color for the link

    # Set the action to launch another PDF file
    # Note: Commented out system command demonstrates potential alternative launch actions
    # link.action = ap.annotations.LaunchAction(document, "start %windir%\explorer.exe")
    link.action = ap.annotations.LaunchAction(document, "sample.pdf")

    # Add the link annotation to the page
    page.annotations.append(link)

    # Save the modified document
    document.save(path_outfile)
```

## Buat Tautan Dokumen PDF dalam File PDF

### Menggunakan GoToRemoteAction

Potongan kode ini menunjukkan cara menambahkan anotasi tautan ke halaman spesifik dari dokumen PDF menggunakan pustaka PDF Python.

1. Buka dokumen PDF
1. Pilih halaman kedua dari dokumen (indeks 1)
1. Buat anotasi tautan:
1. Diposisikan pada koordinat (10, 580, 120, 600)
1. Berwarna hijau
1. Menautkan ke 'sample.pdf' pada halaman pertamanya
1. Tambahkan anotasi tautan ke halaman
1. Simpan dokumen yang dimodifikasi ke jalur file output

Untuk membuat tautan dokumen PDF menggunakan 'GoToRemoteAction':

```python

import aspose.pdf as ap
from os import path

path_infile = path.join(self.dataDir, infile)
path_outfile = path.join(self.dataDir, outfile)

# Load the input PDF document
document = ap.Document(path_infile)

# Access the first page of the document (Aspose uses 1-based indexing)
page = document.pages[1]

# Create a link annotation in the specified rectangle area on the page
link = ap.annotations.LinkAnnotation(
    page, ap.Rectangle(10, 580, 120, 600, True)  # (left, bottom, right, top, isEmpty)
)

# Set the color of the link annotation to green
link.color = ap.Color.green

# Define a remote action to open "sample.pdf" and navigate to its first page
link.action = ap.annotations.GoToRemoteAction("sample.pdf", 1)

# Add the link annotation to the current page
page.annotations.append(link)

# Save the updated PDF to the specified output path
document.save(path_outfile)
```

### Menggunakan GoToAction

Kode ini menunjukkan cara menambahkan anotasi tautan ke halaman tertentu dari dokumen PDF menggunakan Aspose.PDF untuk Python. Tautan muncul sebagai persegi panjang berwarna hijau dengan garis putus-putus dan memungkinkan pengguna menavigasi ke halaman lain dalam PDF yang sama. Untuk membuat tautan dokumen PDF menggunakan 'GoToAction':

```python

    import aspose.pdf as ap
    from os import path

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    # Open the PDF document
    document = ap.Document(path_infile)

    # Select the second page (index 1)
    page = document.pages[1]

    # Create a link annotation with specific coordinates
    link = ap.annotations.LinkAnnotation(page, ap.Rectangle(10, 580, 120, 600, True))

    # Customize link annotation border
    border = ap.annotations.Border(link)
    border.width = 5  # Border width
    border.dash = ap.annotations.Dash(1, 1)  # Dashed border style

    # Set link color to green
    link.color = ap.Color.green

    # Set link destination
    if document.pages.count >= 4:
        # Link to 4th page if document has 4 or more pages
        link.action = ap.annotations.GoToAction(document.pages[4])
    else:
        # Fallback: link to the last page if less than 4 pages
        link.action = ap.annotations.GoToAction(document.pages[document.pages.count])

    # Add the link annotation to the page
    page.annotations.append(link)

    # Save the modified document
    document.save(path_outfile)
```

### Menerapkan GoToURIAction

Contoh berikut menunjukkan cara menambahkan anotasi tautan ke dokumen PDF menggunakan Aspose.PDF untuk Python. Tautan muncul sebagai area hijau yang dapat diklik pada halaman pertama, dan ketika diklik, ia membuka dokumentasi Aspose.PDF untuk Python di peramban web melalui GoToURIAction.

Fungsi ini berguna untuk menyematkan referensi eksternal yang membantu, dokumentasi, atau tautan dukungan langsung di dalam PDF Anda.

1. Muat Dokumen PDF. Buka file PDF yang ada menggunakan ap.Document.
1. Akses Halaman Pertama. Gunakan document.pages[1] untuk mengakses halaman pertama (Aspose menggunakan indeks berbasis 1).
1. Buat Anotasi Tautan. Buat objek LinkAnnotation dan tentukan area persegi panjang yang dapat diklik menggunakan ap.Rectangle.
1. Atur Penampilan Anotasi. Atur warna anotasi menjadi hijau menggunakan link.color = ap.Color.green.
1. Tetapkan Aksi URI. Gunakan GoToURIAction untuk menautkan anotasi ke URL eksternal.
1. Tambahkan Anotasi ke Halaman. Tambahkan anotasi tautan yang telah dikonfigurasi ke koleksi anotasi halaman pertama.
1. Simpan Dokumen yang Dimodifikasi. Simpan dokumen PDF yang diperbarui ke jalur output yang ditentukan.

```python

    import aspose.pdf as ap
    from os import path

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    # Load the input PDF document
    document = ap.Document(path_infile)

    # Access the first page (Aspose uses 1-based indexing)
    page = document.pages[1]

    # Create a link annotation at the specified rectangle position
    link = ap.annotations.LinkAnnotation(
        page, ap.Rectangle(10, 580, 120, 600, True)  # (left, bottom, right, top, isEmpty)
    )

    # Set the color of the link annotation to green
    link.color = ap.Color.green

    # Define a URI action that navigates to the Aspose.PDF Python documentation
    link.action = ap.annotations.GoToURIAction("https://docs.aspose.com/pdf/python")

    # Add the link annotation to the page
    page.annotations.append(link)

    # Save the modified PDF to the output path
    document.save(path_outfile)
```

