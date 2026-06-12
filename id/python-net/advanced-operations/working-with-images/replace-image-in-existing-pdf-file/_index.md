---
title: Ganti Gambar dalam File PDF yang Ada menggunakan Python
linktitle: Ganti Gambar
type: docs
weight: 70
url: /id/python-net/replace-image-in-existing-pdf-file/
description: Pelajari cara mengganti gambar yang disematkan dalam file PDF yang ada menggunakan Python.
lastmod: "2026-06-12"
TechArticle: true
AlternativeHeadline: Ganti gambar dalam file PDF yang ada dengan Python
Abstract: Artikel ini menunjukkan cara mengganti gambar dalam dokumen PDF dengan Aspose.PDF for Python via .NET. Ini mencakup penggantian gambar berdasarkan indeks sumber daya dan penggantian gambar spesifik yang ditemukan dengan ImagePlacementAbsorber.
---

## Ganti Gambar dalam PDF

Gunakan halaman ini saat Anda perlu memperbarui logo, diagram, atau grafik tersemat lainnya dalam PDF tanpa harus membangun ulang tata letak dokumen.

1. Muat PDF sumber dengan `ap.Document(infile)`.
1. Buka gambar pengganti sebagai aliran biner.
1. Ganti sumber daya gambar berdasarkan indeks pada halaman.
1. Simpan PDF yang diperbarui.

```python
import aspose.pdf as ap
from io import FileIO


def replace_image(infile, image_file, outfile):
    document = ap.Document(infile)

    with FileIO(image_file, "rb") as image_stream:
        document.pages[1].resources.images.replace(1, image_stream)

    document.save(outfile)
```

## Ganti Gambar Tertentu

Contoh ini menggantikan penempatan gambar spesifik yang ditemukan oleh `ImagePlacementAbsorber`.

1. Muat PDF sumber.
1. Buat `ImagePlacementAbsorber` dan kumpulkan penempatan gambar pada halaman.
1. Periksa apakah ada penempatan gambar di halaman.
1. Ganti penempatan yang dipilih dengan aliran gambar baru.
1. Simpan PDF yang diperbarui.

```python
import aspose.pdf as ap
from io import FileIO


def replace_image_with_absorber(infile, image_file, outfile):
    document = ap.Document(infile)
    absorber = ap.ImagePlacementAbsorber()
    document.pages[1].accept(absorber)

    if len(absorber.image_placements) > 0:
        image_placement = absorber.image_placements[1]
        with FileIO(image_file, "rb") as image_stream:
            image_placement.replace(image_stream)

    document.save(outfile)
```

## Topik Gambar Terkait

- [Bekerja dengan gambar dalam PDF menggunakan Python](/pdf/id/python-net/working-with-images/)
- [Hapus gambar dari file PDF](/pdf/id/python-net/delete-images-from-pdf-file/)
- [Ekstrak gambar dari file PDF](/pdf/id/python-net/extract-images-from-pdf-file/)
- [Tambahkan gambar ke file PDF yang ada](/pdf/id/python-net/add-image-to-existing-pdf-file/)
