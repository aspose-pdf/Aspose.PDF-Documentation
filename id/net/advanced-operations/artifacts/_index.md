---
title: Bekerja dengan Artefak di .NET
linktitle: Bekerja dengan Artefak
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 170
url: /id/net/artifacts/
description: Aspose.PDF for .NET memungkinkan Anda untuk menambahkan gambar latar belakang ke halaman PDF, dan mendapatkan setiap watermark menggunakan kelas Artefak.
lastmod: "2024-01-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Working with Artifacts in .NET",
    "alternativeHeadline": "Add and Manage Artifacts in PDF Documents",
    "abstract": "Aspose.PDF for .NET memperkenalkan kelas Artefak, memungkinkan pengembang untuk mengelola elemen non-konten seperti gambar latar belakang dan watermark dengan efisien dalam dokumen PDF. Fungsionalitas ini meningkatkan struktur dokumen sambil meningkatkan aksesibilitas dan kinerja, karena artefak dapat diabaikan oleh teknologi bantu. Dengan opsi yang dapat disesuaikan untuk jenis dan properti, pengguna dapat dengan mudah memanipulasi elemen ini untuk membuat PDF yang menarik secara visual.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Artifacts, PDF document generation, Aspose.PDF for .NET, BackgroundArtifact, WatermarkArtifact, Artifact class, PDF artifacts, Artifact types, Accessibility in PDF, PDF watermark handling",
    "wordcount": "779",
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
    "url": "/net/artifacts/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/artifacts/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF for .NET memungkinkan Anda untuk menambahkan gambar latar belakang ke halaman PDF, dan mendapatkan setiap watermark menggunakan kelas Artefak."
}
</script>

Artefak dalam PDF adalah objek grafis atau elemen lain yang bukan bagian dari konten aktual dokumen. Mereka biasanya digunakan untuk dekorasi, tata letak, atau tujuan latar belakang. Contoh artefak termasuk header halaman, footer, pemisah, atau gambar yang tidak menyampaikan makna apa pun.

Tujuan artefak dalam PDF adalah untuk memungkinkan perbedaan antara elemen konten dan non-konten. Ini penting untuk aksesibilitas, karena pembaca layar dan teknologi bantu lainnya dapat mengabaikan artefak dan fokus pada konten yang relevan. Artefak juga dapat meningkatkan kinerja dan kualitas dokumen PDF, karena mereka dapat diabaikan dari pencetakan, pencarian, atau penyalinan.

