---
title: Convert PDF ke Format Gambar
linktitle: Convert PDF to Images
type: docs
weight: 70
url: /cpp/convert-pdf-to-images-format/
lastmod: "2021-11-19"
description: Topik ini menunjukkan bagaimana Aspose.PDF memungkinkan untuk mengonversi PDF ke berbagai format gambar. Konversi halaman PDF ke gambar PNG, JPEG, BMP dengan beberapa baris kode.
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

**Aspose.PDF for C++** menggunakan beberapa pendekatan untuk mengonversi PDF ke gambar. Secara umum, kami menggunakan dua pendekatan: konversi menggunakan pendekatan Device dan konversi menggunakan SaveOption. Bagian ini akan menunjukkan kepada Anda bagaimana mengonversi dokumen PDF ke format gambar seperti format BMP, JPEG, PNG, TIFF, dan SVG menggunakan salah satu dari pendekatan tersebut.

Ada beberapa kelas dalam perpustakaan yang memungkinkan Anda menggunakan perangkat virtual untuk mengubah gambar. DocumentDevice diorientasikan untuk konversi seluruh dokumen, tetapi ImageDevice - untuk halaman tertentu.

## Mengonversi PDF menggunakan kelas DocumentDevice

**Aspose.PDF for C++** memungkinkan untuk mengonversi Halaman PDF ke gambar TIFF.

