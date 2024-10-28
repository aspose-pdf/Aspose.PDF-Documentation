---
title: Tambahkan Halaman di PDF dengan C++
linktitle: Tambahkan Halaman
type: docs
weight: 10
url: /cpp/add-pages/
description: Artikel ini mengajarkan cara menyisipkan (menambahkan) halaman di lokasi yang diinginkan dalam file PDF. Pelajari cara memindahkan, menghapus (menghapus) halaman dari file PDF menggunakan C++.
lastmod: "2021-12-08"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Bagian ini menunjukkan cara menambahkan halaman ke PDF menggunakan pustaka **Aspose.PDF for C++**.

Aspose.PDF for C++ API menyediakan fleksibilitas penuh untuk bekerja dengan halaman dalam dokumen PDF menggunakan C++.

Ini memelihara semua halaman dari dokumen PDF dalam [PageCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection) yang dapat digunakan untuk bekerja dengan halaman PDF. Aspose.PDF for C++ memungkinkan Anda menyisipkan halaman ke dokumen PDF di lokasi mana pun dalam file serta menambahkan halaman ke akhir file PDF.

## Tambahkan atau Sisipkan Halaman dalam File PDF

Aspose.PDF for C++ memungkinkan Anda menyisipkan halaman ke dokumen PDF di lokasi mana pun dalam file serta menambahkan halaman ke akhir file PDF.

### Sisipkan Halaman Kosong dalam File PDF di Lokasi yang Diinginkan

Contoh kode berikut menjelaskan cara menambahkan halaman dalam dokumen PDF.

1. Buat objek kelas [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) dengan file PDF input.
1. Panggil metode [Insert](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection#a1fb1fe44df4d325df5ad41b691501bb2) koleksi [PageCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection) dengan indeks yang ditentukan.
1. Simpan PDF output

Potongan kode berikut menunjukkan cara menyisipkan halaman dalam file PDF.

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;


void InsertEmptyPageAtDesiredLocation() {
    // Buka dokumen
    String _dataDir("C:\\Samples\\");

    // String untuk nama file input
    String inputFileName("InsertEmptyPage.pdf");

    String outputFileName("InsertEmptyPage_out.pdf");

    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // Sisipkan halaman kosong dalam PDF
    document->get_Pages()->Insert(2);

    // Simpan file output
    document->Save(_dataDir + outputFileName);
}
```

Dalam contoh kode berikut, Anda dapat menyisipkan halaman kosong ke lokasi yang diinginkan dengan menyalin parameter dari halaman yang ditentukan:

```cpp
void InsertEmptyPageAtDesiredLocation2() {
    // Buka dokumen
    String _dataDir("C:\\Samples\\");

    // String untuk nama file input
    String inputFileName("InsertEmptyPage.pdf");

    String outputFileName("InsertEmptyPage_out.pdf");

    auto document = MakeObject<Document>(_dataDir + inputFileName);
    auto page = document->get_Pages()->idx_get(1);
    // Sisipkan halaman kosong dalam PDF
    auto pageNew = document->get_Pages()->Insert(2);

    // salin parameter halaman dari halaman 1
    pageNew->set_ArtBox(page->get_ArtBox());
    pageNew->set_BleedBox(page->get_BleedBox());
    pageNew->set_CropBox(page->get_CropBox());
    pageNew->set_MediaBox(page->get_MediaBox());
    pageNew->set_TrimBox(page->get_TrimBox());

    // Simpan file output
    document->Save(_dataDir + outputFileName);
}
```

### Tambahkan Halaman Kosong di Akhir File PDF

Terkadang, Anda ingin memastikan bahwa dokumen berakhir pada halaman kosong. Topik ini menjelaskan cara menyisipkan halaman kosong di akhir dokumen PDF.

Untuk menyisipkan halaman kosong di akhir file PDF:

1. Buat objek kelas [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) dengan file PDF input.
1. Panggil metode [Add](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection#abb0362ffa129a1e2e5650a2f2e7057c1) dari koleksi [PageCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection), tanpa parameter apapun.
1. Simpan PDF output menggunakan metode Save.

Cuplikan kode berikut menunjukkan cara menyisipkan halaman kosong di akhir file PDF.

```cpp
void AddEmptyPageEnd() {
    // Buka dokumen
    String _dataDir("C:\\Samples\\");

    // String untuk nama file input
    String inputFileName("InsertEmptyPageAtEnd.pdf");
    String outputFileName("InsertEmptyPageAtEnd_out.pdf");

    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // Sisipkan halaman kosong di akhir file PDF
    document->get_Pages()->Add();

    // Simpan file output
    document->Save(_dataDir + outputFileName);
}
```