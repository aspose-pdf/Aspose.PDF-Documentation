---
title: Apa yang baru dari C++
linktitle: Apa yang baru
type: docs
weight: 10
url: /id/cpp/whatsnew/
description: Halaman ini memperkenalkan fitur baru paling populer di Aspose.PDF untuk C++ yang telah diperkenalkan dalam rilis terbaru.
sitemap:
    changefreq: "monthly"
    priority: 0.8
lastmod: "2021-12-22"
---

## Apa yang baru di Aspose.PDF 24.8

Kemampuan untuk menambahkan gambar SVG ke halaman.

## Apa yang baru di Aspose.PDF 24.4

Memperbaiki masalah dengan memuat gambar SVG.

## Apa yang baru di Aspose.PDF 24.3

Memperbaiki kebocoran memori saat mengkonversi dokumen PDF ke format lain.

## Apa yang baru di Aspose.PDF 24.2

Sejak 24.2 telah diimplementasikan:

- Kinerja JPXDecoder telah ditingkatkan.

- Memperbaiki pembacaan dokumen dengan struktur yang rusak.

## Apa yang baru di Aspose.PDF 23.7

- Penyimpanan dokumen PDF ke dalam format EPUB telah diperkenalkan:
```cpp

    void ConvertPDFtoEPUB()
    {
        std::clog << __func__ << ": Start" << std::endl;
        // String untuk nama jalur
        String _dataDir("C:\\Samples\\Conversion\\");

        // String untuk nama file input
        String infilename("sample.pdf");
        // String untuk nama file output
        String outfilename("PDFToEPUB_out.epub");

        // Buka dokumen
        auto document = MakeObject<Document>(_dataDir + infilename);

        // Simpan file PDF ke dalam format EPUB
        document->Save(_dataDir + outfilename, SaveFormat::Epub);
        std::clog << __func__ << ": Finish" << std::endl;
    }
```
```

- Memuat file format PCL telah diimplementasikan:

```cpp

    int main(int argc, char** argv)
    {
        try
        {
            auto options = System::MakeObject<PclLoadOptions>();
            options->ConversionEngine = Aspose::Pdf::PclLoadOptions::ConversionEngines::NewEngine;
            options->SupressErrors = false;

            auto doc = System::MakeObject<Document>(u"c:/aspose.pcl", options);
            doc->Save(u"e:/37432.pdf");
        }
        catch (const System::Exception& error)
        {
            Console::WriteLine(u"Error: {0}", error->get_Message());
            return 1;
        }
        catch (const std::exception& error)
        {
            std::cerr << "Error: " << error.what() << std::endl;
            return 1;
        }

        return 0;
    }
```

## Apa yang baru di Aspose.PDF 23.1

Dari 23.1 dukungan gambar format Dicom telah ditambahkan:

```cpp

    int main()
    {
        auto document = MakeObject<Document>();
        auto page = document->get_Pages()->Add();
        auto image = MakeObject<Image>();
        image->set_FileType(ImageFileType::Dicom);
        image->set_ImageStream(MakeObject<FileStream>(u"c:/aspose.pdf/Aspose.dcm", FileMode::Open, FileAccess::Read));
        page->get_Paragraphs()->Add(image);
        document->Save(u"e:/document.pdf");
    }
```

## Apa yang baru di Aspose.PDF 22.11

Dari 22.11 diumumkan rilis publik pertama **Aspose.PDF untuk C++ macOS**.

Kami dengan senang hati mengumumkan rilis publik pertama dari Aspose.PDF untuk C++ macOS. Aspose.PDF untuk C++ macOS adalah pustaka C++ eksklusif yang memungkinkan pengembang untuk membuat dan memanipulasi dokumen PDF tanpa menggunakan Adobe Acrobat. Aspose.PDF untuk C++ macOS memungkinkan pengembang untuk membuat formulir, menambah/mengedit teks, memanipulasi halaman PDF, menambahkan anotasi, memproses font khusus, dan banyak lagi.

## Apa yang baru di Aspose.PDF 22.5

Dukungan untuk formulir XFA dalam dokumen PDF telah diimplementasikan.

## Apa yang baru di Aspose.PDF 22.4

Versi baru dari Aspose.PDF untuk C++ memiliki basis kode dari Aspose.PDF untuk .Net 22.4 dan Aspose.Imaging 22.4.

- metode System::Drawing::GetThumbnailImage() telah diimplementasikan;
- konstruktor RegionDataNodeRect telah dioptimalkan;
- pemuatan gambar hitam-putih 1 bit per piksel telah diperbaiki.

## Apa yang baru di Aspose.PDF 22.3

Overload metode telah ditambahkan ke banyak kelas. These support ArrayView-typed parameters where only ArrayPtr was supported previously.

## Apa yang baru di Aspose.PDF 22.1

Versi baru Aspose.PDF untuk C++ memiliki kode dasar Aspose.PDF untuk .Net 22.1:

- implementasi baru untuk System::Xml telah disediakan. Sebelumnya, kami memiliki implementasi khusus yang berdasarkan pada perpustakaan libxml2 dan libxslt. Versi baru didasarkan pada kode CoreFX yang diporting

- perpustakaan double-conversion telah ditingkatkan ke versi 3.1.7

- file Dll ditandatangani dengan sertifikat Aspose

## Apa yang baru di Aspose.PDF 21.10

### Aspose.PDF untuk C++ mendukung fitur untuk mengonversi format SVG ke PDF

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
        String infilename("Aspose.svg");
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

## Apa yang baru di Aspose.PDF 21.4

### Menyimpan dokumen PDF ke format HTML telah diimplementasikan

Aspose.PDF untuk C++ mendukung fitur untuk mengonversi file PDF menjadi HTML.

```cpp

    int main()
    {
        auto doc = MakeObject<Document>(u"e:\\sample.pdf");
        doc->Save(u"e:\\sample.html", SaveFormat::Html);
    }
```