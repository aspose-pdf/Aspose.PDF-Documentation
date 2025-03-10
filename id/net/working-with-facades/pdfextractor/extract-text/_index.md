---
title: Ekstrak Teks dari File PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 30
url: /id/net/extract-text/
description: Bagian ini menjelaskan cara mengekstrak teks dari pdf menggunakan kelas PdfExtractor.
lastmod: "2021-06-05"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Extract Text from PDF File",
    "alternativeHeadline": "Effortless Text Extraction from PDF Files",
    "abstract": "Kelas PdfExtractor memungkinkan ekstraksi teks yang efisien dari file PDF melalui berbagai metode, memungkinkan pengguna untuk mengambil teks, gambar, dan lampiran dengan mudah. Dengan memanfaatkan metode seperti ExtractText, GetText, dan GetNextPageText, pengembang dapat dengan mudah mengekstrak dan menyimpan konten tekstual dari halaman individu atau seluruh dokumen, menyederhanakan tugas manipulasi PDF. Dengan mode ekstraksi yang fleksibel tersedia, fitur ini meningkatkan kontrol atas format output, menjadikannya alat penting bagi siapa saja yang bekerja dengan data PDF.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "441",
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
    "url": "/net/extract-text/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/extract-text/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF dapat melakukan tidak hanya tugas sederhana dan mudah tetapi juga menangani tujuan yang lebih kompleks. Periksa bagian berikut untuk pengguna dan pengembang tingkat lanjut."
}
</script>

Dalam artikel ini, kita akan melihat rincian tentang cara mengekstrak teks dari file PDF. Semua fitur ekstraksi ini disediakan di satu tempat, dalam kelas [PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor). Kita akan melihat bagaimana cara menggunakan fitur-fitur ini dalam kode kita.

Kelas [PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor) menyediakan tiga jenis kemampuan ekstraksi. Tiga kategori ini adalah Teks, Gambar, dan Lampiran. Untuk melakukan ekstraksi di bawah masing-masing dari tiga kategori ini, PdfExtractor menyediakan berbagai metode yang bekerja sama untuk memberikan output akhir kepada Anda.

Sebagai contoh, untuk mengekstrak teks, Anda dapat menggunakan tiga metode yaitu [ExtractText, GetText, HasNextPageText, dan GetNextPageText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/index). Sekarang, untuk mulai mengekstrak teks, pertama-tama Anda perlu memanggil metode [ExtractText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/extracttext/index); ini akan mengekstrak teks dari file PDF dan menyimpannya ke dalam memori. Setelah itu, metode [GetText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/gettext/index) akan mengambil teks yang diekstrak ini dan menyimpannya ke disk di lokasi yang ditentukan dalam sebuah file. [HasNextPageText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/hasnextpagetext) membantu Anda untuk melintasi setiap halaman dan memeriksa apakah halaman berikutnya memiliki teks atau tidak. Jika mengandung teks, maka [GetNextPageText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/getnextpagetext/index) akan membantu Anda menyimpan teks dari halaman individu ke dalam file.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractText()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    bool wholeText = true;
    // Create an object of the PdfExtractor class
    using (var pdfExtractor = new Aspose.Pdf.Facades.PdfExtractor())
    {
        // Bind PDF document
        pdfExtractor.BindPdf(dataDir + "sample.pdf");

        // ExtractText
        pdfExtractor.ExtractText();

        if (!wholeText)
        {
            pdfExtractor.GetText(dataDir + "sample.txt");
        }
        else
        {
            // Extract the text into separate files
            int pageNumber = 1;
            while (pdfExtractor.HasNextPageText())
            {
                pdfExtractor.GetNextPageText($"{dataDir}\\sample{pageNumber:D3}.txt");
                pageNumber++;
            }
        }
    }
}
```

Untuk Mengambil Mode Ekstraksi Teks, gunakan kode berikut:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractTextExtractonMode()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    bool wholeText = true;
    // Create an object of the PdfExtractor class
    using (var pdfExtractor = new Aspose.Pdf.Facades.PdfExtractor())
    {
        // Bind PDF document
        pdfExtractor.BindPdf(dataDir + "ExtractTextExtractonMode.pdf");

        // ExtractText
        // pdfExtractor.ExtractTextMode = 0; // pure mode
        pdfExtractor.ExtractTextMode = 1; // raw mode
        pdfExtractor.ExtractText();

        if (!wholeText)
        {
            pdfExtractor.GetText(dataDir + "ExtractTextExtractonMode_out.txt");
        }
        else
        {
            // Extract the text into separate files
            int pageNumber = 1;
            while (pdfExtractor.HasNextPageText())
            {
                pdfExtractor.GetNextPageText($"{dataDir}\\sample{pageNumber:D3}.txt");
                pageNumber++;
            }
        }
    }
}
```