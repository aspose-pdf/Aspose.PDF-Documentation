---
title: Mengonversi PDF ke HTML di .NET
linktitle: Mengonversi PDF ke format HTML
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 50
url: /id/net/convert-pdf-to-html/
lastmod: "2021-11-01"
description: Topik ini menunjukkan cara mengonversi file PDF ke format HTML dengan pustaka Aspose.PDF C#.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Convert PDF to HTML in .NET",
    "alternativeHeadline": "Convert PDF Files to HTML with Simplified Options in C#",
    "abstract": "Memperkenalkan fitur baru yang kuat di Aspose.PDF for .NET yang memungkinkan konversi dokumen PDF ke format HTML secara mulus. Fungsionalitas ini mendukung output multi-halaman, manajemen gambar SVG, dan opsi untuk rendering teks transparan, memungkinkan pengembang untuk dengan mudah mengubah PDF menjadi konten siap web hanya dengan beberapa baris kode C#",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1368",
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
    "url": "/net/convert-pdf-to-html/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/convert-pdf-to-html/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF dapat melakukan tidak hanya tugas sederhana dan mudah tetapi juga menangani tujuan yang lebih kompleks. Periksa bagian berikut untuk pengguna dan pengembang tingkat lanjut."
}
</script>

## Ikhtisar

Artikel ini menjelaskan cara **mengonversi PDF ke HTML menggunakan C#**. Ini mencakup topik-topik berikut.

