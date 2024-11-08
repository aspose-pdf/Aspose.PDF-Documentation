```
---
title: Hapus Halaman PDF secara programatis
linktitle: Hapus Halaman PDF
type: docs
weight: 30
url: /id/cpp/delete-pages/
description: Anda dapat menghapus halaman dari file PDF Anda menggunakan pustaka C++.
lastmod: "2021-12-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Anda dapat menghapus halaman dari file PDF menggunakan Aspose.PDF untuk C++. Untuk menghapus halaman tertentu dari koleksi [PageCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection).

## Hapus Halaman dari File PDF

1. Panggil metode [Delete](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page#a02bb7a96e66ef6e10bcf4930b299b3b7) dan tentukan indeks halaman
1. Panggil metode Save untuk menyimpan file PDF yang telah diperbarui
Cuplikan kode berikut menunjukkan cara menghapus halaman tertentu dari file PDF menggunakan C++.

```cpp
void DeletePDFPages() {
    String _dataDir("C:\\Samples\\");
    String inputFileName("DeleteParticularPage.pdf");

    // Buka dokumen
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // Hapus halaman tertentu
    document->get_Pages()->Delete(2);

    // Simpan PDF yang diperbarui
    document->Save(_dataDir + inputFileName);
}
```
```