---
title: Menambahkan Tanda Air ke PDF dengan Python
linktitle: Menambahkan Tanda Air
type: docs
weight: 30
url: /id/python-net/add-watermarks/
description: Pelajari cara menambahkan elemen watermark ke file PDF dalam Python menggunakan Aspose.PDF for Python via .NET.
lastmod: "2026-06-12"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cara menambahkan tanda air ke PDF dengan Python
Abstract: Artikel ini membahas penggunaan Aspose.PDF for Python via .NET untuk menambahkan watermark ke dokumen PDF melalui pengelolaan artifacts. Ini memperkenalkan kelas utama untuk menangani artifacts - `Artifact` dan `ArtifactCollection`, dan menjelaskan cara mengaksesnya melalui properti `Artifacts` dari kelas `Page`. Artikel tersebut merinci properti kelas `Artifact`, termasuk atribut seperti `contents`, `form`, `image`, `text`, `rectangle`, `rotation`, dan `opacity`, yang memungkinkan manipulasi menyeluruh terhadap artifacts dalam file PDF. Selain itu, contoh praktis disediakan, menunjukkan cara menambahkan watermark secara programatik ke halaman pertama PDF menggunakan Python. Potongan kode menggambarkan pembuatan dan konfigurasi `WatermarkArtifact`, mengatur teks, perataan, rotasi, dan opacity-nya, sebelum menambahkannya ke dokumen PDF dan menyimpan perubahan.
---

Tambahkan artefak watermark ke PDF [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) menggunakan Aspose.PDF for Python via .NET. Watermark adalah lapisan visual yang diterapkan pada halaman untuk tujuan branding, keamanan, atau informasi. Contoh ini menunjukkan cara mengkonfigurasi [`TextState`](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstate/) penampilan, penempatan dengan [`HorizontalAlignment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/horizontalalignment/) dan [`VerticalAlignment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/verticalalignment/), rotasi, dan transparansi sebelum menerapkan watermark ke [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/).

## Ekstrak Watermark dari PDF

1. Muat dokumen PDF.
1. Akses artefak halaman.
1. Filter artefak watermark.
1. Kumpulkan elemen watermark.
1. Ekstrak properti watermark.
1. Keluarkan informasi watermark.

```python
from os import path
import sys
import aspose.pdf as ap

def extract_watermark_from_pdf(infile):
    with ap.Document(infile) as document:
        watermarks = [
            artifact
            for artifact in document.pages[1].artifacts
            if artifact.type == ap.Artifact.ArtifactType.PAGINATION
            and artifact.subtype == ap.Artifact.ArtifactSubtype.WATERMARK
        ]

        for watermark in watermarks:
            print(f"{watermark.text} {watermark.rectangle}")
```

## Tambahkan Watermark ke PDF

Tambahkan watermark teks ke dokumen PDF menggunakan Aspose.PDF for Python:

1. Muat dokumen PDF.
1. Buat keadaan teks.
1. Buat artefak watermark.
1. Atur teks watermark dan gaya.
1. Konfigurasikan penempatan dan rotasi.
1. Atur opacity dan perilaku latar belakang.
1. Lampirkan watermark ke halaman.
1. Simpan dokumen yang diperbarui.

```python
from os import path
import sys
import aspose.pdf as ap

def add_watermark_artifact(infile, outfile):
    with ap.Document(infile) as document:
        text_state = ap.text.TextState()
        text_state.font_size = 72
        text_state.foreground_color = ap.Color.blue_violet
        text_state.font_style = ap.text.FontStyles.BOLD
        text_state.font = ap.text.FontRepository.find_font("Arial")

        watermark = ap.WatermarkArtifact()
        watermark.set_text_and_state("WATERMARK", text_state)
        watermark.artifact_horizontal_alignment = ap.HorizontalAlignment.CENTER
        watermark.artifact_vertical_alignment = ap.VerticalAlignment.CENTER
        watermark.rotation = 60
        watermark.opacity = 0.2
        watermark.is_background = True

        document.pages[1].artifacts.append(watermark)
        document.save(outfile)

```

## Hapus Artefak Watermark dari Halaman PDF 

Hapus artefak watermark dari halaman tertentu dalam dokumen PDF menggunakan API Aspose.PDF for Python. Pendekatan ini menargetkan elemen watermark yang disimpan sebagai artefak halaman (khususnya yang diklasifikasikan sebagai subtipe watermark pagination), mengiterasi mereka, dan menghapusnya sebelum menyimpan dokumen yang diperbarui.

1. Muat dokumen PDF.
1. Akses artefak halaman.
1. Filter artefak watermark.
1. Hapus artefak watermark.
1. Simpan dokumen yang diperbarui.

```python
from os import path
import sys
import aspose.pdf as ap

def delete_watermark_artifact(infile, outfile):
    with ap.Document(infile) as document:
        watermarks = [
            artifact
            for artifact in document.pages[1].artifacts
            if artifact.type == ap.Artifact.ArtifactType.PAGINATION
            and artifact.subtype == ap.Artifact.ArtifactSubtype.WATERMARK
        ]

        for watermark in watermarks:
            document.pages[1].artifacts.delete(watermark)

        document.save(outfile)
```

## Topik Artefak Terkait

- [Bekerja dengan artefak PDF dalam Python](/pdf/id/python-net/artifacts/)
- [Tambahkan latar belakang PDF di Python](/pdf/id/python-net/add-backgrounds/)
- [Menambahkan penomoran Bates ke PDF dalam Python](/pdf/id/python-net/add-bates-numbering/)
- [Hitung tipe artefak dalam file PDF](/pdf/id/python-net/counting-artifacts/)