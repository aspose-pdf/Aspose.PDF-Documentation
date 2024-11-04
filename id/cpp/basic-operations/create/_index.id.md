---
title: Membuat Dokumen PDF menggunakan C++
linktitle: Buat
type: docs
weight: 10
url: /cpp/create-document/
description: Tugas paling populer dan dasar dalam bekerja dengan file PDF adalah membuat dokumen dari awal. Gunakan pustaka Aspose.PDF untuk C++.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

**Aspose.PDF untuk C++** API memungkinkan pengembang aplikasi C++ untuk menyematkan fungsionalitas pemrosesan dokumen PDF dalam aplikasi mereka. Ini dapat digunakan untuk membuat dan membaca file PDF tanpa memerlukan perangkat lunak lain yang terpasang pada mesin yang mendasarinya. Aspose.PDF untuk C++ dapat digunakan dalam berbagai jenis aplikasi C++ seperti QT, MFC, dan aplikasi konsol.

## Cara membuat File PDF menggunakan C++

Untuk membuat file PDF menggunakan C++, langkah-langkah berikut dapat digunakan.

1. Instansiasi objek [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document)
1. Tambahkan [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page/) ke objek dokumen
1. Buat objek [TextFragment](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.te_x_fragment/)
1. Tambahkan [TextFragment](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.te_x_fragment/) ke koleksi [Paragraph](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.paragraphs/) pada halaman
1. Simpan dokumen PDF yang dihasilkan

```cpp
void CreatePDF() {
    // String untuk nama path.
    String _dataDir("C:\\Samples\\");

    // String untuk nama file.
    String filename("sample-new.pdf");

    // Inisialisasi objek dokumen
    auto document = MakeObject<Document>();
    // Tambah halaman
    auto page = document->get_Pages()->Add();

    // Tambah teks ke halaman baru
    auto textFragment = MakeObject<TextFragment>(u"Hello World!");
    page->get_Paragraphs()->Add(textFragment);

    // Simpan PDF yang diperbarui
    String outputFileName = _dataDir + filename;

    document->Save(outputFileName);
}
```