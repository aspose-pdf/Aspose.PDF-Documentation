---
title: Tambahkan Teks ke PDF menggunakan C++
linktitle: Tambahkan Teks ke PDF
type: docs
weight: 10
url: /cpp/add-text-to-pdf-file/
description: Artikel ini menjelaskan berbagai aspek bekerja dengan teks di Aspose.PDF. Pelajari cara menambahkan teks ke PDF, menambahkan fragmen HTML, atau menggunakan font OTF kustom.
lastmod: "2021-12-10"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Menambahkan Teks

Untuk menambahkan teks ke file PDF yang sudah ada:

1. Buka PDF input menggunakan objek Document.
2. Dapatkan halaman tertentu di mana Anda ingin menambahkan teks.
3. Buat objek TextFragment dengan teks input bersama dengan properti teks lainnya. Objek TextBuilder yang dibuat dari halaman tertentu – di mana Anda ingin menambahkan teks – memungkinkan Anda untuk menambahkan objek TextFragment ke halaman menggunakan metode AppendText.
4. Panggil metode Save dari objek Document dan simpan file PDF keluaran.

Cuplikan kode berikut menunjukkan cara menambahkan teks dalam file PDF yang sudah ada.

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void AddingText() {
    
    String _dataDir("C:\\Samples\\");

    // String untuk nama file input
    String inputFileName("sample.pdf");
    // String untuk nama file output
    String outputFileName("AddingText_out.pdf");

    // Muat file PDF
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // dapatkan halaman tertentu
    auto pdfPage = document->get_Pages()->idx_get(1);

    // buat text fragment
    auto textFragment = MakeObject<TextFragment>("Aspose.PDF");
    textFragment->set_Position(MakeObject<Position>(80, 700));

    // atur properti teks
    textFragment->get_TextState()->set_Font(FontRepository::FindFont(u"Verdana"));
    textFragment->get_TextState()->set_FontSize(14);
    textFragment->get_TextState()->set_ForegroundColor(Color::get_Blue());
    textFragment->get_TextState()->set_BackgroundColor(Color::get_LightGray());

    // buat objek TextBuilder
    auto textBuilder = MakeObject<TextBuilder>(pdfPage);
    // tambahkan text fragment ke halaman PDF
    textBuilder->AppendText(textFragment);

    // Simpan dokumen PDF yang dihasilkan.
    document->Save(_dataDir + outputFileName);
}
```

## Memuat Font dari Stream

Cuplikan kode berikut menunjukkan cara memuat Font dari objek Stream ketika menambahkan teks ke dokumen PDF.

```cpp
void LoadingFontFromStream() {

    String _dataDir("C:\\Samples\\");
    String inputFileName("sample.pdf");
    String outputFileName("LoadingFontFromStream_out.pdf");

    String fontFile("C:\\Windows\\Fonts\\Arial.ttf");

    // Muat file PDF input
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // Buat objek pembangun teks untuk halaman pertama dokumen
    auto textBuilder = MakeObject<TextBuilder>(document->get_Pages()->idx_get(1));
    // Buat fragmen teks dengan string contoh
    auto textFragment = MakeObject<TextFragment>("Hello world");

    if (!fontFile.IsNullOrEmpty()) {
        // Muat font TrueType ke dalam objek stream
        auto fontStream = System::IO::File::OpenRead(fontFile);
        // Tetapkan nama font untuk string teks
        textFragment->get_TextState()->set_Font(FontRepository::OpenFont(fontStream, FontTypes::TTF));
        // Tentukan posisi untuk Fragmen Teks
        textFragment->set_Position(MakeObject<Position>(10, 10));
        // Tambahkan teks ke TextBuilder sehingga dapat ditempatkan di atas file PDF
        textBuilder->AppendText(textFragment);

        // Simpan dokumen PDF hasil.
        document->Save(_dataDir + outputFileName);
    }
}
```

## Tambahkan Teks menggunakan TextParagraph

Cuplikan kode berikut menunjukkan cara menambahkan teks dalam dokumen PDF menggunakan kelas [TextParagraph](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_paragraph).

```cpp
void AddTextUsingTextParagraph() {

    String _dataDir("C:\\Samples\\");

    // Buka dokumen
    auto document = MakeObject<Document>();

    String outputFileName("AddTextUsingTextParagraph_out.pdf");

    // Tambahkan halaman ke koleksi halaman dari objek Dokumen
    auto page = document->get_Pages()->Add();
    auto builder = MakeObject<TextBuilder>(page);

    // Buat paragraf teks
    auto paragraph = MakeObject<TextParagraph>();

    // Atur indentasi baris berikutnya
    paragraph->set_SubsequentLinesIndent(20);

    // Tentukan lokasi untuk menambahkan TextParagraph
    paragraph->set_Rectangle(MakeObject<Rectangle>(100, 300, 200, 700));

    // Tentukan mode pembungkusan kata
    paragraph->get_FormattingOptions()->set_WrapMode(TextFormattingOptions::WordWrapMode::ByWords);

    // Buat fragmen teks
    auto fragment1 = MakeObject<TextFragment>("the quick brown fox jumps over the lazy dog");
    fragment1->get_TextState()->set_Font(FontRepository::FindFont(u"Times New Roman"));
    fragment1->get_TextState()->set_FontSize(12);
    // Tambahkan fragmen ke paragraf
    paragraph->AppendLine(fragment1);
    // Tambahkan paragraf
    builder->AppendParagraph(paragraph);

    // Simpan dokumen PDF yang dihasilkan.
    document->Save(_dataDir + outputFileName);
}

