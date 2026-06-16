---
title: Dapatkan dan Cari Gambar dalam PDF
linktitle: Dapatkan dan Cari Gambar
type: docs
weight: 40
url: /id/python-net/search-and-get-images-from-pdf-document/
description: Pelajari cara mencari dan memeriksa gambar dalam dokumen PDF menggunakan Python.
lastmod: "2026-06-12"
TechArticle: true
AlternativeHeadline: Cari dan periksa gambar dalam file PDF dengan Python
Abstract: Artikel ini menunjukkan cara mencari dan memeriksa gambar dalam dokumen PDF dengan Aspose.PDF for Python via .NET. Ini mencakup penggunaan ImagePlacementAbsorber untuk menganalisis penempatan gambar, ukuran, resolusi, dan teks alternatif.
---

## Periksa Properti Penempatan Gambar dalam Halaman PDF

Contoh ini menunjukkan cara menganalisis dan menampilkan properti semua gambar pada halaman PDF tertentu menggunakan Aspose.PDF for Python via .NET.

Gunakan halaman ini ketika Anda perlu mengaudit penempatan gambar, memeriksa resolusi gambar, atau mengidentifikasi objek gambar yang disematkan di seluruh halaman PDF.

1. Buat 'ImagePlacementAbsorber' untuk mengumpulkan semua gambar di halaman.
1. Panggil 'document.pages[1].accept(absorber)' untuk menganalisis penempatan gambar pada halaman pertama.
1. Iterasi melalui 'absorber.image_placements' dan tampilkan properti kunci dari setiap gambar:
    - Lebar dan Tinggi (point).
    - Koordinat X kiri-bawah (LLX) dan Y kiri-bawah (LLY).
    - Resolusi Horizontal (X) dan Vertikal (Y) (DPI).

```python
import math
import aspose.pdf as ap
from aspose.pycore import cast, is_assignable
import aspose.pydrawing as drawing

def extract_image_params(infile):
    document = ap.Document(infile)
    absorber = ap.ImagePlacementAbsorber()
    document.pages[1].accept(absorber)

    for image_placement in absorber.image_placements:
        print("image width: " + str(image_placement.rectangle.width))
        print("image height: " + str(image_placement.rectangle.height))
        print("image LLX: " + str(image_placement.rectangle.llx))
        print("image LLY: " + str(image_placement.rectangle.lly))
        print("image horizontal resolution: " + str(image_placement.resolution.x))
        print("image vertical resolution: " + str(image_placement.resolution.y))
```

## Ekstrak dan Hitung Jenis Gambar dalam PDF

Fungsi ini menganalisis semua gambar pada halaman pertama sebuah PDF dan menghitung berapa banyak gambar grayscale dan RGB.

1. Buat 'ImagePlacementAbsorber' untuk mengumpulkan semua gambar di halaman.
1. Inisialisasi penghitung untuk gambar skala abu-abu dan RGB.
1. Panggil 'document.pages[1].accept(absorber)' untuk menganalisis penempatan gambar.
1. Cetak total jumlah gambar yang ditemukan.
1. Iterasi melalui setiap gambar dalam 'absorber.image_placements':
    - Dapatkan tipe warna gambar menggunakan 'image_placement.image.get_color_type()'.
    - Tingkatkan penghitung yang sesuai (grayscaled atau rgb).
    - Cetak pesan untuk setiap gambar yang menunjukkan apakah itu grayscale atau RGB.

```python
import math
import aspose.pdf as ap
from aspose.pycore import cast, is_assignable
import aspose.pydrawing as drawing

def extract_image_types_from_pdf(infile):
    """
    Extract and count image types (grayscale/RGB) with resolution analysis.

    Args:
        infile (str): Input PDF filename

    Returns:
        None

    Example:
        extract_image_types_from_pdf("sample_extr.pdf")

    Note:
        Prints total images count, color type for each image, and resolution info.
    """

    document = ap.Document(infile)
    absorber = ap.ImagePlacementAbsorber()

    # Counters for grayscale and RGB images
    grayscaled = 0
    rgb = 0

    document.pages[1].accept(absorber)

    print("--------------------------------")
    print("Total Images = " + str(len(absorber.image_placements)))

    image_counter = 1

    for image_placement in absorber.image_placements:
        # Determine the color type of the image
        colorType = image_placement.image.get_color_type()
        if colorType == ap.ColorType.GRAYSCALE:
            grayscaled += 1
            print(f"Image {image_counter} is Grayscale...")
        elif colorType == ap.ColorType.RGB:
            rgb += 1
            print(f"Image {image_counter} is RGB...")
        image_counter += 1

    print("--------------------------------")
    print("Grayscale Images = " + str(grayscaled))
    print("RGB Images = " + str(rgb))
```

## Ekstrak Informasi Gambar Rinci dari PDF

