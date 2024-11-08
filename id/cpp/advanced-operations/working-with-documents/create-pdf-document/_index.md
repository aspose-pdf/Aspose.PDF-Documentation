```
title: Membuat Dokumen PDF
linktitle: Buat PDF
type: docs
weight: 10
url: /id/cpp/create-pdf-document/
description: Artikel ini menjelaskan cara Membuat dan memformat Dokumen PDF dengan Aspose.PDF untuk C++.
lastmod: "2021-11-11"
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

Kami selalu mencari cara untuk menghasilkan dokumen PDF dan bekerja dengan mereka dalam proyek C++ dengan lebih tepat, akurat, dan efektif. Memiliki fungsi yang mudah digunakan dari sebuah pustaka memungkinkan kita untuk lebih fokus pada pekerjaan, dan kurang pada detail yang memakan waktu dalam mencoba menghasilkan PDF, baik dalam C++.

## Menghasilkan PDF menggunakan C++

Aspose.PDF untuk C++ API memungkinkan Anda membuat dan membaca file PDF menggunakan C++. API ini dapat digunakan dalam berbagai aplikasi C++ termasuk WinForms, dan beberapa lainnya. Dalam artikel ini, kami akan menunjukkan cara menggunakan Aspose.PDF untuk C++ API untuk dengan mudah menghasilkan dan membaca file PDF dalam aplikasi C++.

### Cara Membuat File PDF Sederhana

Untuk membuat file PDF menggunakan C++, langkah-langkah berikut dapat digunakan.

1.
``` Buat objek dari kelas [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document)
1. Tambahkan objek [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page) ke koleksi 'Pages' dari objek Document
1. Tambahkan [TextFragment](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_fragment/) ke koleksi [Paragraphs](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.paragraphs) dari halaman
1. Simpan dokumen PDF yang dihasilkan

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void CreateDocument() {
    // String untuk nama jalur.
    String _dataDir("C:\\Samples\\");

    // String untuk nama file.
    String outputFileName("HelloWorld_out.pdf");

    auto document = MakeObject<Document>();
    auto page = document->get_Pages()->Add();

    // Tambahkan teks ke halaman baru
    auto text = MakeObject<TextFragment>(u"Hello world!");

    auto paragraphs = page->get_Paragraphs();
    paragraphs->Add(text);

    // Simpan PDF yang diperbarui
    document->Save(_dataDir + outputFileName);
}
```
## Membuat dokumen PDF yang Dapat Dicari

Aspose.PDF untuk C++ memungkinkan Anda membuat PDF dari awal dan memanipulasi yang sudah ada.
Ketika Anda menambahkan elemen teks ke PDF, PDF yang dihasilkan dapat dicari. Namun, jika kita mengonversi gambar yang berisi teks ke file PDF, konten di dalam PDF tidak dapat dicari. Namun, sebagai solusi, kita dapat menggunakan OCR pada file yang dihasilkan untuk membuatnya dapat dicari. Oleh karena itu, pertama-tama Anda perlu menginstal Tesseract-OCR pada sistem Anda, dan Anda akan memiliki aplikasi konsol tesseract.

Berikut adalah kode lengkap untuk memenuhi kebutuhan ini:

```cpp
void CreateSearchableDocument() {
    // String untuk nama path.
    String _dataDir("C:\\Samples\\");
    // String untuk nama file.
    String inputFileName("sample.pdf");

    auto document = MakeObject<Document>(inputFileName);
    bool convertResult = false;
    try
    {
        convertResult = document->Convert(CallBackGetHocr);
    }
    catch (Exception ex)
    {
        std::cerr << ex->get_Message() << std::endl;
    }
    document->Dispose();
}

static String CallBackGetHocr(System::SharedPtr<System::Drawing::Image> img)
{
    String tmpFile = System::IO::Path::GetTempFileNameSafe();

    auto bmp = MakeObject<System::Drawing::Bitmap>(img);

    bmp->Save(tmpFile, System::Drawing::Imaging::ImageFormat::get_Bmp());
    String inputFile = String::Format(u"\"{0}\"", tmpFile);
    String outputFile = String::Format(u"\"{0}\"", tmpFile);
    String arguments = inputFile + u" " + outputFile + u" -l eng hocr";
    String tesseractProcessName = u"C:\\Program Files\\Tesseract-OCR\\Tesseract.exe";

    auto psi = MakeObject<System::Diagnostics::ProcessStartInfo>(tesseractProcessName, arguments);
    psi->set_UseShellExecute(true);
    psi->set_CreateNoWindow(true);
    psi->set_WindowStyle(System::Diagnostics::ProcessWindowStyle::Hidden);
    psi->set_WorkingDirectory(System::IO::Path::GetDirectoryName(tesseractProcessName));

    auto p = MakeObject<System::Diagnostics::Process>(psi);
    p->Start();
    p->WaitForExit();

    auto streamReader = MakeObject<System::IO::StreamReader>(tmpFile + u".hocr");
    String text = streamReader->ReadToEnd();
    streamReader->Close();

    if (System::IO::File::Exists(tmpFile))
        System::IO::File::Delete(tmpFile);
    if (System::IO::File::Exists(tmpFile + u".hocr"))
        System::IO::File::Delete(tmpFile + u".hocr");

    return text;
}
```