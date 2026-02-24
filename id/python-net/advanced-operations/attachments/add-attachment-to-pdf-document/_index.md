---
title: Menambahkan Lampiran ke Dokumen PDF menggunakan Python
linktitle: Menambahkan Lampiran ke Dokumen PDF
type: docs
weight: 10
url: /id/python-net/add-attachment-to-pdf-document/
description: Halaman ini menjelaskan cara menambahkan lampiran ke file PDF dengan Aspose.PDF untuk Python melalui perpustakaan .NET.
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cara Menambahkan Lampiran ke PDF dengan Python
Abstract: Artikel ini menyediakan panduan langkah demi langkah tentang cara menambahkan lampiran ke file PDF menggunakan Python dan perpustakaan Aspose.PDF. Artikel ini merinci proses menyiapkan proyek Python baru, mengimpor paket Aspose.PDF yang diperlukan, dan membuat objek `Document`. Artikel menjelaskan cara membuat objek `FileSpecification` dengan file dan deskripsi yang diinginkan, serta cara menambahkan objek ini ke `EmbeddedFileCollection` dokumen PDF menggunakan metode `add`. `EmbeddedFileCollection` menyimpan semua lampiran dalam PDF. Sebuah potongan kode disertakan untuk mendemonstrasikan proses membuka dokumen, menyiapkan file untuk lampiran, menambahkannya ke koleksi lampiran dokumen, dan menyimpan PDF yang telah diperbarui.
---

Lampiran dapat berisi berbagai macam informasi dan dapat berupa berbagai jenis file. Artikel ini menjelaskan cara menambahkan lampiran ke file PDF.

1. Buat proyek Python baru.
1. Impor paket Aspose.PDF
1. Buat objek [Dokumen](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) .
1. Buat objek [FileSpecification](https://reference.aspose.com/pdf/python-net/aspose.pdf/filespecification/) dengan file yang Anda tambahkan, dan deskripsi file.
1. Tambahkan objek [FileSpecification](https://reference.aspose.com/pdf/python-net/aspose.pdf/filespecification/) ke koleksi [EmbeddedFileCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/embeddedfilecollection/) objek [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/), dengan metode [add](https://reference.aspose.com/pdf/python-net/aspose.pdf/embeddedfilecollection/#methods).

Koleksi [EmbeddedFileCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/embeddedfilecollection/) berisi semua lampiran dalam file PDF. Potongan kode berikut menunjukkan cara menambahkan lampiran dalam dokumen PDF.

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)

    # Setup new file to be added as attachment
    fileSpecification = ap.FileSpecification(attachment_file, "Sample text file")

    # Add attachment to document's attachment collection
    document.embedded_files.append(fileSpecification)

    # Save new output
    document.save(output_pdf)
```


