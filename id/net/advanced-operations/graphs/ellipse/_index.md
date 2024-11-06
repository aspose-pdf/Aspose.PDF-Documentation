---
title: Menambahkan Objek Elips ke File PDF
linktitle: Tambah Elips
type: docs
weight: 60
url: id/net/add-ellipse/
description: Artikel ini menjelaskan cara membuat objek Elips pada PDF Anda menggunakan Aspose.PDF untuk .NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Menambahkan Objek Elips ke File PDF",
    "alternativeHeadline": "Cara Membuat Objek Elips dalam File PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pembuatan dokumen pdf",
    "keywords": "pdf, c#, elips dalam pdf",
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
    "url": "/net/add-ellipse/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-ellipse/"
    },
    "dateModified": "2022-02-04",
    "description": "Artikel ini menjelaskan cara membuat objek Elips pada PDF Anda menggunakan Aspose.PDF untuk .NET."
}
</script>

Potongan kode berikut juga berfungsi dengan perpustakaan [Aspose.PDF.Drawing](/pdf/net/drawing/).

## Tambahkan objek Ellipse

Aspose.PDF untuk .NET mendukung penambahan objek [Ellipse](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/ellipse) ke dokumen PDF. Ini juga menawarkan fitur untuk mengisi objek elips dengan warna tertentu.

```csharp
 public static void Ellipse()
        {
            // Buat instance Dokumen
            var document = new Document();

            // Tambahkan halaman ke koleksi halaman dari file PDF
            var page = document.Pages.Add();

            // Buat objek Drawing dengan dimensi tertentu
            var graph = new Aspose.Pdf.Drawing.Graph(400, 400);

            // Atur batas untuk objek Drawing
            var borderInfo = new BorderInfo(BorderSide.All, Color.Green);
            graph.Border = borderInfo;

            var ellipse1 = new Ellipse(150, 100, 120, 60);
            ellipse1.GraphInfo.Color = Color.GreenYellow;
            ellipse1.Text = new TextFragment("Ellipse");
            graph.Shapes.Add(ellipse1);

            var ellipse2 = new Ellipse(50, 50, 18, 300);
            ellipse2.GraphInfo.Color = Color.DarkRed;

            graph.Shapes.Add(ellipse2);

            // Tambahkan objek Graph ke koleksi paragraf halaman
            page.Paragraphs.Add(graph);

            // Simpan file PDF
            document.Save(_dataDir + "DrawingEllipse_out.pdf");

        }
```
![Tambah Elips](ellipse.png)

## Membuat Objek Elips Berisi

Potongan kode berikut menunjukkan cara menambahkan objek [Elips](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/ellipse) yang diisi dengan warna.

```csharp
     public static void EllipseFilled()
        {
            // Membuat instansi Dokumen
            var document = new Document();

            // Menambahkan halaman ke koleksi halaman file PDF
            var page = document.Pages.Add();

            // Membuat objek Gambar dengan dimensi tertentu
            var graph = new Aspose.Pdf.Drawing.Graph(400, 400);

            // Menetapkan batas untuk objek Gambar
            var borderInfo = new BorderInfo(BorderSide.All, Color.Green);
            graph.Border = borderInfo;

            var ellipse1 = new Ellipse(100, 100, 120, 180);
            ellipse1.GraphInfo.FillColor = Color.GreenYellow;
            graph.Shapes.Add(ellipse1);

            var ellipse2 = new Ellipse(200, 150, 180, 120);
            ellipse2.GraphInfo.FillColor = Color.DarkRed;
            graph.Shapes.Add(ellipse2);

            // Menambahkan objek Grafik ke koleksi paragraf halaman
            page.Paragraphs.Add(graph);

            // Menyimpan file PDF
            document.Save(_dataDir + "DrawingEllipse_out.pdf");
        }
```
![Filled Ellipse](fill_ellipse.png)

## Tambahkan Teks di Dalam Elips

Aspose.PDF untuk .NET mendukung penambahan teks di dalam Objek Grafik. Properti Teks dari Objek Grafik memberikan opsi untuk mengatur teks dari Objek Grafik. Cuplikan kode berikut menunjukkan cara menambahkan teks di dalam objek Persegi Panjang.

```csharp
        public static void EllipseWithText()
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

            var textFragment = new TextFragment("Ellipse");
            textFragment.TextState.Font = FontRepository.FindFont("Helvetica");
            textFragment.TextState.FontSize = 24;

            var ellipse1 = new Ellipse(100, 100, 120, 180);
            ellipse1.GraphInfo.FillColor = Color.GreenYellow;
            ellipse1.Text = textFragment;
            graph.Shapes.Add(ellipse1);


            var ellipse2 = new Ellipse(200, 150, 180, 120);
            ellipse2.GraphInfo.FillColor = Color.DarkRed;
            ellipse2.Text = textFragment;
            graph.Shapes.Add(ellipse2);

            // Tambahkan objek Grafik ke koleksi paragraf halaman
            page.Paragraphs.Add(graph);

            // Simpan file PDF
            document.Save(_dataDir + "DrawingEllipseText_out.pdf");

        }
 ```
![Teks di dalam Elips](text_ellipse.png)

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

