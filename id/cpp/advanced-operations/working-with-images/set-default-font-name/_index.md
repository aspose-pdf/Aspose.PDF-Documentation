---
title: Set Default Font Name menggunakan C++
linktitle: Set Default Font Name
type: docs
weight: 90
url: id/cpp/set-default-font-name/
description: Bagian ini menjelaskan cara mengatur nama font default menggunakan pustaka C++.
lastmod: "2021-12-18"
---

**Aspose.PDF untuk C++** API memungkinkan Anda untuk mengatur nama font default ketika font tidak tersedia dalam dokumen. Anda dapat menggunakan properti DefaultFontName dari kelas RenderingOptions untuk mengatur nama font default. Jika DefaultFontName diatur ke `nullptr` maka font **Times New Roman** akan digunakan. Cuplikan kode berikut menunjukkan cara mengatur nama font default ketika menyimpan PDF ke dalam gambar:

```cpp
void WorkingWithImages::ExampleSetDefaultFontName()
{
    String _dataDir("C:\\Samples\\");
    auto document = MakeObject<Document>(_dataDir + u"input.pdf");

    auto imageStream = System::IO::File::OpenWrite(_dataDir + u"SetDefaultFontName.png");

    auto resolution = MakeObject<Aspose::Pdf::Devices::Resolution>(300);
    auto pngDevice = MakeObject<Aspose::Pdf::Devices::PngDevice>(resolution);
    auto ro = MakeObject<RenderingOptions>();
    ro->set_DefaultFontName(u"Arial");
    pngDevice->set_RenderingOptions(ro);
    pngDevice->Process(document->get_Pages()->idx_get(1), imageStream);
}
```