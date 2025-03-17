---
title: Periksa batas bentuk dalam koleksi Shapes
type: docs
weight: 70
url: /id/net/aspose-pdf-drawing-graph-shapes-bounds-check/
description: Pelajari cara memeriksa batas sebuah bentuk saat dimasukkan ke dalam koleksi Shapes untuk memastikan itu sesuai dengan wadah induknya.
lastmod: "2025-02-28"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Checking Element Bounds in Shapes Collection",
    "alternativeHeadline": "Configurable Bounds Checking for Aspose.PDF Shapes with Exception Mode",
    "abstract": "Fitur pemeriksaan batas baru dari Aspose.PDF for .NET dalam koleksi `Drawing.Graph.Shapes` secara otomatis memvalidasi dimensi elemen terhadap wadah induk, mencegah overflow tata letak. Ini memicu pengecualian ketika elemen melebihi batas wadah, menegakkan batas ukuran yang ketat selama penyisipan untuk memastikan format PDF yang tepat dan memperlancar akurasi desain",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "756",
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
    "url": "/net/aspose-pdf-drawing-graph-shapes-bounds-check/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/aspose-pdf-drawing-graph-shapes-bounds-check/"
    },
    "dateModified": "2025-03-17",
    "description": ""
}
</script>

## Pendahuluan
Dokumen ini memberikan panduan rinci tentang penggunaan fitur pemeriksaan batas dalam koleksi Shapes. Fitur ini memastikan bahwa elemen sesuai dengan wadah induknya dan dapat dikonfigurasi untuk memicu pengecualian jika komponen tidak sesuai. Kami akan menjelaskan langkah-langkah untuk menerapkan fungsionalitas ini dan memberikan contoh lengkap.

## Prasyarat
Anda akan memerlukan yang berikut:
* Visual Studio 2019 atau lebih baru
* Aspose.PDF for .NET 25.3 atau lebih baru
* Sebuah file PDF contoh yang berisi beberapa halaman

Anda dapat mengunduh pustaka Aspose.PDF for .NET dari situs web resmi atau menginstalnya menggunakan NuGet Package Manager di Visual Studio.

## Langkah-langkah
Berikut adalah langkah-langkah untuk menyelesaikan tugas:
1. Buat dokumen PDF.
2. Buat objek `Graph` dengan dimensi yang ditentukan.
3. Buat objek `Shape` dengan dimensi yang ditentukan.
4. Atur `BoundsCheckMode` ke `ThrowExceptionIfDoesNotFit`.
5. Coba tambahkan bentuk ke grafik.

Mari kita lihat bagaimana menerapkan langkah-langkah ini dalam kode C#.

### Langkah 1: Buat dokumen PDF
Pertama, buat dokumen PDF baru dan tambahkan halaman ke dalamnya.

```csharp
using (var doc = new Aspose.Pdf.Document())
{
    Aspose.Pdf.Page page = doc.Pages.Add();
}
```

### Langkah 2: Buat objek Graph dengan dimensi yang ditentukan
Selanjutnya, buat objek `Graph` dengan lebar dan tinggi 100 unit. Posisi grafik 10 unit dari atas dan 15 unit dari kiri halaman. Tambahkan batas hitam ke grafik.

```csharp
var graph = new Aspose.Pdf.Drawing.Graph(100d, 100d)
{
    Top = 10,
    Left = 15,
    Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.Box, 1F, Aspose.Pdf.Color.Black)
};
page.Paragraphs.Add(graph);
```

### Langkah 3: Buat objek Shape (misalnya, Rectangle) dengan dimensi yang ditentukan
Buat objek Rectangle dengan lebar dan tinggi 50 unit. Posisi persegi panjang di (-1, 0), yang berada di luar batas grafik.

```csharp
var rect = new Aspose.Pdf.Drawing.Rectangle(-1, 0, 50, 50)
{
    GraphInfo =
    {
        FillColor = Aspose.Pdf.Color.Tomato
    }
};
```

