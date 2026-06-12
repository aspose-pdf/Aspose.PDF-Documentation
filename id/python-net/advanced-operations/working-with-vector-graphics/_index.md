---
title: Bekerja dengan Grafik Vektor di Python
linktitle: Bekerja dengan Grafik Vektor
type: docs
weight: 100
url: /id/python-net/working-with-vector-graphics/
description: Pelajari cara mengekstrak, memindahkan, menghapus, dan menyalin grafik vektor antar halaman PDF menggunakan GraphicsAbsorber di Python.
lastmod: "2026-06-12"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Gunakan GraphicsAbsorber untuk memeriksa dan memanipulasi grafik vektor PDF di Python.
Abstract: Artikel ini menjelaskan cara bekerja dengan grafik vektor di Aspose.PDF for Python via .NET menggunakan kelas GraphicsAbsorber. Pelajari cara mengekstrak elemen vektor dari halaman PDF, memindahkan atau menghapusnya, dan menyalin grafik antar halaman dengan kontrol tingkat rendah dalam alur kerja Python.
---

[Aspose.PDF for Python via .NET](/pdf/id/python-net/) menyediakan [GraphicsAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.vector/graphicsabsorber/) kelas untuk mengakses dan memanipulasi grafik vektor yang sudah ada di halaman PDF. Panggil `visit` metode pada halaman mana pun untuk mengekstrak jalur, bentuk, dan operator grafis lainnya, kemudian memindahkan, menghapus, atau menyalin elemen tersebut sesuai kebutuhan.

Gunakan halaman ini ketika Anda perlu memeriksa atau memodifikasi elemen gambar vektor yang tertanam dalam PDF yang ada, alih-alih menggambar bentuk baru dari awal.

## Mengekstrak Grafik

Ekstraksi adalah titik awal untuk semua tugas grafis vektor. `GraphicsAbsorber` membaca aliran konten sebuah halaman dan menampilkan setiap elemen grafis dengan referensi halaman, posisi, dan operator mentahnya.

1. Buka dokumen PDF.
1. Buat sebuah [GraphicsAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.vector/graphicsabsorber/) instance.
1. Panggilan `visit` pada halaman target untuk diisi `elements`.
1. Iterasi atas `elements` untuk memeriksa posisi dan jumlah operator.

```python
import aspose.pdf as ap
import sys
from os import path

def using_graphics_absorber(infile: str):
    with ap.Document(infile) as document:
        with ap.vector.GraphicsAbsorber() as graphics_absorber:
            page = document.pages[1]
            graphics_absorber.visit(page)
            for element in graphics_absorber.elements:
                print(f"Page Number: {element.source_page.number}")
                print(f"Position: ({element.position.x}, {element.position.y})")
                print(f"Number of Operators: {element.operators.length}")
```

`GraphicsAbsorber` adalah bagian dari `aspose.pdf.vector` namespace dan secara khusus dirancang untuk berinteraksi dengan grafik vektor dalam aliran konten PDF.

## Grafik Bergerak

Setelah ekstraksi, atur yang baru `position` pada setiap elemen untuk memindahkannya ke halaman yang sama. Bungkus pembaruan dalam `suppress_update` / `resume_update` pemanggilan untuk mengelompokkan penulisan aliran konten menjadi satu operasi dan menghindari pengecatan ulang yang berlebihan.

1. Buka dokumen PDF.
1. Buat sebuah `GraphicsAbsorber` dan panggil `visit` pada halaman target.
1. Panggilan `suppress_update` untuk menjeda penulisan aliran konten.
1. Perbarui `position` dari setiap elemen.
1. Panggilan `resume_update` untuk melakukan commit semua perubahan sekaligus.
1. Simpan dokumen yang telah dimodifikasi.

```python
import aspose.pdf as ap
import sys
from os import path

def move_graphics(infile: str, outfile: str):
    with ap.Document(infile) as document:
        with ap.vector.GraphicsAbsorber() as graphics_absorber:
            page = document.pages[1]
            graphics_absorber.visit(page)
            graphics_absorber.suppress_update()
            for element in graphics_absorber.elements:
                position = element.position
                element.position = ap.Point(position.x + 150, position.y - 10)
            graphics_absorber.resume_update()
        document.save(outfile)
```

## Menghapus Grafik

Untuk menghapus elemen vektor spesifik dari sebuah halaman, filter berdasarkan posisi atau persegi pembatas, lalu hapus mereka. Aspose.PDF for Python menyediakan dua pendekatan tergantung apakah Anda ingin menghapus elemen secara langsung atau mengumpulkannya terlebih dahulu.

### Metode 1: Hapus Inline Menggunakan Batas Persegi Panjang

Pendekatan ini memeriksa posisi setiap elemen terhadap sebuah persegi panjang dan memanggil `element.remove()` langsung di dalam loop. Gunakan itu ketika Anda ingin kode yang singkat dan tidak perlu memeriksa set yang dihapus setelahnya.