```

## Tambahkan Hyperlink ke TextSegment

Halaman PDF dapat terdiri dari satu atau lebih objek TextFragment, di mana setiap objek TextFragment dapat memiliki satu atau lebih instance TextSegment. Untuk menetapkan hyperlink pada TextSegment, properti Hyperlink dari kelas [TextSegment](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_segment) dapat digunakan dengan menyediakan objek dari instance Aspose.Pdf.WebHyperlink. Silakan coba gunakan potongan kode berikut untuk memenuhi persyaratan ini.

```cpp
void AddHyperlinkToTextSegment() {
    
    String _dataDir("C:\\Samples\\");
    String outputFileName("AddHyperlinkToTextSegment_out.pdf");

    // Buat instance dokumen
    auto document = MakeObject<Document>();

    // Tambahkan halaman ke koleksi halaman file PDF
    auto page1 = document->get_Pages()->Add();

    // Buat instance TextFragment
    auto tf = MakeObject<TextFragment>("Sample Text Fragment");
    // Atur perataan horizontal untuk TextFragment
    tf->set_HorizontalAlignment(HorizontalAlignment::Right);

    // Buat textsegment dengan teks contoh
    auto segment = MakeObject<TextSegment>(" ... Text Segment 1...");
    // Tambahkan segment ke koleksi segment dari TextFragment
    tf->get_Segments()->Add(segment);

    // Buat TextSegment baru
    segment = MakeObject<TextSegment>("Link to Google");
    // Tambahkan segment ke koleksi segment dari TextFragment

    tf->get_Segments()->Add(segment);

    // Atur hyperlink untuk TextSegment
    segment->set_Hyperlink(MakeObject<Aspose::Pdf::WebHyperlink>("www.aspose.com"));

    // Atur warna depan untuk text segment
    segment->get_TextState()->set_ForegroundColor(Color::get_Blue());

    // Atur pemformatan teks sebagai miring
    segment->get_TextState()->set_FontStyle(FontStyles::Italic);

    // Buat objek TextSegment lainnya
    segment = MakeObject<TextSegment>(u"TextSegment tanpa hyperlink");

    // Tambahkan segment ke koleksi segment dari TextFragment
    tf->get_Segments()->Add(segment);

    // Tambahkan TextFragment ke koleksi paragraf dari objek halaman
    page1->get_Paragraphs()->Add(tf);

    // Simpan dokumen PDF yang dihasilkan.
    document->Save(_dataDir + outputFileName);

}
```

## Gunakan Font OTF

Aspose.PDF untuk C++ menawarkan fitur untuk menggunakan font Kustom/TrueType saat membuat/memanipulasi konten file PDF sehingga konten file ditampilkan menggunakan konten selain font sistem default.

```cpp
void UseOTFFont() {

    String _dataDir("C:\\Samples\\");
    String outputFileName("OTFFont_out.pdf");

    // Buat instance dokumen baru
    auto document = MakeObject<Document>();

    // Tambahkan halaman ke koleksi halaman file PDF
    auto page = document->get_Pages()->Add();

    // Buat instansi TextFragment dengan teks sampel
    auto fragment = MakeObject<TextFragment>("Teks Sampel dalam font OTF");

    // Atau Anda bahkan dapat menentukan jalur font OTF di direktori sistem
    fragment->get_TextState()->set_Font(FontRepository::OpenFont(u"C:\\Samples\\Fonts\\Montserrat-Black.otf"));
    // Tentukan untuk menyematkan font di dalam file PDF, sehingga ditampilkan dengan benar,
    // Meskipun font tertentu tidak terinstal/ada di mesin target
    fragment->get_TextState()->get_Font()->set_IsEmbedded(true);
    // Tambahkan TextFragment ke koleksi paragraf dari instansi Page
    page->get_Paragraphs()->Add(fragment);
    // Simpan dokumen PDF yang dihasilkan.
    document->Save(_dataDir + outputFileName);
}
```

## Menambahkan String HTML menggunakan DOM

Kelas Aspose.Pdf.Generator.Text mengandung properti bernama IsHtmlTagSupported yang memungkinkan untuk menambahkan tag/konten HTML ke dalam file PDF. Konten yang ditambahkan dirender dalam tag HTML asli alih-alih muncul sebagai string teks sederhana. Untuk mendukung fitur serupa dalam Model Objek Dokumen (DOM) baru dari namespace Aspose.Pdf, kelas HtmlFragment telah diperkenalkan.

Instans [HtmlFragment](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.html_fragment) dapat digunakan untuk menentukan konten HTML yang harus ditempatkan di dalam file PDF. Mirip dengan TextFragment, HtmlFragment adalah objek tingkat paragraf dan dapat ditambahkan ke koleksi paragraf objek Page. Cuplikan kode berikut menunjukkan langkah-langkah untuk menempatkan konten HTML di dalam file PDF menggunakan pendekatan DOM.

```cpp
void AddingHtmlString() {
    
    String _dataDir("C:\\Samples\\");

    // String untuk nama file input
    String inputFileName("sample.pdf");

    // String untuk nama file output
    String outputFileName("sample_html_out.pdf");

    // membuat instans Document
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // Tambahkan halaman ke koleksi halaman file PDF
    auto page = document->get_Pages()->Add();

    // Instansiasi HtmlFragment dengan konten HTML
    auto title = MakeObject<HtmlFragment>("<h1 style=\"color:blue\"><strong>HTML String Demo</strong></h1>");

    // set MarginInfo untuk detail margin
    auto margin = MakeObject<MarginInfo>();
    margin->set_Bottom(10);
    margin->set_Top(200);
    // Tetapkan informasi margin
    title->set_Margin(margin);

    // Tambahkan HTML Fragment ke koleksi paragraf halaman
    page->get_Paragraphs()->Add(title);
    // Simpan file PDF
    document->Save(_dataDir + outputFileName);
}
```

Berikut adalah cuplikan kode yang mendemonstrasikan langkah-langkah bagaimana menambahkan daftar berurutan HTML ke dalam dokumen:

```cpp
void AddHTMLOrderedListIntoDocuments() {
    
    String _dataDir("C:\\Samples\\");

    // String untuk nama file output
    String outputFileName("AddHTMLOrderedListIntoDocuments_out.pdf");

    // Membuat objek Document    
    auto document = MakeObject<Document>();

    // Membuat objek HtmlFragment dengan fragmen HTML yang sesuai
    auto htmlFragment = MakeObject<HtmlFragment>(
        "<div style=\"font-family: sans-serif\"><ul><li>Pertama</li><li>Kedua</li><li>Ketiga</li><li>Keempat</li><li>Kelima</li></ul><p>Teks setelah daftar.</p><p>Baris berikutnya<br/>Baris terakhir</p></div>");
    // Tambahkan Halaman dalam Koleksi Halaman
    auto page = document->get_Pages()->Add();

    // Tambahkan HtmlFragment di dalam halaman
    page->get_Paragraphs()->Add(htmlFragment);

    // Simpan file PDF hasil
    document->Save(_dataDir + outputFileName);
}
```

Anda juga dapat mengatur pemformatan string HTML menggunakan objek TextState sebagai berikut:

```cpp
void AddHTMLStringFormatting() {
    
    String _dataDir("C:\\Samples\\");

    // String untuk nama file output
    String outputFileName("sample_html_out.pdf");

    // Membuat objek Document    
    auto document = MakeObject<Document>();

    // Tambahkan Halaman dalam Koleksi Halaman
    auto page = document->get_Pages()->Add();

    // Membuat HtmlFragment dengan konten HTML
    auto title = MakeObject<HtmlFragment>("<h1><strong>Demo String HTML</strong></h1>");

    auto textState = MakeObject<TextState>(12);

    textState->set_Font(FontRepository::FindFont(u"Calibri"));
    textState->set_ForegroundColor(Color::get_Green());
    textState->set_BackgroundColor(Color::get_Coral());
    title->set_TextState(textState);

    // Tambahkan Fragmen HTML ke koleksi paragraf halaman
    page->get_Paragraphs()->Add(title);
    // Simpan file PDF
    document->Save(_dataDir + outputFileName);
}

