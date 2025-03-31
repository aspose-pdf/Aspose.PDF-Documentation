---
title: Ekstrak Halaman PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 40
url: /id/net/extract-pdf-pages/
description: Bagian ini menjelaskan cara mengekstrak halaman PDF dengan Aspose.PDF Facades menggunakan kelas PdfFileEditor.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Extract PDF pages",
    "alternativeHeadline": "Effortlessly Extract Selected Pages from PDF Files",
    "abstract": "Fitur Ekstrak Halaman PDF dalam Aspose.PDF for .NET Facades memberikan pengguna kemampuan yang ditingkatkan untuk secara selektif mengekstrak halaman dari dokumen PDF. Dengan memanfaatkan kelas PdfFileEditor, pengguna dapat dengan efisien mengekstrak rentang tertentu atau sekumpulan halaman melalui jalur file atau aliran, membuat manipulasi dokumen lebih terstruktur dan fleksibel. Fungsionalitas ini sangat bermanfaat bagi pengguna yang ingin menyesuaikan konten PDF mereka tanpa mengubah file asli.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "660",
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
    "url": "/net/extract-pdf-pages/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/extract-pdf-pages/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF dapat melakukan tidak hanya tugas sederhana dan mudah tetapi juga menangani tujuan yang lebih kompleks. Periksa bagian berikut untuk pengguna dan pengembang tingkat lanjut."
}
</script>

## Ekstrak Halaman PDF antara Dua Nomor Menggunakan Jalur File

Metode [Extract](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/extract/index) dari kelas [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) memungkinkan Anda untuk mengekstrak rentang halaman tertentu dari file PDF. Overload ini memungkinkan Anda untuk mengekstrak halaman sambil memanipulasi file PDF dari disk. Overload ini memerlukan parameter berikut: jalur file input, halaman awal, halaman akhir, dan jalur file output. Halaman dari halaman awal hingga halaman akhir akan diekstrak dan output akan disimpan di disk. Potongan kode berikut menunjukkan cara mengekstrak halaman PDF antara dua nomor menggunakan jalur file.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void Extract_PDFPages_FilePaths()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();

    // Create PdfFileEditor object
    PdfFileEditor pdfEditor = new PdfFileEditor();

    // Extract pages
    pdfEditor.Extract(dataDir + "MultiplePages.pdf", 1, 3, dataDir + "ExtractPagesBetweenNumbers_out.pdf");
}
```

## Ekstrak Array Halaman PDF Menggunakan Jalur File

Jika Anda tidak ingin mengekstrak rentang halaman, melainkan sekumpulan halaman tertentu, metode [Extract](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/extract/index) juga memungkinkan Anda untuk melakukannya. Anda pertama-tama perlu membuat array integer dengan semua nomor halaman yang perlu diekstrak. Overload metode [Extract](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/extract/index) ini mengambil parameter berikut: file PDF input, array integer halaman yang akan diekstrak, dan file PDF output. Potongan kode berikut menunjukkan cara mengekstrak halaman PDF menggunakan jalur file.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void Extract_PDFPages_Streams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();

    // Create PdfFileEditor object
    PdfFileEditor pdfEditor = new PdfFileEditor();

    // Create streams
    using (FileStream inputStream = new FileStream(dataDir + "MultiplePages.pdf", FileMode.Open))
    {
        using (FileStream outputStream = new FileStream(dataDir + "ExtractPagesBetweenTwoNumbers_out.pdf", FileMode.Create))
        {
            // Extract pages
            pdfEditor.Extract(inputStream, 1, 3, outputStream);
        }
    }
}
```

## Ekstrak Halaman PDF antara Dua Nomor Menggunakan Aliran

Metode [Extract](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/extract/index) dari kelas [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) memungkinkan Anda untuk mengekstrak rentang halaman menggunakan aliran. Anda perlu melewatkan parameter berikut ke overload ini: aliran input, halaman awal, halaman akhir, dan aliran output. Halaman yang ditentukan oleh rentang antara halaman awal dan halaman akhir akan diekstrak dari aliran input dan disimpan ke aliran output. Potongan kode berikut menunjukkan cara mengekstrak halaman PDF antara dua nomor menggunakan aliran.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void Extract_ArrayPDFPages_FilePaths()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();

    // Create PdfFileEditor object
    PdfFileEditor pdfEditor = new PdfFileEditor();
    int[] pagesToExtract = new int[] { 1, 2 };
    // Extract pages
    pdfEditor.Extract(dataDir + "Extract.pdf", pagesToExtract, dataDir + "ExtractArrayOfPages_out.pdf");
}
```

## Ekstrak Array Halaman PDF Menggunakan Aliran

Sebuah array halaman dapat diekstrak dari aliran PDF dan disimpan dalam aliran output menggunakan overload yang sesuai dari metode [Extract](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/extract/index). Jika Anda tidak ingin mengekstrak rentang halaman, melainkan sekumpulan halaman tertentu, metode [Extract](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/extract/index) juga memungkinkan Anda untuk melakukannya. Anda pertama-tama perlu membuat array integer dengan semua nomor halaman yang perlu diekstrak. Overload metode [Extract](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/extract/index) ini mengambil parameter berikut: aliran input, array integer halaman yang akan diekstrak, dan aliran output. Potongan kode berikut menunjukkan cara mengekstrak halaman PDF menggunakan aliran.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void Extract_ArrayPDFPages_Streams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    
    // Create PdfFileEditor object
    PdfFileEditor pdfEditor = new PdfFileEditor();
    // Create streams
    using (FileStream inputStream = new FileStream(dataDir + "MultiplePages.pdf", FileMode.Open))
    {
        using (FileStream outputStream = new FileStream(dataDir + "ExtractArrayOfPagesUsingStreams_out.pdf", FileMode.Create))
        {
            int[] pagesToExtract = new int[] { 1, 2 };
            // Extract pages
            pdfEditor.Extract(inputStream, pagesToExtract, outputStream);
        }
    }
}
```