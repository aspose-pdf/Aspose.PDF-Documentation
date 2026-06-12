---
title: Ekstrak Gambar dari File PDF menggunakan Python
linktitle: Ekstrak Gambar
type: docs
weight: 30
url: /id/python-net/extract-images-from-pdf-file/
description: Pelajari cara mengekstrak gambar tersemat dari file PDF dalam Python.
lastmod: "2026-06-12"
TechArticle: true
AlternativeHeadline: Ekstrak gambar dari file PDF dengan Python
Abstract: Artikel ini menunjukkan cara mengekstrak gambar dari dokumen PDF dengan Aspose.PDF for Python via .NET. Artikel ini mencakup mengekstrak satu gambar tersemat dan mengekspor gambar yang ditemukan dalam wilayah persegi panjang tertentu pada halaman.
---

Gunakan halaman ini saat Anda perlu menggunakan kembali grafik tersemat, mengarsipkan aset gambar, atau memproses konten gambar di luar PDF.

1. Muat PDF sumber dengan `ap.Document(infile)`.
1. Pilih halaman target dan indeks sumber daya gambar.
1. Simpan objek gambar ke aliran output.

```python
import aspose.pdf as ap
from io import FileIO


def extract_image(infile, outfile):
    document = ap.Document(infile)
    x_image = document.pages[1].resources.images[1]
    with FileIO(outfile, "wb") as output_image:
        x_image.save(output_image)
```

## Ekstrak Gambar dari Wilayah Spesifik dalam PDF

Contoh ini mengekstrak gambar yang berada dalam wilayah persegi panjang yang ditentukan pada halaman PDF dan menyimpannya sebagai file terpisah.

1. Muat PDF sumber.
1. Buat `ImagePlacementAbsorber` dan terima itu di halaman target.
1. Definisikan persegi panjang target.
1. Iterasi melalui penempatan gambar dan periksa apakah batas masing-masing gambar cocok dengan wilayah.
1. Simpan gambar yang cocok ke file output.

```python
import aspose.pdf as ap
from io import FileIO


def extract_image_from_specific_region(infile, outfile):
    document = ap.Document(infile)
    rectangle = ap.Rectangle(0, 0, 590, 590, True)
    absorber = ap.ImagePlacementAbsorber()
    document.pages[1].accept(absorber)

    index = 1
    for image_placement in absorber.image_placements:
        point1 = ap.Point(image_placement.rectangle.llx, image_placement.rectangle.lly)
        point2 = ap.Point(image_placement.rectangle.urx, image_placement.rectangle.ury)

        if rectangle.contains(point1, True) and rectangle.contains(point2, True):
            with FileIO(outfile.replace("index", str(index)), "wb") as output_image:
                image_placement.image.save(output_image)
            index += 1
```

## Topik Gambar Terkait

- [Bekerja dengan gambar dalam PDF menggunakan Python](/pdf/id/python-net/working-with-images/)
- [Ganti gambar dalam file PDF yang sudah ada](/pdf/id/python-net/replace-image-in-existing-pdf-file/)
- [Hapus gambar dari file PDF](/pdf/id/python-net/delete-images-from-pdf-file/)
- [Tambahkan gambar ke file PDF yang ada](/pdf/id/python-net/add-image-to-existing-pdf-file/)