The [TiffDevice](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.devices.tiff_device/) (berdasarkan DocumentDevice) kelas memungkinkan Anda mengonversi halaman PDF ke gambar TIFF. Kelas ini menyediakan metode bernama [Process](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.devices.tiff_device#a0790daa96125c5638a645647e9678f0c) yang memungkinkan Anda mengonversi semua halaman dalam file PDF ke satu gambar TIFF.

{{% alert color="success" %}}
**Coba konversi PDF ke TIFF online**

Aspose.PDF untuk C++ menyajikan aplikasi online gratis ["PDF to TIFF"](https://products.aspose.app/pdf/conversion/pdf-to-tiff), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitasnya.

[![Aspose.PDF konversi PDF ke TIFF dengan Aplikasi Gratis](pdf_to_tiff.png)](https://products.aspose.app/pdf/conversion/pdf-to-tiff)
{{% /alert %}}

### Konversi Halaman PDF ke Satu Gambar TIFF

Aspose.PDF untuk С++ menjelaskan cara mengonversi semua halaman dalam file PDF ke satu gambar TIFF:

1. Buka [Dokumen](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document/) dengan MakeObject.
1. Buat objek Resolution.
1. Buat objek [TIffSettings](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.devices.tiff_settings/).
1. Buat [perangkat Tiff](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.devices.tiff_device/) dengan atribut yang ditentukan.
1. Konversi halaman tertentu dan simpan gambar ke stream.

Cuplikan kode berikut menunjukkan cara mengonversi semua halaman PDF menjadi satu gambar TIFF.

```cpp
void Convert_PDF_To_Images::ConvertPDFtoTIFF()
{
    std::clog << __func__ << ": Start" << std::endl;
    // String untuk nama path
    String _dataDir("C:\\Samples\\Conversion\\");

    // String untuk nama file
    String infilename("PageToTiff.pdf");
    String outfilename("PagesToTIFF_out.tif");

    // Buka dokumen
    auto document = MakeObject<Document>(_dataDir + infilename);

    auto imageStream = System::IO::File::OpenWrite(_dataDir + outfilename);

    // Buat objek Resolution
    auto resolution = MakeObject<Aspose::Pdf::Devices::Resolution>(300);

    // Buat objek TiffSettings
    auto tiffSettings = MakeObject<Aspose::Pdf::Devices::TiffSettings>();
    tiffSettings->set_Compression(Aspose::Pdf::Devices::CompressionType::None);
    tiffSettings->set_Depth(Aspose::Pdf::Devices::ColorDepth::Default);
    tiffSettings->set_Shape(Aspose::Pdf::Devices::ShapeType::Landscape);
    tiffSettings->set_SkipBlankPages(false);

    // Buat perangkat TIFF
    auto tiffDevice = MakeObject<Aspose::Pdf::Devices::TiffDevice>(resolution, tiffSettings);

    // Konversi halaman dan simpan gambar ke stream
    tiffDevice->Process(document, 1, 2, imageStream);
    std::clog << __func__ << ": Finish" << std::endl;
}
```
### Mengonversi Satu Halaman ke Gambar TIFF

Aspose.PDF untuk C++ memungkinkan Anda mengonversi halaman tertentu dalam file PDF ke gambar TIFF, gunakan versi berlebihan dari metode Process(..) yang mengambil nomor halaman sebagai argumen untuk konversi. Cuplikan kode berikut menunjukkan cara mengonversi halaman pertama PDF ke format TIFF.

```cpp
void Convert_PDF_To_Images::ConvertPDFtoTiffSinglePage()
{
    std::clog << __func__ << ": Start" << std::endl;
    // String untuk nama path
    String _dataDir("C:\\Samples\\Conversion\\");

    // String untuk nama file
    String infilename("PageToTiff.pdf");
    String outfilename("PageToTiff_out.tif");

    // Buka dokumen
    auto document = MakeObject<Document>(_dataDir + infilename);

    auto imageStream = System::IO::File::OpenWrite(_dataDir + outfilename);

    // Buat objek Resolution
    auto resolution = MakeObject<Aspose::Pdf::Devices::Resolution>(300);

    // Buat perangkat TIFF
    auto tiffDevice = MakeObject<Aspose::Pdf::Devices::TiffDevice>(resolution);

    // Konversi halaman tertentu dan simpan gambar ke stream
    tiffDevice->Process(document, 1, 1, imageStream);
    std::clog << __func__ << ": Finish" << std::endl;
}
```

### Gunakan algoritma Bradley selama konversi

Aspose.PDF untuk C++ telah mendukung fitur untuk mengonversi PDF ke TIF menggunakan kompresi LZW dan kemudian dengan penggunaan AForge, Binarisasi dapat diterapkan. Namun, salah satu pelanggan meminta bahwa untuk beberapa gambar, mereka perlu mendapatkan Threshold menggunakan Otsu, jadi mereka juga ingin menggunakan Bradley.

```cpp
void Convert_PDF_To_Images::ConvertPDFtoTiffBradleyBinarization()
{
    // String untuk nama path
    String _dataDir("C:\\Samples\\Conversion\\");

    // Buka dokumen
    auto pdfDocument = MakeObject<Document>(_dataDir + u"PageToTIFF.pdf");

    String outputImageFile = _dataDir + u"resultant_out.tif";
    String outputBinImageFile = _dataDir + u"37116-bin_out.tif";

    // Buat objek Resolution 
    auto resolution = MakeObject<Aspose::Pdf::Devices::Resolution>(300);

    // Buat objek TiffSettings
    auto tiffSettings = MakeObject<Aspose::Pdf::Devices::TiffSettings>();
    tiffSettings->set_Compression(Aspose::Pdf::Devices::CompressionType::LZW);
    tiffSettings->set_Depth(Aspose::Pdf::Devices::ColorDepth::Format1bpp);

    // Buat perangkat TIFF
    auto tiffDevice = MakeObject<Aspose::Pdf::Devices::TiffDevice>(resolution, tiffSettings);
    auto imageStream = System::IO::File::OpenWrite(_dataDir + outputImageFile);

    // Konversi halaman tertentu dan simpan gambar ke stream
    tiffDevice->Process(pdfDocument, 1, 2, imageStream);

    imageStream->Close();

    auto inStream = System::IO::File::OpenRead(outputImageFile);
    auto outStream = System::IO::File::OpenWrite(outputBinImageFile);

    tiffDevice->BinarizeBradley(inStream, outStream, 0.1);
}
```

## Convert PDF using ImageDevice class

`ImageDevice` adalah leluhur untuk `BmpDevice`, `JpegDevice`, `GifDevice`, `PngDevice` dan `EmfDevice`.

- Kelas [BmpDevice](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.devices.bmp_device/) memungkinkan Anda untuk mengkonversi halaman PDF ke gambar <abbr title="Bitmap Image File">BMP</abbr>.
- Kelas [EmfDevice](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.devices.emf_device/) memungkinkan Anda untuk mengkonversi halaman PDF ke gambar <abbr title="Enhanced Meta File">EMF</abbr>.
- Kelas [JpegDevice](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.devices.jpeg_device/) memungkinkan Anda untuk mengkonversi halaman PDF ke gambar JPEG.
- Kelas [PngDevice](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.devices.png_device/) memungkinkan Anda untuk mengkonversi halaman PDF ke gambar <abbr title="Portable Network Graphics">PNG</abbr>.

- Kelas [GifDevice](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.devices.gif_device/) memungkinkan Anda untuk mengkonversi halaman PDF ke gambar <abbr title="Graphics Interchange Format">GIF</abbr>.

Mari kita lihat bagaimana mengubah halaman PDF menjadi gambar.

Kelas [BmpDevice](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.devices.bmp_device) menyediakan metode bernama [Process](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.devices.bmp_device#a22cefdb47b7c762320fa7973aa4f1f93) yang memungkinkan Anda untuk mengubah halaman tertentu dari file PDF menjadi format gambar BMP. Kelas lainnya memiliki metode yang sama. Jadi, jika kita perlu mengubah halaman PDF menjadi gambar, kita hanya perlu membuat instans dari kelas yang diperlukan.

Cuplikan kode berikut menunjukkan kemungkinan ini:

```cpp
void Convert_PDF_To_Images::ConvertPDFusingImageDevice()
{
    std::clog << __func__ << ": Start" << std::endl;

    // String untuk nama path
    String _dataDir("C:\\Samples\\Conversion\\");

    // Buat objek Resolution            
    auto resolution = MakeObject<Aspose::Pdf::Devices::Resolution>(300); //300 dpi

    System::SmartPtr<Aspose::Pdf::Devices::ImageDevice>
    bmpDevice = MakeObject<Aspose::Pdf::Devices::BmpDevice>(resolution);
    System::SmartPtr<Aspose::Pdf::Devices::ImageDevice>
    jpegDevice = MakeObject<Aspose::Pdf::Devices::JpegDevice>(resolution);
    System::SmartPtr<Aspose::Pdf::Devices::ImageDevice>
    gifDevice = MakeObject<Aspose::Pdf::Devices::GifDevice>(resolution);
    System::SmartPtr<Aspose::Pdf::Devices::ImageDevice>
    pngDevice = MakeObject<Aspose::Pdf::Devices::PngDevice>(resolution);
    System::SmartPtr<Aspose::Pdf::Devices::ImageDevice>
    emfDevice = MakeObject<Aspose::Pdf::Devices::EmfDevice>(resolution);

    auto document = MakeObject<Document>(_dataDir + u"ConvertAllPagesToBmp.pdf");

    ConvertPDFtoImage(bmpDevice, u"bmp", document);
    ConvertPDFtoImage(jpegDevice, u"jpeg", document);
    ConvertPDFtoImage(gifDevice, u"gif", document);
    ConvertPDFtoImage(pngDevice, u"png", document);
    ConvertPDFtoImage(emfDevice, u"emf", document);

    std::clog << __func__ << ": Finish" << std::endl;

}

void Convert_PDF_To_Images::ConvertPDFtoImage(
 System::SmartPtr<Aspose::Pdf::Devices::ImageDevice> imageDevice,
 String ext, System::SmartPtr<Document> document)
{
    // String untuk nama path
    String _dataDir("C:\\Samples\\Conversion\\");

    for (int pageCount = 1; pageCount <= document->get_Pages()->get_Count(); pageCount++)
    {
    String outfilename = String::Format(u"{0}PageToBmp{1}_out.{2}",
    _dataDir, pageCount, ext);

    auto imageStream = System::IO::File::OpenWrite(outfilename);

    // Buat objek Resolution
    auto resolution = MakeObject<Aspose::Pdf::Devices::Resolution>(300);

    // Ubah halaman tertentu dan simpan gambar ke stream
    imageDevice->Process(document->get_Pages()->idx_get(pageCount), imageStream);

    // Tutup stream
    imageStream->Close();
    }
}
```

{{% alert color="success" %}}
**Coba konversi PDF ke PNG secara online**

Sebagai contoh bagaimana aplikasi gratis kami bekerja, silakan periksa fitur berikut.

Aspose.PDF untuk C++ menghadirkan aplikasi gratis online ["PDF ke PNG"](https://products.aspose.app/pdf/conversion/pdf-to-png), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitasnya.

[![Cara mengonversi PDF ke PNG menggunakan Aplikasi Gratis](pdf_to_png.png)](https://products.aspose.app/pdf/conversion/pdf-to-png)
{{% /alert %}}

## Konversi PDF menggunakan kelas SaveOptions

Bagian artikel ini menunjukkan kepada Anda cara mengonversi PDF ke <abbr title="Scalable Vector Graphics">SVG</abbr> menggunakan C++ dan kelas SaveOptions.

{{% alert color="success" %}}
**Coba konversi PDF ke SVG secara online**

Aspose.PDF untuk C++ menghadirkan aplikasi gratis online ["PDF ke SVG"](https://products.aspose.app/pdf/conversion/pdf-to-svg), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitasnya.

[![Aspose.PDF Konversi PDF ke SVG dengan Aplikasi Gratis](pdf_to_svg.png)](https://products.aspose.app/pdf/conversion/pdf-to-svg)
{{% /alert %}}

Untuk mengonversi PDF ke SVG, Aspose.PDF untuk CPP menawarkan metode [Save](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#ac082fe8e67b25685fc51d33e804269fa) dari kelas [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document). Anda perlu memberikan jalur keluaran dan enum SaveFormat:: svg ke metode Save untuk mengonversi PDF ke SVG. Kode berikut menunjukkan cara mengonversi PDF ke SVG:

Artikel ini mengajarkan Anda cara mengonversi PDF ke <abbr title="Scalable Vector Graphics">SVG</abbr> menggunakan C++.

**Scalable Vector Graphics (SVG)** adalah keluarga spesifikasi dari format file berbasis XML untuk grafik vektor dua dimensi, baik statis maupun dinamis (interaktif atau animasi). Spesifikasi SVG adalah standar terbuka yang telah dikembangkan oleh World Wide Web Consortium (W3C) sejak tahun 1999.

Gambar SVG dan perilakunya didefinisikan dalam file teks XML. Ini berarti bahwa mereka dapat dicari, diindeks, diskrip, dan jika diperlukan, dikompresi. Sebagai file XML, gambar SVG dapat dibuat dan diedit dengan editor teks apa pun, tetapi seringkali lebih nyaman untuk membuatnya dengan program menggambar seperti Inkscape.

Aspose.PDF untuk C++ mendukung fitur untuk mengonversi gambar SVG ke format PDF dan juga menawarkan kemampuan untuk mengonversi file PDF ke format SVG. Untuk memenuhi persyaratan ini, kelas `SvgSaveOptions` telah diperkenalkan ke dalam namespace Aspose.PDF. Instansiasi objek dari SvgSaveOptions dan berikan sebagai argumen kedua ke metode [Save](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#ac082fe8e67b25685fc51d33e804269fa).

Cuplikan kode berikut menunjukkan langkah-langkah untuk mengonversi file PDF ke format SVG dengan C++.

```cpp
void Convert_PDF_To_Images::ConvertPDFtoSvgSinglePage()
{
    std::clog << __func__ << ": Start" << std::endl;
    // String untuk nama jalur
    String _dataDir("C:\\Samples\\Conversion\\");

    // String untuk nama file
    String infilename("PageToSvg.pdf");
    String outfilename("PageToSvg_out.svg");

    // Buka dokumen
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Instansiasi objek dari SvgSaveOptions
    auto saveOptions = MakeObject<SvgSaveOptions>();
    // Jangan kompres gambar SVG ke arsip Zip
    saveOptions->CompressOutputToZipArchive = false;

    try {
    // Simpan output dalam file SVG
    document->Save(_dataDir + outfilename, saveOptions);
    }
    catch (Exception ex) {
    std::cerr << ex->get_Message();
    }

    std::clog << __func__ << ": Finish" << std::endl;
}
```