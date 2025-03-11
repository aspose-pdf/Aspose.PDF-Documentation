---
title: Ekstrak Data Vektor dari file PDF menggunakan C#
linktitle: Ekstrak Data Vektor dari PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 80
url: /id/net/extract-vector-data-from-pdf/
description: Aspose.PDF memudahkan untuk mengekstrak data vektor dari file PDF. Anda dapat mendapatkan data vektor (jalur, poligon, polilin), seperti posisi, warna, lebar garis, dll.
lastmod: "2024-09-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Extract Vector Data from a PDF file using C#",
    "alternativeHeadline": "Effortless Vector Data Extraction from PDF with C#",
    "abstract": "Aspose.PDF for .NET sekarang menawarkan fitur inovatif yang memungkinkan pengguna untuk dengan mudah mengekstrak data vektor dari file PDF. Fungsionalitas ini mencakup akses rinci ke elemen grafis, seperti jalur dan poligon, bersama dengan properti mereka seperti posisi, warna, dan lebar garis, memberdayakan pengembang untuk menangani grafik vektor dengan efisien dalam aplikasi mereka",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "361",
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
    "url": "/net/extract-vector-data-from-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/extract-vector-data-from-pdf/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF dapat melakukan tidak hanya tugas sederhana dan mudah tetapi juga menangani tujuan yang lebih kompleks. Periksa bagian berikut untuk pengguna dan pengembang tingkat lanjut."
}
</script>

## Akses ke Data Vektor dari dokumen PDF

Sejak rilis 24.2, pustaka Aspose.PDF for .NET memungkinkan ekstraksi data vektor dari file PDF. 
Potongan kode berikut membuat objek Document baru menggunakan beberapa data input, menginisialisasi 'GraphicsAbsorber' (GraphicsAbsorber mengembalikan data vektor) untuk menangani elemen grafis, dan kemudian mengunjungi halaman kedua dari dokumen untuk mengekstrak dan menganalisis elemen-elemen ini. 
Ini mengambil berbagai properti dari elemen grafis kedua, seperti operator terkait, persegi panjang, dan posisi.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ProcessGraphicsInPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Instantiate a new GraphicsAbsorber object to process graphic elements
        using (var grAbsorber = new Aspose.Pdf.Vector.GraphicsAbsorber())
        {
            // Visit the second page of the document to extract graphic elements
            grAbsorber.Visit(document.Pages[1]);

            // Retrieve the list of graphic elements from the GraphicsAbsorber
            var elements = grAbsorber.Elements;

            // Access the operators associated with the second graphic element
            var operations = elements[1].Operators;

            // Retrieve the rectangle associated with the second graphic element
            var rectangle = elements[1].Rectangle;

            // Get the position of the second graphic element
            var position = elements[1].Position;
        }
    }
}
```

## Ekstrak Data Vektor dari dokumen PDF

Untuk ekstraksi Data Vektor dari PDF, kita dapat menggunakan ekstraktor SVG:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SaveVectorGraphicsFromPage()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "VectorGraphics.pdf"))
    {
        // Save vector graphics from the first page to an SVG file
        document.Pages[1].TrySaveVectorGraphics(dataDir + "VectorGraphics_out.svg");
    }
}
```

### Ekstrak semua subjalur ke gambar secara terpisah

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractAllSubpathsToImagesSeparately()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Path to the directory where SVGs will be saved
    var svgDirPath = dataDir + "SvgOutput/";

    // Create extraction options
    var options = new Aspose.Pdf.Vector.SvgExtractionOptions
    {
        ExtractEverySubPathToSvg = true
    };

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "VectorGraphics.pdf"))
    {
        // Get the first page of the document
        var page = document.Pages[1];

        // Create SVG extractor
        var extractor = new Aspose.Pdf.Vector.SvgExtractor(options);
        // Extract SVGs from the page
        extractor.Extract(page, svgDirPath);
    }
}
```

### Ekstrak daftar elemen ke gambar tunggal

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractListOfElementsToSingleImage()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Initialize the list of graphic elements
    var elements = new List<Aspose.Pdf.Vector.GraphicElement>();

    // Example: Fill elements list with needed graphic elements (implement your logic here)

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "VectorGraphics.pdf"))
    {
        // Get the first page of the document
        var page = document.Pages[1];

        // Use SvgExtractor to extract SVGs
        var svgExtractor = new Aspose.Pdf.Vector.SvgExtractor();

        // Extract SVGs from graphic elements on the page
        svgExtractor.Extract(elements, page, Path.Combine(dataDir, "SvgOutput", "VectorGraphics_out.svg"));
    }
}
```

### Ekstrak elemen tunggal

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractSingleElement()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();


    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "VectorGraphics.pdf"))
    {
        // Create a GraphicsAbsorber object to extract graphic elements
        var graphicsAbsorber = new Aspose.Pdf.Vector.GraphicsAbsorber();

        // Get the first page of the document
        var page = document.Pages[1];

        // Process the page to extract graphic elements
        graphicsAbsorber.Visit(page);

        // Extract the graphic element (XFormPlacement) and save it as SVG
        var xFormPlacement = graphicsAbsorber.Elements[1] as Aspose.Pdf.Vector.XFormPlacement;
        xFormPlacement.Elements[2].SaveToSvg(Path.Combine(dataDir, "SvgOutput", "VectorGraphics_out.svg"));
    }
}
```