---
title: Tambahkan Objek Garis ke file PDF
linktitle: Tambahkan Garis
type: docs
weight: 40
url: /id/java/add-line/
description: Artikel ini menjelaskan cara membuat objek garis ke PDF Anda menggunakan Aspose.PDF untuk Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Tambahkan objek Garis

Aspose.PDF untuk Java mendukung fitur untuk menambahkan objek grafis (misalnya grafik, garis, persegi panjang, dll.) ke dokumen PDF. Anda juga mendapatkan keuntungan untuk menambahkan objek [Garis](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/Line) di mana Anda juga dapat menentukan pola garis putus-putus, warna, dan format lainnya untuk elemen Garis.

Ikuti langkah-langkah berikut:

1. Buat instance [Dokumen](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

1. Tambahkan [Halaman](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) ke koleksi halaman dari file PDF.

1. Buat instance [Grafik](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/Graph).

1. Tambahkan objek Grafik ke koleksi paragraf dari instance halaman.

1. Buat instance [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/Rectangle).

1. Tetapkan lebar garis.

1. Tambahkan objek [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/Rectangle) ke koleksi bentuk dari objek Graph.

1. Simpan file PDF Anda.

Cuplikan kode berikut menunjukkan cara menambahkan objek [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/Rectangle) yang diisi dengan warna.

```java
 public static void ExampleLine() {
        // Buat instance Dokumen
        Document pdfDocument = new Document();
        // Tambahkan halaman ke koleksi halaman dari file PDF
        Page page = pdfDocument.getPages().add();
        // Buat instance Graph
        Graph graph = new Graph(100, 400);

        // Tambahkan objek grafik ke koleksi paragraf dari instance halaman
        page.getParagraphs().add(graph);

        // Buat instance Rectangle
        Line line = new Line(new float[] { 100, 100, 200, 100 });
        
        line.getGraphInfo().setLineWidth(5);
        
        // Tambahkan objek persegi panjang ke koleksi bentuk dari objek Graph
        graph.getShapes().add(line);

        // Simpan file PDF
        pdfDocument.save(_dataDir + "LineAdded.pdf");
    }
```


![Add Line](add_line.png)

## Cara menambahkan Garis Putus-putus ke dokumen PDF Anda

```java
public static void ExampleDashedLine() {
        // Buat instance Dokumen
        Document pdfDocument = new Document();
        // Tambahkan halaman ke koleksi halaman file PDF
        Page page = pdfDocument.getPages().add();

        // Buat objek Gambar dengan dimensi tertentu
        Graph canvas = new Graph(100, 400);
        // Tambahkan objek gambar ke koleksi paragraf dari instance halaman
        page.getParagraphs().add(canvas);

        // Buat objek Garis
        Line line = new Line(new float[] { 100, 100, 200, 100 });

        // Atur warna untuk objek Garis
        line.getGraphInfo().setColor(Color.getRed());
        // Tentukan array dash untuk objek garis
        line.getGraphInfo().setDashArray(new int[] { 0, 1, 0 });
        // Atur fase dash untuk instance Garis
        line.getGraphInfo().setDashPhase(1);
        // Tambahkan garis ke koleksi bentuk dari objek gambar
        canvas.getShapes().add(line);
        // Simpan dokumen PDF
        pdfDocument.save(_dataDir + "DashLength_out.pdf");
    }
```


Mari kita periksa hasilnya:

![Garis Putus-putus](dash_line.png)

## Menggambar Garis di Seluruh Halaman

Kita juga dapat menggunakan objek garis untuk menggambar silang mulai dari sudut Kiri-Bawah ke Kanan-Atas dan sudut Kiri-Atas ke Kanan-Bawah.

Silakan lihat potongan kode berikut untuk memenuhi persyaratan ini.

```java
    public static void ExampleLineAcrossPage() {
        // Membuat instance Dokumen
        Document pdfDocument = new Document();
        // Menambahkan halaman ke koleksi halaman dari file PDF
        Page page = pdfDocument.getPages().add();
        // Mengatur margin halaman pada semua sisi menjadi 0

        page.getPageInfo().getMargin().setLeft(0);
        page.getPageInfo().getMargin().setRight(0);
        page.getPageInfo().getMargin().setBottom(0);
        page.getPageInfo().getMargin().setTop(0);

        // Membuat objek Graph dengan Lebar dan Tinggi sama dengan dimensi halaman
        Graph graph = new Graph((float) page.getPageInfo().getWidth(), (float) page.getPageInfo().getHeight());

        // Membuat objek garis pertama mulai dari sudut Kiri-Bawah ke Kanan-Atas halaman
        Line line = new Line(new float[] { (float) page.getRect().getLLX(), 0, (float) page.getPageInfo().getWidth(),
                (float) page.getRect().getURY() });

        // Menambahkan garis ke koleksi shapes dari objek Graph
        graph.getShapes().add(line);
        // Menggambar garis dari sudut Kiri-Atas halaman ke sudut Kanan-Bawah halaman
        Line line2 = new Line(new float[] { 0, (float) page.getRect().getURY(), (float) page.getPageInfo().getWidth(),
                (float) page.getRect().getLLX() });

        // Menambahkan garis ke koleksi shapes dari objek Graph
        graph.getShapes().add(line2);
        // Menambahkan objek Graph ke koleksi paragraf dari halaman
        page.getParagraphs().add(graph);

        // Menyimpan file PDF
        pdfDocument.save(_dataDir + "DrawingLine_out.pdf");
    }
```