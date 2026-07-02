---
title: Konversi PDF ke TIFF
linktitle: Konversi PDF ke TIFF
type: docs
weight: 30
url: /id/androidjava/convert-pdf-to-tiff/
lastmod: "2026-07-01"
description: Artikel ini menjelaskan cara mengonversi halaman dalam dokumen PDF menjadi gambar TIFF. Anda akan belajar cara mengonversi semua atau halaman tunggal menjadi gambar TIFF dengan Aspose.PDF for Android via Android via Java.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

**Aspose.PDF for Android via Java** memungkinkan untuk mengonversi Halaman PDF menjadi gambar TIFF.

The [kelas TiffDevice](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/tiffdevice) memungkinkan Anda mengonversi halaman PDF menjadi gambar TIFF. Kelas ini menyediakan metode bernama Process yang memungkinkan Anda mengonversi semua halaman dalam file PDF menjadi satu gambar TIFF.

{{% alert color="primary" %}}

Coba secara daring. Anda dapat memeriksa kualitas konversi Aspose.PDF dan melihat hasilnya secara daring di tautan ini [products.aspose.app/pdf/conversion/pdf-to-tiff](https://products.aspose.app/pdf/conversion/pdf-to-tiff)

{{% /alert %}}

## Konversi Halaman PDF menjadi Satu Gambar TIFF

Aspose.PDF untuk Android via Java menjelaskan cara mengonversi semua halaman dalam file PDF menjadi satu gambar TIFF:

1. Buat sebuah objek dari kelas Document.
1. Panggil metode Process untuk mengonversi dokumen.
1. Untuk mengatur properti file output, gunakan kelas TiffSettings.

Potongan kode berikut menunjukkan cara mengonversi semua halaman PDF menjadi satu gambar TIFF.

```java
public void convertPDFtoTiffSinglePage() {
        // Open document
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Create Resolution object
        Resolution resolution = new Resolution(300);

        // Create TiffSettings object
        TiffSettings tiffSettings = new TiffSettings();
        tiffSettings.setCompression(CompressionType.None);
        tiffSettings.setDepth(ColorDepth.Default);
        tiffSettings.setShape(ShapeType.Landscape);

        // Create TIFF device
        TiffDevice tiffDevice = new TiffDevice(resolution, tiffSettings);
        File file = new File(fileStorage, "PDF-to-TIFF.tiff");
        try {
            // Convert a particular page and save the image to stream
            tiffDevice.process(document, 1, 1, file.toString());
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
        }
    }

```

## Konversi Halaman Tunggal ke Gambar TIFF

Aspose.PDF for Android via Java memungkinkan mengonversi halaman tertentu dalam file PDF ke gambar TIFF, gunakan versi overload dari metode Process(..) yang menerima nomor halaman sebagai argumen untuk konversi. Cuplikan kode berikut menunjukkan cara mengonversi halaman pertama dari PDF ke format TIFF.

```java
public void convertPDFtoTiffAllPages() {
        // Open document
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }


        // Create Resolution object
        Resolution resolution = new Resolution(300);

        // Create TiffSettings object
        TiffSettings tiffSettings = new TiffSettings();
        tiffSettings.setCompression(CompressionType.None);
        tiffSettings.setDepth(ColorDepth.Default);
        tiffSettings.setShape(ShapeType.Landscape);
        tiffSettings.setSkipBlankPages(false);

        // Create TIFF device
        TiffDevice tiffDevice = new TiffDevice(resolution, tiffSettings);
        File file = new File(fileStorage, "AllPagesToTIFF_out.tif");
        try {
            // Convert a particular page and save the image to stream
            tiffDevice.process(document, file.toString());
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
        }
    }
```

## Gunakan algoritma Bradley selama konversi

Aspose.PDF for Android via Java telah mendukung fitur untuk mengonversi PDF ke TIFF menggunakan kompresi LZW dan kemudian dengan penggunaan AForge, Binarisasi dapat diterapkan. Namun seorang pelanggan meminta bahwa untuk beberapa gambar, mereka perlu memperoleh Threshold menggunakan Otsu, sehingga mereka juga ingin menggunakan Bradley.

```java
public void convertPDFtoTiffBradleyBinarization() {
        //Not implemented in Aspose.PDF for Android
        throw new NotImplementedException();
    }

    public static void convertPDFtoTIFF_Pixelated() {

        //Not implemented in Aspose.PDF for Android
        throw new NotImplementedException();
    }
```

