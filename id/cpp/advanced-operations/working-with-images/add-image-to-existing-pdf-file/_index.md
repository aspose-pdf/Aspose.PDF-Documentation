---
title: Menambahkan Gambar ke PDF menggunakan C++
linktitle: Menambahkan Gambar
type: docs
weight: 10
url: id/cpp/add-image-to-existing-pdf-file/
description: Bagian ini menjelaskan cara menambahkan gambar ke file PDF yang ada menggunakan pustaka C++.
lastmod: "2021-12-18"
---

## Menambahkan Gambar dalam File PDF yang Ada

Setiap halaman PDF mengandung properti Resources dan Contents. Resources dapat berupa gambar dan formulir misalnya, sementara konten diwakili oleh serangkaian operator PDF. Setiap operator memiliki nama dan argumen. Contoh ini menggunakan operator untuk menambahkan gambar ke file PDF.

Untuk menambahkan gambar ke file PDF yang ada:

- Buat objek [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document/) dan buka dokumen PDF input.
- Dapatkan halaman yang ingin Anda tambahkan gambar.
- Tambahkan gambar ke koleksi Resources halaman.
- Gunakan operator untuk menempatkan gambar pada halaman:
- Gunakan [operator GSave](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.operators.g_save/) untuk menyimpan keadaan grafis saat ini.

