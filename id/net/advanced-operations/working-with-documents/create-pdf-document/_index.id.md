---
title: Cara Membuat PDF Menggunakan C#
linktitle: Membuat Dokumen PDF
type: docs
weight: 10
url: /net/create-pdf-document/
description: Buat dan format Dokumen PDF dengan Aspose.PDF untuk .NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Cara Membuat PDF Menggunakan C#",
    "alternativeHeadline": "Buat dokumen PDF dari awal",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pembuatan dokumen pdf",
    "keywords": "pdf, dotnet, buat dokumen pdf",
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
    "url": "/net/create-pdf-document/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/create-pdf-document/"
    },
    "dateModified": "2022-02-04",
    "description": "Buat dan format Dokumen PDF dengan Aspose.PDF untuk .NET."
}
</script>

Kami selalu mencari cara untuk menghasilkan dokumen PDF dan bekerja dengan mereka dalam proyek C# lebih tepat, akurat, dan efektif. Memiliki fungsi yang mudah digunakan dari sebuah perpustakaan memungkinkan kami untuk melacak lebih banyak pekerjaan, dan kurang pada detail yang memakan waktu dalam mencoba menghasilkan PDF, baik dalam .NET.

Potongan kode berikut juga bekerja dengan perpustakaan [Aspose.PDF.Drawing](/pdf/net/drawing/).

## Membuat (atau Menghasilkan) dokumen PDF menggunakan bahasa C#

Aspose.PDF untuk .NET API memungkinkan Anda membuat dan membaca file PDF menggunakan C# dan VB.NET. API dapat digunakan dalam berbagai aplikasi .NET termasuk WinForms, ASP.NET, dan beberapa lainnya. Dalam artikel ini, kami akan menunjukkan cara menggunakan Aspose.PDF untuk .NET API untuk dengan mudah menghasilkan dan membaca file PDF dalam aplikasi .NET.

### Bagaimana Membuat File PDF Sederhana

Untuk membuat file PDF menggunakan C#, langkah-langkah berikut dapat digunakan.

1. Buat objek dari kelas [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document)
1.
1. Tambahkan [TextFragment](https://reference.aspose.com/pdf/net/aspose.pdf.text/textfragment) ke koleksi [Paragraphs](https://reference.aspose.com/pdf/net/aspose.pdf/page/properties/paragraphs) dari halaman
1. Simpan dokumen PDF yang dihasilkan

```csharp
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_QuickStart();

// Inisialisasi objek dokumen
Document document = new Document();
// Tambah halaman
Page page = document.Pages.Add();
// Tambahkan teks ke halaman baru
page.Paragraphs.Add(new Aspose.Pdf.Text.TextFragment("Hello World!"));
// Simpan PDF yang telah diperbarui
document.Save(dataDir + "HelloWorld_out.pdf");
```

### Bagaimana Cara Membuat Dokumen PDF yang Dapat Dicari

Aspose.PDF untuk .NET menyediakan fitur untuk membuat serta memanipulasi dokumen PDF yang ada.
Aspose.PDF untuk .NET menyediakan fitur untuk membuat serta memanipulasi dokumen PDF yang sudah ada.

Logika yang ditentukan di bawah ini mengenali teks untuk gambar PDF. Untuk pengenalan, Anda dapat menggunakan dukungan OCR eksternal yang mendukung standar HOCR. Untuk tujuan pengujian, kami telah menggunakan Google tesseract OCR gratis. Oleh karena itu, pertama-tama Anda perlu menginstal Tesseract-OCR di sistem Anda, dan Anda akan memiliki aplikasi konsol tesseract.

Berikut adalah kode lengkap untuk mencapai persyaratan ini:

```csharp

using System;

namespace Aspose.Pdf.Examples.Advanced.WorkingWithDocuments
{
    class ExampleCreateDocument
    {
        private const string _dataDir = "C:\\Samples";
        public static void CreateSearchableDocuments(string file)
        {
            Aspose.Pdf.Document doc = new Aspose.Pdf.Document(file);
            bool convertResult = false;
            try
            {
                convertResult = doc.Convert(CallBackGetHocr);
            }
            catch (Exception ex)
            {
                Console.WriteLine(ex.Message);
            }
            doc.Save(file);
            doc.Dispose();
        }

        static string CallBackGetHocr(System.Drawing.Image img)
        {
            string tmpFile = System.IO.Path.GetTempFileName();
            try
            {
                System.Drawing.Bitmap bmp = new System.Drawing.Bitmap(img);

                bmp.Save(tmpFile, System.Drawing.Imaging.ImageFormat.Bmp);
                string inputFile = string.Concat('"', tmpFile, '"');
                string outputFile = string.Concat('"', tmpFile, '"');
                string arguments = string.Concat(inputFile, " ", outputFile, " -l eng hocr");
                string tesseractProcessName = @"C:\Program Files\Tesseract-OCR\Tesseract.exe";

                System.Diagnostics.ProcessStartInfo psi =
                    new System.Diagnostics.ProcessStartInfo(tesseractProcessName, arguments)
                    {
                        UseShellExecute = true,
                        CreateNoWindow = true,
                        WindowStyle = System.Diagnostics.ProcessWindowStyle.Hidden,
                        WorkingDirectory = System.IO.Path.GetDirectoryName(tesseractProcessName)
                    };

                System.Diagnostics.Process p = new System.Diagnostics.Process
                    {
                        StartInfo = psi
                    };
                p.Start();
                p.WaitForExit();

                System.IO.StreamReader streamReader = new System.IO.StreamReader(tmpFile + ".hocr");
                string text = streamReader.ReadToEnd();
                streamReader.Close();

                return text;
            }
            finally
            {
                if (System.IO.File.Exists(tmpFile))
                    System.IO.File.Delete(tmpFile);
                if (System.IO.File.Exists(tmpFile + ".hocr"))
                    System.IO.File.Delete(tmpFile + ".hocr");
            }
        }
    }
}
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF untuk .NET Library",
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

