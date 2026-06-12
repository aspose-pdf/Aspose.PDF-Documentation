---
title: Bekerja dengan Operator PDF di Python
linktitle: Bekerja dengan Operator
type: docs
weight: 90
url: /id/python-net/working-with-operators/
description: Pelajari cara menggunakan operator PDF tingkat rendah di Python untuk manipulasi aliran konten yang tepat dan kontrol grafik.
lastmod: "2026-06-12"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Gunakan operator PDF tingkat rendah untuk kontrol aliran konten di Python
Abstract: Artikel ini menjelaskan cara bekerja dengan operator PDF tingkat rendah di Aspose.PDF for Python via .NET. Pelajari cara memanipulasi aliran konten secara langsung, menempatkan grafik secara tepat dengan kelas operator, dan menghapus objek yang digambar dari halaman PDF dalam alur kerja Python.
---

## Pengantar Operator PDF dan Penggunaannya

Operator adalah kata kunci PDF yang menentukan tindakan tertentu yang harus dilakukan, seperti menggambar bentuk grafis pada halaman. Kata kunci operator dibedakan dari objek bernama oleh tidak adanya karakter solidus awal (2Fh). Operator hanya memiliki makna di dalam aliran konten.

Aliran konten adalah objek aliran PDF yang datanya terdiri dari instruksi yang menggambarkan elemen grafis yang akan digambar pada halaman. Detail lebih lanjut tentang operator PDF dapat ditemukan di the [spesifikasi PDF](https://opensource.adobe.com/dc-acrobat-sdk-docs/).

Gunakan halaman ini ketika Anda membutuhkan kontrol langsung atas aliran konten PDF di Python, seperti menempatkan grafik pada koordinat yang tepat, membungkus perubahan status grafik, atau menghapus operator gambar spesifik dari sebuah halaman.

## Tambahkan Gambar dengan Kelas Operator

Gunakan kelas operator tingkat rendah ketika Anda perlu menempatkan konten gambar dengan sangat tepat dalam aliran halaman PDF tanpa bergantung pada abstraksi tata letak tingkat tinggi.

Metode ini menyediakan kontrol terperinci atas penempatan gambar dalam PDF dengan langsung memanipulasi aliran konten menggunakan operator grafis tingkat rendah. Metode ini sangat berguna ketika penempatan dan transformasi gambar yang tepat diperlukan, seperti:

- menambahkan watermark atau logo pada lokasi tertentu.
- menumpangkan gambar di atas konten yang ada dengan penyelarasan yang tepat.
- menerapkan tata letak khusus yang tidak dapat dicapai dengan abstraksi tingkat tinggi.

Dengan menggunakan operator seperti GSave, ConcatenateMatrix, Do, dan GRestore, pengembang dapat memastikan bahwa gambar dirender secara akurat dan tanpa efek samping yang tidak diinginkan pada konten halaman lainnya.

- The [GSave](https://reference.aspose.com/pdf/python-net/aspose.pdf.operators/gsave/) operator menyimpan keadaan grafis PDF saat ini.
- The [ConcatenateMatrix](https://reference.aspose.com/pdf/python-net/aspose.pdf.operators/concatenatematrix/) Operator (concatenate matrix) digunakan untuk menentukan bagaimana gambar harus ditempatkan pada halaman PDF.
- The [Do](https://reference.aspose.com/pdf/python-net/aspose.pdf.operators/do/) operator menggambar gambar pada halaman.
- The [GRestore](https://reference.aspose.com/pdf/python-net/aspose.pdf.operators/grestore/) operator mengembalikan keadaan grafis.

Untuk menambahkan gambar ke dalam file PDF:

1. Buka Dokumen PDF
1. Tentukan Koordinat Penempatan Gambar
1. Akses Halaman Target
1. Muat Gambar ke dalam Stream
1. Simpan Status Grafik Saat Ini
1. Buat Persegi Panjang dan Matriks Transformasi
1. Terapkan Matriks Transformasi
1. Gambar gambar
1. Pulihkan Keadaan Grafis Sebelumnya
1. Simpan Dokumen PDF yang Dimodifikasi

Potongan kode berikut menunjukkan cara menggunakan operator PDF:

```python
import sys
import aspose.pdf as ap
from os import path

def add_image_using_pdf_operators(infile, imagefile, outfile):
    with ap.Document(infile) as document:
        lower_left_x = 100
        lower_left_y = 100
        upper_right_x = 200
        upper_right_y = 200

        page = document.pages[1]

        with open(imagefile, "rb") as image_stream:
            page.resources.images.add(image_stream)

        page.contents.append(ap.operators.GSave())

        rectangle = ap.Rectangle(
            lower_left_x, lower_left_y, upper_right_x, upper_right_y, True
        )
        matrix = ap.Matrix(
            [
                rectangle.urx - rectangle.llx,
                0,
                0,
                rectangle.ury - rectangle.lly,
                rectangle.llx,
                rectangle.lly,
            ]
        )

        page.contents.append(ap.operators.ConcatenateMatrix(matrix))

        x_image = page.resources.images[len(page.resources.images)]

        page.contents.append(ap.operators.Do(x_image.name))

        page.contents.append(ap.operators.GRestore())

        document.save(outfile)
```

## Gambar XForm pada Halaman menggunakan Operator

Contoh ini menggunakan kekuatan XForms dan operator grafis untuk secara efisien menggunakan kembali konten grafis dalam PDF. Dengan membungkus gambar dalam XForm, gambar dapat digambar berulang kali tanpa menduplikasi data gambar, menghasilkan ukuran file yang lebih kecil dan kinerja yang meningkat. Pendekatan ini sangat bermanfaat ketika:

- gambar atau grafik yang sama perlu muncul beberapa kali dalam dokumen.

- kontrol yang tepat atas penempatan dan transformasi grafik diperlukan.

- mengoptimalkan PDF untuk kinerja dan ukuran menjadi prioritas.

Dengan mengelola keadaan grafik menggunakan GSave dan GRestore, serta menggunakan matriks transformasi dengan ConcatenateMatrix, teknik ini memastikan setiap grafik dirender dengan benar dan secara independen.

```python
import sys
import aspose.pdf as ap
from os import path

def draw_xform_on_page(infile, imagefile, outfile):
    with ap.Document(infile) as document:
        page_contents = document.pages[1].contents

        page_contents.insert(1, ap.operators.GSave())
        page_contents.append(ap.operators.GRestore())

        page_contents.append(ap.operators.GSave())

        form = ap.XForm.create_new_form(document.pages[1], document)
        document.pages[1].resources.forms.append(form)

        form.contents.append(ap.operators.GSave())
        form.contents.append(ap.operators.ConcatenateMatrix(200, 0, 0, 200, 0, 0))

        with open(imagefile, "rb") as image_stream:
            form.resources.images.add(image_stream)

        x_image = form.resources.images[len(form.resources.images)]
        form.contents.append(ap.operators.Do(x_image.name))
        form.contents.append(ap.operators.GRestore())

        # Draw XForm at (100, 500)
        page_contents.append(ap.operators.GSave())
        page_contents.append(ap.operators.ConcatenateMatrix(1, 0, 0, 1, 100, 500))
        page_contents.append(ap.operators.Do(form.name))
        page_contents.append(ap.operators.GRestore())

        # Draw XForm at (100, 300)
        page_contents.append(ap.operators.GSave())
        page_contents.append(ap.operators.ConcatenateMatrix(1, 0, 0, 1, 100, 300))
        page_contents.append(ap.operators.Do(form.name))
        page_contents.append(ap.operators.GRestore())

        page_contents.append(ap.operators.GRestore())

        document.save(outfile)
```

## Hapus Objek Grafik menggunakan Kelas Operator

Cuplikan kode berikut menunjukkan cara menghapus grafik. Harap perhatikan bahwa jika file PDF berisi label teks untuk grafik, label tersebut mungkin tetap ada dalam file PDF saat menggunakan pendekatan ini. Oleh karena itu, cari operator grafik untuk metode alternatif menghapus gambar tersebut.

```python
import sys
import aspose.pdf as ap
from os import path

def remove_graphics_objects(infile, outfile):
    with ap.Document(infile) as document:
        page = document.pages[1]
        # Collect operators to remove in single pass
        # Operator codes: S=Stroke, h=ClosePathStroke, f=Fill'
        graphics_operators = {"S", "h", "f"}
        operators_to_remove = [
            op for op in page.contents if str(op) in graphics_operators
        ]

        page.contents.delete(operators_to_remove)
        document.save(outfile)
```

## Topik Terkait

- [Operasi PDF lanjutan di Python](/pdf/id/python-net/advanced-operations/)
- [Bekerja dengan halaman PDF di Python](/pdf/id/python-net/working-with-pages/)
- [Bekerja dengan gambar dalam PDF menggunakan Python](/pdf/id/python-net/working-with-images/)
- [Bekerja dengan grafik PDF di Python](/pdf/id/python-net/working-with-graphs/)
