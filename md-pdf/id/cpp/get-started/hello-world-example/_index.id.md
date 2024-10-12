```
---
title: Aspose.PDF С++ Contoh
linktitle: Contoh Hello World
type: docs
weight: 40
url: /cpp/hello-world-example/
description: Halaman ini menunjukkan cara menggunakan pemrograman sederhana untuk membuat dokumen PDF yang berisi teks - Hello World.
lastmod: "2021-11-01"
sitemap:
    changefreq: "monthly"
    priority: 0.6
---

Contoh "Hello World" secara tradisional digunakan untuk memperkenalkan fitur bahasa pemrograman atau perangkat lunak dengan kasus penggunaan sederhana.

Aspose.PDF untuk C++ adalah API PDF kaya fitur yang memungkinkan pengembang untuk menyematkan kemampuan pembuatan, manipulasi & konversi dokumen PDF dalam aplikasi C++ mereka. Ini mendukung bekerja dengan banyak format file populer termasuk PDF, XFA, TXT, HTML, PCL, XML, XPS, EPUB, TEX dan format file gambar. Dalam artikel ini, kami membuat dokumen PDF yang berisi teks "Hello World!". Setelah menginstal Aspose.PDF untuk C++ di lingkungan Anda, Anda dapat menjalankan contoh kode di bawah ini untuk melihat cara kerja API Aspose.PDF.

Cuplikan kode di bawah ini mengikuti langkah-langkah ini:

1.
``` Buat [Kelas String](https://reference.aspose.com/pdf/cpp/class/system.string) untuk nama jalur dan nama file.
1. Instansiasi objek [Dokumen](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document). Dalam langkah ini, kita akan membuat dokumen PDF kosong dengan beberapa metadata tetapi tanpa halaman.
1. Tambahkan [Halaman](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page) ke objek dokumen. Jadi, sekarang dokumen kita akan memiliki satu halaman.
1. [Simpan](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document/#ac082fe8e67b25685fc51d33e804269fa) dokumen PDF yang dihasilkan

Cuplikan kode berikut adalah program Hello World untuk menunjukkan cara kerja Aspose.PDF untuk C++ API.

```cpp
void ExampleSimple()
{
    // Buffer untuk menampung jalur gabungan.
    String outputFileName;

    // String untuk nama jalur.
    String _dataDir("C:\\Samples\\");

    // String untuk nama file.
    String filename("HelloWorld_out.pdf");

    auto document = MakeObject<Document>();
    auto page = document->get_Pages()->Add();

    // Tambahkan teks ke halaman baru
    auto text = MakeObject<TextFragment>(u"Hello world!");

    auto paragraphs = page->get_Paragraphs();
    paragraphs->Add(text);

    // Simpan PDF yang diperbarui
    outputFileName = _dataDir + filename;

    document->Save(outputFileName);
}
```