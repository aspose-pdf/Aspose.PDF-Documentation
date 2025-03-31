---
title: Mengonversi PDF ke PowerPoint di .NET
linktitle: Mengonversi PDF ke PowerPoint
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 30
url: /id/net/convert-pdf-to-powerpoint/
lastmod: "2021-11-01"
description: Aspose.PDF memungkinkan Anda untuk mengonversi PDF ke format PPT (PowerPoint) menggunakan .NET. Salah satu cara adalah dengan mengonversi PDF ke PPTX dengan Slides sebagai Gambar.
lastmod: "2021-10-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Convert PDF to PowerPoint in .NET",
    "alternativeHeadline": "Convert PDF Documents to PowerPoint Presentations Efficiently in C#",
    "abstract": "Aspose.PDF for .NET memperkenalkan fitur kuat yang memungkinkan konversi dokumen PDF ke format PowerPoint (PPTX) secara mulus, memungkinkan setiap halaman PDF berubah menjadi slide yang berbeda. Dengan opsi untuk merender teks sebagai yang dapat dipilih atau sebagai gambar, pengguna dapat dengan mudah menyesuaikan presentasi mereka sambil melacak kemajuan konversi dengan efisien. Optimalkan alur kerja dokumen Anda dengan memanfaatkan fungsionalitas inovatif ini untuk meningkatkan produktivitas",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1174",
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
    "url": "/net/convert-pdf-to-powerpoint/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/convert-pdf-to-powerpoint/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF dapat melakukan tidak hanya tugas yang sederhana dan mudah tetapi juga menangani tujuan yang lebih kompleks. Periksa bagian berikut untuk pengguna dan pengembang tingkat lanjut."
}
</script>

## Ikhtisar

Artikel ini menjelaskan bagaimana **mengonversi PDF ke PowerPoint menggunakan C#**. Ini mencakup topik-topik berikut.

