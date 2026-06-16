---
title: Bekerja dengan Lapisan PDF menggunakan Python
linktitle: Bekerja dengan lapisan PDF
type: docs
weight: 50
url: /id/python-net/working-with-pdf-layers/
description: Pelajari cara menambahkan, mengunci, mengekstrak, meratakan, dan menggabungkan lapisan PDF dalam Python.
lastmod: "2026-06-12"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Kelola lapisan PDF dengan Python
Abstract: Artikel ini menjelaskan cara bekerja dengan lapisan PDF (Optional Content Groups) dengan menggunakan Aspose.PDF for Python via .NET. Pelajari cara menambahkan lapisan, mengunci visibilitas lapisan, mengekstrak konten lapisan, meratakan konten berlapis, dan menggabungkan lapisan menjadi satu.
---

Lapisan PDF, juga disebut Optional Content Groups (OCGs), memungkinkan Anda mengatur konten ke dalam grup visual terpisah yang dapat ditampilkan atau disembunyikan di penampil PDF yang kompatibel. Di Aspose.PDF, operasi lapisan dibangun di sekitar [`Layer`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/) API.

Dengan Aspose.PDF for Python via .NET, Anda dapat:

- Tambahkan beberapa lapisan ke halaman.
- Kunci dan buka kunci lapisan untuk mengontrol perilaku visibilitas.
- Ekstrak lapisan ke dalam file atau aliran terpisah.
- Ratakan konten berlapis ke halaman.
- Gabungkan beberapa lapisan menjadi satu lapisan.

## Tambahkan Lapisan ke PDF

Contoh ini membuat PDF dengan tiga lapisan. Ini menggunakan sebuah [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/), menambahkan sebuah [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/), dan menambahkan [`Layer`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/) objek ke halaman itu.

1. Buat yang baru [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) dan tambahkan sebuah [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/).
1. Buat dan tambahkan lapisan merah.
1. Buat dan tambahkan lapisan hijau.
1. Buat dan tambahkan lapisan biru.
1. Simpan dokumen PDF.

PDF yang dihasilkan akan berisi tiga lapisan terpisah: sebuah garis merah, sebuah garis hijau, dan sebuah garis biru. Setiap lapisan dapat diaktifkan atau dinonaktifkan di pembaca PDF yang mendukung konten berlapis.

```python
import aspose.pdf as ap

def add_layers(outfile: str) -> None:
    document = ap.Document()
    page = document.pages.add()

    # Red layer
    layer = ap.Layer("oc1", "Red Line")
    layer.contents.append(ap.operators.SetRGBColorStroke(1, 0, 0))
    layer.contents.append(ap.operators.MoveTo(500, 700))
    layer.contents.append(ap.operators.LineTo(400, 700))
    layer.contents.append(ap.operators.Stroke())
    page.layers.append(layer)

    # Green layer
    layer = ap.Layer("oc2", "Green Line")
    layer.contents.append(ap.operators.SetRGBColorStroke(0, 1, 0))
    layer.contents.append(ap.operators.MoveTo(500, 750))
    layer.contents.append(ap.operators.LineTo(400, 750))
    layer.contents.append(ap.operators.Stroke())
    page.layers.append(layer)

    # Blue layer
    layer = ap.Layer("oc3", "Blue Line")
    layer.contents.append(ap.operators.SetRGBColorStroke(0, 0, 1))
    layer.contents.append(ap.operators.MoveTo(500, 800))
    layer.contents.append(ap.operators.LineTo(400, 800))
    layer.contents.append(ap.operators.Stroke())
    page.layers.append(layer)

    document.save(outfile)
    print(f"Layers added successfully. File saved at {outfile}")
```

## Kunci Lapisan PDF

Contoh ini membuka sebuah PDF, mengunci lapisan tertentu pada halaman pertama, dan menyimpan file yang diperbarui.

Mengunci lapisan mencegah pengguna mengubah status visibilitas lapisan tersebut di penampil PDF yang mendukung. Lapisan diakses dari sebuah halaman dan dikelola melalui koleksi lapisan halaman tersebut.

Metode dan properti yang tersedia:

