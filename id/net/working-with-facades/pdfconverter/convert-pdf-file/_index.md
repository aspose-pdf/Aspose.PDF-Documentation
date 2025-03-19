---
title: Mengonversi File PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 30
url: /id/net/convert-pdf-file/
description: Pelajari cara mengonversi file PDF ke berbagai format di .NET menggunakan Aspose.PDF untuk penanganan dokumen yang fleksibel.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Convert PDF File",
    "alternativeHeadline": "Convert PDF Pages to Image Formats Efficiently",
    "abstract": "Buka kekuatan Aspose.PDF for .NET Facades untuk dengan mudah mengonversi halaman PDF menjadi berbagai format gambar seperti JPEG, GIF, dan PNG dengan kelas PdfConverter. Fitur ini memungkinkan kontrol rinci atas proses konversi, memungkinkan Anda untuk menentukan parameter seperti resolusi, jenis koordinat, dan rentang halaman untuk output yang disesuaikan. Tingkatkan kemampuan penanganan dokumen Anda dengan mengintegrasikan konversi PDF ke gambar yang mulus ke dalam aplikasi Anda.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "561",
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
    "url": "/net/convert-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/convert-pdf-file/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF dapat melakukan tidak hanya tugas yang sederhana dan mudah tetapi juga dapat menangani tujuan yang lebih kompleks. Periksa bagian berikut untuk pengguna dan pengembang tingkat lanjut."
}
</script>

## Mengonversi Halaman PDF ke Format Gambar yang Berbeda (Facades)

Untuk mengonversi halaman PDF ke format gambar yang berbeda, Anda perlu membuat objek [PdfConverter](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter) dan membuka file PDF menggunakan metode [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3). Setelah itu, Anda perlu memanggil metode [DoConvert](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter/methods/doconvert) untuk tugas inisialisasi. Kemudian, Anda dapat melakukan loop melalui semua halaman menggunakan metode [HasNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter/methods/hasnextimage) dan [GetNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfconverter/getnextimage/methods/6). Metode [GetNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfconverter/getnextimage/methods/6) memungkinkan Anda untuk membuat gambar dari halaman tertentu. Anda juga perlu melewatkan ImageFormat ke metode ini untuk membuat gambar dari jenis tertentu yaitu JPEG, GIF atau PNG, dll. Akhirnya, panggil metode [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter/methods/close) dari kelas [PdfConverter](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter). Potongan kode berikut menunjukkan cara mengonversi halaman PDF menjadi gambar.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPdfPagesToImages01()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PdfConverter object
    using (var converter = new Aspose.Pdf.Facades.PdfConverter())
    {
        // Bind PDF document
        converter.BindPdf(dataDir + "ConvertPdfPagesToImages.pdf");

        // Initialize the converting process
        converter.DoConvert();

        // Check if pages exist and then convert to image one by one
        while (converter.HasNextImage())
        {
            // Generate output file name with '_out' suffix
            var outputFileName = dataDir + System.DateTime.Now.Ticks.ToString() + "_out.jpg";
            // Convert the page to image and save it
            converter.GetNextImage(outputFileName, System.Drawing.Imaging.ImageFormat.Jpeg);
        }
    }
}
```

Dalam potongan kode berikut, kami akan menunjukkan bagaimana Anda dapat mengubah beberapa parameter. Dengan [CoordinateType](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter/properties/coordinatetype) kami mengatur bingkai 'CropBox'. Juga, kami dapat mengubah [Resolution](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter/properties/resolution) dengan menentukan jumlah titik per inci. Yang berikutnya [FormPresentationMode](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter/properties/formpresentationmode) - mode presentasi formulir. Kemudian kami menunjukkan [StartPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter/properties/startpage) di mana nomor halaman awal konversi ditetapkan. Kami juga dapat menentukan halaman terakhir dengan menetapkan rentang.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPdfPagesToImages02()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PdfConverter object
    using (var converter = new Aspose.Pdf.Facades.PdfConverter())
    {
        // Bind PDF document
        converter.BindPdf(dataDir + "ConvertPdfPagesToImages.pdf");

        // Initialize the converting process
        converter.DoConvert();

        // Set additional conversion settings
        converter.CoordinateType = Aspose.Pdf.PageCoordinateType.CropBox;
        converter.Resolution = new Aspose.Pdf.Devices.Resolution(600);
        converter.FormPresentationMode = Aspose.Pdf.Devices.FormPresentationMode.Production;
        converter.StartPage = 2;

        // Check if pages exist and then convert to image one by one
        while (converter.HasNextImage())
        {
            // Generate output file name
            var outputFileName = dataDir + System.DateTime.Now.Ticks.ToString() + "_out.jpg";
            // Convert the page to image and save it
            converter.GetNextImage(outputFileName, System.Drawing.Imaging.ImageFormat.Jpeg);
        }
    }
}
```

