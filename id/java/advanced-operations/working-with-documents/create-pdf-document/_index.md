---
title: Buat File PDF di Java
linktitle: Buat Dokumen PDF
type: docs
weight: 10
url: /id/java/create-pdf-document/
description: Pelajari cara membuat file PDF dan membuat PDF yang dapat dicari di Java menggunakan Aspose.PDF.
lastmod: "2026-11-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Buat file PDF dan dokumen PDF yang dapat dicari dengan Java
Abstract: Artikel ini menunjukkan cara membuat dokumen PDF menggunakan Aspose.PDF for Java. Artikel ini mencakup pembuatan PDF baru dari awal dan mengonversi dokumen berbasis gambar menjadi PDF yang dapat dicari dengan menyediakan output HOCR dari mesin OCR eksternal.
---
Aspose.PDF for Java mendukung baik pembuatan dokumen sederhana maupun alur kerja PDF yang dapat dicari dengan bantuan OCR.

## Buat dokumen PDF baru

Gunakan pendekatan ini ketika Anda perlu membuat file PDF sederhana dari awal.

1. Buat PDF baru [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Tambahkan [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) ke dokumen.
1. Buat sebuah [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/) dan tambahkan ke halaman.
1. Simpan PDF output [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void createNewDocument(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        page.getParagraphs().add(new TextFragment("Hello World!"));
        document.save(outputFile.toString());
    }
}
```

## Buat PDF yang dapat dicari

PDF yang dipindai berisi gambar teks. Gunakan mesin OCR eksternal untuk mengenali teks dan membuatnya dapat dicari serta dapat dipilih. Contoh berikut menggunakan Tesseract untuk mengembalikan markup HOCR ke Aspose.PDF atau untuk menghasilkan halaman PDF yang dapat dicari yang kemudian digabungkan.

Pasang Tesseract 4 atau yang lebih baru dengan data bahasa LSTM bahasa Inggris sebelum menjalankan contoh-contoh ini. Atur `TESSERACT_PATH` pada metode pembantu bersama di bawah ke jalur file yang dapat dieksekusi, atau gunakan `"tesseract"` jika tersedia di `PATH`. Kedua contoh menggunakan metode pembantu yang sama dan memerlukan Java 11 atau yang lebih baru. Tempatkan metode dan konstanta di kelas yang sama serta sertakan impor ini:

### Buat PDF yang dapat dicari menggunakan callback HOCR

Gunakan [Document.CallBackGetHocr](https://reference.aspose.com/pdf/java/com.aspose.pdf/document.callbackgethocr/) untuk menyediakan teks yang dikenali dan koordinatnya ke Aspose.PDF. Tesseract menghasilkan markup HOCR, dan Aspose.PDF menggunakannya untuk menambahkan lapisan teks yang dapat dicari ke dokumen berbasis gambar.

1. Siapkan direktori sementara untuk gambar, output HOCR, dan log OCR.
1. Implementasikan [Document.CallBackGetHocr](https://reference.aspose.com/pdf/java/com.aspose.pdf/document.callbackgethocr/) dan simpan setiap gambar yang diberikan sebagai file JPEG.
1. Panggil metode pembantu bersama `runTesseract` dengan format keluaran `hocr`.
1. Baca file `.hocr` yang dihasilkan, hapus file sementara, dan kembalikan markup dari callback.
1. Buka dokumen sumber [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) dan berikan callback ke `convert`.
1. Periksa hasil konversi dan simpan PDF yang dapat dicari menggunakan `save`.

```java
import com.aspose.pdf.Document;
import com.aspose.pdf.Page;
import com.aspose.pdf.devices.PngDevice;
import com.aspose.pdf.devices.Resolution;

import javax.imageio.ImageIO;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.Scanner;
import java.util.concurrent.TimeUnit;

public static void createSearchablePdf_1(Path inputFile, Path outputFile) {
    Path tempDir = outputFile.toAbsolutePath().getParent().resolve("ocr-temp");

    // Create callBack - logic recognize text for PDF images. Use outer OCR supports
    // HOCR standard(http://en.wikipedia.org/wiki/HOCR).
    // We have used free google tesseract
    // OCR(http://en.wikipedia.org/wiki/Tesseract_%28software%29)

    Document.CallBackGetHocr callBackGetHocr = new Document.CallBackGetHocr() {
        @Override
        public String invoke(java.awt.image.BufferedImage img) {
            File outputfile = tempDir.resolve("test.jpg").toFile();
            try {
                Files.createDirectories(tempDir);
                ImageIO.write(img, "jpg", outputfile);
            } catch (IOException e1) {
                throw new java.io.UncheckedIOException("Failed to write OCR image.", e1);
            }

            try {
                Path outputBase = tempDir.resolve("out");
                runTesseract(outputfile.toPath(), outputBase, "hocr", tempDir.resolve("tesseract.log"));
            } catch (IOException e) {
                throw new java.io.UncheckedIOException("Tesseract OCR failed.", e);
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
                throw new IllegalStateException("Tesseract OCR was interrupted.", e);
            }

            // Read the HOCR output as a string.
            File file = tempDir.resolve("out.hocr").toFile();
            StringBuilder fileContents = new StringBuilder((int) file.length());
            Scanner scanner = null;
            try {
                scanner = new Scanner(file);
                String lineSeparator = System.getProperty("line.separator");

                while (scanner.hasNextLine()) {
                    fileContents.append(scanner.nextLine() + lineSeparator);
                }
            } catch (FileNotFoundException e) {
                throw new java.io.UncheckedIOException("Tesseract OCR failed.", e);
            } finally {
                if (scanner != null)
                    scanner.close();
            }

            // deleting temp files
            File fileOut = tempDir.resolve("out.hocr").toFile();
            if (fileOut.exists()) {
                fileOut.delete();
            }
            File fileLog = tempDir.resolve("tesseract.log").toFile();
            if (fileLog.exists()) {
                fileLog.delete();
            }
            File fileTest = tempDir.resolve("test.jpg").toFile();
            if (fileTest.exists()) {
                fileTest.delete();
            }

            return fileContents.toString();
        }
    };
    // End callBack
    try (Document document = new Document(inputFile.toString())) {
        if (!document.convert(callBackGetHocr))
            throw new RuntimeException("Failed to convert document.");
        document.save(outputFile.toString());
    }
}
```

Contoh ini menggunakan nama file tetap di dalam `ocr-temp`. Gunakan direktori sementara terpisah untuk setiap konversi jika Anda menyesuaikannya untuk pemrosesan bersamaan.

### Buat PDF yang dapat dicari dengan mengenali halaman yang dirender

Render setiap halaman menjadi gambar PNG, biarkan Tesseract membuat PDF yang dapat dicari untuk gambar itu, dan gabungkan PDF yang dihasilkan menjadi satu dokumen. Output didasarkan pada gambar halaman yang dirender dengan teks yang dikenali, sehingga elemen interaktif yang ada tidak dibawa.

1. Buat direktori sementara unik untuk gambar yang di-render, PDF yang dihasilkan, dan log OCR.
1. Buka dokumen sumber [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) dan buat dokumen keluaran kosong.
1. Buat sebuah [PngDevice](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/pngdevice/) dengan sebuah [Resolution](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/resolution/) dengan 600 DPI.
1. Iterasikan objek [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) pada dokumen sumber dan render setiap halaman menggunakan `process`.
1. Panggil metode pembantu bersama `runTesseract` dengan format keluaran `pdf` dan tambahkan PDF yang dihasilkan menggunakan [Document.merge](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Simpan PDF yang dapat dicari yang digabungkan dan hapus file sementara di blok `finally`.

```java
public static void createSearchablePdf_2(Path inputFile, Path outputFile)
        throws IOException, InterruptedException {
    Path outputDirectory = outputFile.toAbsolutePath().getParent();
    Files.createDirectories(outputDirectory);
    Path tempDir = Files.createTempDirectory(outputDirectory, "ocr-");
    Path tempImage = tempDir.resolve("page.png");
    Path tempDoc = tempDir.resolve("page");
    Path tempPdf = tempDir.resolve("page.pdf");
    Path tempLog = tempDir.resolve("page.log");
    Throwable failure = null;
    try (Document inputDocument = new Document(inputFile.toString());
         Document outputDocument = new Document()) {
        PngDevice pngDevice = new PngDevice(new Resolution(600));
        for (Page page : inputDocument.getPages()) {
            pngDevice.process(page, tempImage.toString());
            runTesseract(tempImage, tempDoc, "pdf", tempLog);
            outputDocument.merge(tempPdf.toString());
            Files.deleteIfExists(tempPdf);
        }
        outputDocument.save(outputFile.toString());
    } catch (InterruptedException e) {
        failure = e;
        Thread.currentThread().interrupt();
        throw e;
    } catch (IOException | RuntimeException | Error e) {
        failure = e;
        throw e;
    } finally {
        IOException cleanupFailure = null;
        for (Path path : new Path[]{tempImage, tempPdf, tempLog, tempDir}) {
            try {
                Files.deleteIfExists(path);
            } catch (IOException e) {
                if (cleanupFailure == null) {
                    cleanupFailure = e;
                } else {
                    cleanupFailure.addSuppressed(e);
                }
            }
        }
        if (cleanupFailure != null) {
            if (failure != null) {
                failure.addSuppressed(cleanupFailure);
            } else {
                throw cleanupFailure;
            }
        }
    }
}
```

### Jalankan Tesseract dari contoh

Tambahkan konstanta ini dan metode pembantu bersama ke kelas yang sama dengan contoh-contohnya. Metode pembantu menggunakan bahasa Inggris (`eng`), mesin LSTM (`--oem 1`), dan segmentasi halaman otomatis (`--psm 3`). Metode ini menulis keluaran diagnostik ke log, menunggu hingga dua menit, dan memverifikasi bahwa file hasil yang tidak kosong telah dibuat. Proses dihentikan jika masih berjalan saat metode pembantu berakhir.

```java
// Change this to match your installation, or use "tesseract" for PATH lookup.
private static final String TESSERACT_PATH = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe";
private static final long TESSERACT_TIMEOUT_MINUTES = 2;

private static void runTesseract(Path image, Path outputBase, String format, Path log)
        throws IOException, InterruptedException {
    Path result = Path.of(outputBase + "." + format);
    Files.deleteIfExists(result);
    ProcessBuilder builder = new ProcessBuilder(
            TESSERACT_PATH, image.toString(), outputBase.toString(),
            "-l", "eng", "--oem", "1", "--psm", "3", format);
    builder.redirectErrorStream(true);
    builder.redirectOutput(log.toFile());
    Process process = builder.start();
    try {
        process.getOutputStream().close();
        if (!process.waitFor(TESSERACT_TIMEOUT_MINUTES, TimeUnit.MINUTES)) {
            throw new IOException("Tesseract timed out after "
                    + TESSERACT_TIMEOUT_MINUTES + " minutes while processing " + image);
        }
        if (process.exitValue() != 0 || !Files.isRegularFile(result)
                || Files.size(result) == 0) {
            throw new IOException("Tesseract failed (exit " + process.exitValue()
                    + ") while processing " + image + ": " + Files.readString(log));
        }
    } finally {
        if (process.isAlive()) {
            process.destroyForcibly();
            process.onExit().join();
        }
    }
}
```
