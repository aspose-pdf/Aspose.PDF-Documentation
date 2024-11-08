---
title: Tambahkan Objek Persegi Panjang ke File PDF
linktitle: Tambah Persegi Panjang
type: docs
weight: 50
url: /id/net/add-rectangle/
description: Artikel ini menjelaskan cara membuat objek Persegi Panjang pada PDF Anda menggunakan Aspose.PDF untuk .NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Tambahkan Objek Persegi Panjang ke File PDF",
    "alternativeHeadline": "Cara membuat Objek Persegi Panjang di File PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pembuatan dokumen pdf",
    "keywords": "pdf, c#, persegi panjang di pdf",
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
    "url": "/net/add-rectangle/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-rectangle/"
    },
    "dateModified": "2022-02-04",
    "description": "Artikel ini menjelaskan cara membuat objek Persegi Panjang pada PDF Anda menggunakan Aspose.PDF untuk .NET."
}
</script>

Kode berikut juga berfungsi dengan perpustakaan [Aspose.PDF.Drawing](/pdf/id/net/drawing/).

## Tambahkan objek Rectangle

Aspose.PDF untuk .NET mendukung fitur untuk menambahkan objek grafis (misalnya grafik, garis, persegi panjang, dll.) ke dokumen PDF. Anda juga mendapatkan keuntungan untuk menambahkan objek [Rectangle](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/rectangle) di mana Anda juga menawarkan fitur untuk mengisi objek persegi panjang dengan warna tertentu, mengontrol Z-Order, menambahkan pengisian warna gradien, dan lainnya.

Pertama, mari kita lihat kemungkinan membuat objek Rectangle.

Ikuti langkah-langkah di bawah ini:

