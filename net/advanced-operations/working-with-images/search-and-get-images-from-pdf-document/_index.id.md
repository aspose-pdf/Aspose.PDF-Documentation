---
title: Dapatkan dan Cari Gambar dalam PDF
linktitle: Cari dan Dapatkan Gambar
type: docs
weight: 60
url: /net/search-and-get-images-from-pdf-document/
description: Bagian ini menjelaskan cara mencari dan mendapatkan gambar dari dokumen PDF dengan perpustakaan Aspose.PDF.
lastmod: "2022-02-17"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Dapatkan dan Cari Gambar dalam PDF",
    "alternativeHeadline": "Cara Dapatkan dan Cari Gambar dalam Berkas PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pembuatan dokumen pdf",
    "keywords": "pdf, .net, get image, search image",
    "wordcount": "302",
    "proficiencyLevel":"Pemula",
    "publisher": {
        "@type": "Organization",
        "name": "Tim Dok Aspose.PDF",
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
                "contactType": "penjualan",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "penjualan",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "penjualan",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/net/search-and-get-images-from-pdf-document/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/search-and-get-images-from-pdf-document/"
    },
    "dateModified": "2022-02-04",
    "description": "Bagian ini menjelaskan cara mencari dan mendapatkan gambar dari dokumen PDF dengan perpustakaan Aspose.PDF."
}
</script>

ImagePlacementAbsorber memungkinkan Anda untuk mencari di antara gambar di semua halaman dalam dokumen PDF.

Kode berikut juga bekerja dengan pustaka [Aspose.PDF.Drawing](/pdf/net/drawing/).

Untuk mencari seluruh dokumen untuk gambar:

1. Panggil metode Accept dari koleksi Pages. Metode Accept menerima objek ImagePlacementAbsorber sebagai parameter. Ini mengembalikan koleksi objek ImagePlacement.
1. Lakukan pengulangan melalui objek ImagePlacements dan dapatkan properti mereka (Gambar, dimensi, resolusi, dan lain-lain).

Kode berikut menunjukkan cara mencari semua gambar dalam dokumen.

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_Images();

// Buka dokumen
Aspose.Pdf.Document doc = new Aspose.Pdf.Document(dataDir+ "SearchAndGetImages.pdf");

// Buat objek ImagePlacementAbsorber untuk melakukan pencarian penempatan gambar
ImagePlacementAbsorber abs = new ImagePlacementAbsorber();

// Terima absorber untuk semua halaman
doc.Pages.Accept(abs);

// Lakukan pengulangan melalui semua ImagePlacements, dapatkan gambar dan Properti ImagePlacement
foreach (ImagePlacement imagePlacement in abs.ImagePlacements)
{
    // Dapatkan gambar menggunakan objek ImagePlacement
    XImage image = imagePlacement.Image;

    // Tampilkan properti penempatan gambar untuk semua penempatan
    Console.Out.WriteLine("lebar gambar:" + imagePlacement.Rectangle.Width);
    Console.Out.WriteLine("tinggi gambar:" + imagePlacement.Rectangle.Height);
    Console.Out.WriteLine("gambar LLX:" + imagePlacement.Rectangle.LLX);
    Console.Out.WriteLine("gambar LLY:" + imagePlacement.Rectangle.LLY);
    Console.Out.WriteLine("resolusi horizontal gambar:" + imagePlacement.Resolution.X);
    Console.Out.WriteLine("resolusi vertikal gambar:" + imagePlacement.Resolution.Y);
}
```
Untuk mendapatkan gambar dari halaman individual, gunakan kode berikut:

```csharp
// Untuk contoh lengkap dan berkas data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
doc.Pages[1].Accept(abs);
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
                "contactType": "penjualan",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "penjualan",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "penjualan",
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
    "applicationCategory": "Perpustakaan Manipulasi PDF untuk .NET",
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

