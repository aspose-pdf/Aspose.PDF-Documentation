---
title: Menggabungkan PDF menggunakan C++
linktitle: Menggabungkan file PDF
type: docs
weight: 50
url: /id/cpp/merge-pdf-documents/
description: Halaman ini menjelaskan cara menggabungkan dokumen PDF menjadi satu file PDF dengan C++.
lastmod: "2021-11-11"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Menggabungkan file PDF bukanlah tugas yang mudah, tetapi sangat populer. Anda dapat menggunakan pustaka Aspose.PDF untuk C++ untuk menggabungkan file PDF menjadi satu dokumen dengan cepat dan mudah.

## Menggabungkan File PDF menggunakan C++

Untuk menggabungkan dua file PDF:

1. Buat dua objek [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document), masing-masing berisi salah satu file PDF masukan.
1. Kemudian panggil metode Add koleksi [PageCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection) untuk objek Document yang ingin Anda tambahkan file PDF lainnya.
1. Tambahkan [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page) dari dokumen kedua ke file pertama.
1. Akhirnya, simpan file PDF keluaran menggunakan metode Save.

Cuplikan kode berikut menunjukkan cara menggabungkan file PDF.

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;
void MergingDocuments() {
    // String untuk nama path
    String _dataDir("C:\\Samples\\");

    // String untuk nama file input
    String pdfDocumentFileName1("Concat1.pdf");
    String pdfDocumentFileName2("Concat2.pdf");
    String outputFileName("ConcatenatePdfFiles.pdf");

    // Buka dokumen
    auto pdfDocument1 = MakeObject<Document>(_dataDir + pdfDocumentFileName1);
    auto pdfDocument2 = MakeObject<Document>(_dataDir + pdfDocumentFileName2);

    // Tambahkan halaman dari dokumen kedua ke yang pertama
    pdfDocument1->get_Pages()->Add(pdfDocument2->get_Pages());

    // Simpan file keluaran yang digabungkan
    pdfDocument1->Save(_dataDir+outputFileName);
}
```

## Contoh Langsung

[Aspose.PDF Merger](https://products.aspose.app/pdf/merger) adalah aplikasi web gratis yang memungkinkan Anda menyelidiki cara kerja fungsionalitas penggabungan presentasi.

[![Aspose.PDF Merger](merger.png)](https://products.aspose.app/pdf/merger)