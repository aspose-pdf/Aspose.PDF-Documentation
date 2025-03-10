---
title: Dukungan untuk Gambar DICOM
linktitle: Dukungan untuk Gambar DICOM
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 100
url: /id/net/support-for-dicom-mages/
description: Bagian ini menjelaskan cara mendukung gambar DICOM dalam file PDF menggunakan pustaka C#.
lastmod: "2022-02-17"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Support for DICOM Images",
    "alternativeHeadline": "Add DICOM images to PDFs using C# library",
    "abstract": "Aspose.PDF for .NET sekarang mengintegrasikan dukungan gambar DICOM, memungkinkan penyisipan gambar medis ke dalam dokumen PDF secara mulus. Fungsionalitas baru ini memanfaatkan pustaka C# untuk penanganan gambar DICOM yang efisien dalam proses pembuatan PDF. Fitur ini menyederhanakan alur kerja untuk menggabungkan gambar DICOM ke dalam file PDF",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "DICOM images, PDF, C#, Aspose.PDF, DICOM to PDF, add DICOM to PDF, .NET library, ImageFileType.Dicom",
    "wordcount": "194",
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
    "url": "/net/support-for-dicom-mages/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/support-for-dicom-mages/"
    },
    "dateModified": "2024-11-26",
    "description": "Bagian ini menjelaskan cara mendukung gambar DICOM dalam file PDF menggunakan pustaka C#."
}
</script>

Standar DICOM dikembangkan oleh Asosiasi Produsen Listrik Nasional. Format ini mencakup fungsi untuk membuat, menyimpan, mentransfer, dan mencetak bingkai gambar individu, serangkaian bingkai, informasi pasien, penelitian, peralatan, institusi, dan tenaga medis yang melakukan pemeriksaan, dan sebagainya.

Cuplikan kode berikut juga bekerja dengan pustaka [Aspose.PDF.Drawing](/pdf/id/net/drawing/).

**Aspose.PDF for .NET** mendukung fungsionalitas untuk menambahkan gambar DICOM ke dokumen PDF. Cuplikan kode berikut menunjukkan cara menggunakan fungsionalitas ini.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddDicomImageToPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();

        // Create an image instance and set its properties
        var image = new Aspose.Pdf.Image
        {
            FileType = Aspose.Pdf.ImageFileType.Dicom,
            ImageStream = new FileStream(dataDir + "DicomImage.dcm", FileMode.Open, FileAccess.Read)
        };

        // Add image to the first page
        page.Paragraphs.Add(image);

        // Save PDF document
        document.Save(dataDir + "PdfWithDicomImage_out.pdf");
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