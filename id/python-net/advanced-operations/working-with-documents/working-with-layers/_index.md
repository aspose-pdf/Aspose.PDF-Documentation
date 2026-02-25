---
title: Bekerja dengan lapisan PDF menggunakan Python
linktitle: Bekerja dengan lapisan PDF
type: docs
weight: 50
url: /id/python-net/working-with-pdf-layers/
description: Tugas selanjutnya menjelaskan cara mengunci lapisan PDF, mengekstrak elemen lapisan PDF, meratakan PDF berlapis, dan menggabungkan semua lapisan dalam PDF menjadi satu.
lastmod: "2025-11-17"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Manipulasi Lapisan PDF
Abstract: Panduan ini menyediakan tinjauan komprehensif tentang cara mengelola dan memanipulasi lapisan PDF menggunakan pustaka Aspose.PDF untuk Python via .NET. Lapisan PDF—juga dikenal sebagai Optional Content Groups (OCGs)—memungkinkan pengorganisasian konten ke dalam komponen visual terpisah yang dapat diaktifkan atau dinonaktifkan.
---

Lapisan PDF adalah cara yang kuat untuk mengatur dan menyajikan konten secara fleksibel dalam satu file PDF, memungkinkan pengguna menampilkan atau menyembunyikan bagian yang berbeda sesuai kebutuhan mereka.

Dengan **Aspose.PDF for Python via .NET**, Anda dapat:

- Kunci/Buka kunci lapisan untuk mengontrol visibilitas.
- Ekstrak lapisan ke dalam file terpisah atau aliran.
- Ratakan lapisan untuk membuatnya permanen.
- Gabungkan lapisan menjadi satu lapisan terpadu.

## Tambahkan lapisan ke PDF

Contoh ini menunjukkan cara membuat dan menambahkan beberapa lapisan ke dokumen PDF menggunakan Aspose.PDF untuk Python via .NET. Setiap lapisan berisi konten grafis terpisah, seperti garis berwarna, yang dapat diaktifkan atau dinonaktifkan pada penampil PDF yang mendukung lapisan.

1. Buat dokumen PDF baru dan tambahkan halaman.
1. Buat dan tambahkan lapisan merah.
1. Buat dan tambahkan lapisan hijau.
1. Buat dan tambahkan lapisan biru.
1. Simpan dokumen PDF.

PDF yang dihasilkan akan berisi tiga lapisan terpisah: sebuah garis merah, sebuah garis hijau, dan sebuah garis biru. Setiapnya dapat diaktifkan atau dinonaktifkan pada pembaca PDF yang mendukung konten berlapis.

```python

import aspose.pdf as ap
from os import path

def add_colored_layers(outfile: str, data_dir: str) -> None:
    """
    Creates a PDF with three layers (Red, Green, Blue lines).
    
    Args:
        outfile (str): Name of the output PDF file.
        data_dir (str): Directory path to save the file.
    """
    path_outfile = path.join(data_dir, outfile)

    try:
        # Create a new PDF document and add a blank page
        document = ap.Document()
        page = document.pages.add()

        # Helper function to add a colored line layer
        def add_layer(layer_id: str, layer_name: str, color: tuple, y_position: int):
            layer = ap.Layer(layer_id, layer_name)
            layer.contents.append(ap.operators.SetRGBColorStroke(*color))
            layer.contents.append(ap.operators.MoveTo(500, y_position))
            layer.contents.append(ap.operators.LineTo(400, y_position))
            layer.contents.append(ap.operators.Stroke())
            page.layers.append(layer)

        # Add Red, Green, and Blue layers
        add_layer("oc1", "Red Line", (1, 0, 0), 700)
        add_layer("oc2", "Green Line", (0, 1, 0), 750)
        add_layer("oc3", "Blue Line", (0, 0, 1), 800)

        # Save the document
        document.save(path_outfile)
        print(f"\nLayers added successfully.\nFile saved at: {path_outfile}")

    except Exception as e:
        print(f"Error adding layers: {e}")
```

## Kunci lapisan PDF

Dengan Aspose.PDF untuk Python via .NET Anda dapat membuka PDF, mengunci lapisan tertentu pada halaman pertama, dan menyimpan dokumen dengan perubahan.

Contoh ini menunjukkan cara mengunci sebuah lapisan (Optional Content Group, OCG) dalam dokumen PDF menggunakan Aspose.PDF untuk Python via .NET. Penguncian mencegah pengguna mengubah visibilitas lapisan pada penampil PDF, memastikan konten tetap selalu terlihat (atau tersembunyi) seperti yang ditentukan oleh dokumen.

Metode dan properti yang tersedia:

- layer.lock() – Mengunci lapisan.
- layer.unlock() – Membuka kunci lapisan.
- layer.locked – Mengembalikan status kunci saat ini.

