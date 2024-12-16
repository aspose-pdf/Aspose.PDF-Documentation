---
title: Tambahkan Objek Busur ke file PDF
linktitle: Tambahkan Busur
type: docs
weight: 10
url: /id/cpp/add-arc/
description: Artikel ini menjelaskan cara membuat objek busur ke dalam PDF Anda menggunakan Aspose.PDF untuk C++.
lastmod: "2021-12-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Tambahkan objek Busur

Aspose.PDF untuk C++ mendukung fitur untuk menambahkan objek grafis (misalnya grafis, garis, persegi panjang, dll.) ke dokumen PDF. Ini juga menawarkan fitur untuk mengisi objek [Busur](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.arc) dengan warna tertentu.

Ikuti langkah-langkah berikut:

1. Buat instance [Dokumen](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document)

1. Buat [objek Gambar](https://reference.aspose.com/pdf/cpp/namespace/aspose.pdf.drawing) dengan dimensi tertentu

1. Tetapkan [Perbatasan](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.graph#ab63dde9501441515b915fd68f66a01bd) untuk objek Gambar

1. Tambahkan objek [Graph](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.graph) ke koleksi paragraf halaman

1. Simpan file PDF kita

Cuplikan kode berikut menunjukkan cara menambahkan objek [Arc](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.arc/).

```cpp
void ExampleArc() {
    // Buat instance Dokumen
    String _dataDir("C:\\Samples\\");
    // Buat instance Dokumen
    auto document = MakeObject<Document>();

    // Tambahkan halaman ke koleksi halaman file PDF
    auto page = document->get_Pages()->Add();

    // Buat objek Gambar dengan dimensi tertentu
    auto graph = MakeObject<Aspose::Pdf::Drawing::Graph>(400, 400);
    // Tetapkan batas untuk objek Gambar
    auto borderInfo = MakeObject<BorderInfo>(BorderSide::All, Color::get_Green());
    graph->set_Border(borderInfo);

    auto arc1 = MakeObject<Aspose::Pdf::Drawing::Arc>(100, 100, 95, 0, 90);
    arc1->get_GraphInfo()->set_Color(Color::get_GreenYellow());
    graph->get_Shapes()->Add(arc1);

    auto arc2 = MakeObject<Aspose::Pdf::Drawing::Arc>(100, 100, 90, 70, 180);
    arc2->get_GraphInfo()->set_Color(Color::get_DarkBlue());
    graph->get_Shapes()->Add(arc2);

    auto arc3 = MakeObject<Aspose::Pdf::Drawing::Arc>(100, 100, 85, 120, 210);
    arc3->get_GraphInfo()->set_Color(Color::get_Red());
    graph->get_Shapes()->Add(arc3);

    // Tambahkan objek Grafis ke koleksi paragraf halaman
    page->get_Paragraphs()->Add(graph);

    // Simpan file PDF
    document->Save(_dataDir + u"DrawingArc_out.pdf");

}
```
## Membuat Objek Busur Terisi

Contoh berikut menunjukkan cara menambahkan objek Busur yang diisi dengan warna dan dimensi tertentu.

```cpp
void ExampleFilledArc() {

    // Membuat instance Dokumen
    String _dataDir("C:\\Samples\\");
    // Membuat instance Dokumen
    auto document = MakeObject<Document>();

    // Menambahkan halaman ke koleksi halaman dari file PDF
    auto page = document->get_Pages()->Add();

    // Membuat objek Gambar dengan dimensi tertentu
    auto graph = MakeObject<Aspose::Pdf::Drawing::Graph>(400, 400);
    // Mengatur batas untuk objek Gambar
    auto borderInfo = MakeObject<BorderInfo>(BorderSide::All, Color::get_Green());
    graph->set_Border(borderInfo);

    auto arc = MakeObject<Aspose::Pdf::Drawing::Arc>(100, 100, 95, 0, 90);
    arc->get_GraphInfo()->set_FillColor(Color::get_GreenYellow());
    graph->get_Shapes()->Add(arc);

    auto line = MakeObject<Aspose::Pdf::Drawing::Line>(MakeArray<double>({ 195, 100, 100, 100, 100, 195 }));
    line->get_GraphInfo()->set_FillColor(Color::get_GreenYellow());
    graph->get_Shapes()->Add(line);

    // Menambahkan objek Gambar ke koleksi paragraf dari halaman
    page->get_Paragraphs()->Add(graph);

    // Menyimpan file PDF
    document->Save(_dataDir + u"DrawingArc_out.pdf");

}
```

```
Mari kita lihat hasil dari menambahkan Arс yang terisi:

![Filled Arc](filled_arc.png)
```