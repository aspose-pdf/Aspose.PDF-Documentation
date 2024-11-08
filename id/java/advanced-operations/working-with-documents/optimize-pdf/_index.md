---
title: Optimize, Compress or Reduce PDF Size in Java
linktitle: Optimize PDF Document
type: docs
weight: 40
url: /id/java/optimize-pdf/
description: Optimalkan file PDF, perkecil semua gambar, kurangi ukuran PDF, Hapus font yang tidak terbenam, Hapus objek yang tidak digunakan dengan Java.
lastmod: "2021-06-05"
---

Sebuah dokumen PDF terkadang dapat mengandung data tambahan. Mengurangi ukuran file PDF akan membantu Anda mengoptimalkan transfer jaringan dan penyimpanan. Ini sangat berguna untuk publikasi di halaman web, berbagi di jejaring sosial, mengirim melalui e-mail, atau mengarsipkan dalam penyimpanan. Kita dapat menggunakan beberapa teknik untuk mengoptimalkan PDF:

- Optimalkan konten halaman untuk penjelajahan online
- Perkecil atau kompres semua gambar
- Aktifkan penggunaan kembali konten halaman
- Gabungkan aliran duplikat
- Hapus font yang tidak terbenam
- Hapus objek yang tidak digunakan
- Hapus bidang formulir yang diratakan
- Hapus atau ratakan anotasi

## Optimalkan Dokumen PDF untuk Web

Optimasi atau linearisasi mengacu pada proses membuat file PDF cocok untuk penjelajahan online menggunakan peramban web.
 Aspose.PDF mendukung proses ini.

Untuk mengoptimalkan PDF untuk tampilan web:

