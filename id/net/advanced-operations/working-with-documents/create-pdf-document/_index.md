---
title: Cara Membuat PDF menggunakan C#
linktitle: Buat Dokumen PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /id/net/create-pdf-document/
description: Buat dan format Dokumen PDF dengan Aspose.PDF for .NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "How to Create PDF using C#",
    "alternativeHeadline": "Create and Format PDFs Effortlessly with C#",
    "abstract": "Fungsi baru dalam Aspose.PDF for .NET memberdayakan pengembang untuk dengan mudah membuat dan memformat dokumen PDF menggunakan C#. Dengan API yang intuitif ini, pengguna dapat menghasilkan PDF yang dapat dicari, memanipulasi konten bertag untuk aksesibilitas, dan mengintegrasikan pembuatan PDF ke dalam berbagai aplikasi .NET, meningkatkan produktivitas dan memperlancar alur kerja",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "PDF creation, C# PDF generation, Aspose.PDF for .NET, searchable PDF, accessible PDF, Document class, TextFragment, PDF document manipulation, .NET applications, BDC operations",
    "wordcount": "871",
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
    "url": "/net/create-pdf-document/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/create-pdf-document/"
    },
    "dateModified": "2024-11-25",
    "description": "Buat dan format Dokumen PDF dengan Aspose.PDF for .NET."
}
</script>

Kami selalu mencari cara untuk menghasilkan dokumen PDF dan bekerja dengan mereka dalam proyek C# dengan lebih tepat, akurat, dan efektif. Memiliki fungsi yang mudah digunakan dari sebuah pustaka memungkinkan kami untuk melacak lebih banyak pekerjaan, dan lebih sedikit pada rincian yang memakan waktu untuk mencoba menghasilkan PDF, baik dalam .NET.

Potongan kode berikut juga bekerja dengan pustaka [Aspose.PDF.Drawing](/pdf/id/net/drawing/).

## Buat (atau Hasilkan) dokumen PDF menggunakan bahasa C#

API Aspose.PDF for .NET memungkinkan Anda untuk membuat dan membaca file PDF menggunakan C# dan VB.NET. API ini dapat digunakan dalam berbagai aplikasi .NET termasuk WinForms, ASP.NET, dan beberapa lainnya. Dalam artikel ini, kami akan menunjukkan cara menggunakan API Aspose.PDF for .NET untuk dengan mudah menghasilkan dan membaca file PDF dalam aplikasi .NET.

### Cara Membuat File PDF Sederhana

Untuk membuat file PDF menggunakan C#, langkah-langkah berikut dapat digunakan.

