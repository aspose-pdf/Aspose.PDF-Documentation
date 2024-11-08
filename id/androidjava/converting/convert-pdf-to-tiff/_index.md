---
title: Convert PDF to TIFF 
linktitle: Convert PDF to TIFF  
type: docs
weight: 30
url: /id/androidjava/convert-pdf-to-tiff/
lastmod: "2021-06-05"
description: Artikel ini menjelaskan cara mengubah halaman dalam dokumen PDF menjadi gambar TIFF. Anda akan belajar bagaimana mengonversi semua atau halaman tunggal menjadi gambar TIFF dengan Aspose.PDF untuk Android melalui Android via Java.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

**Aspose.PDF untuk Android via Java** memungkinkan untuk mengonversi Halaman PDF menjadi gambar TIFF.

Kelas [TiffDevice](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/tiffdevice) memungkinkan Anda untuk mengonversi halaman PDF menjadi gambar TIFF. Kelas ini menyediakan metode bernama Process yang memungkinkan Anda mengonversi semua halaman dalam file PDF menjadi satu gambar TIFF.

{{% alert color="primary" %}}

Coba online. Anda dapat memeriksa kualitas konversi Aspose.PDF dan melihat hasilnya secara online di tautan ini [products.aspose.app/pdf/conversion/pdf-to-tiff](https://products.aspose.app/pdf/conversion/pdf-to-tiff)

{{% /alert %}}

## Mengonversi Halaman PDF ke Satu Gambar TIFF

Aspose.PDF untuk Android melalui Java menjelaskan cara mengonversi semua halaman dalam file PDF ke satu gambar TIFF:

1. Buat objek dari kelas Document.
1. Panggil metode Process untuk mengonversi dokumen.
1. Untuk mengatur properti file keluaran, gunakan kelas TiffSettings.

Cuplikan kode berikut menunjukkan cara mengonversi semua halaman PDF ke satu gambar TIFF.

```java
public void convertPDFtoTiffSinglePage() {
        // Buka dokumen
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Buat objek Resolution
        Resolution resolution = new Resolution(300);

        // Buat objek TiffSettings
        TiffSettings tiffSettings = new TiffSettings();
        tiffSettings.setCompression(CompressionType.None);
        tiffSettings.setDepth(ColorDepth.Default);
        tiffSettings.setShape(ShapeType.Landscape);

        // Buat perangkat TIFF
        TiffDevice tiffDevice = new TiffDevice(resolution, tiffSettings);
        File file = new File(fileStorage, "PDF-to-TIFF.tiff");
        try {
            // Konversi halaman tertentu dan simpan gambar ke stream
            tiffDevice.process(document, 1, 1, file.toString());
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
        }
    }

```


## Ubah Halaman Tunggal ke Gambar TIFF

Aspose.PDF untuk Android melalui Java memungkinkan untuk mengubah halaman tertentu dalam file PDF ke gambar TIFF, gunakan versi kelebihan dari metode Process(..) yang mengambil nomor halaman sebagai argumen untuk konversi. Cuplikan kode berikut menunjukkan cara mengubah halaman pertama PDF ke dalam format TIFF.

```java
public void convertPDFtoTiffAllPages() {
        // Buka dokumen
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }


        // Buat objek Resolution
        Resolution resolution = new Resolution(300);

        // Buat objek TiffSettings
        TiffSettings tiffSettings = new TiffSettings();
        tiffSettings.setCompression(CompressionType.None);
        tiffSettings.setDepth(ColorDepth.Default);
        tiffSettings.setShape(ShapeType.Landscape);
        tiffSettings.setSkipBlankPages(false);

        // Buat perangkat TIFF
        TiffDevice tiffDevice = new TiffDevice(resolution, tiffSettings);
        File file = new File(fileStorage, "AllPagesToTIFF_out.tif");
        try {
            // Konversi halaman tertentu dan simpan gambar ke stream
            tiffDevice.process(document, file.toString());
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
        }
    }
```


## Gunakan algoritma Bradley selama konversi

Aspose.PDF untuk Android melalui Java telah mendukung fitur untuk mengonversi PDF ke TIFF menggunakan kompresi LZW dan kemudian dengan penggunaan AForge, Binarisasi dapat diterapkan. Namun salah satu pelanggan meminta bahwa untuk beberapa gambar, mereka perlu mendapatkan Threshold menggunakan Otsu, jadi mereka juga ingin menggunakan Bradley.

```java
public void convertPDFtoTiffBradleyBinarization() {
        //Belum diimplementasikan di Aspose.PDF untuk Android
        throw new NotImplementedException();
    }

    public static void convertPDFtoTIFF_Pixelated() {

        //Belum diimplementasikan di Aspose.PDF untuk Android
        throw new NotImplementedException();
    }
```