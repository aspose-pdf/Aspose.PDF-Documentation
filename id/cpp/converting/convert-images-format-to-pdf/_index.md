---
title: Mengonversi berbagai format Gambar ke PDF
linktitle: Konversi Gambar ke PDF
type: docs
weight: 60
url: id/cpp/convert-images-format-to-pdf/
lastmod: "2021-11-19"
description: Topik ini menunjukkan bagaimana pustaka Aspose.PDF untuk C++ memungkinkan untuk mengonversi berbagai format gambar ke PDF.
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

**Aspose.PDF untuk C++** memungkinkan Anda untuk mengonversi berbagai format gambar ke file PDF. Pustaka kami menunjukkan potongan kode untuk mengonversi format gambar yang paling populer, seperti - format BMP, DICOM, EMF, JPG, PNG, SVG, dan TIFF.

## Mengonversi BMP ke PDF

Mengonversi file BMP ke dokumen PDF menggunakan pustaka **Aspose.PDF untuk C++**.

Gambar <abbr title="Bitmap Image File">BMP</abbr> adalah file yang memiliki ekstensi. BMP mewakili file Gambar Bitmap yang digunakan untuk menyimpan gambar digital bitmap. Gambar-gambar ini independen dari adapter grafis dan juga disebut format file bitmap independen perangkat (DIB).
Anda dapat mengonversi BMP ke file PDF dengan API Aspose.PDF untuk C++.
``` Oleh karena itu, Anda dapat mengikuti langkah-langkah berikut untuk mengonversi gambar BMP:

1. Buat [Kelas String](https://reference.aspose.com/pdf/cpp/class/system.string) untuk nama jalur dan nama file.
1. Sebuah instance dari objek Dokumen baru dibuat.
1. Tambahkan [Halaman](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page) baru ke [Dokumen](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) ini.
1. Sebuah Aspose.Pdf BMP baru dibuat.
1. Objek Aspose.PDF BMP diinisialisasi menggunakan file input.
1. Aspose.PDF BMP ditambahkan ke Halaman sebagai Paragraf.
1. Terakhir, simpan file PDF keluaran

Jadi cuplikan kode berikut mengikuti langkah-langkah ini dan menunjukkan cara mengonversi BMP ke PDF menggunakan C++:

```cpp
void ConvertBMPtoPDF() 
{
    std::clog << "BMP to PDF convert: Start" << std::endl;

    // String untuk nama jalur
    String _dataDir("C:\\Samples\\Conversion\\");

    // String untuk nama file input
    String infilename("sample.bmp");

    // String untuk nama file output
    String outfilename("ImageToPDF-BMP.pdf");

    // Buka dokumen
    auto document = MakeObject<Document>();

    // Tambahkan halaman kosong dalam dokumen kosong
    auto page = document->get_Pages()->Add();
    auto image = MakeObject<Aspose::Pdf::Image>();
    image->set_File(_dataDir + infilename);

    // Tambahkan gambar pada halaman
    page->get_Paragraphs()->Add(image);

    // Simpan dokumen keluaran
    document->Save(_dataDir + outfilename);

    std::clog << "BMP to PDF convert: Finish" << std::endl;
}
```
{{% alert color="success" %}}
**Cobalah mengonversi BMP ke PDF secara online**

Aspose menghadirkan aplikasi online gratis ["BMP to PDF"](https://products.aspose.app/pdf/conversion/bmp-to-pdf/), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitas kerjanya.

[![Aspose.PDF Konversi BMP ke PDF menggunakan Aplikasi Gratis](bmp_to_pdf.png)](https://products.aspose.app/pdf/conversion/bmp-to-pdf/)
{{% /alert %}}

## Konversikan DICOM ke PDF

<abbr title="Digital Imaging and Communications in Medicine">DICOM</abbr> adalah standar industri medis untuk pembuatan, penyimpanan, transmisi, dan visualisasi gambar medis digital dan dokumen pasien yang diperiksa.

**Aspose.PDF untuk C++** memungkinkan Anda mengonversi gambar DICOM dan SVG, tetapi untuk alasan teknis untuk menambahkan gambar Anda perlu menentukan jenis file yang akan ditambahkan ke PDF:

1. Buat [Kelas String](https://reference.aspose.com/pdf/cpp/class/system.string) untuk nama jalur dan nama file.
1. Instantiate [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) Objek.
1. Tambahkan [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page) ke koleksi halaman dari dokumen.
1. Aspose.PDF TDicom ditambahkan ke Halaman sebagai Paragraf.
1. Muat dan [Simpan](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#ac082fe8e67b25685fc51d33e804269fa) file gambar input.

Cuplikan kode berikut menunjukkan cara mengonversi file DICOM ke format PDF dengan Aspose.PDF. Anda harus memuat gambar DICOM, menempatkan gambar pada halaman dalam file PDF dan menyimpan keluaran sebagai PDF.

```cpp
void ConvertDICOMtoPDF()
{
    std::clog << "DICOM to PDF convert: Start" << std::endl;

    String _dataDir("C:\\Samples\\Conversion\\");
    String infilename("CR_Anno.dcm");
    String outfilename("PDFWithDicomImage_out.pdf");

    // Instantiate Document Object
    auto document = MakeObject<Document>();

    // Add a page to pages collection of document
    auto page = document->get_Pages()->Add();

    auto image = MakeObject<Aspose::Pdf::Image>();
    image->set_File(_dataDir + infilename);
    image->set_FileType(Aspose::Pdf::ImageFileType::Dicom);

    page->get_Paragraphs()->Add(image);

    // Save output as PDF format
    document->Save(_dataDir + outfilename);
    std::clog << "DICOM to PDF convert: Finish" << std::endl;
}
```
{{% alert color="success" %}}
**Coba konversi DICOM ke PDF secara online**

Aspose mempersembahkan aplikasi gratis online ["DICOM ke PDF"](https://products.aspose.app/pdf/conversion/dicom-to-pdf/), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitas kerjanya.

[![Aspose.PDF Konversi DICOM ke PDF menggunakan Aplikasi Gratis](dicom_to_pdf.png)](https://products.aspose.app/pdf/conversion/dicom-to-pdf/)
{{% /alert %}}

## Konversi EMF ke PDF

<abbr title="Enhanced metafile format">EMF</abbr>EMF menyimpan gambar grafis secara independen dari perangkat. Metafile EMF terdiri dari rekaman panjang variabel dalam urutan kronologis yang dapat merender gambar yang disimpan setelah memparsing pada perangkat keluaran mana pun. Selain itu, Anda dapat mengonversi EMF ke gambar PDF menggunakan langkah-langkah di bawah ini:

1. Buat [Kelas String](https://reference.aspose.com/pdf/cpp/class/system.string) untuk nama jalur dan nama file.
1. Sebuah instance dari objek Dokumen baru dibuat.
1. Tambahkan Halaman baru ke [Dokumen](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) ini.
1.  Sebuah Aspose.Pdf TIFF baru telah dibuat.
1. Objek Aspose.PDF TIFF diinisialisasi menggunakan file input.
1. Aspose.PDF TIFF ditambahkan ke Halaman sebagai Paragraph.
1. Memuat dan [Menyimpan](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#ac082fe8e67b25685fc51d33e804269fa) file gambar input.

Selain itu, potongan kode berikut menunjukkan cara mengonversi EMF ke PDF dengan C++ dalam potongan kode Anda:

```cpp
void ConvertEMFtoPDF() 
{
    std::clog << "EMF ke PDF konversi: Mulai" << std::endl;

    String _dataDir("C:\\Samples\\Conversion\\");
    String infilename("sample.emf");
    String outfilename("ImageToPDF_emf.pdf");

    auto fileStream = System::IO::File::OpenRead(_dataDir + infilename);
    auto myimage = MakeObject<System::Drawing::Bitmap>(fileStream);

    auto document = MakeObject<Document>();
    auto page = document->get_Pages()->Add();

    auto currentImage = MakeObject<System::IO::MemoryStream>();
    myimage->Save(currentImage, System::Drawing::Imaging::ImageFormat::get_Tiff());

    auto imageht = MakeObject<Aspose::Pdf::Image>();
    imageht->set_ImageStream(currentImage);
    page->get_Paragraphs()->Add(imageht);

    document->Save(_dataDir + outfilename);

    std::clog << "EMF ke PDF konversi: Selesai" << std::endl;
}
```
{{% alert color="success" %}}
**Coba ubah EMF ke PDF secara online**

Aspose mempersembahkan aplikasi gratis online ["EMF to PDF"](https://products.aspose.app/pdf/conversion/emf-to-pdf/), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitas kerjanya.

[![Aspose.PDF Konversi EMF ke PDF menggunakan Aplikasi Gratis](emf_to_pdf.png)](https://products.aspose.app/pdf/conversion/emf-to-pdf/)
{{% /alert %}}

## Konversi JPG ke PDF

Tidak perlu bingung bagaimana mengonversi JPG ke PDF, karena **Aspose.PDF untuk C++** perpustakaan memiliki keputusan terbaik.

Anda dapat dengan sangat mudah mengonversi gambar JPG ke PDF dengan Aspose.PDF untuk C++ dengan mengikuti langkah-langkah berikut:

1. Buat [Kelas String](https://reference.aspose.com/pdf/cpp/class/system.string) untuk nama jalur dan nama file.
1. Sebuah instance dari objek Dokumen baru dibuat.
1. Tambahkan Halaman baru ke [Dokumen](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) ini.
1. Sebuah Aspose::Pdf::Image baru dibuat.
1. Objek Gambar Aspose.PDF diinisialisasi menggunakan file input.
1. Aspose.PDF Image ditambahkan ke Halaman sebagai Paragraf.  
1. Muat dan simpan file gambar input.

Cuplikan kode di bawah ini menunjukkan cara mengonversi Gambar JPG ke PDF menggunakan C++:

```cpp
void ConvertJPEGtoPDF() 
{
    std::clog << "JPEG to PDF convert: Start" << std::endl;
    // String untuk nama jalur
    String _dataDir("C:\\Samples\\Conversion\\");

    // String untuk nama file input
    String infilename("sample.jpg");

    // String untuk nama file output
    String outfilename("ImageToPDF-JPEG.pdf");

    // Buka dokumen
    auto document = MakeObject<Document>();

    // Tambahkan halaman kosong dalam dokumen kosong
    auto page = document->get_Pages()->Add();
    auto image = MakeObject<Aspose::Pdf::Image>();
    image->set_File(_dataDir + infilename);

    // Tambahkan gambar pada halaman
    page->get_Paragraphs()->Add(image);

    // Simpan dokumen output
    document->Save(_dataDir + outfilename);
    std::clog << "JPEG to PDF convert: Finish" << std::endl;
}
```

Kemudian Anda dapat melihat cara mengonversi gambar ke PDF dengan **tinggi dan lebar halaman yang sama**. We akan mendapatkan dimensi gambar dan menyesuaikan dimensi halaman dokumen PDF dengan langkah-langkah berikut:

1. Muat file gambar input
1. Dapatkan tinggi dan lebar gambar
1. Atur tinggi, lebar, dan margin halaman
1. Simpan file PDF keluaran

Cuplikan kode berikut menunjukkan cara mengonversi Gambar ke PDF dengan tinggi dan lebar halaman yang sama menggunakan C++:

```cpp
void ConvertJPGtoPDF_fitsize() 
{
    std::clog << "JPEG to PDF convert: Start" << std::endl;
    // String untuk nama path
    String _dataDir("C:\\Samples\\Conversion\\");

    // String untuk nama file input
    String infilename("sample.jpg");

    // String untuk nama file output
    String outfilename("ImageToPDF-JPG.pdf");

    // Buka dokumen
    auto document = MakeObject<Document>();

    // Tambahkan halaman kosong di dokumen kosong
    auto page = document->get_Pages()->Add();
    auto fileStream = System::IO::File::OpenRead(_dataDir + infilename);
    auto bitMap = MakeObject<System::Drawing::Bitmap>(fileStream);

    auto image = MakeObject<Aspose::Pdf::Image>();
    image->set_File(_dataDir + infilename);

    // Tambahkan gambar pada halaman
    page->get_Paragraphs()->Add(image);

    // Atur dimensi halaman dan margin
    page->get_PageInfo()->set_Height(bitMap->get_Height());
    page->get_PageInfo()->set_Width(bitMap->get_Width());
    page->get_PageInfo()->get_Margin()->set_Bottom(0);
    page->get_PageInfo()->get_Margin()->set_Top(0);
    page->get_PageInfo()->get_Margin()->set_Right(0);
    page->get_PageInfo()->get_Margin()->set_Left(0);
    page->get_Paragraphs()->Add(image);

    // Simpan dokumen keluaran
    document->Save(_dataDir + outfilename);
    std::clog << "JPEG to PDF convert: Finish" << std::endl;
}
```
{{% alert color="success" %}}
**Coba konversi JPG ke PDF secara online**

Aspose mempersembahkan aplikasi online gratis ["JPG to PDF"](https://products.aspose.app/pdf/conversion/jpg-to-pdf/), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitasnya.

[![Aspose.PDF Konversi JPG ke PDF menggunakan Aplikasi Gratis](jpg_to_pdf.png)](https://products.aspose.app/pdf/conversion/jpg-to-pdf/)
{{% /alert %}}

## Konversi PNG ke PDF

**Aspose.PDF untuk C++** mendukung fitur untuk mengonversi gambar PNG ke format PDF. Periksa potongan kode berikut untuk mewujudkan tugas Anda.

<abbr title="Portable Network Graphics">PNG</abbr> mengacu pada jenis format file gambar raster yang menggunakan kompresi tanpa kehilangan, yang membuatnya populer di kalangan penggunanya.

Anda dapat mengonversi gambar PNG ke PDF menggunakan langkah-langkah berikut:

1. Buat [Kelas String](https://reference.aspose.com/pdf/cpp/class/system.string) untuk nama jalur dan nama file.
1. Sebuah instance dari objek Dokumen baru dibuat.
1. Tambahkan Halaman baru ke [Dokumen](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) ini.
1. Aspose.Pdf PNG baru dibuat.
1. Objek Aspose.PDF PNG diinisialisasi menggunakan file input.
1. Aspose.PDF PNG ditambahkan ke Halaman sebagai Paragraf.
1. Muat dan simpan file gambar input.

Selain itu, cuplikan kode di bawah ini menunjukkan cara mengkonversi PNG ke PDF dalam aplikasi C++ Anda:

```cpp
void ConvertPNGtoPDF() 
{
    std::clog << "PNG to PDF convert: Start" << std::endl;
    // String untuk nama path
    String _dataDir("C:\\Samples\\Conversion\\");

    // String untuk nama file input
    String infilename("sample.png");

    // String untuk nama file output
    String outfilename("ImageToPDF-PNG.pdf");

    // Buka dokumen
    auto document = MakeObject<Document>();

    // Tambahkan halaman kosong di dokumen kosong
    auto page = document->get_Pages()->Add();
    auto image = MakeObject<Aspose::Pdf::Image>();
    image->set_File(_dataDir + infilename);

    // Tambahkan gambar pada halaman
    page->get_Paragraphs()->Add(image);

    // Simpan dokumen output
    document->Save(_dataDir + outfilename);
    std::clog << "PNG to PDF convert: Finish" << std::endl;
}
```
{{% alert color="success" %}}
**Coba konversi PNG ke PDF online**

Aspose mempersembahkan aplikasi online gratis ["PNG to PDF"](https://products.aspose.app/pdf/conversion/png-to-pdf/), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitasnya.

[![Aspose.PDF Konversi PNG ke PDF menggunakan Aplikasi Gratis](png_to_pdf.png)](https://products.aspose.app/pdf/conversion/png-to-pdf/)
{{% /alert %}}

## Konversi SVG ke PDF

**Aspose.PDF untuk C++** menjelaskan cara mengonversi gambar SVG ke format PDF dan cara mendapatkan dimensi dari file <abbr title="Scalable Vector Graphics">SVG</abbr> sumber.

Scalable Vector Graphics (SVG) adalah keluarga spesifikasi dari format file berbasis XML untuk grafik vektor dua dimensi, baik statis maupun dinamis (interaktif atau animasi). Spesifikasi SVG adalah standar terbuka yang telah dikembangkan oleh World Wide Web Consortium (W3C) sejak tahun 1999.

Gambar SVG dan perilakunya didefinisikan dalam file teks XML. Ini berarti bahwa mereka dapat dicari, diindeks, diskript, dan jika diperlukan, dikompresi. Sebagai file XML, gambar SVG dapat dibuat dan diedit dengan editor teks apa pun, tetapi seringkali lebih nyaman untuk membuatnya dengan program menggambar seperti Inkscape.

1. Buat [Kelas String](https://reference.aspose.com/pdf/cpp/class/system.string) untuk nama jalur dan nama file.
1. Buat instance dari kelas [`SvgLoadOptions`](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.svg_load_options).
1. Buat instance dari [Dokumen](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) dengan menyebutkan nama file sumber dan opsi.
1. Simpan dokumen dengan nama file yang diinginkan.

Cuplikan kode berikut menunjukkan proses konversi file SVG ke format PDF dengan Aspose.PDF untuk C++.

```cpp
void ConvertSVGtoPDF() 
{
    std::clog << "SVG to PDF convert: Start" << std::endl;

    String _dataDir("C:\\Samples\\Conversion\\");
    String infilename("sample.svg");
    String outfilename("ImageToPDF-SVG.pdf");

    auto options = MakeObject<SvgLoadOptions>();
    try {
    auto document = MakeObject<Document>(_dataDir + infilename, options);
    document->Save(_dataDir + outfilename);
    }
    catch (System::Exception ex) {
    std::cerr << ex->get_Message() << std::endl;
    }
    std::clog << "SVG to PDF convert: Finish" << std::endl;
}
```
Сonsider an example with advanced features:

```cpp
void ConvertSVGtoPDF_Advanced()
{
    std::clog << "SVG to PDF convert: Start" << std::endl;

    String _dataDir("C:\\Samples\\Conversion\\");
    String infilename("Sweden-Royal-flag-grand-coa.svg");
    String outfilename("ImageToPDF-SVG.pdf");

    auto options = MakeObject<SvgLoadOptions>();
    options->set_AdjustPageSize(true);
    options->ConversionEngine = SvgLoadOptions::ConversionEngines::NewEngine;

    try {
    auto document = MakeObject<Document>(_dataDir + infilename, options);
    document->Save(_dataDir + outfilename);
    }
    catch (System::Exception ex) {
    std::cerr << ex->get_Message() << std::endl;
    }

    std::clog << "SVG to PDF convert: Finish" << std::endl;
}
```

{{% alert color="success" %}}
**Cobalah mengonversi format SVG ke PDF secara online**

Aspose.PDF untuk C++ menghadirkan aplikasi online gratis ["SVG to PDF"](https://products.aspose.app/pdf/conversion/svg-to-pdf), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitasnya bekerja.

[![Aspose.PDF Convertion SVG to PDF with Free App](svg_to_pdf.png)](https://products.aspose.app/pdf/conversion/svg-to-pdf) {{% /alert %}}

## Konversi TIFF ke PDF

**Aspose.PDF** mendukung format file, baik itu gambar <abbr title="Tag Image File Format">TIFF</abbr> satu bingkai atau multi-bingkai. Ini berarti bahwa Anda dapat mengonversi gambar TIFF ke PDF dalam aplikasi C++ Anda.

TIFF atau TIF, Tagged Image File Format, mewakili gambar raster yang ditujukan untuk digunakan pada berbagai perangkat yang mematuhi standar format file ini. Gambar TIFF dapat berisi beberapa bingkai dengan gambar yang berbeda. Format file Aspose.PDF juga didukung, baik itu gambar TIFF satu bingkai atau multi-bingkai. Jadi Anda dapat mengonversi gambar TIFF ke PDF dalam aplikasi C++ Anda. Oleh karena itu, kami akan mempertimbangkan contoh konversi gambar TIFF multi-halaman ke dokumen PDF multi-halaman dengan langkah-langkah berikut:

1. Buat [Kelas String](https://reference.aspose.com/pdf/cpp/class/system.string) untuk nama jalur dan nama file. 1. Sebuah instance dari objek Dokumen baru dibuat.
1. Tambahkan Halaman baru ke [Dokumen](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) ini.
1. Sebuah Aspose.Pdf TIFF baru dibuat.
1. Objek Aspose.PDF TIFF diinisialisasi menggunakan file input.
1. Aspose.PDF TIFF ditambahkan ke Halaman sebagai Paragraf.
1. Muat dan simpan file gambar input.

Selain itu, cuplikan kode berikut menunjukkan cara mengonversi gambar TIFF multi-halaman atau multi-frame ke PDF dengan C++:

```cpp
void ConvertTIFFtoPDF() 
{
    std::clog << "TIFF to PDF convert: Start" << std::endl;

    String _dataDir("C:\\Samples\\Conversion\\");
    String infilename("sample.tiff");
    String outfilename("ImageToPDF-TIFF.pdf");

    auto fileStream = System::IO::File::OpenRead(_dataDir + infilename);
    auto myimage = MakeObject<System::Drawing::Bitmap>(fileStream);

    auto document = MakeObject<Document>();
    auto page = document->get_Pages()->Add();

    auto currentImage = MakeObject<System::IO::MemoryStream>();
    myimage->Save(currentImage, System::Drawing::Imaging::ImageFormat::get_Tiff());

    auto imageht = MakeObject<Aspose::Pdf::Image>();
    imageht->set_ImageStream(currentImage);
    page->get_Paragraphs()->Add(imageht);

    document->Save(_dataDir + outfilename);

    std::clog << "TIFF to PDF convert: Finish" << std::endl;
}
```