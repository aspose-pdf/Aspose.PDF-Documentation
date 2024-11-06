---
title: Tambahkan Objek Persegi Panjang ke file PDF
linktitle: Tambahkan Persegi Panjang
type: docs
weight: 50
url: id/java/add-rectangle/
description: Artikel ini menjelaskan cara membuat objek Persegi Panjang ke PDF Anda menggunakan Aspose.PDF untuk Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Tambahkan objek Persegi Panjang

Aspose.PDF untuk Java mendukung fitur untuk menambahkan objek grafik (misalnya grafik, garis, persegi panjang dll.) ke dokumen PDF. Anda juga mendapatkan keuntungan untuk menambahkan objek [Persegi Panjang](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/Rectangle) di mana Anda juga menawarkan fitur untuk mengisi objek persegi panjang dengan warna tertentu, mengontrol Z-Order, menambahkan isian warna gradasi dan lain-lain.

Pertama, mari kita lihat kemungkinan membuat objek Persegi Panjang.

Ikuti langkah-langkah di bawah ini:

1. Buat [Dokumen](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) PDF baru

1. Tambahkan [Halaman](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) ke koleksi halaman file PDF

1. Tambahkan [Fragmen Teks](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragment) ke koleksi paragraf dari instance halaman

1. Buat instansi [Grafik](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/Graph)

1. Atur batas untuk [objek Gambar](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/package-frame)

1. Buat instansi Persegi Panjang

1. Tambahkan objek [Persegi Panjang](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/Rectangle) ke koleksi bentuk dari objek Grafik

1. Tambahkan objek grafik ke koleksi paragraf dari instance halaman

1. Tambahkan [Fragmen Teks](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragment) ke koleksi paragraf dari instance halaman

1. Dan simpan file PDF Anda

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.BorderInfo;
import com.aspose.pdf.BorderSide;
import com.aspose.pdf.Color;
import com.aspose.pdf.Document;
import com.aspose.pdf.Page;
import com.aspose.pdf.Point;
import com.aspose.pdf.TextFragment;
import com.aspose.pdf.drawing.*;

public class WorkingWithGraphs {

    private static String _dataDir = "/home/aspose/pdf-examples/Samples/";

