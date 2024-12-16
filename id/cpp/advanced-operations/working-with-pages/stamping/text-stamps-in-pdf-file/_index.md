---
title: Tambahkan Cap Teks dalam File PDF
linktitle: Cap Teks dalam File PDF
type: docs
weight: 20
url: /id/cpp/text-stamps-in-the-pdf-file/
description: Tambahkan cap teks ke file PDF menggunakan kelas TextStamp dengan C++.
lastmod: "2021-12-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Tambahkan Cap Teks dengan C++

Anda dapat menggunakan kelas [TextStamp](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text_stamp) untuk menambahkan cap teks dalam file PDF. Kelas TextStamp menyediakan properti yang diperlukan untuk membuat cap berbasis teks seperti ukuran font, gaya font, dan warna font, dll. Untuk menambahkan cap teks, Anda perlu membuat objek Dokumen dan objek TextStamp menggunakan properti yang diperlukan. Setelah itu, Anda dapat memanggil metode AddStamp dari Page untuk menambahkan cap dalam PDF. Cuplikan kode berikut menunjukkan cara menambahkan cap teks dalam file PDF.

```cpp
void AddTextStampToPDFFile() {

    String _dataDir("C:\\Samples\\");

    // String untuk nama file input
    String inputFileName("AddTextStamp.pdf");
    String outputFileName("AddTextStamp_out.pdf");

    // Buka dokumen
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // Buat cap teks
    auto textStamp =MakeObject<TextStamp>(u"Sample Stamp");

    // Atur apakah cap adalah latar belakang
    textStamp->set_Background(true);
    // Atur asal
    textStamp->set_XIndent(100);
    textStamp->set_YIndent(100);
    // Putar cap
    textStamp->set_Rotate(Rotation::on90);

    // Atur properti teks
    textStamp->get_TextState()->set_Font(FontRepository::FindFont(u"Arial"));
    textStamp->get_TextState()->set_FontSize(14.0F);
    textStamp->get_TextState()->set_FontStyle(FontStyles::Bold);
    textStamp->get_TextState()->set_FontStyle(FontStyles::Italic);
    textStamp->get_TextState()->set_ForegroundColor(Color::get_Green());
    // Tambahkan cap ke halaman tertentu
    document->get_Pages()->idx_get(1)->AddStamp(textStamp);

    // Simpan dokumen output
    document->Save(_dataDir + outputFileName);
}
```

## Mendefinisikan penyelarasan untuk objek TextStamp

Menambahkan watermark ke dokumen PDF adalah salah satu fitur yang sering diminta dan Aspose.PDF untuk C++ sepenuhnya mampu menambahkan watermark Gambar serta Teks. Kami memiliki kelas bernama [TextStamp](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text_stamp) yang menyediakan fitur untuk menambahkan cap teks pada file PDF. Baru-baru ini ada kebutuhan untuk mendukung fitur untuk menentukan penyelarasan teks saat menggunakan objek TextStamp. Jadi untuk memenuhi kebutuhan ini, kami telah memperkenalkan properti TextAlignment dalam kelas TextStamp. Dengan menggunakan properti ini, kita dapat menentukan penyelarasan teks Horizontal.

Cuplikan kode berikut menunjukkan contoh tentang cara memuat dokumen PDF yang sudah ada dan menambahkan TextStamp di atasnya.

```cpp
void DefineAlignmentTextStamp() {

    String _dataDir("C:\\Samples\\");

    // String untuk nama file input
    String inputFileName("AddTextStamp.pdf");
    String outputFileName("AddTextStamp_out.pdf");

    // Buka dokumen
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // instansiasi objek FormattedText dengan string contoh
    auto text = MakeObject<Aspose::Pdf::Facades::FormattedText>("This");

    // tambahkan baris teks baru ke FormattedText
    text->AddNewLineText(u"is sample");
    text->AddNewLineText(u"Center Aligned");
    text->AddNewLineText(u"TextStamp");
    text->AddNewLineText(u"Object");

    // buat objek TextStamp menggunakan FormattedText
    auto stamp = MakeObject<TextStamp>(text);
    // tentukan Penyelarasan Horizontal dari cap teks sebagai selaras Tengah
    stamp->set_HorizontalAlignment(HorizontalAlignment::Center);
    // tentukan Penyelarasan Vertikal dari cap teks sebagai selaras Tengah
    stamp->set_VerticalAlignment(VerticalAlignment::Center);
    // tentukan Penyelarasan Teks Horizontal dari TextStamp sebagai selaras Tengah
    stamp->set_TextAlignment(HorizontalAlignment::Center);
    // atur margin atas untuk objek cap
    stamp->set_TopMargin(20);
    // tambahkan cap ke semua halaman file PDF
    document->get_Pages()->idx_get(1)->AddStamp(stamp);

    // simpan dokumen output
    document->Save(_dataDir + outputFileName);
}
```

## Mengisi Teks Stroke sebagai Cap dalam File PDF

Kami telah mengimplementasikan pengaturan mode rendering untuk skenario penambahan dan pengeditan teks. Untuk merender teks stroke, silakan buat objek TextState dan atur RenderingMode ke TextRenderingMode.StrokeText dan juga pilih warna untuk properti StrokingColor. Kemudian, ikat TextState ke cap menggunakan metode BindTextState().

Cuplikan kode berikut menunjukkan penambahan Teks Stroke Isi:

```cpp
void FillStrokeTextAsStampInPDFFile() {

    String _dataDir("C:\\Samples\\");

    // String untuk nama file input
    String inputFileName("AddTextStamp.pdf");
    String outputFileName("AddTextStamp_out.pdf");

    // Buat objek TextState untuk mentransfer properti lanjutan
    auto ts = MakeObject<TextState>();

    // Atur warna untuk stroke
    ts->set_StrokingColor(Color::get_Gray());

    // Atur mode rendering teks
    ts->set_RenderingMode(TextRenderingMode::StrokeText);

    // Muat dokumen PDF input
    auto fileStamp = MakeObject<Aspose::Pdf::Facades::PdfFileStamp>(MakeObject<Document>(_dataDir + inputFileName));

    auto stamp = MakeObject<Aspose::Pdf::Facades::Stamp>();

    auto formattedText = MakeObject<Aspose::Pdf::Facades::FormattedText>(u"PAID IN FULL", Color::get_Gray(), Aspose::Pdf::Facades::EncodingType::Winansi, true, 78);
    stamp->BindLogo(formattedText);

    // Ikat TextState
    stamp->BindTextState(ts);

    // Atur asal X, Y
    stamp->SetOrigin(100, 100);
    stamp->set_Opacity(5);
    stamp->set_BlendingSpace(Aspose::Pdf::Facades::BlendingColorSpace::DeviceRGB);
    stamp->set_Rotation(45.0F);
    stamp->set_IsBackground(false);

    // Tambahkan Cap
    fileStamp->AddStamp(stamp);
    fileStamp->Save(_dataDir + outputFileName);
    fileStamp->Close();
}
```