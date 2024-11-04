---
title: Ekstraksi Halaman PDF
type: docs
weight: 20
url: /java/extract-pdf-pages/
description: Bagian ini menjelaskan cara mengekstraksi halaman PDF dengan com.aspose.pdf.facades menggunakan kelas PdfFileEditor.
lastmod: "2021-06-05"
draft: false
---

## Ekstraksi Halaman PDF Antara Dua Nomor Menggunakan Jalur File

Metode [Extract](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileEditor#extract-java.io.InputStream-int:A-java.io.OutputStream-) dari kelas [PdfFileEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileEditor) memungkinkan Anda untuk mengekstraksi rentang halaman tertentu dari file PDF. Overload ini memungkinkan Anda untuk mengekstraksi halaman saat memanipulasi file PDF dari disk. Overload ini membutuhkan parameter berikut: jalur file input, halaman awal, halaman akhir, dan jalur file output. Halaman dari halaman awal hingga halaman akhir akan diekstraksi dan hasilnya akan disimpan di disk. Cuplikan kode berikut menunjukkan cara mengekstraksi halaman PDF antara dua nomor menggunakan jalur file.

```java
  public static void Extract_PDFPages_FilePaths() {
        // Buat objek PdfFileEditor
        PdfFileEditor pdfEditor = new PdfFileEditor();

        // Ekstraksi halaman
        pdfEditor.Extract(_dataDir + "MultiplePages.pdf", 1, 3, _dataDir + "ExtractPagesBetweenNumbers_out.pdf");
    }
```


## Ekstrak Array Halaman PDF Menggunakan Jalur File

Jika Anda tidak ingin mengekstrak rentang halaman, melainkan sekumpulan halaman tertentu, metode [Extract](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileEditor#extract-java.io.InputStream-int:A-java.io.OutputStream-) memungkinkan Anda untuk melakukannya juga. Anda pertama-tama perlu membuat array integer dengan semua nomor halaman yang perlu diekstraksi. Metode [Extract](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileEditor#extract-java.io.InputStream-int:A-java.io.OutputStream-) ini mengambil parameter berikut: file PDF input, array integer halaman yang akan diekstraksi, dan file PDF output. Cuplikan kode berikut menunjukkan kepada Anda bagaimana mengekstrak halaman PDF menggunakan jalur file.

```java
 public static void Extract_ArrayPDFPages_FilePaths() {
        // Buat objek PdfFileEditor
        PdfFileEditor pdfEditor = new PdfFileEditor();
        int[] pagesToExtract = new int[] { 1, 2 };
        // Ekstrak halaman
        pdfEditor.Extract(_dataDir + "Extract.pdf", pagesToExtract, _dataDir + "ExtractArrayOfPages_out.pdf");
    }
```


## Ekstrak Halaman PDF antara Dua Angka Menggunakan Streams

[Extract](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileEditor#extract-java.io.InputStream-int:A-java.io.OutputStream-) metode dari kelas [PdfFileEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileEditor) memungkinkan Anda untuk mengekstrak rentang halaman menggunakan streams. Anda perlu memberikan parameter berikut ke overload ini: aliran input, halaman awal, halaman akhir, dan aliran output. Halaman yang ditentukan oleh rentang antara halaman awal dan halaman akhir akan diekstrak dari aliran input dan disimpan ke aliran output. Cuplikan kode berikut menunjukkan kepada Anda cara mengekstrak halaman PDF antara dua angka menggunakan streams.

```java
public static void Extract_PDFPages_Streams()
    {
         // Buat objek PdfFileEditor
            PdfFileEditor pdfEditor = new PdfFileEditor();
         // Buat streams
         using (FileStream inputStream = new FileStream(_dataDir + "MultiplePages.pdf", FileMode.Open))
         using (FileStream outputStream = new FileStream(_dataDir + "ExtractPagesBetweenTwoNumbers_out.pdf", FileMode.Create))
         // Ekstrak halaman
         pdfEditor.Extract(inputStream, 1, 3, outputStream);

    }
```


## Ekstrak Array Halaman PDF Menggunakan Stream

Sebuah array halaman dapat diekstrak dari stream PDF dan disimpan dalam output stream menggunakan overload yang sesuai dari metode [Extract](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileEditor#extract-java.io.InputStream-int:A-java.io.OutputStream-). Jika Anda tidak ingin mengekstrak rentang halaman, melainkan satu set halaman tertentu, metode [Extract](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileEditor#extract-java.io.InputStream-int:A-java.io.OutputStream-) memungkinkan Anda untuk melakukannya juga. Anda pertama-tama perlu membuat array integer dengan semua nomor halaman yang perlu diekstrak. Overload dari metode [Extract](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileEditor#extract-java.io.InputStream-int:A-java.io.OutputStream-) ini mengambil parameter berikut: input stream, array integer dari halaman yang akan diekstrak dan output stream. Cuplikan kode berikut menunjukkan kepada Anda bagaimana mengekstrak halaman PDF menggunakan stream.

```java
public static void Extract_ArrayPDFPages_Streams()
        {
            // Buat objek PdfFileEditor
            PdfFileEditor pdfEditor = new PdfFileEditor();
            // Buat stream
            using (FileStream inputStream = new FileStream(_dataDir + "MultiplePages.pdf", FileMode.Open))
            using (FileStream outputStream = new FileStream(_dataDir + "ExtractArrayOfPagesUsingStreams_out.pdf", FileMode.Create))
            {
                int[] pagesToExtract = new int[] { 1, 2 };
                // Ekstrak halaman
                pdfEditor.Extract(inputStream, pagesToExtract, outputStream);
            }
        }
```