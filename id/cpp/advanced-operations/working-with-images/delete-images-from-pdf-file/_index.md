---
title: Hapus Gambar dari File PDF menggunakan C++
linktitle: Hapus Gambar
type: docs
weight: 20
url: id/cpp/delete-images-from-pdf-file/
description: Bagian ini menjelaskan cara menghapus Gambar dari File PDF menggunakan Aspose.PDF untuk C++.
lastmod: "2021-12-18"
---

Untuk menghapus gambar dari file PDF:

1. Buat objek [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) dan buka file PDF input.
1. Dapatkan Halaman yang memegang gambar dari koleksi [Pages collection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection) objek Document.
1. Gambar-gambar dipegang dalam koleksi Images, yang ditemukan di koleksi Resources halaman.
1. Hapus gambar dengan metode Delete dari koleksi Images.
1. Simpan outputnya menggunakan metode Save dari objek Document.

Cuplikan kode berikut menunjukkan cara menghapus gambar dari file PDF.

```cpp
void WorkingWithImages::DeleteImagesFromPDFFile()
{
    String _dataDir("C:\\Samples\\");

    // Buka dokumen
    auto document = MakeObject<Document>(_dataDir + u"DeleteImages.pdf");

    // Hapus gambar tertentu
    document->get_Pages()->idx_get(1)->get_Resources()->get_Images()->Delete(1);

    // Simpan file PDF yang diperbarui
    document->Save(_dataDir + u"DeleteImages_out.pdf");
}
```