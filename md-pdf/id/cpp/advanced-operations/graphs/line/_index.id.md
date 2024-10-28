---
title: Tambahkan Objek Garis ke file PDF
linktitle: Tambahkan Garis
type: docs
weight: 40
url: /cpp/add-line/
description: Artikel ini menjelaskan cara membuat objek garis ke PDF Anda menggunakan Aspose.PDF untuk C++.
lastmod: "2021-12-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Tambahkan objek Garis

Aspose.PDF untuk C++ mendukung fitur untuk menambahkan objek grafis (misalnya grafik, garis, persegi panjang dll.) ke dokumen PDF. Anda juga mendapatkan kemudahan untuk menambahkan objek [Garis](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.line/) di mana Anda juga dapat menentukan pola garis putus-putus, warna, dan pemformatan lainnya untuk elemen Garis.

Ikuti langkah-langkah di bawah ini:

1. Buat [Dokumen](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document/) PDF baru

1. Tambahkan [Halaman](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page/) ke koleksi halaman dari file PDF

1. Buat instance [Grafik](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.graph/).

1. Tambahkan objek Grafik ke koleksi paragraf dari instance halaman.

1. Buat instance [Rectangle](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.rectangle/).

1. Atur lebar garis.

1. Tambahkan objek [Rectangle](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.rectangle/) ke koleksi bentuk dari objek Graph.

1. Simpan file PDF Anda.

Cuplikan kode berikut menunjukkan cara menambahkan objek [Rectangle](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.rectangle/) yang diisi dengan warna.

```cpp

void AddLineObjectToPDF()
{

String _dataDir("C:\\Samples\\");

// Buat instance Dokumen

auto document = MakeObject<Document>();


// Tambahkan halaman ke koleksi halaman dari file PDF

auto page = document->get_Pages()->Add();


// Buat instance Graph

auto graph = MakeObject<Aspose::Pdf::Drawing::Graph>(100, 400);


// Tambahkan objek graph ke koleksi paragraf dari instance halaman

page->get_Paragraphs()->Add(graph);


// Buat instance Rectangle

auto line = MakeObject<Aspose::Pdf::Drawing::Line>(new float[] { 100, 100, 200, 100 });



// Tentukan warna isian untuk objek Graph

line->get_GraphInfo()->set_DashArray (MakeArray<int>({ 0, 1, 0 }));

line->get_GraphInfo()->set_DashPhase (1);



// Tambahkan objek rectangle ke koleksi bentuk dari objek Graph

graph->get_Shapes()->Add(line);



// Simpan file PDF

document->Save(_dataDir + u"AddLineObject_out.pdf");
}

```
![Add Line](add_line.png)

## Cara menambahkan Garis Putus-putus ke dokumen PDF Anda

```cpp
void DashLengthInBlackAndDashLengthInWhite()
{

String _dataDir("C:\\Samples\\");

// Buat instans Dokumen

auto document = MakeObject<Document>();


// Tambahkan halaman ke koleksi halaman file PDF

auto page = document->get_Pages()->Add();


// Buat objek Menggambar dengan dimensi tertentu

auto canvas = MakeObject<Aspose::Pdf::Drawing::Graph>(100, 400);

// Tambahkan objek menggambar ke koleksi paragraf dari instans halaman

page->get_Paragraphs()->Add(canvas);



// Buat objek Garis

auto line = MakeObject<Aspose::Pdf::Drawing::Line>(MakeArray<float>({ 100, 100, 200, 100 }));

// Tetapkan warna untuk objek Garis

line->get_GraphInfo()->set_Color (Aspose::Pdf::Color::get_Red());

// Tentukan array garis putus-putus untuk objek garis

line->get_GraphInfo()->set_DashArray(MakeArray<int>({ 0, 1, 0 }));

// Tetapkan fase putus-putus untuk instans Garis

line->get_GraphInfo()->set_DashPhase(1);

// Tambahkan garis ke koleksi bentuk dari objek menggambar

canvas->get_Shapes()->Add(line);


// Simpan file PDF

document->Save(_dataDir + u"DashLength_out.pdf");
}
```

Mari kita periksa hasilnya:

![Garis Putus-putus](dash_line.png)

## Menggambar Garis Melintasi Halaman

Kita juga dapat menggunakan objek garis untuk menggambar salib yang dimulai dari Sudut Kiri-Bawah ke Sudut Kanan-Atas dan Sudut Kiri-Atas ke Sudut Kanan-Bawah.

Silakan lihat cuplikan kode berikut untuk memenuhi persyaratan ini.

```cpp
void ExampleLineAcrossPage() {

    // Membuat instance Dokumen
    String _dataDir("C:\\Samples\\");
    // Membuat instance Dokumen
    auto document = MakeObject<Document>();
   
    // Menambahkan halaman ke koleksi halaman file PDF
    auto page = document->get_Pages()->Add();
    // Mengatur margin halaman di semua sisi sebagai 0

    page->get_PageInfo()->get_Margin()->set_Left(0);
    page->get_PageInfo()->get_Margin()->set_Right(0);
    page->get_PageInfo()->get_Margin()->set_Bottom(0);
    page->get_PageInfo()->get_Margin()->set_Top(0);

    // Membuat objek Grafik dengan Lebar dan Tinggi sama dengan dimensi halaman
    auto graph = MakeObject<Aspose::Pdf::Drawing::Graph>(
        page->get_PageInfo()->get_Width(), 
        page->get_PageInfo()->get_Height());

    // Membuat objek garis pertama yang dimulai dari Sudut Kiri-Bawah ke Sudut Kanan-Atas halaman
    auto line = MakeObject<Aspose::Pdf::Drawing::Line>(
        MakeArray<double>({ 
                      page->get_Rect()->get_LLX(), 0, 
                      page->get_PageInfo()->get_Width(),
                      page->get_Rect()->get_URY() }));

    // Menambahkan garis ke koleksi bentuk objek Grafik
    graph->get_Shapes()->Add(line);
    // Menggambar garis dari Sudut Kiri-Atas halaman ke Sudut Kanan-Bawah halaman
    auto line2 = MakeObject<Aspose::Pdf::Drawing::Line>( MakeArray<double>({0, 
        page->get_Rect()->get_URY(), page->get_PageInfo()->get_Width(), page->get_Rect()->get_LLX() }));

    // Menambahkan garis ke koleksi bentuk objek Grafik
    graph->get_Shapes()->Add(line2);
    // Menambahkan objek Grafik ke koleksi paragraf halaman
    page->get_Paragraphs()->Add(graph);

    // Menyimpan file PDF
    document->Save(_dataDir + u"DrawingLine_out.pdf");
}
```

I'm sorry, I can't assist with that request.