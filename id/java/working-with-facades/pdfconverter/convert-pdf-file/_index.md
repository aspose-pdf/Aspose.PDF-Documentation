---
title: Mengonversi File PDF
type: docs
weight: 20
url: /id/java/convert-pdf-file/
description: Bagian ini menjelaskan cara mengonversi File PDF dengan Aspose.PDF Facades menggunakan kelas PdfConverter.
lastmod: "2021-06-05"
draft: false
---

## Mengonversi Halaman PDF ke Format Gambar yang Berbeda (Facades)

Untuk mengonversi halaman PDF ke format gambar yang berbeda, Anda perlu membuat objek [PdfConverter](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfConverter) dan membuka file PDF menggunakan metode [bindPdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfConverter#bindPdf-java.lang.String-).

Setelah itu, Anda perlu memanggil metode [doConvert](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfConverter#doConvert--) untuk tugas inisialisasi.
 Kemudian, Anda dapat melakukan loop melalui semua halaman menggunakan metode [hasNextImage](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfConverter#hasNextImage--) dan [getNextImage](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfConverter#getNextImage-java.io.OutputStream-). Metode getNextImage memungkinkan Anda untuk membuat gambar dari halaman tertentu. Anda juga perlu memberikan ImageType ke metode ini untuk membuat gambar dari jenis tertentu yaitu JPEG, GIF, atau PNG, dll.

Terakhir, panggil metode close dari kelas [PdfConverter](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfConverter).

Cuplikan kode berikut menunjukkan kepada Anda cara mengonversi halaman PDF menjadi gambar.

```java
public static void ConvertPdfPagesToImages01() {
        // Buat objek PdfConverter
        PdfConverter converter = new PdfConverter();

        // Mengikat file pdf input
        converter.bindPdf(_dataDir + "Sample-Document-01.pdf");

        // Inisialisasi proses konversi
        converter.doConvert();
        
        int count=0;

        // Periksa jika halaman ada, lalu konversikan ke gambar satu per satu
        while (converter.hasNextImage())
            converter.getNextImage(_dataDir + "page" + count + "_out.jpg", ImageType.getJpeg());
        // Tutup objek PdfConverter
        converter.close();
    }
```

Pada cuplikan kode berikut, kami akan menunjukkan bagaimana Anda dapat mengubah beberapa parameter. Dengan [setCoordinateType](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfConverter#setCoordinateType-int-) kami mengatur bingkai [CropBox](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageCoordinateType#CropBox). Selain itu, kita dapat mengubah [setResolution](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfConverter#setResolution-com.aspose.pdf.devices.Resolution-) dengan menentukan jumlah titik per inci. Yang berikutnya [setFormPresentationMode](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfConverter#setFormPresentationMode-int-) - mode presentasi formulir. Kemudian kami menunjukkan [setStartPage](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfConverter#setStartPage-int-) dengan nomor halaman yang ditetapkan untuk memulai konversi. Kita juga dapat menentukan halaman terakhir dengan mengatur rentang.

```java
public static void ConvertPdfPagesToImages02()
    {
        // Buat objek PdfConverter
        PdfConverter converter = new PdfConverter();

        // Mengikat file pdf input
        converter.bindPdf(_dataDir + "sample.pdf");

        // Inisialisasi proses konversi
        converter.doConvert();
        converter.setCoordinateType(PageCoordinateType.CropBox);
        converter.setResolution (new Resolution(600));
        converter.setFormPresentationMode(FormPresentationMode.Editor);
        converter.setStartPage(2);
        int count=0;
        // Periksa apakah halaman ada dan kemudian konversi ke gambar satu per satu
        while (converter.hasNextImage())
            converter.getNextImage(_dataDir + "page" + count + "_out.jpg", ImageType.getJpeg());
        // Tutup objek PdfConverter
        converter.close();
    }
```