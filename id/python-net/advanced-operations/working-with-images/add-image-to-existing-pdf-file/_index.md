---
title: Tambahkan Gambar ke PDF menggunakan Python
linktitle: Tambahkan Gambar
type: docs
weight: 10
url: /id/python-net/add-image-to-existing-pdf-file/
description: Bagian ini menjelaskan cara menambahkan gambar ke file PDF yang ada menggunakan perpustakaan Python.
lastmod: "2025-09-27"
TechArticle: true
AlternativeHeadline: Cara menambahkan gambar ke PDF menggunakan Python
Abstract: Artikel ini memberikan panduan tentang menambahkan gambar ke file PDF yang ada menggunakan Python dengan perpustakaan Aspose.PDF. Dua metode dijelaskan untuk mencapai hal ini. Metode pertama melibatkan penggunaan kelas `Document` dari Aspose.PDF, dimana pengguna memuat PDF, menentukan nomor halaman, dan menggunakan metode `add_image` dari kelas `Page` untuk menempatkan gambar. Dokumen kemudian disimpan menggunakan metode `save()`. Metode kedua menggunakan kelas `PdfFileMend` dari namespace Aspose.PDF.Facades, yang menawarkan antarmuka yang lebih sederhana. Di sini, metode `add_image()` dipanggil untuk menambahkan gambar ke halaman dan koordinat yang ditentukan, diikuti dengan menyimpan PDF yang diperbarui dan menutup objek `PdfFileMend`. Potongan kode disediakan untuk kedua metode untuk mendemonstrasikan prosesnya.
---

## Tambahkan Gambar dalam File PDF yang Ada

Contoh ini menunjukkan cara menyisipkan gambar ke posisi tertentu pada halaman PDF menggunakan Aspose.PDF untuk Python via .NET.

1. Muat dokumen PDF dengan 'ap.Document'.
1. Pilih halaman target '(document.pages[1]' - halaman pertama.
1. Gunakan 'page.add_image()' untuk menempatkan gambar:
- Jalur file gambar.
- Objek 'Rectangle' yang mendefinisikan koordinat gambar (left=20, bottom=730, right=120, top=830).
1. Simpan PDF yang diperbarui.

```python

    import aspose.pdf as ap
    from io import FileIO
    from os import path

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = ap.Document(path_infile)
    page = document.pages[1]
    page.add_image(
        path.join(self.data_dir, image_file),
        ap.Rectangle(20, 730, 120, 830, True),
    )
    document.save(path_outfile)
```

## Tambahkan Gambar Menggunakan Operator

Potongan kode berikut menunjukkan pendekatan tingkat rendah untuk menambahkan gambar ke halaman PDF dengan secara manual bekerja dengan operator PDF daripada metode bantuan tingkat tinggi.

Langkah-langkah:

1. Buat 'Document' kosong baru.
1. Tambahkan halaman dan atur ukurannya (842 × 595 - lanskap A4).
1. Akses sumber daya gambar halaman (page.resources.images).
1. Muat file gambar ke dalam stream dan tambahkan ke sumber daya.
- Metode mengembalikan 'image_id'.
- Objek gambar yang baru ditambahkan diambil dari sumber daya.
1. Definisikan persegi panjang yang mempertahankan rasio aspek gambar:
1. Bangun urutan operator:
- 'GSave()' - Simpan keadaan grafik saat ini.
- 'ConcatenateMatrix(matrix)' - Terapkan transformasi (skala dan pusatkan gambar secara vertikal pada halaman).
- 'Do(image_id)' - Render gambar.
- 'GRestore()' - Pulihkan keadaan grafik.
1. Tambahkan urutan operator ke 'page.contents'.
1. Simpan PDF hasil.

```python

    import aspose.pdf as ap
    from io import FileIO
    from os import path

    path_infile = path.join(self.data_dir, image_file)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = ap.Document()
    page = document.pages.add()
    page.set_page_size(842,595)

    # Get page resources
    resources_images = page.resources.images

    # Add image to resources
    image_stream = FileIO(path.join(self.data_dir, path_infile), "rb")
    image_id = resources_images.add(image_stream)

    x_image = list(resources_images)[-1]

    rectangle = ap.Rectangle(
        0,
        0,
        page.media_box.width,
        (page.media_box.width * x_image.height) / x_image.width,
        True,
    )

    # Create operator sequence for adding image
    operators = []

    # Save graphics state
    operators.append(ap.operators.GSave())

    # Set transformation matrix (position and size)
    matrix = ap.Matrix(
        rectangle.urx - rectangle.llx,
        0,
        0,
        rectangle.ury - rectangle.lly,
        rectangle.llx,
        rectangle.llx + (page.media_box.height - rectangle.height) / 2,
    )
    operators.append(ap.operators.ConcatenateMatrix(matrix))

    # Draw the image
    operators.append(ap.operators.Do(image_id))

    # Restore graphics state
    operators.append(ap.operators.GRestore())

    # Add operators to page contents
    page.contents.add(operators)

    document.save(path_outfile)
```

## Tambahkan Gambar dengan Teks Alternatif

Contoh ini menunjukkan cara menambahkan gambar ke halaman PDF dan menetapkan teks alternatif (alt text) untuk kepatuhan aksesibilitas (seperti PDF/UA).

1. Buat 'Document' baru dan tambahkan halaman (842 × 595, lanskap A4).
1. Tempatkan gambar pada halaman menggunakan 'page.add_image()' dengan persegi panjang yang meliputi seluruh halaman.
1. Akses sumber daya gambar halaman ('page.resources.images').
1. Definisikan string teks alternatif (mis., 'Alternative text for image').
1. Ambil objek gambar pertama dari sumber daya ('x_image = resources_images[1]').
1. Gunakan 'try_set_alternative_text(alt_text, page)' untuk menetapkan teks alternatif pada gambar.
1. Simpan PDF hasil.

```python

    import aspose.pdf as ap
    from io import FileIO
    from os import path

    path_image_file = path.join(self.data_dir, image_file)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = ap.Document()
    page = document.pages.add()
    page.set_page_size(842,595)

    page.add_image(
        path_image_file,
        ap.Rectangle(0, 0, 842, 595, True),
    )

    resources_images = page.resources.images
    alt_text = "Alternative text for image"
    x_image = resources_images[1]
    result = x_image.try_set_alternative_text(alt_text, page)

    # If set is successful, then get the alternative text for the image
    if (result):
        print ("Text has been added successfuly")
    document.save(path_outfile)
```
