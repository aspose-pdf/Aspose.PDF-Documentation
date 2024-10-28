```
title: Pisahkan PDF secara programatik
linktitle: Pisahkan file PDF
type: docs
weight: 60
url: /cpp/split-pdf-document/
description: Topik ini menunjukkan cara memisahkan halaman PDF menjadi file PDF individu dengan C++.
lastmod: "2022-09-01"
sitemap:
    changefreq: "monthy"
    priority: 0.7
---

## Contoh Langsung

[Aspose.PDF Splitter](https://products.aspose.app/pdf/splitter) adalah aplikasi web gratis online yang memungkinkan Anda untuk menyelidiki bagaimana fungsionalitas pemisahan presentasi bekerja.

[![Aspose Split PDF](splitter.png)](https://products.aspose.app/pdf/splitter)

Topik ini menunjukkan cara memisahkan halaman PDF menjadi file PDF individu dalam aplikasi C++ Anda. Untuk memisahkan halaman PDF menjadi file PDF satu halaman menggunakan C++, langkah-langkah berikut dapat diikuti:

1. Loop melalui halaman dokumen PDF melalui koleksi [PageCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection) dari objek [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document)
1.
``` Untuk setiap iterasi, buat objek Dokumen baru dan salin objek [Halaman](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page) individual ke dalam dokumen kosong
1. Simpan PDF baru menggunakan metode Simpan

Cuplikan kode C++ berikut menunjukkan cara membagi halaman PDF menjadi file PDF individual.

```cpp
void SplittingDocuments() {
    // String untuk nama jalur
    String _dataDir("C:\\Samples\\");

    // String untuk nama file input
    String documentFileName("sample.pdf");
    
    // Buka dokumen
    auto document = MakeObject<Document>(_dataDir + documentFileName);

    int pageCount = 1;

    // Loop melalui semua halaman
    for(auto page : document->get_Pages())
    {
        auto newDocument = MakeObject<Document>(_dataDir + documentFileName);
        newDocument->get_Pages()->CopyPage(page);
        newDocument->Save(_dataDir + u"page_" + pageCount + u"_out.pdf");
        pageCount++;
    }
}
```