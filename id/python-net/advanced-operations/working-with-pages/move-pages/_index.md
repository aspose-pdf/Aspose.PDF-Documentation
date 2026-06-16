---
title: Pindahkan Halaman PDF dalam Python
linktitle: Memindahkan Halaman PDF
type: docs
weight: 100
url: /id/python-net/move-pages/
description: Pelajari cara memindahkan halaman PDF dalam sebuah dokumen atau antara dokumen dalam Python.
lastmod: "2026-06-12"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Pindahkan halaman PDF antara dokumen dalam Python
Abstract: Artikel ini menjelaskan cara memindahkan halaman dalam PDF menggunakan Aspose.PDF for Python via .NET. Pelajari cara memindahkan satu halaman atau beberapa halaman ke dokumen lain, dan cara memposisikan kembali sebuah halaman dalam PDF yang sama menggunakan API Document dan PageCollection.
---

## Pindahkan Halaman dari Satu Dokumen PDF ke Dokumen Lain

Aspose.PDF for Python memungkinkan Anda memindahkan halaman (bukan hanya menyalinnya) dari satu PDF ke PDF lain. Ia menghapus halaman yang dipilih dari dokumen asli dan kemudian menambahkannya ke file PDF baru.

Anggap saja seperti memotong halaman dari satu buku dan menempelkannya ke buku lain — halaman tersebut tidak lagi ada di file asli setelah dipindahkan.

1. Buka dokumen PDF sumber menggunakan the [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) kelas.
1. Pilih halaman spesifik untuk dipindahkan (dalam hal ini, halaman 2) — ini merujuk pada a [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/).
1. Buat dokumen PDF baru (instansiasi lainnya [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)).
1. Tambahkan halaman yang dipilih ke dokumen PDF baru menggunakan dokumen tujuan’s [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) (misalnya, `another_document.pages.add(page)`).
1. Hapus halaman dari dokumen asli melalui [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) (misalnya, `document.pages.delete(index)`).
1. Simpan kedua dokumen.

Potongan kode berikut menunjukkan cara memindahkan satu halaman.

```python
import aspose.pdf as ap

def move_page_from_one_document_to_another(
    input_file_name: str, output_file_name: str
) -> None:

    document = ap.Document(input_file_name)
    page = document.pages[2]
    another_document = ap.Document()
    another_document.pages.add(page)
    document.pages.delete(2)
    document.save(input_file_name.replace(".pdf", "_new.pdf"))
    another_document.save(output_file_name)
```

## Pindahkan Beberapa Halaman dari Satu Dokumen PDF ke Dokumen Lain

Tidak seperti menyalin, operasi ini memindahkan halaman yang dipilih — menghapusnya dari file sumber dan menyimpannya dalam PDF baru.

1. Buat dokumen tujuan baru yang kosong (`Document`).
1. Pilih beberapa halaman (dalam hal ini, halaman 1 dan 3) dari dokumen sumber [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
1. Lakukan perulangan pada halaman yang dipilih dan tambahkan masing‑masing ke dokumen tujuan [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
1. Simpan dokumen tujuan yang berisi halaman yang dipindahkan.
1. Hapus halaman yang dipindahkan dari dokumen sumber menggunakan its [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
1. Simpan dokumen sumber yang dimodifikasi dengan nama file baru untuk mempertahankan kedua versi.

Potongan kode berikut menunjukkan cara memindahkan beberapa halaman.

```python
import aspose.pdf as ap

def move_multiple_pages_from_one_document_to_another(
    input_file_name: str, output_file_name: str
) -> None:
    src_document = ap.Document(input_file_name)
    dst_document = ap.Document()
    pages = [1, 2]
    for page_index in pages:
        page = src_document.pages[page_index]
        dst_document.pages.add(page)
    # Save output files
    dst_document.save(output_file_name)
    src_document.pages.delete(pages)
    src_document.save(input_file_name.replace(".pdf", "_new.pdf"))
```

## Pindahkan Halaman ke Lokasi Baru dalam Dokumen PDF yang Sama

Ini menunjukkan cara memindahkan halaman tertentu ke posisi yang berbeda dalam dokumen yang sama — kebutuhan umum saat mengatur ulang atau mengedit tata letak PDF.

1. Muat dokumen PDF input menggunakan [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) kelas.
1. Pilih halaman yang ingin Anda pindahkan (halaman 2) — ini adalah sebuah [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/).
1. Tambahkan ke akhir dokumen menggunakan dokumen’s [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
1. Hapus halaman asli dari lokasi sebelumnya melalui [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
1. Simpan dokumen yang dimodifikasi sebagai file baru.

```python
import aspose.pdf as ap

def move_page_in_new_location_in_same_document(
    input_file_name: str, output_file_name: str
) -> None:
    src_document = ap.Document(input_file_name)

    page = src_document.pages[2]
    src_document.pages.add(page)
    src_document.pages.delete(2)

    # Save output file
    src_document.save(output_file_name)
```

## Topik Halaman Terkait

- [Bekerja dengan halaman PDF di Python](/pdf/id/python-net/working-with-pages/)
- [Tambahkan halaman PDF di Python](/pdf/id/python-net/add-pages/)
- [Hapus halaman PDF di Python](/pdf/id/python-net/delete-pages/)
- [Ekstrak halaman PDF di Python](/pdf/id/python-net/extract-pages/)
