---
title: Menambahkan Objek Garis ke File PDF
linktitle: Menambahkan Garis
type: docs
weight: 40
url: /net/add-line/
description: Artikel ini menjelaskan cara membuat objek garis pada PDF Anda menggunakan Aspose.PDF untuk .NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Menambahkan Objek Garis ke File PDF",
    "alternativeHeadline": "Cara Membuat Objek Garis dalam File PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pembuatan dokumen pdf",
    "keywords": "pdf, c#, garis dalam pdf",
    "wordcount": "302",
    "proficiencyLevel":"Pemula",
    "publisher": {
        "@type": "Organization",
        "name": "Tim Dokumentasi Aspose.PDF",
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
    "url": "/net/add-line/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-line/"
    },
    "dateModified": "2022-02-04",
    "description": "Artikel ini menjelaskan cara membuat objek garis pada PDF Anda menggunakan Aspose.PDF untuk .NET."
}
</script>

Potongan kode berikut juga bekerja dengan perpustakaan [Aspose.PDF.Drawing](/pdf/net/drawing/).

## Tambahkan objek Garis

Aspose.PDF untuk .NET mendukung fitur untuk menambahkan objek grafik (misalnya grafik, garis, persegi panjang, dll.) ke dokumen PDF. Anda juga mendapatkan keuntungan untuk menambahkan objek [Garis](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/line) di mana Anda juga dapat menentukan pola garis putus-putus, warna, dan format lainnya untuk elemen Garis.

Ikuti langkah-langkah di bawah ini:

1. Buat dokumen PDF [Baru](https://reference.aspose.com/pdf/net/aspose.pdf/document)

1. Tambahkan [Halaman](https://reference.aspose.com/pdf/net/aspose.pdf/page) ke koleksi halaman file PDF

1. Buat instance [Grafik](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/graph).

1. Tambahkan objek Grafik ke koleksi paragraf dari instance halaman.

1. Buat instance [Persegi Panjang](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/rectangle).

1. Atur lebar garis.
1. Simpan file PDF Anda.

Potongan kode berikut menunjukkan cara menambahkan objek [Rectangle](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/rectangle) yang diisi dengan warna.

```csharp
        public static void AddLineObjectToPDF()
        {
            // Buat instansi Dokumen
            var document = new Document();

            // Tambahkan halaman ke koleksi halaman file PDF
            var page = document.Pages.Add();

            // Buat instansi Grafik
            var graph = new Aspose.Pdf.Drawing.Graph(100, 400);

            // Tambahkan objek grafik ke koleksi paragraf dari instansi halaman
            page.Paragraphs.Add(graph);

            // Buat instansi Rectangle
            var line = new Line(new float[] { 100, 100, 200, 100 });

            // Tentukan warna isian untuk objek Grafik
            line.GraphInfo.DashArray = new int[] { 0, 1, 0 };
            line.GraphInfo.DashPhase = 1;

            // Tambahkan objek rectangle ke koleksi bentuk dari objek Grafik
            graph.Shapes.Add(line);

            // Simpan file PDF
            document.Save(_dataDir + "AddLineObject_out.pdf");
        }
```
![Add Line](add_line.png)

## Cara Menambahkan Garis Putus-Putus ke Dokumen PDF Anda

```csharp
        public static void DashLengthInBlackAndDashLengthInWhite()
        {
            // Buat instance Dokumen
            var document = new Document();

            // Tambahkan halaman ke koleksi halaman file PDF
            var page = document.Pages.Add();

            // Buat objek Menggambar dengan dimensi tertentu
            var canvas = new Aspose.Pdf.Drawing.Graph(100, 400);
            // Tambahkan objek gambar ke koleksi paragraf dari instance halaman
            page.Paragraphs.Add(canvas);

            // Buat objek Garis
            var line = new Line(new float[] { 100, 100, 200, 100 });
            // Atur warna untuk objek Garis
            line.GraphInfo.Color = Color.Red;
            // Tentukan array dash untuk objek garis
            line.GraphInfo.DashArray = new int[] { 0, 1, 0 };
            // Atur fase dash untuk instance Garis
            line.GraphInfo.DashPhase = 1;
            // Tambahkan garis ke koleksi bentuk dari objek gambar
            canvas.Shapes.Add(line);
            // Simpan file PDF
            document.Save(_dataDir + "DashLengthInBlackAndDashLengthInWhite_out.pdf");
        }
```
Mari kita periksa hasilnya:

![Garis Putus-Putus](dash_line.png)

## Gambar Garis Melintang di Halaman

Kita juga dapat menggunakan objek garis untuk menggambar garis silang yang dimulai dari sudut Kiri-Bawah ke sudut Kanan-Atas dan dari sudut Kiri-Atas ke sudut Kanan-Bawah.

Silakan lihat potongan kode berikut untuk mencapai kebutuhan ini.

```csharp
   public static void ExampleLineAcrossPage()
        {

            // Buat instansi Dokumen
            var document = new Document();

            // Tambahkan halaman ke koleksi halaman dari file PDF
            var page = document.Pages.Add();
            // Atur margin halaman di semua sisi menjadi 0

            page.PageInfo.Margin.Left = 0;
            page.PageInfo.Margin.Right = 0;
            page.PageInfo.Margin.Bottom = 0;
            page.PageInfo.Margin.Top = 0;

            // Buat objek Grafik dengan Lebar dan Tinggi sama dengan dimensi halaman
            var graph = new Aspose.Pdf.Drawing.Graph(
                (float)page.PageInfo.Width,
                (float)page.PageInfo.Height);

            // Buat objek garis pertama yang dimulai dari sudut Kiri-Bawah ke sudut Kanan-Atas halaman
            var line = new Line(
                    new float[]{
                        (float)page.Rect.LLX, 0,
                        (float)page.PageInfo.Width,
                        (float)page.Rect.URY });

            // Tambahkan garis ke koleksi bentuk dari objek Grafik
            graph.Shapes.Add(line);
            // Gambar garis dari sudut Kiri-Atas halaman ke sudut Kanan-Bawah halaman
            var line2 = new Line(
                new float[]{ 0,
                    (float) page.Rect.URY,
                    (float) page.PageInfo.Width,
                    (float) page.Rect.LLX });

            // Tambahkan garis ke koleksi bentuk dari objek Grafik
            graph.Shapes.Add(line2);

            // Tambahkan objek Grafik ke koleksi paragraf halaman
            page.Paragraphs.Add(graph);

            // Simpan file PDF
            document.Save(_dataDir + "ExampleLineAcrossPage_out.pdf");
        }
```
![Garis Gambar](draw_line.png)

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

