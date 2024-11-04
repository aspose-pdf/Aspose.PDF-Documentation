---
title: Menambahkan Objek Kurva ke Berkas PDF
linktitle: Tambah Kurva
type: docs
weight: 30
url: /net/add-curve/
description: Artikel ini menjelaskan bagaimana cara membuat objek kurva pada PDF Anda menggunakan Aspose.PDF untuk .NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Menambahkan Objek Kurva ke Berkas PDF",
    "alternativeHeadline": "Cara Membuat Objek Kurva dalam Berkas PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pembuatan dokumen pdf",
    "keywords": "pdf, .net, kurva di pdf",
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
    "url": "/net/add-curve/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-curve/"
    },
    "dateModified": "2022-02-04",
    "description": "Artikel ini menjelaskan bagaimana cara membuat objek kurva pada PDF Anda menggunakan Aspose.PDF untuk .NET."
}
</script>
Potongan kode berikut juga bekerja dengan perpustakaan [Aspose.PDF.Drawing](/pdf/net/drawing/).

## Tambahkan Objek Kurva

Grafik [Curve](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/curve) adalah gabungan terhubung dari garis proyektif, setiap garis bertemu tiga lainnya di titik ganda biasa.

Aspose.PDF untuk .NET menunjukkan cara menggunakan kurva Bézier dalam Grafik Anda.
Kurva Bézier banyak digunakan dalam grafis komputer untuk memodelkan kurva yang halus. Kurva ini sepenuhnya terkandung dalam cangkang cembung titik kontrolnya, titik-titik tersebut dapat ditampilkan secara grafis dan digunakan untuk memanipulasi kurva secara intuitif.
Seluruh kurva terkandung dalam segi empat yang sudutnya adalah empat titik yang diberikan (cangkang cembung mereka).

Dalam artikel ini, kita akan menyelidiki kurva grafik sederhana, dan kurva yang diisi, yang dapat Anda buat dalam dokumen PDF Anda.

Ikuti langkah-langkah di bawah ini:

1. Buat instansi [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document)
1. Atur [Border](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/graph/properties/border) untuk objek Drawing

1. Tambahkan objek [Graph](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/graph) ke koleksi paragraf halaman

1. Simpan file PDF kita

```csharp
 public static void ExampleCurve()
        {
            // Create Document instance
            var document = new Document();

            // Add page to pages collection of PDF file
            var page = document.Pages.Add();

            // Create Drawing object with certain dimensions
            var graph = new Aspose.Pdf.Drawing.Graph(400, 200);

            // Set border for Drawing object
            var borderInfo = new BorderInfo(BorderSide.All, Color.Green);
            graph.Border = borderInfo;

            var curve1 = new Curve(new float[] { 10, 10, 50, 60, 70, 10, 100, 120 });
            curve1.GraphInfo.Color = Color.GreenYellow;
            graph.Shapes.Add(curve1);

            // Add Graph object to paragraphs collection of page
            page.Paragraphs.Add(graph);

            // Save PDF file
            document.Save(_dataDir + "DrawingCurve1_out.pdf");
        }
```
Gambar berikut menunjukkan hasil yang dieksekusi dengan potongan kode kami:

![Drawing Curve](drawing_curve.png)

## Membuat Objek Kurva yang Terisi

Contoh ini menunjukkan cara menambahkan objek Kurva yang diisi dengan warna.

```csharp
      public static void CurveFilled()
        {
            // Membuat instance Dokumen
            var document = new Document();

            // Menambahkan halaman ke koleksi halaman dari file PDF
            var page = document.Pages.Add();

            // Membuat objek Gambar dengan dimensi tertentu
            var graph = new Aspose.Pdf.Drawing.Graph(400, 200);

            // Mengatur batas untuk objek Gambar
            var borderInfo = new BorderInfo(BorderSide.All, Color.Green);
            graph.Border = borderInfo;

            var curve1 = new Curve(new float[] { 10, 10, 50, 60, 70, 10, 100, 120 });
            curve1.GraphInfo.FillColor = Color.GreenYellow;
            graph.Shapes.Add(curve1);

            // Menambahkan objek Grafik ke koleksi paragraf dari halaman
            page.Paragraphs.Add(graph);

            // Menyimpan file PDF
            document.Save(_dataDir + "DrawingCurve2_out.pdf");
        }
```
Lihat hasil penambahan Kurva Terisi:

![Kurva Terisi](filled_curve.png)

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

