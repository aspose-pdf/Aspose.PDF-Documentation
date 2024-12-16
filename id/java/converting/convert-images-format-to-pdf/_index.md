---
title: Konversi berbagai format Gambar ke PDF
linktitle: Konversi Gambar ke PDF
type: docs
weight: 60
url: /id/java/convert-images-format-to-pdf/
lastmod: "2021-11-19"
description: Topik ini menunjukkan kepada Anda bagaimana pustaka Aspose.PDF untuk Java memungkinkan konversi berbagai format gambar ke PDF.
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

**Aspose.PDF untuk Java** memungkinkan Anda untuk mengonversi berbagai format gambar ke file PDF. Pustaka kami menunjukkan potongan kode untuk mengonversi format gambar yang paling populer, seperti - format BMP, CGM, DICOM, EMF, JPG, PNG, SVG dan TIFF.

## Konversi BMP ke PDF

Konversi file BMP ke dokumen PDF menggunakan pustaka **Aspose.PDF untuk Java**.

Gambar <abbr title="Bitmap Image File">BMP</abbr> adalah file dengan ekstensi .BMP yang mewakili file Gambar Bitmap yang digunakan untuk menyimpan gambar digital bitmap. Gambar-gambar ini independen dari adapter grafis dan juga disebut format file bitmap independen perangkat (DIB). Anda dapat mengonversi BMP ke PDF dengan API Aspose.PDF untuk Java.
 Oleh karena itu, Anda dapat mengikuti langkah-langkah berikut untuk mengonversi gambar BMP:

1. Inisialisasi Dokumen baru
1. Muat file gambar BMP contoh
1. Terakhir, simpan file PDF keluaran

Jadi, cuplikan kode berikut mengikuti langkah-langkah ini dan menunjukkan cara mengonversi BMP ke PDF menggunakan Java:

```java
package com.aspose.pdf.examples;

import java.io.FileNotFoundException;
import java.nio.file.Path;
import java.nio.file.Paths;

import com.aspose.pdf.*;

public final class ConvertBMPtoPDF {

    private ConvertBMPtoPDF() {
    }

    private static Path _dataDir = Paths.get("<set path to samples>");

    public static void main(String[] args) throws FileNotFoundException {
        // Inisialisasi objek dokumen
        Document document = new Document();

        Page page = document.getPages().add();        
        Image image = new Image();
        
        // Muat file gambar BMP contoh
        image.setFile(Paths.get(_dataDir.toString(), "Sample.bmp").toString());
        page.getParagraphs().add(image);
        
        // Simpan dokumen PDF keluaran
        document.save(Paths.get(_dataDir.toString(),"BMPtoPDF.pdf").toString());
    }
}
```

{{% alert color="success" %}}
**Coba konversi BMP ke PDF secara online**

