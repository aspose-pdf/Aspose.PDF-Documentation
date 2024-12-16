---
title: Mengelola Header dan Footer
type: docs
weight: 40
url: /id/java/manage-header-and-footer/
description: Bagian ini menjelaskan cara mengelola Header dan Footer dengan Aspose.PDF Facades menggunakan Kelas PdfFileStamp.
lastmod: "2021-06-05"
draft: false
---

## Menambahkan Header dalam File PDF

Kelas [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) memungkinkan Anda untuk menambahkan header dalam file PDF.
 Dalam rangka menambahkan header, Anda pertama-tama perlu membuat objek dari kelas [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp). Anda dapat memformat teks header menggunakan kelas [FormattedText](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormattedText). Setelah Anda siap untuk menambahkan header dalam file, Anda perlu memanggil metode [addHeader](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#addHeader-com.aspose.pdf.facades.FormattedText-float-) dari kelas [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp). Anda juga perlu menentukan setidaknya margin atas dalam metode [addHeader](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#addHeader-com.aspose.pdf.facades.FormattedText-float-). Terakhir, simpan file PDF keluaran menggunakan metode [close](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#close--) dari kelas [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp). Cuplikan kode berikut menunjukkan cara menambahkan header dalam file PDF.

```java
 public static void AddHeader() {
        // Buat objek PdfFileStamp
        PdfFileStamp fileStamp = new PdfFileStamp();

        // Buka Dokumen
        fileStamp.bindPdf(_dataDir + "sample.pdf");

        // Buat teks berformat untuk nomor halaman
        FormattedText formattedText = new FormattedText("Aspose - Ahli Format File Anda!", java.awt.Color.YELLOW,
                java.awt.Color.BLACK, FontStyle.Courier, EncodingType.Winansi, false, 14);

        // Tambahkan header
        fileStamp.addHeader(formattedText, 20);

        // Simpan file PDF yang diperbarui
        fileStamp.save(_dataDir + "AddHeader_out.pdf");

        // Tutup fileStamp
        fileStamp.close();
    }
```

## Tambahkan Footer dalam File PDF

Kelas [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) memungkinkan Anda untuk menambahkan footer dalam file PDF.
 Untuk menambahkan footer, pertama-tama Anda perlu membuat objek dari kelas [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp). Anda dapat memformat teks footer menggunakan kelas [FormattedText](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormattedText). Setelah Anda siap untuk menambahkan footer ke dalam file, Anda perlu memanggil metode [addFooter](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#addFooter-com.aspose.pdf.facades.FormattedText-float-) dari kelas [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp). Anda juga perlu menentukan setidaknya margin bawah dalam metode [addFooter](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#addFooter-com.aspose.pdf.facades.FormattedText-float-). Terakhir, simpan file PDF keluaran menggunakan metode [close](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#close--) dari kelas [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp). Cuplikan kode berikut menunjukkan kepada Anda cara menambahkan footer dalam file PDF.

```java
 public static void AddFooter() {
        // Buat objek PdfFileStamp
        PdfFileStamp fileStamp = new PdfFileStamp();

        // Buka Dokumen
        fileStamp.bindPdf(_dataDir + "sample.pdf");

        // Buat teks terformat untuk nomor halaman
        FormattedText formattedText = new FormattedText("Aspose - Ahli Format File Anda!", java.awt.Color.BLUE,
                java.awt.Color.GRAY, FontStyle.Courier, EncodingType.Winansi, false, 14);

        // Tambahkan footer
        fileStamp.addFooter(formattedText, 10);

        // Simpan file PDF yang diperbarui
        fileStamp.save(_dataDir + "AddFooter_out.pdf");

        // Tutup fileStamp
        fileStamp.close();
    }
```

## Tambahkan Gambar di Header File PDF yang Ada

Kelas [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) memungkinkan Anda untuk menambahkan gambar di header file PDF.
 Untuk menambahkan gambar di header, Anda pertama-tama perlu membuat objek dari kelas [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp). Setelah itu, Anda perlu memanggil metode [addHeader](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#addHeader-com.aspose.pdf.facades.FormattedText-float-) dari kelas [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp). Anda dapat mengirimkan gambar ke metode [addHeader](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#addHeader-com.aspose.pdf.facades.FormattedText-float-). Akhirnya, simpan file PDF keluaran menggunakan metode [close](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#close--) dari kelas [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp). Cuplikan kode berikut menunjukkan cara menambahkan gambar di header file PDF.

```java
public static void AddImageHeader() {
        // Buat objek PdfFileStamp
        PdfFileStamp fileStamp = new PdfFileStamp();

        // Buka Dokumen
        fileStamp.bindPdf(_dataDir + "sample.pdf");
        FileInputStream fs;
        try {
            fs = new FileInputStream(_dataDir + "aspose-logo.png");
            // Tambahkan Header
            fileStamp.addHeader(fs, 10);

            // Simpan file PDF yang diperbarui
            fileStamp.save(_dataDir + "AddImage-Header_out.pdf");
        } catch (FileNotFoundException e) {

            e.printStackTrace();
        }

        // Tutup fileStamp
        fileStamp.close();
    }
```

## Tambahkan Gambar di Footer dari File PDF yang Ada

Kelas [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) memungkinkan Anda untuk menambahkan gambar di footer dari file PDF.
 Untuk menambahkan gambar di footer, pertama-tama Anda perlu membuat objek dari kelas [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp). Setelah itu, Anda perlu memanggil metode [addFooter](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#addFooter-com.aspose.pdf.facades.FormattedText-float-) dari kelas [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp). Anda dapat melewatkan gambar ke metode [addFooter](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#addFooter-com.aspose.pdf.facades.FormattedText-float-). Terakhir, simpan file PDF output menggunakan metode [close](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#close--) dari kelas [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp). Cuplikan kode berikut menunjukkan bagaimana menambahkan gambar di footer file PDF.

```java
    public static void AddImageFooter() {
        // Buat objek PdfFileStamp
        PdfFileStamp fileStamp = new PdfFileStamp();

        // Buka Dokumen
        fileStamp.bindPdf(_dataDir + "sample.pdf");
        FileInputStream fs;
        try {
            fs = new FileInputStream(_dataDir + "aspose-logo.png");
            // Tambahkan footer
            fileStamp.addFooter(fs, 10);

            // Simpan file PDF yang diperbarui
            fileStamp.save(_dataDir + "AddImage-Footer_out.pdf");
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }

        // Tutup fileStamp
        fileStamp.close();
    }
```