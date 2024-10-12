---
title: Cari dan Dapatkan Gambar dari Dokumen PDF menggunakan C++
linktitle: Cari dan Dapatkan Gambar
type: docs
weight: 60
url: /cpp/search-and-get-images-from-pdf-document/
description: Bagian ini menjelaskan cara mencari dan mendapatkan gambar dari dokumen PDF dengan pustaka Aspose.PDF.
lastmod: "2021-12-18"
---

ImagePlacementAbsorber memungkinkan Anda untuk mencari di antara gambar-gambar di semua halaman dalam dokumen PDF.

Untuk mencari gambar dalam seluruh dokumen:

1. Panggil metode [Accept](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection#ae71a2782e747936e3c14b7ded5c6dc3f) dari koleksi [Pages](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection). Metode Accept mengambil objek [ImagePlacementAbsorber](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.image_placement_absorber/) sebagai parameter. Ini mengembalikan koleksi objek ImagePlacement.
1. Loop melalui objek ImagePlacements dan dapatkan properti mereka (Gambar, dimensi, resolusi, dan sebagainya).

Cuplikan kode berikut menunjukkan cara mencari semua gambar dalam dokumen.

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void SearchAndGetImagesFromPDFDocument() {

    String _dataDir("C:\\Samples\\");

    // Buka dokumen
    auto document = MakeObject<Document>(_dataDir + u"SearchAndGetImages.pdf");

    // Buat objek ImagePlacementAbsorber untuk melakukan pencarian penempatan gambar
    auto abs = MakeObject<ImagePlacementAbsorber>();

    // Terima absorber untuk semua halaman
    document->get_Pages()->Accept(abs);

    // Loop melalui semua ImagePlacements, dapatkan gambar dan Properti ImagePlacement
    for(auto imagePlacement : abs->get_ImagePlacements())
    {
        // Dapatkan gambar menggunakan objek ImagePlacement
        auto image = imagePlacement->get_Image();

        // Tampilkan properti penempatan gambar untuk semua penempatan
        Console::WriteLine(u"lebar gambar: {0}", imagePlacement->get_Rectangle()->get_Width());
        Console::WriteLine(u"tinggi gambar:{0}", imagePlacement->get_Rectangle()->get_Height());
        Console::WriteLine(u"LLX gambar:{0}", imagePlacement->get_Rectangle()->get_LLX());
        Console::WriteLine(u"LLY gambar:{0}", imagePlacement->get_Rectangle()->get_LLY());
        Console::WriteLine(u"resolusi horizontal gambar:{0}", imagePlacement->get_Resolution()->get_X());
        Console::WriteLine(u"resolusi vertikal gambar:{0}", imagePlacement->get_Resolution()->get_Y());
    }
}
```