### Langkah 4: Atur BoundsCheckMode ke ThrowExceptionIfDoesNotFit
Atur `BoundsCheckMode` ke `ThrowExceptionIfDoesNotFit` untuk memastikan bahwa pengecualian dilemparkan jika persegi panjang tidak sesuai dengan grafik.

```csharp
graph.Shapes.UpdateBoundsCheckMode(Aspose.Pdf.BoundsCheckMode.ThrowExceptionIfDoesNotFit);
```

### Langkah 5: Tambahkan persegi panjang ke grafik
Tambahkan persegi panjang ke grafik. Ini akan memicu `Aspose.Pdf.BoundsOutOfRangeException` karena persegi panjang tidak sesuai dengan dimensi grafik.

```csharp
graph.Shapes.Add(rect);
```

## Output
Setelah menjalankan kode, output yang diharapkan adalah `Aspose.Pdf.BoundsOutOfRangeException` dengan pesan:

```
Bounds not fit. Container dimensions: 100x100
```

## Pemecahan Masalah
Jika terjadi masalah, berikut adalah beberapa tips:
* Pastikan bahwa `BoundsCheckMode` diatur dengan benar.
* Verifikasi bahwa dimensi elemen dan wadah akurat.
* Periksa posisi elemen dalam wadah.

## Contoh Lengkap
Di bawah ini adalah contoh lengkap yang menunjukkan semua langkah yang digabungkan:

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CheckShapeBounds()
{
    // Create PDF document
    using (var doc = new Aspose.Pdf.Document())
    {
        // Add page
        var page = doc.Pages.Add();
        
        // Create a Graph object with specified dimensions
        var graph = new Aspose.Pdf.Drawing.Graph(100d, 100d)
        {
            Top = 10,
            Left = 15,
            Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.Box, 1F, Aspose.Pdf.Color.Black)
        };
        page.Paragraphs.Add(graph);
        
        // Create a Shape object (for example, Rectangle) with specified dimensions
        var rect = new Aspose.Pdf.Drawing.Rectangle(-1, 0, 50, 50)
        {
            GraphInfo =
            {
                FillColor = Aspose.Pdf.Color.Tomato
            }
        };
        
        // Set the BoundsCheckMode to ThrowExceptionIfDoesNotFit
        graph.Shapes.UpdateBoundsCheckMode(Aspose.Pdf.BoundsCheckMode.ThrowExceptionIfDoesNotFit);
        
        // Add the rectangle to the graph
        graph.Shapes.Add(rect);
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CheckShapeBounds()
{
    // Create PDF document
    using var doc = new Aspose.Pdf.Document();
    
    // Add page
    var page = doc.Pages.Add();

    // Create a Graph object with specified dimensions
    var graph = new Aspose.Pdf.Drawing.Graph(100d, 100d)
    {
        Top = 10,
        Left = 15,
        Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.Box, 1F, Aspose.Pdf.Color.Black)
    };
    page.Paragraphs.Add(graph);

    // Create a Aspose.Pdf.Drawing.Shape object (for example, Aspose.Pdf.Drawing.Rectangle) with specified dimensions
    var rect = new Aspose.Pdf.Drawing.Rectangle(-1, 0, 50, 50)
    {
        GraphInfo =
        {
            FillColor = Aspose.Pdf.Color.Tomato
        }
    };

    // Set the BoundsCheckMode to ThrowExceptionIfDoesNotFit
    graph.Shapes.UpdateBoundsCheckMode(Aspose.Pdf.BoundsCheckMode.ThrowExceptionIfDoesNotFit);

    // Add the rectangle to the graph
    graph.Shapes.Add(rect);
}
```
{{< /tab >}}
{{< /tabs >}}

## Kesimpulan
Fitur pemeriksaan batas dalam koleksi Shapes adalah alat yang kuat untuk memastikan elemen sesuai dengan wadah induk. Anda dapat mencegah masalah tata letak dalam dokumen PDF Anda dengan mengatur BoundsCheckMode ke ThrowExceptionIfDoesNotFit. Fitur ini sangat berguna dalam skenario di mana penempatan dan ukuran elemen yang tepat sangat penting. Untuk detail lebih lanjut, kunjungi [dokumentasi resmi](https://docs.aspose.com/pdf/net/).