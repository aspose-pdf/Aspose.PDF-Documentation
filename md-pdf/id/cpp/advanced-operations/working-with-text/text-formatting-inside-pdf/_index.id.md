---

title: Pemformatan Teks di dalam PDF menggunakan C++
linktitle: Pemformatan Teks di dalam PDF
type: docs
weight: 30
url: /cpp/text-formatting-inside-pdf/
description: Halaman ini menjelaskan bagaimana memformat teks di dalam file PDF Anda. Ada penambahan indentasi baris, penambahan batas teks, penambahan garis bawah teks, penambahan batas di sekitar teks yang ditambahkan, penyelarasan teks untuk konten kotak mengambang, dan lain-lain.
lastmod: "2021-12-13"
sitemap:
    changefreq: "weekly"
    priority: 0.7

## Cara menambahkan Indentasi Baris ke PDF

Untuk menambahkan indentasi baris ke PDF Aspose.PDF untuk C++ menggunakan properti [SubsequentLinesIndent](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_formatting_options#a89b064ab1f39d56040625d7d98194ad3) dalam kelas [TextFormattingOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_formatting_options/) dan juga membantu koleksi [TextFragment](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_fragment/) dan [Paragraphs](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.paragraphs).



Silakan gunakan potongan kode berikut untuk menggunakan properti:

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void AddLineIndent() {

    String _dataDir("C:\\Samples\\");

    // String untuk nama file keluaran
    String outputFileName("SubsequentIndent_out.pdf");


    // Buat objek dokumen baru
    auto document = MakeObject<Document>();
    auto page = document->get_Pages()->Add();

    auto text = MakeObject<TextFragment>("Seekor rubah coklat cepat melompati anjing malas. Seekor rubah coklat cepat melompati anjing malas. Seekor rubah coklat cepat melompati anjing malas. Seekor rubah coklat cepat melompati anjing malas. Seekor rubah coklat cepat melompati anjing malas. Seekor rubah coklat cepat melompati anjing malas. Seekor rubah coklat cepat melompati anjing malas. Seekor rubah coklat cepat melompati anjing malas.");

    // Inisialisasi TextFormattingOptions untuk fragmen teks dan tentukan nilai SubsequentLinesIndent

    text->get_TextState()->set_FormattingOptions(MakeObject<Aspose::Pdf::Text::TextFormattingOptions>());
    text->get_TextState()->get_FormattingOptions()->set_SubsequentLinesIndent(20);

    page->get_Paragraphs()->Add(text);

    text = MakeObject<Aspose::Pdf::Text::TextFragment>(u"Baris2");
    page->get_Paragraphs()->Add(text);

    text = MakeObject<Aspose::Pdf::Text::TextFragment>(u"Baris3");
    page->get_Paragraphs()->Add(text);

    text = MakeObject<Aspose::Pdf::Text::TextFragment>(u"Baris4");
    page->get_Paragraphs()->Add(text);

    text = MakeObject<Aspose::Pdf::Text::TextFragment>(u"Baris5");
    page->get_Paragraphs()->Add(text);

    document->Save(_dataDir + outputFileName);

}
```

## Cara Menambahkan Batas Teks

Cuplikan kode berikut menunjukkan, bagaimana menambahkan batas ke teks menggunakan TextBuilder dan mengatur properti DrawTextRectangleBorder dari [TextState](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_state)

```cpp
void AddTextBorder() {

    String _dataDir("C:\\Samples\\");

    // String untuk nama file keluaran
    String outputFileName("PDFWithTextBorder_out.pdf");

    // Buat objek dokumen baru
    auto document = MakeObject<Document>();
    // Dapatkan halaman tertentu
    auto page = document->get_Pages()->Add();

    // Buat fragmen teks
    auto textFragment = MakeObject<TextFragment>("main text");
    textFragment->set_Position(MakeObject<Position>(100, 600));

    // Atur properti teks
    textFragment->get_TextState()->set_FontSize(12);
    textFragment->get_TextState()->set_Font(FontRepository::FindFont(u"DejaVu Serif"));
    textFragment->get_TextState()->set_BackgroundColor(Color::get_LightGray());
    textFragment->get_TextState()->set_ForegroundColor(Color::get_Red());
    // Atur properti StrokingColor untuk menggambar batas (stroking) di sekitar teks
    // persegi panjang
    textFragment->get_TextState()->set_StrokingColor(Color::get_DarkRed());
    // Atur nilai properti DrawTextRectangleBorder menjadi true
    textFragment->get_TextState()->set_DrawTextRectangleBorder(true);
    auto tb = MakeObject<TextBuilder>(page);
    tb->AppendText(textFragment);
    // Simpan dokumen
    document->Save(_dataDir + outputFileName);
}
```

## Cara Menambahkan Teks Garis Bawah

Cuplikan kode berikut menunjukkan cara menambahkan teks garis bawah saat membuat file PDF baru.

```cpp
void AddUnderlineText() {
    String _dataDir("C:\\Samples\\");

    // String untuk nama file output
    String outputFileName("AddUnderlineText_out.pdf");

    // Buat objek dokumen baru
    auto document = MakeObject<Document>();
    // Dapatkan halaman tertentu
    auto page = document->get_Pages()->Add();

    // TextFragment dengan teks contoh
    auto fragment = MakeObject<TextFragment>("Teks dengan dekorasi garis bawah");
    // Atur font untuk TextFragment
    fragment->get_TextState()->set_Font(FontRepository::FindFont(u"DejaVu Serif"));
    fragment->get_TextState()->set_FontSize(10);

    // Atur pemformatan teks sebagai Garis Bawah
    fragment->get_TextState()->set_Underline(true);

    // Tentukan posisi di mana TextFragment perlu ditempatkan
    fragment->set_Position(MakeObject<Position>(10, 800));

    auto tb = MakeObject<TextBuilder>(page);
    // Tambahkan TextFragment ke file PDF
    tb->AppendText(fragment);

    // Simpan dokumen PDF yang dihasilkan.
    document->Save(_dataDir + outputFileName);
}
```

## Cara Menambahkan Batas di Sekitar Teks yang Ditambahkan

Anda memiliki kendali atas tampilan dan nuansa teks yang Anda tambahkan. Contoh di bawah ini menunjukkan cara menambahkan batas di sekitar sepotong teks yang Anda tambahkan dengan menggambar persegi panjang di sekitarnya. Cari tahu lebih lanjut tentang kelas [PdfContentEditor](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.facades.pdf_content_editor/).

```cpp
void AddBorderAroundAddedText() {

    String _dataDir("C:\\Samples\\");

    // String untuk nama file input
    String inputFileName("sample.pdf");

    // String untuk nama file output
    String outputFileName("AddingBorderAroundAddedText_out.pdf");

    auto editor = MakeObject<Aspose::Pdf::Facades::PdfContentEditor>();

    editor->BindPdf(_dataDir + inputFileName);
    auto lineInfo = MakeObject<Aspose::Pdf::Facades::LineInfo>();

    lineInfo->set_LineWidth(2);
    lineInfo->set_VerticeCoordinate(MakeArray<float>({ 0, 0, 100, 100, 50, 100 }));
    lineInfo->set_Visibility(true);
    auto rect = MakeObject<System::Drawing::Rectangle>(0, 0, 0, 0);
    editor->CreatePolygon(lineInfo, 1, System::Drawing::Rectangle(0, 0, 0, 0), String::Empty);

    // Simpan dokumen PDF yang dihasilkan.
    editor->Save(_dataDir + outputFileName);
}
```

## Cara Menambahkan NewLine Feed

Untuk menambahkan teks dengan line feed, silakan gunakan [TextFragment](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_fragment) dengan [TextParagraph](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_paragraph).

Cuplikan kode berikut menunjukkan cara menambahkan NewLine feed dalam file PDF Anda:

```cpp
void AddNewLineFeed() {
    String _dataDir("C:\\Samples\\");

    // String untuk nama file output
    String outputFileName("AddNewLineFeed_out.pdf");

    // Buat objek dokumen baru
    auto document = MakeObject<Document>();
    // Dapatkan halaman tertentu
    auto page = document->get_Pages()->Add();

    // Inisialisasi TextFragment baru dengan teks yang berisi penanda newline yang diperlukan
    auto textFragment = MakeObject<TextFragment>("Nama Pemohon: \r\n Joe Smoe");

    // Atur properti teks fragment jika perlu
    textFragment->get_TextState()->set_FontSize(12);
    textFragment->get_TextState()->set_Font(FontRepository::FindFont(u"DejaVu Serif"));
    textFragment->get_TextState()->set_BackgroundColor(Color::get_LightGray());
    textFragment->get_TextState()->set_ForegroundColor(Color::get_Red());

    // Buat objek TextParagraph
    auto par = MakeObject<TextParagraph>();

    // Tambahkan TextFragment baru ke paragraf
    par->AppendLine(textFragment);

    // Atur posisi paragraf
    par->set_Position(MakeObject<Position>(100, 600));

    // Buat objek TextBuilder
    auto textBuilder = new TextBuilder(page);
    // Tambahkan TextParagraph menggunakan TextBuilder
    textBuilder->AppendParagraph(par);

    // Simpan dokumen PDF yang dihasilkan.
    document->Save(_dataDir + outputFileName);
}
```

## Cara Menambahkan Teks Coret

Anda dapat menggunakan kelas [TextState](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_state) untuk mengatur pemformatan teks seperti Bold, Italic, Underline, dan juga, API telah menyediakan kemampuan untuk menandai pemformatan teks sebagai Coret.

Silakan coba gunakan potongan kode berikut untuk menambahkan TextFragment dengan pemformatan Coret.

```cpp
void AddStrikeOutText() {
    String _dataDir("C:\\Samples\\");

    // String untuk nama file keluaran
    String outputFileName("AddStrikeOutText_out.pdf");

    // Buka dokumen
    auto document = MakeObject<Document>();
    // Dapatkan halaman tertentu
    auto page = document->get_Pages()->Add();

    // Buat fragmen teks
    auto textFragment = MakeObject<TextFragment>("main text");
    textFragment->set_Position(MakeObject<Position>(100, 600));

    // Atur properti teks
    textFragment->get_TextState()->set_FontSize(12);
    textFragment->get_TextState()->set_Font(FontRepository::FindFont(u"DejaVu Serif"));
    textFragment->get_TextState()->set_BackgroundColor(Color::get_LightGray());
    textFragment->get_TextState()->set_ForegroundColor(Color::get_Red());
    // Atur properti Coret
    textFragment->get_TextState()->set_StrikeOut(true);
    // Tandai teks sebagai Bold
    textFragment->get_TextState()->set_FontStyle(FontStyles::Bold);

    // Buat objek TextBuilder
    auto textBuilder = MakeObject<TextBuilder>(page);
    // Tambahkan fragmen teks ke halaman PDF
    textBuilder->AppendText(textFragment);

    // Simpan dokumen PDF yang dihasilkan.
    document->Save(_dataDir + outputFileName);
}
```

## Terapkan Gradasi Bayangan pada Teks

Kelas [Aspose.Pdf.Color](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.color) telah ditingkatkan lebih lanjut dengan memperkenalkan properti baru dari [PatternColorSpace](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.color#a8be6d8ab626d2ba6935a13a9c5b0de54), yang dapat digunakan untuk menentukan warna gradasi untuk teks. Properti baru ini menambahkan berbagai Gradasi Bayangan pada teks seperti Axial Shading, Radial (Type 3) Shading seperti yang ditunjukkan dalam cuplikan kode berikut:

```cpp
void ApplyGradientShading() {

    String _dataDir("C:\\Samples\\");

    // String untuk nama file input
    String inputFileName("sample.pdf");

    // String untuk nama file output
    String outputFileName("ApplyGradientShading_out.pdf");

    // Buka dokumen
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    auto absorber = MakeObject<TextFragmentAbsorber>("always print correctly");

    document->get_Pages()->Accept(absorber);

    auto textFragment = absorber->get_TextFragments()->idx_get(1);

    auto foregroundColor = MakeObject<Aspose::Pdf::Color>();
    foregroundColor->set_PatternColorSpace(MakeObject<Aspose::Pdf::Drawing::GradientAxialShading>(Color::get_Red(), Color::get_Blue()));

    // Buat warna baru dengan pola colorspace
    textFragment->get_TextState()->set_ForegroundColor(foregroundColor);

    textFragment->get_TextState()->set_Underline(true);

    document->Save(_dataDir + outputFileName);

}
```

>Untuk menerapkan Gradien Radial, Anda dapat mengatur properti 'PatternColorSpace' sama dengan 'Aspose.Pdf.Drawing.GradientRadialShading(startingColor, endingColor)' dalam cuplikan kode di atas.

## Cara menyelaraskan teks ke konten mengambang

Aspose.PDF mendukung pengaturan penjajaran teks untuk konten di dalam elemen Floating Box. Properti penjajaran dari instance [Aspose.Pdf.FloatingBox](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.floating_box) dapat digunakan untuk mencapai ini seperti yang ditunjukkan dalam contoh kode berikut.

```cpp
void ApplyGradientShadingRadial() {

    String _dataDir("C:\\Samples\\");

    // String untuk nama file input
    String inputFileName("sample.pdf");

    // String untuk nama file output
    String outputFileName("ApplyGradientShadingRadial_out.pdf");

    auto document = MakeObject<Document>(_dataDir + inputFileName);

    auto absorber = MakeObject<TextFragmentAbsorber>(u"always print correctly");
    document->get_Pages()->Accept(absorber);

    auto textFragment = absorber->get_TextFragments()->idx_get(1);

    auto foregroundColor = MakeObject<Aspose::Pdf::Color>();
    foregroundColor->set_PatternColorSpace(MakeObject<Aspose::Pdf::Drawing::GradientRadialShading>(Color::get_Red(), Color::get_Blue()));

    // Buat warna baru dengan ruang warna pola
    textFragment->get_TextState()->set_ForegroundColor(foregroundColor);

    textFragment->get_TextState()->set_Underline(true);

    document->Save(_dataDir + outputFileName);
}
```