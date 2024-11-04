---
title: Mengonversi Berbagai Format Gambar ke PDF di .NET
linktitle: Mengonversi Gambar ke PDF
type: docs
weight: 60
url: /net/convert-images-format-to-pdf/
lastmod: "2021-11-01"
description: Mengonversi berbagai format gambar seperti BMP, CGM, JPEG, DICOM, PNG, TIFF, EMF, dan SVG menjadi PDF menggunakan C# .NET.
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

## Overview

Artikel ini menjelaskan cara mengonversi berbagai format gambar menjadi PDF menggunakan C#. Artikel ini mencakup topik-topik berikut.

Potongan kode berikut juga bekerja dengan perpustakaan [Aspose.PDF.Drawing](/pdf/net/drawing/).

_Format_: **BMP**
- [C# BMP ke PDF](#csharp-bmp-to-pdf)
- [C# Mengonversi BMP ke PDF](#csharp-bmp-to-pdf)
- [C# Cara mengonversi gambar BMP ke PDF](#csharp-bmp-to-pdf)

_Format_: **CGM**
- [C# CGM ke PDF](#csharp-cgm-to-pdf)
- [C# Mengonversi CGM ke PDF](#csharp-cgm-to-pdf)
- [C# Cara mengonversi gambar CGM ke PDF](#csharp-cgm-to-pdf)

_Format_: **DICOM**
- [C# DICOM ke PDF](#csharp-dicom-to-pdf)
- [C# Mengonversi DICOM ke PDF](#csharp-dicom-to-pdf)
- [C# Cara mengonversi gambar DICOM ke PDF](#csharp-dicom-to-pdf)
- [C# Cara mengonversi gambar DICOM ke PDF](#csharp-dicom-to-pdf)

_Format_: **EMF**
- [C# EMF ke PDF](#csharp-emf-to-pdf)
- [C# Konversi EMF ke PDF](#csharp-emf-to-pdf)
- [C# Cara mengonversi gambar EMF ke PDF](#csharp-emf-to-pdf)

_Format_: **GIF**
- [C# GIF ke PDF](#csharp-gif-to-pdf)
- [C# Konversi GIF ke PDF](#csharp-gif-to-pdf)
- [C# Cara mengonversi gambar GIF ke PDF](#csharp-gif-to-pdf)

_Format_: **JPG**
- [C# JPG ke PDF](#csharp-jpg-to-pdf)
- [C# Konversi JPG ke PDF](#csharp-jpg-to-pdf)
- [C# Cara mengonversi gambar JPG ke PDF](#csharp-jpg-to-pdf)

_Format_: **PNG**
- [C# PNG ke PDF](#csharp-png-to-pdf)
- [C# Konversi PNG ke PDF](#csharp-png-to-pdf)
- [C# Cara mengonversi gambar PNG ke PDF](#csharp-png-to-pdf)

_Format_: **SVG**
- [C# SVG ke PDF](#csharp-svg-to-pdf)
- [C# Konversi SVG ke PDF](#csharp-svg-to-pdf)
- [C# Cara mengonversi gambar SVG ke PDF](#csharp-svg-to-pdf)

_Format_: **TIFF**
- [C# TIFF ke PDF](#csharp-tiff-to-pdf)
- [C# Konversi TIFF ke PDF](#csharp-tiff-to-pdf)
- [C# Cara mengonversi gambar TIFF ke PDF](#csharp-tiff-to-pdf)
- [C# Bagaimana mengubah gambar TIFF menjadi PDF](#csharp-tiff-to-pdf)

Topik lain yang dibahas oleh artikel ini
- [Lihat Juga](#see-also)


## Konversi Gambar C# ke PDF

**Aspose.PDF for .NET** memungkinkan Anda mengonversi berbagai format gambar menjadi file PDF. Perpustakaan kami menunjukkan potongan kode untuk mengonversi format gambar yang paling populer, seperti - BMP, CGM, DICOM, EMF, JPG, PNG, SVG, dan format TIFF.

## Mengubah BMP menjadi PDF

Mengonversi file BMP menjadi dokumen PDF menggunakan perpustakaan **Aspose.PDF for .NET**.

<abbr title="Bitmap Image File">BMP</abbr> adalah file yang memiliki ekstensi BMP yang mewakili file gambar Bitmap yang digunakan untuk menyimpan gambar digital bitmap. Gambar ini independen dari adaptor grafis dan juga disebut sebagai format file bitmap yang independen dari perangkat (DIB).
Anda dapat mengonversi BMP ke file PDF dengan API Aspose.PDF for .NET. Oleh karena itu, Anda dapat mengikuti langkah-langkah berikut untuk mengonversi gambar BMP:

<a name="csharp-bmp-to-pdf" id="csharp-bmp-to-pdf"><strong>Langkah: Mengubah BMP menjadi PDF dalam C#</strong></a>

1.
1.
2. Muat gambar **BMP** masukan.
3. Akhirnya, simpan file PDF keluaran.

Berikut adalah potongan kode yang mengikuti langkah-langkah ini dan menunjukkan cara mengonversi BMP ke PDF menggunakan C#:

```csharp
//Inisialisasi dokumen PDF kosong
using (Document pdfDocument = new Document())
{
    pdfDocument.Pages.Add();
    Aspose.Pdf.Image image = new Aspose.Pdf.Image();

    // Muat file gambar BMP contoh
    image.File = dataDir + "Sample.bmp";
    pdfDocument.Pages[1].Paragraphs.Add(image);

    // Simpan dokumen PDF keluaran
    pdfDocument.Save(dataDir + "BMPtoPDF.pdf");
}
```

{{% alert color="success" %}}
**Coba konversi BMP ke PDF secara online**

Aspose menyajikan aplikasi gratis online ["BMP to PDF"](https://products.aspose.app/pdf/conversion/bmp-to-pdf/), di mana Anda dapat mencoba untuk menyelidiki fungsionalitas dan kualitas kerjanya.

[![Aspose.PDF Convertion BMP to PDF using Free App](bmp_to_pdf.png)](https://products.aspose.app/pdf/conversion/bmp-to-pdf/)
{{% /alert %}}

## Konversi CGM ke PDF

<abbr title="Computer Graphics Metafile">CGM</abbr> adalah ekstensi file untuk format Computer Graphics Metafile yang umum digunakan dalam aplikasi CAD (computer-aided design) dan grafik presentasi.
<abbr title="Computer Graphics Metafile">CGM</abbr> adalah ekstensi file untuk format Computer Graphics Metafile yang umumnya digunakan dalam aplikasi CAD (computer-aided design) dan grafis presentasi.

Lihat potongan kode berikut untuk mengonversi file CGM ke format PDF.

<a name="csharp-cgm-to-pdf" id="csharp-cgm-to-pdf"><strong>Langkah: Mengonversi CGM ke PDF di C#</strong></a>

1. Buat sebuah instance dari kelas [CgmLoadOptions](https://reference.aspose.com/pdf/net/aspose.pdf/cgmloadoptions).
2. Buat sebuah instance dari kelas [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) dengan menyebutkan nama file sumber dan opsi.
3. Simpan dokumen dengan nama file yang diinginkan.

```csharp
public static void ConvertCGMtoPDF()
{
    CgmLoadOptions option = new CgmLoadOptions();
    Document pdfDocument= new Document(_dataDir+"corvette.cgm", option);
    pdfDocument.Save(_dataDir+"CGMtoPDF.pdf");
}
```

## Mengonversi DICOM ke PDF

<abbr title="Digital Imaging and Communications in Medicine">DICOM</abbr> adalah standar industri medis untuk pembuatan, penyimpanan, transmisi, dan visualisasi gambar medis digital dan dokumen pasien yang diperiksa.
Format <abbr title="Digital Imaging and Communications in Medicine">DICOM</abbr> adalah standar industri medis untuk pembuatan, penyimpanan, transmisi, dan visualisasi gambar medis digital dan dokumen pasien yang diperiksa.

**Aspsoe.PDF for .NET** memungkinkan Anda mengonversi gambar DICOM dan SVG, tetapi karena alasan teknis untuk menambahkan gambar Anda perlu menentukan jenis file yang akan ditambahkan ke PDF:

<a name="csharp-dicom-to-pdf" id="csharp-dicom-to-pdf"><strong>Langkah: Mengonversi DICOM ke PDF dalam C#</strong></a>

1. Buat objek dari kelas Image.
2. Tambahkan gambar ke koleksi Paragraphs halaman.
3. Tentukan properti [FileType](https://reference.aspose.com/pdf/net/aspose.pdf/image/properties/filetype).
4. Tentukan jalur atau sumber file.
    - Jika gambar berada di lokasi di hard drive, tentukan lokasi jalur menggunakan properti Image.File.
    - Jika gambar diletakkan di dalam MemoryStream, berikan objek yang memegang gambar ke properti Image.ImageStream.

Potongan kode berikut menunjukkan cara mengonversi file DICOM ke format PDF dengan Aspose.PDF.
Potongan kode berikut menunjukkan cara mengonversi file DICOM ke format PDF dengan Aspose.PDF.

```csharp
private const string _dataDir = "..\\..\\..\\..\\Samples";
// Mengonversi gambar DICOM ke PDF menggunakan kelas Image
public static void ConvertDICOMtoPDF()
{
    // Instansiasi Objek Dokumen
    Document pdfDocument = new Document();

    // Tambahkan halaman ke koleksi halaman dokumen
    Page page = pdfDocument.Pages.Add();

    Image image = new Image
    {
        FileType = ImageFileType.Dicom,
        File = System.IO.Path.Combine(_dataDir,"bmode.dcm")
    };
    pdfDocument.Pages[1].Paragraphs.Add(image);
    // Simpan keluaran sebagai format PDF
    pdfDocument.Save(System.IO.Path.Combine(_dataDir,"PDFWithDicomImage_out.pdf"));
}
```

{{% alert color="success" %}}
**Coba konversi DICOM ke PDF secara online**

Aspose menyajikan aplikasi gratis online ["DICOM to PDF"](https://products.aspose.app/pdf/conversion/dicom-to-pdf/), di mana Anda dapat mencoba untuk menyelidiki fungsionalitas dan kualitas kerjanya.
{{% /alert %}}

[![Aspose.PDF Konversi DICOM ke PDF menggunakan Aplikasi Gratis](dicom_to_pdf.png)](https://products.aspose.app/pdf/conversion/dicom-to-pdf/)
## Mengonversi EMF ke PDF

<abbr title="Enhanced metafile format">EMF</abbr> menyimpan gambar secara independen dari perangkat. Metafile EMF terdiri dari catatan dengan panjang variabel secara berurutan yang dapat merender gambar yang tersimpan setelah diparsing di perangkat output mana pun. Selanjutnya, Anda dapat mengonversi gambar EMF ke PDF menggunakan langkah-langkah berikut:

<a name="csharp-emf-to-pdf" id="csharp-emf-to-pdf"><strong>Langkah: Mengonversi EMF ke PDF dalam C#</strong></a>

1. Pertama, inisialisasi objek kelas [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).
2. Muat file gambar **EMF**.
3. Tambahkan gambar EMF yang dimuat ke sebuah Halaman.
4. Simpan dokumen PDF.

Selain itu, cuplikan kode berikut menunjukkan cara mengonversi EMF ke PDF dengan C# dalam kode .NET Anda:

```csharp
// Inisialisasi dokumen PDF baru
var doc = new Document();

// Tentukan jalur file gambar EMF masukan
var imageFile = dataDir + "drawing.emf";
var page = doc.Pages.Add();
string file = imageFile;
FileStream filestream = new FileStream(file, FileMode.Open, FileAccess.Read);
BinaryReader reader = new BinaryReader(filestream);
long numBytes = new FileInfo(file).Length;
byte[] bytearray = reader.ReadBytes((int)numBytes);
Stream stream = new MemoryStream(bytearray);
var b = new Bitmap(stream);

// Tentukan properti dimensi halaman
page.PageInfo.Margin.Bottom = 0;
page.PageInfo.Margin.Top = 0;
page.PageInfo.Margin.Left = 0;
page.PageInfo.Margin.Right = 0;
page.PageInfo.Width = b.Width;
page.PageInfo.Height = b.Height;
var image = new Aspose.Pdf.Image();
image.File = imageFile;
page.Paragraphs.Add(image);

//Simpan dokumen PDF keluaran
doc.Save(dataDir + "EMFtoPDF.pdf");
```
{{% alert color="success" %}}
**Coba konversi EMF ke PDF secara online**

Aspose mempersembahkan aplikasi gratis online ["EMF ke PDF"](https://products.aspose.app/pdf/conversion/emf-to-pdf/), di mana Anda dapat mencoba untuk menginvestigasi fungsionalitas dan kualitas kerjanya.

[![Konversi Aspose.PDF EMF ke PDF menggunakan Aplikasi Gratis](emf_to_pdf.png)](https://products.aspose.app/pdf/conversion/emf-to-pdf/)
{{% /alert %}}

## Konversi GIF ke PDF

Konversikan file GIF ke dokumen PDF menggunakan pustaka **Aspose.PDF for .NET**.

<abbr title="Graphics Interchange Format">GIF</abbr> mampu menyimpan data terkompresi tanpa kehilangan kualitas dalam format tidak lebih dari 256 warna. Format GIF yang independen dari perangkat dikembangkan pada tahun 1987 (GIF87a) oleh CompuServe untuk mentransmisikan gambar bitmap melalui jaringan.
Anda dapat mengonversi file GIF ke PDF dengan API Aspose.PDF untuk .NET. Oleh karena itu, Anda dapat mengikuti langkah-langkah berikut untuk mengonversi gambar GIF:

<a name="csharp-gif-to-pdf" id="csharp-gif-to-pdf"><strong>Langkah: Konversi GIF ke PDF dalam C#</strong></a>

1.
1.
2. Muat gambar **GIF** yang dimasukkan.
3. Akhirnya, simpan file PDF hasilnya.

Jadi, cuplikan kode berikut ini mengikuti langkah-langkah tersebut dan menunjukkan cara mengonversi BMP ke PDF menggunakan C#:

```csharp
//Inisialisasi dokumen PDF kosong
using (Document pdfDocument = new Document())
{
    pdfDocument.Pages.Add();
    Aspose.Pdf.Image image = new Aspose.Pdf.Image();

    // Muat file gambar GIF contoh
    image.File = dataDir + "Sample.gif";
    pdfDocument.Pages[1].Paragraphs.Add(image);

    // Simpan dokumen PDF hasil
    pdfDocument.Save(dataDir + "GIFtoPDF.pdf");
}
```

{{% alert color="success" %}}
**Coba konversi GIF ke PDF secara online**

Aspose menyajikan aplikasi gratis online ["GIF to PDF"](https://products.aspose.app/pdf/conversion/gif-to-pdf/), di mana Anda dapat mencoba untuk menyelidiki fungsionalitas dan kualitas kerjanya.

[![Aspose.PDF Convertion GIF to PDF using Free App](bmp_to_pdf.png)](https://products.aspose.app/pdf/conversion/gif-to-pdf/)
{{% /alert %}}

## Konversi JPG ke PDF

Tidak perlu heran bagaimana mengonversi JPG ke PDF, karena pustaka **Apose.PDF for .NET** memiliki solusi terbaik.
Tidak perlu heran bagaimana mengubah JPG menjadi PDF, karena perpustakaan **Apose.PDF for .NET** memiliki solusi terbaik.

Anda dapat dengan sangat mudah mengonversi gambar JPG menjadi PDF dengan Aspose.PDF for .NET dengan mengikuti langkah-langkah berikut:

<a name="csharp-jpg-to-pdf" id="csharp-jpg-to-pdf"><strong>Langkah: Mengonversi JPG ke PDF di C#</strong></a>

1. Inisialisasi objek dari kelas [Document](https://reference.aspose.com/page/net/aspose.page/document).
2. Tambahkan halaman baru ke dokumen PDF.
3. Muat gambar **JPG** dan tambahkan ke paragraf.
4. Simpan PDF keluaran.

Potongan kode di bawah ini menunjukkan cara mengonversi Gambar JPG ke PDF menggunakan C#:

```csharp
// Muat file JPG masukan
String path = dataDir + "Aspose.jpg";

// Inisialisasi dokumen PDF baru
Document doc = new Document();

// Tambahkan halaman kosong di dokumen kosong
Page page = doc.Pages.Add();
Aspose.Pdf.Image image = new Aspose.Pdf.Image();
image.File = (path);

// Tambahkan gambar di halaman
page.Paragraphs.Add(image);

// Simpan file PDF keluaran
doc.Save(dataDir + "ImagetoPDF.pdf");
```

Kemudian Anda dapat melihat cara mengonversi gambar ke PDF dengan **tinggi dan lebar halaman yang sama**.
Kemudian Anda dapat melihat cara mengonversi gambar menjadi PDF dengan **tinggi dan lebar halaman yang sama**.

1. Muat file gambar masukan
1. Dapatkan tinggi dan lebar gambar
1. Tetapkan tinggi, lebar, dan margin halaman
1. Simpan file PDF keluaran

Potongan kode berikut menunjukkan cara mengonversi Gambar ke PDF dengan tinggi dan lebar halaman yang sama menggunakan C#:

```csharp
// Muat file gambar JPG masukan
String path = dataDir + "Aspose.jpg";
System.Drawing.Image srcImage = System.Drawing.Image.FromFile(path);

// Baca Tinggi gambar masukan
int h = srcImage.Height;

// Baca Lebar gambar masukan
int w = srcImage.Width;

// Inisialisasi dokumen PDF baru
Document doc = new Document();

// Tambahkan halaman kosong
Page page = doc.Pages.Add();
Aspose.Pdf.Image image = new Aspose.Pdf.Image();
image.File = (path);

// Atur dimensi halaman dan margin
page.PageInfo.Height = (h);
page.PageInfo.Width = (w);
page.PageInfo.Margin.Bottom = (0);
page.PageInfo.Margin.Top = (0);
page.PageInfo.Margin.Right = (0);
page.PageInfo.Margin.Left = (0);
page.Paragraphs.Add(image);

// Simpan file PDF keluaran
doc.Save(dataDir + "ImagetoPDF_HeightWidth.pdf");
```
{{% alert color="success" %}}
**Coba Konversi JPG ke PDF Secara Online**

Aspose mempersembahkan aplikasi gratis online ["JPG to PDF"](https://products.aspose.app/pdf/conversion/jpg-to-pdf/) anda, di mana Anda dapat mencoba untuk meneliti fungsionalitas dan kualitas kerjanya.

[![Konversi Aspose.PDF JPG ke PDF menggunakan Aplikasi Gratis](jpg_to_pdf.png)](https://products.aspose.app/pdf/conversion/jpg-to-pdf/)
{{% /alert %}}

## Konversi PNG ke PDF

**Aspose.PDF for .NET** mendukung fitur untuk mengkonversi gambar PNG ke format PDF. Periksa potongan kode berikut untuk merealisasikan tugas Anda.

<abbr title="Portable Network Graphics">PNG</abbr> merujuk pada tipe format file gambar raster yang menggunakan kompresi tanpa kehilangan, yang membuatnya populer di antara penggunanya.

Anda dapat mengkonversi gambar PNG ke PDF menggunakan langkah-langkah berikut:

<a name="csharp-png-to-pdf" id="csharp-png-to-pdf"><strong>Langkah: Konversi PNG ke PDF dalam C#</strong></a>

1. Muat gambar **PNG** yang diinput.
2. Baca nilai tinggi dan lebar.
3.
3.
4. Tentukan dimensi halaman.
5. Simpan file keluaran.

Selain itu, cuplikan kode di bawah ini menunjukkan cara mengonversi PNG ke PDF dengan C# dalam aplikasi .NET Anda:

```csharp
// Muat file PNG masukan
String path = dataDir + "Aspose.png";
System.Drawing.Image srcImage = System.Drawing.Image.FromFile(path);
int h = srcImage.Height;
int w = srcImage.Width;

// Inisialisasi Dokumen baru
Document doc = new Document();
Page page = doc.Pages.Add();
Aspose.Pdf.Image image = new Aspose.Pdf.Image();
image.File = (path);

// Tentukan dimensi halaman
page.PageInfo.Height = (h);
page.PageInfo.Width = (w);
page.PageInfo.Margin.Bottom = (0);
page.PageInfo.Margin.Top = (0);
page.PageInfo.Margin.Right = (0);
page.PageInfo.Margin.Left = (0);
page.Paragraphs.Add(image);

// Simpan PDF keluaran
doc.Save(dataDir + "ImagetoPDF.pdf");
```

{{% alert color="success" %}}
**Cobalah konversi PNG ke PDF secara online**

Aspose menyajikan aplikasi gratis online ["PNG to PDF"](https://products.aspose.app/pdf/conversion/png-to-pdf/), di mana Anda dapat mencoba untuk menyelidiki fungsionalitas dan kualitas kerjanya.

Aspose menyajikan aplikasi online gratis ["PNG to PDF"](https://products.aspose.app/pdf/conversion/png-to-pdf/), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitas kerjanya.
{{% /alert %}}

[![Konversi Aspose.PDF PNG ke PDF menggunakan Aplikasi Gratis](png_to_pdf.png)](https://products.aspose.app/pdf/conversion/png-to-pdf/)

## Mengonversi SVG ke PDF

**Aspose.PDF untuk .NET** menjelaskan cara mengonversi gambar SVG ke format PDF dan cara mendapatkan dimensi dari file <abbr title="Scalable Vector Graphics">SVG</abbr> sumber.

Scalable Vector Graphics (SVG) adalah keluarga spesifikasi format file berbasis XML untuk grafik vektor dua dimensi, baik statis maupun dinamis (interaktif atau animasi). Spesifikasi SVG adalah standar terbuka yang telah dikembangkan oleh Konsorsium World Wide Web (W3C) sejak tahun 1999.

Gambar SVG dan perilakunya didefinisikan dalam file teks XML.
Gambar SVG dan perilakunya didefinisikan dalam file teks XML.

{{% alert color="success" %}}
**Cobalah mengonversi format SVG ke PDF secara online**

Aspose.PDF untuk .NET menyajikan Anda aplikasi gratis online ["SVG to PDF"](https://products.aspose.app/pdf/conversion/svg-to-pdf), di mana Anda dapat mencoba untuk mengeksplorasi fungsionalitas dan kualitas kerjanya.

[![Konversi Aspose.PDF SVG ke PDF dengan Aplikasi Gratis](svg_to_pdf.png)](https://products.aspose.app/pdf/conversion/svg-to-pdf)
{{% /alert %}}

Untuk mengonversi file SVG ke PDF, gunakan kelas yang bernama [SvgLoadOptions](https://reference.aspose.com/net/pdf/aspose.pdf/svgloadoptions) yang digunakan untuk menginisialisasi objek [`LoadOptions`](https://reference.aspose.com/pdf/net/aspose.pdf/loadoptions). Nantinya, objek ini akan diserahkan sebagai argumen selama inisialisasi objek Dokumen dan membantu mesin rendering PDF untuk menentukan format input dari dokumen sumber.

<a name="csharp-svg-to-pdf" id="csharp-svg-to-pdf"><strong>Langkah-Langkah: Mengonversi SVG ke PDF dalam C#</strong></a>

1.
1.
2. Buat instance kelas [`Document`](https://reference.aspose.com/pdf/net/aspose.pdf/document) dengan menyebutkan nama file sumber dan opsi.
3. Simpan dokumen dengan nama file yang diinginkan.

Berikut ini adalah potongan kode yang menunjukkan proses mengonversi file SVG menjadi format PDF dengan Aspose.PDF untuk .NET.

```csharp
public static void ConvertSVGtoPDF()
{
    SvgLoadOptions option = new SvgLoadOptions();
    Document pdfDocument= new Document(_dataDir + "car.svg", option);
    pdfDocument.Save(_dataDir + "svgtest.pdf");
}
```

## Dapatkan dimensi SVG

Juga dimungkinkan untuk mendapatkan dimensi dari file SVG sumber. Informasi ini dapat berguna jika kita ingin SVG menutupi seluruh halaman dari PDF keluaran. Properti AdjustPageSize dari kelas ScgLoadOption memenuhi kebutuhan ini. Nilai default dari properti ini adalah false. Jika nilai tersebut diatur menjadi true, PDF keluaran akan memiliki ukuran (dimensi) yang sama seperti SVG sumber.

Berikut ini adalah potongan kode yang menunjukkan proses mendapatkan dimensi file SVG sumber dan menghasilkan file PDF.
Potongan kode berikut menunjukkan proses mendapatkan dimensi file SVG sumber dan menghasilkan file PDF.

```csharp
public static void ConvertSVGtoPDF_Advanced()
{
    // Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
    // Jalur ke direktori dokumen.
    string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();
    var loadopt = new SvgLoadOptions();
    loadopt.AdjustPageSize = true;
    var svgDoc = new Document(dataDir + "GetSVGDimensions.svg", loadopt);
    svgDoc.Pages[1].PageInfo.Margin.Top = 0;
    svgDoc.Pages[1].PageInfo.Margin.Left = 0;
    svgDoc.Pages[1].PageInfo.Margin.Bottom = 0;
    svgDoc.Pages[1].PageInfo.Margin.Right = 0;
    svgDoc.Save(dataDir + "GetSVGDimensions_out.pdf");
}
```

### Fitur yang Didukung SVG

<table>
    <thead>
        <tr>
            <th>
                <p>Tag SVG</p>
            </th>
            <th>
                <p>Contoh Penggunaan</p>
            </th>
        </tr>
    </thead>
    <tbody>
<tbody>
   <tr>
       <td>
           <p>lingkaran</p>
       </td>
       <td>
           <code><pre>&lt circle id="r2" cx="10" cy="10" r="10" stroke="blue" stroke-width="2"&gt </pre></code>
       </td>
   </tr>
   <tr>
       <td>
           <p>definisi</p>
       </td>
       <td>
           <code>&lt;defs&gt;&nbsp; <br> &lt;rect id="r1" width="15" height="15"
               stroke="blue" stroke-width="2" /&gt;&nbsp; <br> &lt;circle id="r2"
               cx="10" cy="10" r="10" stroke="blue" stroke-width="2"/&gt;&nbsp; <br>
               &lt;circle id="r3" cx="10" cy="10" r="10" stroke="blue" stroke-width="3"/&gt;&nbsp; <br> &lt;/defs&gt;&nbsp; <br> &lt;use
               x="25" y="40" xlink:href="#r1" fill="red"/&gt;&nbsp; <br> &lt;use
               x="35" y="15" xlink:href="#r2" fill="green"/&gt;&nbsp; <br> &lt;use
               x="58" y="50" xlink:href="#r3" fill="blue"/&gt;</code>
       </td>
   </tr>
</tbody>

         </tr>
        <tr>
            <td>
                <p>tref</p>
            </td>
            <td>
                <p>&lt;defs&gt;&nbsp; <br> &nbsp;&nbsp;&nbsp; &lt;text
                    id="ReferencedText"&gt;&nbsp; <br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                    Data karakter yang dirujuk&nbsp; <br> &nbsp;&nbsp;&nbsp;
                    &lt;/text&gt;&nbsp; <br> &lt;/defs&gt;&nbsp; <br
                        class="atl-forced-newline"> &lt;text x="10" y="100" font-size="15" fill="red" &gt;&nbsp; <br
                        class="atl-forced-newline"> &nbsp;&nbsp;&nbsp; &lt;tref
                    xlink:href="#ReferencedText"/&gt;&nbsp; <br> &lt;/text&gt;</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>use</p>
            </td>
            <td>
                <p>&lt;defs&gt;&nbsp; <br> &nbsp;&nbsp;&nbsp; &lt;text id="Text" x="400"
                    y="200"&nbsp; <br>
                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; font-family="Verdana" font-size="100"
```


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; font-family="Verdana" font-size="100"
                    text-anchor="middle" &gt;&nbsp; <br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                    Teks yang diberi masker&nbsp; <br> &nbsp;&nbsp;&nbsp; &lt;/text&gt;&nbsp; <br
                        class="atl-forced-newline"> &lt;use xlink:href="#Text" fill="blue"&nbsp; /&gt;</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>elips&nbsp;</p>
            </td>
            <td>
                <p>&lt;ellipse cx="2.5" cy="1.5" rx="2" ry="1" fill="merah" /&gt;</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>g&nbsp;</p>
            </td>
            <td>
                <p>&lt;g fill="none" stroke="abu-abu gelap" stroke-width="1.5" &gt;&nbsp; <br>
                    &nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;&lt;line x1="-7"
                    y1="-7" x2="-3" y2="-3"/&gt;&nbsp; <br> &nbsp;&nbsp;
                    &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;&lt;line x1="7" y1="7" x2="3"
```


&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;&lt;line x1="7" y1="7" x2="3"
y2="3"/&gt;&nbsp; <br> &nbsp;&nbsp; &nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;&lt;line x1="-7" y1="7" x2="-3" y2="3"/&gt;&nbsp;
<br> &nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp; &nbsp;&lt;line x1="7" y1="-7" x2="3" y2="-3"/&gt;&nbsp; <br
    class="atl-forced-newline"> &lt;/g&gt;&nbsp;</p>
</td>
</tr>
<tr>
<td>
    <p>gambar</p>
</td>
<td>
    <p>&lt;image id="ShadedRelief" x="24" y="4" width="64" height="82" xlink:href="relief.jpg"
        /&gt;&nbsp;</p>
</td>
</tr>
<tr>
<td>
    <p>garis</p>
</td>
<td>
    <p>&lt;line style="stroke:#eea;stroke-width:8" x1="10" y1="30" x2="260" y2="100"/&gt;&nbsp;</p>
```


<tr>
    <td>
        <p>garis</p>
    </td>
    <td>
        <p>&lt;line style="stroke:#eea;stroke-width:8" x1="10" y1="30" x2="260" y2="100"/&gt;&nbsp;</p>
    </td>
</tr>
<tr>
    <td>
        <p>jalur</p>
    </td>
    <td>
        <p>&lt;path style="fill:#daa;fill-rule:evenodd;stroke:red" d="M 230,150 C 290,30 10,255 110,140 z
            "/&gt;&nbsp;</p>
    </td>
</tr>
<tr>
    <td>
        <p>gaya</p>
    </td>
    <td>
        <p>&lt;path style="fill:#daa;fill-rule:evenodd;stroke:red" d="M 230,150 C 290,30 10,255 110,140 z
            "/&gt;</p>
    </td>
</tr>
<tr>
    <td>
        <p>poligon</p>
    </td>
    <td>
        <p>&lt;polygon style="stroke:#24a;stroke-width:1.5;fill:#eefefe" points="10,10 180,10 10,250 10,10"
            /&gt;</p>
    </td>
</tr>
<tr>
    <td>
        <p>polilin</p>
    </td>
```

<tr>
    <td>
        <p>polyline</p>
    </td>
    <td>
        <p>&lt;polyline fill="none" stroke="abu-abu tua" stroke-width="1" points="-3,-6 3,-6 3,1 5,1 0,7 -5,1
            -3,1 -3,-5"/&gt;</p>
    </td>
</tr>
<tr>
    <td>
        <p>rect&nbsp;</p>
    </td>
    <td>
        <p>&lt;rect x="0" y="0" width="400" height="600" stroke="none" fill="biru alice" /&gt;</p>
    </td>
</tr>
<tr>
    <td>
        <p>svg</p>
    </td>
    <td>
        <p>&lt;svg xmlns="http://www.w3.org/2000/svg" version="1.1" width="10cm" height="5cm" &gt;</p>
    </td>
</tr>
<tr>
    <td>
        <p>text</p>
    </td>
    <td>
        <p>&lt;text font-family="sans-serif" fill="abu-abu tua" font-size="22px" font-weight="bold" x="58"
            y="30" pointer-events="none"&gt;Judul Peta&lt;/text&gt;</p>
    </td>
</tr>
```
## Konversi TIFF ke PDF

**Aspose.PDF** mendukung format file, baik itu frame tunggal atau multi-frame <abbr title="Tag Image File Format">TIFF</abbr>. Ini berarti Anda dapat mengonversi gambar TIFF menjadi PDF dalam aplikasi .NET Anda.

TIFF atau TIF, Tagged Image File Format, mewakili gambar raster yang dimaksudkan untuk penggunaan pada berbagai perangkat yang mematuhi standar format file ini.
TIFF atau TIF, Tagged Image File Format, merupakan format file gambar raster yang dimaksudkan untuk digunakan pada berbagai perangkat yang mematuhi standar format file ini.

Anda dapat mengonversi TIFF ke PDF dengan cara yang sama seperti format file grafis raster lainnya:

<a name="csharp-tiff-to-pdf" id="csharp-tiff-to-pdf"><strong>Langkah-langkah: Mengonversi TIFF ke PDF dalam C#</strong></a>

1. Buat objek kelas [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) baru dan tambahkan Halaman.
2. Muat gambar **TIFF** yang diinput.
3. Simpan dokumen PDF.

```csharp
Inisialisasi dokumen PDF kosong
using (Document pdfDocument = new Document())
{
    pdfDocument.Pages.Add();
    Aspose.Pdf.Image image = new Aspose.Pdf.Image();

    // Muat file gambar Tiff contoh
    image.File = dataDir + "sample.tiff";
    pdfDocument.Pages[1].Paragraphs.Add(image);

    // Simpan dokumen PDF keluaran
    pdfDocument.Save(dataDir + "TIFFtoPDF.pdf");
}
```

Jika Anda perlu mengonversi gambar TIFF multi-halaman menjadi dokumen PDF multi-halaman dan mengontrol beberapa parameter, misalnya.
Jika Anda perlu mengonversi gambar TIFF multi-halaman menjadi dokumen PDF multi-halaman dan mengontrol beberapa parameter, misalnya:

1. Buat instance dari kelas Document
1. Muat gambar TIFF masukan
1. Dapatkan FrameDimension dari frame
1. Tambahkan halaman baru untuk setiap frame
1. Akhirnya, simpan gambar ke halaman PDF

Potongan kode berikut menunjukkan cara mengonversi gambar TIFF multi-halaman atau multi-frame ke PDF dengan C#:

```csharp
public static void TiffToPDF2()
{
    // Inisialisasi Dokumen baru
    Document pdf = new Document();

    // Muat gambar TIFF ke dalam stream
    Bitmap bitmap = new Bitmap(File.OpenRead(_dataDir+"multipage.tif"));
    // Konversi TIFF multi halaman atau multi frame ke PDF
    FrameDimension dimension = new FrameDimension(bitmap.FrameDimensionsList[0]);
    int frameCount = bitmap.GetFrameCount(dimension);

    // Iterasi melalui setiap frame
    for (int frameIdx = 0; frameIdx <= frameCount - 1; frameIdx++)
    {
        Page page = pdf.Pages.Add();

        bitmap.SelectActiveFrame(dimension, frameIdx);

        MemoryStream currentImage = new MemoryStream();
        bitmap.Save(currentImage, ImageFormat.Tiff);

        Aspose.Pdf.Image imageht = new Aspose.Pdf.Image
        {
            ImageStream = currentImage,
            // Terapkan beberapa opsi lain
            // ImageScale = 0.5
        };
        page.Paragraphs.Add(imageht);
    }

    // Simpan file PDF keluaran
    pdf.Save(_dataDir + "TifftoPDF.pdf");
}
```
## Berlaku untuk

|**Platform**|**Supported**|**Comments**|
| :- | :- |:- |
|Windows .NET Framework|2.0-4.6| |
|Windows .NET Core |2.0-3.1| |
|.NET 5 Windows| |
|Linux .NET Core|2.0-3.1 | |
|.NET 5 Linux | |

## Lihat Juga

Artikel ini juga membahas topik-topik berikut. Kodenya sama seperti di atas.

_Format_: **BMP**
- [Kode C# BMP ke PDF](#csharp-bmp-to-pdf)
- [API C# BMP ke PDF](#csharp-bmp-to-pdf)
- [C# BMP ke PDF Secara Pemrograman](#csharp-bmp-to-pdf)
- [Perpustakaan C# BMP ke PDF](#csharp-bmp-to-pdf)
- [C# Simpan BMP sebagai PDF](#csharp-bmp-to-pdf)
- [C# Hasilkan PDF dari BMP](#csharp-bmp-to-pdf)
- [C# Buat PDF dari BMP](#csharp-bmp-to-pdf)
- [Konverter C# BMP ke PDF](#csharp-bmp-to-pdf)

_Format_: **CGM**
- [Kode C# CGM ke PDF](#csharp-cgm-to-pdf)
- [API C# CGM ke PDF](#csharp-cgm-to-pdf)
- [C# CGM ke PDF Secara Pemrograman](#csharp-cgm-to-pdf)
- [Perpustakaan C# CGM ke PDF](#csharp-cgm-to-pdf)
- [C# Simpan CGM sebagai PDF](#csharp-cgm-to-pdf)
- [C# Hasilkan PDF dari CGM](#csharp-cgm-to-pdf)
- [C# Buat PDF dari CGM](#csharp-cgm-to-pdf)
- [Konverter C# CGM ke PDF](#csharp-cgm-to-pdf)
- [C# CGM ke PDF Converter](#csharp-cgm-to-pdf)

_Format_: **DICOM**
- [Kode C# DICOM ke PDF](#csharp-dicom-to-pdf)
- [API C# DICOM ke PDF](#csharp-dicom-to-pdf)
- [C# DICOM ke PDF Secara Programatis](#csharp-dicom-to-pdf)
- [Perpustakaan C# DICOM ke PDF](#csharp-dicom-to-pdf)
- [C# Simpan DICOM sebagai PDF](#csharp-dicom-to-pdf)
- [C# Hasilkan PDF dari DICOM](#csharp-dicom-to-pdf)
- [C# Buat PDF dari DICOM](#csharp-dicom-to-pdf)
- [C# DICOM ke PDF Converter](#csharp-dicom-to-pdf)

_Format_: **EMF**
- [Kode C# EMF ke PDF](#csharp-emf-to-pdf)
- [API C# EMF ke PDF](#csharp-emf-to-pdf)
- [C# EMF ke PDF Secara Programatis](#csharp-emf-to-pdf)
- [Perpustakaan C# EMF ke PDF](#csharp-emf-to-pdf)
- [C# Simpan EMF sebagai PDF](#csharp-emf-to-pdf)
- [C# Hasilkan PDF dari EMF](#csharp-emf-to-pdf)
- [C# Buat PDF dari EMF](#csharp-emf-to-pdf)
- [C# EMF ke PDF Converter](#csharp-emf-to-pdf)


