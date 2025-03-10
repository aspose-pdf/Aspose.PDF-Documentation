---
title: Tambahkan Header dan Footer ke PDF
linktitle: Tambahkan Header dan Footer ke PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 70
url: /id/net/add-headers-and-footers-of-pdf-file/
description: Aspose.PDF for .NET memungkinkan Anda untuk menambahkan header dan footer ke file PDF Anda menggunakan kelas TextStamp.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Add Header and Footer to PDF",
    "alternativeHeadline": "Add Custom Headers and Footers to PDF Files",
    "abstract": "Aspose.PDF for .NET memperkenalkan fitur yang kuat yang memungkinkan pengguna untuk memperkaya dokumen PDF mereka dengan menambahkan header dan footer yang dapat disesuaikan. Menggunakan kelas TextStamp dan ImageStamp, pengembang dapat dengan mudah mengintegrasikan teks dan gambar, menyesuaikan penempatan dan penampilannya agar sesuai dengan berbagai format dan gaya dokumen. Ini meningkatkan profesionalisme dan keterbacaan dokumen, menjadikannya ideal untuk laporan, faktur, dan komunikasi formal lainnya.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1549",
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
    "url": "/net/add-headers-and-footers-of-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-headers-and-footers-of-pdf-file/"
    },
    "dateModified": "2024-11-26",
    "description": "Aspose.PDF for .NET memungkinkan Anda untuk menambahkan header dan footer ke file PDF Anda menggunakan kelas TextStamp."
}
</script>

**Aspose.PDF for .NET** memungkinkan Anda untuk menambahkan header dan footer di file PDF yang sudah ada. Anda dapat menambahkan gambar atau teks ke dokumen PDF. Juga, coba tambahkan berbagai header dalam satu file PDF dengan C#.

Potongan kode berikut juga bekerja dengan pustaka [Aspose.PDF.Drawing](/pdf/net/drawing/).

## Menambahkan Teks di Header File PDF

Anda dapat menggunakan kelas [TextStamp](https://reference.aspose.com/pdf/net/aspose.pdf/textstamp) untuk menambahkan teks di header file PDF. Kelas TextStamp menyediakan properti yang diperlukan untuk membuat stempel berbasis teks seperti ukuran font, gaya font, dan warna font, dll. Untuk menambahkan teks di header, Anda perlu membuat objek Document dan objek TextStamp menggunakan properti yang diperlukan. Setelah itu, Anda dapat memanggil metode AddStamp dari Page untuk menambahkan teks di header PDF.

Anda perlu mengatur properti TopMargin sedemikian rupa sehingga menyesuaikan teks di area header PDF Anda. Anda juga perlu mengatur HorizontalAlignment ke Center dan VerticalAlignment ke Top.

Potongan kode berikut menunjukkan kepada Anda cara menambahkan teks di header file PDF dengan C#.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddHeaderText()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "TextinHeader.pdf"))
    {
        // Create header as a TextStamp
        var textStamp = new Aspose.Pdf.TextStamp("Header Text")
        {
            TopMargin = 10,
            HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Center,
            VerticalAlignment = Aspose.Pdf.VerticalAlignment.Top
        };

        // Add header on all pages
        foreach (var page in document.Pages)
        {
            page.AddStamp(textStamp);
        }

        // Save PDF document
        document.Save(dataDir + "TextinHeader_out.pdf");
    }
}
```

## Menambahkan Teks di Footer File PDF

Anda dapat menggunakan kelas TextStamp untuk menambahkan teks di footer file PDF. Kelas TextStamp menyediakan properti yang diperlukan untuk membuat stempel berbasis teks seperti ukuran font, gaya font, dan warna font, dll. Untuk menambahkan teks di footer, Anda perlu membuat objek Document dan objek TextStamp menggunakan properti yang diperlukan. Setelah itu, Anda dapat memanggil metode AddStamp dari Page untuk menambahkan teks di footer PDF.

{{% alert color="primary" %}}

Anda perlu mengatur properti Bottom Margin sedemikian rupa sehingga menyesuaikan teks di area footer PDF Anda. Anda juga perlu mengatur HorizontalAlignment ke Center dan VerticalAlignment ke Bottom.

{{% /alert %}}

Potongan kode berikut menunjukkan kepada Anda cara menambahkan teks di footer file PDF dengan C#.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddFooterText()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "TextinFooter.pdf"))
    {
        // Create footer as a TextStamp
        var textStamp = new Aspose.Pdf.TextStamp("Footer Text")
        {
            BottomMargin = 10,
            HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Center,
            VerticalAlignment = Aspose.Pdf.VerticalAlignment.Bottom
        };

        // Add footer on all pages
        foreach (var page in document.Pages)
        {
            page.AddStamp(textStamp);
        }

        // Save PDF document
        document.Save(dataDir + "TextinFooter_out.pdf");
    }
}
```

## Menambahkan Gambar di Header File PDF

