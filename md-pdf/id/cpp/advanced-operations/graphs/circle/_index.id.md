---
title: Tambahkan Objek Lingkaran ke File PDF
linktitle: Tambahkan Lingkaran
type: docs
weight: 20
url: /cpp/add-circle/
description: Artikel ini menjelaskan cara membuat objek lingkaran ke PDF Anda menggunakan Aspose.PDF untuk C++.
lastmod: "2021-12-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Tambahkan objek Lingkaran

Seperti grafik batang, grafik lingkaran dapat digunakan untuk menampilkan data dalam sejumlah kategori terpisah. Namun, berbeda dengan grafik batang, grafik lingkaran hanya dapat digunakan ketika Anda memiliki data untuk semua kategori yang membentuk keseluruhan. Jadi, mari kita lihat cara menambahkan objek [Lingkaran](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.circle/) dengan Aspose.PDF untuk C++.

Ikuti langkah-langkah berikut:

1. Buat instance [Dokumen](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document)

1. Buat [objek Gambar](https://reference.aspose.com/pdf/cpp/namespace/aspose.pdf.drawing) dengan dimensi tertentu

1. Set [Border](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.graph#ab63dde9501441515b915fd68f66a01bd) untuk objek Drawing

1. Tambahkan objek [Graph](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.graph) ke koleksi paragraf halaman

1. Simpan file PDF kita

```cpp
void ExampleCircle() {

    // Buat instance Dokumen
    String _dataDir("C:\\Samples\\");
    // Buat instance Dokumen
    auto document = MakeObject<Document>();

    // Tambahkan halaman ke koleksi halaman file PDF
    auto page = document->get_Pages()->Add();

    // Buat objek Drawing dengan dimensi tertentu
    auto graph = MakeObject<Aspose::Pdf::Drawing::Graph>(400, 200);
    // Atur border untuk objek Drawing
    auto borderInfo = MakeObject<BorderInfo>(BorderSide::All, Color::get_Green());
    graph->set_Border(borderInfo);

    auto circle = MakeObject<Aspose::Pdf::Drawing::Circle>(100, 100, 40);

    circle->get_GraphInfo()->set_Color(Color::get_GreenYellow());
    graph->get_Shapes()->Add(circle);

    // Tambahkan objek Graph ke koleksi paragraf halaman
    page->get_Paragraphs()->Add(graph);

    // Simpan file PDF
    document->Save(_dataDir + u"DrawingCircle1_out.pdf");
}
```
Lingkaran yang kita gambar akan terlihat seperti ini:

![Drawing Circle](drawing_circle.png)

## Buat Objek Lingkaran Terisi

Contoh ini menunjukkan cara menambahkan objek Lingkaran yang diisi dengan warna.

```cpp
void ExampleFilledCircle() {
    // Buat instance Dokumen
    String _dataDir("C:\\Samples\\");
    // Buat instance Dokumen
    auto document = MakeObject<Document>();

    // Tambahkan halaman ke koleksi halaman file PDF
    auto page = document->get_Pages()->Add();

    // Buat objek Gambar dengan dimensi tertentu
    auto graph = MakeObject<Aspose::Pdf::Drawing::Graph>(400, 200);
    
    // Atur batas untuk objek Gambar
    auto borderInfo = MakeObject<BorderInfo>(BorderSide::All, Color::get_Green());
    graph->set_Border(borderInfo);

    auto circle = MakeObject<Aspose::Pdf::Drawing::Circle>(100, 100, 40);
    circle->get_GraphInfo()->set_Color(Color::get_GreenYellow());
    circle->get_GraphInfo()->set_FillColor(Color::get_Green());

    circle->set_Text(MakeObject<Aspose::Pdf::Text::TextFragment>(u"Circle"));

    graph->get_Shapes()->Add(circle);

    // Tambahkan objek Gambar ke koleksi paragraf halaman
    page->get_Paragraphs()->Add(graph);

    // Simpan file PDF
    document->Save(_dataDir + u"DrawingCircle2_out.pdf");
}
```

```
Mari kita lihat hasil dari menambahkan Lingkaran yang terisi:

![Filled Circle](filled_circle.png)
```