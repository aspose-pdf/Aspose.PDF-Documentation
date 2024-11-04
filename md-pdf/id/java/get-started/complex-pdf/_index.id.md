---
title: Membuat PDF yang kompleks
linktitle: Membuat PDF yang kompleks
type: docs
weight: 60
url: /java/complex-pdf-example/
description: Aspose.PDF untuk Java memungkinkan Anda membuat dokumen yang lebih kompleks yang berisi gambar, fragmen teks, dan tabel dalam satu dokumen.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Contoh [Hello, World](/pdf/java/hello-world-example/) menunjukkan langkah-langkah sederhana untuk membuat dokumen PDF menggunakan Java dan Aspose.PDF. Dalam artikel ini, kita akan melihat cara membuat dokumen yang lebih kompleks dengan Java dan Aspose.PDF untuk Java. Sebagai contoh, kita akan mengambil dokumen dari perusahaan fiktif yang mengoperasikan layanan feri penumpang. Dokumen kita akan berisi gambar, dua fragmen teks (header dan paragraf), dan sebuah tabel. Untuk membangun dokumen seperti itu, kita akan menggunakan pendekatan berbasis DOM. Anda dapat membaca lebih lanjut di bagian [Dasar-dasar API DOM](/pdf/java/basics-of-dom-api/).

Jika kita membuat dokumen dari awal, kita perlu mengikuti langkah-langkah tertentu:

1. Instansiasi objek [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document). Pada langkah ini kita akan membuat dokumen PDF kosong dengan beberapa metadata tetapi tanpa halaman.
1. Tambahkan [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page) ke objek dokumen. Jadi, sekarang dokumen kita akan memiliki satu halaman.
1. Tambahkan [Image](https://reference.aspose.com/pdf/java/com.aspose.pdf/image). Ini adalah operasi kompleks berdasarkan tindakan tingkat rendah dengan operator PDF.
    - Muat gambar dari aliran
    - Tambahkan gambar ke koleksi Images dari Sumber Daya Halaman
    - Menggunakan operator GSave: operator ini menyimpan status grafik saat ini.
    - Buat objek [Matrix](https://reference.aspose.com/pdf/java/com.aspose.pdf/matrix/).
    - Menggunakan operator ConcatenateMatrix: mendefinisikan bagaimana gambar harus ditempatkan.
    - Menggunakan operator Do: operator ini menggambar gambar.
    - Menggunakan operator GRestore: operator ini mengembalikan status grafik.

1. Buat [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragment) untuk header. Untuk header kita akan menggunakan font Arial dengan ukuran font 24pt dan perataan tengah.
1. Tambahkan header ke [Paragraphs](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#getParagraphs--).
1. Buat [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragment) untuk deskripsi. Untuk deskripsi kita akan menggunakan font Arial dengan ukuran font 24pt dan perataan tengah.
1. Tambahkan (deskripsi) ke Paragraphs halaman.
1. Buat tabel, tambahkan properti tabel.
1. Tambahkan (tabel) ke [Paragraphs](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#getParagraphs--).
1. Simpan dokumen "Complex.pdf".

```java
package com.aspose.pdf.examples;

/**
 * Contoh Kompleks
 */

import java.io.FileNotFoundException;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.time.Duration;
import java.time.LocalTime;

import com.aspose.pdf.*;
import com.aspose.pdf.operators.ConcatenateMatrix;
import com.aspose.pdf.operators.Do;
import com.aspose.pdf.operators.GRestore;
import com.aspose.pdf.operators.GSave;

public final class ComplexExample {

    private ComplexExample() {
    }

    private static Path _dataDir = Paths.get("/home/admin1/pdf-examples/");

    public static void main(String[] args) throws FileNotFoundException {
        // Inisialisasi objek dokumen
        Document document = new Document();
        // Tambahkan halaman
        Page page = document.getPages().add();

        // -------------------------------------------------------------
        // Tambahkan gambar
        Path imageFileName = Paths.get(_dataDir.toString(), "logo.png");
        java.io.FileInputStream imageStream = new java.io.FileInputStream(new java.io.File(imageFileName.toString()));
        // Tambahkan gambar ke koleksi Images dari Sumber Daya Halaman
        page.getResources().getImages().add(imageStream);

        // Menggunakan operator GSave: operator ini menyimpan status grafik saat ini
        page.getContents().add(new GSave());
        Rectangle _logoPlaceHolder = new Rectangle(20, 730, 120, 830);

        // Buat objek Matrix
        Matrix matrix = new Matrix(new double[] {
            _logoPlaceHolder.getURX() - _logoPlaceHolder.getLLX(), 0, 0,
            _logoPlaceHolder.getURY() - _logoPlaceHolder.getLLY(),
            _logoPlaceHolder.getLLX(), _logoPlaceHolder.getLLY() });

        // Menggunakan operator ConcatenateMatrix (menggabungkan matriks): mendefinisikan bagaimana gambar harus ditempatkan
        page.getContents().add(new ConcatenateMatrix(matrix));
        XImage ximage = page.getResources().getImages().get_Item(page.getResources().getImages().size());
        // Menggunakan operator Do: operator ini menggambar gambar
        page.getContents().add(new Do(ximage.getName()));
        // Menggunakan operator GRestore: operator ini mengembalikan status grafik
        page.getContents().add(new GRestore());

        // -------------------------------------------------------------
        // Tambahkan Header
        TextFragment header = new TextFragment("Rute feri baru pada musim gugur 2020");
        header.getTextState().setFont(FontRepository.findFont("Arial"));
        header.getTextState().setFontSize(24);
        header.setHorizontalAlignment(HorizontalAlignment.Center);
        header.setPosition(new Position(130, 720));
        page.getParagraphs().add(header);

        // Tambahkan deskripsi
        String descriptionText = "Pengunjung harus membeli tiket secara online dan tiket dibatasi hingga 5.000 per hari. Layanan feri beroperasi dengan setengah kapasitas dan dengan jadwal yang dikurangi. Harap antri.";
        TextFragment description = new TextFragment(descriptionText);
        description.getTextState().setFont(FontRepository.findFont("Times New Roman"));
        description.getTextState().setFontSize(14);
        description.setHorizontalAlignment(HorizontalAlignment.Left);
        page.getParagraphs().add(description);

        // Tambahkan tabel
        Table table = new Table();
        table.setColumnWidths("200");
        table.setBorder(new BorderInfo(BorderSide.Box, 1f, Color.getDarkSlateGray()));
        table.setDefaultCellBorder(new BorderInfo(BorderSide.Box, 0.5f, Color.getBlack()));
        table.getMargin().setBottom(10);
        table.getDefaultCellTextState().setFont(FontRepository.findFont("Helvetica"));

        Row headerRow = table.getRows().add();
        headerRow.getCells().add("Berangkat dari Kota");
        headerRow.getCells().add("Berangkat dari Pulau");

        for (Cell headerRowCell : headerRow.getCells())
        {
            headerRowCell.setBackgroundColor(Color.getGray());
            headerRowCell.getDefaultCellTextState().setForegroundColor(Color.getWhiteSmoke());
        }

        LocalTime time = LocalTime.of(6, 0);
        Duration incTime = Duration.ofMinutes(30);

        for (int i = 0; i < 10; i++)
        {
            Row dataRow = table.getRows().add();
            dataRow.getCells().add(time.toString());
            time = time.plus(incTime);
            dataRow.getCells().add(time.toString());
        }

        page.getParagraphs().add(table);

        document.save(Paths.get(_dataDir.toString(), "Complex.pdf").toString());
    }

}
```