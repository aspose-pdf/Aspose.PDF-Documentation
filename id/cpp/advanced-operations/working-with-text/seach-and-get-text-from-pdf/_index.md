---
title: Cari dan Dapatkan Teks dari Halaman Dokumen PDF 
linktitle: Cari dan Dapatkan Teks
type: docs
weight: 60
url: id/cpp/search-and-get-text-from-pdf/
description: Artikel ini menjelaskan cara menggunakan berbagai alat untuk mencari dan mendapatkan teks dari dokumen PDF. Kita dapat mencari dengan ekspresi reguler dari halaman tertentu atau seluruh halaman.
lastmod: "2021-12-13"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Cari dan Dapatkan Teks dari Semua Halaman Dokumen PDF

Kelas [TextFragmentAbsorber](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_fragment_absorber/) memungkinkan Anda menemukan teks, yang cocok dengan frasa tertentu, dari semua halaman dokumen PDF. Untuk mencari teks dari seluruh dokumen, Anda perlu memanggil metode Accept dari koleksi [Pages](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page). Metode 'Accept' menerima objek TextFragmentAbsorber sebagai parameter, yang mengembalikan koleksi objek TextFragment.

Cuplikan kode berikut menunjukkan cara mencari teks dari semua halaman.

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void SearchAndGetTextFromAllThePagesOfPDFDocument() {
    String _dataDir("C:\\Samples\\");

    auto document = new Document(_dataDir + u"sample.pdf");

    // Buat objek TextAbsorber untuk menemukan semua instance dari frasa pencarian yang dimasukkan
    auto textFragmentAbsorber = MakeObject<TextFragmentAbsorber>("document");

    // Terima absorber untuk semua halaman
    document->get_Pages()->Accept(textFragmentAbsorber);

    // Dapatkan fragmen teks yang diekstraksi ke dalam koleksi
    auto textFragmentCollection = textFragmentAbsorber->get_TextFragments();

    // Loop melalui fragmen
    for (auto textFragment : textFragmentCollection) {
        Console::WriteLine(u"Teks :- {0}", textFragment->get_Text());
        Console::WriteLine(u"Posisi :- {0}", textFragment->get_Position());
        Console::WriteLine(u"XIndent :- {0}", textFragment->get_Position()->get_XIndent());
        Console::WriteLine(u"YIndent :- {0}", textFragment->get_Position()->get_YIndent());
        Console::WriteLine(u"Font - Nama :- {0}", textFragment->get_TextState()->get_Font()->get_FontName());
        Console::WriteLine(u"Font - Dapat Diakses :- {0}", textFragment->get_TextState()->get_Font()->get_IsAccessible());
        Console::WriteLine(u"Font - Tertanam - {0}", textFragment->get_TextState()->get_Font()->get_IsEmbedded());
        Console::WriteLine(u"Font - Subset :- {0}", textFragment->get_TextState()->get_Font()->get_IsSubset());
        Console::WriteLine(u"Ukuran Font :- {0}", textFragment->get_TextState()->get_FontSize());
        Console::WriteLine(u"Warna Depan :- {0}", textFragment->get_TextState()->get_ForegroundColor());
    }
}
```

## Search and Get Text from all pages using Regular Expression

TextFragmentAbsorber membantu Anda mencari dan mengambil teks, dari semua halaman, berdasarkan ekspresi reguler. Pertama, Anda perlu memberikan ekspresi reguler ke konstruktor [TextFragmentAbsorber](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_fragment_absorber/) sebagai frasa. Setelah itu, Anda harus mengatur properti [TextSearchOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_search_options/) dari objek TextFragmentAbsorber. Properti ini memerlukan objek TextSearchOptions dan Anda perlu memberikan nilai true sebagai parameter ke konstruktornya saat membuat objek baru. Karena Anda ingin mengambil teks yang cocok dari semua halaman, Anda perlu memanggil metode Accept dari koleksi Pages. [TextFragmentAbsorber](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_fragment_absorber/) mengembalikan TextFragmentCollection yang berisi semua fragmen yang cocok dengan kriteria yang ditentukan oleh ekspresi reguler. Potongan kode berikut menunjukkan cara mencari dan mendapatkan teks dari semua halaman berdasarkan ekspresi reguler.

```cpp
void SearchAndGetTextFromPagesUsingRegularExpression()
{
    String _dataDir("C:\\Samples\\");

    auto document = new Document(_dataDir + u"sample.pdf");

    // Buat objek TextAbsorber untuk menemukan semua instansi dari frasa pencarian yang dimasukkan
    auto textFragmentAbsorber = MakeObject<TextFragmentAbsorber>(u"\\d{4}-\\d{4}"); // seperti 1999-2000

    // Atur opsi pencarian teks untuk menentukan penggunaan ekspresi reguler
    auto textSearchOptions = MakeObject<TextSearchOptions>(true);
    textFragmentAbsorber->set_TextSearchOptions(textSearchOptions);

    // Terima absorber untuk halaman pertama dokumen
    document->get_Pages()->Accept(textFragmentAbsorber);

    // Dapatkan fragmen teks yang diekstraksi ke dalam koleksi
    auto textFragmentCollection = textFragmentAbsorber->get_TextFragments();

    // Loop melalui fragmen
    for (auto textFragment : textFragmentCollection) {
        Console::WriteLine(u"Teks :- {0}", textFragment->get_Text());
        Console::WriteLine(u"Posisi :- {0}", textFragment->get_Position());
        Console::WriteLine(u"XIndent :- {0}", textFragment->get_Position()->get_XIndent());
        Console::WriteLine(u"YIndent :- {0}", textFragment->get_Position()->get_YIndent());
        Console::WriteLine(u"Font - Nama :- {0}", textFragment->get_TextState()->get_Font()->get_FontName());
        Console::WriteLine(u"Font - IsAccessible :- {0}", textFragment->get_TextState()->get_Font()->get_IsAccessible());
        Console::WriteLine(u"Font - IsEmbedded - {0}", textFragment->get_TextState()->get_Font()->get_IsEmbedded());
        Console::WriteLine(u"Font - IsSubset :- {0}", textFragment->get_TextState()->get_Font()->get_IsSubset());
        Console::WriteLine(u"Ukuran Font :- {0}", textFragment->get_TextState()->get_FontSize());
        Console::WriteLine(u"Warna Latar Depan :- {0}", textFragment->get_TextState()->get_ForegroundColor());
    }
}
```