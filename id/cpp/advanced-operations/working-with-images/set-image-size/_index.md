---
title: Mengatur Ukuran Gambar menggunakan C++
linktitle: Mengatur Ukuran Gambar
type: docs
weight: 80
url: id/cpp/set-image-size/
description: Bagian ini menjelaskan cara mengatur ukuran gambar file PDF menggunakan pustaka C++.
lastmod: "2021-12-18"
---

Dimungkinkan untuk mengatur ukuran gambar yang ditambahkan ke file PDF. Untuk mengatur ukuran, Anda dapat menggunakan properti [FixWidth](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.image#a08f2f92b184632385eab19fb96c6d40e) dan [FixHeight](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.image#aed67b52e058b97df6931c214d7092dfa) dari [Aspose.Pdf.Image Class](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.image).

Cuplikan kode berikut menunjukkan cara mengatur ukuran gambar:

```cpp
void WorkingWithImages::ExampleSetImageSize()
{
    String _dataDir("C:\\Samples\\");
    // Memperkenalkan objek Dokumen
    auto document = MakeObject<Document>();
    // tambahkan halaman ke koleksi halaman file PDF
    auto page = document->get_Pages()->Add();
    // Buat instance gambar
    auto img = MakeObject<Image>();
    // Atur Lebar dan Tinggi Gambar dalam Poin
    img->set_FixWidth(100);
    img->set_FixHeight(100);
    // Atur tipe gambar sebagai SVG
    img->set_FileType(Aspose::Pdf::ImageFileType::Unknown);
    // Jalur untuk file sumber
    img->set_File(_dataDir + u"aspose-logo.jpg");
    page->get_Paragraphs()->Add(img);
    // Atur properti halaman
    page->get_PageInfo()->set_Width(800);
    page->get_PageInfo()->set_Height(800);
    // simpan file PDF hasil
    document->Save(_dataDir + u"SetImageSize_out.pdf");
}
```
```