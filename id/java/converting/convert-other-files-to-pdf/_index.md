---
title: Mengonversi berbagai format file ke PDF
linktitle: Mengonversi format file lain ke PDF
type: docs
weight: 80
url: id/java/convert-other-files-to-pdf/
lastmod: "2021-11-19"
description: Topik ini menunjukkan bagaimana Aspose.PDF memungkinkan untuk mengonversi format file lain ke dokumen PDF.
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

## Mengonversi EPUB ke PDF

**Aspose.PDF untuk Java** memungkinkan Anda dengan mudah mengonversi file EPUB ke format PDF.

<abbr title="electronic publication">EPUB</abbr> (singkatan dari electronic publication) adalah standar buku elektronik gratis dan terbuka dari International Digital Publishing Forum (IDPF). File memiliki ekstensi .epub. EPUB dirancang untuk konten yang dapat diatur ulang, yang berarti bahwa pembaca EPUB dapat mengoptimalkan teks untuk perangkat tampilan tertentu.

Untuk mengonversi file EPUB ke format PDF, Aspose.PDF untuk Java memiliki kelas bernama [EpubLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/EpubLoadOptions) yang digunakan untuk memuat file sumber EPUB.
 Setelah itu, objek tersebut diteruskan sebagai argumen ke inisialisasi objek [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document), karena ini membantu mesin rendering PDF untuk menentukan format input dokumen sumber.

Cuplikan kode berikut menunjukkan proses konversi file EPUB menjadi format PDF.