```

Jika Anda menetapkan beberapa nilai atribut teks melalui markup HTML dan kemudian memberikan nilai yang sama dalam properti TextState, mereka akan menimpa parameter HTML dengan bentuk properti dari instance TextState. Cuplikan kode berikut menunjukkan perilaku yang dijelaskan.

```cpp
void AddHTMLUsingDOMAndOverwrite() {

    String _dataDir("C:\\Samples\\");
    // String untuk nama file keluaran
    String outputFileName("AddHTMLUsingDOMAndOverwrite_out.pdf");

    // Instansiasi objek Document    
    auto document = MakeObject<Document>();

    // Tambahkan Halaman dalam Koleksi Halaman
    auto page = document->get_Pages()->Add();

    // Instansiasi HtmlFragment dengan konten HTML
    auto title = MakeObject<HtmlFragment>("<p style='font-family: Verdana'><b><i>Table contains text</i></b></p>");

    // Font-family dari 'Verdana' akan direset menjadi 'Arial'
    title->set_TextState(new TextState(u"Arial Black"));
    title->set_TextState(new TextState(20));

    // Atur informasi margin bawah
    title->get_Margin()->set_Bottom(10);
    // Atur informasi margin atas
    title->get_Margin()->set_Top(400);
    // Tambahkan Fragmen HTML ke koleksi paragraf halaman
    page->get_Paragraphs()->Add(title);
    // Simpan file PDF
    document->Save(_dataDir + outputFileName);
}
```

## Catatan Kaki dan Catatan Akhir (DOM)

Catatan Kaki menunjukkan catatan dalam teks makalah Anda dengan menggunakan angka superskrip berurutan. Catatan sebenarnya diindentasi dan dapat terjadi sebagai catatan kaki di bagian bawah halaman.

### Menambahkan Catatan Kaki

Dalam sistem referensi catatan kaki, tunjukkan referensi dengan:

- meletakkan angka kecil di atas garis jenis tepat setelah bahan sumber. Angka ini disebut sebagai pengenal catatan. Angka ini berada sedikit di atas garis teks.
- meletakkan angka yang sama, diikuti oleh kutipan dari sumber Anda, di bagian bawah halaman. Pencatatan kaki harus bersifat numerik dan kronologis: referensi pertama adalah 1, referensi kedua adalah 2, dan seterusnya.

Keuntungan dari pencatatan kaki adalah pembaca dapat dengan mudah melihat ke bagian bawah halaman untuk mengetahui sumber referensi yang menarik minat mereka.

Ikuti langkah-langkah berikut:

- Buat instance [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document)
- Buat objek [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page)

- Buat objek [TextFragment](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_fragment)
- Buat instance Catatan dan berikan nilainya ke properti TextFragment [FootNote](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_fragment#abe1663009fbceed84a0a392527463219)
- Tambahkan TextFragment ke koleksi paragraf dari sebuah instance halaman

```cpp
void AddFootNote() {
    
    String _dataDir("C:\\Samples\\");

    // String untuk nama file keluaran
    String inputFileName("sample.pdf");
    String outputFileName("sample_footnote_out.pdf");

    // Membuat objek Dokumen    
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // Tambahkan Halaman ke Koleksi Halaman
    auto page = document->get_Pages()->idx_get(1);

    auto tfa = MakeObject<TextFragmentAbsorber>("Portable Document Format");
    tfa->Visit(page);

    auto t = tfa->get_TextFragments()->idx_get(1);
    auto note = MakeObject<Note>();
    note->set_Text(u"Demo");
    t->set_FootNote(note);

    // buat instance TextFragment
    auto text = MakeObject<TextFragment>("Hello World");
    // atur nilai FootNote untuk TextFragment
    text->set_FootNote(MakeObject<Note>("catatan kaki untuk teks uji 1"));
    // tambahkan TextFragment ke koleksi paragraf dari halaman pertama dokumen
    page->get_Paragraphs()->Add(text);
    // buat TextFragment kedua
    text = MakeObject<TextFragment>("Aspose.Pdf for Java");
    // atur FootNote untuk fragmen teks kedua
    text->set_FootNote(MakeObject<Note>("catatan kaki untuk teks uji 2"));
    // tambahkan fragmen teks kedua ke koleksi paragraf dari file PDF
    page->get_Paragraphs()->Add(text);

    document->Save(_dataDir + outputFileName);
}
```

### Gaya garis khusus untuk Catatan Kaki

Contoh berikut menunjukkan bagaimana menambahkan Catatan Kaki ke bagian bawah halaman Pdf dan mendefinisikan gaya garis khusus.

```cpp
void CustomFootNote_Line() {
    
    String _dataDir("C:\\Samples\\");

    // String untuk nama file keluaran    
    String outputFileName("customFootNote_Line.pdf");

    // Buat instance Dokumen
    auto document = MakeObject<Document>();

    // tambahkan halaman ke koleksi halaman PDF
    auto page = document->get_Pages()->Add();
    
    // buat objek GraphInfo
    auto graph = MakeObject<GraphInfo>();
    // atur lebar garis sebagai 2
    graph->set_LineWidth(2);
    // atur warna untuk objek graph
    graph->set_Color(Color::get_Red());
    // atur nilai array dash sebagai 3
    graph->set_DashArray(MakeArray<int>(3));
    // atur nilai fase dash sebagai 1
    graph->set_DashPhase(1);
    // atur gaya garis catatan kaki untuk halaman sebagai graph
    page->set_NoteLineStyle(graph);

    // buat instance TextFragment
    auto text = MakeObject<TextFragment>("Hello World");
    // atur nilai Catatan Kaki untuk TextFragment
    text->set_FootNote(MakeObject<Note>("catatan kaki untuk teks uji 1"));
    // tambahkan TextFragment ke koleksi paragraf halaman pertama dokumen
    page->get_Paragraphs()->Add(text);
    // buat TextFragment kedua
    text = MakeObject<TextFragment>("Aspose.Pdf untuk Java");
    // atur Catatan Kaki untuk fragmen teks kedua
    text->set_FootNote(MakeObject<Note>("catatan kaki untuk teks uji 2"));
    // tambahkan fragmen teks kedua ke koleksi paragraf file PDF
    page->get_Paragraphs()->Add(text);
    // simpan file PDF
    document->Save(_dataDir + outputFileName);
}
```

Kami dapat mengatur pemformatan Label Catatan Kaki (pengidentifikasi catatan) menggunakan objek TextState sebagai berikut:

```csharp
void AddCustomFootNoteLabel() {
    
    String _dataDir("C:\\Samples\\");

    // String untuk nama file input    
    String inputFileName("sample.pdf");

    // String untuk nama file output    
    String outputFileName("sample_footnote.pdf");

    // Buat instance Dokumen
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    auto page = document->get_Pages()->idx_get(1);

    auto tfa = MakeObject<TextFragmentAbsorber>("Portable Document Format");
    tfa->Visit(page);

    auto t = tfa->get_TextFragments()->idx_get(1);
    auto note = MakeObject<Note>("Demo");
    t->set_FootNote(note);

    // buat instance TextFragment
    auto text = MakeObject<TextFragment>("Hello World");
    // set nilai FootNote untuk TextFragment
    text->set_FootNote(MakeObject<Note>("catatan kaki untuk teks uji 1"));
    text->get_FootNote()->set_Text(u"21");

    auto ts = MakeObject<TextState>();
    ts->set_ForegroundColor(Color::get_Blue());
    ts->set_FontStyle(FontStyles::Italic);
    text->get_FootNote()->set_TextState(ts);

    // tambahkan TextFragment ke koleksi paragraf halaman pertama dokumen
    page->get_Paragraphs()->Add(text);
    // buat TextFragment kedua
    text = MakeObject<TextFragment>(u"Aspose.Pdf for C++");
    // set FootNote untuk fragmen teks kedua
    text->set_FootNote(MakeObject<Note>("catatan kaki untuk teks uji 2"));
    // tambahkan fragmen teks kedua ke koleksi paragraf file PDF
    page->get_Paragraphs()->Add(text);

    document->Save(_dataDir + outputFileName);
}
```

### Sesuaikan Label Catatan Kaki

Secara default, nomor Catatan Kaki meningkat mulai dari 1. Namun, kita mungkin memiliki persyaratan untuk menetapkan label Catatan Kaki khusus. Untuk memenuhi persyaratan ini, silakan coba gunakan potongan kode berikut

```cpp
void CustomFootNote_Label() {

    String _dataDir("C:\\Samples\\");
    // String untuk nama file keluaran    
    String outputFileName("CustomizeFootNoteLabel_out.pdf");

    // Buat instance Dokumen
    auto document = MakeObject<Document>();

    // Tambahkan halaman ke koleksi halaman PDF
    auto page = document->get_Pages()->Add();

    // Buat objek GraphInfo
    auto graph = MakeObject<GraphInfo>();

    // Atur lebar garis sebagai 2
    graph->set_LineWidth(2);

    // Atur warna untuk objek grafis
    graph->set_Color(Color::get_Red());

    // Atur nilai array garis putus-putus sebagai 3
    graph->set_DashArray(MakeArray<int>(3));

    // Atur nilai fase garis putus-putus sebagai 1
    graph->set_DashPhase(1);

    // Atur gaya garis catatan kaki untuk halaman sebagai grafik
    page->set_NoteLineStyle(graph);

    // Buat instance TextFragment
    auto text = MakeObject<TextFragment>("Hello World");
    // Atur nilai Catatan Kaki untuk TextFragment
    text->set_FootNote(MakeObject<Note>("catatan kaki untuk teks uji 1"));
    // Tentukan label khusus untuk Catatan Kaki
    text->get_FootNote()->set_Text(u" Aspose(2021)");
    // Tambahkan TextFragment ke koleksi paragraf halaman pertama dokumen
    page->get_Paragraphs()->Add(text);

    document->Save(_dataDir + outputFileName);
}
```

## Menambahkan Gambar dan Tabel ke Catatan Kaki

Cuplikan kode berikut menunjukkan langkah-langkah untuk menambahkan [Catatan Kaki](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_fragment#a017ff999979d9f799b8e3cd32ab95722) ke objek [TextFragment](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_fragment) dan kemudian menambahkan objek Gambar dan Tabel ke koleksi paragraf dari bagian Catatan Kaki.

```cpp

