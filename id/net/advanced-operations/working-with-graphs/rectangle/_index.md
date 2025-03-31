---
title: Tambahkan Objek Persegi Panjang ke file PDF
linktitle: Tambahkan Persegi Panjang
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 50
url: /id/net/add-rectangle/
description: Artikel ini menjelaskan cara membuat objek Persegi Panjang ke PDF Anda menggunakan Aspose.PDF for .NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Add Rectangle Object to PDF file",
    "alternativeHeadline": "Add Rectangle to PDF file",
    "abstract": "Fitur baru di Aspose.PDF for .NET memungkinkan pengguna untuk dengan mudah menambahkan objek Persegi Panjang ke dokumen PDF. Fungsionalitas ini mencakup opsi untuk menyesuaikan persegi panjang dengan warna solid, pengisian gradien, dan transparansi, memberikan kustomisasi visual yang lebih baik dan kontrol lapisan untuk konten PDF.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Add Rectangle, PDF document generation, Aspose.PDF for .NET, Rectangle object, fill rectangle, gradient color fill, Z-Order control, alpha channel color, graph objects in PDF, create filled rectangle",
    "wordcount": "1263",
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
    "url": "/net/add-rectangle/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-rectangle/"
    },
    "dateModified": "2024-11-25",
    "description": "Artikel ini menjelaskan cara membuat objek Persegi Panjang ke PDF Anda menggunakan Aspose.PDF for .NET."
}
</script>

Potongan kode berikut juga bekerja dengan pustaka [Aspose.PDF.Drawing](/pdf/id/net/drawing/).

## Tambahkan objek Persegi Panjang

