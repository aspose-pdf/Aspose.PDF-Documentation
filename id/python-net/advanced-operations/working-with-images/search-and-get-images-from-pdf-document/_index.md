---
title: Dapatkan dan Cari Gambar dalam PDF
linktitle: Dapatkan dan Cari Gambar
type: docs
weight: 40
url: /id/python-net/search-and-get-images-from-pdf-document/
description: Pelajari cara mencari dan mengambil gambar dari dokumen PDF menggunakan Python dengan Aspose.PDF.
lastmod: "2025-09-17"
TechArticle: true
AlternativeHeadline: Mencari dan Mengekstrak Gambar dari PDF
Abstract: Pustaka Aspose.PDF untuk Python via .NET menawarkan kemampuan kuat untuk mencari dan mengekstrak gambar dari dokumen PDF. Dengan memanfaatkan kelas 'ImagePlacementAbsorber', pengembang dapat dengan efisien menemukan dan mengakses gambar yang tertanam di semua halaman PDF.
---

## Memeriksa Properti Penempatan Gambar pada Halaman PDF

Contoh ini menunjukkan cara menganalisis dan menampilkan properti semua gambar pada halaman PDF tertentu menggunakan Aspose.PDF untuk Python via .NET.

1. Buat 'ImagePlacementAbsorber' untuk mengumpulkan semua gambar pada halaman.
1. Panggil 'document.pages[1].accept(absorber)' untuk menganalisis penempatan gambar pada halaman pertama.
1. Iterasi melalui 'absorber.image_placements' dan tampilkan properti utama setiap gambar:
- Lebar dan Tinggi (point).
- Koordinat X kiri-bawah (LLX) dan Y kiri-bawah (LLY).
- Resolusi Horizontal (X) dan Vertikal (Y) (DPI).

```python

    import math
    import aspose.pdf as ap
    from aspose.pycore import cast, is_assignable
    from os import path

    path_infile = path.join(self.data_dir, infile)

    document = ap.Document(path_infile)
    absorber = ap.ImagePlacementAbsorber()
    document.pages[1].accept(absorber)

    for image_placement in absorber.image_placements:
        # Display image placement properties for all placements
        print("image width: " + str(image_placement.rectangle.width))
        print("image height: " + str(image_placement.rectangle.height))
        print("image LLX: " + str(image_placement.rectangle.llx))
        print("image LLY: " + str(image_placement.rectangle.lly))
        print("image horizontal resolution: " + str(image_placement.resolution.x))
        print("image vertical resolution: " + str(image_placement.resolution.y))
```

## Ekstrak dan Hitung Jenis Gambar dalam PDF

Fungsi ini menganalisis semua gambar pada halaman pertama PDF dan menghitung berapa banyak gambar grayscale dan RGB.

1. Buat 'ImagePlacementAbsorber' untuk mengumpulkan semua gambar pada halaman.
1. Inisialisasi penghitung untuk gambar grayscale dan RGB.
1. Panggil 'document.pages[1].accept(absorber)' untuk menganalisis penempatan gambar.
1. Cetak total jumlah gambar yang ditemukan.
1. Iterasi melalui setiap gambar dalam 'absorber.image_placements':
- Dapatkan tipe warna gambar menggunakan 'image_placement.image.get_color_type()'.
- Tingkatkan penghitung yang sesuai (grayscale atau rgb).
- Cetak pesan untuk setiap gambar yang menunjukkan apakah itu grayscale atau RGB.

```python

    import math
    import aspose.pdf as ap
    from aspose.pycore import cast, is_assignable
    from os import path

    path_infile = path.join(self.data_dir, infile)

    document = ap.Document(path_infile)
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
```

## Ekstrak Informasi Gambar Detail dari PDF

Fungsi ini menganalisis semua gambar pada halaman pertama PDF dan menghitung dimensi terukur serta resolusi efektif berdasarkan transformasi grafik halaman.

