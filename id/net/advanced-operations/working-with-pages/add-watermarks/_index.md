 ---
title: Menambahkan watermark ke PDF menggunakan C#
linktitle: Tambahkan watermark
type: docs
weight: 90
url: /id/net/add-watermarks/
description: Artikel ini menjelaskan fitur-fitur bekerja dengan artefak dan mendapatkan watermark di PDF menggunakan C# secara programatik.
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
    "headline": "Menambahkan watermark ke PDF menggunakan C#",
    "alternativeHeadline": "Cara menambahkan watermark ke PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pembuatan dokumen pdf",
    "keywords": "pdf, c#, tambahkan watermark",
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
    "url": "/net/add-watermarks/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-watermarks/"
    },
    "dateModified": "2022-02-04",
    "description": "Artikel ini menjelaskan fitur-fitur bekerja dengan artefak dan mendapatkan watermark di PDF menggunakan C# secara programatik."
}
</script>

**Aspose.PDF for .NET** memungkinkan menambahkan watermark pada dokumen PDF Anda menggunakan Artifacts. Silakan periksa artikel ini untuk menyelesaikan tugas Anda.

Potongan kode berikut juga bekerja dengan pustaka [Aspose.PDF.Drawing](/pdf/id/net/drawing/).

Watermark yang dibuat dengan Adobe Acrobat disebut sebagai artifact (seperti yang dijelaskan dalam 14.8.2.2 Konten Nyata dan Artifacts dari spesifikasi PDF). Untuk bekerja dengan artifacts, Aspose.PDF memiliki dua kelas: [Artifact](https://reference.aspose.com/pdf/net/aspose.pdf/artifact) dan [ArtifactCollection](https://reference.aspose.com/pdf/net/aspose.pdf/artifactcollection).

Untuk mendapatkan semua artifact di halaman tertentu, kelas [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) memiliki properti Artifacts. Topik ini menjelaskan cara bekerja dengan artifact dalam file PDF.

## Bekerja dengan Artifacts

Kelas [Artifact](https://reference.aspose.com/pdf/net/aspose.pdf/artifact) memiliki properti berikut:

**Artifact.Type** – mendapatkan tipe artifact (mendukung nilai dari enumerasi Artifact.ArtifactType dimana nilai termasuk Background, Layout, Page, Pagination dan Undefined).
**Artifact.Type** – mendapatkan tipe artefak (mendukung nilai dari enumerasi Artifact.ArtifactType di mana nilai termasuk Background, Layout, Page, Pagination, dan Undefined).
**Artifact.Subtype** – mendapatkan subtype artefak (mendukung nilai dari enumerasi Artifact.ArtifactSubtype di mana nilai termasuk Background, Footer, Header, Undefined, Watermark).

{{% alert color="primary" %}}

Harap dicatat bahwa watermark yang dibuat dengan Adobe Acrobat memiliki tipe Pagination dan subtype Watermark.

{{% /alert %}}

**Artifact.Contents** – Mendapatkan koleksi operator internal artefak. Tipe yang didukung adalah System.Collections.ICollection.
**Artifact.Form** – Mendapatkan XForm dari sebuah artefak (jika XForm digunakan). Artefak watermark, header, dan footer mengandung XForm yang menunjukkan seluruh isi artefak.
**Artifact.Image** – Mendapatkan gambar dari sebuah artefak (jika ada gambar, jika tidak null).
**Artifact.Text** – Mendapatkan teks dari sebuah artefak.
**Artifact.Rectangle** – Mendapatkan posisi artefak di halaman.
**Artifact.Rotation** – Mendapatkan rotasi dari sebuah artefak (dalam derajat, nilai positif menunjukkan rotasi berlawanan arah jarum jam).
**Artifact.Rotation** – Mendapatkan rotasi artefak (dalam derajat, nilai positif menunjukkan rotasi berlawanan arah jarum jam).
**Artifact.Opacity** – Mendapatkan keburaman artefak. Nilai yang mungkin berada dalam rentang 0…1, di mana 1 adalah sepenuhnya buram.

## Contoh Pemrograman: Cara Menambahkan Watermark Pada File PDF

Berikut ini adalah potongan kode yang menunjukkan cara mendapatkan setiap watermark di halaman pertama file PDF dengan C#.

```csharp
public static void AddWatermarks()
{
    Document document = new Document(_dataDir + "text.pdf");
    WatermarkArtifact artifact = new WatermarkArtifact();
    artifact.SetTextAndState(
        "WATERMARK",
        new TextState()
        {
            FontSize = 72,
            ForegroundColor = Color.Blue,
            Font = FontRepository.FindFont("Courier")
        });
    artifact.ArtifactHorizontalAlignment = HorizontalAlignment.Center;
    artifact.ArtifactVerticalAlignment = VerticalAlignment.Center;
    artifact.Rotation = 45;
    artifact.Opacity = 0.5;
    artifact.IsBackground = true;
    document.Pages[1].Artifacts.Add(artifact);
    document.Save(_dataDir + "watermark.pdf");
}
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Perpustakaan Aspose.PDF untuk .NET",
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
```

