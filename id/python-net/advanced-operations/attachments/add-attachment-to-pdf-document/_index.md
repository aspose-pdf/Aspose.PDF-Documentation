---
title: Tambahkan Lampiran ke PDF dengan Python
linktitle: Menambahkan Lampiran ke Dokumen PDF
type: docs
weight: 10
url: /id/python-net/add-attachment-to-pdf-document/
description: Pelajari cara menambahkan lampiran file ke dokumen PDF dalam Python menggunakan Aspose.PDF untuk Python via .NET.
lastmod: "2026-06-12"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cara menambahkan Lampiran ke PDF dengan Python
Abstract: Artikel ini memberikan panduan langkah demi langkah tentang cara menambahkan lampiran ke file PDF menggunakan Python dan pustaka Aspose.PDF. Ini merinci proses menyiapkan proyek Python baru, mengimpor paket Aspose.PDF yang diperlukan, dan membuat objek `Document`. Artikel ini menjelaskan cara membuat objek `FileSpecification` dengan file dan deskripsi yang diinginkan, serta cara menambahkan objek ini ke `EmbeddedFileCollection` dokumen PDF menggunakan metode `add`. `EmbeddedFileCollection` menyimpan semua lampiran dalam PDF. Sebuah potongan kode disertakan untuk menunjukkan proses membuka dokumen, menyiapkan file untuk lampiran, menambahkannya ke koleksi lampiran dokumen, dan menyimpan PDF yang diperbarui.
---

Lampiran dapat berisi berbagai jenis informasi dan dapat berupa beragam tipe file. Artikel ini menjelaskan cara menambahkan lampiran ke file PDF.

Gunakan lampiran PDF yang disematkan saat Anda perlu mengemas file sumber pendukung, spreadsheet, gambar, atau dokumen terkait bersama dengan PDF utama.

1. Buat proyek Python baru.
1. Impor paket Aspose.PDF
1. Buat sebuah [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) objek.
1. Buat sebuah [FileSpecification](https://reference.aspose.com/pdf/python-net/aspose.pdf/filespecification/) objek dengan file yang Anda tambahkan, dan deskripsi file.
1. Tambahkan [FileSpecification](https://reference.aspose.com/pdf/python-net/aspose.pdf/filespecification/) objek ke [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) objek [EmbeddedFileCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/embeddedfilecollection/) koleksi, dengan koleksi [tambahkan](https://reference.aspose.com/pdf/python-net/aspose.pdf/embeddedfilecollection/#methods) metode.

The [EmbeddedFileCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/embeddedfilecollection/) koleksi berisi semua lampiran dalam file PDF. Potongan kode berikut menunjukkan cara menambahkan lampiran dalam dokumen PDF.

```python
from os import path
import aspose.pdf as ap

def add_attachments(infile, attachment_path, outfile):
    with ap.Document(infile) as document:
        file_spec = ap.FileSpecification(attachment_path, "Sample text file")
        document.embedded_files.add(path.basename(attachment_path), file_spec)
        document.save(outfile)
```

## Topik Lampiran Terkait

- [Bekerja dengan lampiran PDF di Python](/pdf/id/python-net/attachments/)
- [Hapus lampiran dari PDF di Python](/pdf/id/python-net/removing-attachment-from-an-existing-pdf/)
- [Buat dan kelola portofolio PDF di Python](/pdf/id/python-net/portfolio/)

