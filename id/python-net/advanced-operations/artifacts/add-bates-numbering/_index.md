---
title: Tambahkan Penomoran Bates ke PDF dengan Python
linktitle: Menambahkan Penomoran Bates
type: docs
weight: 10
url: /id/python-net/add-bates-numbering/
description: Pelajari cara menambahkan dan menghapus penomoran Bates pada dokumen PDF menggunakan Python dengan Aspose.PDF for Python via .NET.
lastmod: "2026-06-12"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Tambahkan Penomoran Bates via Python
Abstract: Penomoran Bates adalah fitur penting dalam alur kerja dokumen hukum, medis, dan bisnis, memastikan bahwa setiap halaman dalam satu set menerima identifikasi unik dan berurutan untuk referensi yang dapat diandalkan. Artikel ini menunjukkan bagaimana Aspose.PDF for Python via .NET menyederhanakan otomatisasi penomoran Bates melalui API fleksibel-nya. Dengan menggunakan kelas BatesNArtifact, pengembang dapat mengonfigurasi perilaku penomoran—termasuk jumlah digit, awalan, akhiran, perataan, dan margin—dan menerapkannya secara programatis di seluruh dokumen. Berbagai pendekatan disajikan, mulai dari penerapan artefak langsung hingga konfigurasi berbasis delegasi, menawarkan kontrol statis dan dinamis. Selain itu, API mendukung penghapusan lengkap nomor Bates dengan satu pemanggilan metode, memungkinkan manajemen siklus hidup penuh artefak paginasi. Contoh kode yang jelas dan langkah demi langkah menggambarkan cara menambahkan, menyesuaikan, dan menghapus penomoran Bates, menjadikan panduan ini sumber daya praktis bagi pengembang yang ingin menyederhanakan alur kerja pemrosesan dokumen.
---

Penomoran Bates banyak digunakan dalam alur kerja hukum, medis, dan bisnis untuk menetapkan pengidentifikasi unik dan berurutan ke halaman dalam sekumpulan dokumen. Aspose.PDF for Python via .NET menawarkan API yang sederhana dan fleksibel untuk mengotomatisasi proses ini, memungkinkan Anda menerapkan nomor Bates standar secara programatik pada PDF apa pun.

Menggunakan [`BatesNArtifact`](https://reference.aspose.com/pdf/python-net/aspose.pdf/batesnartifact/) kelas, pengembang dapat sepenuhnya menyesuaikan perilaku penomoran—termasuk nomor awal, jumlah digit, awalan dan akhiran, perataan, serta margin. Setelah dikonfigurasi, artefak dapat diterapkan ke [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) melalui `add_bates_numbering` metode pada [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) atau ditambahkan sebagai bagian dari daftar [`PaginationArtifact`](https://reference.aspose.com/pdf/python-net/aspose.pdf/paginationartifact/) objek. Aspose.PDF juga mendukung gaya konfigurasi berbasis delegasi, memungkinkan kontrol dinamis terhadap pengaturan artifact pada runtime.

Selain membuat nomor Bates, API menyediakan cara mudah untuk menghapusnya menggunakan `delete_bates_numbering`, menawarkan fleksibilitas lengkap dalam alur kerja pemrosesan dokumen.

Artikel ini menunjukkan beberapa metode untuk menambahkan dan menghapus penomoran Bates dalam PDF menggunakan Aspose.PDF for Python via .NET, dengan contoh yang jelas tentang konfigurasi, penerapan, dan penghapusan artifact.

## Menambahkan Artefak Penomoran Bates

Contoh ini menunjukkan bagaimana cara menambahkan penomoran Bates secara programatis ke dokumen PDF menggunakan Aspose.PDF for Python via .NET. Dengan mengkonfigurasi sebuah [`BatesNArtifact`](https://reference.aspose.com/pdf/python-net/aspose.pdf/batesnartifact/) dengan pengaturan yang diinginkan dan menerapkannya ke halaman dokumen, Anda dapat mengotomatiskan proses penambahan pengidentifikasi standar ke setiap halaman.

Untuk menambahkan artefak penomoran Bates ke sebuah [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/), panggil `AddBatesNumbering(BatesNArtifact)` metode ekstensi pada [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/), melewatkan sebuah [`BatesNArtifact`](https://reference.aspose.com/pdf/python-net/aspose.pdf/batesnartifact/) instance sebagai parameter:

```python
import sys
from os import path
import aspose.pdf as ap

def _create_bates_artifact():
    """Create a Bates numbering artifact with default settings."""
    artifact = ap.BatesNArtifact()
    artifact.start_page = 1
    artifact.end_page = 0
    artifact.subset = ap.Subset.ALL
    artifact.number_of_digits = 6
    artifact.start_number = 1
    artifact.prefix = ""
    artifact.suffix = ""
    artifact.artifact_vertical_alignment = ap.VerticalAlignment.BOTTOM
    artifact.artifact_horizontal_alignment = ap.HorizontalAlignment.RIGHT
    artifact.right_margin = 72
    artifact.left_margin = 72
    artifact.top_margin = 36
    artifact.bottom_margin = 36
    return artifact
```

```python
import sys
from os import path
import aspose.pdf as ap

def add_bates_n_artifact(infile, outfile):
    """Add Bates numbering artifact to a PDF document."""
    with ap.Document(infile) as document:
        for _ in range(2):
            document.pages.add()

        bates_artifact = _create_bates_artifact()
        ap.PageCollectionExtensions.add_bates_numbering(document.pages, bates_artifact)
        document.save(outfile)
```

## Menambahkan Penomoran Bates Menggunakan Artefak Paginasi

Menambahkan penomoran Bates ke PDF menggunakan koleksi artefak paginasi di Aspose.PDF for Python:

1. Muat dokumen PDF.
1. Sisipkan halaman tambahan jika diperlukan sebelum menerapkan penomoran.
1. Buat artefak Bates.
1. Konfigurasikan properti artefak.
1. Tambahkan artefak ke koleksi paginasi.
1. Terapkan pagination ke halaman.
1. Simpan dokumen yang diperbarui.

```python
import sys
from os import path
import aspose.pdf as ap

def add_bates_n_artifact_pagination(infile, outfile):
    """Add Bates numbering using pagination artifacts collection."""
    with ap.Document(infile) as document:
        for _ in range(2):
            document.pages.add()

        bates_artifact = _create_bates_artifact()
        ap.PageCollectionExtensions.add_pagination(document.pages, [bates_artifact])
        document.save(outfile)
```

## Hapus Penomoran Bates

Untuk menghapus penomoran Bates dari sebuah [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/), gunakan `delete_bates_numbering()` metode pada [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/):

```python
import sys
from os import path
import aspose.pdf as ap

def delete_bates_numbering(infile, outfile):
    """Delete Bates numbering from a PDF document."""
    with ap.Document(infile) as document:
        ap.PageCollectionExtensions.delete_bates_numbering(document.pages)
        document.save(outfile)
```

## Topik Artefak Terkait

- [Bekerja dengan artefak PDF dalam Python](/pdf/id/python-net/artifacts/)
- [Menambahkan watermark ke PDF dalam Python](/pdf/id/python-net/add-watermarks/)
- [Tambahkan latar belakang PDF di Python](/pdf/id/python-net/add-backgrounds/)
- [Hitung tipe artefak dalam file PDF](/pdf/id/python-net/counting-artifacts/)