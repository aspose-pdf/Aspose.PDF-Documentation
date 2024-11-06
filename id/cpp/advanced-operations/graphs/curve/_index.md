title: Tambahkan Objek Kurva ke file PDF
linktitle: Tambahkan Kurva
type: docs
weight: 30
url: id/cpp/add-curve/
description: Artikel ini menjelaskan cara membuat objek kurva ke PDF Anda menggunakan Aspose.PDF untuk C++.
lastmod: "2021-12-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Tambahkan objek Kurva

Grafik [Kurva](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.curve/) adalah gabungan bersambung dari garis proyektif, setiap garis bertemu tiga lainnya di titik ganda biasa.

Kurva Bézier banyak digunakan dalam grafik komputer untuk memodelkan kurva halus. Kurva sepenuhnya terkandung dalam kerangka cembung dari titik kontrolnya, titik-titik dapat ditampilkan secara grafis dan digunakan untuk memanipulasi kurva secara intuitif. Seluruh kurva terkandung dalam segiempat yang sudutnya adalah empat titik yang diberikan (kerangka cembung mereka).

Dalam artikel ini, kita akan menyelidiki kurva grafik sederhana, dan kurva yang terisi, yang dapat Anda buat dalam dokumen PDF Anda.

Ikuti langkah-langkah di bawah ini:

1.
``` Buat instance [Dokumen](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document)

1. Buat [objek Gambar](https://reference.aspose.com/pdf/cpp/namespace/aspose.pdf.drawing) dengan dimensi tertentu

1. Atur [Perbatasan](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.graph#ab63dde9501441515b915fd68f66a01bd) untuk objek Gambar

1. Tambahkan objek [Grafik](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.graph) ke koleksi paragraf halaman

1. Simpan file PDF kita

```cpp
void ExampleCurve() {

    // Buat instance Dokumen
    String _dataDir("C:\\Samples\\");
    // Buat instance Dokumen
    auto document = MakeObject<Document>();

    // Tambahkan halaman ke koleksi halaman file PDF
    auto page = document->get_Pages()->Add();

    // Buat objek Gambar dengan dimensi tertentu
    auto graph = MakeObject<Aspose::Pdf::Drawing::Graph>(400, 200);
    
    // Atur perbatasan untuk objek Gambar
    auto borderInfo = MakeObject<BorderInfo>(BorderSide::All, Color::get_Green());
    graph->set_Border(borderInfo);

    auto curve1 = MakeObject<Aspose::Pdf::Drawing::Curve>(MakeArray<double> ({ 10, 10, 50, 60, 70, 10, 100, 120}));
    curve1->get_GraphInfo()->set_Color(Color::get_GreenYellow());
    graph->get_Shapes()->Add(curve1);

    // Tambahkan objek Grafik ke koleksi paragraf halaman
    page->get_Paragraphs()->Add(graph);

    // Simpan file PDF
    document->Save(_dataDir + u"DrawingCurve1_out.pdf");
}
```
Gambar berikut menunjukkan hasil yang dieksekusi dengan cuplikan kode kami:

![Drawing Curve](drawing_curve.png)

## Membuat Objek Kurva Terisi

Contoh ini menunjukkan cara menambahkan objek Kurva yang terisi dengan warna.

```cpp
void ExampleFilledCurve() {

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

    auto curve1 = MakeObject<Aspose::Pdf::Drawing::Curve>(MakeArray<double>({ 10, 10, 50, 60, 70, 10, 100, 120}));
    curve1->get_GraphInfo()->set_FillColor(Color::get_GreenYellow());
    graph->get_Shapes()->Add(curve1);

    // Tambahkan objek Gambar ke koleksi paragraf halaman
    page->get_Paragraphs()->Add(graph);

    // Simpan file PDF
    document->Save(_dataDir + u"DrawingCurve2_out.pdf");
}
```

Look at the result of adding a filled Curve:

![Filled Curve](filled_curve.png)

Lihat hasil dari menambahkan Kurva terisi: