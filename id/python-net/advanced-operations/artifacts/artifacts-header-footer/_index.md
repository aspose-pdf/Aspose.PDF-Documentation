---
title: Kelola Header dan Footer PDF menggunakan Python
linktitle: Kelola Header dan Footer PDF
type: docs
weight: 70
url: /id/python-net/artifacts-header-footer/
description: Pelajari cara mengelola header dan footer dalam dokumen PDF dengan Python dan Aspose.PDF.
lastmod: "2026-06-12"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cara Menambahkan, Menyesuaikan, dan Menghapus Header serta Footer PDF menggunakan Python
Abstract: Mengelola header dan footer merupakan kebutuhan umum saat bekerja dengan dokumen PDF dalam bisnis, penerbitan, dan alur kerja otomasi. Artikel ini menunjukkan cara menggunakan Aspose.PDF for Python untuk menambahkan header dan footer yang tampak profesional dengan gaya khusus seperti Font, ukuran, warna, dan perataan. Artikel ini juga memperlihatkan cara mendeteksi dan menghapus artefak paginasi yang ada seperti header dan footer dari halaman PDF. Dengan fungsi yang dapat digunakan kembali dan contoh yang jelas, pengembang dapat dengan cepat mengintegrasikan fitur-fitur ini ke dalam sistem pemrosesan dokumen untuk branding, pelaporan, atau pembersihan file.
---

## Buat Artefak Teks Bergaya

Fungsi utilitas ini menjelaskan cara membuat artefak teks yang dapat digunakan kembali untuk halaman PDF menggunakan Aspose.PDF for Python. Fungsi ini dirancang untuk menghasilkan header atau footer yang bergaya dengan pemformatan konsisten, termasuk pengaturan font, warna, ukuran, dan perataan. Fungsi ini mengabstraksi pembuatan artefak sehingga dapat digunakan kembali untuk dekorasi teks tingkat halaman yang berbeda.

1. Instansiasi objek artefak.
1. Atur konten teks artefak.
1. Terapkan gaya teks.
1. Atur perataan.
1. Kembalikan artefak yang dikonfigurasi.

```python
from os import path
import aspose.pdf as ap
import sys

def _create_text_artifact(artifact_class, text):
    """Create a text artifact (header/footer) with common styling."""
    artifact = artifact_class()
    artifact.text = text
    artifact.text_state.font_size = 14
    artifact.text_state.font = ap.text.FontRepository.find_font("Arial")
    artifact.text_state.foreground_color = ap.Color.navy
    artifact.artifact_horizontal_alignment = ap.HorizontalAlignment.CENTER
    return artifact

```

## Tambahkan Header ke PDF

1. Buka PDF input.
1. Buat HeaderArtifact dengan teks "Sample Header".
1. Tambahkan ke halaman pertama.
1. Simpan PDF yang diperbarui.

```python
from os import path
import aspose.pdf as ap
import sys

def add_header_artifact(infile, outfile):
    """Add a header artifact to the first page of a PDF document."""
    with ap.Document(infile) as document:
        header = _create_text_artifact(ap.HeaderArtifact, "Sample Header")
        document.pages[1].artifacts.append(header)
        document.save(outfile)
```

## Tambahkan Footer ke PDF

1. Buka PDF input.
1. Buat FooterArtifact dengan teks "Sample Footer".
1. Tambahkan ke halaman pertama.
1. Simpan file output.

```python
from os import path
import aspose.pdf as ap
import sys

def add_footer_artifact(infile, outfile):
    """Add a footer artifact to the first page of a PDF document."""
    with ap.Document(infile) as document:
        footer = _create_text_artifact(ap.FooterArtifact, "Sample Footer")
        document.pages[1].artifacts.append(footer)
        document.save(outfile)
```

## Hapus Artefak Header atau Footer

1. Buka PDF.
1. Temukan artefak yang ditandai sebagai header atau footer pagination.
1. Hapus mereka dari halaman pertama.
1. Simpan dokumen yang sudah dibersihkan.

```python
from os import path
import aspose.pdf as ap
import sys

def delete_header_footer_artifact(infile, outfile):
    with ap.Document(infile) as document:
        header_footers = [
            artifact
            for artifact in document.pages[1].artifacts
            if artifact.type == ap.Artifact.ArtifactType.PAGINATION
            and (
                artifact.subtype == ap.Artifact.ArtifactSubtype.HEADER
                or artifact.subtype == ap.Artifact.ArtifactSubtype.FOOTER
            )
        ]

        for art in header_footers:
            document.pages[1].artifacts.delete(art)

        document.save(outfile)
```

## Topik Artefak Terkait

- [Bekerja dengan artefak PDF dalam Python](/pdf/id/python-net/artifacts/)
- [Tambahkan latar belakang PDF di Python](/pdf/id/python-net/add-backgrounds/)
- [Menambahkan penomoran Bates ke PDF dalam Python](/pdf/id/python-net/add-bates-numbering/)
- [Hitung tipe artefak dalam file PDF](/pdf/id/python-net/counting-artifacts/)