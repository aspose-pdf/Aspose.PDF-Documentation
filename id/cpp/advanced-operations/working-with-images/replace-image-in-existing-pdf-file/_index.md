---
title: Ganti Gambar dalam File PDF yang Ada menggunakan C++
linktitle: Ganti Gambar
type: docs
weight: 70
url: /id/cpp/replace-image-in-existing-pdf-file/
description: Bagian ini menjelaskan tentang mengganti gambar dalam file PDF yang ada menggunakan pustaka ++.
lastmod: "2021-12-18"
---

Metode Replace dari koleksi Images memungkinkan Anda untuk mengganti gambar dalam file PDF yang ada.

Koleksi Images dapat ditemukan dalam koleksi Resources dari sebuah halaman. Untuk mengganti gambar:

1. Buka file PDF menggunakan objek Document.
2. Ganti gambar tertentu, simpan file PDF yang telah diperbarui menggunakan metode Save dari objek Document.

Cuplikan kode berikut menunjukkan cara mengganti gambar dalam file PDF.

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void ReplaceImage() {
    String _dataDir("C:\\Samples\\");

    auto document = MakeObject<Document>(_dataDir + u"input.pdf");
    // Ganti gambar tertentu
    document->get_Pages()->idx_get(1)->get_Resources()->get_Images()->Replace(1, System::IO::File::OpenRead(u"lovely.jpg"));
    // Simpan file PDF yang telah diperbarui
    document->Save(_dataDir + u"output.pdf");
}
```