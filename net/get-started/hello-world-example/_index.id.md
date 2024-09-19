---
title: Contoh Hello World menggunakan bahasa C#
linktitle: Contoh Hello World
type: docs
weight: 40
url: /net/hello-world-example/
description: Sampel ini menunjukkan cara membuat dokumen PDF sederhana dengan teks Hello World menggunakan Aspose.PDF
aliases:
    - /net/hello-world/
lastmod: "2022-02-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Contoh Hello World menggunakan bahasa C#",
    "alternativeHeadline": "Contoh Aspose.PDF C#",
    "author": {
        "@type": "Person",
        "givenName": "Andriy",
        "familyName": "Andrukhovskiy",
        "url":"https://www.linkedin.com/in/andruhovski/"
    },
    "genre": "pembuatan dokumen pdf",
    "keywords": "pdf, c#, pembuatan dokumen",
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
    "url": "http://docs.aspose.com/pdf/net/hello-world-example/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "http://docs.aspose.com/pdf/net/hello-world-example/"
    },
    "dateModified": "2022-02-04",
    "description": "Sampel ini menunjukkan cara membuat dokumen PDF sederhana dengan teks Hello World menggunakan Aspose.PDF",
    "articleBody": "Contoh \"Hello World\" secara tradisional digunakan untuk memperkenalkan fitur bahasa pemrograman atau perangkat lunak dengan kasus penggunaan sederhana.\nAspose.PDF untuk .NET adalah API PDF yang kaya fitur yang memungkinkan para pengembang untuk menyertakan kemampuan pembuatan, manipulasi, dan konversi dokumen PDF dalam aplikasi .NET mereka. Ini mendukung bekerja dengan banyak format file populer termasuk PDF, XFA, TXT, HTML, PCL, XML, XPS, EPUB, TEX dan format file gambar. Dalam artikel ini, kami membuat dokumen PDF yang berisi teks \"Hello World!\". Setelah menginstal Aspose.PDF untuk .NET di lingkungan Anda, Anda dapat menjalankan contoh kode di bawah ini untuk melihat cara kerja API Aspose.PDF.\nPotongan kode di bawah ini mengikuti langkah-langkah ini:\n1. Instansiasi objek Dokumen\n2. Tambahkan Halaman ke objek dokumen\n3. Buat Fragmen Teks\n4. Tambahkan Fragmen Teks ke koleksi Paragraf halaman\n5. Simpan dokumen PDF hasil\nPotongan kode berikut adalah program Hello World untuk memamerkan cara kerja API Aspose.PDF untuk .NET."
}
</script>

Contoh "Hello World" secara tradisional digunakan untuk memperkenalkan fitur dari bahasa pemrograman atau perangkat lunak dengan kasus penggunaan yang sederhana.

Aspose.PDF untuk .NET adalah API PDF yang kaya fitur yang memungkinkan para pengembang untuk menyertakan pembuatan, manipulasi, dan konversi dokumen PDF dalam aplikasi .NET mereka. Ini mendukung bekerja dengan banyak format file populer termasuk PDF, XFA, TXT, HTML, PCL, XML, XPS, EPUB, TEX dan format file gambar. Dalam artikel ini, kami membuat dokumen PDF yang berisi teks "Hello World!". Setelah menginstal Aspose.PDF untuk .NET di lingkungan Anda, Anda dapat menjalankan contoh kode di bawah ini untuk melihat bagaimana API Aspose.PDF bekerja.

Potongan kode berikut juga bekerja dengan perpustakaan [Aspose.PDF.Drawing](/pdf/net/drawing/).

Potongan kode di bawah ini mengikuti langkah-langkah ini:

1. Instansiasi objek [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document)
1. Tambahkan [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) ke objek dokumen
1.
1. Tambahkan TextFragment ke koleksi [Paragraph](https://reference.aspose.com/pdf/net/aspose.pdf/page/properties/paragraphs) dari halaman
1. [Simpan](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4) dokumen PDF yang dihasilkan

Berikut adalah potongan kode program Hello World untuk menunjukkan cara kerja API Aspose.PDF untuk .NET.

```csharp
namespace Aspose.Pdf.Examples
{
    public static class ExampleGetStarted
    {
        private static readonly string _dataDir = "..\\..\\..\\Samples";
        public static void HelloWorld()
        {
            // Inisialisasi objek dokumen
            Document document = new Document();
            // Tambahkan halaman
            Page page = document.Pages.Add();
            // Tambahkan teks ke halaman baru
            page.Paragraphs.Add(new Aspose.Pdf.Text.TextFragment("Hello World!"));
            // Simpan PDF yang telah diperbarui
            var outputFileName = System.IO.Path.Combine(_dataDir, "HelloWorld_out.pdf");
            document.Save( outputFileName );
        }
    }
}
```