1. Buat [Dokumen](https://reference.aspose.com/pdf/net/aspose.pdf/document) PDF baru

1. Tambahkan [Halaman](https://reference.aspose.com/pdf/net/aspose.pdf/page) ke koleksi halaman file PDF

1. Tambahkan [Fragmen Teks](https://reference.aspose.com/pdf/net/aspose.pdf/texfragment) ke koleksi paragraf dari instansi halaman

1. Buat instansi [Grafik](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/graph)
1. Buat instance Rectangle

1. Tambahkan objek [Rectangle](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/rectangle) ke koleksi bentuk dari objek Graph

1. Tambahkan objek graph ke koleksi paragraf dari instance halaman

1. Tambahkan [Fragmen Teks](https://reference.aspose.com/pdf/net/aspose.pdf/texfragment) ke koleksi paragraf dari instance halaman

1. Dan simpan file PDF Anda

```csharp
 private static void AddRectangle(Page page, float x, float y, float width, float height, Color color, int zindex)
        {
            // Membuat objek graph dengan dimensi yang sama seperti yang ditentukan untuk objek Rectangle
            Aspose.Pdf.Drawing.Graph graph = new Aspose.Pdf.Drawing.Graph(width, height)
            {
                // Dapatkah kita mengubah posisi dari instance graph
                IsChangePosition = false,
                // Setel posisi koordinat Kiri untuk instance Graph
                Left = x,
                // Setel posisi koordinat Atas untuk objek Graph
                Top = y
            };
            // Tambahkan sebuah persegi panjang di dalam "graph"
            Rectangle rect = new Rectangle(0, 0, width, height);
            // Setel warna pengisian persegi panjang
            rect.GraphInfo.FillColor = color;
            // Warna dari objek graph
            rect.GraphInfo.Color = color;
            // Tambahkan persegi panjang ke koleksi bentuk dari instance graph
            graph.Shapes.Add(rect);
            // Setel Z-Index untuk objek persegi panjang
            graph.ZIndex = zindex;
            // Tambahkan graph ke koleksi paragraf dari objek halaman
            page.Paragraphs.Add(graph);
        }
```
![Buat Persegi Panjang](create_rectangle.png)

## Buat Objek Persegi Panjang yang Terisi

Aspose.PDF untuk .NET juga menawarkan fitur untuk mengisi objek persegi panjang dengan warna tertentu.

Potongan kode berikut menunjukkan cara menambahkan objek [Persegi Panjang](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/rectangle) yang diisi dengan warna.

```csharp
    {
        private const string _dataDir = "C:\\Samples\\";
        public static void RectangleFilled()
        {
            // Buat instance Dokumen
            var doc = new Document();

            // Tambahkan halaman ke koleksi halaman file PDF
            var page = doc.Pages.Add();
            // Buat instance Grafik
            var graph = new Aspose.Pdf.Drawing.Graph(100, 400);

            // Tambahkan objek grafik ke koleksi paragraf dari instance halaman
            page.Paragraphs.Add(graph);

            // Buat instance Persegi Panjang
            var rect = new Rectangle(100, 100, 200, 120);

            // Tentukan warna isi untuk objek Grafik
            rect.GraphInfo.FillColor = Color.Red;

            // Tambahkan objek persegi panjang ke koleksi bentuk dari objek Grafik
            graph.Shapes.Add(rect);

            // Simpan file PDF
            doc.Save(_dataDir + "CreateFilledRectangle_out.pdf");
        }
```
Lihat hasil persegi panjang yang diisi dengan warna solid:

![Filled Rectangle](fill_rectangle.png)

## Menambahkan Gambar dengan Isian Gradien

Aspose.PDF for .NET mendukung fitur untuk menambahkan objek grafis ke dokumen PDF dan terkadang diperlukan untuk mengisi objek grafis dengan Warna Gradien. Untuk mengisi objek grafis dengan Warna Gradien, kita perlu mengatur setPatterColorSpace dengan objek gradientAxialShading sebagai berikut.

Potongan kode berikut menunjukkan cara menambahkan objek [Rectangle](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/rectangle) yang diisi dengan Warna Gradien.

```csharp
 public static void CreateFilledRectangletGradientFill()
        {
            // Membuat instansi Dokumen
            var doc = new Document();

            // Menambahkan halaman ke koleksi halaman dari file PDF
            var page = doc.Pages.Add();
            // Membuat instansi Grafik
            var graph = new Aspose.Pdf.Drawing.Graph(400, 400);
            // Menambahkan objek grafik ke koleksi paragraf dari instansi halaman
            page.Paragraphs.Add(graph);
            // Membuat instansi Rectangle
            var rect = new Rectangle(0, 0, 300, 300);
            // Menentukan warna isian untuk Objek Grafik
            var gradientColor = new Color();
            var gradientSettings = new GradientAxialShading(Color.Red, Color.Blue)
            {
                Start = new Point(0, 0),
                End = new Point(350, 350)
            };
            gradientColor.PatternColorSpace = gradientSettings;
            rect.GraphInfo.FillColor = gradientColor;

            // Menambahkan objek persegi panjang ke koleksi bentuk dari Objek Grafik
            graph.Shapes.Add(rect);

            // Menyimpan file PDF
            doc.Save(_dataDir + "CreateFilledRectangle_out.pdf");
        }
```
![Gradient Rectangle](gradient.png)

## Membuat Persegi Panjang dengan Saluran Warna Alpha

Aspose.PDF untuk .NET mendukung pengisian objek persegi panjang dengan warna tertentu. Objek persegi panjang juga dapat memiliki saluran warna Alpha untuk memberikan tampilan transparan. Cuplikan kode berikut menunjukkan cara menambahkan objek [Rectangle](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/rectangle) dengan saluran warna Alpha.

Piksel gambar dapat menyimpan informasi tentang keopakannya bersama dengan nilai warna. Ini memungkinkan pembuatan gambar dengan area transparan atau semi-transparan.

Alih-alih membuat warna menjadi transparan, setiap piksel menyimpan informasi tentang seberapa buram itu. Data keburaman ini disebut saluran alpha dan biasanya disimpan setelah saluran warna dari piksel.

```csharp
     public static void RectangleFilled_AlphaChannel()
        {
            // Buat instance Dokumen
            var doc = new Document();

            // Tambahkan halaman ke koleksi halaman dari file PDF
            var page = doc.Pages.Add();
            // Buat instance Grafik
            var graph = new Aspose.Pdf.Drawing.Graph(100, 400);
            // Tambahkan objek grafik ke koleksi paragraf dari instance halaman
            page.Paragraphs.Add(graph);
            // Buat instance Persegi Panjang
            var rect = new Rectangle(100, 100, 200, 120);
            // Tentukan warna isi untuk objek Grafik
            rect.GraphInfo.FillColor = Color.FromArgb(128, 244, 180, 0);

            // Tambahkan objek persegi panjang ke koleksi bentuk dari objek Grafik
            graph.Shapes.Add(rect);

            // Buat objek persegi panjang kedua
            var rect1 = new Rectangle(200, 150, 200, 100);
            rect1.GraphInfo.FillColor = Color.FromArgb(160, 120, 0, 120);
            graph.Shapes.Add(rect1);

            // Tambahkan instance grafik ke koleksi paragraf dari objek halaman
            page.Paragraphs.Add(graph);

            // Simpan file PDF
            doc.Save(_dataDir + "CreateFilledRectangle_out.pdf");
        }
```
![Rectangle Alpha Channel Color](rectangle_color.png)

## Mengontrol Urutan Z-Order dari Rectangle

Aspose.PDF untuk .NET mendukung fitur untuk menambahkan objek grafis (misalnya grafik, garis, persegi panjang, dll.) ke dokumen PDF. Saat menambahkan lebih dari satu instansi objek yang sama ke dalam file PDF, kita dapat mengontrol rendering mereka dengan menentukan Z-Order. Z-Order juga digunakan saat kita perlu me-render objek di atas objek lain.

Potongan kode berikut menunjukkan langkah-langkah untuk me-render objek [Rectangle](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/rectangle) di atas satu sama lain.

```csharp
 public static void AddRectangleZOrder()
        {
            // Instansiasi objek kelas Document
            Document doc1 = new Document();
            /// Tambahkan halaman ke koleksi halaman file PDF
            Page page1 = doc1.Pages.Add();
            // Atur ukuran halaman PDF
            page1.SetPageSize(375, 300);
            // Atur margin kiri untuk objek halaman sebagai 0
            page1.PageInfo.Margin.Left = 0;
            // Atur margin atas dari objek halaman sebagai 0
            page1.PageInfo.Margin.Top = 0;
            // Buat persegi panjang baru dengan Warna sebagai Merah, Z-Order sebagai 0 dan dimensi tertentu
            AddRectangle(page1, 50, 40, 60, 40, Color.Red, 2);
            // Buat persegi panjang baru dengan Warna sebagai Biru, Z-Order sebagai 0 dan dimensi tertentu
            AddRectangle(page1, 20, 20, 30, 30, Color.Blue, 1);
            // Buat persegi panjang baru dengan Warna sebagai Hijau, Z-Order sebagai 0 dan dimensi tertentu
            AddRectangle(page1, 40, 40, 60, 30, Color.Green, 0);
            // Simpan file PDF hasil
            doc1.Save(_dataDir + "ControlRectangleZOrder_out.pdf");
        }
```
![Mengontrol Urutan Z](control.png)

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