1. Buat [`LoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/loadoptions) EPUB.
1. Inisialisasi objek [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/document).
1. Simpan dokumen PDF keluaran.

```java
package com.aspose.pdf.examples;

import java.io.FileNotFoundException;
import java.nio.file.Path;
import java.nio.file.Paths;

import com.aspose.pdf.*;

public final class ConvertEPUBtoPDF {

    private ConvertEPUBtoPDF() {
    }

    private static Path _dataDir = Paths.get("/home/admin1/pdf-examples/Samples");

    public static void main(String[] args) throws FileNotFoundException {
        
        // Buat EPUB LoadOptions
        EpubLoadOptions options = new EpubLoadOptions();

        // Inisialisasi objek document
        String epubFileName = Paths.get(_dataDir.toString(), "aliceDynamic.epub").toString();
        Document document = new Document(epubFileName, options);

        // Simpan dokumen PDF keluaran
        document.save(Paths.get(_dataDir.toString(),"EPUBtoPDF.pdf").toString());
    }
}
```

{{% alert color="success" %}}
**Cobalah untuk mengonversi EPUB ke PDF secara online**

Aspose.PDF untuk Java mempersembahkan aplikasi gratis online ["EPUB ke PDF"](https://products.aspose.app/pdf/conversion/epub-to-pdf), di mana Anda dapat mencoba menyelidiki fungsi dan kualitas kerjanya.

[![Konversi Aspose.PDF EPUB ke PDF dengan Aplikasi Gratis](epub.png)](https://products.aspose.app/pdf/conversion/epub-to-pdf)
{{% /alert %}}

## Konversi Markdown ke PDF

**Fitur ini didukung oleh versi 19.6 atau lebih tinggi.**

{{% alert color="success" %}}
**Cobalah untuk mengonversi Markdown ke PDF secara online**

Aspose.PDF untuk Java mempersembahkan aplikasi gratis online ["Markdown ke PDF"](https://products.aspose.app/pdf/conversion/md-to-pdf), di mana Anda dapat mencoba menyelidiki fungsi dan kualitas kerjanya.

[![Konversi Aspose.PDF Markdown ke PDF dengan Aplikasi Gratis](markdown.png)](https://products.aspose.app/pdf/conversion/md-to-pdf)
{{% /alert %}}

Markdown adalah alat konversi teks ke HTML untuk penulis web.
 Markdown memungkinkan Anda menulis dalam format teks biasa yang mudah dibaca dan ditulis dan kemudian mengubahnya menjadi XHTML (atau HTML) yang valid secara struktural.

Cuplikan kode berikut menunjukkan cara menggunakan fungsionalitas ini dengan Aspose.PDF untuk Java:

```java
package com.aspose.pdf.examples;

import java.io.FileNotFoundException;
import java.nio.file.Path;
import java.nio.file.Paths;

import com.aspose.pdf.*;

public final class ConvertMDtoPDF {

    private ConvertMDtoPDF() {
    }

    private static Path _dataDir = Paths.get("/home/admin1/pdf-examples/Samples");

    public static void main(String[] args) throws FileNotFoundException {
        
        // Memperkenalkan objek opsi Muat Latex
        MdLoadOptions options = new MdLoadOptions();
        
        // Membuat objek Dokumen
        String markdownFileName = Paths.get(_dataDir.toString(), "samplefile.md").toString();
        Document document = new Document(markdownFileName, options);

        // Simpan dokumen PDF keluaran
        document.save(Paths.get(_dataDir.toString(),"MarkdownToPDF.pdf").toString());
    }
}

```

## Mengonversi PCL ke PDF

<abbr title="Printer Command Language">PCL</abbr> (Printer Command Language) adalah bahasa printer Hewlett-Packard yang dikembangkan untuk mengakses fitur printer standar. PCL level 1 hingga 5e/5c adalah bahasa berbasis perintah yang menggunakan urutan kontrol yang diproses dan diinterpretasikan sesuai urutan diterimanya. Pada tingkat konsumen, aliran data PCL dihasilkan oleh driver cetak. Keluaran PCL juga dapat dengan mudah dihasilkan oleh aplikasi khusus.

{{% alert color="success" %}}
**Coba konversi PCL ke PDF online**

Aspose.PDF untuk Java menyajikan kepada Anda aplikasi gratis online ["PCL ke PDF"](https://products.aspose.app/pdf/conversion/pcl-to-pdf), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitas kerjanya.

[![Aspose.PDF Konversi PCL ke PDF dengan Aplikasi Gratis](pcl_to_pdf.png)](https://products.aspose.app/pdf/conversion/pcl-to-pdf)
{{% /alert %}}

**Saat ini, hanya PCL5 dan versi yang lebih lama yang didukung.**

|**Set Perintah**|**Dukungan**|**Pengecualian**|**Deskripsi**|
|Perintah kontrol pekerjaan|+|Mode pencetakan dupleks|Mengontrol proses pencetakan: jumlah salinan, tempat keluaran, pencetakan simplex/dupleks, offset kiri dan atas dll.|
|Perintah kontrol halaman|+|Perintah Lompatan Perforasi|Menentukan ukuran halaman, margin, orientasi halaman antar-baris, jarak antar-karakter dll.|
|Perintah Pemposisian Kursor|+| |Menentukan posisi kursor dan, dengan demikian, asal teks, gambar raster atau vektor dan detailnya.|

|Perintah pemilihan font|+|<p>1. Perintah Data Cetak Transparan.</p><p>2. Font lunak yang tersemat. Dalam versi saat ini, alih-alih membuat font lunak, pustaka kami memilih font yang sesuai dari font TrueType "keras" yang ada yang terpasang pada mesin target. <br>   Kesesuaian ditentukan oleh rasio lebar/tinggi. <br>   Fitur ini hanya berfungsi untuk font Bitmap dan TrueType dan tidak menjamin bahwa teks yang dicetak dengan font lunak akan relevan dengan yang ada di file sumber. <br>   Karena kode karakter dalam font lunak dapat tidak sesuai dengan yang default.</p><p>3. Set Simbol yang Didefinisikan Pengguna.</p>|Mengizinkan pemuatan font lunak (tersemat) dari file PCL dan mengelolanya dalam memori.|
|Perintah grafik raster|+|Hanya hitam & putih|Mengizinkan pemuatan gambar raster dari file PCL ke memori, menentukan parameter raster <br>seperti lebar, tinggi, jenis kompresi, resolusi, dll.|
|Perintah warna|+| |Mengizinkan pewarnaan untuk semua objek yang dapat dicetak.|
|Perintah Model Cetak|+| |Mengizinkan pengisian teks, gambar raster, dan area persegi panjang dengan pola yang telah ditentukan sebelumnya dan yang didefinisikan oleh pengguna, menentukan mode transparansi untuk pola dan gambar raster sumber.
 <br>Pola yang telah ditentukan adalah arsir, arsir silang, dan bayangan.|
|Perintah isi area persegi panjang|+| |Memungkinkan pembuatan dan pengisian area persegi panjang dengan pola.|
|Perintah Grafis Vektor HP-GL/2|+|Perintah Vektor Berlayar (SV), Perintah Mode Transparansi (TR), Perintah Data Transparan (TD), RO (Putar Sistem Koordinat), Perintah Font Skala atau Bitmap (SB), Perintah Kemiringan Karakter (SL) dan Ruang Ekstra (ES) tidak diterapkan dan perintah DV (Tentukan Jalur Teks Variabel) direalisasikan dalam versi beta.|<p>- Memungkinkan pemuatan gambar vektor HP-GL/2 dari file PCL ke dalam memori. Gambar vektor memiliki titik asal di sudut kiri bawah area cetak, dapat diskalakan, diterjemahkan, diputar, dan dipotong.</p><p>- Gambar vektor dapat mengandung teks, sebagai label, dan bentuk geometris seperti persegi panjang, lingkaran, elips, garis, busur, kurva bezier, dan bentuk kompleks yang terdiri dari yang sederhana.</p><p>- Bentuk tertutup termasuk huruf dari label dapat diisi dengan isi padat atau pola vektor.</p><p>- Pola dapat berupa arsiran, garis silang, bayangan, raster yang ditentukan pengguna, PCL arsiran atau garis silang dan PCL yang ditentukan pengguna. Pola PCL adalah raster. Label dapat diputar, diskalakan, dan diarahkan secara individual dalam empat arah: atas, bawah, kiri, dan kanan. Arah Kiri dan Kanan melibatkan pengaturan huruf satu demi satu. Arah Atas dan Bawah melibatkan pengaturan huruf satu di bawah yang lain.</p>|
|Macross|―| |Memungkinkan memuat urutan perintah PCL ke dalam memori dan menggunakan urutan ini berkali-kali, misalnya, untuk mencetak header halaman atau mengatur satu format untuk satu set halaman.|
|Unicode text|―| |Memungkinkan pencetakan karakter non-ASCII. Tidak diterapkan karena kurangnya file contoh dengan teks Unicode  
|PCL6 (PCL-XL)| |Diimplementasikan hanya dalam versi Beta karena kekurangan file uji. Font yang tertanam juga tidak didukung. Ekstensi JetReady tidak didukung karena tidak mungkin memiliki spesifikasi JetReady.|Format file biner.|

### Mengonversi file PCL ke format PDF

Untuk memungkinkan konversi dari PCL ke PDF, [Aspose.PDF for Java](https://products.aspose.com/pdf/java) memiliki kelas [PclLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/PclLoadOptions) yang digunakan untuk menginisialisasi objek [LoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/LoadOptions). Objek ini kemudian diteruskan sebagai argumen selama inisialisasi objek [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document) dan membantu mesin rendering PDF untuk menentukan format input dokumen sumber.

Cuplikan kode berikut menunjukkan proses mengonversi file PCL ke format PDF.

```java
package com.aspose.pdf.examples;

import java.io.FileNotFoundException;
import java.nio.file.Path;
import java.nio.file.Paths;

import com.aspose.pdf.*;

public final class ConvertPCLtoPDF {

    private ConvertPCLtoPDF() {
        
    }

    private static Path _dataDir = Paths.get("/home/admin1/pdf-examples/Samples");

    public static void main(String[] args) throws FileNotFoundException {        
        ConvertPCLtoPDF_Simple();
        ConvertPCLtoPDF_Advanced();
    }

    public static void ConvertPCLtoPDF_Simple() {
        PclLoadOptions options = new PclLoadOptions();
        Document pdfDocument= new Document(_dataDir + "demo.pcl", options);
        pdfDocument.save(_dataDir + "epub_test.pdf");        
    }

    public static void ConvertPCLtoPDF_Advanced() {
        PclLoadOptions options = new PclLoadOptions();
        options.SupressErrors=true;
        Document pdfDocument= new Document(_dataDir + "demo.pcl", options);
        if (options.Exceptions!=null)
            for (Exception ex : options.Exceptions)
            {
                System.out.println(ex.getMessage());
            }
        pdfDocument.save(_dataDir + "pcl_test.pdf");        
    }
}
```

### Masalah yang Diketahui

1. Asal dari string teks dan gambar dapat sedikit berbeda dari yang ada di file PCL sumber jika arah cetak tidak 0º. Hal yang sama berlaku untuk gambar vektor jika sistem koordinat plot vektor diputar (perintah RO didahului).
2. Asal label dalam gambar vektor dapat berbeda dari yang ada di file PCL sumber jika label dipengaruhi oleh serangkaian perintah: Asal Label (LO), Definisikan Jalur Teks Variabel (DV), Arah Absolut (DI) atau Arah Relatif (DR).
3. Teks dapat dibaca dengan tidak benar jika harus dirender dengan font Bitmap atau TrueType soft (tertanam), karena saat ini font ini hanya didukung sebagian (lihat pengecualian di "Tabel fitur yang didukung"). Dalam situasi ini teks dapat dibaca dengan benar hanya jika kode karakter dalam font soft sesuai dengan yang default. Gaya teks yang dibaca juga dapat berbeda dari yang ada di file PCL sumber karena tidak perlu mengatur gaya di header font soft.

1. Jika file PCL yang diurai berisi font Intellifont atau Universal, sebuah pengecualian akan dilemparkan, karena font Intellifont dan Universal sama sekali tidak didukung.
1. Jika file PCL yang diurai berisi perintah makro, hasil penguraian akan sangat berbeda dari file sumber, karena perintah makro tidak didukung.

## Mengkonversi Teks ke PDF

**Aspose.PDF untuk Java** menyediakan kemampuan untuk mengkonversi file Teks ke format PDF. Dalam artikel ini, kami menunjukkan betapa mudah dan efisiennya kami dapat mengkonversi file teks ke PDF menggunakan Aspose.PDF.

Ketika Anda perlu mengkonversi file Teks ke PDF, awalnya baca file teks sumber dalam beberapa pembaca. Kami telah menggunakan StringBuilder untuk membaca konten file Teks. Instansiasi objek Document dan tambahkan halaman baru dalam koleksi Pages. Buat objek baru dari TextFragment dan berikan objek StringBuilder ke konstruktor. Tambahkan paragraf baru dalam koleksi Paragraphs menggunakan objek TextFragment dan simpan file PDF hasil menggunakan metode Save dari kelas Document.


{{% alert color="success" %}}
**Coba konversi TEKS ke PDF secara online**

Aspose.PDF untuk Java menyajikan aplikasi gratis online ["Teks ke PDF"](https://products.aspose.app/pdf/conversion/txt-to-pdf), di mana Anda dapat mencoba menyelidiki fungsi dan kualitasnya bekerja.

[![Aspose.PDF Konversi TEKS ke PDF dengan Aplikasi Gratis](text_to_pdf.png)](https://products.aspose.app/pdf/conversion/txt-to-pdf)
{{% /alert %}}

### Konversi file teks biasa ke PDF

```java
package com.aspose.pdf.examples;
/**
 * Konversi TXT ke PDF
 */

import java.io.IOException;
import java.nio.charset.Charset;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;

import com.aspose.pdf.*;

public final class ConvertTextToPDF {

    private ConvertTextToPDF() {
    }

    final static Path _dataDir = Paths.get("/home/admin1/pdf-examples/Samples");
    final static Charset ENCODING = StandardCharsets.UTF_8;

    public static void main(String[] args) throws IOException {
        ConvertTXT_to_PDF_Simple();
    }

    public static void ConvertTXT_to_PDF_Simple() throws IOException {
        // Inisialisasi objek dokumen

        String pdfDocumentFileName = Paths.get(_dataDir.toString(), "demo_txt.pdf").toString();
        Path txtDocumentFileName = Paths.get(_dataDir.toString(), "rfc822.txt");

        // Memperoleh instansi objek Document dengan memanggil konstruktor kosongnya
        Document pdfDocument = new Document();

        // Menambahkan halaman baru dalam koleksi Pages dari Document
        Page page = pdfDocument.getPages().add();

        // Membuat instansi TextFragment dan mengoper teks dari objek pembaca ke
        // konstruktor sebagai argumen
        TextFragment text = new TextFragment(Files.readString(txtDocumentFileName, ENCODING));

        // Menambahkan paragraf teks baru dalam koleksi paragraf dan mengoper objek
        // TextFragment
        page.getParagraphs().add(text);

        // Menyimpan file PDF hasil
        pdfDocument.save(pdfDocumentFileName);
    }
```


### Mengonversi file teks pra-format ke PDF

```java
    public static void ConvertPreFormattedTextToPdf() throws IOException {

        Path txtDocumentFileName = Paths.get(_dataDir.toString(), "rfc822.txt");
        String pdfDocumentFileName = Paths.get(_dataDir.toString(), "demo_txt.pdf").toString();

        // Baca file teks sebagai array string
        java.util.List<String> lines = Files.readAllLines(txtDocumentFileName, ENCODING);

        // Menginstansiasi objek Document dengan memanggil konstruktor kosongnya
        Document pdfDocument = new Document();

        // Tambahkan halaman baru dalam koleksi Pages dari Document
        Page page = pdfDocument.getPages().add();

        // Atur margin kiri dan kanan untuk presentasi yang lebih baik
        page.getPageInfo().getMargin().setLeft(20);
        page.getPageInfo().getMargin().setRight(10);
        page.getPageInfo().getDefaultTextState().setFont(FontRepository.findFont("Courier New"));
        page.getPageInfo().getDefaultTextState().setFontSize(12);

        for (String line : lines) {
            // periksa apakah baris mengandung karakter "form feed"
            // lihat https://en.wikipedia.org/wiki/Page_break
            if (line.startsWith("\f")) {
                page = pdfDocument.getPages().add();
                page.getPageInfo().getMargin().setLeft(20);
                page.getPageInfo().getMargin().setRight(10);
                page.getPageInfo().getDefaultTextState().setFont(FontRepository.findFont("Courier New"));
                page.getPageInfo().getDefaultTextState().setFontSize(12);
            } else {
                // Buat instance dari TextFragment dan
                // berikan baris ke
                // konstruktor sebagai argumen
                TextFragment text = new TextFragment(line);

                // Tambahkan paragraf teks baru dalam koleksi paragraf dan berikan objek TextFragment
                page.getParagraphs().add(text);
            }

            pdfDocument.save(pdfDocumentFileName);
        }
    }
}
```


## Mengonversi XPS ke PDF

**Aspose.PDF untuk Java** mendukung fitur mengonversi file <abbr title="XML Paper Specification">XPS</abbr> ke format PDF. Periksa artikel ini untuk menyelesaikan tugas Anda.

XPS, XML Paper Specification, adalah format file Microsoft yang digunakan untuk mengintegrasikan pembuatan dan penampilan dokumen ke Windows. Dengan Aspose.PDF untuk Java, dimungkinkan untuk mengonversi file XPS ke PDF, format file portabel dari Adobe.

Format file ini pada dasarnya adalah file XML yang dikompresi, terutama digunakan untuk distribusi dan penyimpanan. Sangat sulit untuk diedit dan sebagian besar diimplementasikan oleh Microsoft.

Untuk mengonversi file XPS ke PDF menggunakan [Aspose.PDF untuk Java](https://products.aspose.com/pdf/java), gunakan kelas [XpsLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/XpsLoadOptions).
 Ini digunakan untuk menginisialisasi objek [LoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/LoadOptions). Kemudian, objek ini diteruskan sebagai argumen selama inisialisasi objek [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document) dan membantu mesin rendering PDF untuk menentukan format input dokumen sumber.

Di XP dan Windows 7, Anda harus menemukan Printer XPS yang sudah terpasang jika Anda melihat di Control Panel dan kemudian Printers. Untuk membuat file XPS, Anda dapat menggunakan printer tersebut sebagai perangkat output. Di Windows 7, Anda seharusnya bisa cukup dengan mengklik dua kali file tersebut untuk membukanya di penampil XPS. Anda juga dapat mengunduh [penampil XPS](http://windows.microsoft.com/en-US/windows-vista/what-is-the-xps-viewer) dari situs web Microsoft.

Cuplikan kode berikut menunjukkan proses konversi file XPS ke format PDF.

```java
public final class ConvertXPStoPDF {

    private ConvertXPStoPDF() {
    }

    final static Path _dataDir = Paths.get("/home/aspose/pdf-examples/Samples");

    public static void main(String[] args) throws IOException {
        Convert_XSLFO_to_PDF();
    }

    public static void Convert_XSLFO_to_PDF() throws IOException {
        // Inisialisasi objek dokumen

        String pdfDocumentFileName = Paths.get(_dataDir.toString(), "demo_txt.pdf").toString();
        String xpsDocumentFileName = Paths.get(_dataDir.toString(), "demo.xml").toString();

        // Instansiasi objek LoadOption menggunakan opsi muat XPS
        LoadOptions options = new XpsLoadOptions();

        // Instansiasi objek Document dengan memanggil konstruktor kosongnya
        Document pdfDocument = new Document(xpsDocumentFileName, options);

        // Simpan file PDF yang dihasilkan
        pdfDocument.save(pdfDocumentFileName);
    }
}
```

{{% alert color="success" %}}
**Coba mengonversi format XPS ke PDF secara online**

Aspose.PDF untuk Java mempersembahkan aplikasi gratis online ["XPS ke PDF"](https://products.aspose.app/pdf/conversion/xps-to-pdf/), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitas kerjanya.

[![Aspose.PDF Konversi XPS ke PDF dengan Aplikasi Gratis](xps_to_pdf.png)](https://products.aspose.app/pdf/conversion/xps-to-pdf/)
{{% /alert %}}

## Mengonversi PostScript ke PDF

**Aspose.PDF untuk Java** mendukung fitur konversi file PostScript ke format PDF. Salah satu fitur dari Aspose.PDF adalah Anda dapat mengatur sekumpulan folder font yang akan digunakan selama konversi.

Untuk mengonversi file PostScript ke format PDF, Aspose.PDF untuk Java menawarkan kelas [PsLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/PsLoadOptions) yang digunakan untuk menginisialisasi objek LoadOptions. Nantinya objek ini dapat diteruskan sebagai argumen ke konstruktor objek Document, yang akan membantu Mesin Rendering PDF untuk menentukan format dokumen sumber.


Berikut cuplikan kode yang dapat digunakan untuk mengonversi file PostScript menjadi format PDF:

```java
public static void ConvertPostScriptToPDF_Simple(){
        // Inisialisasi objek dokumen

        String pdfDocumentFileName = Paths.get(_dataDir.toString(), "demo.pdf").toString();
        String psDocumentFileName = Paths.get(_dataDir.toString(), "demo.ps").toString();
        PsLoadOptions options = new PsLoadOptions();

        // Buat objek Dokumen
        Document document = new Document(psDocumentFileName, options);

        // Simpan output dokumen PDF
        document.save(pdfDocumentFileName);
    }
```

Selain itu, Anda dapat menetapkan serangkaian folder font yang akan digunakan selama konversi:

```java
public static void ConvertPostscriptToPDFAvdanced() {
        String pdfDocumentFileName = Paths.get(_dataDir.toString(), "demo.pdf").toString();
        String psDocumentFileName = Paths.get(_dataDir.toString(), "demo.ps").toString();
        PsLoadOptions options = new PsLoadOptions();
        
        options.setFontsFolders(new String[] { "c:\tmp\fonts1", "c:\tmp\fonts2" });

        // Buat objek Dokumen
        Document document = new Document(psDocumentFileName, options);

        // Simpan output dokumen PDF
        document.save(pdfDocumentFileName);
    }
```


## Konversi XML ke PDF

Format XML digunakan untuk menyimpan data terstruktur. Ada beberapa cara untuk mengonversi <abbr title="Extensible Markup Language">XML</abbr> ke PDF di Aspose.PDF.

{{% alert color="success" %}}
**Cobalah untuk mengonversi XML ke PDF secara online**

Aspose.PDF untuk Java menghadirkan aplikasi gratis online ["XML to PDF"](https://products.aspose.app/pdf/conversion/xml-to-pdf), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitas kerjanya.

[![Aspose.PDF Konversi XML ke PDF dengan Aplikasi Gratis](xml_to_pdf.png)](https://products.aspose.app/pdf/conversion/xml-to-pdf)
{{% /alert %}}

Pertimbangkan opsi menggunakan dokumen XML berdasarkan standar XSL-FO.

### Konversi XSL-FO ke PDF

Konversi file XSL-FO ke PDF dapat diimplementasikan menggunakan objek [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/document) dengan [XslFoLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/xslfoloadoptions).

```java
package com.aspose.pdf.examples;
/**
 * Konversi XML ke PDF
 */

import java.io.IOException;
import java.nio.file.Path;
import java.nio.file.Paths;

import com.aspose.pdf.*;

public final class ConvertXMLtoPDF {

    private ConvertXMLtoPDF() {
    }

    final static Path _dataDir = Paths.get("/home/admin1/pdf-examples/Samples");
    public static void main(String[] args) throws IOException {
        Convert_XSLFO_to_PDF();
        Convert_XSLFO_to_PDF_Adv();
    }

    public static void Convert_XSLFO_to_PDF() throws IOException {
        // Inisialisasi objek dokumen

        String pdfDocumentFileName = Paths.get(_dataDir.toString(), "demo_txt.pdf").toString();
        String xmlDocumentFileName = Paths.get(_dataDir.toString(), "demo.xml").toString();
        String xsltDocumentFileName = Paths.get(_dataDir.toString(), "employees.xslt").toString();

        XslFoLoadOptions options = new XslFoLoadOptions(xsltDocumentFileName);

        // Instansiasi objek Document dengan memanggil konstruktor kosongnya
        Document pdfDocument = new Document(xmlDocumentFileName,options);

        // Simpan file PDF hasil
        pdfDocument.save(pdfDocumentFileName);
    }
}
```


### Mengonversi XSL-FO ke PDF dengan strategi penanganan kesalahan yang ditetapkan

```java
// Inisialisasi objek dokumen

String documentFileName = Paths.get(DATA_DIR.toString(), "demo_txt.pdf").toString();
String xmlDocumentFileName = Paths.get(DATA_DIR.toString(), "demo.xml").toString();
String xsltDocumentFileName = Paths.get(DATA_DIR.toString(), "employees.xslt").toString();

XslFoLoadOptions options = new XslFoLoadOptions(xsltDocumentFileName);

// Tetapkan strategi penanganan kesalahan
options.setParsingErrorsHandlingType(XslFoLoadOptions.ParsingErrorsHandlingTypes.ThrowExceptionImmediately);

// Membuat objek Dokumen dengan memanggil konstruktor kosongnya
Document document = new Document(xmlDocumentFileName, options);

// Simpan file PDF hasil
document.save(documentFileName);
document.close();
```

## Mengonversi LaTeX/TeX ke PDF

Format file LaTeX adalah format file teks dengan markup dalam turunan LaTeX dari keluarga bahasa TeX dan LaTeX adalah format turunan dari sistem TeX.
 LaTeX (ˈleɪtɛk/ lay-tek atau lah-tek) adalah sistem persiapan dokumen dan bahasa markup dokumen. Ini banyak digunakan untuk komunikasi dan publikasi dokumen ilmiah di banyak bidang, termasuk matematika, fisika, dan ilmu komputer. Ini juga memiliki peran penting dalam persiapan dan publikasi buku dan artikel yang mengandung materi multibahasa yang kompleks, seperti Sanskerta dan Arab, termasuk edisi kritis. LaTeX menggunakan program pengaturan huruf TeX untuk memformat keluarannya dan ditulis dalam bahasa makro TeX.

**Aspose.PDF for Java** mendukung fitur untuk mengkonversi file TeX ke format PDF dan untuk memenuhi kebutuhan ini, paket com.aspose.pdf memiliki kelas bernama [LatexLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/LatexLoadOptions) yang menyediakan kemampuan untuk memuat file LaTex dan merender keluaran dalam format PDF menggunakan kelas [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document). Berikut cuplikan kode menunjukkan proses konversi file LaTex ke format PDF.

```java
package com.aspose.pdf.examples;

import java.io.FileNotFoundException;
import java.nio.file.Path;
import java.nio.file.Paths;

import com.aspose.pdf.*;

public final class ConvertLATEXtoPDF {

    private ConvertLATEXtoPDF() {
    }

    private static Path _dataDir = Paths.get("/home/admin1/pdf-examples/Samples");

    public static void main(String[] args) throws FileNotFoundException {
        
        // Membuat objek opsi pemuatan Latex
        TeXLoadOptions options = new TeXLoadOptions();
        
        // Membuat objek Dokumen
        String latexFileName = Paths.get(_dataDir.toString(), "samplefile.tex").toString();
        Document document = new Document(latexFileName, options);

        // Simpan dokumen PDF keluaran
        document.save(Paths.get(_dataDir.toString(),"TEXtoPDF.pdf").toString());
    }
}
```

{{% alert color="success" %}}
**Cobalah mengonversi LaTeX/TeX ke PDF secara online**


Aspose.PDF for Java menghadirkan aplikasi online gratis ["LaTex to PDF"](https://products.aspose.app/pdf/conversion/tex-to-pdf), di mana Anda dapat mencoba mengeksplorasi fungsionalitas dan kualitasnya.
[![Aspose.PDF Konversi LaTeX/TeX ke PDF dengan Aplikasi Gratis](latex.png)](https://products.aspose.app/pdf/conversion/tex-to-pdf)
{{% /alert %}}