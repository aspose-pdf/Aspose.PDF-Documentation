---
title: Tambahkan Objek Kurva ke File PDF
linktitle: Tambahkan Kurva
type: docs
weight: 30
url: /id/java/add-curve/
description: Artikel ini menjelaskan cara membuat objek kurva ke PDF Anda menggunakan Aspose.PDF untuk Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Tambahkan objek Kurva

Grafik [Kurva](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/Curve) adalah gabungan garis-garis proyektif yang terhubung, setiap garis bertemu dengan tiga lainnya di titik-titik ganda biasa.

Aspose.PDF untuk Java menunjukkan cara menggunakan kurva Bézier dalam Grafik Anda.
Kurva Bézier banyak digunakan dalam grafik komputer untuk memodelkan kurva halus. Kurva sepenuhnya terkandung dalam cangkang cembung dari titik-titik kontrolnya, titik-titik tersebut dapat ditampilkan secara grafis dan digunakan untuk memanipulasi kurva secara intuitif.
Seluruh kurva terkandung dalam segi empat yang sudut-sudutnya adalah empat titik yang diberikan (cangkang cembung mereka).

Dalam artikel ini, kita akan menyelidiki kurva grafik sederhana, dan kurva yang diisi, yang dapat Anda buat dalam dokumen PDF Anda.

Ikuti langkah-langkah di bawah ini:

1. Buat instance [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

1. Buat [Drawing object](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/package-frame) dengan dimensi tertentu.

1. Atur [Border](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/Graph#setBorder-com.aspose.pdf.BorderInfo-) untuk Drawing object.

1. Tambahkan objek [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/Graph) ke dalam koleksi paragraf halaman.

1. Simpan file PDF Anda

```java
    public static void ExampleCurve() {
        // Buat instance Document
        Document pdfDocument = new Document();
        // Tambahkan halaman ke koleksi halaman file PDF
        Page page = pdfDocument.getPages().add();

        // Buat Drawing object dengan dimensi tertentu
        Graph graph = new Graph(400, 200);
        // Atur border untuk Drawing object
        BorderInfo borderInfo = new BorderInfo(BorderSide.All, Color.getGreen());
        graph.setBorder(borderInfo);

        Curve curve1 = new Curve(new float[] { 10, 10, 50, 60, 70, 10, 100, 120});

        curve1.getGraphInfo().setColor(Color.getGreenYellow());
        graph.getShapes().add(curve1);

        // Tambahkan objek Graph ke dalam koleksi paragraf halaman
        page.getParagraphs().add(graph);

        // Simpan file PDF
        pdfDocument.save(_dataDir + "DrawingCurve1_out.pdf");
    }
```


Gambar berikut menunjukkan hasil yang dieksekusi dengan potongan kode kami:

![Drawing Curve](drawing_curve.png)

## Membuat Objek Kurva Terisi

Contoh ini menunjukkan cara menambahkan objek Kurva yang diisi dengan warna.

```java
    public static void ExampleFilledCurve() {
        // Buat instance Document
        Document pdfDocument = new Document();
        // Tambahkan halaman ke koleksi halaman file PDF
        Page page = pdfDocument.getPages().add();

        // Buat objek Drawing dengan dimensi tertentu
        Graph graph = new Graph(400, 200);
        // Atur batas untuk objek Drawing
        BorderInfo borderInfo = new BorderInfo(BorderSide.All, Color.getGreen());
        graph.setBorder(borderInfo);

        Curve curve1 = new Curve(new float[] { 10, 10, 50, 60, 70, 10, 100, 120});
        curve1.getGraphInfo().setFillColor(Color.getGreenYellow());
        graph.getShapes().add(curve1);

        // Tambahkan objek Graph ke koleksi paragraf halaman
        page.getParagraphs().add(graph);

        // Simpan file PDF
        pdfDocument.save(_dataDir + "DrawingCurve2_out.pdf");
    }
```


Look at the result of adding a filled Curve:

![Kurva Terisi](filled_curve.png)