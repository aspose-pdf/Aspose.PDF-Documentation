---
title: Tambahkan Objek Elips ke file PDF
linktitle: Tambahkan Elips
type: docs
weight: 60
url: /cpp/add-ellipse/
description: Artikel ini menjelaskan bagaimana cara membuat objek Elips ke PDF Anda menggunakan Aspose.PDF untuk C++.
lastmod: "2021-12-21"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Tambahkan objek Elips

Aspose.PDF untuk C++ mendukung penambahan objek [Elips](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.ellipse/) ke dokumen PDF. Ini juga menawarkan fitur untuk mengisi objek elips dengan warna tertentu.

```cpp
void ExampleEllipse() {
    // Buat instance Dokumen
    String _dataDir("C:\\Samples\\");
    // Buat instance Dokumen
    auto document = MakeObject<Document>();

    // Tambahkan halaman ke koleksi halaman file PDF
    auto page = document->get_Pages()->Add();

    // Buat objek Drawing dengan dimensi tertentu
    auto graph = MakeObject<Aspose::Pdf::Drawing::Graph>(400, 400);
    // Tetapkan batas untuk objek Drawing
    auto borderInfo = MakeObject<BorderInfo>(BorderSide::All, Color::get_Green());
    graph->set_Border(borderInfo);

    auto ellipse1 = MakeObject<Aspose::Pdf::Drawing::Ellipse>(150, 100, 120, 60);
    ellipse1->get_GraphInfo()->set_Color(Color::get_GreenYellow());
    ellipse1->set_Text(MakeObject<Aspose::Pdf::Text::TextFragment>("Elips"));
    graph->get_Shapes()->Add(ellipse1);

    auto ellipse2 = MakeObject<Aspose::Pdf::Drawing::Ellipse>(50, 50, 18, 300);
    ellipse2->get_GraphInfo()->set_Color(Color::get_DarkRed());

    graph->get_Shapes()->Add(ellipse2);

    // Tambahkan objek Graph ke koleksi paragraf halaman
    page->get_Paragraphs()->Add(graph);

    // Simpan file PDF
    document->Save(_dataDir + u"DrawingEllipse_out.pdf");

}
```

![Tambahkan Elips](ellipse.png)

## Membuat Objek Elips Terisi

Cuplikan kode berikut menunjukkan cara menambahkan objek [Elips](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.ellipse/) yang diisi dengan warna.

```csharp
void ExampleFilledEllipse() {
    // Buat instance Dokumen
    String _dataDir("C:\\Samples\\");
    // Buat instance Dokumen
    auto document = MakeObject<Document>();

    // Tambahkan halaman ke koleksi halaman dari file PDF
    auto page = document->get_Pages()->Add();

    // Buat objek Gambar dengan dimensi tertentu
    auto graph = MakeObject<Aspose::Pdf::Drawing::Graph>(400, 400);
    // Atur batas untuk objek Gambar
    auto borderInfo = MakeObject<BorderInfo>(BorderSide::All, Color::get_Green());
    graph->set_Border(borderInfo);

    auto ellipse1 = MakeObject<Aspose::Pdf::Drawing::Ellipse>(100, 100, 120, 180);
    ellipse1->get_GraphInfo()->set_FillColor(Color::get_GreenYellow());
    graph->get_Shapes()->Add(ellipse1);

    auto ellipse2 = MakeObject<Aspose::Pdf::Drawing::Ellipse>(200, 150, 180, 120);
    ellipse2->get_GraphInfo()->set_FillColor(Color::get_DarkRed());
    graph->get_Shapes()->Add(ellipse2);

    // Tambahkan objek Gambar ke koleksi paragraf dari halaman
    page->get_Paragraphs()->Add(graph);

    // Simpan file PDF
    document->Save(_dataDir + u"DrawingEllipse_out.pdf");
}
```

![Filled Ellipse](fill_ellipse.png)

## Tambahkan Teks di dalam Elips

Aspose.PDF untuk C++ mendukung penambahan teks di dalam Objek Grafik. Properti teks dari Objek Grafik menyediakan opsi untuk mengatur teks dari Objek Grafik.

Cuplikan kode berikut menunjukkan cara menambahkan teks di dalam objek Persegi Panjang.

```cpp
void ExampleEllipseWithText() {
    // Buat instance Dokumen
    String _dataDir("C:\\Samples\\");
    // Buat instance Dokumen
    auto document = MakeObject<Document>();

    // Tambahkan halaman ke koleksi halaman file PDF
    auto page = document->get_Pages()->Add();

    // Buat objek Gambar dengan dimensi tertentu
    auto graph = MakeObject<Aspose::Pdf::Drawing::Graph>(400, 400);
    // Atur batas untuk objek Gambar
    auto borderInfo = MakeObject<BorderInfo>(BorderSide::All, Color::get_Green());
    graph->set_Border(borderInfo);

    auto textFragment = MakeObject<Aspose::Pdf::Text::TextFragment>("Elips");
    textFragment->get_TextState()->set_Font(Aspose::Pdf::Text::FontRepository::FindFont(u"Helvetica"));
    textFragment->get_TextState()->set_FontSize(24);

    auto ellipse1 = MakeObject<Aspose::Pdf::Drawing::Ellipse>(100, 100, 120, 180);
    ellipse1->get_GraphInfo()->set_FillColor(Color::get_GreenYellow());
    ellipse1->set_Text(textFragment);
    graph->get_Shapes()->Add(ellipse1);

    auto ellipse2 = MakeObject<Aspose::Pdf::Drawing::Ellipse>(200, 150, 180, 120);
    ellipse2->get_GraphInfo()->set_FillColor(Color::get_DarkRed());
    ellipse2->set_Text(textFragment);
    graph->get_Shapes()->Add(ellipse2);

    // Tambahkan objek Gambar ke koleksi paragraf halaman
    page->get_Paragraphs()->Add(graph);

    // Simpan file PDF
    document->Save(_dataDir + u"DrawingEllipseText_out.pdf");

}
```