```
---
title: Ekstrak teks dari semua halaman PDF menggunakan C++
linktitle: Ekstrak teks dari PDF
type: docs
weight: 10
url: /cpp/extract-text-from-all-pdf/
description: Artikel ini menjelaskan berbagai cara untuk mengekstrak teks dari dokumen PDF menggunakan Aspose.PDF dalam C++. Dari seluruh halaman, dari bagian tertentu, berdasarkan kolom, dll.
lastmod: "2021-12-13"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Ekstrak Teks Dari Semua Halaman Dokumen PDF

Mengekstrak teks dari dokumen PDF adalah kebutuhan umum.
``` Dalam contoh ini, Anda akan melihat bagaimana Aspose.PDF untuk C++ memungkinkan ekstraksi teks dari semua halaman dokumen PDF. Anda perlu membuat objek dari kelas [TextAbsorber](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.table_absorber). Setelah itu, buka PDF menggunakan kelas [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) dan panggil metode 'Accept' dari koleksi [Pages](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page). Kelas [TextAbsorber](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.table_absorber) menyerap teks dari dokumen dan mengembalikannya dalam properti 'Text'. Cuplikan kode berikut menunjukkan bagaimana mengekstraksi teks dari semua halaman dokumen PDF.

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void ExtractTextFromAllThePages() {

    std::clog << __func__ << ": Start" << std::endl;
    // String untuk nama path
    String _dataDir("C:\\Samples\\Parsing\\");

    // String untuk nama file
    String infilename("sample-4pages.pdf");
    String outfilename("extracted-text.txt");

    // Buka dokumen
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Buat objek TextAbsorber untuk mengekstrak teks
    auto textAbsorber = MakeObject<TextAbsorber>();
    // Terima absorber untuk semua halaman
    document->get_Pages()->Accept(textAbsorber);
    // Dapatkan teks yang diekstraksi
    auto extractedText = textAbsorber->get_Text();

    System::IO::File::WriteAllText(_dataDir + outfilename, extractedText);
    std::clog << __func__ << ": Finish" << std::endl;
}
```
Panggil metode **Accept** pada halaman tertentu dari objek Dokumen. Indeks adalah nomor halaman tertentu dari mana teks perlu diekstraksi.

```cpp
void ExtractTextFromParticularPage() {

    std::clog << __func__ << ": Start" << std::endl;
    // String untuk nama jalur
    String _dataDir("C:\\Samples\\Parsing\\");

    // String untuk nama file
    String infilename("sample-4pages.pdf");
    String outfilename("extracted-text.txt");

    // Buka dokumen
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Buat objek TextAbsorber untuk mengekstrak teks
    auto textAbsorber = MakeObject<TextAbsorber>();
    // Terima absorber untuk semua halaman
    document->get_Pages()->idx_get(1)->Accept(textAbsorber);
    // Dapatkan teks yang diekstraksi
    auto extractedText = textAbsorber->get_Text();

    System::IO::File::WriteAllText(_dataDir + outfilename, extractedText);
    std::clog << __func__ << ": Finish" << std::endl;
}
```

## Ekstrak Teks dari Halaman menggunakan Perangkat Teks

Anda dapat menggunakan kelas [TextDevice](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.devices.text_device/) untuk mengekstrak teks dari file PDF. TextDevice menggunakan TextAbsorber dalam implementasinya, sehingga, pada kenyataannya, mereka melakukan hal yang sama tetapi TextDevice hanya diimplementasikan untuk menyatukan pendekatan "Perangkat" untuk mengekstrak apa pun dari halaman seperti ImageDevice, PageDevice, dll. TextAbsorber dapat mengekstrak teks dari Halaman, seluruh PDF, atau XForm, TextAbsorber ini lebih universal

### Ekstrak teks dari semua halaman

Langkah-langkah berikut dan potongan kode menunjukkan kepada Anda cara mengekstrak teks dari PDF menggunakan perangkat teks.

1. Buat objek dari kelas Document dengan file PDF input yang ditentukan
1. Buat objek dari kelas TextDevice
1. Gunakan objek dari kelas TextExtractOptions untuk menentukan opsi ekstraksi
1. Gunakan metode Process dari kelas TextDevice untuk mengonversi konten menjadi teks
1. Simpan teks ke file output

```cpp
void ExtractTextUsingTextDevice() {

    std::clog << __func__ << ": Start" << std::endl;
    // String untuk nama jalur
    String _dataDir("C:\\Samples\\Parsing\\");

    // String untuk nama file
    String infilename("sample-4pages.pdf");
    String outfilename("extracted-text.txt");

    // Buka dokumen
    auto document = MakeObject<Document>(_dataDir + infilename);

    auto builder = MakeObject<System::Text::StringBuilder>();
    // String untuk menampung teks yang diekstrak
    String extractedText;

    for (auto page : document->get_Pages()) {
        auto textStream = MakeObject<System::IO::MemoryStream>();
        // Buat perangkat teks
        auto textDevice = MakeObject<Aspose::Pdf::Devices::TextDevice>();

        // Setel opsi ekstraksi teks - setel mode ekstraksi teks (Raw atau Pure)
        auto textExtOptions = MakeObject<TextExtractionOptions>(TextExtractionOptions::TextFormattingMode::Pure);

        textDevice->set_ExtractionOptions(textExtOptions);

        // Konversi halaman tertentu dan simpan teks ke aliran
        textDevice->Process(page, textStream);

        // Tutup aliran memori
        textStream->Close();

        // Dapatkan teks dari aliran memori
        extractedText = System::Text::Encoding::get_Unicode()->GetString(textStream->ToArray());
        builder->Append(extractedText);

    }
    // Simpan teks yang diekstrak dalam file teks
    System::IO::File::WriteAllText(_dataDir + outfilename, builder->ToString());
    std::clog << __func__ << ": Finish" << std::endl;
}
```
## Ekstrak Teks dari wilayah halaman tertentu

Kelas [TextAbsorber](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.table_absorber) menyediakan kemampuan untuk mengekstrak teks dari halaman tertentu atau semua halaman dokumen PDF. Kelas ini mengembalikan teks yang diekstrak dalam properti 'Text'. Namun, jika kita memiliki kebutuhan untuk mengekstrak teks dari wilayah halaman tertentu, kita dapat menggunakan properti **Rectangle** dari [TextSearchOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_search_options/). Properti Rectangle mengambil objek Rectangle sebagai nilai dan menggunakan properti ini, kita dapat menentukan wilayah halaman dari mana kita perlu mengekstrak teks.

Metode **Accept** dari sebuah halaman dipanggil untuk mengekstrak teks. Buat objek dari kelas [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document/) dan [TextAbsorber](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.table_absorber). Panggil metode 'Accept' pada halaman individu, sebagai **Page** Index, dari objek [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document/). **Index** adalah nomor halaman tertentu dari mana teks perlu diekstraksi. Anda dapat mendapatkan teks dari properti 'Text' dari kelas [TextAbsorber](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.table_absorber). Cuplikan kode berikut menunjukkan cara mengekstrak teks dari halaman individu.

```cpp
void ExtractTextFromParticularPageRegion() {

    std::clog << __func__ << ": Start" << std::endl;
    // String untuk nama path
    String _dataDir("C:\\Samples\\Parsing\\");

    // String untuk nama file
    String infilename("sample-4pages.pdf");
    String outfilename("extracted-text.txt");

    // Buka dokumen
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Buat objek TextAbsorber untuk mengekstrak teks
    auto textAbsorber = MakeObject<TextAbsorber>();
    textAbsorber->get_TextSearchOptions()->set_LimitToPageBounds(true);
    textAbsorber->get_TextSearchOptions()->set_Rectangle(MakeObject<Rectangle>(100, 200, 250, 350));

    // Terima absorber untuk semua halaman
    document->get_Pages()->idx_get(1)->Accept(textAbsorber);
    // Dapatkan teks yang diekstraksi
    auto extractedText = textAbsorber->get_Text();

    System::IO::File::WriteAllText(_dataDir + outfilename, extractedText);
    std::clog << __func__ << ": Finish" << std::endl;

}
```
## Ekstrak teks berdasarkan kolom

PDF adalah format yang sangat populer, dan untuk alasan yang baik: dengan PDF, Anda dapat yakin bahwa dokumen Anda akan ditampilkan dan dicetak dengan cara yang sama pada komputer yang berbeda.

Namun, dokumen PDF memiliki kelemahan karena biasanya tidak memiliki informasi tentang apa yang ada dalam paragraf, tabel, gambar, informasi header/footer, dan sebagainya.

Aspose.PDF for C++ - ini adalah utilitas yang mudah digunakan, yang memungkinkan Anda untuk mengekstrak teks berdasarkan kolom.

```cpp
void ExtractTextBasedOnColumns() {

    std::clog << __func__ << ": Start" << std::endl;
    // String untuk nama jalur
    String _dataDir("C:\\Samples\\Parsing\\");

    // String untuk nama file
    String infilename("sample-4pages.pdf");
    String outfilename("extracted-text.txt");

    // Buka dokumen
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Buat objek TextAbsorber untuk mengekstrak teks
    auto textFragmentAbsorber = MakeObject<TextFragmentAbsorber>();


    // Terima penyerap untuk semua halaman
    document->get_Pages()->Accept(textFragmentAbsorber);

    auto tfc = textFragmentAbsorber->get_TextFragments();
    for (auto tf : tfc)
    {
        // Perlu mengurangi ukuran font setidaknya 70%
        auto size = tf->get_TextState()->get_FontSize() * 0.7f;
        tf->get_TextState()->set_FontSize(size);
    }
    auto stream = MakeObject<System::IO::MemoryStream>();
    document->Save(stream);
    document = MakeObject<Document>(stream);
    auto textAbsorber = MakeObject<TextAbsorber>();
    document->get_Pages()->Accept(textAbsorber);
    String extractedText = textAbsorber->get_Text();

    System::IO::File::WriteAllText(_dataDir + outfilename, extractedText);
    std::clog << __func__ << ": Finish" << std::endl;
}
```

### Pendekatan kedua - Menggunakan ScaleFactor

Dalam rilis baru ini, kami juga telah memperkenalkan beberapa perbaikan dalam TextAbsorber dan dalam mekanisme pemformatan teks internal. Jadi sekarang selama ekstraksi teks menggunakan mode 'Murni', Anda dapat menentukan opsi [ScaleFactor](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_extraction_options#a4f9a173765d483b493c31e416f8b035a) dan ini dapat menjadi pendekatan lain untuk mengekstrak teks dari dokumen PDF multi-kolom selain pendekatan yang disebutkan di atas. Faktor skala ini dapat diatur untuk menyesuaikan grid yang digunakan untuk mekanisme pemformatan teks internal selama ekstraksi teks. Menentukan nilai ScaleFactor antara 1 dan 0.1 (termasuk 0.1) memiliki efek yang sama seperti pengurangan font.

Menentukan nilai ScaleFactor antara 0.1 dan -0.1 diperlakukan sebagai nilai nol, tetapi ini membuat algoritma menghitung faktor skala yang diperlukan selama ekstraksi teks secara otomatis. Perhitungan didasarkan pada lebar rata-rata glif dari font paling populer di halaman, tetapi kami tidak dapat menjamin bahwa dalam teks yang diekstraksi tidak ada string kolom yang mencapai awal kolom berikutnya. Harap dicatat bahwa jika nilai ScaleFactor tidak ditentukan, nilai default 1.0 akan digunakan. Ini berarti tidak akan ada penskalaan yang dilakukan. Jika nilai ScaleFactor yang ditentukan lebih dari 10 atau kurang dari -0.1, nilai default 1.0 akan digunakan.

Kami mengusulkan penggunaan penskalaan otomatis (ScaleFactor = 0) saat memproses sejumlah besar file PDF untuk ekstraksi konten teks. Atau secara manual mengatur pengurangan lebar grid yang berlebihan (tentang ScaleFactor = 0.5). Namun, Anda tidak boleh menentukan apakah penskalaan diperlukan untuk dokumen konkret atau tidak. Jika Anda mengatur pengurangan lebar grid yang berlebihan untuk dokumen (yang tidak memerlukannya), konten teks yang diekstraksi akan tetap sepenuhnya memadai. Silakan lihat cuplikan kode berikut.

```cpp
void ExtractTextUsingScaleFactor() {

    std::clog << __func__ << ": Start" << std::endl;
    // String untuk nama jalur
    String _dataDir("C:\\Samples\\Parsing\\");

    // String untuk nama file
    String infilename("sample-4pages.pdf");
    String outfilename("extracted-text.txt");

    // Buka dokumen
    auto document = MakeObject<Document>(_dataDir + infilename);

    auto textAbsorber = MakeObject<TextAbsorber>();
    textAbsorber->set_ExtractionOptions(MakeObject<TextExtractionOptions>(TextExtractionOptions::TextFormattingMode::Pure));
    // Mengatur faktor skala ke 0.5 sudah cukup untuk membagi kolom di sebagian besar dokumen
    // Pengaturan nol memungkinkan algoritma memilih faktor skala secara otomatis
    textAbsorber->get_ExtractionOptions()->set_ScaleFactor(0.5); /* 0; */
    document->get_Pages()->Accept(textAbsorber);
    String extractedText = textAbsorber->get_Text();

    System::IO::File::WriteAllText(_dataDir + outfilename, extractedText);
    std::clog << __func__ << ": Finish" << std::endl;
}
```
## Mengekstrak Teks yang Disorot dari Dokumen PDF

Dalam berbagai skenario ekstraksi teks dari dokumen PDF, Anda mungkin memiliki persyaratan untuk mengekstrak hanya teks yang disorot dari dokumen PDF. Untuk mengimplementasikan fungsionalitas ini, kami telah menambahkan metode TextMarkupAnnotation.GetMarkedText() dan TextMarkupAnnotation.GetMarkedTextFragments() dalam API. Anda dapat mengekstrak teks yang disorot dari dokumen PDF dengan memfilter TextMarkupAnnotation dan menggunakan metode yang disebutkan. Cuplikan kode berikut menunjukkan bagaimana Anda dapat mengekstrak teks yang disorot dari dokumen PDF.

```cpp
void ExtractHighlightedText() {

    std::clog << __func__ << ": Start" << std::endl;
    // String untuk nama jalur
    String _dataDir("C:\\Samples\\Parsing\\");

    // String untuk nama file
    String infilename("sample-highlight.pdf");
    String outfilename("extracted-text.txt");

    // Buka dokumen
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Loop melalui semua anotasi
    for (auto annotation : document->get_Pages()->idx_get(1)->get_Annotations())
    {
        // Filter TextMarkupAnnotation
        if (annotation->get_AnnotationType() == Aspose::Pdf::Annotations::AnnotationType::Highlight)
        {
        auto highlightedAnnotation = System::DynamicCast<Aspose::Pdf::Annotations::HighlightAnnotation>(annotation);

        // Ambil fragmen teks yang disorot
        auto collection = highlightedAnnotation->GetMarkedTextFragments();
        for (auto tf : collection)
        {
            // Tampilkan teks yang disorot
            String s = tf->get_Text();
            std::cout << s << std::endl;
        }
        }
    }
}
```

## Akses Elemen Fragmen Teks dan Segmen dari XML

Terkadang kita perlu mengakses item TextFragment atau TextSegment saat memproses dokumen PDF yang dihasilkan dari XML. Aspose.PDF untuk C++ menyediakan akses ke item-item tersebut berdasarkan nama. Cuplikan kode di bawah ini menunjukkan cara menggunakan fungsionalitas ini.

```cpp
void AccessTextFragmentandSegmentElementsXML()
{
    std::clog << __func__ << ": Start" << std::endl;
    // String untuk nama path
    String _dataDir("C:\\Samples\\Parsing\\");

    // String untuk nama file
    String infilename("sample-doc.xml");
    String outfilename("sample-doc.pdf");

    auto document = MakeObject<Document>();
    document->BindXml(_dataDir + infilename);

    System::SharedPtr<Page> page = System::DynamicCast<Aspose::Pdf::Page>(document->GetObjectById(u"mainSection"));
    // Lakukan beberapa operasi dengan halaman
    // ...

    System::SharedPtr<TextSegment> segment = System::DynamicCast<Aspose::Pdf::Text::TextSegment>(document->GetObjectById(u"product_description"));
    // Lakukan beberapa operasi dengan segmen
    // ...
    document->Save(_dataDir + outfilename);

    std::clog << __func__ << ": Finish" << std::endl;
}
```