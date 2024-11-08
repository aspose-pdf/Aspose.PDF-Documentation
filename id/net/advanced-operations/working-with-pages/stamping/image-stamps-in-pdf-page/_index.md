---
title: Tambahkan Cap Gambar di PDF menggunakan C#
linktitle: Cap Gambar dalam Berkas PDF
type: docs
weight: 10
url: /id/net/image-stamps-in-pdf-page/
description: Tambahkan Cap Gambar dalam dokumen PDF Anda menggunakan kelas ImageStamp dengan pustaka Aspose.PDF.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Tambahkan Cap Gambar di PDF menggunakan C#",
    "alternativeHeadline": "Tambahkan Cap Gambar di PDF menggunakan C#",
    "author": {
        "@type": "Person",
        "name":"Andriy Andrukhovskiy",
        "givenName": "Andriy",
        "familyName": "Andrukhovskiy",
        "url":"https://www.linkedin.com/in/andruhovski/"
    },
    "genre": "generasi dokumen pdf",
    "keywords": "pdf, c#, generasi dokumen",
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
    "dateModified": "2022-02-04",
    "description": "Tambahkan Cap Gambar dalam dokumen PDF Anda menggunakan kelas ImageStamp dengan pustaka Aspose.PDF."
}
</script>
## Tambahkan Cap Gambar di File PDF

Anda dapat menggunakan kelas ImageStamp untuk menambahkan cap gambar ke file PDF. Kelas ImageStamp menyediakan properti yang diperlukan untuk membuat cap berbasis gambar, seperti tinggi, lebar, keburaman, dan sebagainya.

Potongan kode berikut ini juga berfungsi dengan pustaka [Aspose.PDF.Drawing](/pdf/id/net/drawing/).

Untuk menambahkan cap gambar:

1. Buat objek Dokumen dan objek ImageStamp menggunakan properti yang dibutuhkan.
1. Panggil metode AddStamp dari kelas Halaman untuk menambahkan cap ke PDF.

Potongan kode berikut menunjukkan cara menambahkan cap gambar dalam file PDF.

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

// Buka dokumen
Document pdfDocument = new Document(dataDir+ "AddImageStamp.pdf");

// Buat cap gambar
ImageStamp imageStamp = new ImageStamp(dataDir + "aspose-logo.jpg");
imageStamp.Background = true;
imageStamp.XIndent = 100;
imageStamp.YIndent = 100;
imageStamp.Height = 300;
imageStamp.Width = 300;
imageStamp.Rotate = Rotation.on270;
imageStamp.Opacity = 0.5;
// Tambahkan cap ke halaman tertentu
pdfDocument.Pages[1].AddStamp(imageStamp);

dataDir = dataDir + "AddImageStamp_out.pdf";
// Simpan dokumen keluaran
pdfDocument.Save(dataDir);
```
## Mengontrol Kualitas Gambar Saat Menambahkan Stempel

Saat menambahkan gambar sebagai objek stempel, Anda dapat mengontrol kualitas gambar tersebut. Properti Quality dari kelas ImageStamp digunakan untuk tujuan ini. Properti tersebut menunjukkan kualitas gambar dalam persentase (nilai valid adalah 0..100).

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Lokasi direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

// Buka dokumen
Document pdfDocument = new Document(dataDir+ "AddImageStamp.pdf");

// Buat stempel gambar
ImageStamp imageStamp = new ImageStamp(dataDir + "aspose-logo.jpg");

imageStamp.Quality = 10;
pdfDocument.Pages[1].AddStamp(imageStamp);
pdfDocument.Save(dataDir + "ControlImageQuality_out.pdf");
```

## Stempel Gambar sebagai Latar Belakang di Kotak Mengambang

API Aspose.PDF memungkinkan Anda menambahkan stempel gambar sebagai latar belakang di dalam kotak mengambang.
API Aspose.PDF memungkinkan Anda menambahkan cap gambar sebagai latar belakang dalam kotak mengambang.

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

// Instansiasi objek Dokumen
Document doc = new Document();
// Tambahkan halaman ke dokumen PDF
Page page = doc.Pages.Add();
// Buat objek FloatingBox
FloatingBox aBox = new FloatingBox(200, 100);
// Atur posisi kiri untuk FloatingBox
aBox.Left = 40;
// Atur posisi Atas untuk FloatingBox
aBox.Top = 80;
// Atur perataan horizontal untuk FloatingBox
aBox.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Center;
// Tambahkan fragmen teks ke koleksi paragraf dari FloatingBox
aBox.Paragraphs.Add(new TextFragment("main text"));
// Atur batas untuk FloatingBox
aBox.Border = new BorderInfo(BorderSide.All, Aspose.Pdf.Color.Red);
// Tambahkan gambar latar belakang
aBox.BackgroundImage = new Image
{
    File = dataDir + "aspose-logo.jpg"
};
// Atur warna latar belakang untuk FloatingBox
aBox.BackgroundColor = Aspose.Pdf.Color.Yellow;
// Tambahkan FloatingBox ke koleksi paragraf dari objek halaman
page.Paragraphs.Add(aBox);
// Simpan dokumen PDF
doc.Save(dataDir + "AddImageStampAsBackgroundInFloatingBox_out.pdf");
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
                "areaServed": "AS",
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
```