_Format_: **HTML**
- [C# PDF ke HTML](#csharp-pdf-to-html)
- [C# Mengonversi PDF ke HTML](#csharp-pdf-to-html)
- [C# Cara mengonversi file PDF ke HTML](#csharp-pdf-to-html)

Cuplikan kode berikut juga bekerja dengan pustaka [Aspose.PDF.Drawing](/pdf/id/net/drawing/).

## Mengonversi PDF ke HTML

**Aspose.PDF for .NET** menyediakan banyak fitur untuk mengonversi berbagai format file menjadi dokumen PDF dan mengonversi file PDF menjadi berbagai format output. Artikel ini membahas cara mengonversi file PDF menjadi <abbr title="HyperText Markup Language">HTML</abbr>. Aspose.PDF for .NET menyediakan kemampuan untuk mengonversi file HTML menjadi format PDF menggunakan pendekatan InLineHtml. Kami telah menerima banyak permintaan untuk fungsionalitas yang mengonversi file PDF menjadi format HTML dan telah menyediakan fitur ini. Harap dicatat bahwa fitur ini juga mendukung XHTML 1.0.

**Aspose.PDF for .NET** mendukung fitur untuk mengonversi file PDF menjadi HTML. Tugas utama yang dapat Anda capai dengan pustaka Aspose.PDF tercantum:

- Mengonversi PDF ke HTML.
- Memisahkan Output ke HTML Multi-halaman.
- Menentukan Folder untuk Menyimpan File SVG.
- Mengompresi Gambar SVG Selama Konversi.
- Menyimpan gambar sebagai latar belakang PNG.
- Menentukan Folder Gambar.
- Membuat File Berikutnya dengan Konten Body Saja.
- Rendering Teks Transparan.
- Rendering lapisan dokumen PDF.

{{% alert color="success" %}}
**Cobalah mengonversi PDF ke HTML secara online**

Aspose.PDF for .NET mempersembahkan aplikasi gratis online ["PDF ke HTML"](https://products.aspose.app/pdf/conversion/pdf-to-html), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitasnya.

[![Aspose.PDF Konversi PDF ke HTML dengan Aplikasi Gratis](pdf_to_html.png)](https://products.aspose.app/pdf/conversion/pdf-to-html)
{{% /alert %}}

Aspose.PDF for .NET menyediakan kode dua baris untuk mengubah file PDF sumber menjadi HTML. Enumerasi [`SaveFormat`](https://reference.aspose.com/pdf/net/aspose.pdf/saveformat) berisi nilai Html yang memungkinkan Anda menyimpan file sumber ke HTML. Cuplikan kode berikut menunjukkan proses mengonversi file PDF menjadi HTML.

<a name="csharp-pdf-to-html"><strong>Langkah: Mengonversi PDF ke HTML di C#</strong></a>

1. Buat instance objek [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document/) dengan dokumen PDF sumber.
2. Simpan ke format **SaveFormat.Html** dengan memanggil metode **Document.Save()**.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFtoHTML()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDFToHTML.pdf"))
    {
        // Save the output HTML
        document.Save(dataDir + "output_out.html", Aspose.Pdf.SaveFormat.Html);
    }
}
```

### Memisahkan Output ke HTML Multi-halaman

Saat mengonversi file PDF besar dengan beberapa halaman ke format HTML, output muncul sebagai satu halaman HTML. Ini bisa menjadi sangat panjang. Untuk mengontrol ukuran halaman, dimungkinkan untuk memisahkan output menjadi beberapa halaman selama konversi PDF ke HTML. Silakan coba menggunakan cuplikan kode berikut.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFtoMultiPageHTML()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDFToHTML.pdf"))
    {
        // Instantiate HTML SaveOptions object
        var htmlOptions = new Aspose.Pdf.HtmlSaveOptions
        {
            // Specify to split the output into multiple pages
            SplitIntoPages = true
        };

        // Save the output HTML
        document.Save(dataDir + "MultiPageHTML_out.html", htmlOptions);
    }
}
```

### Menentukan Folder untuk Menyimpan File SVG

Selama konversi PDF ke HTML, dimungkinkan untuk menentukan folder tempat gambar SVG harus disimpan. Gunakan kelas [`HtmlSaveOption`](https://reference.aspose.com/pdf/net/aspose.pdf/htmlsaveoptions) properti [`SpecialFolderForSvgImages`](https://reference.aspose.com/pdf/net/aspose.pdf/htmlsaveoptions/fields/specialfolderforsvgimages) untuk menentukan direktori gambar SVG khusus. Properti ini mendapatkan atau mengatur jalur ke direktori tempat gambar SVG harus disimpan saat ditemukan selama konversi. Jika parameter kosong atau null, maka file SVG apa pun disimpan bersama dengan file gambar lainnya.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SavePDFtoHTMLWithSVG()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDFToHTML.pdf"))
    {
        // Instantiate HTML save options object
        var newOptions = new Aspose.Pdf.HtmlSaveOptions
        {
            // Specify the folder where SVG images are saved during PDF to HTML conversion
            SpecialFolderForSvgImages = dataDir
        };

        // Save the output HTML
        document.Save(dataDir + "SaveSVGFiles_out.html", newOptions);
    }
}
```

### Mengompresi Gambar SVG Selama Konversi

Untuk mengompresi gambar SVG selama konversi PDF ke HTML, silakan coba menggunakan kode berikut:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SavePDFtoCompressedHTMLWithSVG()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDFToHTML.pdf"))
    {
        // Create HtmlSaveOptions with tested feature
        var newOptions = new Aspose.Pdf.HtmlSaveOptions
        {
            // Compress the SVG images if there are any
            CompressSvgGraphicsIfAny = true
        };

        // Save the output HTML
        document.Save(dataDir + "CompressedSVGHTML_out.html", newOptions);
    }
}
```

### Menyimpan gambar sebagai latar belakang PNG

Format output default untuk menyimpan gambar adalah SVG. Selama konversi, beberapa gambar dari PDF diubah menjadi gambar vektor SVG. Ini bisa lambat. Sebagai gantinya, gambar dapat diubah menjadi satu file latar belakang PNG untuk setiap halaman.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void PdfToHtmlSaveImagesAsPngBackground()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion_PDFToHTMLFormat();
           
    // Create HtmlSaveOption with tested feature
    var htmlSaveOptions = new HtmlSaveOptions();
           
    // Option to save images in PNG format as background for each page.
    htmlSaveOptions.RasterImagesSavingMode = HtmlSaveOptions.RasterImagesSavingModes.AsEmbeddedPartsOfPngPageBackground;

    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
       document.Save(dataDir + "imagesAsPngBackground_out.html", htmlSaveOptions);         
    }
}
```

### Menentukan Folder Gambar

Kita juga dapat menentukan folder tempat gambar akan disimpan selama konversi PDF ke HTML:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SavePDFtoHTMLWithSeparateImageFolder()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDFToHTML.pdf"))
    {
        // Create HtmlSaveOptions with tested feature
        var newOptions = new Aspose.Pdf.HtmlSaveOptions
        {
            // Specify the separate folder to save images
            SpecialFolderForAllImages = dataDir
        };

        // Save the output HTML
        document.Save(dataDir + "HTMLWithSeparateImageFolder_out.html", newOptions);
    }
}
```

### Membuat File Berikutnya dengan Konten Body Saja

Baru-baru ini, kami diminta untuk memperkenalkan fitur di mana file PDF diubah menjadi HTML dan pengguna dapat mendapatkan hanya konten dari tag `<body>` untuk setiap halaman. Ini akan menghasilkan satu file dengan CSS, detail `<html>`, `<head>` dan semua halaman di file lain hanya dengan konten `<body>`.

Untuk memenuhi persyaratan ini, properti baru, HtmlMarkupGenerationMode, diperkenalkan ke kelas HtmlSaveOptions.

Dengan cuplikan kode sederhana berikut, Anda dapat memisahkan output HTML menjadi halaman. Di halaman output, semua objek HTML harus pergi persis ke tempat mereka sekarang (proses font dan output, pembuatan CSS dan output, pembuatan gambar dan output), kecuali bahwa output HTML akan berisi konten yang saat ini ditempatkan di dalam tag (sekarang tag “body” akan dihilangkan). Namun, saat menggunakan pendekatan ini, tautan ke CSS adalah tanggung jawab kode Anda, karena hal-hal seperti akan dihapus. Untuk tujuan ini, Anda dapat membaca CSS melalui File.ReadAllText() dan mengirimkannya melalui AJAX ke halaman web di mana itu akan diterapkan oleh jQuery.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFToHTMLWithBodyContent()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDFToHTML.pdf"))
    {
        // Initialize HtmlSaveOptions
        var options = new Aspose.Pdf.HtmlSaveOptions
        {
            // Set HtmlMarkupGenerationMode to generate only body content
            HtmlMarkupGenerationMode =
                Aspose.Pdf.HtmlSaveOptions.HtmlMarkupGenerationModes.WriteOnlyBodyContent,

            // Specify to split the output into multiple pages
            SplitIntoPages = true
        };

        // Save the output HTML
        document.Save(dataDir + "CreateSubsequentFiles_out.html", options);
    }
}
```

### Rendering Teks Transparan

Jika file PDF sumber/input mengandung teks transparan yang dibayangi oleh gambar latar depan, maka mungkin ada masalah rendering teks. Jadi untuk mengatasi skenario seperti itu, properti SaveShadowedTextsAsTransparentTexts dan SaveTransparentTexts dapat digunakan.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFToHTMLWithTransparentTextRendering()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDFToHTML.pdf"))
    {
        // Initialize HtmlSaveOptions
        var htmlOptions = new Aspose.Pdf.HtmlSaveOptions
        {
            // Enable transparent text rendering
            SaveShadowedTextsAsTransparentTexts = true,
            SaveTransparentTexts = true
        };

        // Save the output HTML
        document.Save(dataDir + "TransparentTextRendering_out.html", htmlOptions);
    }
}
```

### Rendering lapisan dokumen PDF

Kita dapat merender lapisan dokumen PDF dalam elemen tipe lapisan terpisah selama konversi PDF ke HTML:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFToHTMLWithLayersRendering()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDFToHTML.pdf"))
    {
        // Instantiate HTML SaveOptions object
        var htmlOptions = new Aspose.Pdf.HtmlSaveOptions
        {
            // Enable rendering of PDF document layers separately in the output HTML
            ConvertMarkedContentToLayers = true
        };

        // Save the output HTML
        document.Save(dataDir + "LayersRendering_out.html", htmlOptions);
    }
}
```

## Lihat Juga 

Artikel ini juga mencakup topik-topik berikut. Kode sama seperti di atas.

_Format_: **HTML**
- [C# Kode PDF ke HTML](#csharp-pdf-to-html)
- [C# API PDF ke HTML](#csharp-pdf-to-html)
- [C# PDF ke HTML Secara Programatis](#csharp-pdf-to-html)
- [C# Pustaka PDF ke HTML](#csharp-pdf-to-html)
- [C# Simpan PDF sebagai HTML](#csharp-pdf-to-html)
- [C# Hasilkan HTML dari PDF](#csharp-pdf-to-html)
- [C# Buat HTML dari PDF](#csharp-pdf-to-html)
- [C# Pengonversi PDF ke HTML](#csharp-pdf-to-html)