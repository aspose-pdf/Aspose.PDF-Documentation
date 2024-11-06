---
title: Bekerja dengan Penempatan Gambar menggunakan C++
linktitle: Bekerja dengan Penempatan Gambar
type: docs
weight: 50
url: id/cpp/working-with-image-placement/
description: Bagian ini menjelaskan fitur bekerja dengan penempatan gambar file PDF menggunakan pustaka C++.
lastmod: "2021-12-18"
---

**Aspose.PDF for C++** mendukung [ImagePlacement](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.image_placement), [ImagePlacementAbsorber](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.image_placement_absorber) dan [ImagePlacementCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.image_placement_collection) yang menyediakan kemampuan serupa seperti kelas yang dijelaskan di atas untuk mendapatkan resolusi dan posisi gambar dalam dokumen PDF.

- ImagePlacementAbsorber melakukan pencarian penggunaan gambar sebagai koleksi objek ImagePlacement.
- ImagePlacement menyediakan anggota Resolution dan Rectangle yang mengembalikan nilai penempatan gambar sebenarnya.

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void WorkingWithImagePlacement() {

    String _dataDir("C:\\Samples\\");

    // Memuat dokumen PDF sumber
    auto document = MakeObject<Aspose::Pdf::Document>(_dataDir + u"ImagePlacement.pdf");

    auto abs = MakeObject<ImagePlacementAbsorber>();

    // Memuat konten halaman pertama
    document->get_Pages()->idx_get(1)->Accept(abs);
    for(auto imagePlacement : abs->get_ImagePlacements())
    {
        // Mendapatkan properti gambar
        Console::WriteLine(u"lebar gambar: {0}", imagePlacement->get_Rectangle()->get_Width());
        Console::WriteLine(u"tinggi gambar:{0}", imagePlacement->get_Rectangle()->get_Height());
        Console::WriteLine(u"LLX gambar:{0}", imagePlacement->get_Rectangle()->get_LLX());
        Console::WriteLine(u"LLY gambar:{0}", imagePlacement->get_Rectangle()->get_LLY());
        Console::WriteLine(u"resolusi horizontal gambar:{0}", imagePlacement->get_Resolution()->get_X());
        Console::WriteLine(u"resolusi vertikal gambar:{0}", imagePlacement->get_Resolution()->get_Y());

        // Mengambil gambar dengan dimensi terlihat
        auto imageStream = MakeObject<System::IO::MemoryStream>();

        // Mengambil gambar dari sumber daya
        imagePlacement->get_Image()->Save(imageStream, System::Drawing::Imaging::ImageFormat::get_Png());
        auto resourceImage = System::DynamicCast< System::Drawing::Bitmap>(System::Drawing::Bitmap::FromStream(imageStream));

        // Membuat bitmap dengan dimensi sebenarnya
        auto scaledImage = MakeObject<System::Drawing::Bitmap>(resourceImage, (int)imagePlacement->get_Rectangle()->get_Width(), (int)imagePlacement->get_Rectangle()->get_Height());
        // ...

    }

}
```