---
title: Ekstrak Gambar dari File PDF menggunakan C++
linktitle: Ekstrak Gambar
type: docs
weight: 30
url: id/cpp/extract-images-from-pdf-file/
description: Bagian ini menunjukkan cara mengekstrak gambar dari file PDF menggunakan pustaka C++.
lastmod: "2021-12-18"
---

Anda dapat menggunakan Aspose.PDF for C++ untuk mengekstrak semua gambar dari dokumen PDF Anda ke dalam file terpisah yang dapat digunakan kembali di program lain.

Gambar disimpan dalam koleksi Gambar dari koleksi Sumber Daya di setiap halaman. Untuk mengekstrak halaman tertentu, kemudian dapatkan gambar dari koleksi Gambar menggunakan indeks tertentu dari gambar tersebut.

Indeks gambar mengembalikan objek [XImage](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.x_image). Objek ini menyediakan metode Simpan yang dapat digunakan untuk menyimpan gambar yang diekstrak.

Cuplikan kode berikut menunjukkan cara mengekstrak gambar dari file PDF.

```cpp
void WorkingWithImages::ExtractImages()
{
    String _dataDir("C:\\Samples\\");

    // Buka dokumen
    auto document = MakeObject<Document>(_dataDir + u"ExtractImages.pdf");

    // Ekstrak gambar tertentu
    auto xImage = document->get_Pages()->idx_get(1)->get_Resources()->get_Images()->idx_get(1);

    auto outputImage = System::IO::File::OpenWrite(_dataDir + u"output.jpg");

    // Simpan gambar output
    xImage->Save(outputImage, System::Drawing::Imaging::ImageFormat::get_Jpeg());
    outputImage->Close();

    // Simpan file PDF yang diperbarui
    document->Save(_dataDir + u"ExtractImages_out.pdf");
}
```