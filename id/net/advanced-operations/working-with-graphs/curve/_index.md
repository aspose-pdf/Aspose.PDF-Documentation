---
title: Tambahkan Objek Kurva ke file PDF
linktitle: Tambahkan Kurva
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 30
url: /id/net/add-curve/
description: Artikel ini menjelaskan cara membuat objek kurva ke PDF Anda menggunakan Aspose.PDF for .NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Add Curve Object to PDF file",
    "alternativeHeadline": "Create Curves in PDFs",
    "abstract": "Fitur baru dalam Aspose.PDF for .NET memungkinkan pengembang untuk membuat dan memanipulasi objek kurva dalam dokumen PDF, memanfaatkan kurva Bezier untuk grafik yang halus. Peningkatan ini memfasilitasi desain kurva sederhana dan terisi, menyediakan alat yang kuat untuk menghasilkan representasi visual yang kompleks dalam PDF sambil mempertahankan kontrol atas dimensi dan gaya.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Add Curve, Curve object, Bezier curves, Aspose.PDF for .NET, PDF document generation, Drawing object, Filled Curve, Graph object, PDF manipulation, ASP.NET PDF",
    "wordcount": "500",
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
    "url": "/net/add-curve/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-curve/"
    },
    "dateModified": "2024-11-25",
    "description": "Artikel ini menjelaskan cara membuat objek kurva ke PDF Anda menggunakan Aspose.PDF for .NET."
}
</script>

Potongan kode berikut juga bekerja dengan pustaka [Aspose.PDF.Drawing](/pdf/id/net/drawing/).

## Tambahkan objek Kurva

Sebuah grafik [Kurva](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/curve) adalah gabungan terhubung dari garis proyektif, setiap garis bertemu dengan tiga garis lainnya di titik ganda biasa.

Aspose.PDF for .NET menunjukkan cara menggunakan kurva Bézier dalam Grafik Anda.
Kurva Bézier banyak digunakan dalam grafik komputer untuk memodelkan kurva yang halus. Kurva sepenuhnya terkandung dalam cangkang cembung dari titik kontrolnya, titik-titik tersebut dapat ditampilkan secara grafis dan digunakan untuk memanipulasi kurva secara intuitif.
Seluruh kurva terkandung dalam segi empat yang sudutnya adalah empat titik yang diberikan (cangkang cembung mereka).

Dalam artikel ini, kita akan menyelidiki kurva grafik sederhana, dan kurva terisi, yang dapat Anda buat dalam dokumen PDF Anda.

Ikuti langkah-langkah di bawah ini:

1. Buat instance [Dokumen](https://reference.aspose.com/pdf/net/aspose.pdf/document).
1. Buat [objek Gambar](https://reference.aspose.com/pdf/net/aspose.pdf.drawing) dengan dimensi tertentu.
1. Atur [Batas](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/graph/properties/border) untuk objek Gambar.
1. Tambahkan objek [Grafik](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/graph) ke koleksi paragraf halaman.
1. Simpan file PDF kita.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExampleCurve()
{
    // The path to the document directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();

        // Create Drawing object with certain dimensions
        var graph = new Aspose.Pdf.Drawing.Graph(400, 200);

        // Set border for Drawing object
        var borderInfo = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, Aspose.Pdf.Color.Green);
        graph.Border = borderInfo;

        // Create a curve and set its properties
        var curve1 = new Aspose.Pdf.Drawing.Curve(new float[] { 10, 10, 50, 60, 70, 10, 100, 120 })
        {
            GraphInfo = 
            { 
                Color = Aspose.Pdf.Color.GreenYellow 
            }
        };

        // Add the curve to the graph shapes
        graph.Shapes.Add(curve1);

        // Add Graph object to paragraphs collection of page
        page.Paragraphs.Add(graph);

        // Save PDF document
        document.Save(dataDir + "DrawingCurve1_out.pdf");
    }
}

```

Gambar berikut menunjukkan hasil yang dieksekusi dengan potongan kode kita:

![Menggambar Kurva](drawing_curve.png)

## Buat Objek Kurva Terisi

Contoh ini menunjukkan cara menambahkan objek Kurva yang terisi dengan warna.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CurveFilled()
{
    // The path to the document directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();

        // Create Drawing object with certain dimensions
        var graph = new Aspose.Pdf.Drawing.Graph(400, 200);

        // Set border for Drawing object
        var borderInfo = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, Aspose.Pdf.Color.Green);
        graph.Border = borderInfo;

        // Create a curve and set fill color
        var curve1 = new Aspose.Pdf.Drawing.Curve(new float[] { 10, 10, 50, 60, 70, 10, 100, 120 })
        {
            GraphInfo = 
            { 
                FillColor = Aspose.Pdf.Color.GreenYellow 
            }
        };

        // Add the curve to the graph shapes
        graph.Shapes.Add(curve1);

        // Add Graph object to paragraphs collection of page
        page.Paragraphs.Add(graph);

        // Save PDF document
        document.Save(dataDir + "DrawingCurve2_out.pdf");
    }
}
```

Lihat hasil penambahan Kurva terisi:

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