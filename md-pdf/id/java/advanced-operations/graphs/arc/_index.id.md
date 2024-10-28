---
title: Menambahkan Objek Busur ke File PDF
linktitle: Tambahkan Busur
type: docs
weight: 10
url: /java/add-arc/
description: Artikel ini menjelaskan cara membuat objek busur ke PDF Anda menggunakan Aspose.PDF untuk Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Menambahkan objek Busur

Aspose.PDF untuk Java mendukung fitur untuk menambah objek grafis (misalnya grafik, garis, persegi panjang, dll.) ke dokumen PDF. Ini juga menawarkan fitur untuk mengisi objek busur dengan warna tertentu.

Ikuti langkah-langkah di bawah ini:

1. Buat instance [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document)

1. Buat [Drawing object](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/package-frame) dengan dimensi tertentu

1. Atur [Border](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/Graph#setBorder-com.aspose.pdf.BorderInfo-) untuk objek Drawing

1. Tambahkan objek [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/Graph) ke koleksi paragraf halaman

1. Simpan file PDF kita


Cuplikan kode berikut menunjukkan cara menambahkan objek [Arc](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/Arc).

```java
    public static void ExampleArc() {
        // Buat instance Dokumen
        Document pdfDocument = new Document();
        // Tambahkan halaman ke koleksi halaman dari file PDF
        Page page = pdfDocument.getPages().add();

        // Buat objek Gambar dengan dimensi tertentu
        Graph graph = new Graph(400, 400);
        // Setel batas untuk objek Gambar
        BorderInfo borderInfo = new BorderInfo(BorderSide.All, Color.getGreen());
        graph.setBorder(borderInfo);

        Arc arc1 = new Arc(100, 100, 95, 0, 90);
        arc1.getGraphInfo().setColor(Color.getGreenYellow());
        graph.getShapes().add(arc1);

        Arc arc2 = new Arc(100, 100, 90, 70, 180);
        arc2.getGraphInfo().setColor(Color.getDarkBlue());
        graph.getShapes().add(arc2);

        Arc arc3 = new Arc(100, 100, 85, 120, 210);
        arc3.getGraphInfo().setColor(Color.getRed());
        graph.getShapes().add(arc3);

        // Tambahkan objek Gambar ke koleksi paragraf dari halaman
        page.getParagraphs().add(graph);

        // Simpan file PDF
        pdfDocument.save(_dataDir + "DrawingArc_out.pdf");

    }
```


## Membuat Objek Arc Terisi

Contoh berikut menunjukkan bagaimana menambahkan objek Arc yang diisi dengan warna dan dimensi tertentu.

```java
    public static void ExampleFilledArc() {
        // Buat instance Dokumen
        Document pdfDocument = new Document();
        // Tambahkan halaman ke koleksi halaman file PDF
        Page page = pdfDocument.getPages().add();

        // Buat objek Gambar dengan dimensi tertentu
        Graph graph = new Graph(400, 400);
        // Atur batas untuk objek Gambar
        BorderInfo borderInfo = new BorderInfo(BorderSide.All, Color.getGreen());
        graph.setBorder(borderInfo);

        Arc arc = new Arc(100, 100, 95, 0, 90);
        arc.getGraphInfo().setFillColor(Color.getGreenYellow());
        graph.getShapes().add(arc);

        Line line = new Line(new float[] { 195, 100, 100, 100, 100, 195 });
        line.getGraphInfo().setFillColor(Color.getGreenYellow());
        graph.getShapes().add(line);

        // Tambahkan objek Gambar ke koleksi paragraf halaman
        page.getParagraphs().add(graph);

        // Simpan file PDF
        pdfDocument.save(_dataDir + "DrawingArc_out.pdf");

    }
```


Mari kita lihat hasil dari menambahkan Arс yang terisi:

![Filled Arc](filled_arc.png)