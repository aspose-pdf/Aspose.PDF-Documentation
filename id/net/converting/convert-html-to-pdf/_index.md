---
title: Mengonversi HTML ke PDF di .NET
linktitle: Mengonversi file HTML ke PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 40
url: /id/net/convert-html-to-pdf/
lastmod: "2021-11-01"
description: Topik ini menunjukkan cara mengonversi HTML ke PDF dan MHTML ke PDF menggunakan Aspose.PDF.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Convert HTML to PDF in .NET",
    "alternativeHeadline": "Convert HTML and MHTML to PDF with C#",
    "abstract": "Fitur konversi di Aspose.PDF for .NET memungkinkan transformasi dokumen HTML dan MHTML menjadi file PDF berkualitas tinggi secara mulus. Dengan opsi kustomisasi yang canggih, pengguna dapat mengontrol penyematan font, kueri media, dan manajemen sumber daya eksternal sambil memastikan bahwa halaman web atau file HTML lokal dirender dengan akurat ke dalam format PDF dengan fleksibilitas yang disesuaikan dengan kebutuhan spesifik mereka.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1889",
    "proficiencyLevel": "Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF for .NET",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "sales",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "sales",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "sales",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/net/convert-html-to-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/convert-html-to-pdf/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF dapat melakukan tidak hanya tugas yang sederhana dan mudah tetapi juga menangani tujuan yang lebih kompleks. Periksa bagian berikut untuk pengguna dan pengembang tingkat lanjut."
}
</script>

## Ikhtisar 

Artikel ini menjelaskan cara **mengonversi HTML ke PDF menggunakan C#**. Ini mencakup topik berikut.

Potongan kode berikut juga bekerja dengan pustaka [Aspose.PDF.Drawing](/pdf/id/net/drawing/).

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

## Konversi C# HTML ke PDF

**Aspose.PDF for .NET** adalah API manipulasi PDF yang memungkinkan Anda mengonversi dokumen HTML yang ada ke PDF secara mulus. Proses mengonversi HTML ke PDF dapat disesuaikan dengan fleksibel.

## Mengonversi HTML ke PDF

Contoh kode C# berikut menunjukkan cara mengonversi dokumen HTML ke PDF.

<a name="csharp-html-to-pdf"><strong>Langkah: Mengonversi HTML ke PDF di C#</strong></a>