    public static void ExampleRectangle() {

        // Buat dokumen PDF baru
        Document pdfDocument = new Document();

        // Tambahkan halaman ke koleksi halaman dari file PDF
        Page page = pdfDocument.getPages().add();

        // Tambahkan fragmen teks ke koleksi paragraf dari instance halaman
        page.getParagraphs().add(new TextFragment("Teks sebelum objek Grafik"));

        // Buat instansi Grafik
        Graph graph = new Graph(400, 200);

        // Atur batas untuk objek Gambar
        BorderInfo borderInfo = new BorderInfo(BorderSide.All, Color.getRed());
        graph.setBorder(borderInfo);

        // Buat instansi Persegi Panjang
        Rectangle rect = new Rectangle(10, 10, 380, 180);

        // Tambahkan objek persegi panjang ke koleksi bentuk dari objek Grafik
        graph.getShapes().add(rect);

        // Tambahkan objek grafik ke koleksi paragraf dari instance halaman
        page.getParagraphs().add(graph);

        // Tambahkan fragmen teks ke koleksi paragraf dari instance halaman
        page.getParagraphs().add(new TextFragment("Teks setelah objek Grafik"));

        // Simpan file PDF
        pdfDocument.save(_dataDir + "CreateRectangle_out.pdf");
    }
```


![Create Rectangle](create_rectangle.png)

## Membuat Objek Persegi Panjang Terisi

Aspose.PDF untuk Java juga menawarkan fitur untuk mengisi objek persegi panjang dengan warna tertentu.

Cuplikan kode berikut menunjukkan cara menambahkan objek [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/Rectangle) yang diisi dengan warna.

```java
   public static void ExampleRectangleFilledSolidColor() {

        Document pdfDocument = new Document();

        // Tambahkan halaman ke koleksi halaman dari file PDF
        Page page = pdfDocument.getPages().add();
        // Buat instance Graph
        Graph graph = new Graph(100, 400);

        // Tambahkan objek grafik ke koleksi paragraf dari instance halaman
        page.getParagraphs().add(graph);

        // Buat instance Rectangle
        Rectangle rect = new Rectangle(100, 100, 200, 120);

        // Tentukan warna isi untuk objek Graph
        rect.getGraphInfo().setFillColor(Color.getRed());

        // Tambahkan objek persegi panjang ke koleksi shapes dari objek Graph
        graph.getShapes().add(rect);

        // Simpan file PDF
        pdfDocument.save(_dataDir + "CreateFilledRectangle_out.pdf");
    }
```


Lihatlah hasil dari persegi panjang yang diisi dengan warna solid:

![Filled Rectangle](fill_rectangle.png)

## Menambahkan Gambar dengan Isi Gradien

Aspose.PDF untuk Java mendukung fitur untuk menambahkan objek grafis ke dokumen PDF dan terkadang diperlukan untuk mengisi objek grafis dengan Warna Gradien. Untuk Mengisi objek grafis dengan Warna Gradien, kita perlu mengatur setPatterColorSpace dengan objek gradientAxialShading seperti berikut.

Cuplikan kode berikut menunjukkan cara menambahkan objek [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/Rectangle) yang diisi dengan Warna Gradien.

```java
   public static void ExampleRectangleFilledGradient() {

        Document pdfDocument = new Document();
        Page page = pdfDocument.getPages().add();

        Graph graph = new Graph(300, 300);
        page.getParagraphs().add(graph);
        Rectangle rect = new Rectangle(0, 0, 300, 300);
        graph.getShapes().add(rect);

        // Tentukan warna isi Gradien untuk objek Grafis dan isi
        Color gradientFill = new com.aspose.pdf.Color();
        rect.getGraphInfo().setFillColor(gradientFill);

        GradientAxialShading gradientAxialShading = new GradientAxialShading(Color.getRed(), Color.getBlue());

        gradientAxialShading.setStart(new Point(0, 0));
        gradientAxialShading.setEnd(new Point(300, 300));
        gradientFill.setPatternColorSpace(gradientAxialShading);

        // Simpan file PDF
        pdfDocument.save(_dataDir + "AddDrawingWithGradientFill_out.pdf");
    }
```


![Gradient Rectangle](gradient.png)

## Membuat Persegi Panjang dengan Saluran Warna Alpha

Aspose.PDF untuk Java mendukung pengisian objek persegi panjang dengan warna tertentu. Objek persegi panjang juga dapat memiliki saluran warna Alpha untuk memberikan tampilan transparan. Cuplikan kode berikut menunjukkan cara menambahkan objek [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/Rectangle) dengan saluran warna Alpha.

Piksel dari gambar dapat menyimpan informasi tentang opasitas mereka bersama dengan nilai warna. Ini memungkinkan pembuatan gambar dengan area transparan atau semi-transparan.

Alih-alih membuat warna menjadi transparan, setiap piksel menyimpan informasi tentang seberapa buram itu. Data opasitas ini disebut saluran alpha dan biasanya disimpan setelah saluran warna piksel.

Dalam cuplikan kode kami, kami menggunakan metode [fromArgb](https://reference.aspose.com/pdf/java/com.aspose.pdf/Color#fromArgb-int-int-int-) dari [com.aspose.pdf.Color](https://reference.aspose.com/pdf/java/com.aspose.pdf/Color).
 Kita perlu menentukan nilai di mana 3 yang pertama adalah komponen warna, ditentukan dalam rentang 0 hingga 255, dan yang terakhir adalah tingkat opasitas (saluran alfa), ditentukan oleh angka pecahan dari 0 hingga 1.

```java
    public static void ExampleRectangleAlphaChannelColor() {
        Document pdfDocument = new Document();
        Page page = pdfDocument.getPages().add();

        // Buat instance Graph
        Graph graph = new Graph(100, 400);

        // Buat objek persegi panjang dengan dimensi spesifik
        Rectangle rect1 = new Rectangle(100, 100, 200, 100);
        Color color1 = Color.fromArgb(128, 224, 0, 224);
        rect1.getGraphInfo().setFillColor(color1);
        // Tambahkan objek persegi panjang ke koleksi bentuk dari instance Graph
        graph.getShapes().add(rect1);

        // Buat objek persegi panjang kedua
        Rectangle rect2 = new Rectangle(200, 150, 200, 100);
        Color color2 = Color.fromArgb(64, 0, 224, 224);
        rect2.getGraphInfo().setFillColor(color2);
        graph.getShapes().add(rect2);

        // Tambahkan instance graph ke koleksi paragraf dari objek halaman
        page.getParagraphs().add(graph);

        // Simpan file PDF
        pdfDocument.save(_dataDir + "CreateRectangleWithAlphaColor_out.pdf");
    }
```

![Rectangle Alpha Channel Color](rectangle_color.png)

## Kontrol Z-Order dari Persegi Panjang

Aspose.PDF untuk Java mendukung fitur untuk menambahkan objek grafis (misalnya grafik, garis, persegi panjang, dll.) ke dokumen PDF. Ketika menambahkan lebih dari satu instance dari objek yang sama ke dalam file PDF, kita dapat mengendalikan rendering mereka dengan menentukan Z-Order. Z-Order juga digunakan ketika kita perlu merender objek di atas satu sama lain.

Cuplikan kode berikut menunjukkan langkah-langkah untuk merender objek [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/Rectangle) di atas satu sama lain.

```java
   public static void Controlling_Z_Order() {

        Document pdfDocument = new Document();
        Page page = pdfDocument.getPages().add();

        // Membuat persegi panjang baru dengan Warna Merah, Z-Order 0 dan dimensi tertentu
        AddRectangle(page, 50, 40, 60, 40, Color.getRed(), 2);
        // Membuat persegi panjang baru dengan Warna Biru, Z-Order 0 dan dimensi
        // tertentu
        AddRectangle(page, 20, 20, 30, 30, Color.getBlue(), 1);
        // Membuat persegi panjang baru dengan Warna Hijau, Z-Order 0 dan dimensi
        // tertentu
        AddRectangle(page, 40, 40, 60, 30, Color.getGreen(), 0);

        // Menyimpan file PDF hasil
        pdfDocument.save(_dataDir + "ControlRectangleZOrder_out.pdf");

    }
```


![Mengontrol Urutan Z](control.png)