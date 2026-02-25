---
title: Menghapus lampiran dari PDF menggunakan Python
linktitle: Menghapus lampiran dari PDF yang ada
type: docs
weight: 30
url: /id/python-net/removing-attachment-from-an-existing-pdf/
description: Aspose.PDF dapat menghapus lampiran dari dokumen PDF Anda. Gunakan API PDF Python untuk menghapus lampiran dalam file PDF menggunakan Aspose.PDF untuk Python via perpustakaan .NET.
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cara menghapus lampiran dari PDF dengan Python
Abstract: Artikel ini membahas cara menghapus lampiran dari file PDF menggunakan Aspose.PDF untuk Python. Lampiran dalam dokumen PDF disimpan dalam koleksi `EmbeddedFiles` objek `Document`. Untuk menghapus semua lampiran dari PDF, Anda dapat memanggil metode `delete()` pada koleksi `EmbeddedFiles` dan kemudian menyimpan dokumen yang telah diperbarui menggunakan metode `save()` dari objek `Document`. Sebuah potongan kode disediakan untuk menunjukkan proses ini, menampilkan langkah-langkah membuka dokumen, menghapus lampirannya, dan menyimpan file yang telah dimodifikasi.
---

Aspose.PDF untuk Python dapat menghapus lampiran dari file PDF. Lampiran dokumen PDF disimpan dalam koleksi [FileTertanam](https://reference.aspose.com/pdf/python-net/aspose.pdf/embeddedfilecollection/) objek Document.

Untuk menghapus semua lampiran yang terkait dengan file PDF:

1. Panggil metode [delete()](https://reference.aspose.com/pdf/python-net/aspose.pdf/embeddedfilecollection/#methods) pada koleksi [FileTertanam](https://reference.aspose.com/pdf/python-net/aspose.pdf/embeddedfilecollection/).
1. Simpan file yang diperbarui menggunakan metode [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) pada objek [Dokumen](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).

Potongan kode berikut menunjukkan cara menghapus lampiran dari dokumen PDF.

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)

    # Delete all attachments
    document.embedded_files.delete()

    # Save updated file
    document.save(output_pdf)
```


