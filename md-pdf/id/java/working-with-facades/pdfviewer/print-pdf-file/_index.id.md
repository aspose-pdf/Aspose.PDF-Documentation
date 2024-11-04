---
title: Bekerja dengan Pencetakan PDF
type: docs
weight: 10
url: /java/print-pdf-file/
description: Bagian ini menjelaskan cara mencetak file PDF dengan Aspose.PDF Facades menggunakan Kelas PdfViewer.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Mencetak File PDF ke Printer Default menggunakan Pengaturan Printer dan Halaman

Kelas [PdfViewer](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfViewer) memungkinkan Anda untuk mencetak file PDF ke printer default. Oleh karena itu, Anda perlu membuat objek [PdfViewer](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfViewer) dan membuka PDF menggunakan metode openPdfFile(..).

Panggil metode printDocument(..) untuk mencetak PDF ke printer default.

Cuplikan kode berikut menunjukkan cara mencetak PDF ke printer default dengan Pengaturan printer dan halaman.

```java
 public static void PrintingPDFFile() {
        // Buat objek PdfViewer
        PdfViewer viewer = new PdfViewer();

        // Buka file PDF input
        viewer.bindPdf(_dataDir + "sample.pdf");

        // Tetapkan atribut untuk pencetakan
        viewer.setAutoResize(true); // Cetak file dengan ukuran yang disesuaikan
        viewer.setAutoRotate(true); // Cetak file dengan rotasi yang disesuaikan
        viewer.setPrintPageDialog(false); // Jangan tampilkan dialog nomor halaman saat mencetak

        // Buat objek untuk pengaturan printer dan halaman serta PrintDocument
        PdfPrinterSettings printerSettings = new PdfPrinterSettings();
        PrintPageSettings pageSettings = new PrintPageSettings();

        // Tetapkan nama printer
        printerSettings.setPrinterName("Microsoft Print to PDF");
        
        // Tetapkan UkuranHalaman (jika diperlukan)
        pageSettings.setPaperSize(new PrintPaperSize("A4", 827, 1169));

        // Tetapkan MarginHalaman (jika diperlukan)
        pageSettings.setMargins(new PrinterMargins(0, 0, 0, 0));

        // Cetak dokumen menggunakan pengaturan printer dan halaman
        viewer.printDocumentWithSettings(pageSettings, printerSettings);
        
        // Tutup file PDF setelah mencetak
        viewer.close();
    }
```


Untuk menampilkan dialog cetak, coba gunakan cuplikan kode berikut:

```java
public static void PrintingPDFDisplayPrintDialog() {
        // Buat objek PdfViewer
        PdfViewer viewer = new PdfViewer();

        // Buka file PDF input
        viewer.bindPdf(_dataDir + "sample.pdf");

        // Atur atribut untuk pencetakan
        viewer.setAutoResize(true); // Cetak file dengan ukuran yang disesuaikan
        viewer.setAutoRotate(true); // Cetak file dengan rotasi yang disesuaikan
        viewer.setPrintPageDialog(true);

        // Buat objek untuk pengaturan printer dan halaman serta PrintDocument
        PdfPrinterSettings printerSettings = new PdfPrinterSettings();
        PrintPageSettings pageSettings = new PrintPageSettings();

        // Atur UkuranHalaman (jika diperlukan)
        pageSettings.setPaperSize(new PrintPaperSize("A4", 827, 1169));

        // Atur MarginHalaman (jika diperlukan)
        pageSettings.setMargins(new PrinterMargins(0, 0, 0, 0));

        java.awt.print.PrinterJob pj = java.awt.print.PrinterJob.getPrinterJob();

        if (pj.printDialog()) {
            printerSettings.setPrinterName(pj.getPrintService().getName());
            printerSettings.setCopies((short) pj.getCopies());
            // Cetak dokumen menggunakan pengaturan printer dan halaman
            viewer.printDocumentWithSettings(pageSettings, printerSettings);
        }
        // Tutup file PDF setelah mencetak
        viewer.close();
    }
```


## Cetak PDF ke Printer Lunak

Ada printer yang mencetak ke file. Kami mengatur nama printer virtual, dan, dengan analogi dengan contoh sebelumnya, kami membuat pengaturan.

