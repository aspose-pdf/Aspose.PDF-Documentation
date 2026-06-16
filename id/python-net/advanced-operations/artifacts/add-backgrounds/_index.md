---
title: Tambahkan Latar Belakang PDF di Python
linktitle: Menambahkan latar belakang
type: docs
weight: 20
url: /id/python-net/add-backgrounds/
description: Pelajari cara menambahkan gambar latar belakang ke halaman PDF dalam Python menggunakan kelas BackgroundArtifact di Aspose.PDF for Python via .NET.
lastmod: "2026-06-12"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cara menambahkan latar belakang ke PDF dengan Python
Abstract: Artikel ini membahas penggunaan gambar latar belakang dalam dokumen PDF menggunakan Aspose.PDF for Python via .NET. Artikel ini menyoroti kemampuan menambahkan watermark atau desain halus ke dokumen dengan memanfaatkan kelas `BackgroundArtifact`, yang memungkinkan penyertaan gambar latar belakang ke objek halaman individual. Artikel ini menyediakan contoh kode praktis yang mendemonstrasikan cara mengimplementasikan fitur ini. Prosesnya meliputi pembuatan dokumen PDF baru, menambahkan halaman, membuat objek `BackgroundArtifact`, menetapkan gambar latar belakang, dan menambahkan artefak latar belakang ke koleksi artefak halaman. Akhirnya, dokumen yang telah dimodifikasi disimpan sebagai file PDF. Teknik ini memungkinkan penyajian visual yang lebih baik untuk dokumen PDF.
---

## Menambahkan Gambar Latar Belakang ke PDF

Gambar latar dapat digunakan untuk menambahkan watermark, atau desain halus lainnya, ke dokumen. Dalam Aspose.PDF for Python via .NET, setiap dokumen PDF adalah kumpulan halaman dan setiap halaman berisi kumpulan artefak. The [BackgroundArtifact](https://reference.aspose.com/pdf/python-net/aspose.pdf/backgroundartifact/) kelas dapat digunakan untuk menambahkan gambar latar ke objek halaman.

Pendekatan ini berguna ketika Anda perlu menempatkan gambar dekoratif di belakang konten PDF utama tanpa mengubahnya menjadi teks dokumen yang dapat dicari.

Cuplikan kode berikut menunjukkan cara menambahkan gambar latar belakang ke halaman PDF menggunakan objek BackgroundArtifact dengan Python.

1. Muat dokumen PDF.
1. Buat artefak latar belakang.
1. Muat file gambar.
1. Lampirkan artefak ke halaman.
1. Simpan dokumen yang diperbarui.

```python

from os import path
from io import FileIO
import aspose.pdf as ap
import sys

def add_background_image_to_pdf(infile, imagefile, outfile):
    """Add a background image to a PDF document as an artifact."""
    with ap.Document(infile) as document:
        artifact = ap.BackgroundArtifact()
        artifact.background_image = FileIO(imagefile, "rb")
        document.pages[1].artifacts.append(artifact)
        document.save(outfile)
```

## Tambahkan Gambar Latar Belakang dengan Opasitas ke PDF

Tambahkan gambar latar belakang semi-transparan ke halaman PDF menggunakan Aspose.PDF for Python.

Dengan menerapkan opasitas, gambar latar belakang menjadi sebagian transparan, memungkinkan konten halaman asli (teks, gambar, dll.) tetap terlihat jelas. Ini sangat berguna untuk:

- Watermark
- Overlay merek
- Peningkatan desain yang halus

Latar belakang ditambahkan sebagai artefak, memastikan tetap berada di belakang semua konten halaman.

1. Muat dokumen PDF.
1. Buat artefak latar belakang.
1. Muat file gambar.
1. Atur tingkat opasitas.
1. Lampirkan artefak ke halaman.
1. Simpan dokumen yang diperbarui.

```python

from os import path
from io import FileIO
import aspose.pdf as ap
import sys

def add_background_image_with_opacity_to_pdf(infile, imagefile, outfile):
    """Add a background image with opacity to a PDF document as an artifact."""
    with ap.Document(infile) as document:
        artifact = ap.BackgroundArtifact()
        artifact.background_image = FileIO(imagefile, "rb")
        artifact.opacity = 0.5
        document.pages[1].artifacts.append(artifact)
        document.save(outfile)
```

## Tambahkan Warna Latar Belakang ke PDF

Terapkan warna latar belakang solid ke halaman PDF menggunakan Aspose.PDF for Python.

1. Muat dokumen PDF.
1. Buat artefak latar belakang.
1. Atur warna latar belakang.
1. Lampirkan artefak ke halaman.
1. Simpan dokumen yang diperbarui.

```python

from os import path
from io import FileIO
import aspose.pdf as ap
import sys

def add_background_color_to_pdf(infile, outfile):
    """Add a solid color background to a PDF document as an artifact."""
    with ap.Document(infile) as document:
        artifact = ap.BackgroundArtifact()
        artifact.background_color = ap.Color.dark_khaki
        document.pages[1].artifacts.append(artifact)
        document.save(outfile)
```

## Hapus Latar Belakang dari PDF

Hapus artefak latar belakang dari halaman PDF menggunakan Aspose.PDF for Python.
Latar belakang dalam PDF sering disimpan sebagai artefak, dan metode ini secara selektif mengidentifikasi serta menghapus hanya artefak yang diklasifikasikan sebagai elemen latar belakang.

1. Muat dokumen PDF.
1. Akses artefak halaman.
1. Saring artefak latar belakang.
1. Kumpulkan elemen latar belakang.
1. Hapus artefak latar belakang.
1. Simpan dokumen yang diperbarui.

```python

from os import path
from io import FileIO
import aspose.pdf as ap
import sys

def remove_background(infile, outfile):
    with ap.Document(infile) as document:
        backgrounds = [
            artifact
            for artifact in document.pages[1].artifacts
            if artifact.type == ap.Artifact.ArtifactType.PAGINATION
            and artifact.subtype == ap.Artifact.ArtifactSubtype.BACKGROUND
        ]

        for background in backgrounds:
            document.pages[1].artifacts.delete(background)

        document.save(outfile)
```

## Topik Artefak Terkait

- [Bekerja dengan artefak PDF dalam Python](/pdf/id/python-net/artifacts/)
- [Menambahkan watermark ke PDF dalam Python](/pdf/id/python-net/add-watermarks/)
- [Menambahkan penomoran Bates ke PDF dalam Python](/pdf/id/python-net/add-bates-numbering/)
- [Hitung tipe artefak dalam file PDF](/pdf/id/python-net/counting-artifacts/)