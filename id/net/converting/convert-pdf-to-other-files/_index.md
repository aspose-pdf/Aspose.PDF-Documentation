---
title: Mengonversi PDF ke EPUB, LaTeX, Teks, XPS di C#
linktitle: Mengonversi PDF ke format lain
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 90
url: /id/net/convert-pdf-to-other-files/
lastmod: "2021-11-01"
description: Topik ini menunjukkan kepada Anda cara mengonversi file PDF ke format file lain seperti EPUB, LaTeX, Teks, XPS, dll menggunakan C# atau .NET.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Convert PDF to EPUB, LaTeX, Text, XPS in C#",
    "alternativeHeadline": "Add PDF format conversion to EPUB, LaTeX, Text, XPS in C#",
    "abstract": "Aspose.PDF for .NET memperkenalkan fitur kuat yang memungkinkan konversi file PDF ke berbagai format, termasuk EPUB, LaTeX, Teks, XPS, dan Markdown. Fungsionalitas ini meningkatkan aksesibilitas dan kegunaan dokumen dengan memungkinkan pengembang untuk dengan mudah mengintegrasikan konversi format file yang beragam ke dalam aplikasi C# mereka, sehingga memenuhi audiens yang lebih luas dan mengoptimalkan konten untuk berbagai platform",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1419",
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
    "url": "/net/convert-pdf-to-other-files/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/convert-pdf-to-other-files/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF dapat melakukan tidak hanya tugas sederhana dan mudah tetapi juga menangani tujuan yang lebih kompleks. Periksa bagian berikut untuk pengguna dan pengembang tingkat lanjut."
}
</script>

## Mengonversi PDF ke EPUB

{{% alert color="success" %}}
**Cobalah untuk mengonversi PDF ke EPUB secara online**