Fungsi ini menganalisis semua gambar pada halaman pertama sebuah PDF dan menghitung dimensi yang terskala serta resolusi efektif berdasarkan transformasi grafis halaman.

1. Muat PDF dan inisialisasi variabel
1. Kumpulkan sumber daya gambar
1. Proses operator konten halaman:
    - 'GSave' - dorong CTM saat ini ke dalam tumpukan.
    - 'GRestore' - keluarkan CTM terakhir dari stack.
    - 'ConcatenateMatrix' - perbarui CTM saat ini dengan mengalikan dengan matriks operator.
1. Cetak nama gambar, dimensi yang diskalakan, dan resolusi yang dihitung.

```python
import math
import aspose.pdf as ap
from aspose.pycore import cast, is_assignable
import aspose.pydrawing as drawing

def extract_image_information_from_pdf(infile):
    with ap.Document(infile) as document:
        default_resolution = 72
        graphics_state = []

        image_names = list(document.pages[1].resources.images.names)

        graphics_state.append(
            drawing.drawing2d.Matrix(
                float(1), float(0), float(0), float(1), float(0), float(0)
            )
        )

        for op in document.pages[1].contents:
            if is_assignable(op, ap.operators.GSave):
                graphics_state.append(
                    cast(drawing.drawing2d.Matrix, graphics_state[-1]).clone()
                )

            elif is_assignable(op, ap.operators.GRestore):
                graphics_state.pop()

            elif is_assignable(op, ap.operators.ConcatenateMatrix):
                op_cm = cast(ap.operators.ConcatenateMatrix, op)
                cm = drawing.drawing2d.Matrix(
                    float(op_cm.matrix.a),
                    float(op_cm.matrix.b),
                    float(op_cm.matrix.c),
                    float(op_cm.matrix.d),
                    float(op_cm.matrix.e),
                    float(op_cm.matrix.f),
                )

                graphics_state[-1].multiply(cm)
                continue

            elif is_assignable(op, ap.operators.Do):
                op_do = cast(ap.operators.Do, op)
                if op_do.name in image_names:
                    last_ctm = cast(drawing.drawing2d.Matrix, graphics_state[-1])
                    index = image_names.index(op_do.name) + 1
                    image = document.pages[1].resources.images[index]

                    scaled_width = math.sqrt(
                        last_ctm.elements[0] ** 2 + last_ctm.elements[1] ** 2
                    )
                    scaled_height = math.sqrt(
                        last_ctm.elements[2] ** 2 + last_ctm.elements[3] ** 2
                    )

                    original_width = image.width
                    original_height = image.height

                    res_horizontal = (
                        original_width * default_resolution / scaled_width
                    )
                    res_vertical = (
                        original_height * default_resolution / scaled_height
                    )

                    info = (
                        f"{infile} image {op_do.name} "
                        f"({scaled_width:.2f}:{scaled_height:.2f}): "
                        f"res {res_horizontal:.2f} x {res_vertical:.2f}\n"
                    )
                    print(info.rstrip())
```

## Ekstrak Teks Alternatif dari Gambar dalam PDF

Fungsi ini mengambil teks alternatif (alt text) dari semua gambar pada halaman pertama sebuah PDF, berguna untuk pemeriksaan aksesibilitas dan kepatuhan PDF/UA.

1. Muat dokumen PDF menggunakan 'ap.Document()'.
1. Buat 'ImagePlacementAbsorber' untuk mengumpulkan semua gambar di halaman.
1. Terima absorber pada halaman pertama (page.accept(absorber)).
1. Iterasi melalui setiap gambar dalam 'absorber.image_placements':
    - Cetak nama gambar dalam koleksi sumber daya halaman (get_name_in_collection()).
    - Dapatkan teks alternatif menggunakan 'get_alternative_text(page)'.
    - Cetak baris pertama dari alt text.

```python
import math
import aspose.pdf as ap
from aspose.pycore import cast, is_assignable
import aspose.pydrawing as drawing

def extract_image_alt_text(infile):
    document = ap.Document(infile)
    absorber = ap.ImagePlacementAbsorber()
    page = document.pages[1]
    page.accept(absorber)

    for image_placement in absorber.image_placements:
        print(
            "Name in collection: " + str(image_placement.image.get_name_in_collection())
        )
        lines = image_placement.image.get_alternative_text(page)
        print("Alt Text: " + lines[0])
```

## Topik Gambar Terkait

- [Bekerja dengan gambar dalam PDF menggunakan Python](/pdf/id/python-net/working-with-images/)
- [Ekstrak gambar dari file PDF](/pdf/id/python-net/extract-images-from-pdf-file/)
- [Ganti gambar dalam file PDF yang sudah ada](/pdf/id/python-net/replace-image-in-existing-pdf-file/)
- [Tambahkan gambar ke file PDF yang ada](/pdf/id/python-net/add-image-to-existing-pdf-file/)