Aspose mempersembahkan aplikasi gratis online ["BMP to PDF"](https://products.aspose.app/pdf/conversion/bmp-to-pdf/), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitas kerjanya.

[![Aspose.PDF Konversi BMP ke PDF menggunakan Aplikasi Gratis](bmp_to_pdf.png)](https://products.aspose.app/pdf/conversion/bmp-to-pdf/)
{{% /alert %}}

## Konversi CGM ke PDF

<abbr title="Computer Graphics Metafile">CGM</abbr> adalah standar ISO yang menyediakan format file gambar 2D berbasis vektor untuk penyimpanan dan pengambilan informasi grafis. CGM adalah format yang independen perangkat. CGM adalah format grafik vektor yang mendukung tiga metode pengkodean berbeda: biner (terbaik untuk kecepatan pembacaan program), berbasis karakter (menghasilkan ukuran file terkecil dan memungkinkan transfer data lebih cepat) atau pengkodean teks jelas (memungkinkan pengguna untuk membaca dan memodifikasi file dengan editor teks).

Cuplikan kode berikut menunjukkan kepada Anda bagaimana mengonversi file CGM ke format PDF menggunakan Aspose.PDF untuk Java.

1. Buat kelas [CgmLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/cgmloadoptions/).
1. Buat sebuah instance dari kelas [Document](https://reference.aspose.com/page/java/com.aspose.page/Document) dengan menyebutkan nama file sumber dan opsi.
1. Simpan dokumen dengan nama file yang diinginkan.

```java
package com.aspose.pdf.examples;

import java.io.FileNotFoundException;
import java.nio.file.Path;
import java.nio.file.Paths;

import com.aspose.pdf.*;

public final class ConvertCGMtoPDF {

    private ConvertCGMtoPDF() {
    }

    private static Path _dataDir = Paths.get("/home/admin1/pdf-examples/Samples");

    public static void main(String[] args) throws FileNotFoundException {
        
        // Buat CGM LoadOptions
        CgmLoadOptions options = new CgmLoadOptions();

        // Inisialisasi objek dokumen
        String cgmFileName = Paths.get(_dataDir.toString(), "corvette.cgm").toString();
        Document document = new Document(cgmFileName, options);

        // Simpan dokumen PDF keluaran
        document.save(Paths.get(_dataDir.toString(),"CGMtoPDF.pdf").toString());
    }
}
```


## Konversi DICOM ke PDF

<abbr title="Digital Imaging and Communications in Medicine">DICOM</abbr> adalah standar untuk menangani, menyimpan, mencetak, dan mengirimkan informasi dalam pencitraan medis. Ini termasuk definisi format file dan protokol komunikasi jaringan.

Aspose.PDF untuk Java memungkinkan Anda untuk mengonversi file DICOM ke format PDF, periksa cuplikan kode berikut:

1. Memuat gambar ke dalam stream
1. Inisialisasi [objek Dokumen](https://reference.aspose.com/pdf/java/com.aspose.pdf/document)
1. Memuat file gambar DICOM contoh
1. Menyimpan dokumen PDF keluaran

```java
package com.aspose.pdf.examples;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.nio.file.Path;
import java.nio.file.Paths;

import com.aspose.pdf.*;

public final class ConvertDICOMtoPDF {

    private ConvertDICOMtoPDF() {
    }

    private static Path _dataDir = Paths.get("/home/admin1/pdf-examples/Samples");

    public static void main(String[] args) throws FileNotFoundException {
        
        // Memuat gambar ke dalam stream
        FileInputStream imageStream = new FileInputStream(
            new java.io.File(Paths.get(_dataDir.toString(),"0002.dcm").toString()));

        // Inisialisasi objek dokumen
        Document document = new Document();
        document.getPages().add();
        
        // Memuat file gambar DICOM contoh
        Image image = new Image();
        image.setFileType(ImageFileType.Dicom);
        image.setImageStream(imageStream);

        document.getPages().get_Item(1).getParagraphs().add(image);

        // Menyimpan dokumen PDF keluaran
        document.save(Paths.get(_dataDir.toString(),"CGMtoPDF.pdf").toString());
    }
}
```


{{% alert color="success" %}}
**Coba untuk mengonversi DICOM ke PDF secara online**

Aspose mempersembahkan aplikasi gratis online ["DICOM ke PDF"](https://products.aspose.app/pdf/conversion/dicom-to-pdf/), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitas kerjanya.

[![Aspose.PDF Konversi DICOM ke PDF menggunakan Aplikasi Gratis](dicom_to_pdf.png)](https://products.aspose.app/pdf/conversion/dicom-to-pdf/)
{{% /alert %}}

## Mengonversi EMF ke PDF

Format metafile yang ditingkatkan (<abbr title="Enhanced metafile format">EMF</abbr>) menyimpan gambar grafis secara independen dari perangkat. Metafile EMF terdiri dari catatan dengan panjang yang bervariasi dalam urutan kronologis yang dapat merender gambar yang disimpan setelah diurai pada perangkat output mana pun.

Kami memiliki beberapa pendekatan untuk mengonversi EMF menjadi PDF.

## Menggunakan kelas Gambar

Dokumen PDF terdiri dari halaman-halaman dan setiap halaman berisi satu atau lebih objek paragraf. Sebuah paragraf dapat berupa teks, gambar, tabel, kotak mengambang, grafik, judul, bidang formulir, atau lampiran.

Untuk mengonversi file gambar menjadi format PDF, bungkus dalam sebuah paragraf.

Dimungkinkan untuk mengonversi gambar di lokasi fisik pada hard drive lokal, ditemukan pada URL web atau dalam instance Stream.

Untuk menambahkan gambar:

1. Buat objek dari kelas com.aspose.pdf.Image.
2. Tambahkan gambar ke koleksi [Paragraphs](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/paragraphs) dari instance halaman.
3. Tentukan jalur atau sumber Gambar.
   - Jika gambar berada di lokasi pada hard drive, tentukan lokasi jalur menggunakan metode [Image.setFile(…)](https://reference.aspose.com/pdf/java/com.aspose.pdf/Image).
   - Jika gambar ditempatkan dalam FileInputStream, berikan objek yang menyimpan gambar ke metode [Image.setImageStream(…)](https://reference.aspose.com/pdf/java/com.aspose.pdf/Image).

Cuplikan kode berikut menunjukkan cara memuat objek gambar, mengatur margin halaman, menempatkan gambar di halaman, dan menyimpan output sebagai PDF.

```java
package com.aspose.pdf.examples;

import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;
import java.io.File;

/**
 * Konversi EMF ke PDF
 */

import java.io.FileNotFoundException;
import java.io.IOException;
import java.nio.file.Path;
import java.nio.file.Paths;

import javax.imageio.ImageIO;

import com.aspose.pdf.*;

public final class ConvertEMFtoPDF {

    private ConvertEMFtoPDF() {
    }

    private static Path _dataDir = Paths.get("/home/admin1/pdf-examples/Samples");

    public static void main(String[] args) throws IOException {

        convertEMFtoPDF_01();
        convertEMFtoPDF_02();
    }

    

    public static void convertEMFtoPDF_01() throws FileNotFoundException {                
        // Instansiasi Objek Dokumen
        Document doc = new Document();
        // Tambahkan halaman ke koleksi halaman dokumen
        Page page = doc.getPages().add();
        // Muat file gambar sumber ke objek Stream
        java.io.FileInputStream fs = new java.io.FileInputStream(
            Paths.get(_dataDir.toString(),"source.emf").toString());

        // Atur margin agar gambar sesuai, dll.
        page.getPageInfo().getMargin().setBottom(0);
        page.getPageInfo().getMargin().setTop(0);
        page.getPageInfo().getMargin().setLeft(0);
        page.getPageInfo().getMargin().setRight(0);

        page.setCropBox(new Rectangle(0, 0, 400, 400));
        // Buat objek gambar
        Image image1 = new Image();
        // Tambahkan gambar ke dalam koleksi paragraf dari bagian
        page.getParagraphs().add(image1);
        // Atur stream file gambar
        image1.setImageStream(fs);
        // Simpan file PDF hasil
        doc.save("EMFtoPDF_01.pdf");
    }   
    public static void convertEMFtoPDF_02() throws IOException {
        // lihat kode di bawah
    } 
}
```


### Tambahkan gambar dari BufferedImage

Aspose.PDF untuk Java juga menawarkan fitur untuk memuat gambar dari instance Stream di mana gambar dapat dimuat ke objek BufferedImage dan dapat ditempatkan di dalam koleksi paragraf dari file Pdf.

```java
public static void convertEMFtoPDF_02() throws IOException {    
    Document doc = new Document();
    // tambahkan halaman ke koleksi halaman dari file Pdf
    Page page = doc.getPages().add();
    // buat instance gambar
    Image image1 = new Image();
    // buat instance BufferedImage
    java.awt.image.BufferedImage bufferedImage = ImageIO.read(new File("source.emf"));
    ByteArrayOutputStream baos = new ByteArrayOutputStream();
    // tulis BufferedImage ke instance OutputStream
    ImageIO.write(bufferedImage, "emf", baos);
    baos.flush();
    ByteArrayInputStream bais = new ByteArrayInputStream(baos.toByteArray());
    // tambahkan gambar ke koleksi paragraf dari halaman pertama
    page.getParagraphs().add(image1);
    // setel aliran gambar sebagai OutputStream yang menampung BufferedImage
    image1.setImageStream(bais);
    // simpan file PDF yang dihasilkan
    doc.save("BufferedImage.pdf");
}
```


## Tambahkan Gambar menggunakan Operator PDF

Setiap objek halaman PDF berisi metode [getResources()](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#getResources--) dan [getContents()](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#getContents--). Sumber daya dapat berupa gambar dan formulir, misalnya, sementara konten diwakili oleh serangkaian operator PDF. Setiap operator memiliki nama dan argumennya masing-masing.

Contoh ini menggunakan operator untuk menambahkan gambar ke file PDF.

Untuk menambahkan gambar ke file PDF yang sudah ada:

1. Buat objek [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) dan buka dokumen PDF input.
1. Dapatkan halaman yang ingin Anda tambahkan gambar.
1. Tambahkan gambar ke koleksi [getResources()](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#getResources--) halaman.
1. Gunakan operator untuk menempatkan gambar pada halaman:
   1. Gunakan operator GSave untuk menyimpan status grafis saat ini.
   1. Gunakan operator ConcatenateMatrix untuk menentukan di mana gambar akan ditempatkan.

1. Gunakan operator Do untuk menggambar gambar pada halaman.
   1. Terakhir, gunakan operator GRestore untuk menyimpan status grafis yang diperbarui.
1. Simpan file.

Cuplikan kode berikut menunjukkan cara menambahkan gambar ke dokumen PDF.

```java
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.Pdf-for-Java
// Buka dokumen
Document pdfDocument1 = new Document("input.pdf");

// Tetapkan koordinat
int lowerLeftX = 100;
int lowerLeftY = 100;
int upperRightX = 200;
int upperRightY = 200;

// Dapatkan halaman yang ingin Anda tambahkan gambar ke
Page page = pdfDocument1.getPages().get_Item(1);

// Muat gambar ke dalam stream
java.io.FileInputStream imageStream = new java.io.FileInputStream(new java.io.File("input_image1.jpg"));

// Tambahkan gambar ke koleksi Gambar dari sumber daya halaman
page.getResources().getImages().add(imageStream);

// Menggunakan operator GSave: operator ini menyimpan status grafis saat ini
page.getContents().add(new Operator.GSave());

// Buat objek Rectangle dan Matrix
Rectangle rectangle = new Rectangle(lowerLeftX, lowerLeftY, upperRightX, upperRightY);
Matrix matrix = new Matrix(new double[] { rectangle.getURX() - rectangle.getLLX(), 0, 0, rectangle.getURY() - rectangle.getLLY(), rectangle.getLLX(), rectangle.getLLY() });

// Menggunakan operator ConcatenateMatrix (menggabungkan matriks): mendefinisikan bagaimana gambar harus ditempatkan
page.getContents().add(new Operator.ConcatenateMatrix(matrix));
XImage ximage = page.getResources().getImages().get_Item(page.getResources().getImages().size());

// Menggunakan operator Do: operator ini menggambar gambar
page.getContents().add(new Operator.Do(ximage.getName()));

// Menggunakan operator GRestore: operator ini mengembalikan status grafis
page.getContents().add(new Operator.GRestore());

// Simpan PDF baru
pdfDocument1.save("Updated_document.pdf");

// Tutup stream gambar
imageStream.close();
```


{{% alert color="success" %}}
**Cobalah mengonversi EMF ke PDF secara online**

Aspose mempersembahkan aplikasi online gratis ["EMF to PDF"](https://products.aspose.app/pdf/conversion/emf-to-pdf/), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitas kerjanya.

[![Aspose.PDF Konversi EMF ke PDF menggunakan Aplikasi Gratis](emf_to_pdf.png)](https://products.aspose.app/pdf/conversion/emf-to-pdf/)
{{% /alert %}}

## Konversi JPG ke PDF

Tidak perlu bingung bagaimana mengonversi JPG ke PDF, karena pustaka Apose.PDF untuk Java memiliki solusi terbaik.

Anda dapat dengan sangat mudah mengonversi gambar JPG ke PDF dengan Aspose.PDF untuk Java dengan mengikuti langkah-langkah berikut:

1. Inisialisasi objek dari kelas [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document)
1. Muat gambar JPG dan tambahkan ke paragraf
1. Simpan PDF keluaran

Potongan kode di bawah ini menunjukkan cara mengonversi Gambar JPG ke PDF menggunakan Java:

```java
package com.aspose.pdf.examples;

import java.io.FileNotFoundException;
import java.nio.file.Path;
import java.nio.file.Paths;

import com.aspose.pdf.*;

public final class ConvertJPEGtoPDF {

    private static Path _dataDir = Paths.get("/home/aspose/pdf-examples/Samples");

    public static void main(String[] args) throws FileNotFoundException {
        // Inisialisasi objek dokumen
        Document document = new Document();

        Page page = document.getPages().add();
        Image image = new Image();

        // Muat file gambar JPEG contoh
        image.setFile(Paths.get(_dataDir.toString(), "Sample.jpg").toString());
        page.getParagraphs().add(image);

        // Simpan dokumen PDF keluaran
        document.save(Paths.get(_dataDir.toString(),"JPEGtoPDF.pdf").toString());
    }
}
```


{{% alert color="success" %}}
**Coba ubah JPG ke PDF secara online**

Aspose menghadirkan aplikasi online gratis ["JPG ke PDF"](https://products.aspose.app/pdf/conversion/jpg-to-pdf/), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitas kerjanya.

[![Aspose.PDF Konversi JPG ke PDF menggunakan Aplikasi Gratis](jpg_to_pdf.png)](https://products.aspose.app/pdf/conversion/jpg-to-pdf/)
{{% /alert %}}

## Konversi PNG ke PDF

**Aspose.PDF untuk Java** mendukung fitur untuk mengonversi gambar PNG ke format PDF. Periksa cuplikan kode berikut untuk menyadari tugas Anda.

<abbr title="Portable Network Graphics">PNG</abbr> mengacu pada jenis format file gambar raster yang menggunakan kompresi tanpa kehilangan, yang membuatnya populer di antara penggunanya.

Anda dapat mengonversi gambar PNG ke PDF menggunakan langkah-langkah berikut:

1. Muat gambar PNG input
1. Baca nilai tinggi dan lebar
1. Buat dokumen baru dan tambahkan Halaman
1. Atur dimensi halaman
1. Simpan file keluaran

Selain itu, cuplikan kode di bawah ini menunjukkan cara mengonversi PNG ke PDF dalam aplikasi Java Anda:

```java
package com.aspose.pdf.examples;

/**
 * Konversi PNG ke PDF
 */

import java.io.FileNotFoundException;
import java.nio.file.Path;
import java.nio.file.Paths;

import com.aspose.pdf.*;

public final class ConvertPNGtoPDF {

    private ConvertPNGtoPDF() {
    }

    private static Path _dataDir = Paths.get("/home/admin1/pdf-examples/Samples");

    public static void main(String[] args) throws FileNotFoundException {
        // Inisialisasi objek dokumen
        Document document = new Document();

        Page page = document.getPages().add();
        Image image = new Image();

        // Muat file gambar BMP contoh
        image.setFile(Paths.get(_dataDir.toString(), "Sample.png").toString());


        page.getPageInfo().getMargin().setBottom(0);
        page.getPageInfo().getMargin().setTop(0);
        page.getPageInfo().getMargin().setRight (0);
        page.getPageInfo().getMargin().setLeft (0);
        page.getParagraphs().add(image);

        // Simpan dokumen PDF keluaran
        document.save(Paths.get(_dataDir.toString(), "PNGtoPDF.pdf").toString());
    }
}

```


{{% alert color="success" %}}
**Cobalah mengonversi PNG ke PDF secara online**

Aspose mempersembahkan aplikasi online gratis ["PNG to PDF"](https://products.aspose.app/pdf/conversion/png-to-pdf/), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitas kerjanya.

[![Aspose.PDF Konversi PNG ke PDF menggunakan Aplikasi Gratis](png_to_pdf.png)](https://products.aspose.app/pdf/conversion/png-to-pdf/)
{{% /alert %}}

## Konversi SVG ke PDF

Scalable Vector Graphics (SVG) adalah keluarga spesifikasi dari format file berbasis XML untuk grafik vektor dua dimensi, baik statis maupun dinamis (interaktif atau animasi). Spesifikasi SVG adalah standar terbuka yang telah dikembangkan oleh World Wide Web Consortium (W3C) sejak tahun 1999.

Gambar SVG dan perilakunya didefinisikan dalam file teks XML.
 Ini berarti bahwa mereka dapat dicari, diindeks, diskrip, dan, jika diperlukan, dikompresi. Sebagai file XML, gambar SVG dapat dibuat dan diedit dengan editor teks apa pun, tetapi sering kali lebih mudah untuk membuatnya dengan program menggambar seperti Inkscape.

## Cara mengonversi file SVG ke format PDF

Untuk mengonversi file SVG ke PDF, gunakan kelas bernama [SvgLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/svgloadoptions) yang digunakan untuk menginisialisasi objek [LoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/LoadOptions). Kemudian, objek ini diteruskan sebagai argumen selama inisialisasi objek [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document) dan membantu mesin rendering PDF untuk menentukan format input dari dokumen sumber.

Cuplikan kode berikut menunjukkan proses konversi file SVG menjadi format PDF.

```java
// Inisialisasi objek dokumen

String pdfDocumentFileName = Paths.get(_dataDir.toString(), "svg_test.pdf").toString();
String svgDocumentFileName = Paths.get(_dataDir.toString(), "car.svg").toString();

SvgLoadOptions option = new SvgLoadOptions();
Document pdfDocument = new Document(svgDocumentFileName, option);
pdfDocument.save(pdfDocumentFileName);
```

{{% alert color="success" %}}
**Coba mengonversi format SVG ke PDF secara online**

Aspose.PDF untuk Java menyajikan aplikasi online gratis ["SVG ke PDF"](https://products.aspose.app/pdf/conversion/svg-to-pdf), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitas kerjanya.

[![Konversi Aspose.PDF SVG ke PDF dengan Aplikasi Gratis](svg_to_pdf.png)](https://products.aspose.app/pdf/conversion/svg-to-pdf)
{{% /alert %}}

## Mengonversi TIFF ke PDF

**Aspose.PDF untuk Java** mendukung format file, baik itu gambar <abbr title="Tag Image File Format">TIFF</abbr> satu frame atau multi-frame. Ini berarti Anda dapat mengonversi gambar TIFF ke PDF dalam aplikasi Java Anda.

TIFF atau TIF, Tagged Image File Format, mewakili gambar raster yang dimaksudkan untuk penggunaan pada berbagai perangkat yang mematuhi standar format file ini.
 TIFF image dapat berisi beberapa frame dengan gambar yang berbeda. Format file Aspose.PDF juga didukung, baik itu gambar TIFF satu frame atau multi-frame. Jadi, Anda dapat mengonversi gambar TIFF ke PDF dalam aplikasi Java Anda. Oleh karena itu, kita akan mempertimbangkan contoh mengonversi gambar TIFF multi-halaman ke dokumen PDF multi-halaman dengan langkah-langkah berikut:

1. Membuat instance dari kelas Document
1. Memuat gambar TIFF input
1. Akhirnya, simpan gambar sebagai halaman PDF

Selain itu, potongan kode berikut menunjukkan cara mengonversi gambar TIFF multi-halaman atau multi-frame ke PDF:

```java
import com.aspose.pdf.Document;
import com.aspose.pdf.Image;
import com.aspose.pdf.Page;

import java.io.IOException;
import java.nio.file.Path;
import java.nio.file.Paths;

/**
 * Mengonversi TIFF ke PDF.
 */
public final class ConvertTIFFtoPDF {

    private static final Path DATA_DIR = Paths.get("/home/aspose/pdf-examples/Samples");

    private ConvertTIFFtoPDF() {
    }

    public static void run() throws IOException {
        // Inisialisasi objek dokumen
        Document document = new Document();

        Page page = document.getPages().add();
        Image image = new Image();

        image.setFile(Paths.get(DATA_DIR.toString(), "Sample.tiff").toString());
        page.getParagraphs().add(image);

        // Simpan dokumen PDF keluaran
        document.save(Paths.get(DATA_DIR.toString(), "TIFFtoPDF.pdf").toString());
        document.close();
    }    
}
```