```java
public static void PrintingPDFToSoftPrinter() {
        // Buat objek PdfViewer
        PdfViewer viewer = new PdfViewer();

        // Buka file PDF input
        viewer.bindPdf(_dataDir + "sample.pdf");

        // Atur atribut untuk pencetakan
        viewer.setAutoResize(true); // Cetak file dengan ukuran yang disesuaikan
        viewer.setAutoRotate(true); // Cetak file dengan rotasi yang disesuaikan
        viewer.setPrintPageDialog(false); // Jangan tampilkan dialog nomor halaman saat mencetak

        // Buat objek untuk pengaturan printer dan halaman serta PrintDocument
        PdfPrinterSettings printerSettings = new PdfPrinterSettings();
        PrintPageSettings pageSettings = new PrintPageSettings();

        // Atur printer Microsoft Soft Printer
        printerSettings.setPrinterName("Microsoft Print to PDF");
        // atau Adobe
        // printerSettings.setPrinterName("Adobe PDF");

        // Atur UkuranHalaman (jika diperlukan)
        pageSettings.setPaperSize(new PrintPaperSize("A4", 827, 1169));

        // Atur MarginHalaman (jika diperlukan)
        pageSettings.setMargins(new PrinterMargins(0, 0, 0, 0));

        // Cetak dokumen menggunakan pengaturan printer dan halaman
        viewer.printDocumentWithSettings(pageSettings, printerSettings);

        // Tutup file PDF setelah pencetakan
        viewer.close();
    }
```


## Menyembunyikan Dialog Cetak

