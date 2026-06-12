---
title: Tambah Halaman PDF di Python
linktitle: Menambahkan Halaman
type: docs
weight: 10
url: /id/python-net/add-pages/
description: Pelajari cara menambahkan atau menyisipkan halaman ke dalam dokumen PDF menggunakan Python.
lastmod: "2026-06-12"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Tambahkan atau sisipkan halaman PDF dengan Python
Abstract: Artikel ini menjelaskan cara menambahkan halaman ke file PDF menggunakan Aspose.PDF for Python via .NET. Pelajari cara menyisipkan halaman kosong pada posisi tertentu, menambahkan halaman di akhir dokumen, dan mengimpor halaman dari PDF lain menggunakan API Document dan PageCollection.
---

Aspose.PDF for Python via .NET menyediakan operasi tingkat halaman yang fleksibel untuk dokumen PDF. Anda dapat mengelola halaman melalui [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) dan menambahkan halaman ke sebuah [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) pada posisi tertentu atau di akhir file.

Gunakan halaman ini ketika Anda perlu menyisipkan halaman kosong baru ke dalam PDF yang ada atau menambahkan halaman ke akhir dokumen selama alur kerja pembuatan.

## Tambahkan atau Sisipkan Halaman dalam File PDF

Aspose.PDF for Python via .NET mendukung baik penyisipan halaman pada indeks tertentu maupun penambahan halaman di akhir PDF.

### Menyisipkan Halaman Kosong dalam File PDF

Untuk menyisipkan halaman kosong dalam file PDF:

1. Buka yang ada [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) menggunakan metode yang tepat.
1. Masukkan halaman kosong baru pada indeks tertentu menggunakan [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) `insert()` metode.
1. Simpan yang dimodifikasi [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) ke jalur output yang diinginkan.

Sisipkan halaman kosong ke dalam file PDF yang sudah ada pada posisi yang ditentukan:

```python
import aspose.pdf as ap

def insert_empty_page(input_file_name: str, output_file_name: str) -> None:
    document = ap.Document(input_file_name)
    document.pages.insert(2)
    document.save(output_file_name)
```

### Tambahkan Halaman Kosong di Akhir File PDF

Kadang-kadang, Anda ingin memastikan bahwa sebuah dokumen berakhir dengan halaman kosong. Topik ini menjelaskan cara menyisipkan halaman kosong di akhir dokumen PDF.

Untuk menyisipkan halaman kosong di akhir file PDF:

1. Buka yang ada [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) menggunakan metode yang tepat.
1. Tambahkan halaman kosong baru ke akhir dokumen menggunakan [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) `add()` metode.
1. Simpan yang diperbarui [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).

Potongan kode berikut menunjukkan cara menyisipkan halaman kosong di akhir file PDF.

```python
import aspose.pdf as ap

def add_empty_page_to_end(input_file_name: str, output_file_name: str) -> None:
    document = ap.Document(input_file_name)
    document.pages.add()
    document.save(output_file_name)
```

### Tambahkan Halaman dari Dokumen PDF Lain

Dengan Aspose.PDF for Python via .NET, Anda dapat membuat yang baru [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/), tambahkan halaman awal, dan kemudian impor halaman dari PDF lain ke dalamnya.

1. Buat yang baru [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Tambahkan yang kosong baru [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) dan tulis beberapa teks di atasnya menggunakan [`TextFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/textfragment/).
1. Buka yang lain yang sudah ada [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Salin sebuah [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) dari dokumen itu.
1. Tempel halaman yang disalin ke dokumen utama Anda menggunakan [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
1. Simpan file gabungan.

```python
import aspose.pdf as ap

def add_page_from_another_document(input_file_name: str, output_file_name: str) -> None:
    document = ap.Document()
    page = document.pages.add()
    text_fragment = ap.text.TextFragment("This is first page!")
    page.paragraphs.add(text_fragment)

    another_document = ap.Document(input_file_name)
    document.pages.add(another_document.pages[1])

    document.save(output_file_name)
```

## Topik Halaman Terkait

- [Bekerja dengan halaman PDF di Python](/pdf/id/python-net/working-with-pages/)
- [Pindahkan halaman PDF di Python](/pdf/id/python-net/move-pages/)
- [Hapus halaman PDF di Python](/pdf/id/python-net/delete-pages/)
- [Ekstrak halaman PDF dalam Python](/pdf/id/python-net/extract-pages/)