Aspose.PDF for .NET mempersembahkan aplikasi gratis online ["PDF to EPUB"](https://products.aspose.app/pdf/conversion/pdf-to-epub), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitasnya.

[![Aspose.PDF Konversi PDF ke EPUB dengan Aplikasi Gratis](pdf_to_epub.png)](https://products.aspose.app/pdf/conversion/pdf-to-epub)
{{% /alert %}}

**<abbr title="Electronic Publication">EPUB</abbr>** adalah standar e-book gratis dan terbuka dari International Digital Publishing Forum (IDPF). File memiliki ekstensi .epub.
EPUB dirancang untuk konten yang dapat mengalir, yang berarti bahwa pembaca EPUB dapat mengoptimalkan teks untuk perangkat tampilan tertentu. EPUB juga mendukung konten dengan tata letak tetap. Format ini dimaksudkan sebagai satu format yang dapat digunakan penerbit dan rumah konversi secara internal, serta untuk distribusi dan penjualan. Ini menggantikan standar Open eBook.

Potongan kode berikut juga bekerja dengan pustaka [Aspose.PDF.Drawing](/pdf/id/net/drawing/).

Aspose.PDF for .NET juga mendukung fitur untuk mengonversi dokumen PDF ke format EPUB. Aspose.PDF for .NET memiliki kelas bernama EpubSaveOptions yang dapat digunakan sebagai argumen kedua untuk metode [`Document.Save(..)`](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save/index), untuk menghasilkan file EPUB.
Silakan coba menggunakan potongan kode berikut untuk memenuhi kebutuhan ini dengan C#.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFtoEPUB()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDFToEPUB.pdf"))
    {
        // Instantiate Epub Save options
        EpubSaveOptions options = new EpubSaveOptions();
        // Specify the layout for contents
        options.ContentRecognitionMode = EpubSaveOptions.RecognitionMode.Flow;

        // Save ePUB document
        document.Save(dataDir + "PDFToEPUB_out.epub", options);
    }
}
```

## Mengonversi PDF ke LaTeX/TeX

**Aspose.PDF for .NET** mendukung mengonversi PDF ke LaTeX/TeX.
Format file LaTeX adalah format file teks dengan markup khusus dan digunakan dalam sistem persiapan dokumen berbasis TeX untuk penyetelan berkualitas tinggi.

{{% alert color="success" %}}
**Cobalah untuk mengonversi PDF ke LaTeX/TeX secara online**

Aspose.PDF for .NET mempersembahkan aplikasi gratis online ["PDF to LaTeX"](https://products.aspose.app/pdf/conversion/pdf-to-tex), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitasnya.

[![Aspose.PDF Konversi PDF ke LaTeX/TeX dengan Aplikasi Gratis](pdf_to_latex.png)](https://products.aspose.app/pdf/conversion/pdf-to-tex)
{{% /alert %}}

Untuk mengonversi file PDF ke TeX, Aspose.PDF memiliki kelas [LaTeXSaveOptions](https://reference.aspose.com/pdf/net/aspose.pdf/latexsaveoptions) yang menyediakan properti OutDirectoryPath untuk menyimpan gambar sementara selama proses konversi.

Potongan kode berikut menunjukkan proses mengonversi file PDF menjadi format TEX dengan C#.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFtoTeX()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDFToTeX.pdf"))
    {
        // Instantiate LaTex save option          
        LaTeXSaveOptions saveOptions = new LaTeXSaveOptions();

        // Specify the output directory
        string pathToOutputDirectory = dataDir;

        // Set the output directory path for save option object
        saveOptions.OutDirectoryPath = pathToOutputDirectory;

        // Save PDF document into LaTex format           
        document.Save(dataDir + "PDFToTeX_out.tex", saveOptions);
    }
}
```

## Mengonversi PDF ke Teks

**Aspose.PDF for .NET** mendukung mengonversi seluruh dokumen PDF dan halaman tunggal ke file Teks.

### Mengonversi seluruh dokumen PDF ke file Teks

Anda dapat mengonversi dokumen PDF ke file TXT menggunakan metode [Visit](https://reference.aspose.com/pdf/net/aspose.pdf.text/textabsorber/methods/visit/index) dari kelas [TextAbsorber](https://reference.aspose.com/pdf/net/aspose.pdf.text/textabsorber).

Potongan kode berikut menjelaskan cara mengekstrak teks dari semua halaman.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFtoTXT()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "demo.pdf"))
    {
        var ta = new Aspose.Pdf.Text.TextAbsorber();
        ta.Visit(document);

        // Save the extracted text in text file
        File.WriteAllText(dataDir + "input_Text_Extracted_out.txt",ta.Text);
    }
}
```

{{% alert color="success" %}}
**Cobalah untuk mengonversi PDF ke Teks secara online**

Aspose.PDF for .NET mempersembahkan aplikasi gratis online ["PDF to Text"](https://products.aspose.app/pdf/conversion/pdf-to-txt), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitasnya.

[![Aspose.PDF Konversi PDF ke Teks dengan Aplikasi Gratis](pdf_to_text.png)](https://products.aspose.app/pdf/conversion/pdf-to-txt)
{{% /alert %}}

### Mengonversi halaman PDF ke file teks

Anda dapat mengonversi dokumen PDF ke file TXT dengan Aspose.PDF for .NET. Anda harus menggunakan metode `Visit` dari kelas `TextAbsorber` untuk menyelesaikan tugas ini.

Potongan kode berikut menjelaskan cara mengekstrak teks dari halaman tertentu.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFtoTXT()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "demo.pdf"))
    {
        var ta = new Aspose.Pdf.Text.TextAbsorber();
        var pages = new [] {1, 3, 4};
        foreach (var page in pages)
        {
            ta.Visit(document.Pages[page]);
        }
    
        // Save the extracted text in text file
        File.WriteAllText(dataDir + "input_Text_Extracted_out.txt", ta.Text);
    }
}
```

## Mengonversi PDF ke XPS

**Aspose.PDF for .NET** memberikan kemungkinan untuk mengonversi file PDF ke format <abbr title="XML Paper Specification">XPS</abbr>. Mari kita coba menggunakan potongan kode yang disajikan untuk mengonversi file PDF ke format XPS dengan C#.

{{% alert color="success" %}}
**Cobalah untuk mengonversi PDF ke XPS secara online**