Anda dapat menggunakan kelas [ImageStamp](https://reference.aspose.com/pdf/net/aspose.pdf/ImageStamp) untuk menambahkan gambar di header file PDF. Kelas Image Stamp menyediakan properti yang diperlukan untuk membuat stempel berbasis gambar seperti ukuran font, gaya font, dan warna font, dll. Untuk menambahkan gambar di header, Anda perlu membuat objek Document dan objek Image Stamp menggunakan properti yang diperlukan. Setelah itu, Anda dapat memanggil metode [AddStamp](https://reference.aspose.com/pdf/net/aspose.pdf/page/methods/addstamp) dari Page untuk menambahkan gambar di header PDF.

{{% alert color="primary" %}}

Anda perlu mengatur properti TopMargin sedemikian rupa sehingga menyesuaikan gambar di area header PDF Anda. Anda juga perlu mengatur HorizontalAlignment ke Center dan VerticalAlignment ke Top.

{{% /alert %}}

Potongan kode berikut menunjukkan kepada Anda cara menambahkan gambar di header file PDF dengan C#.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddImageHeader()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ImageinHeader.pdf"))
    {
        // Create header as an ImageStamp
        var imageStamp = new Aspose.Pdf.ImageStamp(dataDir + "aspose-logo.jpg")
        {
            TopMargin = 10,
            HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Center,
            VerticalAlignment = Aspose.Pdf.VerticalAlignment.Top
        };

        // Add image header on all pages
        foreach (var page in document.Pages)
        {
            page.AddStamp(imageStamp);
        }

        // Save PDF document
        document.Save(dataDir + "ImageinHeader_out.pdf");
    }
}
```

## Menambahkan Gambar di Footer File PDF

Anda dapat menggunakan kelas Image Stamp untuk menambahkan gambar di footer file PDF. Kelas Image Stamp menyediakan properti yang diperlukan untuk membuat stempel berbasis gambar seperti ukuran font, gaya font, dan warna font, dll. Untuk menambahkan gambar di footer, Anda perlu membuat objek Document dan objek Image Stamp menggunakan properti yang diperlukan. Setelah itu, Anda dapat memanggil metode AddStamp dari Page untuk menambahkan gambar di footer PDF.

{{% alert color="primary" %}}

Anda perlu mengatur properti [BottomMargin](https://reference.aspose.com/pdf/net/aspose.pdf/stamp/properties/bottommargin) sedemikian rupa sehingga menyesuaikan gambar di area footer PDF Anda. Anda juga perlu mengatur [HorizontalAlignment](https://reference.aspose.com/pdf/net/aspose.pdf/stamp/properties/horizontalalignment) ke `Center` dan [VerticalAlignment](https://reference.aspose.com/pdf/net/aspose.pdf/stamp/properties/verticalalignment) ke `Bottom`.

{{% /alert %}}

Potongan kode berikut menunjukkan kepada Anda cara menambahkan gambar di footer file PDF dengan C#.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddImageFooter()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ImageInFooter.pdf"))
    {
        // Create footer as an ImageStamp
        var imageStamp = new Aspose.Pdf.ImageStamp(dataDir + "aspose-logo.jpg")
        {
            BottomMargin = 10,
            HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Center,
            VerticalAlignment = Aspose.Pdf.VerticalAlignment.Bottom
        };

        // Add image footer on all pages
        foreach (var page in document.Pages)
        {
            page.AddStamp(imageStamp);
        }

        // Save PDF document
        document.Save(dataDir + "ImageInFooter_out.pdf");
    }
}
```

## Menambahkan berbagai Header dalam satu File PDF

Kita tahu bahwa kita dapat menambahkan TextStamp di bagian Header/Footer dokumen dengan menggunakan properti TopMargin atau Bottom Margin, tetapi terkadang kita mungkin memiliki kebutuhan untuk menambahkan beberapa header/footer dalam satu dokumen PDF. **Aspose.PDF for .NET** menjelaskan cara melakukannya.

Untuk memenuhi kebutuhan ini, kita akan membuat objek TextStamp individu (jumlah objek tergantung pada jumlah Header/Footer yang diperlukan) dan akan menambahkannya ke dokumen PDF. Kita juga dapat menentukan informasi format yang berbeda untuk setiap objek stempel. Dalam contoh berikut, kita telah membuat objek Document dan tiga objek TextStamp dan kemudian kita telah menggunakan metode [AddStamp](https://reference.aspose.com/pdf/net/aspose.pdf/page/methods/addstamp) dari Page untuk menambahkan teks di bagian header PDF. Potongan kode berikut menunjukkan kepada Anda cara menambahkan gambar di footer file PDF dengan Aspose.PDF for .NET.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddDifferentHeaders()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "AddingDifferentHeaders.pdf"))
    {
        // Create three stamps
        var stamp1 = new Aspose.Pdf.TextStamp("Header 1");
        var stamp2 = new Aspose.Pdf.TextStamp("Header 2");
        var stamp3 = new Aspose.Pdf.TextStamp("Header 3");

        // Set stamp1 properties (Header 1)
        stamp1.VerticalAlignment = Aspose.Pdf.VerticalAlignment.Top;
        stamp1.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Center;
        stamp1.TextState.FontStyle = Aspose.Pdf.Text.FontStyles.Bold;
        stamp1.TextState.ForegroundColor = Aspose.Pdf.Color.Red;
        stamp1.TextState.FontSize = 14;

        // Set stamp2 properties (Header 2)
        stamp2.VerticalAlignment = Aspose.Pdf.VerticalAlignment.Top;
        stamp2.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Center;
        stamp2.Zoom = 10;

        // Set stamp3 properties (Header 3)
        stamp3.VerticalAlignment = Aspose.Pdf.VerticalAlignment.Top;
        stamp3.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Center;
        stamp3.RotateAngle = 35;
        stamp3.TextState.BackgroundColor = Aspose.Pdf.Color.Pink;
        stamp3.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("Verdana");

        // Add the stamps to specific pages
        document.Pages[1].AddStamp(stamp1);
        document.Pages[2].AddStamp(stamp2);
        document.Pages[3].AddStamp(stamp3);

        // Save PDF document
        document.Save(dataDir + "MultiHeader_out.pdf");
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