1. Buat objek dari kelas [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).
1. Tambahkan objek [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) ke koleksi [Pages](https://reference.aspose.com/pdf/net/aspose.pdf/document/properties/pages) dari objek Document.
1. Tambahkan [TextFragment](https://reference.aspose.com/pdf/net/aspose.pdf.text/textfragment) ke koleksi [Paragraphs](https://reference.aspose.com/pdf/net/aspose.pdf/page/properties/paragraphs) dari halaman.
1. Simpan dokumen PDF yang dihasilkan.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CreateHelloWorldDocument()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_QuickStart();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();
        // Add text to new page
        page.Paragraphs.Add(new Aspose.Pdf.Text.TextFragment("Hello World!"));
        // Save PDF document
        document.Save(dataDir + "HelloWorld_out.pdf");
    }
}
```

### Cara Membuat dokumen PDF yang dapat dicari

Aspose.PDF for .NET menyediakan fitur untuk membuat serta memanipulasi dokumen PDF yang ada. Saat menambahkan elemen Teks di dalam file PDF, PDF yang dihasilkan dapat dicari. Namun, jika kami mengonversi Gambar yang berisi teks menjadi file PDF, konten di dalam PDF tidak dapat dicari. Namun sebagai solusi, kami dapat menggunakan OCR pada file yang dihasilkan, sehingga menjadi dapat dicari.

Logika yang ditentukan di bawah ini mengenali teks untuk gambar PDF. Untuk pengenalan, Anda dapat menggunakan dukungan OCR luar standar HOCR. Untuk tujuan pengujian, kami telah menggunakan OCR Google tesseract gratis. Oleh karena itu, pertama-tama Anda perlu menginstal Tesseract-OCR di sistem Anda, dan Anda akan memiliki aplikasi konsol tesseract.

Berikut adalah kode lengkap untuk memenuhi persyaratan ini:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CreateSearchableDocument()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_QuickStart();
    
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SearchableDocument.pdf"))
    {
        document.Convert(CallBackGetHocr);

        // Save PDF document
        document.Save(dataDir + "SearchableDocument_out.pdf");
    }
}

private static string CallBackGetHocr(System.Drawing.Image img)
{
    var tmpFile = Path.GetTempFileName();
    try
    {
        using (var bmp = new System.Drawing.Bitmap(img))
        {
            bmp.Save(tmpFile, System.Drawing.Imaging.ImageFormat.Bmp);
        }

        var inputFile = string.Concat('"', tmpFile, '"');
        var outputFile = string.Concat('"', tmpFile, '"');
        var arguments = string.Concat(inputFile, " ", outputFile, " -l eng hocr");
        var tesseractProcessName = RunExamples.GetTesseractExePath();

        var psi = new System.Diagnostics.ProcessStartInfo(tesseractProcessName, arguments)
        {
            UseShellExecute = true,
            CreateNoWindow = true,
            WindowStyle = System.Diagnostics.ProcessWindowStyle.Hidden,
            WorkingDirectory = Path.GetDirectoryName(tesseractProcessName)
        };

        var p = new System.Diagnostics.Process
        {
            StartInfo = psi
        };
        p.Start();
        p.WaitForExit();

        using (var streamReader = new StreamReader(tmpFile + ".hocr"))
        {
            string text = streamReader.ReadToEnd();
            return text;
        }
    }
    finally
    {
        if (File.Exists(tmpFile))
        {
            File.Delete(tmpFile);
        }
        if (File.Exists(tmpFile + ".hocr"))
        {
            File.Delete(tmpFile + ".hocr");
        }
    }
}
```

### Cara Membuat PDF yang dapat diakses menggunakan fungsi tingkat rendah

Potongan kode ini bekerja dengan dokumen PDF dan konten bertag-nya, memanfaatkan pustaka Aspose.PDF untuk memprosesnya.

Contoh ini membuat elemen span baru dalam konten bertag dari halaman pertama PDF, menemukan semua elemen BDC, dan mengaitkannya dengan span tersebut. Dokumen yang dimodifikasi kemudian disimpan.

Anda dapat membuat pernyataan bdc dengan menentukan mcid, lang, dan teks ekspansi menggunakan objek BDCProperties:

```cs
var bdc = new Aspose.Pdf.Operators.BDC("P", new Aspose.Pdf.Facades.BDCProperties(1, "de", "Hallo, welt!"));
```

Setelah membuat pohon struktur, dimungkinkan untuk mengikat operator BDC ke elemen struktur yang ditentukan dengan metode Tag pada objek elemen:

```cs
Aspose.Pdf.LogicalStructure.SpanElement span = content.CreateSpanElement();
span.Tag(bdc);
```

Langkah-langkah untuk membuat PDF yang dapat diakses:

1. Muat Dokumen PDF.
1. Akses Konten Bertag.
1. Buat Elemen Span.
1. Tambahkan Span ke Elemen Root.
1. Iterasi Melalui Konten Halaman.
1. Periksa Elemen BDC dan Tandai Mereka.
1. Simpan Dokumen yang Dimodifikasi.

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CreateAnAccessibleDocument()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_QuickStart();
    
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "tourguidev2_gb_tags.pdf"))
    {
        // Access tagged content
        Aspose.Pdf.Tagged.ITaggedContent content = document.TaggedContent;
        // Create a span element
        Aspose.Pdf.LogicalStructure.SpanElement span = content.CreateSpanElement();
        // Append span to root element
        content.RootElement.AppendChild(span);
        // Iterate over page contents
        foreach (var op in document.Pages[1].Contents)
        {
            var bdc = op as Aspose.Pdf.Operators.BDC;
            if (bdc != null)
            {
                span.Tag(bdc);
            }
        }
        // Save PDF document
        document.Save(dataDir + "AccessibleDocument_out.pdf");
    }
}
```

Kode ini memodifikasi PDF dengan membuat elemen span di dalam konten bertag dokumen dan menandai konten tertentu (operasi BDC) dari halaman pertama dengan span ini. PDF yang dimodifikasi kemudian disimpan ke file baru.

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