Aspose.PDF untuk Java memungkinkan Anda untuk menyembunyikan dialog cetak. Untuk ini gunakan metode [getPrintPageDialog](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfViewer#getPrintPageDialog--).

Cuplikan kode berikut menunjukkan cara menyembunyikan dialog cetak.

```java
public static void PrintingPDFHidePrintDialog() {
        // Buat objek PdfViewer
        PdfViewer viewer = new PdfViewer();

        // Buka file PDF input
        viewer.bindPdf(_dataDir + "sample.pdf");

        // Atur atribut untuk pencetakan
        viewer.setAutoResize(true); // Cetak file dengan ukuran yang disesuaikan
        viewer.setAutoRotate(true); // Cetak file dengan rotasi yang disesuaikan

        viewer.setPrintPageDialog(false); // Jangan tampilkan dialog nomor halaman saat mencetak

        // Buat objek untuk pengaturan printer dan halaman serta PrintDocument
        PdfPrinterSettings printerSettings = new PdfPrinterSettings();
        PrintPageSettings pageSettings = new PrintPageSettings();

        // Atur printer Microsoft Soft Printer
        printerSettings.setPrinterName("Microsoft Print to PDF");

        // Atur Ukuran Halaman (jika diperlukan)
        pageSettings.setPaperSize(new PrintPaperSize("A4", 827, 1169));

        // Atur Margin Halaman (jika diperlukan)
        pageSettings.setMargins(new PrinterMargins(0, 0, 0, 0));

        // Cetak dokumen menggunakan pengaturan printer dan halaman
        viewer.printDocumentWithSettings(pageSettings, printerSettings);

        // Tutup file PDF setelah mencetak
        viewer.close();
    }
```


## Mencetak PDF Berwarna ke File XPS sebagai Grayscale

Dokumen PDF berwarna dapat dicetak ke printer XPS sebagai grayscale, menggunakan [PdfViewer](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfViewer). Untuk mencapainya, Anda perlu menggunakan properti PdfViewer.PrintAsGrayscale dan mengaturnya ke *true*.

Cuplikan kode berikut menunjukkan implementasi dari Properti PdfViewer.PrintAsGrayscale.

```java
 public static void PrintingPDFasGrayscale() {
        // Buat objek PdfViewer
        PdfViewer viewer = new PdfViewer();

        // Buka file PDF input
        viewer.bindPdf(_dataDir + "sample.pdf");

        // Atur atribut untuk pencetakan
        viewer.setAutoResize(true); // Cetak file dengan ukuran yang disesuaikan
        viewer.setAutoRotate(true); // Cetak file dengan rotasi yang disesuaikan

        viewer.setPrintAsGrayscale(true);

        // Buat objek untuk pengaturan printer dan halaman serta PrintDocument
        PdfPrinterSettings printerSettings = new PdfPrinterSettings();
        PrintPageSettings pageSettings = new PrintPageSettings();

        // Atur printer Microsoft Soft Printer
        printerSettings.setPrinterName("Microsoft Print to PDF");

        // Atur UkuranHalaman (jika diperlukan)
        pageSettings.setPaperSize(new PrintPaperSize("A4", 827, 1169));

        // Atur MarginHalaman (jika diperlukan)
        pageSettings.setMargins(new PrinterMargins(0, 0, 0, 0));

        // Cetak dokumen menggunakan pengaturan printer dan halaman
        viewer.printDocumentWithSettings(pageSettings, printerSettings);

        // Tutup file PDF setelah mencetak
        viewer.close();
    }
```


## Konversi PDF ke PostScript

Kelas [PdfViewer](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfViewer) menyediakan kemampuan untuk mencetak dokumen PDF dan dengan bantuan kelas ini, kita juga dapat mengonversi file PDF ke format PostScript. Untuk mengonversi file PDF menjadi PostScript, pertama-tama pasang printer PS dan cukup cetak ke file dengan bantuan PdfViewer.

Cuplikan kode berikut menunjukkan cara mencetak dan mengonversi PDF ke format PostScript.

```java
public static void PrintingPDFToPostScript() {
        // Buat objek PdfViewer
        PdfViewer viewer = new PdfViewer();

        // Buka file PDF input
        viewer.bindPdf(_dataDir + "sample.pdf");

        // Atur atribut untuk pencetakan
        viewer.setAutoResize(true); // Cetak file dengan ukuran yang disesuaikan
        viewer.setAutoRotate(true); // Cetak file dengan rotasi yang disesuaikan

        viewer.setPrintAsGrayscale(true);
        

        // Buat objek untuk pengaturan printer dan halaman dan PrintDocument
        PdfPrinterSettings printerSettings = new PdfPrinterSettings();
        PrintPageSettings pageSettings = new PrintPageSettings();

        // Atur Printer PostScript
        printerSettings.setPrinterName("HP Universal Printing PS (v7.0.0)");
        printerSettings.setPrintToFile(true);
        printerSettings.setPrintFileName(_dataDir+"result.ps");

        // Atur UkuranHalaman (jika diperlukan)
        pageSettings.setPaperSize(new PrintPaperSize("A4", 827, 1169));

        // Atur MarginHalaman (jika diperlukan)
        pageSettings.setMargins(new PrinterMargins(0, 0, 0, 0));

        // Cetak dokumen menggunakan pengaturan printer dan halaman
        viewer.printDocumentWithSettings(pageSettings, printerSettings);

        // Tutup file PDF setelah mencetak
        viewer.close();
    }
```


## Memeriksa Status Pekerjaan Cetak

File PDF dapat dicetak ke printer fisik maupun ke Microsoft XPS Document Writer, tanpa menampilkan dialog cetak, menggunakan kelas [PdfViewer](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfViewer). Saat mencetak file PDF berukuran besar, prosesnya mungkin memakan waktu lama sehingga pengguna mungkin tidak yakin apakah proses pencetakan selesai atau mengalami masalah. Untuk menentukan status pekerjaan cetak, gunakan properti PrintStatus. Cuplikan kode berikut menunjukkan cara mencetak file PDF ke file XPS dan mendapatkan status pencetakan.

```java
public static void CheckingPrintJobStatus() {
        // Membuat objek PdfViewer
        PdfViewer viewer = new PdfViewer();

        // Membuka file PDF input
        viewer.bindPdf(_dataDir + "sample.pdf");

        // Mengatur atribut untuk pencetakan
        viewer.setAutoResize(true); // Cetak file dengan ukuran yang disesuaikan
        viewer.setAutoRotate(true); // Cetak file dengan rotasi yang disesuaikan

        viewer.setPrintAsGrayscale(true);

        // Membuat objek untuk pengaturan printer dan halaman serta PrintDocument
        PdfPrinterSettings printerSettings = new PdfPrinterSettings();
        PrintPageSettings pageSettings = new PrintPageSettings();

        // Mengatur printer Microsoft Soft Printer
        printerSettings.setPrinterName("HP Universal Printing PS (v7.0.0)");

        // Mengatur PageSize (jika diperlukan)
        pageSettings.setPaperSize(new PrintPaperSize("A4", 827, 1169));

        // Mengatur PageMargins (jika diperlukan)
        pageSettings.setMargins(new PrinterMargins(0, 0, 0, 0));

        // Mencetak dokumen menggunakan pengaturan printer dan halaman
        viewer.printDocumentWithSettings(pageSettings, printerSettings);

        // // Memeriksa status cetak
        if (viewer.getPrintStatus() != null) {
            Exception ex = (Exception) viewer.getPrintStatus();
            System.out.println(ex.getMessage());
        } else {
            // Tidak ada kesalahan yang ditemukan. Pekerjaan cetak telah berhasil diselesaikan
            System.out.println("Semuanya berjalan dengan baik!");
        }
        // Menutup file PDF setelah pencetakan
        viewer.close();
    }
```