1. Buka dokumen input dalam objek [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).
1. Gunakan metode [optimize()](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#optimize--).
1. Simpan dokumen yang telah dioptimalkan menggunakan metode save(..).

Cuplikan kode berikut menunjukkan cara mengoptimalkan dokumen PDF untuk web.

```java
package com.aspose.pdf.examples;

import java.io.FileNotFoundException;
import java.time.Clock;
import java.time.Duration;

import com.aspose.pdf.*;
import com.aspose.pdf.optimization.ImageCompressionVersion;
import com.aspose.pdf.optimization.ImageEncoding;

public class ExampleOptimize {

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void OptimizePDFDocumentForTheWeb() {

        // Buka dokumen
        Document pdfDocument = new Document(_dataDir + "sample.pdf");

        // Optimalkan untuk web
        pdfDocument.optimize();

        // Simpan dokumen keluaran
        pdfDocument.save(_dataDir + "OptimizeDocument_out.pdf");
    }
```

## Mengurangi Ukuran File PDF

Topik ini menjelaskan langkah-langkah untuk mengoptimalkan/mengurangi ukuran file PDF. Aspose.PDF API menyediakan kelas [OptimizationOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf.optimization/class-use/OptimizationOptions) yang memberikan fleksibilitas untuk mengoptimalkan PDF keluaran dengan menghapus objek yang tidak diperlukan dan mengompresi file PDF yang memiliki gambar. Kedua opsi ini dijelaskan dalam bagian berikut.

### Menghapus Objek yang Tidak Diperlukan
Kita dapat mengoptimalkan ukuran dokumen PDF dengan menghapus objek yang duplikat dan tidak digunakan. Potongan kode berikut menunjukkan caranya.

```java
public static void ReduceSizePDF() {

        // Buka dokumen
        Document pdfDocument = new Document(_dataDir + "sample.pdf");

        // Optimalkan dokumen PDF. Namun, perlu dicatat bahwa metode ini tidak dapat menjamin
        // penyusutan dokumen
        pdfDocument.optimizeResources();

        // Simpan dokumen keluaran
        pdfDocument.save(_dataDir + "OptimizeDocument_out.pdf");
    }
```

## Mengecilkan atau Mengompresi Semua Gambar

Jika file PDF sumber berisi gambar, pertimbangkan untuk mengompres gambar dan mengatur kualitasnya. Untuk mengaktifkan kompresi gambar, berikan nilai true sebagai argumen ke metode setCompressImages(..). Semua gambar dalam dokumen akan dikompresi ulang. Kompresi ditentukan oleh metode setImageQuality(..), yang merupakan nilai kualitas dalam persen. 100% adalah kualitas dan ukuran gambar yang tidak berubah. Untuk mengurangi ukuran gambar, berikan argumen kurang dari 100 ke metode setImageQuality(..).

```java
public static void ShrinkingCompressing() {
        // Buka dokumen
        Document pdfDocument = new Document(_dataDir + "Shrinkimage.pdf");

        // Inisialisasi OptimizationOptions
        com.aspose.pdf.optimization.OptimizationOptions optimizationOptions = new com.aspose.pdf.optimization.OptimizationOptions();

        // Atur opsi CompressImages
        optimizationOptions.getImageCompressionOptions().setCompressImages(true);

        // Atur opsi ImageQuality
        optimizationOptions.getImageCompressionOptions().setImageQuality(50);

        // Optimalkan dokumen PDF menggunakan OptimizationOptions
        pdfDocument.optimizeResources(optimizationOptions);
        _dataDir = _dataDir + "Shrinkimage_out.pdf";
        // Simpan dokumen yang diperbarui
        pdfDocument.save(_dataDir);
    }
```

Cara lain adalah dengan mengubah ukuran gambar dengan resolusi lebih rendah. Dalam hal ini, kita harus mengatur ResizeImages ke true dan MaxResolution ke nilai yang sesuai.

```java
public static void ShrinkingCompressing2() {
        // Buka dokumen
        Document pdfDocument = new Document(_dataDir + "ResizeImage.pdf");

        // Inisialisasi OptimizationOptions
        com.aspose.pdf.optimization.OptimizationOptions optimizationOptions = new com.aspose.pdf.optimization.OptimizationOptions();

        // Atur opsi CompressImages
        optimizationOptions.getImageCompressionOptions().setCompressImages(true);
        // Atur opsi ImageQuality
        optimizationOptions.getImageCompressionOptions().setImageQuality(75);

        // Atur opsi ResizeImage
        optimizationOptions.getImageCompressionOptions().setResizeImages(true);

        // Atur opsi MaxResolution
        optimizationOptions.getImageCompressionOptions().setMaxResolution(300);

        // Optimalkan dokumen PDF menggunakan OptimizationOptions
        pdfDocument.optimizeResources(optimizationOptions);
        _dataDir = _dataDir + "ResizeImages_out.pdf";
        // Simpan dokumen yang diperbarui
        pdfDocument.save(_dataDir);
    }
```

Masalah penting lainnya adalah waktu eksekusi. Namun sekali lagi, kita dapat mengatur pengaturan ini juga. Saat ini, kita dapat menggunakan dua algoritma - Standar dan Cepat. Untuk mengontrol waktu eksekusi, kita harus mengatur properti Versi. Cuplikan berikut menunjukkan algoritma Cepat:

```java
public static void ShrinkingCompressing3() {

        Clock clock = Clock.systemUTC();

        Duration tickDuration = Duration.ofNanos(250000);
        Clock clock1 = Clock.tick(clock, tickDuration);
        System.out.println("Mulai : " + clock.instant());

        // Buka dokumen
        Document pdfDocument = new Document(_dataDir + "ResizeImage.pdf");

        // Inisialisasi OptimizationOptions
        com.aspose.pdf.optimization.OptimizationOptions optimizationOptions = new com.aspose.pdf.optimization.OptimizationOptions();

        // Atur opsi CompressImages
        optimizationOptions.getImageCompressionOptions().setCompressImages(true);

        // Atur opsi ImageQuality
        optimizationOptions.getImageCompressionOptions().setImageQuality(75);

        // Atur Versi Kompresi Gambar ke cepat
        optimizationOptions.getImageCompressionOptions().setVersion(ImageCompressionVersion.Fast);

        // Optimalkan dokumen PDF menggunakan OptimizationOptions
        pdfDocument.optimizeResources(optimizationOptions);

        _dataDir = _dataDir + "ResizeImages_out.pdf";

        // Simpan dokumen yang diperbarui
        pdfDocument.save(_dataDir);
        System.out.println("Selesai : " + clock1.instant());
    }
```

## Menghapus Objek yang Tidak Terpakai

Sebuah dokumen PDF kadang-kadang mengandung objek PDF yang tidak direferensikan dari objek lain dalam dokumen tersebut. Ini dapat terjadi, misalnya, ketika sebuah halaman dihapus dari pohon halaman dokumen tetapi objek halaman itu sendiri tidak dihapus. Menghapus objek-objek ini tidak membuat dokumen menjadi tidak valid, tetapi justru mengecilkannya.

```java
    public static void RemovingUnusedObjects() {

        // Buka dokumen
        Document pdfDocument = new Document(_dataDir + "OptimizeDocument.pdf");
        com.aspose.pdf.optimization.OptimizationOptions optimizationOptions = new com.aspose.pdf.optimization.OptimizationOptions();
        
        optimizationOptions.setRemoveUnusedObjects(true);
        pdfDocument.optimizeResources(optimizationOptions);
        
        _dataDir = _dataDir + "emoveUnusedObjects_out.pdf";

        // Simpan dokumen yang diperbarui
        pdfDocument.save(_dataDir);

    }
```
## Menghapus Aliran yang Tidak Terpakai

Kadang-kadang sebuah dokumen mengandung aliran sumber daya yang tidak terpakai.
 Aliran ini bukan "objek yang tidak digunakan" karena mereka dirujuk dari kamus sumber daya halaman. Ini dapat terjadi dalam kasus di mana sebuah gambar telah dihapus dari halaman tetapi tidak dari sumber daya halaman. Juga, situasi ini sering terjadi ketika halaman diekstraksi dari dokumen dan halaman dokumen memiliki sumber daya "umum", yaitu, objek Sumber Daya yang sama. Isi halaman dianalisis untuk menentukan apakah aliran sumber daya digunakan atau tidak. Aliran yang tidak digunakan dihapus. Terkadang ini mengurangi ukuran dokumen.

```java
public static void RemovingUnusedStream() {
        // Buka dokumen
        Document pdfDocument = new Document(_dataDir + 
        "OptimizeDocument.pdf");
        com.aspose.pdf.optimization.OptimizationOptions optimizationOptions = new com.aspose.pdf.optimization.OptimizationOptions();
        optimizationOptions.setRemoveUnusedStreams(true);
        pdfDocument.optimizeResources(optimizationOptions);
        _dataDir = _dataDir + "removeUnusedObjects_out.pdf";
        
        // Simpan dokumen yang diperbarui
        pdfDocument.save(_dataDir);
        
    }
```
## Menautkan Aliran Duplikat

Terkadang sebuah dokumen berisi beberapa aliran sumber daya yang identik (misalnya gambar). Ini dapat terjadi misalnya ketika sebuah dokumen digabungkan dengan dirinya sendiri. Dokumen keluaran berisi dua salinan independen dari aliran sumber daya yang sama. Kami menganalisis semua aliran sumber daya dan membandingkannya. Jika aliran terduplikat, mereka digabungkan, yaitu, hanya satu salinan yang tersisa, referensi diubah dengan tepat dan salinan objek dihapus. Terkadang ini mengurangi ukuran dokumen.

```java
    public static void LinkingDuplicateStream() {
        // Buka dokumen
        Document pdfDocument = new Document(_dataDir + "OptimizeDocument.pdf");
        com.aspose.pdf.optimization.OptimizationOptions optimizationOptions = new com.aspose.pdf.optimization.OptimizationOptions();
        optimizationOptions.setRemoveUnusedStreams(true);
        
        // Optimalkan dokumen PDF menggunakan OptimizationOptions
        pdfDocument.optimizeResources(optimizationOptions);
        _dataDir = _dataDir + "OptimizeDocument_out.pdf";
        
        // Simpan dokumen yang diperbarui
        pdfDocument.save(_dataDir);
    }
```

Selain itu, kita dapat menggunakan pengaturan AllowReusePageContent. Jika properti ini diatur ke true, konten halaman akan digunakan kembali saat mengoptimalkan dokumen untuk halaman yang identik.

```java
public static void AllowReusePageContent() {
        // Buka dokumen
        Document pdfDocument = new Document(_dataDir + "OptimizeDocument.pdf");
        com.aspose.pdf.optimization.OptimizationOptions optimizationOptions = new com.aspose.pdf.optimization.OptimizationOptions();
        optimizationOptions.setAllowReusePageContent(true);
        
        // Optimalkan dokumen PDF menggunakan OptimizationOptions
        pdfDocument.optimizeResources(optimizationOptions);
        _dataDir = _dataDir + "OptimizeDocument_out.pdf";
        
        // Simpan dokumen yang diperbarui
        pdfDocument.save(_dataDir);
    }
```
## Melepaskan Font yang Tertanam

Jika dokumen menggunakan font yang tertanam, ini berarti bahwa semua data font ditempatkan dalam dokumen.
 Keuntungan adalah bahwa dokumen dapat dilihat terlepas dari apakah font diinstal pada mesin pengguna atau tidak. Tetapi menyematkan font membuat dokumen menjadi lebih besar. Metode unembed fonts menghapus semua font yang disematkan. Ini mengurangi ukuran dokumen tetapi dokumen mungkin menjadi tidak terbaca jika font yang benar tidak diinstal.

```java
    public static void UnembedFonts() {
        // Buka dokumen
        Document pdfDocument = new Document(_dataDir + "OptimizeDocument.pdf");
        com.aspose.pdf.optimization.OptimizationOptions optimizationOptions = new com.aspose.pdf.optimization.OptimizationOptions();
        optimizationOptions.setUnembedFonts(true);
        
        // Optimalkan dokumen PDF menggunakan OptimizationOptions
        pdfDocument.optimizeResources(optimizationOptions);
        
        _dataDir = _dataDir + "OptimizeDocument_out.pdf";
        // Simpan dokumen yang diperbarui
        pdfDocument.save(_dataDir);
    }
```

## Menghapus atau Memadatkan Anotasi

Anotasi dapat dihapus ketika mereka tidak diperlukan. Ketika mereka dibutuhkan tetapi tidak memerlukan pengeditan tambahan, mereka dapat diratakan. Kedua teknik ini akan mengurangi ukuran file.

```java
    public static void FlatteningAnnotations() {
        // Buka dokumen
        Document pdfDocument = new Document(_dataDir + "OptimizeDocument.pdf");

        for (Page page : pdfDocument.getPages()) {
            for (Annotation annotation : page.getAnnotations())
                annotation.flatten();
        }

        _dataDir = _dataDir + "OptimizeDocument_out.pdf";
        // Simpan dokumen yang diperbarui
        pdfDocument.save(_dataDir);
    }

```
## Menghapus Bidang Formulir

Jika dokumen PDF berisi AcroForms, kita dapat mencoba mengurangi ukuran file dengan meratakan bidang formulir.

```java
    public static void RemovingFormFields() {
        // Buka dokumen
        Document pdfDocument = new Document(_dataDir + "OptimizeDocument.pdf");

        // Ratakan Formulir
        if (pdfDocument.getForm().getFields().length > 0) {
            for (Field field : pdfDocument.getForm().getFields()) {
                field.flatten();
            }
        }
        _dataDir = _dataDir + "FlattenForms_out.pdf";
        // simpan dokumen yang diperbarui
        pdfDocument.save(_dataDir);
    }

```
## Mengonversi PDF dari ruang warna RGB ke skala abu-abu

File PDF terdiri dari Teks, Gambar, Lampiran, Anotasi, Grafik dan objek lainnya. Anda mungkin menghadapi kebutuhan untuk mengonversi PDF dari ruang warna RGB ke skala abu-abu agar lebih cepat saat mencetak file PDF tersebut. Selain itu, ketika file dikonversi ke skala abu-abu, ukuran dokumen juga berkurang tetapi dengan perubahan ini, kualitas dokumen mungkin menurun. Saat ini, fitur ini didukung oleh fitur Pre-Flight dari Adobe Acrobat, tetapi ketika berbicara tentang otomasi Office, Aspose.PDF adalah solusi utama untuk memberikan kemudahan tersebut dalam manipulasi dokumen.

Untuk memenuhi kebutuhan ini, cuplikan kode berikut dapat digunakan.

```java
    public static void ConvertRGBtoGrayscale() {

        // Buka dokumen
        Document pdfDocument = new Document(_dataDir + "OptimizeDocument.pdf");

        com.aspose.pdf.RgbToDeviceGrayConversionStrategy strategy = new com.aspose.pdf.RgbToDeviceGrayConversionStrategy();
        for (int idxPage = 1; idxPage <= pdfDocument.getPages().size(); idxPage++) {
            Page page = pdfDocument.getPages().get_Item(idxPage);
            strategy.convert(page);
        }
        pdfDocument.save("output.pdf");
    }
```

## FlateDecode Compression

Aspose.PDF untuk Java mendukung kompresi FlateDecode untuk fungsionalitas Optimisasi PDF. Cuplikan kode berikut menunjukkan cara menggunakan opsi dalam Optimisasi untuk menyimpan gambar dengan kompresi FlateDecode:

```java
    public static void FlateDecodeCompression() {

        // Buka dokumen
        Document pdfDocument = new Document(_dataDir + "OptimizeDocument.pdf");
        com.aspose.pdf.optimization.OptimizationOptions optimizationOptions = new com.aspose.pdf.optimization.OptimizationOptions();

        optimizationOptions.getImageCompressionOptions().setEncoding(ImageEncoding.Flate);

        // Optimalkan dokumen PDF menggunakan OptimizationOptions
        pdfDocument.optimizeResources(optimizationOptions);

        _dataDir = _dataDir + "OptimizeDocument_out.pdf";
        // Simpan dokumen yang telah diperbarui
        pdfDocument.save(_dataDir);
    }
```
## Simpan Gambar dalam XImageCollection 

Aspose.PDF untuk Java menyediakan kemampuan untuk menyimpan gambar baru ke dalam [XImageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/XImageCollection) dengan kompresi FlateDecode.
 Untuk mengaktifkan opsi ini, Anda dapat menggunakan flag ImageFilterType.Flate. Potongan kode berikut menunjukkan cara menggunakan fungsionalitas ini:

```java
    public static void StoreImageInXImageCollection() {
        // Inisialisasi Dokumen
        Document document = new Document();
        document.getPages().add();
        Page page = document.getPages().get_Item(1);

        // Memuat gambar ke dalam stream
        java.io.FileInputStream imageStream = null;
        try {
            imageStream = new java.io.FileInputStream(new java.io.File("input_image1.jpg"));
        } catch (FileNotFoundException e) {
            e.printStackTrace();
            return;
        }
        page.getResources().getImages().add(imageStream, ImageFilterType.Flate);
        XImage ximage = page.getResources().getImages().get_Item(page.getResources().getImages().size());
        page.getContents().add(new com.aspose.pdf.operators.GSave());

        // Mengatur koordinat
        int lowerLeftX = 0;
        int lowerLeftY = 0;
        int upperRightX = 600;
        int upperRightY = 600;
        Rectangle rectangle = new Rectangle(lowerLeftX, lowerLeftY, upperRightX, upperRightY);
        Matrix matrix = new Matrix(new double[] { rectangle.getURX() - rectangle.getLLX(), 0, 0,
                rectangle.getURY() - rectangle.getLLY(), rectangle.getLLX(), rectangle.getLLY() });
        // Menggunakan operator ConcatenateMatrix (menggabungkan matriks): mendefinisikan bagaimana gambar harus ditempatkan
        page.getContents().add(new com.aspose.pdf.operators.ConcatenateMatrix(matrix));
        page.getContents().add(new com.aspose.pdf.operators.Do(ximage.getName()));
        page.getContents().add(new com.aspose.pdf.operators.GRestore());

        document.save(_dataDir + "FlateDecodeCompression.pdf");
    }

}
```