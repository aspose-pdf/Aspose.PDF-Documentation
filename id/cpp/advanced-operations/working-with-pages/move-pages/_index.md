---
title: Memindahkan Halaman PDF secara Pemrograman C++
linktitle: Memindahkan Halaman PDF
type: docs
weight: 20
url: /id/cpp/move-pages/
description: Cobalah memindahkan halaman ke lokasi yang diinginkan atau di akhir file PDF menggunakan Aspose.PDF untuk C++.
lastmod: "2021-12-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Memindahkan Halaman dari satu Dokumen PDF ke Dokumen Lain

Memindahkan halaman PDF dalam dokumen adalah tugas yang sangat menarik dan populer. Topik ini menjelaskan cara memindahkan halaman dari satu dokumen PDF ke akhir dokumen lain menggunakan C++. Untuk memindahkan halaman kita harus:

1. Membuat objek kelas [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) dengan file PDF sumber.
1. Mendapatkan Halaman dari koleksi [PageCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection).
1. [Menambahkan](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection#abb0362ffa129a1e2e5650a2f2e7057c1) halaman ke dokumen tujuan.
1. Menyimpan output PDF menggunakan metode Save.
1. [Delete](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection#afaa57836d1b206e396f2cb7dd91b5d15) halaman dalam dokumen sumber.
1. Simpan PDF sumber menggunakan metode Save.

Cuplikan kode berikut menunjukkan cara memindahkan satu halaman.

```cpp
void MovePage()
{
    // Buka dokumen
    String _dataDir("C:\\Samples\\");
    String srcFileName("<masukkan nama file>");
    String dstFileName("<masukkan nama file>");

    auto srcDocument = MakeObject<Document>(_dataDir + srcFileName);
    auto dstDocument = MakeObject<Document>();

    auto page = srcDocument->get_Pages()->idx_get(2);
    dstDocument->get_Pages()->Add(page);
    // Simpan file keluaran
    dstDocument->Save(srcFileName);
    srcDocument->get_Pages()->Delete(2);
    srcDocument->Save(dstFileName);
}
```

## Memindahkan banyak Halaman dari satu Dokumen PDF ke Dokumen Lain

1. Buat objek kelas [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) dengan file PDF sumber.
1. Tentukan array dengan nomor halaman yang akan dipindahkan.
1. Jalankan loop melalui array:
1. Dapatkan Halaman dari koleksi [PageCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection).
1. [Tambahkan](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection#abb0362ffa129a1e2e5650a2f2e7057c1) halaman ke dokumen tujuan.
1. Simpan output PDF menggunakan metode Save.
1. [Hapus](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection#afaa57836d1b206e396f2cb7dd91b5d15) halaman di dokumen sumber.
1. Simpan PDF sumber menggunakan metode Save.

Cuplikan kode berikut menunjukkan cara menyisipkan halaman kosong di akhir file PDF.

```cpp
void MoveBunchPages()
{
    // Buka dokumen
    String _dataDir("C:\\Samples\\");
    String srcFileName("<enter file name>");
    String dstFileName("<enter file name>");

    auto srcDocument = MakeObject<Document>(_dataDir + srcFileName);
    auto dstDocument = MakeObject<Document>();


    auto pages = MakeArray<int>({ 1,3 });

    for (auto pageIndex : pages)
    {
        auto page = srcDocument->get_Pages()->idx_get(pageIndex);
        dstDocument->get_Pages()->Add(page);
    }
    // Simpan file output
    dstDocument->Save(srcFileName);
    srcDocument->get_Pages()->Delete();
    srcDocument->Save(dstFileName);
}
```
## Memindahkan Halaman ke Lokasi Baru dalam Dokumen PDF Saat Ini

1. Buat objek kelas [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) dengan file PDF sumber.
1. Dapatkan Halaman dari koleksi [PageCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection).
1. [Tambahkan](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection#abb0362ffa129a1e2e5650a2f2e7057c1) halaman ke lokasi baru (misalnya ke akhir).
1. [Hapus](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection#afaa57836d1b206e396f2cb7dd91b5d15) halaman di lokasi sebelumnya.
1. Simpan output PDF menggunakan metode Save.

```cpp
void MovePagesInOnePDF()
{
    // Buka dokumen
    String _dataDir("C:\\Samples\\");
    String srcFileName("<enter file name>");
    String dstFileName("<enter file name>");

    auto srcDocument = MakeObject<Document>(_dataDir + srcFileName);
    auto dstDocument = MakeObject<Document>();

    auto page = srcDocument->get_Pages()->idx_get(2);
    srcDocument->get_Pages()->Add(page);
    srcDocument->get_Pages()->Delete(2);

    // Simpan file output
    srcDocument->Save(dstFileName);
}
```