---
title: Optimalkan File PDF di Python
linktitle: Optimalkan PDF
type: docs
weight: 30
url: /id/python-net/optimize-pdf/
description: Pelajari cara mengoptimalkan, mengompres, dan mengurangi ukuran file PDF di Python menggunakan Aspose.PDF.
lastmod: "2026-06-12"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Kompres halaman PDF menggunakan Python
Abstract: Artikel ini menyediakan panduan komprehensif tentang mengoptimalkan file PDF untuk mengurangi ukuran mereka dan meningkatkan kinerja di berbagai platform, seperti halaman web, email, dan sistem penyimpanan. Teknik optimisasi mencakup mengurangi ukuran gambar, menghapus sumber daya yang tidak terpakai, dan meng‑unembed font. Metode khusus untuk mengoptimalkan PDF untuk web dan mengurangi ukuran file secara keseluruhan dibahas, menggunakan metode `Optimize` dan `OptimizeResources` dalam Aspose.PDF for Python. Kustomisasi strategi optimisasi dimungkinkan melalui `OptimizationOptions`, memungkinkan tindakan terarah seperti mengompresi gambar, menghapus objek dan stream yang tidak terpakai, menautkan stream duplikat, dan meng‑unembed font. Strategi tambahan mencakup meratakan anotasi, menghapus field formulir, dan mengonversi file PDF dari RGB ke skala abu‑abu untuk lebih mengurangi ukuran. Artikel ini juga menyoroti penggunaan kompresi FlateDecode untuk optimisasi gambar, memastikan manajemen file PDF yang efektif sambil mempertahankan kualitas dan fungsionalitas.
---

Dokumen PDF terkadang dapat berisi data tambahan. Mengurangi ukuran file PDF akan membantu Anda mengoptimalkan transfer jaringan dan penyimpanan. Ini sangat berguna untuk penerbitan di halaman web, berbagi di jejaring sosial, mengirim lewat e‑mail, atau mengarsipkan dalam penyimpanan. Kita dapat menggunakan beberapa teknik untuk mengoptimalkan PDF:

Gunakan halaman ini ketika Anda perlu mengurangi ukuran PDF untuk pengiriman web, berbagi email, penghematan penyimpanan, atau output yang ramah cetak tanpa harus membangun ulang dokumen dari awal.

- Optimalkan konten halaman untuk penelusuran daring
- Perkecil atau kompres semua gambar
- Aktifkan penggunaan kembali konten halaman
- Gabungkan aliran duplikat
- Lepaskan penyematan font
- Hapus objek yang tidak digunakan
- Hapus pemipihan bidang formulir
- Hapus atau ratakan anotasi

{{% alert color="primary" %}}

 Penjelasan rinci tentang metode optimisasi dapat ditemukan di halaman Ikhtisar Metode Optimasi.

{{% /alert %}}

## Optimalkan Dokumen PDF untuk Web

Optimisasi, atau linearisasi untuk Web, mengacu pada proses menjadikan file PDF cocok untuk penelusuran online menggunakan peramban web. Untuk mengoptimalkan file untuk tampilan web:

1. Buka dokumen input dalam sebuah [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) objek.
1. Gunakan [optimize](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) metode.
1. Simpan dokumen yang dioptimalkan menggunakan [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) metode.

Cuplikan kode berikut menunjukkan cara mengoptimalkan dokumen PDF untuk web.

```python
import aspose.pdf as ap
from os import path, stat
import sys


def optimize_pdf(infile, outfile):
    document = ap.Document(infile)
    document.optimize()
    document.save(outfile)
    file_stats_1 = stat(infile)
    file_stats_2 = stat(outfile)
    print(
        "Original file size: {}. Reduced file size: {}".format(
            file_stats_1.st_size, file_stats_2.st_size
        )
    )
```

## Kurangi Ukuran PDF

The [OptimizeResources()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) metode memungkinkan Anda mengurangi ukuran dokumen dengan menghilangkan informasi yang tidak perlu. Secara default, metode ini bekerja sebagai berikut:

