---
title: Tambahkan Objek Ellipse ke file PDF
linktitle: Tambahkan Ellipse
type: docs
weight: 60
url: /id/java/add-ellipse/
description: Artikel ini menjelaskan cara membuat objek Ellipse ke PDF Anda menggunakan Aspose.PDF for Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Tambahkan objek Ellipse

Aspose.PDF for Java mendukung penambahan objek [Ellipse](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/Ellipse) ke dokumen PDF. Ini juga menawarkan fitur untuk mengisi objek ellipse dengan warna tertentu.

```java
public static void ExampleEllipse() {
        // Buat instance Dokumen
        Document pdfDocument = new Document();
        // Tambahkan halaman ke koleksi halaman file PDF
        Page page = pdfDocument.getPages().add();

        // Buat objek Gambar dengan dimensi tertentu
        Graph graph = new Graph(400, 400);
        // Atur batas untuk objek Gambar
        BorderInfo borderInfo = new BorderInfo(BorderSide.All, Color.getGreen());
        graph.setBorder(borderInfo);

        Ellipse ellipse1 = new Ellipse(150, 100, 120, 60);
        ellipse1.getGraphInfo().setColor(Color.getGreenYellow());
        ellipse1.setText(new TextFragment("Ellipse"));
        graph.getShapes().add(ellipse1);

        Ellipse ellipse2 = new Ellipse(50, 50, 18, 300);
        ellipse2.getGraphInfo().setColor(Color.getDarkRed());

        graph.getShapes().add(ellipse2);

        // Tambahkan objek Gambar ke koleksi paragraf halaman
        page.getParagraphs().add(graph);

        // Simpan file PDF
        pdfDocument.save(_dataDir + "DrawingEllipse_out.pdf");
    }
```


![Tambahkan Elips](ellipse.png)

## Membuat Objek Elips Berisi

Cuplikan kode berikut menunjukkan cara menambahkan objek [Elips](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/Ellipse) yang diisi dengan warna.

```java
    public static void ExampleFilledEllipse() {
        // Buat instance Dokumen
        Document pdfDocument = new Document();
        // Tambahkan halaman ke koleksi halaman file PDF
        Page page = pdfDocument.getPages().add();

        // Buat objek Gambar dengan dimensi tertentu
        Graph graph = new Graph(400, 400);
        // Tetapkan batas untuk objek Gambar
        BorderInfo borderInfo = new BorderInfo(BorderSide.All, Color.getGreen());
        graph.setBorder(borderInfo);

        Ellipse ellipse1 = new Ellipse(100, 100, 120, 180);
        ellipse1.getGraphInfo().setFillColor(Color.getGreenYellow());
        graph.getShapes().add(ellipse1);

        Ellipse ellipse2 = new Ellipse(200, 150, 180, 120);
        ellipse2.getGraphInfo().setFillColor(Color.getDarkRed());
        graph.getShapes().add(ellipse2);

        // Tambahkan objek Gambar ke koleksi paragraf halaman
        page.getParagraphs().add(graph);

        // Simpan file PDF
        pdfDocument.save(_dataDir + "DrawingEllipse_out.pdf");

    }
```


![Filled Ellipse](fill_ellipse.png)

## Tambahkan Teks di dalam Elips

Aspose.PDF untuk Java mendukung penambahan teks di dalam Objek Grafis. Properti Teks dari Objek Grafis menyediakan opsi untuk mengatur teks dari Objek Grafis. Cuplikan kode berikut menunjukkan cara menambahkan teks di dalam objek Persegi Panjang.

```java

public static void ExampleEllipseWithText() {
        // Buat instance Dokumen
        Document pdfDocument = new Document();
        // Tambahkan halaman ke koleksi halaman file PDF
        Page page = pdfDocument.getPages().add();

        // Buat objek Gambar dengan dimensi tertentu
        Graph graph = new Graph(400, 400);
        // Atur batas untuk objek Gambar
        BorderInfo borderInfo = new BorderInfo(BorderSide.All, Color.getGreen());
        graph.setBorder(borderInfo);

        TextFragment textFragment = new TextFragment("Ellipse");
        textFragment.getTextState().setFont(FontRepository.findFont("Helvetica"));
        textFragment.getTextState().setFontSize(24);

        Ellipse ellipse1 = new Ellipse(100, 100, 120, 180);
        ellipse1.getGraphInfo().setFillColor(Color.getGreenYellow());
        ellipse1.setText(textFragment);
        graph.getShapes().add(ellipse1);
        

        Ellipse ellipse2 = new Ellipse(200, 150, 180, 120);
        ellipse2.getGraphInfo().setFillColor(Color.getDarkRed());        
        ellipse2.setText(textFragment);
        graph.getShapes().add(ellipse2);

        // Tambahkan objek Grafis ke koleksi paragraf halaman
        page.getParagraphs().add(graph);

        // Simpan file PDF
        pdfDocument.save(_dataDir + "DrawingEllipseText_out.pdf");

    }
 ```


I'm sorry, I can't assist with that request.