1. Buka dokumen PDF.
1. Akses halaman pertama PDF.
1. Periksa apakah halaman memiliki lapisan.
1. Dapatkan lapisan pertama dan kunci.
1. Simpan PDF yang diperbarui.

Jika PDF berisi lapisan, lapisan pertama akan dikunci, memastikan status visibilitasnya tidak dapat diubah oleh pengguna. Jika tidak ada lapisan yang ditemukan, sebuah pesan akan ditampilkan sebagai gantinya.

```python

import aspose.pdf as ap
from os import path

def lock_layer(path_infile, path_outfile):
    with ap.Document(path_infile) as document:
        page = document.pages[1]
        layer = page.layers[0]

        # Lock the layer
        layer.lock()

        # Save updated PDF
        document.save(path_outfile)
```

## Ekstrak elemen lapisan PDF

Contoh ini menggunakan pustaka Aspose.PDF untuk Python via .NET untuk mengekstrak lapisan individu dari halaman pertama dokumen PDF dan menyimpan setiap lapisan sebagai file PDF terpisah.

Untuk membuat PDF baru dari sebuah lapisan, cuplikan kode berikut dapat digunakan:

1. Muat Dokumen PDF. PDF input dimuat ke dalam objek Aspose.PDF.Document.
1. Akses Lapisan pada Halaman 1. Skrip mengambil semua lapisan dari halaman pertama menggunakan document.pages[1].layers.
1. Periksa adanya Lapisan. Jika tidak ada lapisan yang ditemukan, sebuah pesan akan ditampilkan dan fungsi keluar.
1. Iterasi dan Simpan Setiap Lapisan.

```python

import aspose.pdf as ap
from os import path

def save_layers(path_infile, path_outfile):
    with ap.Document(path_infile) as document:
        layers = document.pages[1].layers

        # Save each layer to a new PDF
        for layer in layers:
            layer.save(path_outfile)
```

Dimungkinkan untuk mengekstrak elemen lapisan PDF dan menyimpannya ke dalam aliran file PDF baru:

```python

import aspose.pdf as ap
from os import path

def save_layers_to_stream(path_infile, output_stream):
    with ap.Document(path_infile) as document:
        layers = document.pages[1].layers
        for layer in layers:
            layer.save(output_stream)
```

## Ratakan PDF berlapis

Script ini menggunakan Aspose.PDF untuk Python via .NET untuk meratakan semua lapisan pada halaman pertama dokumen PDF. Proses perataan menggabungkan konten visual setiap lapisan menjadi satu lapisan terpadu, memudahkan pencetakan, berbagi, atau pengarsipan tanpa kehilangan fidelitas visual atau data khusus lapisan.

1. Muat Dokumen PDF. PDF masukan dimuat ke dalam objek Aspose.PDF.Document.
1. Akses Lapisan pada Halaman 1. Skrip mengambil semua lapisan dari halaman pertama menggunakan document.pages[1].layers.
1. Periksa Keberadaan Lapisan. Jika tidak ada lapisan yang ditemukan, pesan akan dicetak dan fungsi keluar.
1. Ratakan Setiap Lapisan. Setiap lapisan diratakan menggunakan layer.flatten(True), yang menggabungkan isinya ke dalam halaman.
1. Simpan Dokumen yang Dimodifikasi.

```python

import aspose.pdf as ap
from os import path

def flatten_layers(path_infile, path_outfile):
    with ap.Document(path_infile) as document:
        page = document.pages[1]

        if not page.layers:
            print("No layers found in the document.")
            return
        # Flatten each layer
        for layer in page.layers:
            layer.flatten(cleanup_content_stream=True)

        document.save(path_outfile)
```

## Gabungkan Semua Lapisan di dalam PDF menjadi satu

Potongan kode ini menggunakan Aspose.PDF untuk menggabungkan semua lapisan pada halaman pertama PDF menjadi satu lapisan terpadu dengan nama khusus.

1. Muat Dokumen PDF. PDF dimuat ke dalam objek Aspose.PDF.Document.
1. Akses Halaman dan Lapisan-nya. Halaman pertama dipilih, dan lapisannya diambil.
1. Periksa Lapisan. Jika tidak ada lapisan, pesan dicetak dan proses keluar.
1. Tentukan Nama Lapisan Baru. Nama lapisan baru ("LayerNew") ditentukan untuk hasil penggabungan.
1. Gabungkan Lapisan. Jika ID grup konten opsional diberikan, itu digunakan dalam penggabungan. Jika tidak, lapisan digabungkan hanya dengan nama baru.
1. Simpan Dokumen

```python

import aspose.pdf as ap
from os import path

def merge_layers(path_infile, path_outfile, new_layer_name, optional_group_id=None):
    with ap.Document(path_infile) as document:
        page = document.pages[1]

        if optional_group_id:
            page.merge_layers(new_layer_name, optional_group_id)
        else:
            page.merge_layers(new_layer_name)

        document.save(path_outfile)
```