Aspose.PDF for .NET mendukung fitur untuk menambahkan objek grafik (misalnya grafik, garis, persegi panjang, dll.) ke dokumen PDF. Anda juga mendapatkan keuntungan untuk menambahkan objek [Rectangle](https://reference.aspose.com/pdf/id/net/aspose.pdf.drawing/rectangle) di mana Anda juga menawarkan fitur untuk mengisi objek persegi panjang dengan warna tertentu, mengontrol Z-Order, menambahkan pengisian warna gradien, dan lain-lain.

Pertama, mari kita lihat kemungkinan membuat objek Persegi Panjang.

Ikuti langkah-langkah di bawah ini:

1. Buat PDF [Document](https://reference.aspose.com/pdf/id/net/aspose.pdf/document) baru.
1. Tambahkan [Page](https://reference.aspose.com/pdf/id/net/aspose.pdf/page) ke koleksi halaman file PDF.
1. Tambahkan [Text fragment](https://reference.aspose.com/pdf/id/net/aspose.pdf/texfragment) ke koleksi paragraf dari instance halaman.
1. Buat instance [Graph](https://reference.aspose.com/pdf/id/net/aspose.pdf.drawing/graph).
1. Atur batas untuk [Drawing object](https://reference.aspose.com/pdf/id/net/aspose.pdf.drawing).
1. Buat instance Persegi Panjang.

1. Tambahkan objek [Rectangle](https://reference.aspose.com/pdf/id/net/aspose.pdf.drawing/rectangle) ke koleksi bentuk dari objek Graph.
1. Tambahkan objek grafik ke koleksi paragraf dari instance halaman.
1. Tambahkan [Text fragment](https://reference.aspose.com/pdf/id/net/aspose.pdf/texfragment) ke koleksi paragraf dari instance halaman.

1. Dan simpan file PDF Anda.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddRectangle(Aspose.Pdf.Page page, float x, float y, float width, float height, Aspose.Pdf.Color color, int zIndex)
{
    // Create a Graph object with dimensions matching the specified rectangle
    var graph = new Aspose.Pdf.Drawing.Graph(width, height)
    {
        // Prevent the graph from repositioning automatically
        IsChangePosition = false,
        // Set the Left coordinate position for the Graph instance
        Left = x,
        // Set the Top coordinate position for the Graph instance
        Top = y
    };

    // Create a Rectangle object inside the Graph
    var rect = new Aspose.Pdf.Drawing.Rectangle(0, 0, width, height)
    {
        // Set the fill color of the rectangle
        GraphInfo =
        {
            FillColor = color,
            // Set the border color of the rectangle
            Color = color
        }
    };

    // Add the rectangle to the Shapes collection of the Graph
    graph.Shapes.Add(rect);

    // Set the Z-Index for the Graph object to control layering
    graph.ZIndex = zIndex;

    // Add the Graph object to the Paragraphs collection of the page
    page.Paragraphs.Add(graph);
}
```

![Buat Persegi Panjang](create_rectangle.png)

## Buat Objek Persegi Panjang Terisi

Aspose.PDF for .NET juga menawarkan fitur untuk mengisi objek persegi panjang dengan warna tertentu.

Potongan kode berikut menunjukkan cara menambahkan objek [Rectangle](https://reference.aspose.com/pdf/id/net/aspose.pdf.drawing/rectangle) yang diisi dengan warna.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void RectangleFilled()
{
    // The path to the documents directory directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();

        // Create Graph instance
        var graph = new Aspose.Pdf.Drawing.Graph(100, 400);

        // Add graph object to paragraphs collection of page instance
        page.Paragraphs.Add(graph);

        // Create Rectangle instance with specified dimensions
        var rect = new Aspose.Pdf.Drawing.Rectangle(100, 100, 200, 120)
        {
            // Specify fill color for the Rectangle object
            GraphInfo = 
            { 
                FillColor = Aspose.Pdf.Color.Red 
            }
        };

        // Add rectangle object to shapes collection of Graph object
        graph.Shapes.Add(rect);

        // Save PDF document
        document.Save(dataDir + "CreateFilledRectangle_out.pdf");
    }
}
```

Lihat hasil persegi panjang yang diisi dengan warna solid:

![Persegi Panjang Terisi](fill_rectangle.png)

## Tambahkan Gambar dengan Pengisian Gradien

Aspose.PDF for .NET mendukung fitur untuk menambahkan objek grafik ke dokumen PDF dan terkadang diperlukan untuk mengisi objek grafik dengan Warna Gradien. Untuk mengisi objek grafik dengan Warna Gradien, kita perlu mengatur setPatterColorSpace dengan objek gradientAxialShading seperti berikut.

Potongan kode berikut menunjukkan cara menambahkan objek [Rectangle](https://reference.aspose.com/pdf/id/net/aspose.pdf.drawing/rectangle) yang diisi dengan Warna Gradien.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CreateFilledRectangleGradientFill()
{
    // The path to the documents directory directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();

        // Create Graph instance
        var graph = new Aspose.Pdf.Drawing.Graph(400, 400);

        // Add graph object to paragraphs collection of page instance
        page.Paragraphs.Add(graph);

        // Create Rectangle instance
        var rect = new Aspose.Pdf.Drawing.Rectangle(0, 0, 300, 300);

        // Create a gradient fill color
        var gradientColor = new Aspose.Pdf.Color();
        var gradientSettings = new Aspose.Pdf.Drawing.GradientAxialShading(Aspose.Pdf.Color.Red, Aspose.Pdf.Color.Blue)
        {
            Start = new Aspose.Pdf.Point(0, 0),
            End = new Aspose.Pdf.Point(350, 350)
        };
        gradientColor.PatternColorSpace = gradientSettings;

        // Apply gradient fill color to the rectangle
        rect.GraphInfo.FillColor = gradientColor;

        // Add rectangle object to shapes collection of Graph object
        graph.Shapes.Add(rect);

        // Save PDF document
        document.Save(dataDir + "CreateFilledRectangleGradient_out.pdf");
    }
}
```

![Persegi Panjang Gradien](gradient.png)

## Buat Persegi Panjang dengan Saluran warna Alpha

Aspose.PDF for .NET mendukung pengisian objek persegi panjang dengan warna tertentu. Objek persegi panjang juga dapat memiliki saluran warna Alpha untuk memberikan penampilan transparan. Potongan kode berikut menunjukkan cara menambahkan objek [Rectangle](https://reference.aspose.com/pdf/id/net/aspose.pdf.drawing/rectangle) dengan saluran warna Alpha.

Piksel gambar dapat menyimpan informasi tentang opasitas mereka bersama dengan nilai warna. Ini memungkinkan pembuatan gambar dengan area transparan atau semi-transparan.

Alih-alih membuat warna transparan, setiap piksel menyimpan informasi tentang seberapa opak itu. Data opasitas ini disebut saluran alpha dan biasanya disimpan setelah saluran warna piksel.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void RectangleFilled_AlphaChannel()
{
    // The path to the documents directory directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();

        // Create Graph instance
        var graph = new Aspose.Pdf.Drawing.Graph(100, 400);

        // Add graph object to paragraphs collection of page instance
        page.Paragraphs.Add(graph);

        // Create first rectangle with alpha channel fill color
        var rect = new Aspose.Pdf.Drawing.Rectangle(100, 100, 200, 120)
        {
            GraphInfo = 
            { 
                FillColor = Aspose.Pdf.Color.FromArgb(128, 244, 180, 0) 
            }
        };

        // Add the first rectangle to the shapes collection of the Graph object
        graph.Shapes.Add(rect);

        // Create second rectangle with different alpha channel fill color
        var rect1 = new Aspose.Pdf.Drawing.Rectangle(200, 150, 200, 100)
        {
            GraphInfo = 
            { 
                FillColor = Aspose.Pdf.Color.FromArgb(160, 120, 0, 120) 
            }
        };

        // Add the second rectangle to the shapes collection of the Graph object
        graph.Shapes.Add(rect1);

        // Save PDF document
        document.Save(dataDir + "CreateFilledRectangle_out.pdf");
    }
}
```

![Warna Saluran Alpha Persegi Panjang](rectangle_color.png)

## Kontrol Z-Order dari Persegi Panjang

Aspose.PDF for .NET mendukung fitur untuk menambahkan objek grafik (misalnya grafik, garis, persegi panjang, dll.) ke dokumen PDF. Ketika menambahkan lebih dari satu instance dari objek yang sama di dalam file PDF, kita dapat mengontrol rendering mereka dengan menentukan Z-Order. Z-Order juga digunakan ketika kita perlu merender objek di atas satu sama lain.

Potongan kode berikut menunjukkan langkah-langkah untuk merender objek [Rectangle](https://reference.aspose.com/pdf/id/net/aspose.pdf.drawing/rectangle) di atas satu sama lain.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddRectangleZOrder()
{
    // The path to the documents directory directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();

        // Set size of PDF page
        page.SetPageSize(375, 300);

        // Set left and top margins for the page object as 0
        page.PageInfo.Margin.Left = 0;
        page.PageInfo.Margin.Top = 0;

        // Create rectangles with different colors and Z-Order values
        AddRectangle(page, 50, 40, 60, 40, Aspose.Pdf.Color.Red, 2);
        AddRectangle(page, 20, 20, 30, 30, Aspose.Pdf.Color.Blue, 1);
        AddRectangle(page, 40, 40, 60, 30, Aspose.Pdf.Color.Green, 0);

        // Save PDF document
        document.Save(dataDir + "ControlRectangleZOrder_out.pdf");
    }
}
```

![Mengontrol Z Order](control.png)

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