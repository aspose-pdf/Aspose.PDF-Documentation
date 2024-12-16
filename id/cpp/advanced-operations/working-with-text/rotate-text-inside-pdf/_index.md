---
title: Memutar Teks di Dalam PDF menggunakan C++
linktitle: Memutar Teks di Dalam PDF
type: docs
weight: 50
url: /id/cpp/rotate-text-inside-pdf/
description: Pelajari berbagai cara untuk memutar teks ke PDF. Aspose.PDF memungkinkan Anda memutar teks ke sudut mana pun, memutar fragmen teks atau seluruh paragraf.
lastmod: "2021-12-13"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Memutar Teks di Dalam PDF menggunakan Properti Rotasi

Dengan menggunakan properti Rotasi dari kelas [TextFragment](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_fragment/), Anda dapat memutar teks pada berbagai sudut. Rotasi teks dapat digunakan dalam berbagai skenario pembuatan dokumen. Anda dapat menetapkan sudut rotasi dalam derajat untuk memutar teks sesuai kebutuhan Anda. Silakan periksa skenario berbeda berikut, di mana Anda dapat menerapkan rotasi teks.

## Menerapkan Rotasi menggunakan TextFragment dan TextBuilder

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void ImplementRotationUsingTextFragmentAndTextBuilder() {

    String _dataDir("C:\\Samples\\");

    // Inisialisasi objek dokumen
    auto document = MakeObject<Document>();
    // Dapatkan halaman tertentu
    auto page = document->get_Pages()->Add();
    // Buat fragmen teks
    auto textFragment1 = MakeObject<TextFragment>("teks utama");
    textFragment1->set_Position(MakeObject<Position>(100, 600));

    // Atur properti teks
    textFragment1->get_TextState()->set_FontSize(12);
    textFragment1->get_TextState()->set_Font(FontRepository::FindFont(u"TimesNewRoman"));

    // Buat fragmen teks yang diputar
    auto textFragment2 = MakeObject<TextFragment>("teks diputar");
    textFragment2->set_Position(MakeObject<Position>(200, 600));
    // Atur properti teks
    textFragment2->get_TextState()->set_FontSize(12);
    textFragment2->get_TextState()->set_Font(FontRepository::FindFont(u"TimesNewRoman"));
    textFragment2->get_TextState()->set_Rotation(45);

    // Buat fragmen teks yang diputar
    auto textFragment3 = MakeObject<TextFragment>("teks diputar");
    textFragment3->set_Position(MakeObject<Position>(300, 600));

    // Atur properti teks
    textFragment3->get_TextState()->set_FontSize(12);
    textFragment3->get_TextState()->set_Font(FontRepository::FindFont(u"TimesNewRoman"));
    textFragment3->get_TextState()->set_Rotation(90);

    // buat objek TextBuilder
    auto textBuilder = MakeObject<TextBuilder>(page);
    // Tambahkan fragmen teks ke halaman PDF
    textBuilder->AppendText(textFragment1);
    textBuilder->AppendText(textFragment2);
    textBuilder->AppendText(textFragment3);

    // Simpan dokumen
    document->Save(_dataDir + u"TextFragmentTests_Rotated1_out.pdf");
}
```

## Menerapkan Rotasi menggunakan TextParagraph dan TextBuilder (Fragmen yang Diputar)

```cpp
void ImplementRotationUsingTextParagraphAndTextBuilder_RotatedFragments() {

    String _dataDir("C:\\Samples\\");

    // Inisialisasi objek dokumen
    auto document = MakeObject<Document>();
    // Dapatkan halaman tertentu
    auto page = document->get_Pages()->Add();
    auto paragraph = MakeObject<TextParagraph>();
    paragraph->set_Position(MakeObject<Position>(200, 600));

    // Buat fragmen teks
    auto textFragment1 = MakeObject<TextFragment>("teks yang diputar");
    // Tetapkan properti teks
    textFragment1->get_TextState()->set_FontSize(12);
    textFragment1->get_TextState()->set_Font(FontRepository::FindFont(u"TimesNewRoman"));
    // Tetapkan rotasi
    textFragment1->get_TextState()->set_Rotation(45);

    // Buat fragmen teks
    auto textFragment2 = MakeObject<TextFragment>("teks utama");
    // Tetapkan properti teks
    textFragment2->get_TextState()->set_FontSize(12);
    textFragment2->get_TextState()->set_Font(FontRepository::FindFont(u"TimesNewRoman"));

    // Buat fragmen teks
    auto textFragment3 = MakeObject<TextFragment>("teks lain yang diputar");
    // Tetapkan properti teks
    textFragment3->get_TextState()->set_FontSize(12);
    textFragment3->get_TextState()->set_Font(FontRepository::FindFont(u"TimesNewRoman"));
    // Tetapkan rotasi
    textFragment3->get_TextState()->set_Rotation(-45);

    // Tambahkan fragmen teks ke paragraf
    paragraph->AppendLine(textFragment1);
    paragraph->AppendLine(textFragment2);
    paragraph->AppendLine(textFragment3);
    // Buat objek TextBuilder
    auto textBuilder = MakeObject<TextBuilder>(page);
    // Tambahkan paragraf teks ke halaman PDF
    textBuilder->AppendParagraph(paragraph);
    // Simpan dokumen
    document->Save(_dataDir + u"TextFragmentTests_Rotated2_out.pdf");

}
```

## Menerapkan Rotasi menggunakan TextFragment dan Page.Paragraphs

```cpp
void ImplementRotationUsingTextFragmentAndPageParagraphs() {

    String _dataDir("C:\\Samples\\");

    // Inisialisasi objek dokumen
    auto document = MakeObject<Document>();
    // Dapatkan halaman tertentu
    auto page = document->get_Pages()->Add();
    // Buat fragmen teks
    auto textFragment1 = MakeObject<TextFragment>("teks utama");
    // Tetapkan properti teks
    textFragment1->get_TextState()->set_FontSize(12);
    textFragment1->get_TextState()->set_Font(FontRepository::FindFont(u"TimesNewRoman"));

    // Buat fragmen teks
    auto textFragment2 = MakeObject<TextFragment>("teks yang diputar");

    // Tetapkan properti teks
    textFragment2->get_TextState()->set_FontSize(12);
    textFragment2->get_TextState()->set_Font(FontRepository::FindFont(u"TimesNewRoman"));

    // Tetapkan rotasi
    textFragment2->get_TextState()->set_Rotation(315);

    // Buat fragmen teks
    auto textFragment3 = MakeObject<TextFragment>("teks yang diputar");
    // Tetapkan properti teks
    textFragment3->get_TextState()->set_FontSize(12);
    textFragment3->get_TextState()->set_Font(FontRepository::FindFont(u"TimesNewRoman"));

    // Tetapkan rotasi
    textFragment3->get_TextState()->set_Rotation(270);
    page->get_Paragraphs()->Add(textFragment1);
    page->get_Paragraphs()->Add(textFragment2);
    page->get_Paragraphs()->Add(textFragment3);

    // Simpan dokumen
    document->Save(_dataDir + u"TextFragmentTests_Rotated3_out.pdf");
}
```

## Implementasikan Rotasi menggunakan TextParagraph dan TextBuilder (Seluruh Paragraf Diputar)

```cpp
void ImplementRotationUsingTextParagraphAndTextBuilder() {

    String _dataDir("C:\\Samples\\");

    // Inisialisasi objek dokumen
    auto document = MakeObject<Document>();
    // Dapatkan halaman tertentu
    auto page = document->get_Pages()->Add();
    for (int i = 0; i < 4; i++) {
        auto paragraph = MakeObject<TextParagraph>();
        paragraph->set_Position(MakeObject<Position>(200, 600));
        // Tentukan rotasi
        paragraph->set_Rotation(i * 90 + 45);
        // Buat fragmen teks
        auto textFragment1 = MakeObject<TextFragment>("Teks Paragraf");
        // Buat fragmen teks
        textFragment1->get_TextState()->set_FontSize(12);
        textFragment1->get_TextState()->set_Font(FontRepository::FindFont(u"TimesNewRoman"));
        textFragment1->get_TextState()->set_BackgroundColor(Color::get_LightGray());
        textFragment1->get_TextState()->set_ForegroundColor(Color::get_Blue());

        // Buat fragmen teks
        auto textFragment2 = MakeObject<TextFragment>("Baris kedua dari teks");
        // Atur properti teks
        textFragment2->get_TextState()->set_FontSize(12);
        textFragment2->get_TextState()->set_Font(FontRepository::FindFont(u"TimesNewRoman"));
        textFragment2->get_TextState()->set_BackgroundColor(Color::get_LightGray());
        textFragment2->get_TextState()->set_ForegroundColor(Color::get_Blue());

        // Buat fragmen teks
        auto textFragment3 = MakeObject<TextFragment>("Dan beberapa teks lagi...");
        // Atur properti teks
        textFragment3->get_TextState()->set_FontSize(12);
        textFragment3->get_TextState()->set_Font(FontRepository::FindFont(u"TimesNewRoman"));
        textFragment3->get_TextState()->set_BackgroundColor(Color::get_LightGray());
        textFragment3->get_TextState()->set_ForegroundColor(Color::get_Blue());
        textFragment3->get_TextState()->set_Underline(true);

        paragraph->AppendLine(textFragment1);
        paragraph->AppendLine(textFragment2);
        paragraph->AppendLine(textFragment3);
        // Buat objek TextBuilder
        auto textBuilder = MakeObject<TextBuilder>(page);
        // Tambahkan fragmen teks ke halaman PDF
        textBuilder->AppendParagraph(paragraph);
    }
    // Simpan dokumen
    document->Save(_dataDir + u"TextFragmentTests_Rotated4_out.pdf");
}
```