- [`Layer.lock()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/#methods) mengunci lapisan.
- [`Layer.unlock()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/#methods) membuka kunci lapisan.
- [`Layer.locked`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/#properties) mengembalikan status kunci saat ini.

1. Buka dokumen PDF.
1. Akses halaman pertama PDF.
1. Periksa apakah halaman memiliki lapisan.
1. Dapatkan lapisan pertama dan kunci.
1. Simpan PDF yang diperbarui.

Jika PDF berisi lapisan, lapisan pertama akan dikunci, memastikan keadaan visibilitasnya tidak dapat diubah oleh pengguna. Jika tidak ada lapisan yang ditemukan, pesan akan dicetak sebagai gantinya.

```python
import aspose.pdf as ap

def lock_layer(infile: str, outfile: str) -> None:
    document = ap.Document(infile)
    page = document.pages[1]

    if len(page.layers) > 0:
        layer = page.layers[0]
        layer.lock()
        document.save(outfile)
        print(f"Layer locked successfully. File saved at {outfile}")
    else:
        print("No layers found in the document.")
```

## Ekstrak Elemen Lapisan PDF

Contoh ini menggunakan pustaka Aspose.PDF for Python via .NET untuk mengekstrak lapisan individu dari halaman pertama dokumen PDF dan menyimpan setiap lapisan sebagai file PDF terpisah dengan menggunakan [`Layer.save()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/#methods).

Untuk membuat PDF baru dari lapisan, cuplikan kode berikut dapat digunakan:

1. Muat PDF [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Akses lapisan pada halaman 1 sampai [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/).
1. Periksa apakah lapisan ada.
1. Iterasi melalui lapisan dan simpan masing-masing.

```python
import aspose.pdf as ap

def extract_layers(infile: str, outfile: str) -> None:
    document = ap.Document(infile)
    layers = document.pages[1].layers

    if len(layers) == 0:
        print("No layers found in the document.")
        return

    index = 1
    for layer in layers:
        output_file = outfile.replace(".pdf", f"{index}.pdf")
        layer.save(output_file)
        print(f"Layer {index} saved to {output_file}")
        index += 1
```

Dimungkinkan untuk mengekstrak elemen lapisan PDF dan menyimpannya ke dalam aliran file PDF baru:

```python
from io import FileIO
import aspose.pdf as ap

def extract_layers_stream(infile: str, outfile: str) -> None:
    document = ap.Document(infile)

    if len(document.pages[1].layers) == 0:
        print("No layers found in the document.")
        return

    layer = document.pages[1].layers[0]

    with FileIO(outfile, "wb") as output_layer:
        layer.save(output_layer)
    print(f"Layer extracted to stream: {outfile}")
```

## Meratakan PDF Berlapis

Skrip ini menggunakan Aspose.PDF for Python via .NET untuk meratakan semua lapisan pada halaman pertama dari dokumen PDF. Proses perataan menggabungkan konten visual setiap lapisan menjadi satu lapisan terpadu, sehingga lebih mudah untuk mencetak, berbagi, atau mengarsipkan tanpa kehilangan fidelitas visual atau data spesifik lapisan. Operasi ini dilakukan dengan [`Layer.flatten()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/#methods).

1. Muat dokumen PDF.
1. Akses lapisan pada halaman 1.
1. Periksa apakah lapisan ada.
1. Ratakan setiap lapisan dengan `layer.flatten(True)`.
1. Simpan dokumen yang telah dimodifikasi.

```python
import aspose.pdf as ap

def flatten_layers(infile: str, outfile: str) -> None:
    document = ap.Document(infile)
    layers = document.pages[1].layers

    if len(layers) == 0:
        print("No layers found in the document.")
        return

    for layer in layers:
        layer.flatten(True)

    document.save(outfile)
    print(f"Layers flattened successfully. File saved at {outfile}")
```

## Gabungkan Semua Lapisan dalam PDF menjadi Satu

Potongan kode ini menggunakan Aspose.PDF untuk menggabungkan semua lapisan pada halaman pertama PDF menjadi satu lapisan terpadu dengan nama khusus dengan menggunakan [`Page.merge_layers()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#methods).

1. Muat dokumen PDF.
1. Akses halaman 1 dan ambil lapisannya.
1. Periksa apakah lapisan ada.
1. Tentukan nama lapisan baru.
1. Gabungkan lapisan menjadi satu.
1. Simpan dokumen.

```python
import aspose.pdf as ap

def merge_layers(infile: str, outfile: str) -> None:
    document = ap.Document(infile)
    page = document.pages[1]

    if len(page.layers) == 0:
        print("No layers found in the document.")
        return

    new_layer_name = "LayerNew"
    page.merge_layers(new_layer_name)
    document.save(outfile)
    print(f"Layers merged successfully. File saved at {outfile}")
```

## Topik Lapisan Terkait

- [Bekerja dengan halaman PDF di Python](/pdf/id/python-net/working-with-pages/)
- [Bekerja dengan tabel di PDF menggunakan Python](/pdf/id/python-net/working-with-tables/)
- [Tambahkan halaman PDF di Python](/pdf/id/python-net/add-pages/)