1. Buat instance dari kelas [HtmlLoadOptions](https://reference.aspose.com/pdf/id/net/aspose.pdf/htmlloadoptions/).
2. Inisialisasi objek [Document](https://reference.aspose.com/pdf/id/net/aspose.pdf/document/).
3. Simpan dokumen PDF keluaran dengan memanggil metode **Document.Save()**.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertHTMLtoPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Load the HTML file into a document using HtmlLoadOptions
    var options = new Aspose.Pdf.HtmlLoadOptions();

    // Open HTML document
    using (var document = new Aspose.Pdf.Document(dataDir + "test.html", options))
    {
        // Save PDF document
        document.Save(dataDir + "ConvertHTMLtoPDF_out.pdf");
    }
}
```

{{% alert color="success" %}}
**Cobalah untuk mengonversi HTML ke PDF secara online**

Aspose mempersembahkan aplikasi gratis online ["HTML ke PDF"](https://products.aspose.app/html/en/conversion/html-to-pdf), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitasnya.

[![Aspose.PDF Konversi HTML ke PDF menggunakan Aplikasi Gratis](html.png)](https://products.aspose.app/html/en/conversion/html-to-pdf)
{{% /alert %}}

## Konversi lanjutan dari HTML ke PDF

Mesin Konversi HTML memiliki beberapa opsi yang memungkinkan kita mengontrol proses konversi.

### Dukungan Kueri Media

Kueri media adalah teknik populer untuk menyampaikan lembar gaya yang disesuaikan ke perangkat yang berbeda. Kita dapat mengatur jenis perangkat menggunakan properti [`HtmlMediaType`](https://reference.aspose.com/pdf/id/net/aspose.pdf/htmlloadoptions/properties/htmlmediatype).

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertHTMLtoPDFAdvancedMediaType()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Load the HTML file into a document using HtmlLoadOptions with Print media type
    var options = new HtmlLoadOptions
    {
        // Set Print or Screen mode
        HtmlMediaType = Aspose.Pdf.HtmlMediaType.Print
    };

    // Open HTML document
    using (var document = new Aspose.Pdf.Document(dataDir + "test.html", options))
    {
        // Save PDF document
        document.Save(dataDir + "ConvertHTMLtoPDFAdvancedMediaType_out.pdf");
    }
}
```

### Mengaktifkan (menonaktifkan) penyematan font

Halaman HTML sering menggunakan font (misalnya, font dari folder lokal, Google Fonts, dll). Kita juga dapat mengontrol penyematan font dalam dokumen menggunakan properti [`IsEmbedFonts`](https://reference.aspose.com/pdf/id/net/aspose.pdf/htmlloadoptions/properties/isembedfonts).

```csharp
 // For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
 private static void ConvertHTMLtoPDFAdvancedEmbedFonts()
 {
     // The path to the documents directory
     var dataDir = RunExamples.GetDataDir_AsposePdf();

     // Load the HTML file into a document using HtmlLoadOptions with the font embedding option set
     var options = new Aspose.Pdf.HtmlLoadOptions
     {
         // Disable font embedding
         IsEmbedFonts = false
     };

     // Open HTML document
     using (var document = new Aspose.Pdf.Document(dataDir + "test_fonts.html", options))
     {
         // Save PDF document
         document.Save(dataDir + "ConvertHTMLtoPDFAdvanced_EmbedFonts_out.pdf");
     }
 }
```

### Mengelola pemuatan sumber daya eksternal

Mesin Konversi menyediakan mekanisme yang memungkinkan Anda mengontrol pemuatan sumber daya tertentu yang terkait dengan dokumen HTML. Kelas [`HtmlLoadOptions`](https://reference.aspose.com/pdf/id/net/aspose.pdf/htmlloadoptions) memiliki properti [`CustomLoaderOfExternalResources`](https://reference.aspose.com/pdf/id/net/aspose.pdf/htmlloadoptions/fields/customloaderofexternalresources) di mana kita dapat mendefinisikan perilaku pemuat sumber daya. Misalkan kita perlu mengganti semua gambar PNG dengan gambar tunggal `test.jpg` dan mengganti URL eksternal menjadi internal untuk sumber daya lainnya. Untuk melakukan ini, kita dapat mendefinisikan pemuat kustom `SamePictureLoader` dan mengarahkan [`CustomLoaderOfExternalResources`](https://reference.aspose.com/pdf/id/net/aspose.pdf/htmlloadoptions/fields/customloaderofexternalresources) ke nama ini.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertHTMLtoPDFAdvanced_DummyImage()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Load the HTML file into a document with a custom resource loader for external images
    var options = new Aspose.Pdf.HtmlLoadOptions
    {
        CustomLoaderOfExternalResources = SamePictureLoader
    };

    // Open HTML document
    using (var document = new Aspose.Pdf.Document(dataDir + "test.html", options))
    {
        // Save PDF document
        document.Save(dataDir + "html_test.pdf");
    }
}

private static Aspose.Pdf.LoadOptions.ResourceLoadingResult SamePictureLoader(string resourceURI)
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();
    Aspose.Pdf.LoadOptions.ResourceLoadingResult result;

    if (resourceURI.EndsWith(".png"))
    {
        byte[] resultBytes = File.ReadAllBytes(dataDir + "test.jpg");
        result = new Aspose.Pdf.LoadOptions.ResourceLoadingResult(resultBytes)
        {
            // Set MIME Type
            MIMETypeIfKnown = "image/jpeg"
        };
    }
    else
    {
        result = new Aspose.Pdf.LoadOptions.ResourceLoadingResult(GetContentFromUrl(resourceURI));
    }
    return result;
}

private static byte[] GetContentFromUrl(string url)
{
    var httpClient = new System.Net.Http.HttpClient();
    return httpClient.GetByteArrayAsync(url).GetAwaiter().GetResult();
}
```

## Mengonversi Halaman Web ke PDF

Mengonversi halaman web sedikit berbeda dari mengonversi dokumen HTML lokal. Untuk mengonversi konten halaman Web ke format PDF, kita dapat terlebih dahulu mengambil konten halaman HTML menggunakan instance HttpClient, membuat objek Stream, meneruskan konten ke objek Document, dan merender keluaran dalam format PDF.

Saat mengonversi halaman web yang dihosting di server web ke PDF:

<a name="csharp-webpage-to-pdf"><strong>Langkah: Mengonversi WebPage ke PDF di C#</strong></a>

1. Baca konten halaman menggunakan objek HttpClient.
1. Buat objek [HtmlLoadOptions](https://reference.aspose.com/pdf/id/net/aspose.pdf/htmlloadoptions) dan atur URL dasar.
1. Inisialisasi objek Document sambil meneruskan objek stream.
1. Opsional, atur ukuran halaman dan/atau orientasi.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertHTMLtoPDFAdvanced_WebPage()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    const string url = "https://en.wikipedia.org/wiki/Aspose_API";

    // Set page size A3 and Landscape orientation;   
    var options = new Aspose.Pdf.HtmlLoadOptions(url)
    {
        PageInfo =
        {
            Width = 842,
            Height = 1191,
            IsLandscape = true
        }
    };

    // Load the web page content as a stream and create a PDF document
    using (var document = new Aspose.Pdf.Document(GetContentFromUrlAsStream(url), options))
    {
        // Save PDF document
        document.Save(dataDir + "html_test.pdf");
    }
}

private static Stream GetContentFromUrlAsStream(string url, System.Net.ICredentials credentials = null)
{
    using (var handler = new System.Net.Http.HttpClientHandler { Credentials = credentials })
    using (var httpClient = new System.Net.Http.HttpClient(handler))
    {
        return httpClient.GetStreamAsync(url).GetAwaiter().GetResult();
    }
}
```

### Berikan kredensial untuk konversi Halaman Web ke PDF

Terkadang kita perlu melakukan konversi file HTML yang memerlukan otentikasi dan hak akses, sehingga hanya pengguna yang sah yang dapat mengambil konten halaman. Ini juga mencakup skenario di mana beberapa sumber daya/data yang dirujuk di dalam HTML diambil dari server eksternal yang memerlukan otentikasi dan untuk memenuhi kebutuhan ini, properti [`ExternalResourcesCredentials`](https://reference.aspose.com/pdf/id/net/aspose.pdf/htmlloadoptions/fields/externalresourcescredentials) ditambahkan ke kelas [`HtmlLoadOptions`](https://reference.aspose.com/pdf/id/net/aspose.pdf/htmlloadoptions). Potongan kode berikut menunjukkan langkah-langkah untuk meneruskan kredensial untuk meminta HTML & sumber daya terkait saat mengonversi file HTML ke PDF.

```csharp
 // For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
 private static void ConvertHTMLtoPDFAdvancedAuthorized()
 {
     // The path to the documents directory
     var dataDir = RunExamples.GetDataDir_AsposePdf();

     const string url = "http://httpbin.org/basic-auth/user1/password1";
     var credentials = new System.Net.NetworkCredential("user1", "password1");

     var options = new Aspose.Pdf.HtmlLoadOptions(url)
     {
         ExternalResourcesCredentials = credentials
     };

     using (var document = new Aspose.Pdf.Document(GetContentFromUrlAsStream(url, credentials), options))
     {
         // Save PDF document
         document.Save(dataDir + "HtmlTest_out.pdf");
     }
 }

private static Stream GetContentFromUrlAsStream(string url, System.Net.ICredentials credentials = null)
{
    using (var handler = new System.Net.Http.HttpClientHandler { Credentials = credentials })
    using (var httpClient = new System.Net.Http.HttpClient(handler))
    {
        return httpClient.GetStreamAsync(url).GetAwaiter().GetResult();
    }
}
```

### Render semua konten HTML dalam satu Halaman

Aspose.PDF for .NET memberikan kemampuan untuk merender semua konten dalam satu halaman saat mengonversi file HTML ke format PDF. Misalnya, jika Anda memiliki beberapa konten HTML yang ukuran keluarnya lebih besar dari satu halaman, Anda dapat menggunakan opsi untuk merender data keluaran ke dalam satu halaman PDF. Untuk menggunakan opsi ini, kelas HtmlLoadOptions diperluas dengan flag IsRenderToSinglePage. Potongan kode di bawah ini menunjukkan cara menggunakan fungsionalitas ini.

```csharp
 // For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
 private static void ConvertHTMLtoPDFAdvancedSinglePageRendering()
 {
     // The path to the documents directory
     var dataDir = RunExamples.GetDataDir_AsposePdf();

     // Initialize HtmlLoadOptions
     var options = new Aspose.Pdf.HtmlLoadOptions
     {
         // Set Render to single page property
         IsRenderToSinglePage = true
     };

     // Open PDF document
     using (var document = new Aspose.Pdf.Document(dataDir + "HTMLToPDF.html", options))
     {
         // Save PDF document
         document.Save(dataDir + "RenderContentToSamePage_out.pdf");
     }
 }
```

### Render HTML dengan Data SVG

Aspose.PDF for .NET memberikan kemampuan untuk mengonversi halaman HTML menjadi dokumen PDF. Karena HTML memungkinkan penambahan elemen grafik SVG sebagai tag di halaman, Aspose.PDF juga mendukung konversi data semacam itu ke dalam file PDF yang dihasilkan. Potongan kode berikut menunjukkan cara mengonversi file HTML dengan tag grafik SVG menjadi Dokumen PDF Berlabel.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertHTMLtoPDFWithSVG()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Initialize HtmlLoadOptions
    var options = new Aspose.Pdf.HtmlLoadOptions(Path.GetDirectoryName(dataDir + "HTMLSVG.html"));

    // Initialize Document object
    using (var document = new Aspose.Pdf.Document(dataDir + "HTMLSVG.html", options))
    {
        // Save PDF document
        document.Save(dataDir + "RenderHTMLwithSVGData_out.pdf");
    }
}
```

## Mengonversi MHTML ke PDF 

{{% alert color="success" %}}
**Cobalah untuk mengonversi MHTML ke PDF secara online**

Aspose.PDF for .NET mempersembahkan aplikasi gratis online ["MHTML ke PDF"](https://products.aspose.app/pdf/conversion/mhtml-to-pdf), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitasnya.

[![Aspose.PDF Konversi MHTML ke PDF menggunakan Aplikasi Gratis](mhtml.png)](https://products.aspose.app/pdf/conversion/mhtml-to-pdf)
{{% /alert %}}

<abbr title="MIME encapsulation of aggregate HTML documents">MHTML</abbr>, singkatan dari MIME HTML, adalah format arsip halaman web yang digunakan untuk menggabungkan sumber daya yang biasanya diwakili oleh tautan eksternal (seperti gambar, animasi Flash, applet Java, dan file audio) dengan kode HTML menjadi satu file. Konten file MHTML dikodekan seolah-olah itu adalah pesan email HTML, menggunakan tipe MIME multipart/related. Aspose.PDF for .NET dapat mengonversi file HTML ke format PDF dan dengan rilis Aspose.PDF for .NET 9.0.0, kami telah memperkenalkan fitur baru yang memungkinkan Anda mengonversi file MHTML ke format PDF. Potongan kode berikut menunjukkan cara mengonversi file MHTML ke format PDF dengan C#:

<a name="csharp-mhtml-to-pdf"><strong>Langkah: Mengonversi MHTML ke PDF di C#</strong></a>

1. Buat instance dari kelas [MhtLoadOptions](https://reference.aspose.com/pdf/id/net/aspose.pdf/mhtloadoptions/).
2. Inisialisasi objek [Document](https://reference.aspose.com/pdf/id/net/aspose.pdf/document/).
3. Simpan dokumen PDF keluaran dengan memanggil metode **Document.Save()**.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertMHTtoPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Initialize MhtLoadOptions with page setup
    var options = new Aspose.Pdf.MhtLoadOptions()
    {
        PageInfo = { Width = 842, Height = 1191, IsLandscape = true }
    };

    // Initialize Document object using the MHT file and options
    using (var document = new Aspose.Pdf.Document(dataDir + "fileformatinfo.mht", options))
    {
        // Save PDF document
        document.Save(dataDir + "MhtmlTest_out.pdf");
    }
}
```

## Lihat Juga 

Artikel ini juga mencakup topik-topik ini. Kode sama seperti di atas.

_Format_: **HTML**
- [C# Kode HTML ke PDF](#csharp-html-to-pdf)
- [C# API HTML ke PDF](#csharp-html-to-pdf)
- [C# HTML ke PDF Secara Programatis](#csharp-html-to-pdf)
- [C# Perpustakaan HTML ke PDF](#csharp-html-to-pdf)
- [C# Simpan HTML sebagai PDF](#csharp-html-to-pdf)
- [C# Hasilkan PDF dari HTML](#csharp-html-to-pdf)
- [C# Buat PDF dari HTML](#csharp-html-to-pdf)
- [C# Konverter HTML ke PDF](#csharp-html-to-pdf)

_Format_: **MHTML**
- [C# Kode MHTML ke PDF](#csharp-mhtml-to-pdf)
- [C# API MHTML ke PDF](#csharp-mhtml-to-pdf)
- [C# MHTML ke PDF Secara Programatis](#csharp-mhtml-to-pdf)
- [C# Perpustakaan MHTML ke PDF](#csharp-mhtml-to-pdf)
- [C# Simpan MHTML sebagai PDF](#csharp-mhtml-to-pdf)
- [C# Hasilkan PDF dari MHTML](#csharp-mhtml-to-pdf)
- [C# Buat PDF dari MHTML](#csharp-mhtml-to-pdf)
- [C# Konverter MHTML ke PDF](#csharp-mhtml-to-pdf)

_Format_: **WebPage**
- [C# Kode WebPage ke PDF](#csharp-webpage-to-pdf)
- [C# API WebPage ke PDF](#csharp-webpage-to-pdf)
- [C# WebPage ke PDF Secara Programatis](#csharp-webpage-to-pdf)
- [C# Perpustakaan WebPage ke PDF](#csharp-webpage-to-pdf)
- [C# Simpan WebPage sebagai PDF](#csharp-webpage-to-pdf)
- [C# Hasilkan PDF dari WebPage](#csharp-webpage-to-pdf)
- [C# Buat PDF dari WebPage](#csharp-webpage-to-pdf)
- [C# Konverter WebPage ke PDF](#csharp-webpage-to-pdf)