- Sumber daya yang tidak digunakan pada halaman dokumen dihapus
- Sumber daya yang sama digabung menjadi satu objek
- Objek yang tidak terpakai dihapus

Potongan kode di bawah ini adalah contoh. Catatan, meskipun, metode ini tidak dapat menjamin pengecilan dokumen.

```python
import aspose.pdf as ap
from os import path, stat
import sys


def reduce_size_pdf(infile, outfile):
    # Open document
    document = ap.Document(infile)
    # Optimize PDF document. Note, though, that this method cannot guarantee document shrinking
    document.optimize_resources()
    # Save updated document
    document.save(outfile)
    file_stats_1 = stat(infile)
    file_stats_2 = stat(outfile)
    print(
        "Original file size: {}. Reduced file size: {}".format(
            file_stats_1.st_size, file_stats_2.st_size
        )
    )
```

## Manajemen Strategi Optimasi

Kami juga dapat menyesuaikan strategi optimisasi. Saat ini, [OptimizeResources()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) metode menggunakan 5 teknik. Teknik-teknik ini dapat diterapkan menggunakan metode OptimizeResources() dengan [OpsiOptimisasi](https://reference.aspose.com/pdf/python-net/aspose.pdf.optimization/optimizationoptions/) parameter.

### Memperkecil atau Mengompresi Semua Gambar

Kami memiliki dua cara untuk bekerja dengan gambar: mengurangi kualitas gambar dan/atau mengubah resolusinya. Dalam hal apapun, [OpsiKompresiGambar](https://reference.aspose.com/pdf/python-net/aspose.pdf.optimization/imagecompressionoptions/) harus diterapkan. Pada contoh berikut, kami memperkecil gambar dengan mengurangi ImageQuality menjadi 50.

```python
import aspose.pdf as ap
from os import path, stat
import sys


def shrinking_or_compressing_all_images(infile, outfile):
    # Open document
    document = ap.Document(infile)
    # Initialize OptimizationOptions
    optimizeOptions = ap.optimization.OptimizationOptions()
    # Set CompressImages option
    optimizeOptions.image_compression_options.compress_images = True
    # Set ImageQuality option
    optimizeOptions.image_compression_options.image_quality = 50
    # Optimize PDF document using OptimizationOptions
    document.optimize_resources(optimizeOptions)
    # Save updated document
    document.save(outfile)
    file_stats_1 = stat(infile)
    file_stats_2 = stat(outfile)
    print(
        "Original file size: {}. Reduced file size: {}".format(
            file_stats_1.st_size, file_stats_2.st_size
        )
    )
```

### Menghapus Objek yang Tidak Digunakan

Dokumen PDF kadang‑kadang berisi objek PDF yang tidak dirujuk oleh objek lain manapun dalam dokumen. Ini dapat terjadi, misalnya, ketika sebuah halaman dihapus dari pohon halaman dokumen tetapi objek halaman itu sendiri tidak dihapus. Menghapus objek‑objek ini tidak membuat dokumen menjadi tidak valid, melainkan mengurangi ukurannya.

```python
import aspose.pdf as ap
from os import path, stat
import sys


def removing_unused_objects(infile, outfile):
    # Open document
    document = ap.Document(infile)
    # Set RemoveUnusedObjects option
    optimizeOptions = ap.optimization.OptimizationOptions()
    optimizeOptions.remove_unused_objects = True

    # Optimize PDF document using OptimizationOptions
    document.optimize_resources(optimizeOptions)
    # Save updated document
    document.save(outfile)
    file_stats_1 = stat(infile)
    file_stats_2 = stat(outfile)
    print(
        "Original file size: {}. Reduced file size: {}".format(
            file_stats_1.st_size, file_stats_2.st_size
        )
    )
```

### Menghapus Stream yang Tidak Digunakan

Kadang-kadang dokumen mengandung aliran sumber daya yang tidak terpakai. Aliran tersebut bukan “unused objects” karena direferensikan dari kamus sumber daya halaman. Oleh karena itu, mereka tidak dihapus dengan metode “remove unused objects”. Namun aliran ini tidak pernah digunakan dalam konten halaman. Ini dapat terjadi ketika sebuah gambar telah dihapus dari halaman tetapi tidak dari sumber daya halaman. Selain itu, situasi ini sering terjadi ketika halaman diekstrak dari dokumen dan halaman dokumen memiliki sumber daya “common”, yaitu, objek Resources yang sama. Konten halaman dianalisis untuk menentukan apakah aliran sumber daya digunakan atau tidak. Aliran yang tidak terpakai dihapus. Hal ini kadang-kadang mengurangi ukuran dokumen. Penggunaan teknik ini mirip dengan langkah sebelumnya:

```python
import aspose.pdf as ap
from os import path, stat
import sys


def removing_unused_streams(infile, outfile):
    # Open document
    document = ap.Document(infile)
    # Set RemoveUnusedStreams option
    optimizeOptions = ap.optimization.OptimizationOptions()
    optimizeOptions.remove_unused_streams = True
    # Optimize PDF document using OptimizationOptions
    document.optimize_resources(optimizeOptions)
    # Save updated document
    document.save(outfile)
    file_stats_1 = stat(infile)
    file_stats_2 = stat(outfile)
    print(
        "Original file size: {}. Reduced file size: {}".format(
            file_stats_1.st_size, file_stats_2.st_size
        )
    )
```

### Menautkan Aliran Duplikat

Beberapa dokumen dapat berisi beberapa aliran sumber daya yang identik (seperti gambar, misalnya). Ini dapat terjadi, misalnya ketika sebuah dokumen digabungkan dengan dirinya sendiri. Dokumen output berisi dua salinan independen dari aliran sumber daya yang sama. Kami menganalisis semua aliran sumber daya dan membandingkannya. Jika aliran tersebut diduplikasi, mereka digabungkan, yaitu hanya satu salinan yang tersisa. Referensi diubah secara tepat, dan salinan objek dihapus. Dalam beberapa kasus, ini membantu mengurangi ukuran dokumen.

```python
import aspose.pdf as ap
from os import path, stat
import sys


def linking_duplicate_streams(infile, outfile):
    # Open document
    document = ap.Document(infile)
    # Set link_duplicate_streams option
    optimizeOptions = ap.optimization.OptimizationOptions()
    optimizeOptions.link_duplicate_streams = True
    # Optimize PDF document using OptimizationOptions
    document.optimize_resources(optimizeOptions)
    # Save updated document
    document.save(outfile)
    file_stats_1 = stat(infile)
    file_stats_2 = stat(outfile)
    print(
        "Original file size: {}. Reduced file size: {}".format(
            file_stats_1.st_size, file_stats_2.st_size
        )
    )
```

### Melepaskan Penyematan Font

Jika dokumen menggunakan font yang disematkan, itu berarti semua data font disimpan dalam dokumen. Keuntungannya adalah dokumen dapat dilihat terlepas dari apakah font tersebut terpasang di mesin pengguna atau tidak. Namun menyematkan font membuat dokumen menjadi lebih besar. Metode unembed fonts menghapus semua font yang disematkan. Dengan demikian, ukuran dokumen berkurang tetapi dokumen itu sendiri mungkin menjadi tidak dapat dibaca jika font yang tepat tidak terpasang.

```python
import aspose.pdf as ap
from os import path, stat
import sys


def unembed_fonts(infile, outfile):
    # Open document
    document = ap.Document(infile)
    # Set unembed_fonts option
    optimize_options = ap.optimization.OptimizationOptions()
    optimize_options.unembed_fonts = True
    # Optimize PDF document using OptimizationOptions
    document.optimize_resources(optimize_options)
    # Save updated document
    document.save(outfile)
    file_stats_1 = stat(infile)
    file_stats_2 = stat(outfile)
    print(
        "Original file size: {}. Reduced file size: {}".format(
            file_stats_1.st_size, file_stats_2.st_size
        )
    )
```

Sumber daya optimasi menerapkan metode‑metode ini pada dokumen. Jika salah satu dari metode ini diterapkan, ukuran dokumen kemungkinan besar akan berkurang. Jika tidak ada metode ini yang diterapkan, ukuran dokumen tidak akan berubah, yang jelas.

## Cara Tambahan untuk Mengurangi Ukuran Dokumen PDF

### Menghapus atau Meratakan Anotasi

Annotasi dapat dihapus ketika tidak diperlukan. Ketika diperlukan tetapi tidak memerlukan penyuntingan tambahan, mereka dapat diflatkan. Kedua teknik ini akan mengurangi ukuran file.

```python
import aspose.pdf as ap
from os import path, stat
import sys


def flatten_annotations(infile, outfile):
    # Open document
    document = ap.Document(infile)
    # Flatten annotations
    for page in document.pages:
        for annotation in page.annotations:
            annotation.flatten()

    # Save updated document
    document.save(outfile)
```

### Menghapus Bidang Form

Jika dokumen PDF berisi AcroForms, kita dapat mencoba mengurangi ukuran file dengan meratakan bidang formulir.

```python
import aspose.pdf as ap
from os import path, stat
import sys


def flatten_forms(infile, outfile):
    # Load source PDF form
    doc = ap.Document(infile)

    # Flatten Forms
    if len(doc.form.fields) > 0:
        for item in doc.form.fields:
            item.flatten()

    # Save the updated document
    doc.save(outfile)
    file_stats_1 = stat(infile)
    file_stats_2 = stat(outfile)
    print(
        "Original file size: {}. Reduced file size: {}".format(
            file_stats_1.st_size, file_stats_2.st_size
        )
    )
```

### Konversi PDF dari ruang warna RGB ke skala abu-abu

File PDF terdiri dari Text, Image, Attachment, Annotations, Graphs, dan objek lainnya. Anda mungkin menemukan kebutuhan untuk mengubah PDF dari ruang warna RGB ke grayscale sehingga pencetakan file PDF tersebut lebih cepat. Selain itu, ketika file diubah menjadi grayscale, ukuran dokumen juga berkurang, tetapi hal itu juga dapat menyebabkan penurunan kualitas dokumen. Fitur ini saat ini didukung oleh fitur Pre-Flight di Adobe Acrobat, tetapi ketika membahas otomasi Office, Aspose.PDF adalah solusi utama untuk menyediakan manfaat tersebut dalam manipulasi dokumen. Untuk memenuhi kebutuhan ini, cuplikan kode berikut dapat digunakan.

```python
import aspose.pdf as ap
from os import path, stat
import sys


def сonvert_PDF_from_RGB_colorspace_to_grayscale(infile, outfile):
    document = ap.Document(infile)
    strategy = ap.RgbToDeviceGrayConversionStrategy()
    for page in document.pages:
        # Convert the RGB colorspace image to GrayScale colorspace
        strategy.convert(page)

    # Save resultant file
    document.save(outfile)
```

### Kompresi FlateDecode

Aspose.PDF for Python via .NET menyediakan dukungan kompresi FlateDecode untuk fungsi Optimalisasi PDF. Potongan kode di bawah ini menunjukkan cara menggunakan opsi dalam Optimalisasi untuk menyimpan gambar dengan kompresi **FlateDecode**:

```python
import aspose.pdf as ap
from os import path, stat
import sys


def using_flatedecode_compression(infile, outfile):

    # Open Document
    doc = ap.Document(infile)
    # Initialize OptimizationOptions
    optimizationOptions = ap.optimization.OptimizationOptions()
    # To optimise image using FlateDecode Compression set optimization options to Flate
    optimizationOptions.image_compression_options.encoding = (
        ap.optimization.ImageEncoding.FLATE
    )
    # Set Optimization Options
    doc.optimize_resources(optimizationOptions)
    # Save Document
    doc.save(outfile)
```

## Topik Dokumen Terkait

- [Bekerja dengan dokumen PDF di Python](/pdf/id/python-net/working-with-documents/)
- [Gabungkan file PDF di Python](/pdf/id/python-net/merge-pdf-documents/)
- [Membagi file PDF dengan Python](/pdf/id/python-net/split-document/)
- [Manipulasi dokumen PDF dalam Python](/pdf/id/python-net/manipulate-pdf-document/)

