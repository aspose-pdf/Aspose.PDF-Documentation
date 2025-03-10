---
title: Bekerja dengan Portofolio dalam PDF
linktitle: Portofolio
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 40
url: /id/net/portfolio/
description: Cara Membuat Portofolio PDF dengan C#. Anda harus menggunakan File Microsoft Excel, dokumen Word, dan file gambar untuk membuat Portofolio PDF.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Working with Portfolio in PDF",
    "alternativeHeadline": "Create Dynamic PDF Portfolios from Multiple File Types",
    "abstract": "Temukan fitur Portofolio PDF yang inovatif di Aspose.PDF, yang memungkinkan pengguna untuk dengan mudah menggabungkan berbagai jenis file termasuk Microsoft Excel, dokumen Word, dan gambar menjadi PDF yang kohesif. Fungsionalitas ini tidak hanya mempertahankan identitas masing-masing file tetapi juga menyederhanakan proses pengelolaan, ekstraksi, dan modifikasi komponen dalam portofolio, memastikan pengalaman pengguna yang lancar untuk pembuatan dan pengelolaan dokumen.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "PDF Portfolio, C# PDF creation, Aspose.PDF library, Document class, FileSpecification class, file extraction PDF, remove files PDF Portfolio, unified container PDF, embedded files collection, PDF manipulation .NET",
    "wordcount": "575",
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
    "url": "/net/portfolio/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/portfolio/"
    },
    "dateModified": "2024-11-25",
    "description": "Cara Membuat Portofolio PDF dengan C#. Anda harus menggunakan File Microsoft Excel, dokumen Word, dan file gambar untuk membuat Portofolio PDF."
}
</script>

## Cara Membuat Portofolio PDF

Aspose.PDF memungkinkan pembuatan dokumen Portofolio PDF menggunakan kelas [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document). Tambahkan file ke objek Document.Collection setelah mendapatkannya dengan kelas [FileSpecification](https://reference.aspose.com/pdf/net/aspose.pdf/filespecification). Setelah file ditambahkan, gunakan metode Save kelas Document untuk menyimpan dokumen portofolio.

Contoh berikut menggunakan File Microsoft Excel, dokumen Word, dan file gambar untuk membuat Portofolio PDF.

Kode di bawah ini menghasilkan portofolio berikut.

Potongan kode berikut juga bekerja dengan pustaka [Aspose.PDF.Drawing](/pdf/id/net/drawing/).

### Portofolio PDF yang dibuat dengan Aspose.PDF

![Portofolio PDF yang dibuat dengan Aspose.PDF for .NET](working-with-pdf-portfolio_1.jpg)

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CreatePortfolio()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_TechnicalArticles();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Instantiate document Collection object
        document.Collection = new Aspose.Pdf.Collection();

        // Get Files to add to Portfolio
        var excel = new Aspose.Pdf.FileSpecification(dataDir + "HelloWorld.xlsx");
        var word = new Aspose.Pdf.FileSpecification(dataDir + "HelloWorld.docx");
        var image = new Aspose.Pdf.FileSpecification(dataDir + "aspose-logo.jpg");

        // Provide description of the files
        excel.Description = "Excel File";
        word.Description = "Word File";
        image.Description = "Image File";

        // Add files to document collection
        document.Collection.Add(excel);
        document.Collection.Add(word);
        document.Collection.Add(image);

        // Save PDF document
        document.Save(dataDir + "CreatePortfolio_out.pdf");
    }
}
```

## Ekstrak file dari Portofolio PDF

Portofolio PDF memungkinkan Anda untuk menggabungkan konten dari berbagai sumber (misalnya, PDF, Word, Excel, file JPEG) ke dalam satu wadah terpadu. File asli mempertahankan identitas masing-masing tetapi disusun menjadi file Portofolio PDF. Pengguna dapat membuka, membaca, mengedit, dan memformat setiap file komponen secara independen dari file komponen lainnya.

Aspose.PDF memungkinkan pembuatan dokumen Portofolio PDF menggunakan kelas [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document). Ini juga menawarkan kemampuan untuk mengekstrak file dari portofolio PDF.

Potongan kode berikut menunjukkan langkah-langkah untuk mengekstrak file dari portofolio PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractPortfolioFiles()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_TechnicalArticles();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDFPortfolio.pdf"))
    {
        // Get collection of embedded files
        Aspose.Pdf.EmbeddedFileCollection embeddedFiles = document.EmbeddedFiles;
        // Iterate through individual file of Portfolio
        foreach (Aspose.Pdf.FileSpecification fileSpecification in embeddedFiles)
        {
            // Get the attachment and write to file or stream
            byte[] fileContent = new byte[fileSpecification.Contents.Length];
            fileSpecification.Contents.Read(fileContent, 0, fileContent.Length);
            string filename = Path.GetFileName(fileSpecification.Name);
            // Save the extracted file to some location
            using (FileStream fileStream = new FileStream(dataDir + filename + "_out", FileMode.Create))
            {
                fileStream.Write(fileContent, 0, fileContent.Length);
            }
        }
    }
}
```

![Ekstrak file dari Portofolio PDF](working-with-pdf-portfolio_2.jpg)

## Hapus File dari Portofolio PDF

Untuk menghapus/menghapus file dari portofolio PDF, coba gunakan baris kode berikut.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void RemovePortfolioFiles()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_TechnicalArticles();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDFPortfolio.pdf"))
    {
        document.Collection.Delete();
        // Save PDF document
        document.Save(dataDir + "NoPortFolio_out.pdf");
    }
}
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for .NET Library",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
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
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "PDF Manipulation Library for .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/net/create-pdf-document/screenshot.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>