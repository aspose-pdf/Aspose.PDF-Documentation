---
title: Menambahkan Artefak Penomoran Bates dalam Python via .NET
linktitle: Menambahkan Penomoran Bates
type: docs
weight: 10
url: /id/python-net/add-bates-numbering/
description: Aspose.PDF untuk Python via .NET memungkinkan Anda menambahkan Penomoran Bates ke PDF.
lastmod: "2025-11-13"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Tambah Penomoran Bates via Python
Abstract: Penomoran Bates adalah fitur penting dalam alur kerja dokumen hukum, medis, dan bisnis, memastikan setiap halaman dalam satu set menerima identifier unik dan berurutan untuk referensi yang dapat diandalkan. Artikel ini menunjukkan bagaimana Aspose.PDF untuk Python via .NET menyederhanakan otomatisasi penomoran Bates melalui API yang fleksibel. Dengan menggunakan kelas BatesNArtifact, pengembang dapat mengonfigurasi perilaku penomoran—termasuk jumlah digit, awalan, akhiran, perataan, dan margin—dan menerapkannya secara programatis pada seluruh dokumen. Berbagai pendekatan disajikan, mulai dari penerapan artefak langsung hingga konfigurasi berbasis delegasi, menawarkan kontrol statis dan dinamis. Selain itu, API mendukung penghapusan lengkap nomor Bates dengan satu pemanggilan metode, memungkinkan manajemen siklus hidup penuh artefak pagination. Contoh kode yang jelas dan langkah demi langkah menggambarkan cara menambahkan, menyesuaikan, dan menghapus penomoran Bates, menjadikan panduan ini sumber daya praktis bagi pengembang yang ingin menyederhanakan alur kerja pemrosesan dokumen.
---

Penomoran Bates secara luas digunakan dalam alur kerja hukum, medis, dan bisnis untuk menugaskan identifier unik dan berurutan ke halaman dalam satu set dokumen. Aspose.PDF untuk Python via .NET menawarkan API yang sederhana dan fleksibel untuk mengotomatisasi proses ini, memungkinkan Anda menerapkan nomor Bates standar secara programatis pada PDF apa pun.

Menggunakan kelas [`BatesNArtifact`](https://reference.aspose.com/pdf/python-net/aspose.pdf/batesnartifact/) , pengembang dapat menyesuaikan sepenuhnya perilaku penomoran—termasuk nomor mulai, jumlah digit, awalan dan akhiran, perataan, dan margin. Setelah dikonfigurasi, artefak dapat diterapkan ke [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) melalui metode `add_bates_numbering` pada [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/), atau ditambahkan sebagai bagian dari daftar objek [`PaginationArtifact`](https://reference.aspose.com/pdf/python-net/aspose.pdf/paginationartifact/). Aspose.PDF juga mendukung gaya konfigurasi berbasis delegasi, memungkinkan kontrol dinamis atas pengaturan artefak pada waktu berjalan.

Selain membuat nomor Bates, API menyediakan cara mudah untuk menghapusnya menggunakan `delete_bates_numbering`, menawarkan fleksibilitas lengkap dalam alur kerja pemrosesan dokumen.

Artikel ini menunjukkan berbagai metode untuk menambah dan menghapus penomoran Bates dalam PDF menggunakan Aspose.PDF untuk Python via .NET, dengan contoh yang jelas tentang konfigurasi, penerapan, dan penghapusan artefak.

## Menambahkan Artefak Penomoran Bates

Contoh ini menunjukkan cara menambahkan penomoran Bates secara programatis ke dokumen PDF menggunakan Aspose.PDF untuk Python via .NET. Dengan mengonfigurasi sebuah [`BatesNArtifact`](https://reference.aspose.com/pdf/python-net/aspose.pdf/batesnartifact/) dengan pengaturan yang diinginkan dan menerapkannya pada halaman dokumen, Anda dapat mengotomatisasi proses penambahan identifier standar pada setiap halaman.

Untuk menambahkan artefak penomoran Bates ke [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/), panggil metode ekstensi `AddBatesNumbering(BatesNArtifact)` pada [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/), dengan mengirimkan sebuah instance [`BatesNArtifact`](https://reference.aspose.com/pdf/python-net/aspose.pdf/batesnartifact/) sebagai parameter:

```python

import aspose.pdf as ap

def add_bates_numbering(path_outfile):
    # Create a new or empty PDF document
    with ap.Document() as document:

        # Add 10 blank pages
        for _ in range(10):
            document.pages.add()

        # Create Bates numbering artifact
        bates = ap.BatesNArtifact(
            start_page=1,
            end_page=0,  # 0 = apply until last page
            subset=ap.Subset.ALL,
            number_of_digits=6,
            start_number=1,
            prefix="",
            suffix="",
            artifact_vertical_alignment=ap.VerticalAlignment.BOTTOM,
            artifact_horizontal_alignment=ap.HorizontalAlignment.RIGHT,
            right_margin=72,
            left_margin=72,
            top_margin=36,
            bottom_margin=36
        )

        # Add Bates numbering to all pages
        document.pages.add_bates_numbering(bates)

        # Save the resulting PDF
        document.save(path_outfile)
```

Atau, Anda dapat mengirimkan koleksi objek [`PaginationArtifact`](https://reference.aspose.com/pdf/python-net/aspose.pdf/paginationartifact/) :

```python

import aspose.pdf as ap

def add_bates_numbering_collection(path_outfile):
    with ap.Document() as document:

        # Add 10 pages
        for _ in range(10):
            document.pages.add()

        # Create Bates artifact
        bates = ap.BatesNArtifact(
            start_page=1,
            end_page=0,
            subset=ap.Subset.ALL,
            number_of_digits=6,
            start_number=1,
            prefix="",
            suffix="",
            artifact_vertical_alignment=ap.VerticalAlignment.BOTTOM,
            artifact_horizontal_alignment=ap.HorizontalAlignment.RIGHT,
            right_margin=72,
            left_margin=72,
            top_margin=36,
            bottom_margin=36
        )

        # Add as a pagination artifact list
        document.pages.add_pagination([bates])

        # Save document
        document.save(path_outfile)
```

Tambahkan artefak penomoran Bates menggunakan delegasi aksi:

```python

import aspose.pdf as ap

def add_bates_numbering_delegate(path_outfile):
    def configure_bates(b):
        """Configure Bates numbering artifact with desired settings."""
        b.start_page = 1
        b.end_page = 0
        b.subset = ap.Subset.ALL
        b.number_of_digits = 6
        b.start_number = 1
        b.prefix = ""
        b.suffix = ""
        b.artifact_vertical_alignment = ap.VerticalAlignment.BOTTOM
        b.artifact_horizontal_alignment = ap.HorizontalAlignment.RIGHT
        b.right_margin = 72
        b.left_margin = 72
        b.top_margin = 36
        b.bottom_margin = 36
        b.text_state.font_size = 10
    
    with ap.Document() as document:

        # Add 10 pages
        for _ in range(10):
            document.pages.add()

        # Use delegate function to configure Bates artifact
        document.pages.add_bates_numbering(configure_bates)

        # Save output PDF
        document.save(path_outfile)
```

## Hapus Penomoran Bates

Untuk menghapus penomoran Bates dari [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/), gunakan metode `delete_bates_numbering()` pada [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/):

```python

import aspose.pdf as ap

def delete_bates_numbering(path_infile, path_outfile):
    with ap.Document(path_infile) as document:

        # Remove Bates numbering from all pages
        document.pages.delete_bates_numbering()

        # Save updated document
        document.save(path_outfile)
```
