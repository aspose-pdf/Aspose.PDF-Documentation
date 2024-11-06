---
title: Mengonversi HTML ke PDF di .NET
linktitle: Mengonversi file HTML ke PDF
type: docs
weight: 40
url: id/net/convert-html-to-pdf/
lastmod: "2021-11-01"
description: Topik ini menunjukkan cara mengonversi HTML ke PDF dan MHTML ke PDF menggunakan Aspose.PDF.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---
## Overview 

Artikel ini menjelaskan cara **mengonversi HTML ke PDF menggunakan C#**. Ini mencakup topik-topik berikut.

Potongan kode berikut juga bekerja dengan pustaka [Aspose.PDF.Drawing](/pdf/net/drawing/).

_Format_: **HTML**
- [C# HTML ke PDF](#csharp-html-to-pdf)
- [C# Mengonversi HTML ke PDF](#csharp-html-to-pdf)
- [C# Cara mengonversi HTML ke PDF](#csharp-html-to-pdf)

_Format_: **MHTML**
- [C# MHTML ke PDF](#csharp-mhtml-to-pdf)
- [C# Mengonversi MHTML ke PDF](#csharp-mhtml-to-pdf)
- [C# Cara mengonversi MHTML ke PDF](#csharp-mhtml-to-pdf)

_Format_: **WebPage**
- [C# WebPage ke PDF](#csharp-webpage-to-pdf)
- [C# Mengonversi WebPage ke PDF](#csharp-webpage-to-pdf)
- [C# Cara mengonversi WebPage ke PDF](#csharp-webpage-to-pdf)

## Konversi HTML ke PDF dengan C#
## Konversi HTML ke PDF dengan C#

**Aspose.PDF untuk .NET** adalah API manipulasi PDF yang memungkinkan Anda mengonversi dokumen HTML yang ada menjadi PDF secara mulus. Proses konversi HTML ke PDF dapat disesuaikan dengan fleksibel.

## Mengonversi HTML ke PDF

Contoh kode C# berikut menunjukkan cara mengonversi dokumen HTML menjadi PDF.

<a name="csharp-html-to-pdf"><strong>Langkah-langkah: Mengonversi HTML ke PDF dalam C#</strong></a>

1. Buat instance dari kelas [HtmlLoadOptions](https://reference.aspose.com/pdf/net/aspose.pdf/htmlloadoptions/).
2. Inisialisasi objek [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document/).
3. Simpan dokumen PDF keluaran dengan memanggil metode **Document.Save()**.

```csharp
public static void ConvertHTMLtoPDF()
{
    HtmlLoadOptions options= new HtmlLoadOptions();
    Document pdfDocument= new Document(_dataDir + "test.html", options);
    pdfDocument.Save(_dataDir + "html_test.PDF");
}
```

{{% alert color="success" %}}
**Coba konversi HTML ke PDF secara online**

Aspose mempersembahkan aplikasi gratis online ["HTML to PDF"](https://products.aspose.app/html/en/conversion/html-to-pdf) di mana Anda dapat mencoba untuk menyelidiki fungsionalitas dan kualitas kerjanya.
Aspose mempersembahkan aplikasi gratis online ["HTML to PDF"](https://products.aspose.app/html/en/conversion/html-to-pdf), di mana Anda dapat mencoba untuk mengeksplorasi fungsionalitas dan kualitas kerjanya.
{{% /alert %}}

[![Konversi Aspose.PDF HTML ke PDF menggunakan Aplikasi Gratis](html.png)](https://products.aspose.app/html/en/conversion/html-to-pdf)

## Konversi lanjutan dari HTML ke PDF

Mesin Konversi HTML memiliki beberapa opsi yang memungkinkan kita mengontrol proses konversi.

### Dukungan Media Queries

Media queries adalah teknik populer untuk menyampaikan style sheet yang disesuaikan ke berbagai perangkat. Kita dapat mengatur tipe perangkat menggunakan properti [`HtmlMediaType`](https://reference.aspose.com/pdf/net/aspose.pdf/htmlloadoptions/properties/htmlmediatype).

```csharp
public static void ConvertHTMLtoPDFAdvanced_MediaType()
{
    HtmlLoadOptions options = new HtmlLoadOptions
    {
        // setel mode Print atau Screen
        HtmlMediaType = HtmlMediaType.Print
    };
    Document pdfDocument = new Document(_dataDir + "test.html", options);
    pdfDocument.Save(_dataDir + "html_test.PDF");
}
```
### Mengaktifkan (menonaktifkan) penyertaan font

Halaman HTML sering menggunakan font (misalnya font dari folder lokal, Google Fonts, dll). Kita juga dapat mengontrol penyertaan font dalam dokumen menggunakan properti [`IsEmbedFonts`](https://reference.aspose.com/pdf/net/aspose.pdf/htmlloadoptions/properties/isembedfonts).

```csharp
public static void ConvertHTMLtoPDFAdvanced_EmbedFonts()
{
    // Menonaktifkan penyertaan font
    HtmlLoadOptions options = new HtmlLoadOptions {IsEmbedFonts = false};
    Document pdfDocument= new Document(_dataDir + "test_fonts.html", options);
    pdfDocument.Save(_dataDir + "html_test.PDF");
}
```

### Mengelola pemuatan sumber daya eksternal

Mesin Konversi menyediakan mekanisme yang memungkinkan Anda untuk mengontrol pemuatan sumber daya tertentu yang terkait dengan dokumen HTML.
Kelas [`HtmlLoadOptions`](https://reference.aspose.com/pdf/net/aspose.pdf/htmlloadoptions) memiliki properti [`CustomLoaderOfExternalResources`](https://reference.aspose.com/pdf/net/aspose.pdf/htmlloadoptions/fields/customloaderofexternalresources) yang memungkinkan kita mendefinisikan perilaku pemuat sumber daya.
Kelas [`HtmlLoadOptions`](https://reference.aspose.com/pdf/net/aspose.pdf/htmlloadoptions) memiliki properti [`CustomLoaderOfExternalResources`](https://reference.aspose.com/pdf/net/aspose.pdf/htmlloadoptions/fields/customloaderofexternalresources) yang memungkinkan kita menentukan perilaku loader sumber daya.
Misalkan kita perlu mengganti semua gambar PNG dengan satu gambar `test.jpg` dan mengganti URL eksternal dengan internal untuk sumber daya lainnya.
Untuk melakukan ini, kita dapat mendefinisikan loader khusus `SamePictureLoader` dan menunjuk [`CustomLoaderOfExternalResources`](https://reference.aspose.com/pdf/net/aspose.pdf/htmlloadoptions/fields/customloaderofexternalresources) ke nama ini.

```csharp
public static void ConvertHTMLtoPDFAdvanced_DummyImage()
{
    HtmlLoadOptions options = new HtmlLoadOptions
    {
        CustomLoaderOfExternalResources = SamePictureLoader
    };
    Document pdfDocument= new Document(_dataDir + "test.html", options);
    pdfDocument.Save(_dataDir + "html_test.PDF");
}

private static LoadOptions.ResourceLoadingResult SamePictureLoader(string resourceURI)
{
    LoadOptions.ResourceLoadingResult result;

    if (resourceURI.EndsWith(".png"))
    {
        byte[] resultBytes = File.ReadAllBytes(_dataDir + "test.jpg");
        result = new LoadOptions.ResourceLoadingResult(resultBytes)
        {
            //Setel Tipe MIME
            MIMETypeIfKnown = "image/jpeg"
        };
    }
    else
    {
        result = new LoadOptions.ResourceLoadingResult(GetContentFromUrl(resourceURI));
    }
    return result;
}

private static byte[] GetContentFromUrl(string url)
{
    var httpClient = new HttpClient();
    return httpClient.GetByteArrayAsync(url).GetAwaiter().GetResult();
}
```
## Mengonversi Halaman Web ke PDF

Mengonversi halaman web sedikit berbeda dari mengonversi dokumen HTML lokal. Untuk mengonversi isi halaman web ke format PDF, kita dapat terlebih dahulu mengambil isi halaman HTML menggunakan instance HttpClient, membuat objek Stream, mengoper isinya ke objek Dokumen dan merender hasilnya dalam format PDF.

Ketika mengonversi halaman web yang dihosting di webserver ke PDF:

<a name="csharp-webpage-to-pdf"><strong>Langkah-langkah: Mengonversi Halaman Web ke PDF dalam C#</strong></a>

1. Baca isi halaman menggunakan objek HttpClient.
1. Instansiasi objek [HtmlLoadOptions](https://reference.aspose.com/pdf/net/aspose.pdf/htmlloadoptions) dan atur URL dasar.
1. Inisialisasi objek Dokumen sambil mengoper objek stream.
1. Opsional, atur ukuran halaman dan/atau orientasi.

```csharp
public static void ConvertHTMLtoPDFAdvanced_WebPage()
{
    const string url = "https://en.wikipedia.org/wiki/Aspose_API";
    // Atur ukuran halaman A3 dan orientasi Landscape;   
    HtmlLoadOptions options = new HtmlLoadOptions(url)
    {
        PageInfo = {Width = 842, Height = 1191, IsLandscape = true}
    };
    Document pdfDocument= new Document(GetContentFromUrlAsStream(url), options);
    pdfDocument.Save(_dataDir + "html_test.PDF");
}

private static Stream GetContentFromUrlAsStream(string url, ICredentials credentials = null)
{
    using (var handler = new HttpClientHandler { Credentials = credentials })
    using (var httpClient = new HttpClient(handler))
    {
        return httpClient.GetStreamAsync(url).GetAwaiter().GetResult();
    }
}
```
### Menyediakan halaman web kredensial untuk konversi PDF

Terkadang kita perlu melakukan konversi file HTML yang memerlukan otentikasi dan hak akses, sehingga hanya pengguna autentik yang dapat mengambil konten halaman. Ini juga termasuk skenario di mana beberapa sumber/data yang dirujuk di dalam HTML diambil dari server eksternal yang memerlukan otentikasi dan untuk memenuhi kebutuhan ini, properti [`ExternalResourcesCredentials`](https://reference.aspose.com/pdf/net/aspose.pdf/htmlloadoptions/fields/externalresourcescredentials) ditambahkan ke kelas [`HtmlLoadOptions`](https://reference.aspose.com/pdf/net/aspose.pdf/htmlloadoptions). Cuplikan kode berikut menunjukkan langkah-langkah untuk mengirimkan kredensial untuk meminta HTML & sumber daya terkaitnya saat mengonversi file HTML ke konversi PDF.

```csharp
public static void ConvertHTMLtoPDFAdvanced_Authorized()
{
    const string url = "http://httpbin.org/basic-auth/user1/password1";
    var credentials = new NetworkCredential("user1", "password1");
    HtmlLoadOptions options = new HtmlLoadOptions(url)
    {
        ExternalResourcesCredentials = credentials
    };
    Document pdfDocument= new Document(GetContentFromUrlAsStream(url, credentials), options);
    pdfDocument.Save(_dataDir + "html_test.PDF");
}

private static Stream GetContentFromUrlAsStream(string url, ICredentials credentials = null)
{
    using (var handler = new HttpClientHandler { Credentials = credentials })
    using (var httpClient = new HttpClient(handler))
    {
        return httpClient.GetStreamAsync(url).GetAwaiter().GetResult();
    }
}
```
### Render semua konten HTML dalam satu Halaman

Aspose.PDF untuk .NET menyediakan kemampuan untuk merender semua konten dalam satu halaman saat mengonversi file HTML ke format PDF. Misalnya, jika Anda memiliki beberapa konten HTML yang ukuran keluarannya lebih besar dari satu halaman, Anda dapat menggunakan opsi untuk merender data keluaran ke dalam satu halaman PDF. Untuk menggunakan opsi ini, kelas HtmlLoadOptions diperluas dengan bendera IsRenderToSinglePage. Potongan kode di bawah ini menunjukkan cara menggunakan fungsionalitas ini.

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();
// Inisialisasi HTMLLoadSave Options
HtmlLoadOptions options = new HtmlLoadOptions();
// Atur Render ke properti halaman tunggal
options.IsRenderToSinglePage = true;
// Muat dokumen
Document pdfDocument= new Document(dataDir + "HTMLToPDF.html", options);
// Simpan
pdfDocument.Save(dataDir + "RenderContentToSamePage.pdf");
```

### Render HTML dengan Data SVG
### Render HTML dengan Data SVG

Aspose.PDF untuk .NET menyediakan kemampuan untuk mengonversi halaman HTML menjadi dokumen PDF. Karena HTML memungkinkan penambahan elemen grafis SVG sebagai tag di halaman, Aspose.PDF juga mendukung konversi data tersebut ke dalam file PDF hasilnya. Cuplikan kode berikut menunjukkan cara mengonversi file HTML dengan tag grafis SVG ke Dokumen PDF Bertag.

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();
// Tetapkan jalur file masukan
string inFile = dataDir + "HTMLSVG.html";
// Tetapkan jalur file keluaran
string outFile = dataDir + "RenderHTMLwithSVGData.pdf";
// Inisialisasi HtmlLoadOptions
HtmlLoadOptions options = new HtmlLoadOptions(Path.GetDirectoryName(inFile));
// Inisialisasi objek Dokumen
Document pdfDocument = new Document(inFile, options);
// simpan
pdfDocument.Save(outFile);
```

## Konversi MHTML ke PDF

{{% alert color="success" %}}
**Coba konversi MHTML ke PDF secara online**
**Coba Konversi MHTML ke PDF Secara Online**

Aspose.PDF untuk .NET mempersembahkan aplikasi gratis online ["MHTML ke PDF"](https://products.aspose.app/pdf/conversion/mhtml-to-pdf), di mana Anda dapat mencoba untuk meneliti fungsionalitas dan kualitas kerjanya.

[![Konversi Aspose.PDF MHTML ke PDF menggunakan Aplikasi Gratis](mhtml.png)](https://products.aspose.app/pdf/conversion/mhtml-to-pdf)
{{% /alert %}}

<abbr title="MIME encapsulation of aggregate HTML documents">MHTML</abbr>, singkatan dari MIME HTML, adalah format arsip halaman web yang digunakan untuk menggabungkan sumber daya yang biasanya diwakili oleh tautan eksternal (seperti gambar, animasi Flash, applet Java, dan file audio) dengan kode HTML ke dalam satu file.
<abbr title="MIME encapsulation of aggregate HTML documents">MHTML</abbr>, singkatan dari MIME HTML, adalah format arsip halaman web yang digunakan untuk menggabungkan sumber daya yang biasanya diwakili oleh tautan eksternal (seperti gambar, animasi Flash, applet Java, dan file audio) dengan kode HTML ke dalam satu file.

<a name="csharp-mhtml-to-pdf"><strong>Langkah: Mengonversi MHTML ke PDF dalam C#</strong></a>

1. Buat sebuah instansi dari kelas [MhtLoadOptions](https://reference.aspose.com/pdf/net/aspose.pdf/mhtloadoptions/).
2. Inisialisasi objek [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document/).
3. Simpan dokumen PDF keluaran dengan memanggil metode **Document.Save()**.

```csharp
public static void ConvertMHTtoPDF()
{
    MhtLoadOptions options = new MhtLoadOptions()
    {
        PageInfo = { Width = 842, Height = 1191, IsLandscape = true}
    };
    Document pdfDocument= new Document(_dataDir + "fileformatinfo.mht", options);
    pdfDocument.Save(_dataDir + "mhtml_test.PDF");
}
```

## Lihat Juga

Artikel ini juga mencakup topik-topik ini.
Artikel ini juga membahas topik-topik ini.

_Format_: **HTML**
- [Kode C# HTML ke PDF](#csharp-html-to-pdf)
- [API C# HTML ke PDF](#csharp-html-to-pdf)
- [C# HTML ke PDF Secara Pemrograman](#csharp-html-to-pdf)
- [Perpustakaan C# HTML ke PDF](#csharp-html-to-pdf)
- [C# Simpan HTML sebagai PDF](#csharp-html-to-pdf)
- [C# Hasilkan PDF dari HTML](#csharp-html-to-pdf)
- [C# Buat PDF dari HTML](#csharp-html-to-pdf)
- [Konverter C# HTML ke PDF](#csharp-html-to-pdf)

_Format_: **MHTML**
- [Kode C# MHTML ke PDF](#csharp-mhtml-to-pdf)
- [API C# MHTML ke PDF](#csharp-mhtml-to-pdf)
- [C# MHTML ke PDF Secara Pemrograman](#csharp-mhtml-to-pdf)
- [Perpustakaan C# MHTML ke PDF](#csharp-mhtml-to-pdf)
- [C# Simpan MHTML sebagai PDF](#csharp-mhtml-to-pdf)
- [C# Hasilkan PDF dari MHTML](#csharp-mhtml-to-pdf)
- [C# Buat PDF dari MHTML](#csharp-mhtml-to-pdf)
- [Konverter C# MHTML ke PDF](#csharp-mhtml-to-pdf)

_Format_: **WebPage**
- [Kode C# WebPage ke PDF](#csharp-webpage-to-pdf)
- [API C# WebPage ke PDF](#csharp-webpage-to-pdf)
- [C# WebPage ke PDF Secara Pemrograman](#csharp-webpage-to-pdf)
- [C# WebPage ke PDF Secara Pemrograman](#csharp-webpage-to-pdf)
- [C# Perpustakaan WebPage ke PDF](#csharp-webpage-to-pdf)
- [C# Simpan WebPage sebagai PDF](#csharp-webpage-to-pdf)
- [C# Hasilkan PDF dari WebPage](#csharp-webpage-to-pdf)
- [C# Buat PDF dari WebPage](#csharp-webpage-to-pdf)
- [C# Pengonversi WebPage ke PDF](#csharp-webpage-to-pdf)