_Format_: **PPTX**
- [C# PDF ke PPTX](#csharp-pdf-to-pptx)
- [C# Mengonversi PDF ke PPTX](#csharp-pdf-to-pptx)
- [C# Cara mengonversi file PDF ke PPTX](#csharp-pdf-to-pptx)

_Format_: **PowerPoint**
- [C# PDF ke PowerPoint](#csharp-pdf-to-powerpoint)
- [C# Mengonversi PDF ke PowerPoint](#csharp-pdf-to-powerpoint)
- [C# Cara mengonversi file PDF ke PowerPoint](#csharp-pdf-to-powerpoint)

Potongan kode berikut juga bekerja dengan pustaka [Aspose.PDF.Drawing](/pdf/id/net/drawing/).

## Konversi C# PDF ke PowerPoint dan PPTX

**Aspose.PDF for .NET** memungkinkan Anda melacak kemajuan konversi PDF ke PPTX.

Kami memiliki API bernama Aspose.Slides yang menawarkan fitur untuk membuat serta memanipulasi presentasi PPT/PPTX. API ini juga menyediakan fitur untuk mengonversi file PPT/PPTX ke format PDF. Baru-baru ini kami menerima permintaan dari banyak pelanggan kami untuk mendukung kemampuan transformasi PDF ke format PPTX. Mulai rilis Aspose.PDF for .NET 10.3.0, kami telah memperkenalkan fitur untuk mengubah dokumen PDF ke format PPTX. Selama konversi ini, halaman-halaman individu dari file PDF diubah menjadi slide terpisah dalam file PPTX.

Selama konversi PDF ke <abbr title="Microsoft PowerPoint 2007 XML Presentation">PPTX</abbr>, teks dirender sebagai Teks di mana Anda dapat memilih/memperbaruinya. Harap dicatat bahwa untuk mengonversi file PDF ke format PPTX, Aspose.PDF menyediakan kelas bernama [`PptxSaveOptions`](https://reference.aspose.com/pdf/id/net/aspose.pdf/pptxsaveoptions). Sebuah objek dari kelas PptxSaveOptions diteruskan sebagai argumen kedua ke [`Document.Save(..) method`](https://reference.aspose.com/pdf/id/net/aspose.pdf/document/methods/save). Potongan kode berikut menunjukkan proses untuk mengonversi file PDF ke format PPTX.

## Konversi sederhana PDF ke PowerPoint menggunakan C# dan Aspose.PDF .NET

Untuk mengonversi PDF ke PPTX, Aspose.PDF for .NET menyarankan untuk menggunakan langkah-langkah kode berikut.

<a name="csharp-pdf-to-powerpoint"><strong>Langkah: Mengonversi PDF ke PowerPoint di C#</strong></a> | <a name="csharp-pdf-to-pptx"><strong>Langkah: Mengonversi PDF ke PPTX di C#</strong></a>

1. Buat instance dari kelas [Document](https://reference.aspose.com/pdf/id/net/aspose.pdf/document).
2. Buat instance dari kelas [PptxSaveOptions](https://reference.aspose.com/pdf/id/net/aspose.pdf/pptxsaveoptions).
3. Gunakan metode **Save** dari objek **Document** untuk menyimpan PDF sebagai PPTX.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFToPPTX()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Instantiate PptxSaveOptions object
        var saveOptions = new Aspose.Pdf.PptxSaveOptions();

        // Save the file in PPTX format
        document.Save(dataDir + "PDFToPPT_out.pptx", saveOptions);
    }
}
```

## Mengonversi PDF ke PPTX dengan Slides sebagai Gambar

{{% alert color="success" %}}
**Cobalah untuk mengonversi PDF ke PowerPoint secara online**

Aspose.PDF for .NET mempersembahkan aplikasi gratis online ["PDF ke PPTX"](https://products.aspose.app/pdf/conversion/pdf-to-pptx), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitasnya.

[![Aspose.PDF Konversi PDF ke PPTX dengan Aplikasi Gratis](pdf_to_pptx.png)](https://products.aspose.app/pdf/conversion/pdf-to-pptx)
{{% /alert %}}

Jika Anda perlu mengonversi PDF yang dapat dicari ke PPTX sebagai gambar alih-alih teks yang dapat dipilih, Aspose.PDF menyediakan fitur tersebut melalui kelas [Aspose.Pdf.PptxSaveOptions](https://reference.aspose.com/pdf/id/net/aspose.pdf/pptxsaveoptions). Untuk mencapai ini, atur properti [SlidesAsImages](https://reference.aspose.com/pdf/id/net/aspose.pdf/pptxsaveoptions/properties/slidesasimages) dari kelas [PptxSaveOptios](https://reference.aspose.com/pdf/id/net/aspose.pdf/pptxsaveoptions) ke 'true' seperti yang ditunjukkan dalam contoh kode berikut.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFToPPTWithSlidesAsImages()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Instantiate PptxSaveOptions object
        var saveOptions = new Aspose.Pdf.PptxSaveOptions
        {
            SlidesAsImages = true
        };

        // Save the file in PPTX format with slides as images
        document.Save(dataDir + "PDFToPPT_out.pptx", saveOptions);
    }
}
```

## Detail Kemajuan Konversi PPTX

Aspose.PDF for .NET memungkinkan Anda melacak kemajuan konversi PDF ke PPTX. Kelas [Aspose.Pdf.PptxSaveOptions](https://reference.aspose.com/pdf/id/net/aspose.pdf/pptxsaveoptions) menyediakan properti [CustomProgressHandler](https://reference.aspose.com/pdf/id/net/aspose.pdf/pptxsaveoptions/properties/customprogresshandler) yang dapat ditentukan ke metode kustom untuk melacak kemajuan konversi seperti yang ditunjukkan dalam contoh kode berikut.

```csharp
 // For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFToPPTWithCustomProgressHandler()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {

        // Instantiate PptxSaveOptions object
        var saveOptions = new Aspose.Pdf.PptxSaveOptions();

        // Specify custom progress handler
        saveOptions.CustomProgressHandler = ShowProgressOnConsole;

        // Save the file in PPTX format with progress tracking
        document.Save(dataDir + "PDFToPPTWithProgressTracking_out.pptx", saveOptions);
    }
}

 // Define the method to handle progress events and display them on the console
private static void ShowProgressOnConsole(Aspose.Pdf.UnifiedSaveOptions.ProgressEventHandlerInfo eventInfo)
{
    switch (eventInfo.EventType)
    {
        case Aspose.Pdf.ProgressEventType.TotalProgress:
            // Display overall progress of the conversion
            Console.WriteLine($"{DateTime.Now.TimeOfDay}  - Conversion progress: {eventInfo.Value}%.");
            break;

        case Aspose.Pdf.ProgressEventType.ResultPageCreated:
            // Display progress of the page layout creation
            Console.WriteLine($"{DateTime.Now.TimeOfDay}  - Result page {eventInfo.Value} of {eventInfo.MaxValue} layout created.");
            break;

        case Aspose.Pdf.ProgressEventType.ResultPageSaved:
            // Display progress of the page being exported
            Console.WriteLine($"{DateTime.Now.TimeOfDay}  - Result page {eventInfo.Value} of {eventInfo.MaxValue} exported.");
            break;

        case Aspose.Pdf.ProgressEventType.SourcePageAnalysed:
            // Display progress of the source page analysis
            Console.WriteLine($"{DateTime.Now.TimeOfDay}  - Source page {eventInfo.Value} of {eventInfo.MaxValue} analyzed.");
            break;

        default:
            break;
    }
}
```

## Lihat Juga 

Artikel ini juga mencakup topik-topik berikut. Kode-kodenya sama seperti di atas.

_Format_: **PowerPoint**
- [C# Kode PDF ke PowerPoint](#csharp-pdf-to-powerpoint)
- [C# API PDF ke PowerPoint](#csharp-pdf-to-powerpoint)
- [C# PDF ke PowerPoint Secara Programatis](#csharp-pdf-to-powerpoint)
- [C# Perpustakaan PDF ke PowerPoint](#csharp-pdf-to-powerpoint)
- [C# Simpan PDF sebagai PowerPoint](#csharp-pdf-to-powerpoint)
- [C# Hasilkan PowerPoint dari PDF](#csharp-pdf-to-powerpoint)
- [C# Buat PowerPoint dari PDF](#csharp-pdf-to-powerpoint)
- [C# Konverter PDF ke PowerPoint](#csharp-pdf-to-powerpoint)

_Format_: **PPTX**
- [C# Kode PDF ke PPTX](#csharp-pdf-to-pptx)
- [C# API PDF ke PPTX](#csharp-pdf-to-pptx)
- [C# PDF ke PPTX Secara Programatis](#csharp-pdf-to-pptx)
- [C# Perpustakaan PDF ke PPTX](#csharp-pdf-to-pptx)
- [C# Simpan PDF sebagai PPTX](#csharp-pdf-to-pptx)
- [C# Hasilkan PPTX dari PDF](#csharp-pdf-to-pptx)
- [C# Buat PPTX dari PDF](#csharp-pdf-to-pptx)
- [C# Konverter PDF ke PPTX](#csharp-pdf-to-pptx)