## Mengonversi Halaman PDF ke Format Gambar dengan Substitusi Font Kustom 

Dalam potongan kode berikut, kami menunjukkan cara menerapkan substitusi font kustom selama proses konversi PDF ke gambar. Kami menggunakan koleksi FontRepository.Substitutions untuk mendaftarkan aturan substitusi kustom. Dalam contoh ini, ketika font "Helvetica" ditemukan, font tersebut diganti dengan "Arial".

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertWithCustomFontSubstitution()
{
    // Add custom font substitution
    Aspose.Pdf.Text.FontRepository.Substitutions.Add(new CustomPdfFontSubstitution());

    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();
    
    using (var converter = new Aspose.Pdf.Facades.PdfConverter())
    {
        // Bind PDF document
        converter.BindPdf(dataDir + "ConvertWithSubstitution.pdf");

        // Initialize the converting process
        converter.DoConvert();

        // Check if pages exist and then convert to image one by one
        while (converter.HasNextImage())
        {
            // Generate output file name with '_out' suffix
            var outputFileName = dataDir + System.DateTime.Now.Ticks.ToString() + "_out.jpg";
            // Convert the page to image and save it
            converter.GetNextImage(outputFileName, System.Drawing.Imaging.ImageFormat.Jpeg);
        }
    }
}

private class CustomPdfFontSubstitution : Aspose.Pdf.Text.CustomFontSubstitutionBase
{
    public override bool TrySubstitute(
        Aspose.Pdf.Text.CustomFontSubstitutionBase.OriginalFontSpecification originalFontSpecification,
        out Aspose.Pdf.Text.Font substitutionFont)
    {
        if (originalFontSpecification.OriginalFontName == "Helvetica")
        {
            substitutionFont = Aspose.Pdf.Text.FontRepository.FindFont("Arial");
            return true;
        }
        // Default substitution logic
        return base.TrySubstitute(originalFontSpecification, out substitutionFont);
    }
}
```
{{< /tab >}}
{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertWithCustomFontSubstitution()
{
    // Add custom font substitution
    Aspose.Pdf.Text.FontRepository.Substitutions.Add(new CustomPdfFontSubstitution());

    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();
    
    using var converter = new Aspose.Pdf.Facades.PdfConverter();
    
    // Bind PDF document
    converter.BindPdf(dataDir + "ConvertWithSubstitution.pdf");

    // Initialize the converting process
    converter.DoConvert();

    // Check if pages exist and then convert to image one by one
    while (converter.HasNextImage())
    {
        // Generate output file name with '_out' suffix
        var outputFileName = dataDir + System.DateTime.Now.Ticks.ToString() + "_out.jpg";
        // Convert the page to image and save it
        converter.GetNextImage(outputFileName, System.Drawing.Imaging.ImageFormat.Jpeg);
    }
}

private class CustomPdfFontSubstitution : Aspose.Pdf.Text.CustomFontSubstitutionBase
{
    public override bool TrySubstitute(
        Aspose.Pdf.Text.CustomFontSubstitutionBase.OriginalFontSpecification originalFontSpecification,
        out Aspose.Pdf.Text.Font substitutionFont)
    {
        if (originalFontSpecification.OriginalFontName == "Helvetica")
        {
            substitutionFont = Aspose.Pdf.Text.FontRepository.FindFont("Arial");
            return true;
        }
        // Default substitution logic
        return base.TrySubstitute(originalFontSpecification, out substitutionFont);
    }
}
```
{{< /tab >}}
{{< /tabs >}}

## Lihat juga

Aspose.PDF for .NET memungkinkan mengonversi dokumen PDF ke berbagai format dan juga mengonversi dari format lain ke PDF. Juga, Anda dapat memeriksa kualitas konversi Aspose.PDF dan melihat hasilnya secara online dengan aplikasi konverter Aspose.PDF. Pelajari bagian [Mengonversi](/pdf/id/net/converting/) untuk menyelesaikan tugas Anda.