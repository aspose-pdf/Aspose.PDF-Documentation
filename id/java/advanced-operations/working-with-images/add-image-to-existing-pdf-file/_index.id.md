---
title: Menambahkan Gambar ke File PDF yang Ada 
linktitle: Menambahkan Gambar
type: docs
weight: 10
url: /java/menambahkan-gambar-ke-file-pdf-yang-ada/
description: Bagian ini menjelaskan cara menambahkan gambar ke file PDF yang ada menggunakan pustaka Java.
lastmod: "2021-06-05"
---

Setiap halaman PDF memiliki properti Resources dan Contents. Resources dapat berupa gambar dan formulir misalnya, sedangkan konten diwakili oleh serangkaian operator PDF. Setiap operator memiliki nama dan argumen. Contoh ini menggunakan operator untuk menambahkan gambar ke file PDF.

Untuk menambahkan gambar ke file PDF yang ada:

- Buat objek [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) dan buka dokumen PDF input.
- Dapatkan halaman yang ingin Anda tambahkan gambar.
- Tambahkan gambar ke dalam koleksi [getResources](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#getResources--) halaman.
- Gunakan operator untuk menempatkan gambar pada halaman:
- Gunakan operator GSave untuk menyimpan status grafis saat ini.

- Gunakan operator [ConcatenateMatrix](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators.class-use/concatenatematrix) untuk menentukan di mana gambar akan ditempatkan.
- Gunakan operator [Do](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/class-use/Do) untuk menggambar gambar pada halaman.
- Terakhir, gunakan operator [GRestore](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators.class-use/grestore) untuk menyimpan keadaan grafis yang diperbarui.
- Simpan file.

Cuplikan kode berikut menunjukkan cara menambahkan gambar dalam dokumen PDF.

```java
package com.aspose.pdf.examples;

import java.awt.image.BufferedImage;
import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;

import javax.imageio.ImageIO;

import com.aspose.pdf.*;
import com.aspose.pdf.facades.PdfFileMend;
import com.aspose.pdf.operators.*;

public class ExampleAddImages {

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void AddImageToExistingPDF() throws IOException {
        // Buka dokumen
        Document pdfDocument1 = new Document(_dataDir + "sample.pdf");

        // Atur koordinat
        int lowerLeftX = 50;
        int lowerLeftY = 750;
        int upperRightX = 100;
        int upperRightY = 800;

        // Dapatkan halaman yang ingin Anda tambahkan gambar
        Page page = pdfDocument1.getPages().get_Item(1);

        // Muat gambar ke dalam stream
        java.io.FileInputStream imageStream = new java.io.FileInputStream(new java.io.File(_dataDir + "logo.png"));

        // Tambahkan gambar ke koleksi Images dari sumber daya halaman
        page.getResources().getImages().add(imageStream);

        // Menggunakan operator GSave: operator ini menyimpan keadaan grafis saat ini
        page.getContents().add(new GSave());

        // Buat objek Rectangle dan Matrix
        Rectangle rectangle = new Rectangle(lowerLeftX, lowerLeftY, upperRightX, upperRightY);
        Matrix matrix = new Matrix(new double[] { rectangle.getURX() - rectangle.getLLX(), 0, 0,
                rectangle.getURY() - rectangle.getLLY(), rectangle.getLLX(), rectangle.getLLY() });

        // Menggunakan operator ConcatenateMatrix (menggabungkan matriks): mendefinisikan
        // bagaimana gambar harus ditempatkan
        page.getContents().add(new ConcatenateMatrix(matrix));
        XImage ximage = page.getResources().getImages().get_Item(page.getResources().getImages().size());

        // Menggunakan operator Do: operator ini menggambar gambar
        page.getContents().add(new Do(ximage.getName()));

        // Menggunakan operator GRestore: operator ini mengembalikan keadaan grafis
        page.getContents().add(new GRestore());

        // Simpan PDF baru
        pdfDocument1.save(_dataDir + "updated_document.pdf");

        // Tutup stream gambar
        imageStream.close();
    }
```


## Menambahkan gambar dari BufferedImage ke dalam PDF

Mulai rilis Aspose.PDF untuk Java 9.5.0, kami telah memperkenalkan dukungan untuk menambahkan gambar dari instance BufferedImage ke dokumen PDF. Untuk mendukung kebutuhan ini, sebuah metode diimplementasikan: [XImageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/XImageCollection).add(BufferedImage image);

```java
    public static void AddingImageFromBufferedImageIntoPDF() throws IOException {
        BufferedImage originalImage = ImageIO.read(new File("anyImage.jpg"));
        Document pdfDocument = new Document();
        Page page = pdfDocument.getPages().add();
        page.getResources().getImages().add(originalImage);
    }
```
Anda dapat menggunakan InputStream apapun dan tidak hanya objek FileInputStream untuk menambahkan gambar. Jadi ketika menggunakan objek java.io.ByteArrayInputStream, Anda tidak perlu menyimpan file apapun ke dalam sistem:

```java
    public static void AddingImageFromBufferedImageIntoPDF2() throws IOException {
        BufferedImage originalImage = ImageIO.read(new File("anyImage.jpg"));
        ByteArrayOutputStream baos = new ByteArrayOutputStream();

        Document pdfDocument = new Document();
        ImageIO.write(originalImage, "jpg", baos);
        baos.flush();
        Page page = pdfDocument.getPages().get_Item(1);
        page.getResources().getImages().add(new ByteArrayInputStream(baos.toByteArray()));
    }
```


## Menambahkan Gambar dalam File PDF yang Ada (Facades)

Ada juga cara alternatif yang lebih mudah untuk menambahkan gambar ke file PDF. Anda dapat menggunakan metode AddImage dari kelas [PdfFileMend](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileMend). Metode AddImage memerlukan gambar yang akan ditambahkan, nomor halaman di mana gambar perlu ditambahkan dan informasi koordinat. Setelah itu, simpan file PDF yang telah diperbarui menggunakan metode Close.

Cuplikan kode berikut menunjukkan kepada Anda cara menambahkan gambar dalam file PDF yang ada.

```java
    public static void AddImageInAnExistingPDFFile_Facades() {
        // Membuka dokumen
        PdfFileMend mender = new PdfFileMend();

        // Membuat objek PdfFileMend untuk menambahkan teks
        mender.bindPdf(_dataDir + "AddImage.pdf");

        // Menambahkan gambar dalam file PDF
        mender.addImage(_dataDir + "aspose-logo.jpg", 1, 100, 600, 200, 700);

        // Menyimpan perubahan
        mender.save(_dataDir + "AddImage_out.pdf");

        // Menutup objek PdfFileMend
        mender.close();
    }
```


## Tambahkan Referensi dari satu Gambar beberapa kali dalam Dokumen PDF

Terkadang kita memiliki kebutuhan untuk menggunakan gambar yang sama beberapa kali dalam dokumen PDF. Menambahkan instance baru meningkatkan ukuran dokumen PDF yang dihasilkan. Kami telah menambahkan metode baru XImageCollection.add(XImage) yang mendukung objek Ximage untuk ditambahkan ke dalam Koleksi Gambar. Metode ini memungkinkan untuk menambahkan referensi ke objek PDF yang sama seperti gambar asli yang mengoptimalkan ukuran Dokumen PDF.

```java
    public static void AddReferenceOfaSingleImageMultipleTimes() throws FileNotFoundException {
        Rectangle imageRectangle = new Rectangle(0, 0, 30, 15);
        Document document = new Document(_dataDir + "sample.pdf");
        document.getPages().add();
        document.getPages().add();
        java.io.FileInputStream imageStream = new java.io.FileInputStream(
                new java.io.File(_dataDir + "aspose-logo.png"));

        XImage image = null;

        for (Page page : document.getPages()) {
            WatermarkAnnotation annotation = new WatermarkAnnotation(page, page.getRect());
            XForm form = annotation.getAppearance().get_Item("N");
            form.setBBox(page.getRect());
            String name;
            if (image == null) {
                name = form.getResources().getImages().add(imageStream);
                image = form.getResources().getImages().get_Item(name);
            } else {
                name = form.getResources().getImages().add(image);
            }
            form.getContents().add(new GSave());
            form.getContents().add(new ConcatenateMatrix(
                    new Matrix(imageRectangle.getWidth(), 0, 0, imageRectangle.getHeight(), 0, 0)));
            form.getContents().add(new Do(name));
            form.getContents().add(new GRestore());
            page.getAnnotations().add(annotation, false);
            imageRectangle = new Rectangle(0, 0, imageRectangle.getWidth() * 1.01, imageRectangle.getHeight() * 1.01);
        }
        document.save(_dataDir + "output.pdf");
    }
```


## Mengidentifikasi apakah gambar di dalam PDF berwarna atau hitam putih

Berbagai jenis kompresi dapat diterapkan pada gambar untuk mengurangi ukurannya. Jenis kompresi yang diterapkan pada gambar tergantung pada ColorSpace gambar sumber yaitu jika gambar berwarna (RGB), maka terapkan kompresi JPEG2000, dan jika hitam putih, maka kompresi JBIG2/JBIG2000 harus diterapkan. Oleh karena itu, mengidentifikasi setiap jenis gambar dan menggunakan jenis kompresi yang tepat akan menciptakan output yang terbaik/teroptimasi.

Sebuah file PDF dapat berisi elemen-elemen seperti Teks, Gambar, Grafik, Lampiran, Anotasi, dll. dan jika file PDF sumber berisi gambar, kita dapat menentukan ruang warna gambar dan menerapkan kompresi yang tepat untuk gambar guna mengurangi ukuran file PDF. Cuplikan kode berikut menunjukkan langkah-langkah untuk mengidentifikasi apakah gambar di dalam PDF berwarna atau hitam putih.

```java
    public static void CheckColors() {

        Document document = new Document(_dataDir + "test4.pdf");
        try {
            // iterasi melalui semua halaman file PDF
            for (Page page : (Iterable<Page>) document.getPages()) {
                // buat instance Image Placement Absorber
                ImagePlacementAbsorber abs = new ImagePlacementAbsorber();
                page.accept(abs);
                for (ImagePlacement ia : (Iterable<ImagePlacement>) abs.getImagePlacements()) {
                    /* ColorType */
                    int colorType = ia.getImage().getColorType();
                    switch (colorType) {
                    case ColorType.Grayscale:
                        System.out.println("Gambar Grayscale");
                        break;
                    case ColorType.Rgb:
                        System.out.println("Gambar Berwarna");
                        break;
                    }
                }
            }
        } catch (Exception ex) {
            System.out.println("Kesalahan membaca file = " + document.getFileName());
        }
    }
}
```