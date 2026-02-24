---
title: Menambahkan Watermark ke PDF menggunakan Python
linktitle: Menambahkan Watermark
type: docs
weight: 30
url: /id/python-net/add-watermarks/
description: Artikel ini menjelaskan fitur-fitur bekerja dengan artefak dan menambahkan watermark pada PDF secara programatis menggunakan Python.
lastmod: "2025-11-21"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cara menambahkan watermark ke PDF dengan Python
Abstract: Artikel ini membahas penggunaan Aspose.PDF untuk Python via .NET untuk menambahkan watermark ke dokumen PDF melalui pengelolaan artefak. Artikel ini memperkenalkan kelas utama untuk menangani artefak - `Artifact` dan `ArtifactCollection`, serta menjelaskan cara mengaksesnya melalui properti `Artifacts` pada kelas `Page`. Artikel ini merinci properti kelas `Artifact`, termasuk atribut seperti `contents`, `form`, `image`, `text`, `rectangle`, `rotation`, dan `opacity`, yang memungkinkan manipulasi lengkap artefak dalam file PDF. Selain itu, contoh praktis disediakan, yang menunjukkan cara menambahkan watermark secara programatis ke halaman pertama PDF menggunakan Python. Potongan kode menggambarkan pembuatan dan konfigurasi `WatermarkArtifact`, menetapkan teks, perataan, rotasi, dan opacity-nya, sebelum menambahkannya ke dokumen PDF dan menyimpan perubahan.
---

## Contoh Pemrograman: Cara Menambahkan Watermark pada File PDF

Tambahkan artefak watermark ke PDF [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) menggunakan Aspose.PDF untuk Python via .NET. Watermark adalah lapisan visual yang diterapkan pada halaman untuk tujuan branding, keamanan, atau informasi. Contoh ini menunjukkan cara mengonfigurasi tampilan [`TextState`](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstate/) , penempatan dengan [`HorizontalAlignment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/horizontalalignment/) dan [`VerticalAlignment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/verticalalignment/), rotasi, dan transparansi sebelum menerapkan watermark ke [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/).

1. Buat artefak watermark (lihat [`WatermarkArtifact`](https://reference.aspose.com/pdf/python-net/aspose.pdf/watermarkartifact/)).
1. Konfigurasikan keadaan teks (lihat [`TextState`](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstate/)).
1. Kaitkan teks ke watermark.
1. Tentukan posisi dan gaya menggunakan [`HorizontalAlignment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/horizontalalignment/) dan [`VerticalAlignment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/verticalalignment/).
1. Lampirkan watermark ke [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) melalui koleksi [`Artifacts`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) milik halaman (lihat [`ArtifactCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/artifactcollection/)).
1. Simpan [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) yang telah diperbarui menggunakan [`Document.save()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods).

```python

import aspose.pdf as ap

def add_watermark(input_pdf, output_pdf):
    # Load the existing PDF document
    document = ap.Document(input_pdf)

    # Create a watermark artifact
    watermark = ap.WatermarkArtifact()

    # Configure text state for the watermark
    text_state = ap.text.TextState()
    text_state.font_size = 72
    text_state.foreground_color = ap.Color.blue
    text_state.font = ap.text.FontRepository.find_font("Courier")

    # Apply text and style to the watermark
    watermark.set_text_and_state("WATERMARK", text_state)

    # Position and style settings
    watermark.artifact_horizontal_alignment = ap.HorizontalAlignment.CENTER
    watermark.artifact_vertical_alignment = ap.VerticalAlignment.CENTER
    watermark.rotation = 45
    watermark.opacity = 0.5
    watermark.is_background = True

    # Add watermark to the first page
    document.pages[1].artifacts.append(watermark)

    # Save the updated PDF
    document.save(output_pdf)
```