Aspose.PDF for .NET mempersembahkan aplikasi gratis online ["PDF to XPS"](https://products.aspose.app/pdf/conversion/pdf-to-xps), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitasnya.

[![Aspose.PDF Konversi PDF ke XPS dengan Aplikasi Gratis](pdf_to_xps.png)](https://products.aspose.app/pdf/conversion/pdf-to-xps)
{{% /alert %}}

Tipe file XPS terutama terkait dengan Spesifikasi Kertas XML oleh Microsoft Corporation. Spesifikasi Kertas XML (XPS), sebelumnya bernama Metro dan mencakup konsep pemasaran Jalur Cetak Generasi Berikutnya (NGPP), adalah inisiatif Microsoft untuk mengintegrasikan pembuatan dan tampilan dokumen ke dalam sistem operasi Windows.

Untuk mengonversi file PDF ke XPS, Aspose.PDF memiliki kelas [XpsSaveOptions](https://reference.aspose.com/net/pdf/aspose.pdf/xpssaveoptions) yang digunakan sebagai argumen kedua untuk metode [Document.Save(..)](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save/index) untuk menghasilkan file XPS.

Sejak rilis 24.2, Aspose.PDF telah menerapkan konversi PDF yang Dapat Dicari ke XPS sambil menjaga Teks Dapat Dipilih di XPS yang dihasilkan. Untuk mempertahankan teks, perlu untuk mengatur properti XpsSaveOptions.SaveTransparentTexts ke true.

Potongan kode berikut menunjukkan proses mengonversi file PDF menjadi format XPS.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFtoXPS()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

    using (var document = new Aspose.Pdf.Document(dataDir + "demo.pdf"))
    {
        var xpsOptions = new XpsSaveOptions
        {
            SaveTransparentTexts = true
        };

        // Save XPS document
        document.Save(dataDir + "PDFtoXPS_out.xps", xpsOptions);
    }
}
```

## Mengonversi PDF ke Markdown

**Aspose.PDF for .NET** memberikan kemungkinan untuk mengonversi file PDF ke format <abbr title="Markdown">MD</abbr>. Mari kita coba menggunakan potongan kode yang disajikan untuk mengonversi file PDF ke format MD dengan C#.

Markdown adalah bahasa markup ringan yang dirancang untuk mewakili format teks biasa dengan maksimum keterbacaan manusia dan keterbacaan mesin untuk bahasa penerbitan yang lebih maju.

### Optimalkan penggunaan gambar dengan konverter PDF ke Markdown

Anda dapat memperhatikan bahwa di direktori dengan gambar, jumlah gambar lebih sedikit daripada jumlah gambar dalam file PDF.

Karena file markdown tidak dapat mengatur ukuran gambar, tanpa opsi MarkdownSaveOptions.UseImageHtmlTag, jenis gambar yang sama dengan ukuran berbeda disimpan sebagai berbeda.

Untuk opsi yang diaktifkan MarkdownSaveOptions.UseImageHtmlTag akan menyimpan gambar unik, yang diskalakan dalam dokumen dengan tag img.

Kode membuka dokumen PDF, mengonfigurasi parameter untuk mengonversinya menjadi file Markdown (menyimpan gambar apa pun di folder bernama "images"), dan menyimpan file Markdown yang dihasilkan di jalur output yang ditentukan.

Potongan kode berikut menunjukkan proses mengonversi file PDF menjadi format MD.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFtoMarkup()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "demo.pdf"))
    {
        // Create an instance of MarkdownSaveOptions to configure the Markdown export settings
        var saveOptions = new MarkdownSaveOptions()
        {
            // Set to false to prevent the use of HTML <img> tags for images in the Markdown output
            UseImageHtmlTag = false
        }
        
        // Specify the directory name where resources (like images) will be stored
        saveOptions.ResourcesDirectoryName = "images";

        // Save PDF document in Markdown format to the specified output file path using the defined save options   
        document.Save(dataDir + "PDFtoMarkup_out.md", saveOptions);
    }
}
```

### Mengonversi PDF ke MobiXml

MobiXML adalah format eBook populer, dirancang untuk digunakan di platform seluler.
Potongan kode berikut menjelaskan cara mengonversi dokumen PDF ke file MobiXML.
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET      
private static void ConvertPdfToMobiXml()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDFToXML.pdf"))
    {
        // Save PDF document in XML format
        document.Save(dataDir + "PDFToXML_out.xml", Aspose.Pdf.SaveFormat.MobiXml);
    }
}
```