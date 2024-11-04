---
title: Menghapus lampiran dari PDF 
linktitle: Menghapus lampiran dari PDF yang ada
type: docs
weight: 30
url: /cpp/removing-attachment-from-an-existing-pdf/
description: Aspose.PDF untuk C++ dapat menghapus lampiran dari dokumen PDF Anda. Gunakan API PDF C++ untuk menghapus lampiran dalam file PDF menggunakan pustaka Aspose.PDF.
lastmod: "2022-02-07"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Aspose.PDF dapat menghapus lampiran dari file PDF. Lampiran dari dokumen PDF disimpan dalam koleksi EmbeddedFiles dari objek Document.

Untuk menghapus semua lampiran yang terkait dengan file PDF:

1. Panggil metode [Delete](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.embedded_file_collection#afff8b235b554a66c203464b61204b843) dari koleksi [EmbeddedFiles](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.embedded_file_collection).
1. Simpan file yang telah diperbarui menggunakan metode Save dari objek [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document).

Berikut adalah potongan kode yang menunjukkan cara menghapus lampiran dari dokumen PDF.

```cpp
void WorkingWithAttachments::RemovingAttachment() {

 String _dataDir("C:\\Samples\\");

 // Buka dokumen
 auto pdfDocument = new Document(_dataDir + u"DeleteAllAttachments.pdf");

 // Hapus semua lampiran
 pdfDocument->get_EmbeddedFiles()->Delete();

 // Simpan file yang diperbarui
 pdfDocument->Save(_dataDir + u"DeleteAllAttachments_out.pdf");
}
```