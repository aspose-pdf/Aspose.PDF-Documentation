---
title: Hapus Lampiran dari PDF dengan Python
linktitle: Menghapus lampiran dari PDF yang ada
type: docs
weight: 30
url: /id/python-net/removing-attachment-from-an-existing-pdf/
description: Aspose.PDF dapat menghapus lampiran dari dokumen PDF Anda. Gunakan API PDF Python untuk menghapus lampiran dalam file PDF menggunakan Aspose.PDF for Python via .NET library.
lastmod: "2026-06-12"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cara menghapus lampiran dari PDF dengan Python
Abstract: Artikel ini membahas cara menghapus lampiran dari file PDF menggunakan Aspose.PDF for Python. Lampiran dalam dokumen PDF disimpan dalam koleksi `EmbeddedFiles` dari objek `Document`. Untuk menghapus semua lampiran dari PDF, Anda dapat memanggil metode `delete()` pada koleksi `EmbeddedFiles` dan kemudian menyimpan dokumen yang diperbarui menggunakan metode `save()` dari objek `Document`. Sebuah cuplikan kode disediakan untuk mendemonstrasikan proses ini, menampilkan langkah-langkah membuka dokumen, menghapus lampirannya, dan menyimpan file yang telah dimodifikasi.
---

Aspose.PDF for Python dapat menghapus lampiran dari file PDF. Lampiran dokumen PDF disimpan di objek Document. [File Tertanam](https://reference.aspose.com/pdf/python-net/aspose.pdf/embeddedfilecollection/) koleksi.

Alur kerja ini berguna ketika Anda perlu membersihkan file tertanam yang usang, mengurangi ukuran paket, atau menyiapkan PDF untuk distribusi ulang tanpa materi sumber yang terlampir.

Untuk menghapus semua lampiran yang terkait dengan file PDF:

1. Panggil [File Tertanam](https://reference.aspose.com/pdf/python-net/aspose.pdf/embeddedfilecollection/) koleksi [delete()](https://reference.aspose.com/pdf/python-net/aspose.pdf/embeddedfilecollection/#methods) metode.
1. Simpan file yang diperbarui menggunakan [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) objek [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) metode.

Potongan kode berikut menunjukkan cara menghapus lampiran dari dokumen PDF.

```python

import aspose.pdf as ap

def remove_attachment(infile, outfile):
    # Open PDF document
    with ap.Document(infile) as document:
        document.embedded_files.delete()
        document.save(outfile)
```

## Hapus lampiran tertentu berdasarkan nama

Jika Anda perlu menghapus hanya satu lampiran dan mempertahankan yang lain, gunakan the [delete_by_key()](https://reference.aspose.com/pdf/python-net/aspose.pdf/embeddedfilecollection/delete_by_key/) metode dan berikan nama lampiran.

Untuk menghapus lampiran tertentu:

1. Buka file PDF sumber.
1. Panggilan `document.embedded_files.delete_by_key(attachment_name)`.
1. Simpan file PDF yang diperbarui.

Potongan kode berikut menghapus satu lampiran berdasarkan namanya.

```python

import aspose.pdf as ap

def remove_attachment(infile, attachment_name, outfile):
    # Open PDF document
    with ap.Document(infile) as document:
        document.embedded_files.delete_by_key(attachment_name)
        document.save(outfile)
```

## Topik Lampiran Terkait

- [Bekerja dengan lampiran PDF di Python](/pdf/id/python-net/attachments/)
- [Menambahkan lampiran ke PDF di Python](/pdf/id/python-net/add-attachment-to-pdf-document/)
- [Buat dan kelola portofolio PDF menggunakan Python](/pdf/id/python-net/portfolio/)

