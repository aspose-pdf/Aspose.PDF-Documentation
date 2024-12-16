---
title: Membuat PDF yang kompleks 
linktitle: Membuat PDF yang kompleks
type: docs
weight: 60
url: /id/cpp/complex-pdf-example/
description: Aspose.PDF untuk C++ memungkinkan Anda membuat dokumen yang lebih kompleks yang berisi gambar, fragmen teks, dan tabel dalam satu dokumen.
lastmod: "2021-11-05"
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

Contoh [Hello, World](/pdf/id/cpp/hello-world-example/) menunjukkan langkah-langkah sederhana untuk membuat dokumen PDF menggunakan C++ dan Aspose.PDF. Dalam artikel ini, kita akan melihat pembuatan dokumen yang lebih kompleks dengan C++ dan Aspose.PDF untuk C++. Sebagai contoh, kita akan mengambil dokumen dari perusahaan fiktif yang mengoperasikan layanan feri penumpang.
Dokumen kita akan berisi gambar, dua fragmen teks (header dan paragraf), dan sebuah tabel. Untuk membangun dokumen semacam itu, kita akan menggunakan pendekatan berbasis DOM. Anda dapat membaca lebih lanjut di bagian [Dasar-dasar API DOM](/pdf/id/cpp/basics-of-dom-api/).

Jika kita membuat dokumen dari awal kita perlu mengikuti langkah-langkah tertentu:

1. Buat [Kelas String](https://reference.aspose.com/pdf/cpp/class/system.string) untuk nama jalur dan nama file.
1. Instansikan objek [Dokumen](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document). Pada langkah ini kita akan membuat dokumen PDF kosong dengan beberapa metadata tetapi tanpa halaman.
1. Tambahkan [Halaman](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page) ke objek dokumen. Jadi, sekarang dokumen kita akan memiliki satu halaman.
1. Tambahkan [Gambar](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.image) ke Halaman.
1. Buat [TextFragment](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_fragment/) untuk header. Untuk header kita akan menggunakan font Arial dengan ukuran font 24pt dan perataan tengah.
1. Tambahkan header ke [Paragraf](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page#ac5c48bedc9fe8a7e0800a1d9b2c28170) halaman. Buat [TextFragment](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_fragment/) untuk deskripsi. Untuk deskripsi kita akan menggunakan font Arial dengan ukuran font 24pt dan perataan tengah.
1. Tambahkan (deskripsi) ke halaman Paragraf.
1. Buat tabel, tambahkan properti tabel.
1. Tambahkan (tabel) ke halaman [Paragraf](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page#ac5c48bedc9fe8a7e0800a1d9b2c28170).
1. Simpan dokumen "Complex.pdf".

```cpp
void ExampleComplex()
{
    String outputFileName;

    // String untuk nama jalur.
    String _dataDir("C:\\Samples\\");

    // String untuk nama file.
    String filename("Complex.pdf");

    // Inisialisasi objek dokumen
    auto document = MakeObject<Document>();
    // Tambahkan halaman
    auto page = document->get_Pages()->Add();

    // Tambahkan gambar
    String imageFileName = _dataDir + String(u"logo.png");

    // Tambahkan gambar ke koleksi Gambar dari Sumber Daya Halaman
    auto rectangle = MakeObject<Rectangle>(20, 730, 120, 830);
    page->AddImage(imageFileName, rectangle);

    // Tambahkan Header
    auto header = MakeObject<TextFragment>(u"Rute feri baru pada Musim Gugur 2020");
    auto textFragementState = header->get_TextState();
    textFragementState->set_Font(FontRepository::FindFont(u"Arial"));
    textFragementState->set_FontSize(24);
    header->set_HorizontalAlignment(HorizontalAlignment::Center);
    auto position = MakeObject<Aspose::Pdf::Text::Position>(130, 720);
    header->set_Position(position);
    page->get_Paragraphs()->Add(header);

    // Tambahkan deskripsi
    String descriptionText(u"Pengunjung harus membeli tiket secara online dan tiket dibatasi hingga 5.000 per hari. Layanan feri beroperasi dengan setengah kapasitas dan dengan jadwal yang dikurangi. Harapkan antrean.");
    auto description = MakeObject<TextFragment>(descriptionText);
    description->get_TextState()->set_Font(FontRepository::FindFont(u"Times New Roman"));
    description->get_TextState()->set_FontSize(14);
    description->set_HorizontalAlignment(HorizontalAlignment::Left);
    page->get_Paragraphs()->Add(description);

    // Tambahkan tabel
    auto table = MakeObject<Table>();
    table->set_ColumnWidths(u"200");

    table->set_Border(MakeObject<BorderInfo>(Aspose::Pdf::BorderSide::Box, 1.0f, Aspose::Pdf::Color::get_DarkSlateGray()));
    table->set_DefaultCellBorder(MakeObject<BorderInfo>(Aspose::Pdf::BorderSide::Box, .5f, Aspose::Pdf::Color::get_Black()));
    table->get_Margin()->set_Bottom(10);
    table->get_DefaultCellTextState()->set_Font(FontRepository::FindFont(u"Helvetica"));

    auto headerRow = table->get_Rows()->Add();
    headerRow->get_Cells()->Add(u"Berangkat Kota");
    headerRow->get_Cells()->Add(u"Berangkat Pulau");

    for (auto headerRowCell : headerRow->get_Cells())
    {
        headerRowCell->set_BackgroundColor(Color::get_Gray());
        headerRowCell->get_DefaultCellTextState()->set_ForegroundColor(Color::get_WhiteSmoke());
    }

    String arrivals[10] = { u"6:00",u"6:45", u"7:00", u"7:45", u"8:00", u"8:45", u"9:00", u"9:45", u"10:00", u"10:45" };
    String departures[10] = { u"7:00", u"7:45", u"8:00", u"8:45", u"9:00", u"9:45", u"10:00", u"10:45", u"11:00", u"11:45" };

    for (int i = 0; i < 10; i++)
    {
        auto dataRow = table->get_Rows()->Add();
        dataRow->get_Cells()->Add(arrivals[i]);
        dataRow->get_Cells()->Add(departures[i]);
    }

    page->get_Paragraphs()->Add(table);

    // Simpan PDF yang diperbarui
    outputFileName = _dataDir + filename;

    document->Save(outputFileName);
}
```