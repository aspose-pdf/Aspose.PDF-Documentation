---
title: Tambahkan Gambar ke PDF yang Ada di Python
linktitle: Tambahkan Gambar ke PDF
type: docs
weight: 10
url: /id/python-net/add-image-to-existing-pdf-file/
description: Pelajari cara menambahkan gambar ke file PDF yang ada di Python, menempatkannya pada koordinat tetap, mengatur teks alternatif, dan menggunakan kompresi gambar.
lastmod: "2026-06-12"
TechArticle: true
AlternativeHeadline: Tambahkan gambar ke file PDF yang ada menggunakan Python
Abstract: Artikel ini menunjukkan cara menambahkan gambar ke dokumen PDF dengan Aspose.PDF for Python via .NET. Artikel ini mencakup penempatan gambar pada koordinat tetap, menggambar gambar dengan operator PDF tingkat rendah, menetapkan teks alternatif untuk aksesibilitas, dan menyematkan gambar dengan kompresi Flate.
---

## Menambahkan Gambar ke File PDF yang Ada dalam Python

Contoh ini menunjukkan cara menempatkan gambar pada posisi tetap di halaman PDF yang ada menggunakan Aspose.PDF for Python via .NET.

Gunakan contoh-contoh ini ketika Anda perlu menambahkan logo, foto, cap, grafik, atau elemen grafis lainnya ke tata letak PDF yang ada. Anda dapat menempatkan gambar dengan koordinat halaman, menggambarnya dengan operator, menambahkan teks aksesibilitas, atau mengendalikan kompresi gambar.

1. Muat PDF yang ada dengan `ap.Document(infile)`.
1. Pilih halaman target (`document.pages[1]` untuk halaman pertama).
1. Panggilan `page.add_image()` dengan:
    - Jalur file gambar.
    - A `Rectangle` menentukan koordinat penempatan.
1. Simpan PDF yang diperbarui.

```python
import aspose.pdf as ap


def add_image(infile, image_file, outfile):
    document = ap.Document(infile)
    page = document.pages[1]
    page.add_image(image_file, ap.Rectangle(20, 730, 120, 830, True))
    document.save(outfile)
```

## Menambahkan Gambar ke PDF Menggunakan Operator

Pendekatan ini menambahkan gambar dengan operator PDF tingkat rendah alih-alih yang tingkat tinggi `add_image()` pembantu.

1. Buat yang baru `Document` dan tambahkan halaman.
1. Tambahkan gambar ke sumber daya halaman (`page.resources.images`).
1. Buat operator transformasi (`GSave`, `ConcatenateMatrix`, `Do`, `GRestore`).
1. Tambahkan operator ke konten halaman.
1. Simpan PDF yang dihasilkan.

```python
import aspose.pdf as ap
from io import FileIO


def add_image_using_operators(image_file, outfile):
    document = ap.Document()
    page = document.pages.add()
    page.set_page_size(842, 595)
    resources_images = page.resources.images

    with FileIO(image_file, "rb") as image_stream:
        image_id = resources_images.add(image_stream)

    rectangle = ap.Rectangle(0, 0, page.media_box.width, page.media_box.height, True)

    operators = [
        ap.operators.GSave(),
        ap.operators.ConcatenateMatrix(
            ap.Matrix(
                rectangle.urx - rectangle.llx,
                0,
                0,
                rectangle.ury - rectangle.lly,
                rectangle.llx,
                rectangle.lly,
            )
        ),
        ap.operators.Do(image_id),
        ap.operators.GRestore(),
    ]

    page.contents.add(operators)
    document.save(outfile)
```

## Tambahkan Gambar ke PDF dengan Teks Alternatif

Contoh ini menambahkan gambar dan menetapkan teks alternatif untuk aksesibilitas.

1. Buat yang baru `Document` dan tambahkan halaman.
1. Tambahkan gambar ke halaman dengan `page.add_image()`.
1. Dapatkan sumber daya gambar dari `page.resources.images`.
1. Atur teks alternatif menggunakan `try_set_alternative_text()`.
1. Simpan PDF yang dihasilkan.

```python
import aspose.pdf as ap


def add_image_set_alternative_text(image_file, outfile):
    document = ap.Document()
    page = document.pages.add()
    page.set_page_size(842, 595)

    page.add_image(image_file, ap.Rectangle(0, 0, 842, 595, True))
    resources_images = page.resources.images
    x_image = resources_images[1]
    result = x_image.try_set_alternative_text("Alternative text for image", page)

    if result:
        print("Alternative text has been added successfully")

    document.save(outfile)
```

## Menambahkan Gambar ke PDF dengan Kompresi Flate

Contoh ini menyisipkan gambar menggunakan `ImageFilterType.FLATE` kompresi.

1. Buat yang baru `Document` dan tambahkan halaman.
1. Tambahkan gambar ke sumber daya halaman dengan kompresi Flate.
1. Gunakan operator matriks untuk menempatkan dan menggambar gambar.
1. Simpan dokumen.

```python
import aspose.pdf as ap
from io import FileIO


def add_image_to_pdf_with_flate_compression(image_file, outfile):
    document = ap.Document()
    page = document.pages.add()
    resources_images = page.resources.images

    with FileIO(image_file, "rb") as image_stream:
        image_id = resources_images.add(image_stream, ap.ImageFilterType.FLATE)

    rectangle = ap.Rectangle(0, 0, 600, 600, True)
    matrix = ap.Matrix(
        rectangle.urx - rectangle.llx,
        0,
        0,
        rectangle.ury - rectangle.lly,
        rectangle.llx,
        rectangle.lly,
    )

    page.contents.add([ap.operators.GSave()])
    page.contents.add([ap.operators.ConcatenateMatrix(matrix)])
    page.contents.add([ap.operators.Do(image_id)])
    page.contents.add([ap.operators.GRestore()])

    document.save(outfile)
```

## Topik Gambar Terkait

- [Bekerja dengan gambar dalam PDF menggunakan Python](/pdf/id/python-net/working-with-images/)
- [Ganti gambar dalam file PDF yang sudah ada](/pdf/id/python-net/replace-image-in-existing-pdf-file/)
- [Hapus gambar dari file PDF](/pdf/id/python-net/delete-images-from-pdf-file/)
- [Ekstrak gambar dari file PDF](/pdf/id/python-net/extract-images-from-pdf-file/)
