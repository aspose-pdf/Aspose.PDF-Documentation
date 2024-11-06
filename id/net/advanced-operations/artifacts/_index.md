---
title: Bekerja dengan Artifak di .NET
linktitle: Bekerja dengan Artifak
type: docs
weight: 110
url: id/net/artifacts/
description: Aspose.PDF untuk .NET memungkinkan Anda untuk menambahkan gambar latar belakang ke halaman PDF, dan mendapatkan setiap watermark menggunakan kelas Artifact.
lastmod: "2024-01-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Bekerja dengan Artifak di .NET",
    "alternativeHeadline": "Artifak dalam dokumen PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pembuatan dokumen pdf",
    "keywords": "pdf, c#, artifak dalam pdf",
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
    "url": "/net/artifacts/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/artifacts/"
    },
    "dateModified": "2022-02-04",
    "description": "Aspose.PDF untuk .NET memungkinkan Anda untuk menambahkan gambar latar belakang ke halaman PDF, dan mendapatkan setiap watermark menggunakan kelas Artifact."
}
</script>
Artefak dalam PDF adalah objek grafis atau elemen lain yang bukan bagian dari konten sebenarnya dokumen. Mereka biasanya digunakan untuk dekorasi, tata letak, atau tujuan latar belakang. Contoh artefak termasuk header halaman, footer, pemisah, atau gambar yang tidak menyampaikan makna apa pun.

Tujuan dari artefak dalam PDF adalah untuk memungkinkan perbedaan antara elemen konten dan non-konten. Ini penting untuk aksesibilitas, karena pembaca layar dan teknologi bantu lainnya dapat mengabaikan artefak dan fokus pada konten yang relevan. Artefak juga dapat meningkatkan kinerja dan kualitas dokumen PDF, karena dapat dihilangkan dari pencetakan, pencarian, atau penyalinan.

