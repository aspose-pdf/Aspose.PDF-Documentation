---
title: Ekstrak Teks SuperScripts dan SubScripts dari PDF
linktitle: Ekstrak SuperScripts dan SubScripts
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 30
url: /id/net/extract-superscripts-subscripts-from-pdf/
description: Artikel ini menjelaskan berbagai cara untuk mengekstrak teks SuperScripts dan SubScripts dari PDF menggunakan Aspose.PDF dalam C#.
lastmod: "2022-10-07"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Extract SuperScripts and SubScripts text from PDF",
    "alternativeHeadline": "Extract SuperScripts and SubScripts from PDF Documents",
    "abstract": "Fitur baru untuk mengekstrak teks SuperScripts dan SubScripts dari dokumen PDF menggunakan pustaka Aspose.PDF for .NET memungkinkan pengguna untuk dengan akurat mengambil format teks khusus yang ditemukan dalam dokumen teknis. Peningkatan ini menyederhanakan proses penanganan ekspresi matematis dan spesifikasi kimia dengan memberikan pengembang alat untuk dengan mudah memanipulasi elemen teks ini.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "323",
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
    "url": "/net/extract-superscripts-subscripts-from-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/extract-superscripts-subscripts-from-pdf/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF dapat melakukan tidak hanya tugas sederhana dan mudah tetapi juga menangani tujuan yang lebih kompleks. Periksa bagian berikut untuk pengguna dan pengembang tingkat lanjut."
}
</script>

## Ekstrak Teks SuperScripts dan SubScripts

Mengekstrak teks dari dokumen PDF adalah hal yang umum. Namun, dalam teks tersebut, ketika diekstrak, **SuperScripts dan SubScripts** yang terkandung di dalamnya, yang khas untuk dokumen teknis dan artikel, mungkin tidak ditampilkan. SubScript atau SuperScript adalah karakter, angka, atau huruf yang ditempatkan di bawah atau di atas garis teks biasa. Biasanya lebih kecil dari sisa teks.

**SubScripts dan SuperScripts** paling sering digunakan dalam rumus, ekspresi matematis, dan spesifikasi senyawa kimia. Sangat sulit untuk mengeditnya ketika bisa ada banyak dari mereka dalam satu bagian teks.
Dalam salah satu rilis terbaru, pustaka **Aspose.PDF for .NET** menambahkan dukungan untuk mengekstrak teks SuperScripts dan SubScripts dari PDF.

Gunakan kelas **TextFragmentAbsorber** dan Anda sudah bisa melakukan apa saja dengan teks yang ditemukan, yaitu, Anda bisa menggunakan seluruh teks. Cobalah cuplikan kode berikut:

Cuplikan kode berikut juga bekerja dengan pustaka [Aspose.PDF.Drawing](/pdf/net/drawing/).

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractSuperScriptsAndSubScripts()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SuperScriptExample.pdf"))
    {
        // Create an absorber
        var absorber = new Aspose.Pdf.Text.TextFragmentAbsorber();
        document.Pages[1].Accept(absorber);
        using (StreamWriter writer = new StreamWriter(dataDir + "SuperScriptExample_out.txt"))
        {
            // Write the extracted text in text file
            writer.WriteLine(absorber.Text);
        }
    }
}
```

Atau gunakan **TextFragments** secara terpisah dan lakukan berbagai manipulasi dengan mereka, misalnya, urutkan berdasarkan koordinat atau berdasarkan ukuran.

Cuplikan kode berikut juga bekerja dengan pustaka [Aspose.PDF.Drawing](/pdf/net/drawing/).

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractSuperScriptsAndSubScriptsWithTextFragments()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SuperScriptExample.pdf"))
    {
        // Create an absorber
        var absorber = new Aspose.Pdf.Text.TextFragmentAbsorber();
        document.Pages[1].Accept(absorber);
        using (StreamWriter writer = new StreamWriter(dataDir + "SuperScriptExample_out.txt"))
        {
            foreach (var textFragment in absorber.TextFragments)
            {
                // Write the extracted text in text file
                writer.Write(textFragment.Text);
            }

        }
    }
}
```