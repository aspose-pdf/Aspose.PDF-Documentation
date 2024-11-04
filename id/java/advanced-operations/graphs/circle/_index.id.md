---

title: Tambahkan Objek Lingkaran ke file PDF
linktitle: Tambahkan Lingkaran
type: docs
weight: 20
url: /java/add-circle/
description: Artikel ini menjelaskan cara membuat objek lingkaran ke PDF Anda menggunakan Aspose.PDF untuk Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Tambahkan objek Lingkaran

Seperti grafik batang, grafik lingkaran dapat digunakan untuk menampilkan data dalam sejumlah kategori terpisah. Namun, tidak seperti grafik batang, grafik lingkaran hanya dapat digunakan ketika Anda memiliki data untuk semua kategori yang membentuk keseluruhan. Jadi mari kita lihat menambahkan objek [Lingkaran](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/Circle) dengan Aspose.PDF untuk Java.

Ikuti langkah-langkah di bawah ini:

1. Buat instance [Dokumen](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document)

2. Buat [objek Gambar](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/package-frame) dengan dimensi tertentu


1. Setel [Perbatasan](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/Graph#setBorder-com.aspose.pdf.BorderInfo-) untuk objek Gambar

1. Tambahkan objek [Grafik](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/Graph) ke koleksi paragraf halaman

1. Simpan file PDF kita

```java
public static void ExampleCircle() {
        // Buat instance Dokumen
        Document pdfDocument = new Document();
        // Tambahkan halaman ke koleksi halaman file PDF
        Page page = pdfDocument.getPages().add();

        // Buat objek Gambar dengan dimensi tertentu
        Graph graph = new Graph(400, 200);
        // Setel perbatasan untuk objek Gambar
        BorderInfo borderInfo = new BorderInfo(BorderSide.All, Color.getGreen());
        graph.setBorder(borderInfo);

        Circle circle = new Circle(100,100,40);

        circle.getGraphInfo().setColor(Color.getGreenYellow());
        graph.getShapes().add(circle);

        // Tambahkan objek Grafik ke koleksi paragraf halaman
        page.getParagraphs().add(graph);

        // Simpan file PDF
        pdfDocument.save(_dataDir + "DrawingCircle1_out.pdf");
    }
```


Lingkaran yang kita gambar akan terlihat seperti ini:

![Lingkaran Gambar](drawing_circle.png)

## Membuat Objek Lingkaran Terisi

Contoh ini menunjukkan cara menambahkan objek Lingkaran yang diisi dengan warna.

```java

    public static void ExampleFilledCircle() {
        // Buat instance Dokumen
        Document pdfDocument = new Document();
        // Tambahkan halaman ke koleksi halaman file PDF
        Page page = pdfDocument.getPages().add();

        // Buat objek Gambar dengan dimensi tertentu
        Graph graph = new Graph(400, 200);
        // Atur batas untuk objek Gambar
        BorderInfo borderInfo = new BorderInfo(BorderSide.All, Color.getGreen());
        graph.setBorder(borderInfo);

        Circle circle = new Circle(100,100,40);
        circle.getGraphInfo().setColor(Color.getGreenYellow());       
        circle.getGraphInfo().setFillColor(Color.getGreenYellow());

        graph.getShapes().add(circle);

        // Tambahkan objek Graph ke koleksi paragraf halaman
        page.getParagraphs().add(graph);

        // Simpan file PDF
        pdfDocument.save(_dataDir + "DrawingCircle2_out.pdf");
    }
```


Let's see the result of adding a filled Circle:

Lihat hasil dari menambahkan Lingkaran yang diisi:

![Filled Circle](filled_circle.png)