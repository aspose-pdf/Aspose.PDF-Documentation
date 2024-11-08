---
title: Bekerja dengan Artefak
linktitle: Bekerja dengan Artefak
type: docs
weight: 110
url: /id/java/artifacts/
description: Halaman ini menjelaskan cara bekerja dengan kelas Artefak menggunakan Aspose.PDF untuk Java. Cuplikan kode menunjukkan cara menambahkan gambar latar belakang ke halaman PDF dan cara mendapatkan setiap watermark di halaman pertama file PDF.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Artefak umumnya adalah objek grafis atau tanda lain yang bukan bagian dari konten yang dibuat. Dalam contoh PDF Anda, artefak mencakup informasi berbeda, ada header atau footer halaman, garis atau grafik lainnya yang memisahkan bagian halaman, atau gambar dekoratif.

Kelas [Artifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/Artifact) berisi:

- [Artifact.Type](https://reference.aspose.com/pdf/java/com.aspose.pdf/Artifact.ArtifactType) – mendapatkan tipe artefak (mendukung nilai dari enumerasi Artifact.ArtifactType di mana nilai termasuk Background, Layout, Page, Pagination, dan Undefined).
- [Artifact.Subtype](https://reference.aspose.com/pdf/java/com.aspose.pdf/Artifact.ArtifactSubtype) – mendapatkan subtipe artefak (mendukung nilai dari enumerasi Artifact.ArtifactSubtype di mana nilainya termasuk Latar Belakang, Footer, Header, Tidak Ditentukan, Watermark).

Watermark yang dibuat dengan Adobe Acrobat disebut artefak (sebagaimana dijelaskan dalam 14.8.2.2 Konten Nyata dan Artefak dari spesifikasi PDF). Untuk bekerja dengan artefak, Aspose.PDF memiliki dua kelas: [Artifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/Artifact) dan [ArtifactCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/ArtifactCollection).

Untuk mendapatkan semua artefak pada halaman tertentu, kelas [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) memiliki properti Artifacts. Topik ini menjelaskan cara bekerja dengan artefak dalam file PDF.

Cuplikan kode berikut menunjukkan cara mengatur watermark pada halaman pertama dari file PDF.

```java

 public class ExamplesArtifacts {

    private static String _dataDir = "/home/aspose/pdf-examples/Samples/Artifacts/";

    public static void SetWatermark(){
        Document doc = new Document(_dataDir + "sample.pdf");
        WatermarkArtifact artifact = new WatermarkArtifact();        
        artifact.setText(new FormattedText("WATERMARK", java.awt.Color.BLUE, 
                            FontStyle.Courier,
                            EncodingType.Identity_h, true, 72));
        artifact.setArtifactHorizontalAlignment (HorizontalAlignment.Center);
        artifact.setArtifactVerticalAlignment (VerticalAlignment.Center);
        artifact.setRotation (45);
        artifact.setOpacity (0.5);
        artifact.setBackground (true);
        doc.getPages().get_Item(1).getArtifacts().add(artifact);
        doc.save(_dataDir + "watermark.pdf");
    }
```


Gambar latar belakang dapat digunakan untuk menambahkan watermark atau desain halus lainnya ke dokumen. Dalam Aspose.PDF untuk Java, setiap dokumen PDF adalah kumpulan halaman dan setiap halaman berisi kumpulan artefak. Kelas [BackgroundArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/BackgroundArtifact) dapat digunakan untuk menambahkan gambar latar belakang ke objek halaman.

Cuplikan kode berikut menunjukkan cara menambahkan gambar latar belakang ke halaman PDF menggunakan objek BackgroundArtifact.

```java

    public static void SetBackground() throws FileNotFoundException {

        // Buka dokumen
        Document pdfDocument = new Document();
                
        // Tambahkan halaman baru ke objek dokumen
        Page page = pdfDocument.getPages().add();

        // Buat objek Background Artifact
        BackgroundArtifact background = new BackgroundArtifact();

        // Tentukan gambar untuk objek backgroundartifact
        background.setBackgroundImage(new java.io.FileInputStream(new java.io.File(_dataDir + "background.png")));
        
        // Tambahkan BackgroundArtifact ke koleksi artefak halaman
        page.getArtifacts().add(background);

        // Simpan PDF yang telah dimodifikasi
        pdfDocument.save(_dataDir + "ImageAsBackground_out.pdf");

    }
```


## Contoh Pemrograman: Mendapatkan Watermark

Cuplikan kode berikut menunjukkan cara mendapatkan setiap watermark pada halaman pertama dari file PDF.

```java
    public static void GettingWatermarks() {
        // Buka dokumen
        Document pdfDocument = new Document(_dataDir +  "watermark_new.pdf");
        // Iterasi dan dapatkan sub-jenis, teks, dan lokasi artefak
        for (Artifact artifact : pdfDocument.getPages().get_Item(1).getArtifacts())
        {
            System.out.println(artifact.getSubtype() + " " + artifact.getText() + " " + artifact.getRectangle().toString());
        }
```

## Contoh Pemrograman: Menghitung Artefak dari Jenis Tertentu

Untuk menghitung jumlah total artefak dari jenis tertentu (misalnya, jumlah total watermark), gunakan kode berikut:

```java
    public static void CountingArtifacts() {
        // Buka dokumen
        Document pdfDocument = new Document(_dataDir +  "watermark_new.pdf");
        int count = 0;
        for (Artifact artifact : pdfDocument.getPages().get_Item(1).getArtifacts())
        {
            // Jika jenis artefak adalah watermark, tingkatkan penghitung
            if (artifact.getSubtype() == Artifact.ArtifactSubtype.Watermark) count++;
        }
        System.out.println("Halaman berisi " + count + " watermark");
    }
```