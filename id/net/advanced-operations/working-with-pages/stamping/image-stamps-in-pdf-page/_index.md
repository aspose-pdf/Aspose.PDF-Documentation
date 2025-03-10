---
title: Tambahkan Stempel Gambar di PDF menggunakan C#
linktitle: Stempel Gambar di File PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /id/net/image-stamps-in-pdf-page/
description: Tambahkan Stempel Gambar di dokumen PDF Anda menggunakan kelas ImageStamp dengan pustaka Aspose.PDF.
lastmod: "2024-09-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Add Image stamps in PDF using C#",
    "alternativeHeadline": "Add Custom Image Stamps to PDF Documents",
    "abstract": "Fitur baru dalam pustaka Aspose.PDF memungkinkan pengguna untuk dengan mudah menambahkan stempel gambar ke dokumen PDF menggunakan C#. Dengan kelas ImageStamp, pengembang dapat menyesuaikan atribut seperti ukuran, opasitas, dan kualitas, secara signifikan meningkatkan presentasi dan aksesibilitas dokumen. Fungsionalitas ini juga mencakup kemampuan untuk menambahkan teks alternatif, yang meningkatkan kegunaan untuk pembaca layar.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "646",
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
    "url": "/net/image-stamps-in-pdf-page/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/image-stamps-in-pdf-page/"
    },
    "dateModified": "2024-11-26",
    "description": "Tambahkan Stempel Gambar di dokumen PDF Anda menggunakan kelas ImageStamp dengan pustaka Aspose.PDF."
}
</script>

## Tambahkan Stempel Gambar di File PDF

Anda dapat menggunakan kelas ImageStamp untuk menambahkan stempel gambar ke file PDF. Kelas ImageStamp menyediakan properti yang diperlukan untuk membuat stempel berbasis gambar, seperti tinggi, lebar, opasitas, dan sebagainya.

Cuplikan kode berikut juga bekerja dengan pustaka [Aspose.PDF.Drawing](/pdf/net/drawing/).

Untuk menambahkan stempel gambar:

1. Buat objek Document dan objek ImageStamp menggunakan properti yang diperlukan.
1. Panggil metode AddStamp dari kelas Page untuk menambahkan stempel ke PDF.

Cuplikan kode berikut menunjukkan cara menambahkan stempel gambar di file PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddImageStampInPdfFile()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ImageStampInput.pdf"))
    {
        // Create image stamp
        var imageStamp = new Aspose.Pdf.ImageStamp(dataDir + "aspose-logo.jpg");
        imageStamp.Background = true;
        imageStamp.XIndent = 100;
        imageStamp.YIndent = 100;
        imageStamp.Height = 300;
        imageStamp.Width = 300;
        imageStamp.Rotate = Rotation.on270;
        imageStamp.Opacity = 0.5;
        // Add stamp to particular page
        document.Pages[1].AddStamp(imageStamp);
        // Save PDF document
        document.Save(dataDir + "AddImageStamp_out.pdf");
    }
}
```

## Kontrol Kualitas Gambar saat Menambahkan Stempel

Saat menambahkan gambar sebagai objek stempel, Anda dapat mengontrol kualitas gambar. Properti Quality dari kelas ImageStamp digunakan untuk tujuan ini. Ini menunjukkan kualitas gambar dalam persen (nilai yang valid adalah 0..100).

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ControlImageQualityWhenAddingStamp()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ImageStampInput.pdf"))
    {
        // Create image stamp
        var imageStamp = new Aspose.Pdf.ImageStamp(dataDir + "aspose-logo.jpg");
        imageStamp.Quality = 10;
        document.Pages[1].AddStamp(imageStamp);
        // Save PDF document
        document.Save(dataDir + "ControlImageQuality_out.pdf");
    }
}
```

## Stempel Gambar sebagai Latar Belakang di Kotak Mengambang

API Aspose.PDF memungkinkan Anda menambahkan stempel gambar sebagai latar belakang di kotak mengambang. Properti BackgroundImage dari kelas FloatingBox dapat digunakan untuk mengatur stempel gambar latar belakang untuk kotak mengambang seperti yang ditunjukkan dalam cuplikan kode berikut.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ImageStampAsBackgroundInFloatingBox()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page to PDF document
        Page page = document.Pages.Add();
        // Create FloatingBox object
        var aBox = new Aspose.Pdf.FloatingBox(200, 100);
        // Set left position for FloatingBox
        aBox.Left = 40;
        // Set Top position for FloatingBox
        aBox.Top = 80;
        // Set the Horizontal alignment for FloatingBox
        aBox.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Center;
        // Add text fragment to paragraphs collection of FloatingBox
        aBox.Paragraphs.Add(new Aspose.Pdf.Text.TextFragment("main text"));
        // Set border for FloatingBox
        aBox.Border = new Aspose.Pdf.BorderInfo(BorderSide.All, Aspose.Pdf.Color.Red);
        // Add background image
        aBox.BackgroundImage = new Aspose.Pdf.Image
        {
            File = dataDir + "aspose-logo.jpg"
        };
        // Set background color for FloatingBox
        aBox.BackgroundColor = Aspose.Pdf.Color.Yellow;
        // Add FloatingBox to paragraphs collection of page object
        page.Paragraphs.Add(aBox);
        // Save PDF document
        document.Save(dataDir + "AddImageStampAsBackgroundInFloatingBox_out.pdf");
    }
}
```

## Tambahkan teks alternatif ke stempel gambar

Sejak versi 24.6, dimungkinkan untuk menambahkan teks alternatif ke stempel gambar.

Kode ini membuka file PDF, menambahkan gambar sebagai stempel pada posisi tertentu, dan menyertakan teks alternatif untuk aksesibilitas. PDF yang diperbarui kemudian disimpan dengan nama file baru.

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddAlternativeTextToTheImageStamp()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();
    
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ImageStampInput.pdf"))
    {
        // Create image stamp
        var imageStamp = new Aspose.Pdf.ImageStamp(dataDir + "aspose-logo.jpg")
        {
            XIndent = 100,
            YIndent = 700,
            Quality = 100,
            AlternativeText = "Your alt text"  // This property added.
        };
        // Add stamp
        document.Pages[1].AddStamp(imageStamp);
        // Save PDF document
        document.Save(dataDir + "DocWithImageStamp_out.pdf");
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