Untuk membuat elemen sebagai artefak dalam PDF, Anda perlu menggunakan kelas [Artifact](https://reference.aspose.com/pdf/net/aspose.pdf/artifact).
Kelas ini memiliki properti berguna berikut:

- **Artifact.Type** – mendapatkan tipe artefak (mendukung nilai dari enumerasi Artifact.ArtifactType di mana nilai termasuk Background, Layout, Page, Pagination dan Undefined).
- **Artifact.Type** – mendapatkan tipe artifact (mendukung nilai dari enumerasi Artifact.ArtifactType di mana nilai termasuk Background, Layout, Page, Pagination dan Undefined).
- **Artifact.Subtype** – mendapatkan subtype artifact (mendukung nilai dari enumerasi Artifact.ArtifactSubtype di mana nilai termasuk Background, Footer, Header, Undefined, Watermark).
- **Artifact.Image** – Mendapatkan gambar dari artifact (jika ada gambar, jika tidak null).
- **Artifact.Text** – Mendapatkan teks dari artifact.
- **Artifact.Contents** – Mendapatkan kumpulan operator internal dari artifact. Tipe yang didukung adalah System.Collections.ICollection.
- **Artifact.Form** – Mendapatkan XForm dari artifact (jika XForm digunakan). Artifact watermark, header, dan footer mengandung XForm yang menampilkan semua isi artifact.
- **Artifact.Rectangle** – Mendapatkan posisi dari artifact di halaman.
- **Artifact.Rotation** – Mendapatkan rotasi dari artifact (dalam derajat, nilai positif menunjukkan rotasi berlawanan arah jarum jam).
- **Artifact.Opacity** – Mendapatkan keopakan dari artifact.
- **Artifact.Opacity** – Mendapatkan opasitas artifak.

Kelas-kelas berikut juga mungkin berguna untuk bekerja dengan artifak:

- [ArtifactCollection](https://reference.aspose.com/pdf/net/aspose.pdf/artifactcollection)
- [BackgroundArtifact](https://reference.aspose.com/pdf/net/aspose.pdf/backgroundartifact/)
- [HeaderArtifact](https://reference.aspose.com/pdf/net/aspose.pdf/headerartifact/)
- [FooterArtifact](https://reference.aspose.com/pdf/net/aspose.pdf/footerartifact/)
- [WatermarkArtifact](https://reference.aspose.com/pdf/net/aspose.pdf/watermarkartifact/)

## Bekerja dengan Watermark yang Ada

Watermark yang dibuat dengan Adobe Acrobat disebut artifak (seperti yang dijelaskan dalam 14.8.2.2 Konten Nyata dan Artifak dari spesifikasi PDF).

Untuk mendapatkan semua Watermark di halaman tertentu, kelas [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) memiliki properti Artifacts.

Potongan kode berikut menunjukkan cara mendapatkan semua watermark pada halaman pertama file PDF.

_Catatan:_ Kode ini juga berfungsi dengan perpustakaan [Aspose.PDF.Drawing](/pdf/net/drawing/).
_Catatan:_ Kode ini juga berfungsi dengan perpustakaan [Aspose.PDF.Drawing](/pdf/net/drawing/).

```csharp
var document = new Document(System.IO.Path.Combine(_dataDir, "sample-w.pdf"));
var watermarks = document.Pages[1].Artifacts
    .Where(artifact =>
    artifact.Type == Artifact.ArtifactType.Pagination
    && artifact.Subtype == Artifact.ArtifactSubtype.Watermark);
foreach (WatermarkArtifact item in watermarks.Cast<WatermarkArtifact>())
{
    Console.WriteLine($"{item.Text} {item.Rectangle}");
}
```

## Bekerja dengan Latar Belakang sebagai Artefak

Gambar latar belakang dapat digunakan untuk menambahkan watermark, atau desain halus lainnya, pada dokumen. Di Aspose.PDF untuk .NET, setiap dokumen PDF adalah kumpulan halaman dan setiap halaman berisi kumpulan artefak. Kelas [BackgroundArtifact](https://reference.aspose.com/pdf/net/aspose.pdf/backgroundartifact) dapat digunakan untuk menambahkan gambar latar belakang ke objek halaman.

Potongan kode berikut menunjukkan cara menambahkan gambar latar belakang ke halaman PDF menggunakan objek BackgroundArtifact.

```csharp
var document = new Document(System.IO.Path.Combine(_dataDir, "sample.pdf"));
var background = new BackgroundArtifact()
{
    BackgroundImage = System.IO.File.OpenRead(System.IO.Path.Combine(_dataDir, "background.jpg"))
};
document.Pages[1].Artifacts.Add(background);
document.Save(System.IO.Path.Combine(_dataDir, "sample_artifacts_background.pdf"));
```
Jika Anda ingin, karena alasan tertentu, menggunakan latar belakang warna solid, silakan ubah kode sebelumnya dengan cara berikut:

```csharp
var document = new Document(System.IO.Path.Combine(_dataDir, "sample.pdf"));
var background = new BackgroundArtifact()
{
    BackgroundColor = Color.DarkKhaki,
};
document.Pages[1].Artifacts.Add(background);
document.Save(System.IO.Path.Combine(_dataDir, "sample_artifacts_background.pdf"));
```

## Menghitung Jumlah Artifak dari Jenis Tertentu

Untuk menghitung jumlah total artifak dari jenis tertentu (misalnya, jumlah total watermark), gunakan kode berikut:

```csharp
var document = new Document(System.IO.Path.Combine(_dataDir, "sample.pdf"));
var paginationArtifacts = document.Pages[1].Artifacts.Where(artifact => artifact.Type == Artifact.ArtifactType.Pagination);
Console.WriteLine("Watermarks: {0}", paginationArtifacts.Count(a => a.Subtype == Artifact.ArtifactSubtype.Watermark));
Console.WriteLine("Backgrounds: {0}", paginationArtifacts.Count(a => a.Subtype == Artifact.ArtifactSubtype.Background));
Console.WriteLine("Headers: {0}", paginationArtifacts.Count(a => a.Subtype == Artifact.ArtifactSubtype.Header));
Console.WriteLine("Footers: {0}", paginationArtifacts.Count(a => a.Subtype == Artifact.ArtifactSubtype.Footer));
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

