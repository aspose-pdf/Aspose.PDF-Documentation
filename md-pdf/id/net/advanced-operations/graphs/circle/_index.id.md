---
title: Menambahkan Objek Lingkaran ke File PDF
linktitle: Tambah Lingkaran
type: docs
weight: 20
url: /net/add-circle/
description: Artikel ini menjelaskan cara membuat objek lingkaran pada PDF Anda menggunakan Aspose.PDF untuk .NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Menambahkan Objek Lingkaran ke File PDF",
    "alternativeHeadline": "Cara Membuat Objek Lingkaran dalam File PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pembuatan dokumen pdf",
    "keywords": "pdf, c#, lingkaran dalam pdf",
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
    "url": "/net/add-circle/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-circle/"
    },
    "dateModified": "2022-02-04",
    "description": "Artikel ini menjelaskan cara membuat objek lingkaran pada PDF Anda menggunakan Aspose.PDF untuk .NET."
}
</script>
Potongan kode berikut juga bekerja dengan pustaka [Aspose.PDF.Drawing](/pdf/net/drawing/).

## Tambahkan Objek Lingkaran

Seperti grafik batang, grafik lingkaran dapat digunakan untuk menampilkan data dalam beberapa kategori terpisah. Namun, berbeda dengan grafik batang, grafik lingkaran hanya dapat digunakan ketika Anda memiliki data untuk semua kategori yang membentuk keseluruhan. Jadi, mari kita lihat cara menambahkan objek [Lingkaran](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/circle) dengan Aspose.PDF untuk .NET.

Ikuti langkah-langkah di bawah ini:

1. Buat instans [Dokumen](https://reference.aspose.com/pdf/net/aspose.pdf/document)

1. Buat [objek Gambar](https://reference.aspose.com/pdf/net/aspose.pdf.drawing) dengan dimensi tertentu

1. Atur [Batas](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/graph/properties/border) untuk objek Gambar

1. Tambahkan objek [Grafik](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/graph) ke koleksi paragraf halaman

1. Simpan file PDF kita

```csharp
        public static void Circle()
        {
            // Buat instans Dokumen
            var document = new Document();

            // Tambahkan halaman ke koleksi halaman file PDF
            var page = document.Pages.Add();

            // Buat objek Gambar dengan dimensi tertentu
            var graph = new Aspose.Pdf.Drawing.Graph(400, 200);
            // Atur batas untuk objek Gambar
            var borderInfo = new BorderInfo(BorderSide.All, Color.Green);
            graph.Border = borderInfo;

            var circle = new Circle(100, 100, 40);

            circle.GraphInfo.Color = Color.GreenYellow;
            graph.Shapes.Add(circle);

            // Tambahkan objek Grafik ke koleksi paragraf halaman
            page.Paragraphs.Add(graph);

            // Simpan file PDF
            document.Save(_dataDir + "DrawingCircle1_out.pdf");
        }
```
Lingkaran yang kita gambar akan terlihat seperti ini:

![Menggambar Lingkaran](drawing_circle.png)

## Membuat Objek Lingkaran Berisi

Contoh ini menunjukkan cara menambahkan objek Lingkaran yang diisi dengan warna.

```csharp
        public static void CircleFilled()
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

            var circle = new Circle(100, 100, 40);
            circle.GraphInfo.Color = Color.GreenYellow;
            circle.GraphInfo.FillColor = Color.Green;
            circle.Text = new TextFragment("Lingkaran");

            graph.Shapes.Add(circle);

            // Menambahkan objek Grafis ke koleksi paragraf halaman
            page.Paragraphs.Add(graph);

            // Menyimpan file PDF
            document.Save(_dataDir + "DrawingCircle2_out.pdf");
        }
```
Mari kita lihat hasil penambahan Lingkaran yang terisi:

![Lingkaran Terisi](filled_circle.png)

