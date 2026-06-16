---
title: Hapus Gambar dari File PDF menggunakan Python
linktitle: Hapus Gambar
type: docs
weight: 20
url: /id/python-net/delete-images-from-pdf-file/
description: Pelajari cara menghapus gambar tertentu atau semua gambar dari file PDF dengan Python.
lastmod: "2026-06-12"
TechArticle: true
AlternativeHeadline: Hapus gambar dari file PDF dengan Python
Abstract: Artikel ini menunjukkan cara menghapus gambar dari dokumen PDF dengan Aspose.PDF for Python via .NET. Artikel ini mencakup penghapusan sumber gambar tertentu dan menghapus semua gambar dari halaman yang dipilih.
---

Gunakan halaman ini ketika Anda perlu menghapus grafik yang tidak diperlukan, mengurangi ukuran PDF, atau membersihkan konten visual sensitif dari sebuah dokumen.

## Hapus Gambar dari File PDF

Gunakan langkah-langkah berikut untuk menghapus satu gambar dari halaman:

1. Muat PDF sumber dengan `ap.Document(infile)`.
1. Pilih halaman dan indeks sumber daya gambar.
1. Hapus gambar dengan `resources.images.delete(index)`.
1. Simpan PDF yang diperbarui.

```python
import aspose.pdf as ap


def delete_image(infile, outfile):
    document = ap.Document(infile)
    document.pages[1].resources.images.delete(1)
    document.save(outfile)
```

## Hapus Semua Gambar dari Halaman

Gunakan contoh ini untuk menghapus setiap gambar dari halaman tertentu.

```python
import aspose.pdf as ap


def delete_all_images_from_page(infile, outfile, page_number):
    document = ap.Document(infile)
    page = document.pages[page_number]

    while len(page.resources.images) != 0:
        page.resources.images.delete(1)

    document.save(outfile)
```

## Topik Gambar Terkait

- [Bekerja dengan gambar dalam PDF menggunakan Python](/pdf/id/python-net/working-with-images/)
- [Ganti gambar dalam file PDF yang sudah ada](/pdf/id/python-net/replace-image-in-existing-pdf-file/)
- [Ekstrak gambar dari file PDF](/pdf/id/python-net/extract-images-from-pdf-file/)
- [Tambahkan gambar ke file PDF yang ada](/pdf/id/python-net/add-image-to-existing-pdf-file/)