1. Muat PDF dan inisialisasi variabel
1. Kumpulkan sumber daya gambar
1. Proses operator konten halaman:
- 'GSave' - dorong CTM saat ini ke tumpukan.
- 'GRestore' - keluarkan CTM terakhir dari tumpukan.
- 'ConcatenateMatrix' - perbarui CTM saat ini dengan mengalikan matriks operator.
1. Cetak nama gambar, dimensi terukur, dan resolusi yang dihitung.

```python

    import math
    import aspose.pdf as ap
    from aspose.pycore import cast, is_assignable
    from os import path

    path_infile = path.join(self.data_dir, infile)

    document = ap.Document(path_infile)

    default_resolution = 72
    graphics_state = []

    image_names = list(document.pages[1].resources.images.names)

    graphics_state.append(drawing.drawing2d.Matrix(float(1), float(0), float(0), float(1), float(0), float(0)))

    for op in document.pages[1].contents:
        if is_assignable(op, ap.operators.GSave):
            graphics_state.append(cast(drawing.drawing2d.Matrix, graphics_state[-1]).clone())

        elif is_assignable(op, ap.operators.GRestore):
            graphics_state.pop()

        elif is_assignable(op, ap.operators.ConcatenateMatrix):
            opCM = cast(ap.operators.ConcatenateMatrix, op)
            cm = drawing.drawing2d.Matrix(
                float(opCM.matrix.a),
                float(opCM.matrix.b),
                float(opCM.matrix.c),
                float(opCM.matrix.d),
                float(opCM.matrix.e),
                float(opCM.matrix.f),
            )

            graphics_state[-1].multiply(cm)
            continue

        elif is_assignable(op, ap.operators.Do):
            opDo = cast(ap.operators.Do, op)
            if opDo.name in image_names:
                last_ctm = cast(drawing.drawing2d.Matrix, graphics_state[-1])
                index = image_names.index(opDo.name) + 1
                image = document.pages[1].resources.images[index]

                scaled_width = math.sqrt(last_ctm.elements[0] ** 2 + last_ctm.elements[1] ** 2)
                scaled_height = math.sqrt(last_ctm.elements[2] ** 2 + last_ctm.elements[3] ** 2)

                original_width = image.width
                original_height = image.height

                res_horizontal = original_width * default_resolution / scaled_width
                res_vertical = original_height * default_resolution / scaled_height

                print(
                    f"{self.data_dir}image {opDo.name} "
                    f"({scaled_width:.2f}:{scaled_height:.2f}): "
                    f"res {res_horizontal:.2f} x {res_vertical:.2f}"
                )
```

## Ekstrak Teks Alternatif dari Gambar dalam PDF

Fungsi ini mengambil teks alternatif (alt text) dari semua gambar pada halaman pertama PDF, berguna untuk aksesibilitas dan pemeriksaan kepatuhan PDF/UA.

1. Muat dokumen PDF menggunakan 'ap.Document()'.
1. Buat 'ImagePlacementAbsorber' untuk mengumpulkan semua gambar pada halaman.
1. Terima absorber pada halaman pertama (page.accept(absorber)).
1. Iterasi melalui setiap gambar dalam 'absorber.image_placements':
- Cetak nama gambar dalam koleksi sumber daya halaman (get_name_in_collection()).
- Ambil teks alternatif menggunakan 'get_alternative_text(page)'.
- Cetak baris pertama dari teks alt.

```python

    import math
    import aspose.pdf as ap
    from aspose.pycore import cast, is_assignable
    from os import path

    path_infile = path.join(self.data_dir, infile)

    document = ap.Document(path_infile)
    absorber = ap.ImagePlacementAbsorber()
    page = document.pages[1]
    page.accept(absorber)

    for image_placement in absorber.image_placements:
        print(
            "Name in collection: "
            + str(image_placement.image.get_name_in_collection())
        )
        lines = image_placement.image.get_alternative_text(page)
        print("Alt Text: " + lines[0])
```