1. Buka dokumen PDF.
1. Buat sebuah `GraphicsAbsorber` dan panggil `visit` pada halaman target.
1. Tentukan target [Persegi panjang](https://reference.aspose.com/pdf/python-net/aspose.pdf/rectangle/).
1. Panggilan `suppress_update` untuk menjeda penulisan aliran konten.
1. Iterasi `elements`, memanggil `remove()` pada setiap elemen yang posisinya berada di dalam persegi panjang.
1. Panggilan `resume_update` untuk melakukan penghapusan.
1. Simpan dokumen yang telah dimodifikasi.

```python
import aspose.pdf as ap
import sys
from os import path

def remove_graphics_method_1(infile: str, outfile: str):
    with ap.Document(infile) as document:
        with ap.vector.GraphicsAbsorber() as graphics_absorber:
            page = document.pages[1]
            graphics_absorber.visit(page)
            rectangle = ap.Rectangle(70, 248, 170, 252, True)
            graphics_absorber.suppress_update()
            for element in graphics_absorber.elements:
                if rectangle.contains(element.position, False):
                    element.remove()
            graphics_absorber.resume_update()
        document.save(outfile)
```

### Metode 2: Kumpulkan Elemen Terlebih Dahulu, Kemudian Hapus

Pendekatan ini mengumpulkan elemen yang cocok ke dalam sebuah [KoleksiElemenGrafis](https://reference.aspose.com/pdf/python-net/aspose.pdf.vector/graphicelementcollection/) dan melewatkan koleksi ke `page.delete_graphics`. Gunakan itu ketika Anda perlu meninjau atau mencatat apa yang akan dihapus sebelum melakukan penghapusan.

1. Buka dokumen PDF.
1. Buat sebuah `GraphicsAbsorber` dan panggil `visit` pada halaman target.
1. Tentukan persegi panjang target.
1. Iterasi `elements` dan tambahkan elemen yang cocok ke a `GraphicElementCollection`.
1. Panggilan `page.contents.suppress_update` untuk menjeda penulisan aliran konten.
1. Panggilan `page.delete_graphics` dengan koleksi.
1. Panggilan `page.contents.resume_update` untuk melakukan penghapusan.
1. Simpan dokumen yang telah dimodifikasi.

```python
import aspose.pdf as ap
import sys
from os import path

def remove_graphics_method_2(infile: str, outfile: str):
    with ap.Document(infile) as document:
        with ap.vector.GraphicsAbsorber() as graphics_absorber:
            page = document.pages[1]
            rectangle = ap.Rectangle(70, 248, 170, 252, True)
            graphics_absorber.visit(page)
            removed_elements_collection = ap.vector.GraphicElementCollection()
            for element in graphics_absorber.elements:
                if rectangle.contains(element.position, False):
                    removed_elements_collection.add(element)
            page.contents.suppress_update()
            page.delete_graphics(removed_elements_collection)
            page.contents.resume_update()
        document.save(outfile)
```

## Menambahkan Grafik ke Halaman Lain

Elemen vektor yang diekstrak dari satu halaman dapat ditempatkan pada halaman lain dalam dokumen yang sama. Dua metode tersedia: menambahkan elemen satu per satu, atau melewatkan seluruh koleksi dalam satu panggilan.

### Metode 1: Tambahkan Elemen Secara Individual

Gunakan metode ini ketika Anda memerlukan kontrol per‑elemen, seperti menyaring atau mengubah elemen individual sebelum menempatkannya pada halaman tujuan.

1. Buka dokumen PDF.
1. Buat sebuah `GraphicsAbsorber` dan panggil `visit` di halaman sumber.
1. Tambahkan halaman tujuan baru ke dokumen.
1. Panggilan `page_2.contents.suppress_update` untuk menjeda penulisan aliran konten.
1. Panggilan `element.add_on_page(page_2)` untuk setiap elemen.
1. Panggilan `page_2.contents.resume_update` untuk melakukan commit semua penambahan.
1. Simpan dokumen yang telah dimodifikasi.

```python
import aspose.pdf as ap
import sys
from os import path

def add_to_another_page_method_1(infile: str, outfile: str):
    with ap.Document(infile) as document:
        with ap.vector.GraphicsAbsorber() as graphics_absorber:
            page_1 = document.pages[1]
            page_2 = document.pages.add()
            graphics_absorber.visit(page_1)
            page_2.contents.suppress_update()
            for element in graphics_absorber.elements:
                element.add_on_page(page_2)
            page_2.contents.resume_update()
        document.save(outfile)
```

### Metode 2: Tambahkan Seluruh Koleksi Sekaligus

Gunakan metode ini ketika Anda ingin menyalin semua elemen yang diekstrak ke sebuah halaman dalam satu operasi tanpa harus mengulang secara manual.

1. Buka dokumen PDF.
1. Buat sebuah `GraphicsAbsorber` dan panggil `visit` di halaman sumber.
1. Tambahkan halaman tujuan baru ke dokumen.
1. Panggilan `page_2.contents.suppress_update` untuk menjeda penulisan aliran konten.
1. Panggilan `page_2.add_graphics` dengan seluruh `elements` koleksi.
1. Panggilan `page_2.contents.resume_update` untuk melakukan commit semua penambahan.
1. Simpan dokumen yang telah dimodifikasi.

```python
import aspose.pdf as ap
import sys
from os import path

def add_to_another_page_method_2(infile: str, outfile: str):
    with ap.Document(infile) as document:
        with ap.vector.GraphicsAbsorber() as graphics_absorber:
            page_1 = document.pages[1]
            page_2 = document.pages.add()
            graphics_absorber.visit(page_1)
            page_2.contents.suppress_update()
            page_2.add_graphics(graphics_absorber.elements, None)
            page_2.contents.resume_update()
        document.save(outfile)
```

## Topik Terkait

- [Operasi PDF lanjutan di Python](/pdf/id/python-net/advanced-operations/)
- [Bekerja dengan grafik PDF di Python](/pdf/id/python-net/working-with-graphs/)
- [Bekerja dengan operator PDF di Python](/pdf/id/python-net/working-with-operators/)
- [Bekerja dengan halaman PDF di Python](/pdf/id/python-net/working-with-pages/)