- Gunakan [operator ConcatenateMatrix](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.operators.concatenate_matrix#a40ca09b1fa45560d57a1fd042d3fbe96) untuk menentukan di mana gambar akan ditempatkan.
- Gunakan [Do operator](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.operators.do/) untuk menggambar gambar pada halaman.
- Terakhir, gunakan [GRestore operator](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.operators.g_restore/) untuk menyimpan status grafis yang diperbarui.
- Simpan file tersebut.
Cuplikan kode berikut menunjukkan cara menambahkan gambar dalam dokumen PDF.

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void WorkingWithImages::AddImageToExistingPDF()
{
    String _dataDir("C:\\Samples\\");

    // Buka dokumen
    auto document = MakeObject<Document>(_dataDir + u"AddImage.pdf");

    // Atur koordinat
    int lowerLeftX = 50;
    int lowerLeftY = 750;
    int upperRightX = 100;
    int upperRightY = 800;

    // Dapatkan halaman yang ingin Anda tambahkan gambar
    auto page = document->get_Pages()->idx_get(1);

    // Muat gambar ke dalam stream
    auto imageStream = System::IO::File::OpenRead(_dataDir + u"logo.png");

    // Tambahkan gambar ke koleksi Gambar dari sumber daya halaman
    page->get_Resources()->get_Images()->Add(imageStream);

    // Menggunakan operator GSave: operator ini menyimpan status grafis saat ini
    page->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::GSave>());

    // Buat objek Rectangle dan Matrix
    auto rectangle = MakeObject<Rectangle>(lowerLeftX, lowerLeftY, upperRightX, upperRightY);

    auto matrix = MakeObject<Matrix>(
        MakeArray<double>({
            rectangle->get_URX() - rectangle->get_LLX(),
            0,                  0,
            rectangle->get_URY() - rectangle->get_LLY(),
            rectangle->get_LLX(), rectangle->get_LLY() }));

    // Menggunakan operator ConcatenateMatrix (menggabungkan matriks):
    // mendefinisikan bagaimana gambar harus ditempatkan
    page->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::ConcatenateMatrix>(matrix));
    auto ximage = page->get_Resources()->get_Images()->idx_get(page->get_Resources()->get_Images()->get_Count());

    // Menggunakan operator Do: operator ini menggambar gambar
    page->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::Do>(ximage->get_Name()));

    // Menggunakan operator GRestore: operator ini memulihkan status grafis
    page->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::GRestore>());

    // Simpan PDF baru
    document->Save(_dataDir + u"updated_document.pdf");

    // Tutup stream gambar
    imageStream->Close();
}
```

## Tambahkan Referensi Gambar Tunggal beberapa kali dalam Dokumen PDF

Terkadang kita memiliki kebutuhan untuk menggunakan gambar yang sama beberapa kali dalam dokumen PDF. Menambahkan instance baru meningkatkan ukuran dokumen PDF yang dihasilkan. Metode [XImageCollection.Add(XImage)](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.x_image/) memungkinkan untuk menambahkan referensi ke objek PDF yang sama seperti gambar asli yang mengoptimalkan ukuran Dokumen PDF.

```cpp
void WorkingWithImages::AddReferenceOfaSingleImageMultipleTimes() {

    String _dataDir("C:\\Samples\\");
    auto imageRectangle = MakeObject<Rectangle>(0, 0, 30, 15);

    auto document = MakeObject<Document>(_dataDir + u"sample.pdf");

    document->get_Pages()->Add();
    document->get_Pages()->Add();

    auto imageStream = System::IO::File::OpenRead(_dataDir + u"aspose-logo.png");

    SharedPtr<Aspose::Pdf::XImage> image;

    for (auto page : document->get_Pages()) {
        auto annotation = MakeObject<Aspose::Pdf::Annotations::WatermarkAnnotation>(page, page->get_Rect());
        auto form = annotation->get_Appearance()->idx_get(u"N");
        form->set_BBox(page->get_Rect());
        String name;
        if (image != nullptr) {
            name = form->get_Resources()->get_Images()->Add(imageStream);
            image = form->get_Resources()->get_Images()->idx_get(name);
        }
        else {
            form->get_Resources()->get_Images()->AddWithName(image);
        }
        form->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::GSave>());
        form->get_Contents()->Add(
            MakeObject<Aspose::Pdf::Operators::ConcatenateMatrix>(
                MakeObject<Matrix>(imageRectangle->get_Width(), 0, 0, imageRectangle->get_Height(), 0, 0)));

        form->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::Do>(name));
        form->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::GRestore>());
        page->get_Annotations()->Add(annotation, false);
        imageRectangle = MakeObject<Rectangle>(0, 0, imageRectangle->get_Width() * 1.01, imageRectangle->get_Height() * 1.01);
    }
    document->Save(_dataDir + u"AddReferenceOfaSingleImageMultipleTimes_out.pdf");
}
```

## Tempatkan gambar pada halaman dan pertahankan rasio aspek

Jika kita tidak mengetahui dimensi gambar, ada kemungkinan besar mendapatkan gambar yang terdistorsi pada halaman. Contoh berikut menunjukkan salah satu cara untuk menghindarinya.

```cpp
void WorkingWithImages::AddingImageAndPreserveAspectRatioIntoPDF() {

    String _dataDir("C:\\Samples\\");

    auto bitmap = System::Drawing::Image::FromFile(_dataDir + u"3410492.jpg");

    int width;
    int height;

    width = bitmap->get_Width();
    height = bitmap->get_Height();

    auto document = MakeObject<Document>();
    auto page = document->get_Pages()->Add();

    int scaledWidth = 400;
    int scaledHeight = scaledWidth * height / width;

    page->AddImage(_dataDir + u"3410492.jpg", new Rectangle(10, 10, scaledWidth, scaledHeight));
    document->Save(_dataDir + u"sample_image.pdf");
}
```

## Identifikasi apakah gambar di dalam PDF berwarna atau hitam putih

Untuk mengurangi ukuran gambar, Anda perlu mengompresnya. Sebelum Anda dapat menentukan jenis kompresi dari sebuah gambar, Anda perlu mengetahui apakah gambar tersebut berwarna atau hitam putih.

Jenis kompresi yang diterapkan pada gambar tergantung pada ColorSpace dari gambar asli, yaitu jika gambar berwarna (RGB) maka gunakan kompresi JPEG2000, dan jika hitam putih maka gunakan kompresi JBIG2 / JBIG2000.

File PDF dapat berisi elemen Teks, Gambar, Grafik, Lampiran, Anotasi, dll, dan jika file PDF sumber berisi gambar, kita dapat menentukan ruang warna gambar dan menerapkan kompresi yang sesuai untuk gambar untuk mengurangi ukuran file PDF.

Cuplikan kode berikut menunjukkan langkah-langkah untuk Mengidentifikasi apakah gambar di dalam PDF berwarna atau hitam putih.

```cpp
void WorkingWithImages::CheckColors() {

    String _dataDir("C:\\Samples\\");
    auto document = MakeObject<Document>(_dataDir + u"test4.pdf");
    try {
        // iterate through all pages of PDF file
        for (auto page : document->get_Pages()) {
            // create Image Placement Absorber instance
            auto abs = MakeObject<ImagePlacementAbsorber>();
            page->Accept(abs);

            for (auto ia : abs->get_ImagePlacements()) {
                /* ColorType */
                auto colorType = ia->get_Image()->GetColorType();
                switch (colorType) {
                case ColorType::Grayscale:
                    Console::WriteLine(u"Gambar Grayscale");
                    break;
                case ColorType::Rgb:
                    Console::WriteLine(u"Gambar Berwarna");
                    break;
                }
            }
        }
    }
    catch (Exception ex) {
        Console::WriteLine(u"Kesalahan membaca file = {0}", document->get_FileName());
    }
}
```
## Kontrol Kualitas Gambar

Dimungkinkan untuk mengontrol kualitas gambar yang ditambahkan ke file PDF. Gunakan metode [Replace](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.x_image_collection#a698b65051b073f0f4b84b1235889bd72) yang berlebihan dalam kelas [XImageCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.x_image_collection).

Cuplikan kode berikut menunjukkan cara mengonversi semua gambar dokumen menjadi JPEG yang menggunakan kualitas 80% untuk kompresi.

```cpp
void WorkingWithImages::ControlImageQuality() {

    String _dataDir("C:\\Samples\\");

    auto document = MakeObject<Document>(_dataDir + u"sample_with_images.pdf");

    for (auto page : document->get_Pages())
    {
        int idx = 1;
        for (auto image : page->get_Resources()->get_Images())
        {
            auto imageStream = MakeObject<System::IO::MemoryStream>();
            image->Save(imageStream, System::Drawing::Imaging::ImageFormat::get_Jpeg());
            page->get_Resources()->get_Images()->Replace(idx, imageStream, 80);
            idx = idx + 1;
        }
    }

    document->Save(_dataDir + u"sample_with_images_out.pdf");
}
```