void AddingImageAndTableToFootnote() {
    
    String _dataDir("C:\\Samples\\");

    // String untuk nama file keluaran    
    String outputFileName("AddImageAndTableToFootNote_out.pdf");

    // Membuat instance Document
    auto document = new Document();
    // Menambahkan halaman ke koleksi halaman PDF
    auto page = document->get_Pages()->Add();

    // Membuat instance TextFragment
    auto text = MakeObject<TextFragment>("Hello World");

    page->get_Paragraphs()->Add(text);

    text->set_FootNote(MakeObject<Note>());
    auto image = MakeObject<Image>();
    image->set_File(_dataDir + u"aspose-logo.jpg");
    image->set_FixHeight(20);

    text->get_FootNote()->get_Paragraphs()->Add(image);

    auto footNote = MakeObject<TextFragment>("teks catatan kaki");
    footNote->get_TextState()->set_FontSize(20);
    footNote->set_IsInLineParagraph(true);
    text->get_FootNote()->get_Paragraphs()->Add(footNote);
    
    auto table = MakeObject<Table>();
    table->get_Rows()->Add()->get_Cells()->Add()->get_Paragraphs()->Add(MakeObject<TextFragment>("Baris 1 Sel 1"));
    text->get_FootNote()->get_Paragraphs()->Add(table);

    page->get_Paragraphs()->Add(text);

    document->Save(_dataDir + outputFileName);
}
```

## Cara Membuat EndNote

EndNote adalah sitasi sumber yang mengarahkan pembaca ke tempat tertentu di akhir makalah di mana mereka dapat menemukan sumber informasi atau kata-kata yang dikutip atau disebutkan dalam makalah. Ketika menggunakan endnotes, kalimat yang Anda kutip atau parafrase atau materi yang diringkas diikuti oleh nomor superskrip.

Contoh berikut menunjukkan cara menambahkan Endnote pada halaman Pdf.

```cpp
void HowToCreateEndNotes() {
    
    String _dataDir("C:\\Samples\\");

    // String untuk nama file output    
    String outputFileName("endNote_out.pdf");

    // Buat instance Dokumen
    auto document = new Document();
    // Tambahkan halaman ke koleksi halaman PDF
    auto page = document->get_Pages()->Add();

    // buat instance TextFragment
    auto text = MakeObject<TextFragment>("Hello World");

    // setel nilai FootNote untuk TextFragment
    text->set_EndNote(MakeObject<Note>("contoh End note"));

    // tentukan label kustom untuk FootNote
    text->get_EndNote()->set_Text(u" Aspose(2021)");
    // tambahkan TextFragment ke koleksi paragraf halaman pertama dokumen
    page->get_Paragraphs()->Add(text);
    // simpan file PDF
    document->Save(_dataDir + outputFileName);
}
```

## Teks dan Gambar sebagai Paragraf Sejajar

Tata letak default dari file PDF adalah tata letak aliran (Kiri-Atas ke Kanan-Bawah). Oleh karena itu, setiap elemen baru yang ditambahkan ke file PDF ditambahkan dalam aliran kanan bawah. Namun, kita mungkin memiliki kebutuhan untuk menampilkan berbagai elemen halaman yaitu Gambar dan Teks pada tingkat yang sama (satu setelah yang lain). Salah satu pendekatan dapat membuat instance Tabel dan menambahkan kedua elemen ke objek sel individual. Namun, pendekatan lain dapat berupa paragraf sejajar. Dengan mengatur properti IsInLineParagraph dari Gambar dan Teks sebagai benar, paragraf ini akan muncul sebagai sejajar dengan elemen halaman lainnya.

Cuplikan kode berikut menunjukkan bagaimana menambahkan teks dan Gambar sebagai paragraf sejajar dalam file PDF.

```cpp
void TextAndImageAsInLineParagraph() {

    String _dataDir("C:\\Samples\\");
    String outputFileName("TextAndImageAsParagraph_out.pdf");

    // Membuat instance Dokumen
    auto document = MakeObject<Document>();

    // Tambahkan halaman ke koleksi halaman dari instance Dokumen
    auto page = document->get_Pages()->Add();

    // Buat TextFragment
    auto text = MakeObject<TextFragment>("Hello World.. ");
    // Tambahkan fragmen teks ke koleksi paragraf dari objek Halaman
    page->get_Paragraphs()->Add(text);

    // Buat instance gambar
    auto image = MakeObject<Image>();

    // Atur gambar sebagai paragraf sejajar sehingga muncul tepat setelah
    // Objek paragraf sebelumnya (TextFragment)
    image->set_IsInLineParagraph(true);

    // Tentukan jalur file gambar
    image->set_File(_dataDir + u"aspose-logo.jpg");
    // Atur tinggi gambar (opsional)
    image->set_FixHeight(30);
    // Atur lebar gambar (opsional)
    image->set_FixWidth(100);
    // Tambahkan gambar ke koleksi paragraf dari objek halaman
    page->get_Paragraphs()->Add(image);
    // Inisialisasi ulang objek TextFragment dengan konten yang berbeda
    text = MakeObject<TextFragment>(" Hello Again..");
    // Atur TextFragment sebagai paragraf sejajar
    text->set_IsInLineParagraph(true);
    // Tambahkan TextFragment yang baru dibuat ke koleksi paragraf dari halaman
    page->get_Paragraphs()->Add(text);

    document->Save(_dataDir + outputFileName);
}
```

## Tentukan Spasi Karakter saat Menambahkan Teks

Teks dapat ditambahkan ke koleksi paragraf PDF menggunakan instance TextFragment atau objek TextParagraph, dan Anda bahkan dapat menstempel teks di dalam PDF menggunakan kelas TextStamp. Saat menambahkan teks, kita mungkin diharuskan menentukan spasi antara karakter untuk objek teks. Untuk memenuhi persyaratan ini, properti baru telah diperkenalkan bernama Property CharacterSpacing.

Harap pertimbangkan pendekatan berikut untuk memenuhi persyaratan ini.

Pendekatan berikut menunjukkan langkah-langkah untuk menentukan spasi karakter saat menambahkan teks di dalam dokumen PDF.

### Menggunakan TextBuilder dan TextFragment

```cpp
// Tentukan Spasi Karakter saat menambahkan Teks menggunakan TextBuilder dan TextFragment
void CharacterSpacing_TextFragment() {
    
    String _dataDir("C:\\Samples\\");

    // String untuk nama file keluaran    
    String outputFileName("CharacterSpacingUsingTextBuilderAndFragment_out.pdf");

    // Buat instance Dokumen
    auto document = MakeObject<Document>();
    // Tambahkan halaman ke koleksi halaman Dokumen
    auto page = document->get_Pages()->Add();

    // Buat instance TextBuilder
    auto builder = MakeObject<TextBuilder>(page);

    // Buat instance fragmen teks dengan konten sampel
    auto wideFragment = MakeObject<TextFragment>("Teks dengan spasi karakter yang lebih besar");
    wideFragment->get_TextState()->ApplyChangesFrom(MakeObject<TextState>("Arial", 12));

    // Tentukan spasi karakter untuk TextFragment
    wideFragment->get_TextState()->set_CharacterSpacing(2.0f);

    // Tentukan posisi TextFragment
    wideFragment->set_Position(MakeObject<Position>(100, 650));

    // Tambahkan TextFragment ke instance TextBuilder
    builder->AppendText(wideFragment);

    // Simpan dokumen PDF yang dihasilkan.
    document->Save(_dataDir + outputFileName);
}
```

### Menggunakan TextParagraph

```cpp
void CharacterSpacing_TextParagraph() {
    
    String _dataDir("C:\\Samples\\");

    // String untuk nama file keluaran    
    String outputFileName("CharacterSpacingUsingTextBuilderAndFragment_out.pdf");

    // Buat instance Dokumen
    auto document = MakeObject<Document>();

    // Tambahkan halaman ke koleksi halaman Dokumen
    auto page = document->get_Pages()->Add();

    // Buat instance TextBuilder
    auto builder = MakeObject<TextBuilder>(page);

    // Instansiasi instance TextParagraph
    auto paragraph = MakeObject<TextParagraph>();

    // Buat instance TextState untuk menentukan nama dan ukuran font
    auto state = MakeObject<TextState>("Arial", 12);

    // Tentukan spasi karakter
    state->set_CharacterSpacing(1.5f);

    // Tambahkan teks ke objek TextParagraph
    paragraph->AppendLine(u"Ini adalah paragraf dengan spasi karakter", state);

    // Tentukan posisi untuk TextParagraph
    paragraph->set_Position(MakeObject<Position>(100, 550));

    // Tambahkan TextParagraph ke instance TextBuilder
    builder->AppendParagraph(paragraph);

    // Simpan dokumen PDF hasil.
    document->Save(_dataDir + outputFileName);
}
```

### Menggunakan TextStamp

```cpp
void CharacterSpacing_TextStamp() {
    
    String _dataDir("C:\\Samples\\");
    String outputFileName("CharacterSpacingUsingTextStamp_out.pdf");
    // Buat instance Dokumen
    auto document = MakeObject<Document>();

    // Tambahkan halaman ke koleksi halaman Dokumen    
    auto page = document->get_Pages()->Add();

    // Instansiasi instance TextStamp dengan teks contoh
    auto stamp = MakeObject<TextStamp>("Ini adalah cap teks dengan spasi karakter");

    // Tentukan nama font untuk objek Stamp
    stamp->get_TextState()->set_Font(FontRepository::FindFont(u"Arial"));
    // Tentukan ukuran Font untuk TextStamp
    stamp->get_TextState()->set_FontSize(12);
    // Tentukan spasi karakter sebagai 1f
    stamp->get_TextState()->set_CharacterSpacing(1.0f);
    // Atur XIndent untuk Stamp
    stamp->set_XIndent(100);
    // Atur YIndent untuk Stamp
    stamp->set_YIndent(500);
    // Tambahkan cap tekstual ke instance halaman
    stamp->Put(page);
    // Simpan dokumen PDF yang dihasilkan.
    document->Save(_dataDir + outputFileName);
}
```

## Membuat Dokumen PDF Multi-Kolom

Topik ini menunjukkan bagaimana Anda dapat membuat PDF multi-kolom menggunakan Aspose.Pdf untuk C++.

Saat ini, kita lebih sering melihat berita ditampilkan dalam beberapa kolom pada halaman terpisah, daripada di buku, di mana paragraf teks sebagian besar dicetak di semua halaman dari kiri ke kanan. Banyak aplikasi pemrosesan dokumen, seperti Microsoft Word dan Adobe Acrobat Writer, memungkinkan pengguna untuk membuat beberapa kolom pada satu halaman dan kemudian menambahkan data ke dalamnya.

Aspose.Pdf untuk C++ juga menawarkan kemampuan untuk membuat beberapa kolom di halaman dokumen PDF. Untuk membuat PDF dengan beberapa kolom, kita dapat menggunakan kelas [Aspose.Pdf.FloatingBox](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.floating_box) karena menyediakan properti ColumnInfo.ColumnCount untuk menentukan jumlah kolom di dalam FloatingBox, dan kita juga dapat menentukan jarak antar kolom dan lebar kolom menggunakan ColumnInfo .ColumnSpacing dan ColumnInfo .ColumnWidths masing-masing.

Contoh di bawah ini menunjukkan pembuatan dua kolom dengan objek Grafik (Garis) dan mereka ditambahkan ke koleksi paragraf dari FloatingBox, yang kemudian ditambahkan ke koleksi paragraf dari instance Page.

```cpp
void CreateMultiColumn() {

    String _dataDir("C:\\Samples\\");
    String outputFileName("CreateMultiColumnPdf_out.pdf");

    // Buat instance dokumen baru
    auto document = MakeObject<Document>();

    // Tentukan info margin kiri untuk file PDF
    document->get_PageInfo()->get_Margin()->set_Left(40);

    // Tentukan info margin kanan untuk file PDF
    document->get_PageInfo()->get_Margin()->set_Right(40);

    // Tambahkan halaman ke koleksi halaman file PDF
    auto page = document->get_Pages()->Add();

    auto graph1 = MakeObject<Aspose::Pdf::Drawing::Graph>(500, 2);

    // Tambahkan garis ke koleksi paragraf objek bagian
    page->get_Paragraphs()->Add(graph1);

    // Tentukan koordinat untuk garis
    auto posArr = MakeArray<float>({ 1, 2, 500, 2 });
    auto l1 = MakeObject<Aspose::Pdf::Drawing::Line>(posArr);
    graph1->get_Shapes()->Add(l1);

    // Buat variabel string dengan teks yang mengandung tag html
    String s ("<span style=\"font-family: \"Times New Roman\", Times, serif;\" font-size=\"14pt\" \">\
<strong> Cara Menghindari Penipuan Uang</<strong> </span>");

    // Buat paragraf teks yang mengandung teks HTML

    auto heading_text = MakeObject<HtmlFragment>(s);
    page->get_Paragraphs()->Add(heading_text);

    auto box = MakeObject<FloatingBox>();

    // Tambahkan empat kolom di dalam bagian
    box->get_ColumnInfo()->set_ColumnCount(2);
    // Atur jarak antara kolom
    box->get_ColumnInfo()->set_ColumnSpacing(u"5");

    box->get_ColumnInfo()->set_ColumnWidths(u"105 105");
    auto text1 = MakeObject<TextFragment>("Oleh Seorang Googler (Blog Resmi Google)");
    text1->get_TextState()->set_FontSize(8);
    text1->get_TextState()->set_LineSpacing(2);
    text1->get_TextState()->set_FontSize(10);
    text1->get_TextState()->set_FontStyle(FontStyles::Italic);

    box->get_Paragraphs()->Add(text1);

    // Buat objek grafik untuk menggambar garis
    auto graph2 = MakeObject<Aspose::Pdf::Drawing::Graph>(50, 10);
    // Tentukan koordinat untuk garis
    auto posArr2 = MakeArray<float>({ 1, 10, 100, 10 });

    auto l2 = MakeObject<Aspose::Pdf::Drawing::Line>(posArr2);
    graph2->get_Shapes()->Add(l2);

    // Tambahkan garis ke koleksi paragraf objek bagian
    box->get_Paragraphs()->Add(graph2);

    auto text2 = MakeObject<TextFragment>(
        "Sed augue tortor, sodales id, luctus et, pulvinar ut, eros. Suspendisse vel dolor. \
        Sed quam. Curabitur ut massa vitae eros euismod aliquam. Pellentesque sit amet elit. Vestibulum interdum pellentesque augue.\
        Cras mollis arcu sit amet purus. Donec augue. Nam mollis tortor a elit. Nulla viverra nisl vel mauris. Vivamus sapien. nascetur \
        ridiculus mus. Nam justo lorem, aliquam luctus, sodales et, semper sed, enim Nam justo lorem, aliquam luctus, sodales et,nAenean \
        posuere ante ut neque. Morbi sollicitudin congue felis. Praesent turpis diam, iaculis sed, pharetra non, mollis ac, mauris. \
        Phasellus nisi ipsum, pretium vitae, tempor sed, molestie eu, dui. Duis lacus purus, tristique ut, iaculis cursus, tincidunt vitae, \
        risus. Sed commodo. *** sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Nam justo lorem, aliquam \
        luctus, sodales et, semper sed, enim Nam justo lorem, aliquam luctus, sodales et, semper sed, enim Nam justo lorem, aliquam luctus, \
        sodales et, semper sed, enim nAenean posuere ante ut neque. Morbi sollicitudin congue felis. Praesent turpis diam, iaculis sed, \
        pharetra non, mollis ac, mauris. Phasellus nisi ipsum, pretium vitae, tempor sed, molestie eu, dui. Duis lacus purus, tristique ut,\
        iaculis cursus, tincidunt vitae, risus. Sed commodo. *** sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus \
        mus. Sed urna. . Duis convallis ultrices nisi. Maecenas non ligula. Nunc nibh est, tincidunt in, placerat sit amet, vestibulum a, nulla.\
        Praesent porttitor turpis eleifend ante. Morbi sodales.nAenean posuere ante ut neque. Morbi sollicitudin congue felis. Praesent turpis diam,\
        iaculis sed, pharetra non, mollis ac, mauris. Phasellus nisi ipsum, pretium vitae, tempor sed, molestie eu, dui. Duis lacus purus, tristique\
        ut, iaculis cursus, tincidunt vitae, risus. Sed commodo. *** sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus.\
        Sed urna. . Duis convallis ultrices nisi. Maecenas non ligula. Nunc nibh est, tincidunt in, placerat sit amet, vestibulum a, nulla. \
        Praesent porttitor turpis eleifend ante. Morbi sodales.");
    box->get_Paragraphs()->Add(text2);

    page->get_Paragraphs()->Add(box);

    // Simpan file PDF
    document->Save(_dataDir + outputFileName);
}
```

## Bekerja dengan Tab Stops Kustom

Tab Stop adalah titik berhenti untuk tabulasi. Dalam pengolahan kata, setiap baris berisi sejumlah tab stop yang ditempatkan pada interval reguler (misalnya, setiap setengah inci). Namun, mereka dapat diubah, karena sebagian besar pengolah kata memungkinkan Anda untuk mengatur tab stop di mana pun Anda mau. Ketika Anda menekan tombol Tab, kursor atau titik penyisipan melompat ke tab stop berikutnya, yang pada dirinya sendiri tidak terlihat. Meskipun tab stop tidak ada dalam file teks, pengolah kata melacaknya sehingga dapat bereaksi dengan benar terhadap tombol Tab.

Berikut adalah contoh cara mengatur TAB stop kustom.

```cpp
void CustomTabStops() {
    String _dataDir("C:\\Samples\\");
    String outputFileName("CustomTabStops_out.pdf");

    auto document = MakeObject<Document>();
    auto page = document->get_Pages()->Add();

    auto ts = MakeObject<TabStops>();
    auto ts1 = ts->Add(100);

    ts1->set_AlignmentType(TabAlignmentType::Right);
    ts1->set_LeaderType(TabLeaderType::Solid);

    auto ts2 = ts->Add(200);
    ts2->set_AlignmentType(TabAlignmentType::Center);
    ts2->set_LeaderType(TabLeaderType::Dash);

    auto ts3 = ts->Add(300);
    ts3->set_AlignmentType(TabAlignmentType::Left);
    ts3->set_LeaderType(TabLeaderType::Dot);

    auto header = MakeObject<TextFragment>("Ini adalah contoh pembentukan tabel dengan TAB stops", ts);
    auto text0 =  MakeObject<TextFragment>("#$TABHead1 #$TABHead2 #$TABHead3", ts);

    auto text1 = MakeObject<TextFragment>("#$TABdata11 #$TABdata12 #$TABdata13", ts);
    auto text2 = MakeObject<TextFragment>("#$TABdata21 ", ts);
    text2->get_Segments()->Add(MakeObject<TextSegment>("#$TAB"));
    text2->get_Segments()->Add(MakeObject<TextSegment>("data22 "));
    text2->get_Segments()->Add(MakeObject<TextSegment>("#$TAB"));
    text2->get_Segments()->Add(MakeObject<TextSegment>("data23"));
              
    page->get_Paragraphs()->Add(header);
    page->get_Paragraphs()->Add(text0);
    page->get_Paragraphs()->Add(text1);
    page->get_Paragraphs()->Add(text2);

    document->Save(_dataDir + outputFileName);
}
```

## Cara Menambahkan Teks Transparan dalam PDF

PDF 1.4 (format file yang didukung oleh Acrobat 5) adalah versi pertama dari PDF yang mendukung transparansi. PDF ini masuk ke pasar hampir bersamaan dengan Adobe Illustrator 9.

File PDF berisi objek Gambar, Teks, Grafik, lampiran, Anotasi dan saat membuat TextFragment, Anda dapat mengatur informasi warna latar depan, latar belakang serta pemformatan teks. Aspose.PDF untuk C++ mendukung fitur untuk menambahkan teks dengan saluran warna Alpha. Cuplikan kode berikut menunjukkan cara menambahkan teks dengan warna transparan.

```cpp
void AddTransparentText() {

    String _dataDir("C:\\Samples\\");
    String outputFileName("AddTransparentText_out.pdf");

    // Membuat instance Dokumen
    auto document = MakeObject<Document>();    
    // Membuat halaman untuk koleksi halaman dari file PDF
    auto page = document->get_Pages()->Add();

    // Membuat objek Grafik
    auto canvas = MakeObject<Aspose::Pdf::Drawing::Graph>(100, 400);

    // Membuat instance persegi panjang dengan dimensi tertentu
    auto rect = MakeObject<Aspose::Pdf::Drawing::Rectangle>(100, 100, 400, 400);
    // Membuat objek warna dari saluran warna Alpha
    int alpha = 10;
    int green = 0;
    int red = 100;
    int blue = 0;

    auto alphaColor = Color::FromArgb(alpha, red, green, blue);

    rect->get_GraphInfo()->set_FillColor(alphaColor);

    // Menambahkan persegi panjang ke koleksi bentuk dari objek Grafik
    canvas->get_Shapes()->Add(rect);

    // Menambahkan objek grafik ke koleksi paragraf dari objek halaman
    page->get_Paragraphs()->Add(canvas);

    // Mengatur nilai untuk tidak mengubah posisi untuk objek grafik
    canvas->set_IsChangePosition(false);

    // Membuat instance TextFragment dengan nilai sampel
    auto text = MakeObject<TextFragment>(
        "teks transparan teks transparan teks transparan teks transparan teks transparan teks transparan teks transparan teks transparan teks transparan teks transparan teks transparan teks transparan teks transparan teks transparan teks transparan teks transparan ");
    // Membuat objek warna dari saluran Alpha
    alpha = 30;
    alphaColor = Color::FromArgb(alpha, red, green, blue);
    // Mengatur informasi warna untuk instance teks
    text->get_TextState()->set_ForegroundColor(alphaColor);
    // Menambahkan teks ke koleksi paragraf dari instance halaman
    page->get_Paragraphs()->Add(text);

    document->Save(_dataDir + outputFileName);
}
```

## Tentukan Jarak Baris untuk Font

Kelas [Aspose.Pdf.Text.TextFormattingOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_formatting_options) memiliki enumerasi [LineSpacingMode](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_formatting_options#a240276fd8a270b7c134d3355c5fb1c91) yang dirancang untuk font tertentu, misalnya input font "HPSimplified.ttf". Juga, kelas [Aspose.Pdf.Text.TextFormattingOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_formatting_options) memiliki properti [LineSpacing](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_formatting_options#a240276fd8a270b7c134d3355c5fb1c91a9e120eead36071a90367e425c96b5eaf) dari tipe LineSpacingMode. Anda hanya perlu mengatur LineSpacing ke LineSpacingMode.FullSize. Cuplikan kode untuk menampilkan font dengan benar adalah sebagai berikut:

```cpp
void SpecifyLineSpacingForFonts() {

    String _dataDir("C:\\Samples\\");
    String outputFileName("SpecifyLineSpacing_out.pdf");

    String fontFile ("hp-simplified-265.ttf");

    // Load input PDF file
    auto document = MakeObject<Document>();
    
    // Create TextFormattingOptions with LineSpacingMode.FullSize
    auto formattingOptions = MakeObject<TextFormattingOptions>();
    formattingOptions->set_LineSpacing(TextFormattingOptions::LineSpacingMode::FullSize);
    
    // Create text fragment with sample string
    auto textFragment = MakeObject<TextFragment>("Hello world");

    // Load the TrueType font into stream object
    auto fontStream = System::IO::File::OpenRead(_dataDir + fontFile);
    
    // Set the font name for text string
    textFragment->get_TextState()->set_Font(FontRepository::OpenFont(fontStream, FontTypes::TTF));
    // Specify the position for Text Fragment
    textFragment->set_Position(MakeObject<Position>(100, 600));
    // Set TextFormattingOptions of current fragment to predefined(which points to
    // LineSpacingMode.FullSize)
    textFragment->get_TextState()->set_FormattingOptions(formattingOptions);
    
    // Add the text to TextBuilder so that it can be placed over the PDF file    
    auto page = document->get_Pages()->Add();
    page->get_Paragraphs()->Add(textFragment);

    // Save resulting PDF document
    document->Save(_dataDir + outputFileName);
}
```

## Mendapatkan Lebar Teks Secara Dinamis

Kelas [Aspose.Pdf.Text.TextState](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_state) menunjukkan cara mendapatkan lebar teks secara dinamis dalam dokumen PDF.

Terkadang, diperlukan untuk mendapatkan lebar teks secara dinamis. Aspose.PDF untuk C++ menyertakan dua metode untuk pengukuran lebar string. Anda dapat memanggil metode [MeasureString](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_state#a084c1781028cd3483c82b4fd4cec4967) dari kelas Aspose.Pdf.Text.Font atau Aspose.Pdf.Text.TextState (atau keduanya). Cuplikan kode di bawah ini menunjukkan cara menggunakan fungsi ini.

```cpp
void GetTextWidthDynamicaly() {
    auto font = FontRepository::FindFont(u"Arial");
    auto ts = MakeObject<TextState>();

    ts->set_Font(font);
    ts->set_FontSize(14);

    if (Math::Abs(font->MeasureString(u"A", 14) - 9.337) > 0.001)
        Console::WriteLine(u"Pengukuran string font tidak terduga!");

    if (Math::Abs(ts->MeasureString(u"z") - 7.0) > 0.001)
        Console::WriteLine(u"Pengukuran string font tidak terduga!");

    for (char c = 'A'; c <= 'z'; c++) {
        String v(c);
        double fnMeasure = font->MeasureString(v, 14);
        double tsMeasure = ts->MeasureString(v);

        if (Math::Abs(fnMeasure - tsMeasure) > 0.001)
            Console::WriteLine(u"Pengukuran string font dan state tidak cocok!");
    }
}
```