Untuk membuat elemen sebagai artefak dalam PDF, Anda perlu menggunakan kelas [Artefak](https://reference.aspose.com/pdf/net/aspose.pdf/artifact).
Ini memiliki properti berguna berikut:

- **Artefak.Tipe** – mendapatkan tipe artefak (mendukung nilai dari enumerasi Artifact.ArtifactType di mana nilai termasuk Latar Belakang, Tata Letak, Halaman, Penomoran dan Tidak Terdefinisi).
- **Artefak.Subtipe** – mendapatkan subtipe artefak (mendukung nilai dari enumerasi Artifact.ArtifactSubtype di mana nilai termasuk Latar Belakang, Footer, Header, Tidak Terdefinisi, Watermark).
- **Artefak.Gambar** – Mendapatkan gambar artefak (jika gambar ada, jika tidak null).
- **Artefak.Teks** – Mendapatkan teks artefak.
- **Artefak.Konten** – Mendapatkan koleksi operator internal artefak. Tipe yang didukung adalah System.Collections.ICollection.
- **Artefak.Form** – Mendapatkan XForm artefak (jika XForm digunakan). Watermark, header, dan footer artefak mengandung XForm yang menunjukkan semua konten artefak.
- **Artefak.Persegi Panjang** – Mendapatkan posisi artefak di halaman.
- **Artefak.Putar** – Mendapatkan rotasi artefak (dalam derajat, nilai positif menunjukkan rotasi berlawanan arah jarum jam).
- **Artefak.Ketebalan** – Mendapatkan ketebalan artefak. Nilai yang mungkin berada dalam rentang 0...1, di mana 1 sepenuhnya tidak transparan.

Kelas berikut juga mungkin berguna untuk bekerja dengan artefak:

- [ArtifactCollection](https://reference.aspose.com/pdf/net/aspose.pdf/artifactcollection)
- [BackgroundArtifact](https://reference.aspose.com/pdf/net/aspose.pdf/backgroundartifact/)
- [HeaderArtifact](https://reference.aspose.com/pdf/net/aspose.pdf/headerartifact/)
- [FooterArtifact](https://reference.aspose.com/pdf/net/aspose.pdf/footerartifact/)
- [WatermarkArtifact](https://reference.aspose.com/pdf/net/aspose.pdf/watermarkartifact/)

## Bekerja dengan Watermark yang Ada

Watermark yang dibuat dengan Adobe Acrobat disebut artefak (seperti yang dijelaskan dalam 14.8.2.2 Konten Nyata dan Artefak dari spesifikasi PDF).

Untuk mendapatkan semua Watermark di halaman tertentu, kelas [Halaman](https://reference.aspose.com/pdf/net/aspose.pdf/page) memiliki properti Artefak.

Cuplikan kode berikut menunjukkan cara mendapatkan semua watermark di halaman pertama dari file PDF.

_Catatan:_ Kode ini juga berfungsi dengan pustaka [Aspose.PDF.Drawing](/pdf/net/drawing/).

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractWatermarkFromPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "sample-w.pdf"))
    {
        // Get the watermarks from the first page artifacts
        var watermarks = document.Pages[1].Artifacts
            .Where(artifact =>
                artifact.Type == Aspose.Pdf.Artifact.ArtifactType.Pagination
                && artifact.Subtype == Aspose.Pdf.Artifact.ArtifactSubtype.Watermark);

        // Iterate through the found watermark artifacts and print details
        foreach (Aspose.Pdf.WatermarkArtifact item in watermarks.Cast<Aspose.Pdf.WatermarkArtifact>())
        {
            Console.WriteLine($"{item.Text} {item.Rectangle}");
        }
    }
}
```

## Bekerja dengan Latar Belakang sebagai Artefak

Gambar latar belakang dapat digunakan untuk menambahkan watermark, atau desain halus lainnya, ke dokumen. Dalam Aspose.PDF for .NET, setiap dokumen PDF adalah kumpulan halaman dan setiap halaman berisi kumpulan artefak. Kelas [BackgroundArtifact](https://reference.aspose.com/pdf/net/aspose.pdf/backgroundartifact) dapat digunakan untuk menambahkan gambar latar belakang ke objek halaman.

Cuplikan kode berikut menunjukkan cara menambahkan gambar latar belakang ke halaman PDF menggunakan objek BackgroundArtifact.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddBackgroundImageToPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "sample.pdf"))
    {
        // Create a new BackgroundArtifact and set the background image
        var background = new Aspose.Pdf.BackgroundArtifact()
        {
            BackgroundImage = File.OpenRead(dataDir + "background.jpg")
        };

        // Add the background image to the first page's artifacts
        document.Pages[1].Artifacts.Add(background);

        // Save PDF document with the added background
        document.Save(dataDir + "SampleArtifactsBackground_out.pdf");
    }
}
```

Jika Anda ingin, karena suatu alasan, menggunakan latar belakang warna solid, silakan ubah kode sebelumnya dengan cara berikut:

```csharp
 // For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET

 private static void AddBackgroundColorToPDF()
 {
    // The path to the documents directory
     var dataDir = RunExamples.GetDataDir_AsposePdf();

     // Open PDF document
     using (var document = new Aspose.Pdf.Document(dataDir + "sample.pdf"))
     {
         // Create a new BackgroundArtifact and set the background color
         var background = new Aspose.Pdf.BackgroundArtifact()
         {
             BackgroundColor = Aspose.Pdf.Color.DarkKhaki
         };

         // Add the background color to the first page's artifacts
         document.Pages[1].Artifacts.Add(background);

         // Save PDF document
         document.Save(dataDir + "SampleArtifactsBackground_out.pdf");
     }
 }
```

## Menghitung Artefak dari Tipe Tertentu

Untuk menghitung total jumlah artefak dari tipe tertentu (misalnya, total jumlah watermark), gunakan kode berikut:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CountPDFArtifacts()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "sample.pdf"))
    {
        // Get pagination artifacts from the first page
        var paginationArtifacts = document.Pages[1].Artifacts
            .Where(artifact => artifact.Type == Aspose.Pdf.Artifact.ArtifactType.Pagination);

        // Count and display the number of each artifact type
        Console.WriteLine("Watermarks: {0}",
            paginationArtifacts.Count(a => a.Subtype == Aspose.Pdf.Artifact.ArtifactSubtype.Watermark));
        Console.WriteLine("Backgrounds: {0}",
            paginationArtifacts.Count(a => a.Subtype == Aspose.Pdf.Artifact.ArtifactSubtype.Background));
        Console.WriteLine("Headers: {0}",
            paginationArtifacts.Count(a => a.Subtype == Aspose.Pdf.Artifact.ArtifactSubtype.Header));
        Console.WriteLine("Footers: {0}",
            paginationArtifacts.Count(a => a.Subtype == Aspose.Pdf.Artifact.ArtifactSubtype.Footer));
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