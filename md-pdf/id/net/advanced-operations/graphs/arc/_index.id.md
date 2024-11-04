---
title: Menambahkan Objek Busur ke File PDF
linktitle: Tambah Busur
type: docs
weight: 10
url: /net/add-arc/
description: Artikel ini menjelaskan cara membuat objek busur pada PDF Anda menggunakan Aspose.PDF untuk .NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Menambahkan Objek Busur ke File PDF",
    "alternativeHeadline": "Cara Membuat Busur dalam File PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pembuatan dokumen PDF",
    "keywords": "pdf, c#, busur di pdf",
    "wordcount": "302",
    "proficiencyLevel":"Pemula",
    "publisher": {
        "@type": "Organization",
        "name": "Tim Dokumen Aspose.PDF",
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
    "url": "/net/add-arc/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-arc/"
    },
    "dateModified": "2022-02-04",
    "description": "Artikel ini menjelaskan cara membuat objek busur pada PDF Anda menggunakan Aspose.PDF untuk .NET."
}
</script>

Berikut cuplikan kode juga berfungsi dengan perpustakaan [Aspose.PDF.Drawing](/pdf/net/drawing/).

## Tambahkan objek Arc

Aspose.PDF untuk .NET mendukung fitur untuk menambahkan objek grafik (misalnya grafik, garis, persegi panjang, dll.) ke dokumen PDF. Ini juga menawarkan fitur untuk mengisi objek arc dengan warna tertentu.

Ikuti langkah-langkah di bawah ini:

1. Buat instance [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document)

1. Buat [objek Drawing](https://reference.aspose.com/pdf/net/aspose.pdf.drawing) dengan dimensi tertentu

1. Atur [Border](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/graph/properties/border) untuk objek Drawing

1. Tambahkan objek [Graph](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/graph) ke koleksi paragraf halaman

1. Simpan file PDF kita

Cuplikan kode berikut menunjukkan cara menambahkan objek [Arc](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/arc).

```csharp
 public static void Arc()
        {
            // Buat instance Document
            var document = new Document();

            // Tambahkan halaman ke koleksi halaman file PDF
            var page = document.Pages.Add();

            // Buat objek Drawing dengan dimensi tertentu
            var graph = new Aspose.Pdf.Drawing.Graph(400, 400);
            // Atur border untuk objek Drawing
            var borderInfo = new BorderInfo(BorderSide.All, Color.Green);
            graph.Border = borderInfo;

            var arc1 = new Arc(100, 100, 95, 0, 90);
            arc1.GraphInfo.Color = Color.GreenYellow;
            graph.Shapes.Add(arc1);

            var arc2 = new Arc(100, 100, 90, 70, 180);
            arc2.GraphInfo.Color = Color.DarkBlue;
            graph.Shapes.Add(arc2);

            var arc3 = new Arc(100, 100, 85, 120, 210);
            arc3.GraphInfo.Color = Color.Red;
            graph.Shapes.Add(arc3);

            // Tambahkan objek Graph ke koleksi paragraf halaman
            page.Paragraphs.Add(graph);

            // Simpan file PDF
            document.Save(_dataDir + "DrawingArc_out.pdf");

        }
```
## Buat Objek Busur Terisi

Contoh berikut menunjukkan bagaimana menambahkan objek Busur yang diisi dengan warna dan dimensi tertentu.

```csharp
        public static void ArcFilled()
        {
            // Buat instance Dokumen
            var document = new Document();

            // Tambahkan halaman ke koleksi halaman file PDF
            var page = document.Pages.Add();

            // Buat objek Gambar dengan dimensi tertentu
            var graph = new Aspose.Pdf.Drawing.Graph(400, 400);
            // Atur batas untuk objek Gambar
            var borderInfo = new BorderInfo(BorderSide.All, Color.Green);
            graph.Border = borderInfo;

            var arc = new Arc(100, 100, 95, 0, 90);
            arc.GraphInfo.FillColor = Color.GreenYellow;
            graph.Shapes.Add(arc);

            var line = new Line(new float[] { 195, 100, 100, 100, 100, 195 });
            line.GraphInfo.FillColor = Color.GreenYellow;
            graph.Shapes.Add(line);

            // Tambahkan objek Grafik ke koleksi paragraf halaman
            page.Paragraphs.Add(graph);

            // Simpan file PDF
            document.Save(_dataDir + "ExampleFilledArc_out.pdf");

        }
```
Mari kita lihat hasil penambahan Busur yang diisi:

![Busur Yang Diisi](filled_arc.png)

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


