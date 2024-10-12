```
---
title: Ekstrak Gambar dari PDF 
linktitle: Ekstrak Gambar dari PDF
type: docs
weight: 20
url: /cpp/extract-images-from-the-pdf-file/
description: Cara mengekstrak bagian dari gambar dari PDF menggunakan Aspose.PDF untuk C++.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Juga, tugas yang banyak diminta ketika bekerja dengan dokumen PDF adalah mengekstrak gambar dari file PDF. Misalnya, Anda menerima email PDF dengan banyak gambar bagus yang ingin Anda ekstrak sebagai file terpisah.

Perpustakaan Aspose.PDF memungkinkan Anda mengekstrak gambar dari PDF dengan cuplikan kode berikut:

```cpp
void ExtractImage()
{
    std::clog << __func__ << ": Start" << std::endl;
    // String untuk nama jalur
    String _dataDir("C:\\Samples\\Parsing\\");

    // String untuk nama file
    String infilename("sample-image.pdf");
    String outfilename("extracted_image.jpeg");

    // Buka dokumen
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Ekstrak gambar tertentu
    auto xImage = document->get_Pages()->idx_get(1)->get_Resources()->get_Images()->idx_get(1);

    auto outputImage = System::IO::File::OpenWrite(_dataDir + outfilename);

    // Simpan gambar keluaran
    xImage->Save(outputImage, System::Drawing::Imaging::ImageFormat::get_Jpeg());
    outputImage->Close();

    std::clog << __func__ << ": Finish" << std::endl;
}
```
```