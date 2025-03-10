---
title: Tambahkan Nomor Halaman ke PDF
linktitle: Tambahkan Nomor Halaman
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 100
url: /id/net/add-page-number/
description: Aspose.PDF for .NET memungkinkan Anda untuk menambahkan Cap Nomor Halaman ke file PDF Anda menggunakan kelas PageNumber Stamp.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
aliases:
    - /net/get-and-set-page-properties/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Add Page Number to PDF",
    "alternativeHeadline": "Add Dynamic Page Numbering to PDF",
    "abstract": "Aspose.PDF for .NET memperkenalkan fitur Cap Nomor Halaman yang kuat, memungkinkan integrasi nomor halaman ke dalam dokumen PDF secara mulus. Fungsionalitas ini meningkatkan navigasi dan organisasi dokumen dengan memungkinkan pengguna untuk menyesuaikan format, penyelarasan, dan gaya untuk keterbacaan yang lebih baik dan presentasi yang profesional.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Add Page Number, PDF Stamp, Aspose.PDF for .NET, PageNumberStamp class, Document object, PageNumberStamp properties, Bates numbering, PDF document generation, Page number stamp, C# PDF manipulation",
    "wordcount": "559",
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
    "url": "/net/add-page-number/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-page-number/"
    },
    "dateModified": "2024-11-26",
    "description": "Aspose.PDF for .NET memungkinkan Anda untuk menambahkan Cap Nomor Halaman ke file PDF Anda menggunakan kelas PageNumber Stamp."
}
</script>

Semua dokumen harus memiliki nomor halaman di dalamnya. Nomor halaman memudahkan pembaca untuk menemukan bagian-bagian berbeda dari dokumen.
**Aspose.PDF for .NET** memungkinkan Anda untuk menambahkan nomor halaman dengan PageNumberStamp.

Potongan kode berikut juga bekerja dengan pustaka [Aspose.PDF.Drawing](/pdf/net/drawing/).

Anda dapat menggunakan kelas [PageNumberStamp](https://reference.aspose.com/pdf/net/aspose.pdf/pagenumberstamp) untuk menambahkan cap nomor halaman dalam file PDF. Kelas [PageNumber Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/pagenumberstamp) menyediakan properti yang diperlukan untuk membuat cap berdasarkan nomor halaman seperti format, margin, penyelarasan, nomor awal, dll. Untuk menambahkan cap nomor halaman, Anda perlu membuat objek [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) dan objek [PageNumberStamp](https://reference.aspose.com/pdf/net/aspose.pdf/pagenumberstamp) menggunakan properti yang diperlukan. Setelah itu, Anda dapat memanggil metode [AddStamp](https://reference.aspose.com/pdf/net/aspose.pdf/page/methods/addstamp) dari [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) untuk menambahkan cap ke dalam PDF. Anda juga dapat mengatur atribut font dari cap nomor halaman. Potongan kode berikut menunjukkan kepada Anda cara menambahkan nomor halaman dalam file PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddPageNumberToPdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PageNumberStamp.pdf"))
    {
        // Create page number stamp
        var pageNumberStamp = new Aspose.Pdf.PageNumberStamp();
        // Whether the stamp is background
        pageNumberStamp.Background = false;
        pageNumberStamp.Format = "Page # of " + document.Pages.Count;
        pageNumberStamp.BottomMargin = 10;
        pageNumberStamp.HorizontalAlignment = HorizontalAlignment.Center;
        pageNumberStamp.StartingNumber = 1;
        // Set text properties
        pageNumberStamp.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("Arial");
        pageNumberStamp.TextState.FontSize = 14.0F;
        pageNumberStamp.TextState.FontStyle = Aspose.Pdf.Text.FontStyles.Bold;
        pageNumberStamp.TextState.FontStyle = Aspose.Pdf.Text.FontStyles.Italic;
        pageNumberStamp.TextState.ForegroundColor = Color.Aqua;
        // Add stamp to particular page
        document.Pages[1].AddStamp(pageNumberStamp);
        // Save PDF document
        document.Save(dataDir + "PageNumberStamp_out.pdf");  
    }
}
```

## Contoh Langsung

[Tambahkan nomor halaman PDF](https://products.aspose.app/pdf/page-number) adalah aplikasi web gratis online yang memungkinkan Anda menyelidiki bagaimana fungsionalitas penambahan nomor halaman bekerja.

[![Cara menambahkan nomor halaman di pdf menggunakan C#](page_number.png)](https://products.aspose.app/pdf/page-number)

## Tambah/Hapus penomoran Bates

**Penomoran Bates** (juga dikenal sebagai cap Bates) digunakan di bidang hukum, medis, dan bisnis untuk menempatkan nomor identifikasi dan/atau tanda tanggal/waktu pada gambar dan dokumen saat dipindai atau diproses, misalnya, selama tahap penemuan persiapan untuk persidangan atau mengidentifikasi kwitansi bisnis. Proses ini memberikan identifikasi, perlindungan, dan penomoran berurutan otomatis dari gambar atau dokumen.

Aspose.PDF memiliki dukungan terbatas untuk Penomoran Bates saat ini. Fungsionalitas ini akan diperbarui sesuai dengan permintaan pelanggan.

### Cara menghapus penomoran Bates

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void RemoveBatesNumbering()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();
    
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "RemoveBatesNumberingInput.pdf"))
    {
        foreach (var page in document.Pages)
        {
            // Remove bates numbering
            var artifacts = page.Artifacts.Where(ar => ar.CustomSubtype == "BatesN");
            foreach (var artifact in artifacts)
            {
                page.Artifacts.Delete(artifact);   
            }
        }
        // Save PDF document
        document.Save(dataDir + "RemoveBatesNumbering_out.pdf");
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