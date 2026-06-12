---
title: Hapus Halaman PDF di Python
linktitle: Menghapus Halaman PDF
type: docs
weight: 80
url: /id/python-net/delete-pages/
description: Pelajari cara menghapus halaman dari file PDF di Python.
lastmod: "2026-06-12"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Hapus satu atau lebih halaman PDF di Python
Abstract: Artikel ini menjelaskan cara menghapus halaman dari file PDF menggunakan Aspose.PDF for Python via .NET. Pelajari cara menghapus satu halaman atau beberapa halaman dari dokumen dengan menggunakan API PageCollection dan kemudian menyimpan PDF yang telah diperbarui.
---

Anda dapat menghapus halaman dari file PDF menggunakan Aspose.PDF for Python via .NET. Untuk menghapus halaman tertentu, gunakan the [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) dari sebuah [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).

Gunakan alur kerja ini ketika Anda perlu menghapus halaman yang tidak diinginkan dari PDF sebelum membagikan, mengarsipkan, atau menggabungkan dokumen.

## Hapus Halaman dari File PDF

Aspose.PDF for Python via .NET menghapus halaman 2 dari PDF input dan menyimpan dokumen yang diperbarui ke file baru. Fitur ini berguna untuk menghapus halaman yang tidak diinginkan atau sensitif tanpa mengubah sisa dokumen.

1. Muat PDF input sebagai sebuah [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Hapus halaman menggunakan [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
1. Panggil [`Document.save()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) metode untuk menyimpan file PDF yang diperbarui.

Potongan kode berikut menunjukkan cara menghapus halaman tertentu dari file PDF menggunakan Python.

```python
import aspose.pdf as ap

def delete_page(input_file_name: str, output_file_name: str) -> None:
    document = ap.Document(input_file_name)
    document.pages.delete(2)
    document.save(output_file_name)
```

## Hapus Beberapa Halaman dari Dokumen PDF

Menghapus beberapa halaman memungkinkan Anda menghapus satu set halaman tertentu dalam satu operasi, yang lebih efisien daripada menghapus halaman satu per satu. PDF yang dihasilkan disimpan ke file baru, menjaga dokumen asli.

1. Muat PDF input sebagai sebuah [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Hapus halaman yang terdaftar dalam array pages menggunakan [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
1. Simpan yang diperbarui [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) ke file baru.

```python
import aspose.pdf as ap

def delete_multiple_pages(input_file_name: str, output_file_name: str) -> None:
    document = ap.Document(input_file_name)
    # Example: delete pages 2, 3, and 4.
    pages = [2, 3, 4]
    document.pages.delete(pages)
    document.save(output_file_name)
```

## Topik Halaman Terkait

- [Bekerja dengan halaman PDF di Python](/pdf/id/python-net/working-with-pages/)
- [Tambahkan halaman PDF di Python](/pdf/id/python-net/add-pages/)
- [Pindahkan halaman PDF di Python](/pdf/id/python-net/move-pages/)
- [Ekstrak halaman PDF dalam Python](/pdf/id/python-net/extract-pages/)
