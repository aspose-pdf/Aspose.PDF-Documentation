---
title: Mengonversi Format File Lain ke PDF di .NET
linktitle: Mengonversi Format File Lain ke PDF
type: docs
weight: 80
url: /net/convert-other-files-to-pdf/
lastmod: "2021-11-01"
description: Topik ini menunjukkan bagaimana Aspose.PDF memungkinkan untuk mengkonversi format file lain seperti EPUB, MD, PCL, XPS, PS, XML, dan LaTeX menjadi dokumen PDF.
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

## Overview

Artikel ini menjelaskan cara **mengkonversi berbagai jenis format file lain ke PDF menggunakan C#**. Ini mencakup topik berikut.

Potongan kode berikut juga bekerja dengan pustaka [Aspose.PDF.Drawing](/pdf/net/drawing/).

_Format_: **EPUB**
- [C# EPUB ke PDF](#csharp-convert-epub-to-pdf)
- [C# Mengonversi EPUB ke PDF](#csharp-convert-epub-to-pdf)
- [C# Cara mengkonversi file EPUB ke PDF](#csharp-convert-epub-to-pdf)

_Format_: **Markdown**
- [C# Markdown ke PDF](#csharp-convert-markdown-to-pdf)
- [C# Mengonversi Markdown ke PDF](#csharp-convert-markdown-to-pdf)
- [C# Cara mengkonversi file Markdown ke PDF](#csharp-convert-markdown-to-pdf)
- [C# Bagaimana cara mengonversi file Markdown ke PDF](#csharp-convert-markdown-to-pdf)

_Format_: **MD**
- [C# MD ke PDF](#csharp-convert-md-to-pdf)
- [C# Konversi MD ke PDF](#csharp-convert-md-to-pdf)
- [C# Bagaimana cara mengonversi file MD ke PDF](#csharp-convert-md-to-pdf)

_Format_: **PCL**
- [C# PCL ke PDF](#csharp-convert-pcl-to-pdf)
- [C# Konversi PCL ke PDF](#csharp-convert-pcl-to-pdf)
- [C# Bagaimana cara mengonversi file PCL ke PDF](#csharp-convert-pcl-to-pdf)

_Format_: **Text**
- [C# Teks ke PDF](#csharp-convert-text-to-pdf)
- [C# Konversi Teks ke PDF](#csharp-convert-text-to-pdf)
- [C# Bagaimana cara mengonversi file Teks ke PDF](#csharp-convert-text-to-pdf)

_Format_: **TXT**
- [C# TXT ke PDF](#csharp-convert-txt-to-pdf)
- [C# Konversi TXT ke PDF](#csharp-convert-txt-to-pdf)
- [C# Bagaimana cara mengonversi file TXT ke PDF](#csharp-convert-txt-to-pdf)

_Format_: **Plain Text**
- [C# Teks Biasa ke PDF](#csharp-convert-plain-text-to-pdf)
- [C# Konversi Teks Biasa ke PDF](#csharp-convert-plain-text-to-pdf)
- [C# Bagaimana cara mengonversi file Teks Biasa ke PDF](#csharp-convert-plain-text-to-pdf)
- [C# Cara mengonversi file Teks Biasa ke PDF](#csharp-convert-plain-text-to-pdf)

_Format_: **Teks Terformat**
- [C# Teks Terformat ke PDF](#csharp-convert-pre-formatted-txt-to-pdf)
- [C# Mengonversi Teks Terformat ke PDF](#csharp-convert-pre-formatted-txt-to-pdf)
- [C# Cara mengonversi file Teks Terformat ke PDF](#csharp-convert-pre-formatted-txt-to-pdf)

_Format_: **Teks Praformat**
- [C# Teks Praformat ke PDF](#csharp-convert-pre-text-to-pdf)
- [C# Mengonversi Teks Praformat ke PDF](#csharp-convert-pre-text-to-pdf)
- [C# Cara mengonversi file Teks Praformat ke PDF](#csharp-convert-pre-text-to-pdf)

_Format_: **XPS**
- [C# XPS ke PDF](#csharp-convert-xps-to-pdf)
- [C# Mengonversi XPS ke PDF](#csharp-convert-xps-to-pdf)
- [C# Cara mengonversi file XPS ke PDF](#csharp-convert-xps-to-pdf)

## Mengonversi EPUB ke PDF

**Aspose.PDF for .NET** memungkinkan Anda untuk dengan mudah mengonversi file EPUB ke format PDF.

<abbr title="publikasi elektronik">EPUB</abbr> (singkatan dari publikasi elektronik) adalah standar e-book gratis dan terbuka dari International Digital Publishing Forum (IDPF).
<abbr title="publikasi elektronik">EPUB</abbr> (singkatan dari publikasi elektronik) adalah standar buku elektronik gratis dan terbuka dari International Digital Publishing Forum (IDPF).

EPUB juga mendukung konten dengan tata letak tetap. Format ini dimaksudkan sebagai satu format yang dapat digunakan oleh penerbit dan rumah konversi baik secara internal maupun untuk distribusi dan penjualan. Ini menggantikan standar Open eBook. Versi EPUB 3 juga didukung oleh Book Industry Study Group (BISG), sebuah asosiasi perdagangan buku terkemuka untuk praktik terbaik yang distandarisasi, penelitian, informasi, dan acara, untuk pengemasan konten.

{{% alert color="success" %}}
**Coba konversi EPUB ke PDF secara online**

Aspose.PDF untuk .NET menyajikan aplikasi gratis online ["EPUB ke PDF"](https://products.aspose.app/pdf/conversion/epub-to-pdf), di mana Anda dapat mencoba untuk menyelidiki fungsionalitas dan kualitas kerjanya.

[![Konversi Aspose.PDF EPUB ke PDF dengan Aplikasi Gratis](epub.png)](https://products.aspose.app/pdf/conversion/epub-to-pdf)
{{% /alert %}}

<a name="csharp-convert-epub-to-pdf" id="csharp-convert-epub-to-pdf"><strong><em>Langkah-langkah:</em> Konversi EPUB ke PDF dalam C#</strong></a>
<a name="csharp-convert-epub-to-pdf" id="csharp-convert-epub-to-pdf"><strong><em>Langkah-langkah:</em> Mengonversi EPUB ke PDF di C#</strong></a>

1. Buat sebuah instansi dari kelas [EpubLoadOptions](https://reference.aspose.com/pdf/net/aspose.pdf/epubloadoptions).
2. Buat sebuah instansi dari kelas [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) dengan menyebutkan nama file sumber dan opsi.
3. Simpan dokumen dengan nama file yang diinginkan.

Kode berikut menunjukkan cara mengonversi file EPUB ke format PDF dengan C#.

```csharp
public static void ConvertEPUBtoPDF()
{
    EpubLoadOptions option = new EpubLoadOptions();
    Document pdfDocument= new Document(_dataDir + "WebAssembly.epub", option);
    pdfDocument.Save(_dataDir + "epub_test.pdf");
}
```

Anda juga dapat mengatur ukuran halaman untuk konversi. Untuk menentukan ukuran halaman baru, gunakan objek `SizeF` dan lewatkan ke konstruktor [EpubLoadOptions](https://reference.aspose.com/pdf/net/aspose.pdf/epubloadoptions/constructors/main).

```csharp
public static void ConvertEPUBtoPDFAdv()
{
    EpubLoadOptions option = new EpubLoadOptions(new SizeF(1190, 1684));
    Document pdfDocument= new Document(_dataDir + "WebAssembly.epub", option);
    pdfDocument.Save(_dataDir + "epub_test.pdf");
}
```
## Mengonversi Markdown ke PDF

**Fitur ini didukung oleh versi 19.6 atau lebih tinggi.**

{{% alert color="success" %}}
**Coba konversi Markdown ke PDF secara online**

Aspose.PDF untuk .NET mempersembahkan aplikasi gratis online ["Markdown ke PDF"](https://products.aspose.app/pdf/conversion/md-to-pdf), di mana Anda dapat mencoba untuk meneliti fungsionalitas dan kualitas kerjanya.

[![Konversi Aspose.PDF Markdown ke PDF dengan Aplikasi Gratis](markdown.png)](https://products.aspose.app/pdf/conversion/md-to-pdf)
{{% /alert %}}

Aspose.PDF untuk .NET menyediakan fungsionalitas untuk membuat dokumen PDF berdasarkan file data [Markdown](https://daringfireball.net/projects/markdown/syntax) masukan. Untuk mengonversi Markdown ke PDF, Anda perlu menginisialisasi [Dokumen](https://reference.aspose.com/pdf/net/aspose.pdf/document) menggunakan [MdLoadOptions](https://reference.aspose.com/pdf/net/aspose.pdf/mdloadoptions).

Potongan kode berikut menunjukkan cara menggunakan fungsionalitas ini dengan pustaka Aspose.PDF:

<a name="csharp-convert-markdown-to-pdf" id="csharp-convert-markdown-to-pdf"><strong><em>Langkah:</em> Mengonversi Markdown ke PDF dalam C#</strong></a> |
<a name="csharp-convert-markdown-to-pdf" id="csharp-convert-markdown-to-pdf"><strong><em>Langkah-langkah:</em> Mengonversi Markdown ke PDF dalam C#</strong></a> |
<a name="csharp-convert-md-to-pdf" id="csharp-convert-md-to-pdf"><strong><em>Langkah-langkah:</em> Mengonversi MD ke PDF dalam C#</strong></a>

1. Buat instance dari kelas [MdLoadOptions](https://reference.aspose.com/pdf/net/aspose.pdf/mdloadoptions/).
2. Buat instance dari kelas [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) dengan menyebutkan nama file sumber dan opsi.
3. Simpan dokumen dengan nama file yang diinginkan.

```csharp
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();
// Buka dokumen Markdown
Document pdfDocument= new Document(dataDir + "sample.md", new MdLoadOptions());
// Simpan dokumen dalam format PDF
pdfDocument.Save(dataDir + "MarkdownToPDF.pdf");
```

## Konversi PCL ke PDF

<abbr title="Printer Command Language">PCL</abbr> (Printer Command Language) adalah bahasa printer yang dikembangkan oleh Hewlett-Packard untuk mengakses fitur printer standar.
<abbr title="Printer Command Language">PCL</abbr> (Printer Command Language) adalah bahasa printer yang dikembangkan oleh Hewlett-Packard untuk mengakses fitur printer standar.

{{% alert color="success" %}}
**Coba konversi PCL ke PDF secara online**

Aspose.PDF untuk .NET menyajikan aplikasi gratis online ["PCL to PDF"](https://products.aspose.app/pdf/conversion/pcl-to-pdf), di mana Anda dapat mencoba mengeksplorasi fungsionalitas dan kualitas kerjanya.

[![Aspose.PDF Konversi PCL ke PDF dengan Aplikasi Gratis](pcl_to_pdf.png)](https://products.aspose.app/pdf/conversion/pcl-to-pdf)
{{% /alert %}}

**Saat ini hanya mendukung PCL5 dan versi yang lebih lama**

<table>
    <thead>
        <tr>
            <th>
                Sets of Commands
            </th>
            <th>
                Support
            </th>
            <th>
                Exceptions
            </th>
            <th>
                Description
            </th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>
                Perintah kontrol pekerjaan

        <tr>
            <td>
                Perintah kontrol pekerjaan
            </td>
            <td>
                +
            </td>
            <td>
                Mode pencetakan dua sisi
            </td>
            <td>
                Kontrol proses pencetakan: jumlah salinan, tempat keluaran, pencetakan satu/dua sisi, offset kiri dan atas dll.
            </td>
        </tr>
        <tr>
            <td>
                Perintah kontrol halaman
            </td>
            <td>
                +
            </td>
            <td>
                Perintah Melompati Perforasi
            </td>
            <td>
                Tentukan ukuran halaman, margin, orientasi halaman, jarak antar-baris, antar-karakter dll.
            </td>
        </tr>
        <tr>
            <td>
                Perintah Posisi Kursor
            </td>
            <td>
                +
            </td>
            <td>
                &nbsp;
            </td>
            <td>
                Tentukan posisi kursor dan, oleh karena itu, asal-usul teks, gambar raster atau vektor, dan detailnya.
            </td>
        </tr>
```

Tentukan posisi kursor dan, oleh karena itu, asal-usul teks, gambar raster atau vektor, dan detailnya.
</td>
</tr>
<tr>
<td>
Perintah pemilihan font
</td>
<td>
+
</td>
<td>
<ol>
<li>Perintah Data Cetak Transparan.</li>
<li>Font lunak tertanam. Dalam versi saat ini, alih-alih membuat font lunak, perpustakaan kami memilih
font "keras" TrueType yang cocok dari font TrueType yang ada yang terinstal di mesin target. <br/>
Kesesuaian didefinisikan oleh rasio lebar/tinggi.<br/>
Fitur ini hanya berfungsi untuk font Bitmap dan TrueType dan tidak
menjamin bahwa teks yang dicetak dengan font lunak akan relevan dengan yang ada di file sumber.<br/>
Karena kode karakter dalam font lunak bisa tidak sesuai dengan yang default.
</li>
<li>Set Simbol yang Ditetapkan Pengguna.</li>
```

<li>Set Simbol yang Ditentukan Pengguna.</li>
</ol>
</td>
<td>
Izinkan memuat font lunak (tertanam) dari file PCL dan mengelolanya di memori.
</td>
</tr>
<tr>
<td>
Perintah grafik raster
</td>
<td>
+
</td>
<td>
Hanya hitam & putih
</td>
<td>
Izinkan memuat gambar raster dari file PCL ke memori, tentukan parameter raster. <br
> seperti lebar, tinggi, tipe kompresi, resolusi, dll.
</td>
</tr>
<tr>
<td>
Perintah warna
</td>
<td>
+
</td>
<td>
&nbsp;
</td>
<td>
Izinkan pewarnaan untuk semua objek yang dapat dicetak.
</td>
</tr>
<tr>
<td>
Perintah Model Cetak
```

Perintah Model Cetak
                +
                
                Mengizinkan pengisian teks, gambar raster, dan area persegi panjang dengan pola raster yang telah ditentukan dan pola yang ditentukan pengguna menentukan mode transparansi untuk pola dan gambar raster sumber. Pola yang telah ditentukan adalah garis berpetak, garis silang, dan pola bayangan.

Perintah Pengisian Area Persegi Panjang
                +
                
                Mengizinkan pembuatan dan pengisian area persegi panjang dengan pola.

Perintah Grafis Vektor HP-GL/2
                +
                Perintah Vektor Berlayar (SV), Perintah Mode Transparansi (TR), Perintah Data Transparan (TD), RO
Perintah Screened Vector (SV), Mode Transparansi (TR), Data Transparan (TD), RO (Rotasi Sistem Koordinat), Font Skalabel atau Bitmap (SB), Miring Karakter (SL) dan Ruang Ekstra (ES) tidak diimplementasikan dan perintah DV (Definisi Jalur Teks Variabel) direalisasikan dalam versi beta.

Izinkan memuat gambar vektor HP-GL/2 dari file PCL ke dalam memori. Gambar vektor memiliki titik asal di sudut kiri bawah area yang dapat dicetak, dapat diskalakan, diterjemahkan, diputar, dan dipotong. <br>
Gambar vektor dapat berisi teks, sebagai label, dan figur geometris seperti persegi panjang, lingkaran, elips, garis, busur, kurva bezier dan figur kompleks yang terdiri dari yang sederhana. <br> Figur tertutup termasuk huruf dari label dapat diisi dengan pengisian padat atau pola vektor. <br> Pola dapat berupa garis silang, garis silang PCL, naungan, raster yang ditentukan pengguna, garis silang PCL atau garis silang PCL.

hatching, cross-hatch, shading, raster user-defined, PCL hatching atau cross-hatch dan PCL
user-defined. Pola PCL adalah raster. Label dapat diputar, diskalakan, dan diarahkan secara individu dalam
empat arah: atas, bawah, kiri, dan kanan. Arah Kiri dan Kanan melibatkan penyusunan huruf satu demi satu.
Arah Atas dan Bawah melibatkan penyusunan huruf satu di bawah yang lain.
```


Macroses
―
&nbsp;
Memungkinkan memuat urutan perintah PCL ke dalam memori dan menggunakan urutan ini berkali-kali, misalnya,
untuk mencetak header halaman atau mengatur satu format untuk sekumpulan halaman.
```


Unicode text
―
```

### Mengonversi file PCL ke format PDF

Untuk mengizinkan konversi dari PCL ke PDF, Aspose.PDF memiliki kelas [`PclLoadOptions`](https://reference.aspose.com/pdf/net/aspose.pdf/pclloadoptions) yang digunakan untuk menginisialisasi objek LoadOptions.
```
Untuk mengizinkan konversi dari PCL ke PDF, Aspose.PDF memiliki kelas [`PclLoadOptions`](https://reference.aspose.com/pdf/net/aspose.pdf/pclloadoptions) yang digunakan untuk menginisialisasi objek LoadOptions.

Potongan kode berikut menunjukkan proses mengonversi file PCL menjadi format PDF.

<a name="csharp-convert-pcl-to-pdf" id="csharp-convert-pcl-to-pdf"><strong><em>Langkah:</em> Mengonversi PCL ke PDF dalam C#</strong></a>

1. Buat sebuah instansi dari kelas [PclLoadOptions](https://reference.aspose.com/pdf/net/aspose.pdf/pclloadoptions/).
2. Buat sebuah instansi dari kelas [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document/) dengan menyebutkan nama file sumber dan opsi.
3. Simpan dokumen dengan nama file yang diinginkan.

```csharp
public static void ConvertPCLtoPDF()
{
    PclLoadOptions options = new PclLoadOptions();
    Document pdfDocument= new Document(_dataDir + "demo.pcl", options);
    pdfDocument.Save(_dataDir + "pcl_test.pdf");
}
```

Anda juga dapat memantau deteksi kesalahan selama proses konversi.
Anda juga dapat memantau deteksi kesalahan selama proses konversi.

```csharp
public static void ConvertPCLtoPDFAvdanced()
{
    PclLoadOptions options = new PclLoadOptions { SupressErrors = true };
    Document pdfDocument= new Document(_dataDir + "demo.pcl", options);
    if (options.Exceptions!=null)
        foreach (var ex in options.Exceptions)
        {
            Console.WriteLine(ex.Message);
        }
    pdfDocument.Save(_dataDir + "pcl_test.pdf");
}
```

### Masalah yang Diketahui

1. Asal teks dan gambar dapat sedikit berbeda dari yang ada di file PCL sumber jika arah cetak bukan 0°. Hal yang sama berlaku untuk gambar vektor jika sistem koordinat plot vektor diputar (perintah RO mendahului).
1. Asal label pada gambar vektor dapat berbeda dari yang ada di file PCL sumber jika label dipengaruhi oleh urutan perintah: Asal Label (LO), Tentukan Jalur Teks Variabel (DV), Arah Mutlak (DI) atau Arah Relatif (DR).
1. Jika file PCL yang diparsing mengandung Intellifont atau Universal soft fonts, akan muncul pengecualian, karena Intellifont dan Universal font sama sekali tidak didukung.
1. Jika file PCL yang diparsing mengandung perintah makro, hasil parsing akan sangat berbeda dari file sumber, karena perintah makro tidak didukung.

## Mengonversi Teks ke PDF

**Aspose.PDF for .NET** mendukung fitur mengonversi file teks biasa dan teks yang telah diformat ke format PDF.

Mengonversi teks ke PDF berarti menambahkan fragmen teks ke halaman PDF. Untuk file teks, kita berurusan dengan 2 jenis teks: pra-pemformatan (misalnya, 25 baris dengan 80 karakter per baris) dan teks tidak terformat (teks biasa). Tergantung pada kebutuhan kita, kita dapat mengontrol penambahan ini sendiri atau mempercayakannya pada algoritma perpustakaan.

{{% alert color="success" %}}
**Coba konversi TEKS ke PDF secara online**

Aspose.PDF for .NET mempersembahkan aplikasi gratis online ["Text to PDF"](https://products.aspose.app/pdf/conversion/txt-to-pdf), di mana Anda dapat mencoba untuk menyelidiki fungsionalitas dan kualitas kerjanya.
Aspose.PDF untuk .NET memperkenalkan aplikasi gratis online ["Text to PDF"](https://products.aspose.app/pdf/conversion/txt-to-pdf) yang memungkinkan Anda untuk mengeksplorasi fungsi dan kualitas kerjanya.

[![Konversi Aspose.PDF TEKS ke PDF dengan Aplikasi Gratis](text_to_pdf.png)](https://products.aspose.app/pdf/conversion/txt-to-pdf)

### Mengonversi file teks biasa ke PDF

Dalam kasus file teks biasa, kita dapat menggunakan teknik berikut:

<a name="csharp-convert-text-to-pdf" id="csharp-convert-text-to-pdf"><strong><em>Langkah:</em> Mengonversi Teks ke PDF dalam C#</strong></a> |
<a name="csharp-convert-txt-to-pdf" id="csharp-convert-txt-to-pdf"><strong><em>Langkah:</em> Mengonversi TXT ke PDF dalam C#</strong></a> |
<a name="csharp-convert-plain-text-to-pdf" id="csharp-convert-plain-text-to-pdf"><strong><em>Langkah:</em> Mengonversi Teks Biasa ke PDF dalam C#</strong></a>

1. Gunakan _TextReader_ untuk membaca seluruh teks;
2.
2.
3. Buat objek baru dari [TextFragment](https://reference.aspose.com/pdf/net/aspose.pdf.text/textfragment/) dan berikan objek _TextReader_ kepada konstruktornya;
4. Tambahkan objek _TextFragment_ sebagai paragraf dalam koleksi _Paragraphs_. Jika jumlah teks lebih besar dari halaman, algoritma perpustakaan secara otomatis menambahkan halaman tambahan;
5. Gunakan metode **Save** dari kelas [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document/);

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();
// Baca file teks sumber
TextReader tr = new StreamReader(dataDir + "log.txt");

// Instansiasi objek Dokumen dengan memanggil konstruktor kosongnya
Document pdfDocument= new Document();

// Tambahkan halaman baru dalam koleksi Halaman dari Dokumen
Page page = pdfDocument.Pages.Add();

// Buat instansi TextFragmet dan berikan teks dari objek pembaca ke konstruktornya sebagai argumen
TextFragment text = new TextFragment(tr.ReadToEnd());

// Tambahkan paragraf teks baru dalam koleksi paragraf dan berikan objek TextFragment
page.Paragraphs.Add(text);

// Simpan file PDF hasil
pdfDocument.Save(dataDir + "TexttoPDF_out.pdf");
```
### Mengonversi file teks yang sudah diformat menjadi PDF

Mengonversi teks yang sudah diformat mirip dengan teks biasa tetapi Anda perlu melakukan beberapa tindakan tambahan seperti mengatur margin, jenis font, dan ukuran font. Jelas bahwa font harus monospace (misalnya Courier New).

Ikuti langkah-langkah ini untuk mengonversi teks yang sudah diformat menjadi PDF dengan C#:

<a name="csharp-convert-pre-text-to-pdf" id="csharp-convert-pre-text-to-pdf"><strong><em>Langkah:</em> Mengonversi Teks Pra ke PDF di C#</strong></a> |
<a name="csharp-convert-pre-formatted-txt-to-pdf" id="csharp-convert-pre-formatted-txt-to-pdf"><strong><em>Langkah:</em> Mengonversi TXT yang Sudah Diformat menjadi PDF di C#</strong></a>

1. Baca seluruh teks sebagai array string;
2. Instansiasi objek [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document/) dan tambahkan halaman baru dalam koleksi [Pages](https://reference.aspose.com/pdf/net/aspose.pdf/document/pages/);
Dalam hal ini, algoritma perpustakaan juga menambahkan halaman ekstra, tetapi kita dapat mengontrol proses ini sendiri. Contoh berikut menunjukkan cara mengonversi file teks yang telah diformat sebelumnya (80x25) menjadi dokumen PDF dengan ukuran halaman A4.

```csharp
public static void ConvertPreFormattedTextToPdf()
{
    // Membaca file teks sebagai array string
    var lines = System.IO.File.ReadAllLines(_dataDir + "rfc822.txt");

    // Menginstansiasi objek Document dengan memanggil konstruktornya yang kosong
    Document pdfDocument= new Document();

    // Menambahkan halaman baru dalam koleksi Halaman dari Dokumen
    Page page = pdfDocument.Pages.Add();

    // Mengatur margin kiri dan kanan untuk presentasi yang lebih baik
    page.PageInfo.Margin.Left = 20;
    page.PageInfo.Margin.Right = 10;
    page.PageInfo.DefaultTextState.Font = FontRepository.FindFont("Courier New");
    page.PageInfo.DefaultTextState.FontSize = 12;

    foreach (var line in lines)
    {
        // memeriksa apakah baris mengandung karakter "form feed"
        // lihat https://en.wikipedia.org/wiki/Page_break
        if (line.StartsWith("\x0c"))
        {
            page = pdfDocument.Pages.Add();
            page.PageInfo.Margin.Left = 20;
            page.PageInfo.Margin.Right = 10;
            page.PageInfo.DefaultTextState.Font = FontRepository.FindFont("Courier New");
            page.PageInfo.DefaultTextState.FontSize = 12;
        }
        else
        {
            // Membuat instansi dari TextFragment dan
            // memberikan baris ke
            // konstruktornya sebagai argumen
            TextFragment text = new TextFragment(line);

            // Menambahkan paragraf teks baru dalam koleksi paragraf dan memberikan objek TextFragment
            page.Paragraphs.Add(text);
        }
    }

    // Menyimpan file PDF hasil
    pdfDocument.Save(_dataDir + "TexttoPDF_out.pdf");
}
```
## Mengonversi XPS ke PDF

**Aspose.PDF for .NET** mendukung fitur mengonversi file <abbr title="XML Paper Specification">XPS</abbr> ke format PDF. Periksa artikel ini untuk menyelesaikan tugas Anda.

Tipe file XPS terutama dikaitkan dengan Spesifikasi Kertas XML oleh Microsoft Corporation. Spesifikasi Kertas XML (XPS), sebelumnya dikenal dengan nama kode Metro dan mencakup konsep pemasaran Jalur Cetak Generasi Berikutnya (NGPP), adalah inisiatif Microsoft untuk mengintegrasikan pembuatan dan penayangan dokumen ke dalam sistem operasi Windows.

{{% alert color="primary" %}}

Format file pada dasarnya adalah file XML yang dikompres yang terutama digunakan untuk distribusi dan penyimpanan. Sangat sulit untuk diedit dan sebagian besar diimplementasikan oleh Microsoft.

{{% /alert %}}

Untuk mengonversi XPS ke PDF dengan Aspose.PDF for .NET, kami telah memperkenalkan sebuah kelas bernama [XpsLoadOption](https://reference.aspose.com/pdf/net/aspose.pdf/xpsloadoptions) yang digunakan untuk menginisialisasi objek [LoadOptions](https://reference.aspose.com/pdf/net/aspose.pdf/loadoptions).
Untuk mengonversi XPS ke PDF dengan Aspose.PDF untuk .NET, kami telah memperkenalkan sebuah kelas bernama [XpsLoadOption](https://reference.aspose.com/pdf/net/aspose.pdf/xpsloadoptions) yang digunakan untuk menginisialisasi objek [LoadOptions](https://reference.aspose.com/pdf/net/aspose.pdf/loadoptions).

{{% alert color="primary" %}}

Baik di XP maupun Windows 7, Anda seharusnya menemukan Printer XPS yang telah terpasang jika Anda melihat di Control Panel lalu Printers. Untuk membuat file-file ini Anda dapat menggunakan printer tersebut sebagai perangkat output. Di Windows 7, Anda seharusnya dapat hanya mengklik dua kali file tersebut untuk membukanya di penampil XPS. Anda juga dapat mengunduh penampil XPS dari situs web Microsoft.

{{% /alert %}}

Potongan kode berikut menunjukkan proses mengonversi file XPS menjadi format PDF dengan C#.

<a name="csharp-convert-xps-to-pdf" id="csharp-convert-xps-to-pdf"><strong><em>Langkah:</em> Konversi XPS ke PDF dalam C#</strong></a>

1. Buat sebuah instansi dari kelas [XpsLoadOptions](https://reference.aspose.com/pdf/net/aspose.pdf/xpsloadoptions/).
2.
2.
3. Simpan dokumen dalam format PDF dengan nama file yang diinginkan.

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

// Instansiasi objek LoadOption menggunakan opsi muat XPS
Aspose.Pdf.LoadOptions options = new XpsLoadOptions();

// Buat objek dokumen
Aspose.Pdf.Document pdfDocument = new Aspose.Pdf.Document(dataDir + "XPSToPDF.xps", options);

// Simpan dokumen PDF hasil
document.Save(dataDir + "XPSToPDF_out.pdf");
```

{{% alert color="success" %}}
**Coba konversi format XPS ke PDF secara online**

Aspose.PDF for .NET mempersembahkan aplikasi gratis online ["XPS to PDF"](https://products.aspose.app/pdf/conversion/xps-to-pdf/), di mana Anda dapat mencoba untuk menyelidiki fungsionalitas dan kualitas kerjanya.

[![Aspose.PDF Convertion XPS to PDF with Free App](xps_to_pdf.png)](https://products.aspose.app/pdf/conversion/xps-to-pdf/)
{{% /alert %}}
{{% /alert %}}

## Mengonversi PostScript ke PDF

**Aspose.PDF for .NET** mendukung fitur mengonversi file PostScript ke format PDF. Salah satu fitur dari Aspose.PDF adalah Anda dapat mengatur serangkaian folder font yang akan digunakan selama konversi.

Untuk mengonversi file PostScript ke format PDF, Aspose.PDF for .NET menawarkan kelas [PsLoadOptions](https://reference.aspose.com/pdf/net/aspose.pdf/psloadoptions) yang digunakan untuk menginisialisasi objek LoadOptions. Nantinya objek ini dapat dioper sebagai argumen ke konstruktor objek Document, yang akan membantu PDF Rendering Engine untuk menentukan format dokumen sumber.

Potongan kode berikut dapat digunakan untuk mengonversi file PostScript menjadi format PDF dengan Aspose.PDF for .NET:

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string _dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();
// Buat instance baru dari PsLoadOptions
PsLoadOptions options = new PsLoadOptions();
// Buka dokumen .ps dengan opsi muat yang dibuat
Document pdfDocument = new Document(_dataDir + "input.ps", options);
// Simpan dokumen
pdfDocument.Save(dataDir + "PSToPDF.pdf");
```
Selain itu, Anda dapat mengatur serangkaian folder font yang akan digunakan selama konversi:

```csharp
public static void ConvertPostscriptToPDFAvdanced()
{
    PsLoadOptions options = new PsLoadOptions
    {
        FontsFolders = new [] { @"c:\tmp\fonts1", @"c:\tmp\fonts2"}
    };
    Document pdfDocument = new Document(_dataDir + "input.ps", options);
    pdfDocument.Save(_dataDir + "ps_test.pdf");
}
```

## Konversi XML ke PDF

Format XML digunakan untuk menyimpan data terstruktur. Ada beberapa cara untuk mengonversi XML ke PDF di Aspose.PDF:

1. Transformasikan data XML ke HTML menggunakan XSLT dan konversikan HTML ke PDF seperti dijelaskan di bawah ini
1. Hasilkan dokumen XML menggunakan Skema XSD Aspose.PDF
1. Gunakan dokumen XML berdasarkan standar XSL-FO

{{% alert color="success" %}}
**Coba konversi XML ke PDF secara online**

Aspose.PDF untuk .NET menyajikan aplikasi gratis secara online ["XML to PDF"](https://products.aspose.app/pdf/conversion/xml-to-pdf), di mana Anda dapat mencoba untuk meneliti fungsionalitas dan kualitas kerjanya.

Aspose.PDF for .NET mempersembahkan aplikasi gratis online ["XML to PDF"](https://products.aspose.app/pdf/conversion/xml-to-pdf), di mana Anda dapat mencoba menginvestigasi fungsionalitas dan kualitas kerjanya.

[![Aspose.PDF Konversi XML ke PDF dengan Aplikasi Gratis](xml_to_pdf.png)](https://products.aspose.app/pdf/conversion/xml-to-pdf)
{{% /alert %}}


## Konversi XSL-FO ke PDF

Konversi file XSL-FO ke PDF dapat diimplementasikan menggunakan teknik Aspose.PDF tradisional - menginstansiasi objek [Document](https://reference.aspose.com/page/net/aspose.page/document) dengan [XslFoLoadOptions](https://reference.aspose.com/pdf/net/aspose.pdf/xslfoloadoptions). Namun terkadang Anda mungkin menemukan struktur file yang tidak benar. Untuk kasus ini, konverter XSL-FO memungkinkan pengaturan strategi penanganan kesalahan. Anda dapat memilih `ThrowExceptionImmediately`, `TryIgnore` atau `InvokeCustomHandler`.

```csharp
public static void Convert_XSLFO_to_PDF()
{
    // Instansiasi objek XslFoLoadOption
    var options = new XslFoLoadOptions(".\\samples\\employees.xslt");
    // Atur strategi penanganan kesalahan
    options.ParsingErrorsHandlingType = XslFoLoadOptions.ParsingErrorsHandlingTypes.ThrowExceptionImmediately;
    // Buat objek Document
    var pdfDocument = new Aspose.Pdf.Document(".\\samples\\employees.xml", options);
    pdfDocument.Save(_dataDir + "data_xml.pdf");
}
```
## Mengonversi LaTeX/TeX ke PDF

Format file LaTeX adalah format file teks dengan markup dalam turunan LaTeX dari keluarga bahasa TeX dan LaTeX merupakan format turunan dari sistem TeX. LaTeX (ˈleɪtɛk/lay-tek atau lah-tek) adalah sistem persiapan dokumen dan bahasa markup dokumen. Ini banyak digunakan untuk komunikasi dan publikasi dokumen ilmiah di banyak bidang, termasuk matematika, fisika, dan ilmu komputer. Ini juga memiliki peran penting dalam persiapan dan publikasi buku dan artikel yang mengandung materi multibahasa yang kompleks, seperti Sanskerta dan Arab, termasuk edisi kritis. LaTeX menggunakan program penataan teks TeX untuk memformat outputnya, dan ditulis dalam bahasa makro TeX.

{{% alert color="success" %}}
**Coba konversi LaTeX/TeX ke PDF secara online**

Aspose.PDF untuk .NET menyajikan aplikasi gratis online ["LaTex ke PDF"](https://products.aspose.app/pdf/conversion/tex-to-pdf), di mana Anda dapat mencoba untuk menyelidiki fungsionalitas dan kualitas kerjanya.

[![Aspose.PDF Konversi LaTeX/TeX ke PDF dengan Aplikasi Gratis](latex.png)](https://products.aspose.app/pdf/conversion/tex-to-pdf)
Aspose.PDF untuk .NET mendukung fitur untuk mengonversi file TeX ke format PDF dan untuk mencapai kebutuhan ini, ruang nama Aspose.Pdf memiliki kelas bernama [LatexLoadOptions](https://reference.aspose.com/pdf/net/aspose.pdf/latexloadoptions) yang menyediakan kemampuan untuk memuat file LaTex dan merender output dalam format PDF menggunakan [Kelas Dokumen](https://reference.aspose.com/pdf/net/aspose.pdf/document).
Potongan kode berikut menunjukkan proses mengonversi file LaTex ke format PDF dengan C#.

```csharp
public static void ConvertTeXtoPDF()
{
    // Instansiasi objek opsi muat Latex
    TeXLoadOptions options = new TeXLoadOptions();
    // Buat objek Dokumen
    Aspose.Pdf.Document pdfDocument= new Aspose.Pdf.Document(_dataDir + "samplefile.tex", options);
    // Simpan output dalam file PDF
    pdfDocument.Save(_dataDir + "TeXToPDF_out.pdf");
}
```
