---
title: Tambahkan watermark ke PDF menggunakan C#
linktitle: Tambahkan watermark
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 90
url: /id/net/add-watermarks/
description: Artikel ini menjelaskan fitur bekerja dengan artefak dan mendapatkan watermark di PDF menggunakan secara programatik C#.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
aliases:
    - /net/working-with-existing-watermarks/
    - /net/adding-multi-line-watermark-to-existing-pdf/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Add watermark to PDF using C#",
    "alternativeHeadline": "Add Custom Watermarks to PDF with C#",
    "abstract": "Fitur baru di Aspose.PDF for .NET memungkinkan pengembang untuk secara programatik menambahkan watermark yang dapat disesuaikan ke dokumen PDF menggunakan fungsionalitas Artefak. Fitur ini meningkatkan manajemen dokumen dengan mendukung berbagai properti artefak, termasuk jenis, opasitas, rotasi, dan kustomisasi teks, memungkinkan pengguna untuk dengan mudah membuat file PDF yang profesional dan dapat dikenali.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "462",
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
    "url": "/net/add-watermarks/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-watermarks/"
    },
    "dateModified": "2024-11-26",
    "description": "Artikel ini menjelaskan fitur bekerja dengan artefak dan mendapatkan watermark di PDF menggunakan secara programatik C#."
}
</script>

**Aspose.PDF for .NET** memungkinkan menambahkan watermark ke dokumen PDF Anda menggunakan Artefak. Silakan periksa artikel ini untuk menyelesaikan tugas Anda.

Potongan kode berikut juga bekerja dengan [Aspose.PDF.Drawing](/pdf/net/drawing/) library.

Watermark yang dibuat dengan Adobe Acrobat disebut artefak (seperti yang dijelaskan dalam 14.8.2.2 Konten Nyata dan Artefak dari spesifikasi PDF). Untuk bekerja dengan artefak, Aspose.PDF memiliki dua kelas: [Artifact](https://reference.aspose.com/pdf/net/aspose.pdf/artifact) dan [ArtifactCollection](https://reference.aspose.com/pdf/net/aspose.pdf/artifactcollection).

Untuk mendapatkan semua artefak di halaman tertentu, kelas [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) memiliki properti Artifacts. Topik ini menjelaskan cara bekerja dengan artefak dalam file PDF.

## Bekerja dengan Artefak

Kelas [Artifact](https://reference.aspose.com/pdf/net/aspose.pdf/artifact) memiliki properti berikut:

- **Artifact.Type**: mendapatkan jenis artefak (mendukung nilai dari enumerasi Artifact.ArtifactType di mana nilai termasuk Latar Belakang, Tata Letak, Halaman, Penomoran dan Tidak Terdefinisi).
- **Artifact.Subtype**: mendapatkan subtype artefak (mendukung nilai dari enumerasi Artifact.ArtifactSubtype di mana nilai termasuk Latar Belakang, Footer, Header, Tidak Terdefinisi, Watermark).

{{% alert color="primary" %}}

Harap dicatat bahwa watermark yang dibuat dengan Adobe Acrobat memiliki jenis Penomoran dan subtype Watermark.

{{% /alert %}}

- **Artifact.Contents**: Mendapatkan koleksi operator internal artefak. Tipe yang didukung adalah System.Collections.ICollection.
- **Artifact.Form**: Mendapatkan XForm artefak (jika XForm digunakan). Watermark, header, dan artefak footer berisi XForm yang menunjukkan semua konten artefak.
- **Artifact.Image**: Mendapatkan gambar artefak (jika gambar ada, jika tidak null).
- **Artifact.Text**: Mendapatkan teks artefak.
- **Artifact.Rectangle**: Mendapatkan posisi artefak di halaman.
- **Artifact.Rotation**: Mendapatkan rotasi artefak (dalam derajat, nilai positif menunjukkan rotasi berlawanan arah jarum jam).
- **Artifact.Opacity**: Mendapatkan opasitas artefak. Nilai yang mungkin berada dalam rentang 0…1, di mana 1 sepenuhnya tidak transparan.

## Cara Menambahkan Watermark Pada File PDF

Potongan kode berikut menunjukkan cara mendapatkan setiap watermark di halaman pertama file PDF dengan C#.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddWatermarks()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();
    
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "AddWatermarksInput.pdf"))
    {
        // Create a new watermark artifact
        var artifact = new Aspose.Pdf.WatermarkArtifact();
        artifact.SetTextAndState(
            "WATERMARK",
            new Aspose.Pdf.Text.TextState()
            {
                FontSize = 72,
                ForegroundColor = Aspose.Pdf.Color.Blue,
                Font = Aspose.Pdf.Text.FontRepository.FindFont("Courier")
            });
        // Set watermark properties
        artifact.ArtifactHorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Center;
        artifact.ArtifactVerticalAlignment = Aspose.Pdf.VerticalAlignment.Center;
        artifact.Rotation = 45;
        artifact.Opacity = 0.5;
        artifact.IsBackground = true;
        // Add watermark artifact to the first page
        document.Pages[1].Artifacts.Add(artifact);
        // Save PDF document
        document.Save(dataDir + "AddWatermarks_out.pdf");
    }
}
```

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