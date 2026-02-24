---
title: Bekerja dengan lapisan PDF menggunakan Python
linktitle: Bekerja dengan lapisan PDF
type: docs
weight: 50
url: /id/python-net/work-with-pdf-layers/
description: Artikel ini menjelaskan cara mengunci lapisan PDF, mengekstrak elemen lapisan PDF, meratakan PDF berlapis, dan menggabungkan semua lapisan dalam sebuah PDF menjadi satu.
lastmod: "2025-11-16"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cara mengelola, mengunci, mengekstrak, meratakan, dan menggabungkan lapisan PDF di Python
Abstract: Artikel ini menjelaskan cara bekerja dengan lapisan PDF di Python menggunakan Aspose.PDF untuk .NET, termasuk mengunci lapisan, mengekstrak elemen lapisan, meratakan PDF berlapis, dan menggabungkan lapisan.
---

Lapisan PDF memungkinkan dokumen berisi beberapa set konten yang dapat ditampilkan atau disembunyikan secara selektif. Setiap lapisan dapat mencakup teks, gambar, atau grafik, dan pengguna dapat mengaktifkan atau menonaktifkannya sesuai kebutuhan. Lapisan sangat berguna dalam dokumen kompleks di mana konten harus diatur atau dipisahkan. Contoh di bawah ini menggunakan API [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) dan [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) serta memanipulasi objek [`Layer`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/) melalui koleksi `layers` pada halaman.

## Mengunci lapisan PDF

Dengan Aspose.PDF untuk Python via .NET Anda dapat membuka PDF (lihat [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)), mengunci [`Layer`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/) tertentu pada halaman pertama [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/), dan menyimpan dokumen dengan perubahan.

Metode dan properti yang tersedia pada objek [`Layer`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/):

- `layer.lock()` – Mengunci lapisan. (lihat [`Layer.lock()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/#methods))
- `layer.unlock()` – Membuka kunci lapisan. (lihat [`Layer.unlock()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/#methods))
- `layer.locked` – Mengembalikan status kunci saat ini. (lihat [`Layer.locked`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/#properties))

1. Buka dokumen PDF (lihat [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)).
1. Dapatkan halaman pertama menggunakan koleksi [`Pages`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties) dokumen (lihat [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/)).
1. Pilih [`Layer`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/) yang akan dikunci dari `page.layers`.
1. Panggil `layer.lock()` untuk mencegah pengguna mengubah visibilitas lapisan.
1. Simpan dokumen yang diperbarui menggunakan [`Document.save()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods).

```python

import aspose.pdf as ap

def lock_layer(path_infile, path_outfile):
    with ap.Document(path_infile) as document:
        page = document.pages[1]
        layer = page.layers[0]

        # Lock the layer
        layer.lock()

        # Save updated PDF
        document.save(path_outfile)
```

## Mengekstrak elemen lapisan PDF

Aspose.PDF memungkinkan Anda mengekstrak setiap [`Layer`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/) dari sebuah [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) dan menyimpannya sebagai file PDF terpisah.

Untuk membuat PDF baru dari sebuah lapisan, potongan kode berikut dapat digunakan (koleksi `layers` diakses melalui `Page.layers`):

```python

import aspose.pdf as ap

def save_layers(path_infile, path_outfile):
    with ap.Document(path_infile) as document:
        layers = document.pages[1].layers

        # Save each layer to a new PDF with a unique filename
        for i, layer in enumerate(layers):
            layer.save(f"{path_outfile}_layer_{i}.pdf")
```

Anda juga dapat menyimpan lapisan ke dalam aliran:

```python

import aspose.pdf as ap
import io

def save_layers_to_stream(path_infile):
    with ap.Document(path_infile) as document:
        layers = document.pages[1].layers
        streams = []
        for layer in layers:
            layer_stream = io.BytesIO()
            layer.save(layer_stream)
            layer_stream.seek(0)
            streams.append(layer_stream)
        return streams
```

## Meratakan PDF berlapis

Pemrosesan flatten membuat [`Layer`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/) menjadi permanen pada halaman, menghapus fungsi togglenya.

```python

import aspose.pdf as ap

def flatten_layers(path_infile, path_outfile):
    with ap.Document(path_infile) as document:
        page = document.pages[1]

        # Flatten each layer
        for layer in page.layers:
            layer.flatten(cleanup_content_stream=True)

        document.save(path_outfile)
```

Parameter `cleanup_content_stream` mengontrol apakah penanda grup konten opsional (OCG markers) dihapus. Mengatur ke `False` mempercepat proses flattening. Lihat metode [`Layer.flatten()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/#methods) untuk detail.

## Menggabungkan Semua Lapisan dalam PDF menjadi satu

Anda dapat menggabungkan semua lapisan (atau yang tertentu) menjadi satu [`Layer`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/) baru (API penggabungan ada pada objek [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/)).

Metode pada objek [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/):

- `page.merge_layers(new_layer_name)` — menggabungkan semua lapisan menjadi nama lapisan baru (lihat [`Page.MergeLayers()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#methods)).
- `page.merge_layers(new_layer_name, new_optional_content_group_id)` — menggabungkan menggunakan ID grup konten opsional khusus (lihat [`Page.MergeLayers()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#methods)).

```python

import aspose.pdf as ap

def merge_layers(path_infile, path_outfile, new_layer_name, optional_group_id=None):
    with ap.Document(path_infile) as document:
        page = document.pages[1]

        if optional_group_id:
            page.merge_layers(new_layer_name, optional_group_id)
        else:
            page.merge_layers(new_layer_name)

        document.save(path_outfile)
```
