---
title: Tambahkan Stempel Gambar di PDF secara Programatik
linktitle: Stempel Gambar di File PDF
type: docs
weight: 10
url: /id/cpp/image-stamps-in-pdf-page/
description: Tambahkan Stempel Gambar dalam dokumen PDF Anda menggunakan kelas ImageStamp dengan pustaka Aspose.PDF untuk C++.
lastmod: "2021-12-08"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Tambahkan Stempel Gambar di File PDF

Anda dapat menggunakan kelas ImageStamp untuk menambahkan stempel gambar ke file PDF. Kelas ImageStamp menyediakan properti yang diperlukan untuk membuat stempel berbasis gambar, seperti tinggi, lebar, opasitas, dan sebagainya.

Untuk menambahkan stempel gambar:

1. Buat objek [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) dan objek ImageStamp menggunakan properti yang diperlukan.
2. Panggil metode [AddStamp](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page#a3b998038dedf5266b4d60586b1b53d02) dari kelas [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page) untuk menambahkan stempel ke PDF.

Cuplikan kode berikut menunjukkan cara menambahkan stempel gambar dalam file PDF.

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void AddImageStampToPDFFile()
{    
    String _dataDir("C:\\Samples\\");

    // String untuk nama file input
    String inputFileName("AddImageStamp.pdf");

    String outputFileName("AddImageStamp_out.pdf");

    // Buka dokumen
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // Buat cap gambar
    auto imageStamp = MakeObject<ImageStamp>(_dataDir + u"aspose-logo.jpg");
    imageStamp->set_Background(true);
    imageStamp->set_XIndent(100);
    imageStamp->set_YIndent(100);
    imageStamp->set_Height(48);
    imageStamp->set_Width(225);
    imageStamp->set_Rotate(Rotation::on270);
    imageStamp->set_Opacity(0.5);
   
    // Tambahkan cap ke halaman tertentu    
    document->get_Pages()->idx_get(1)->AddStamp(imageStamp);

    // Simpan dokumen keluaran
    document->Save(_dataDir + outputFileName);
}
```

## Kontrol Kualitas Gambar saat Menambahkan Cap

Saat menambahkan gambar sebagai objek cap, Anda dapat mengontrol kualitas gambar. Properti Quality dari kelas [ImageStamp](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.image_stamp) digunakan untuk tujuan ini. Ini menunjukkan kualitas gambar dalam persen (nilai yang valid adalah 0..100).

```cpp
void ControlImageQualityWhenAddingStamp() {
    
    String _dataDir("C:\\Samples\\");

    // String untuk nama file input
    String inputFileName("AddImageStamp.pdf");
    String outputFileName("ControlImageQuality_out.pdf");

    // Buka dokumen
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // Buat cap gambar
    auto imageStamp = MakeObject<ImageStamp>(_dataDir + u"aspose-logo.jpg");

    imageStamp->set_Quality(10);
    document->get_Pages()->idx_get(1)->AddStamp(imageStamp);    
    document->Save(_dataDir + u"ControlImageQuality_out.pdf");
}
```

## Cap Gambar sebagai Latar Belakang dalam Kotak Mengambang

API Aspose.PDF memungkinkan Anda menambahkan cap gambar sebagai latar belakang dalam kotak mengambang. Properti BackgroundImage dari kelas FloatingBox dapat digunakan untuk mengatur stempel gambar latar belakang untuk kotak mengambang seperti yang ditunjukkan dalam contoh kode berikut.

```cpp
void ImageStampAsBackgroundInFloatingBox() {
    
    String _dataDir("C:\\Samples\\");

    // String untuk nama file input
    String inputFileName("AddImageStamp.pdf");
    String outputFileName("AddImageStampAsBackgroundInFloatingBox_out.pdf");

    // Membuat objek Dokumen
    auto document = MakeObject<Document>();

    // Menambahkan halaman ke dokumen PDF
    auto page = document->get_Pages()->Add();

    // Membuat objek FloatingBox
    auto aBox = MakeObject<FloatingBox>(200, 100);

    // Mengatur posisi kiri untuk FloatingBox
    aBox->set_Left(40);
    // Mengatur posisi atas untuk FloatingBox
    aBox->set_Top(80);
    // Mengatur penyelarasan horizontal untuk FloatingBox
    aBox->set_HorizontalAlignment(HorizontalAlignment::Center);
    
    // Menambahkan fragmen teks ke koleksi paragraf FloatingBox    
    aBox->get_Paragraphs()->Add(MakeObject<TextFragment>(u"main text"));

    // Mengatur batas untuk FloatingBox
    aBox->set_Border(MakeObject<BorderInfo>(BorderSide::All, Color::get_Red()));

    // Menambahkan gambar latar belakang
    auto image = MakeObject<Image>();
    image->set_File(_dataDir + u"aspose-logo.png");
    aBox->set_BackgroundImage(image);

    // Mengatur warna latar belakang untuk FloatingBox
    aBox->set_BackgroundColor(Color::get_Yellow());

    // Menambahkan FloatingBox ke koleksi paragraf dari objek halaman
    page->get_Paragraphs()->Add(aBox);
    // Menyimpan dokumen PDF
    document->Save(_dataDir + outputFileName);
}
```