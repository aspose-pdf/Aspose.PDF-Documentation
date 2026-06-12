---
title: Kelas PdfViewer
linktitle: Kelas PdfViewer
type: docs
weight: 135
url: /id/python-net/pdfviewer-class/
description: Pelajari cara menggunakan kelas PdfViewer dalam Aspose.PDF for Python via .NET untuk mendekode semua halaman PDF, mendekode halaman tertentu, dan memeriksa metadata PDF terkait penampil.
lastmod: "2026-06-12"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Dekode halaman PDF dan periksa data penampil dalam Python dengan PdfViewer
Abstract: Artikel ini menjelaskan cara menggunakan PdfViewer facade dalam Aspose.PDF for Python via .NET untuk tugas dekode halaman dan inspeksi terkait penampil. Pelajari cara mendekode semua halaman PDF, merender halaman tertentu, dan memeriksa properti seperti jumlah halaman, tipe koordinat, dan resolusi.
---

Aspose.PDF for Python via .NET menyediakan [PdfViewer](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfviewer/) fasad untuk bekerja dengan skenario penampilan PDF dan decoding halaman. Salah satu kasus penggunaan umum adalah mengonversi halaman PDF menjadi objek gambar yang kemudian dapat disimpan ke disk.

## Buat pembantu PdfViewer yang dapat digunakan kembali

Sebelum mendekode halaman atau membaca properti terkait penampil, buatlah helper kecil yang menginisialisasi dan mengembalikan sebuah `PdfViewer` instance. Ini menjaga contoh-contoh di bawah tetap mandiri dan membuatnya jelas bagaimana objek viewer dibuat sebelum dihubungkan ke dokumen PDF.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades


def _create_viewer() -> pdf_facades.PdfViewer:
    """Create a PdfViewer configured for decoding examples."""
    viewer = pdf_facades.PdfViewer()
    viewer.coordinate_type = ap.PageCoordinateType.MEDIA_BOX
    viewer.resolution = 150
    viewer.scale_factor = 1.0
    viewer.show_hidden_areas = False
    return viewer
```

## Dekode semua halaman PDF

Gunakan `decode_all_pages()` ketika Anda ingin mengonversi setiap halaman dalam PDF menjadi gambar terpisah. Gambar halaman yang dikembalikan kemudian dapat disimpan satu per satu ke direktori output.

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

from config import initialize_data_dir, set_license


def decode_all_pages(infile: str, output_dir: str) -> None:
    """Decode all pages of a PDF document into image files."""
    viewer = _create_viewer()
    try:
        viewer.open_pdf_file(infile)
        decoded_pages = viewer.decode_all_pages()

        for index, page_image in enumerate(decoded_pages, start=1):
            image_path = path.join(output_dir, f"decode_all_pages_{index}.png")
            page_image.save(image_path)
    finally:
        viewer.close_pdf_file()
```

## Mendekode halaman PDF tertentu

Gunakan `decode_page()` ketika Anda hanya membutuhkan satu halaman dari dokumen. Ini berguna saat membuat pratinjau, thumbnail, atau ekspor khusus halaman.

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

from config import initialize_data_dir, set_license


def decode_specific_page(infile: str, outfile: str, page_number: int = 1) -> None:
    """Decode a specific PDF page into an image file."""
    viewer = _create_viewer()
    try:
        viewer.bind_pdf(infile)
        page_image = viewer.decode_page(page_number)
        page_image.save(outfile)

    finally:
        viewer.close()
```

## Periksa Metadata PDF

The `inspect_pdf_metadata` fungsi menunjukkan cara membuka dokumen PDF dan mengambil metadata dasar yang terkait dengan penampil menggunakan Aspose.PDF. Ini fokus pada mengekstrak informasi yang menggambarkan bagaimana dokumen ditafsirkan dan ditampilkan daripada isinya.

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

from config import initialize_data_dir, set_license


def inspect_pdf_metadata(infile: str) -> None:
    """Open a PDF and print page-count related viewer metadata."""
    viewer = _create_viewer()
    try:
        viewer.open_pdf_file(infile)
        print(f"Page count: {viewer.page_count}")
        print(f"Coordinate type: {viewer.coordinate_type}")
        print(f"Resolution: {viewer.resolution}")
    finally:
        viewer.close_pdf_file()
```
