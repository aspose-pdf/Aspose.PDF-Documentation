---
title: Ekstrak Gambar dari File PDF menggunakan Python
linktitle: Ekstrak Gambar
type: docs
weight: 30
url: /id/python-net/extract-images-from-pdf-file/
description: Bagian ini menunjukkan cara mengekstrak gambar dari file PDF menggunakan perpustakaan Python.
lastmod: "2025-09-27"
TechArticle: true
AlternativeHeadline: Ekstrak gambar dari PDF dengan Python
Abstract: Artikel ini membahas proses mengekstrak gambar dari file PDF menggunakan Aspose.PDF untuk Python. Artikel ini menyoroti kegunaan memisahkan gambar untuk tujuan seperti manajemen, arsip, analisis, atau berbagi. Dijelaskan bahwa gambar dalam PDF disimpan dalam koleksi sumber daya setiap halaman, khususnya dalam koleksi XImage. Untuk mengekstrak gambar, pengguna dapat mengakses halaman tertentu dan mengambil gambar menggunakan indeksnya dari koleksi Images. Objek XImage yang dikembalikan oleh indeks menyediakan metode `save()` untuk menyimpan gambar yang diekstrak. Sebuah potongan kode disediakan untuk mendemonstrasikan langkah-langkah yang diperlukan untuk membuka dokumen PDF, mengekstrak gambar tertentu dari halaman kedua menggunakan indeksnya, dan menyimpannya ke file.
---

Apakah Anda perlu memisahkan gambar dari file PDF Anda? Untuk manajemen, arsip, analisis, atau berbagi gambar dokumen Anda yang lebih sederhana, gunakan **Aspose.PDF for Python** dan ekstrak gambar dari file PDF.

1. Muat dokumen PDF dengan 'ap.Document()'.
1. Akses halaman yang diinginkan dari dokumen (document.pages[1]).
1. Pilih gambar dari sumber daya halaman (misalnya, resources.images[1]).
1. Buat aliran keluaran (FileIO) untuk file target.
1. Simpan gambar yang diekstrak menggunakan 'xImage.save(output_image)'.

```python

    import aspose.pdf as ap
    from io import FileIO
    from os import path

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, outfile)

    document = ap.Document(path_infile)
    xImage = document.pages[1].resources.images[1]
    with FileIO(path_outfile, "w") as output_image:
        xImage.save(output_image)
```

## Ekstrak Gambar dari Wilayah Spesifik dalam PDF

Contoh ini mengekstrak gambar yang berada dalam wilayah persegi panjang tertentu pada halaman PDF dan menyimpannya sebagai file terpisah.

1. Muat dokumen PDF menggunakan 'ap.Document'.
1. Buat 'ImagePlacementAbsorber' untuk mengumpulkan semua gambar pada halaman pertama.
1. Panggil 'document.pages[1].accept(absorber)' untuk menganalisis penempatan gambar.
1. Iterasi melalui semua gambar dalam 'absorber.image_placements':
- Dapatkan kotak pembatas gambar (llx, lly, urx, ury).
- Periksa apakah kedua sudut persegi panjang gambar berada di dalam persegi panjang target (rectangle.contains()).
- Jika benar, simpan gambar ke file menggunakan FileIO, mengganti 'index' dalam nama file dengan nomor berurutan.
1. Tingkatkan indeks untuk setiap gambar yang disimpan.

```python

    import aspose.pdf as ap
    from io import FileIO
    from os import path

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, outfile)

    rectangle = ap.Rectangle(0, 0, 590, 590, True)

    document = ap.Document(path_infile)
    absorber = ap.ImagePlacementAbsorber()
    document.pages[1].accept(absorber)
    index = 1
    for image_placement in absorber.image_placements:
        point1 = ap.Point(
            image_placement.rectangle.llx, image_placement.rectangle.lly
        )
        point2 = ap.Point(
            image_placement.rectangle.urx, image_placement.rectangle.urx
        )
        if rectangle.contains(point1, True) and rectangle.contains(point2, True):
            with FileIO(path_outfile.replace("index", str(index)), "w") as output_image:
                image_placement.image.save(output_image)
            index = index + 1
```

## Ekstrak Informasi Gambar dari PDF

Contoh di bawah ini menunjukkan cara menganalisis gambar yang tertanam dalam halaman PDF dan menghitung resolusi efektifnya.

1. Buka PDF dengan 'ap.Document'.
1. Lacak keadaan grafis saat membaca konten halaman.
1. Tangani operator:
- 'GSave'/'GRestore' - dorong/tarik matriks.
- 'ConcatenateMatrix' - perbarui transformasi.
- 'Do' - jika itu gambar, dapatkan ukuran & terapkan transformasi.
1. Hitung DPI efektif.
1. Cetak nama gambar, ukuran setelah skala, dan DPI.

```python

    import aspose.pdf as ap
    from io import FileIO
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
