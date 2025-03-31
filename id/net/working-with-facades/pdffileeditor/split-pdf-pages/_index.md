---
title: Memisahkan Halaman PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 60
url: /id/net/split-pdf-pages/
description: Bagian ini menjelaskan cara memisahkan halaman PDF dengan Aspose.PDF Facades menggunakan kelas PdfFileEditor.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Split PDF pages",
    "alternativeHeadline": "Effortlessly Split PDF Pages via File Paths and Streams",
    "abstract": "Fitur Memisahkan Halaman PDF yang baru di Aspose.PDF for .NET memungkinkan pengguna untuk secara efisien membagi dokumen PDF menjadi berbagai segmen menggunakan kelas PdfFileEditor. Fungsionalitas ini mendukung pemisahan dari halaman pertama hingga halaman yang ditentukan, pemisahan menjadi set besar, dan bahkan mengisolasi halaman individu, semua melalui jalur file atau aliran, memberikan opsi yang serbaguna untuk manipulasi PDF.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1017",
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
    "url": "/net/split-pdf-pages/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/split-pdf-pages/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF dapat melakukan tidak hanya tugas yang sederhana dan mudah tetapi juga menangani tujuan yang lebih kompleks. Periksa bagian berikut untuk pengguna dan pengembang tingkat lanjut."
}
</script>

## Memisahkan Halaman PDF dari Pertama Menggunakan Jalur File

[SplitFromFirst](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades.pdffileeditor/splitfromfirst/methods/1) metode dari kelas [PdfFileEditor](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/pdffileeditor) memungkinkan Anda untuk memisahkan file PDF mulai dari halaman pertama dan berakhir di nomor halaman yang ditentukan. Jika Anda ingin memanipulasi file PDF dari disk, Anda dapat mengirimkan jalur file dari file PDF input dan output ke metode ini. Potongan kode berikut menunjukkan cara memisahkan halaman PDF dari pertama menggunakan jalur file.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SplitPdfPagesFromFirstUsingFilePaths()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Split pages
    pdfEditor.SplitFromFirst(dataDir + "MultiplePages.pdf", 3, dataDir + "SplitPagesUsingPaths_out.pdf");
}
```

## Memisahkan Halaman PDF dari Pertama Menggunakan Aliran File

[SplitFromFirst](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades.pdffileeditor/splitfromfirst/methods/1) metode dari kelas [PdfFileEditor](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/pdffileeditor) memungkinkan Anda untuk memisahkan file PDF mulai dari halaman pertama dan berakhir di nomor halaman yang ditentukan. Jika Anda ingin memanipulasi file PDF dari aliran, Anda dapat mengirimkan aliran PDF input dan output ke metode ini. Potongan kode berikut menunjukkan cara memisahkan halaman PDF dari pertama menggunakan aliran file.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SplitPdfPagesFromFirstUsingFileStreams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Create streams
    using (var inputStream = new FileStream(dataDir + "MultiplePages.pdf", FileMode.Open))
    {
        using (var outputStream = new FileStream(dataDir + "SplitPagesUsingStreams_out.pdf", FileMode.Create))
        {
            // Split pages
            pdfEditor.SplitFromFirst(inputStream, 3, outputStream);
        }
    }
}
```

## Memisahkan Halaman PDF ke Set Besar Menggunakan Jalur File

[SplitToBulks](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/pdffileeditor/methods/splittobulks/index) metode dari kelas [PdfFileEditor](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/pdffileeditor) memungkinkan Anda untuk memisahkan file PDF menjadi beberapa set halaman. Dalam contoh ini, kami memerlukan dua set halaman (1, 2) dan (5, 6). Jika Anda ingin mengakses file PDF dari disk, Anda perlu mengirimkan PDF input sebagai jalur file. Metode ini mengembalikan array MemoryStream. Anda dapat melakukan loop melalui array ini dan menyimpan set halaman individu sebagai file terpisah. Potongan kode berikut menunjukkan cara memisahkan halaman PDF ke set besar menggunakan jalur file.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SplitPdfPagesToBulkUsingFilePaths()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    var fileNumber = 1;
    // Create array of pages to split
    var numberOfPages = new int[][] { new int[] { 1, 2 }, new int[] { 3, 4 } };
    // Split to bulk
    var outBuffer = pdfEditor.SplitToBulks(dataDir + "MultiplePages.pdf", numberOfPages);
    // Save individual files
    foreach (var outStream in outBuffer)
    {
        using (var outFileStream = new FileStream(dataDir + "File_" + fileNumber.ToString() + "_out.pdf", FileMode.Create))
        {
            outStream.WriteTo(outFileStream);
            fileNumber++;
        }
    }
}
```

## Memisahkan Halaman PDF ke Set Besar Menggunakan Aliran

[SplitToBulks](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/pdffileeditor/methods/splittobulks/index) metode dari kelas [PdfFileEditor](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/pdffileeditor) memungkinkan Anda untuk memisahkan file PDF menjadi beberapa set halaman. Dalam contoh ini, kami memerlukan dua set halaman (1, 2) dan (5, 6). Anda dapat mengirimkan aliran ke metode ini sebagai pengganti mengakses file dari disk. Metode ini mengembalikan array MemoryStream. Anda dapat melakukan loop melalui array ini dan menyimpan set halaman individu sebagai file terpisah. Potongan kode berikut menunjukkan cara memisahkan halaman PDF ke set besar menggunakan aliran.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SplitPdfPagesToBulkUsingStreams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Create input stream
    using (var inputStream = new FileStream(dataDir + "MultiplePages.pdf", FileMode.Open))
    {
        var fileNumber = 1;
        // Create array of pages to split
        var numberOfPages = new int[][] { new int[] { 1, 2 }, new int[] { 3, 4 } };
        // Split to bulk
        var outBuffer = pdfEditor.SplitToBulks(inputStream, numberOfPages);
        // Save individual files
        foreach (var outStream in outBuffer)
        {
            using (var outFileStream = new FileStream(dataDir + "File_" + fileNumber.ToString() + "_out.pdf", FileMode.Create))
            {
                outStream.WriteTo(outFileStream);
                fileNumber++;
            }
        }
    }
}
```

## Memisahkan Halaman PDF ke Akhir Menggunakan Jalur File

[SplitToEnd](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/pdffileeditor/methods/splittoend/index) metode dari kelas [PdfFileEditor](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/pdffileeditor) memungkinkan Anda untuk memisahkan PDF dari nomor halaman yang ditentukan hingga akhir file PDF dan menyimpannya sebagai PDF baru. Untuk melakukan ini, menggunakan jalur file, Anda perlu mengirimkan jalur file input dan output serta nomor halaman dari mana pemisahan perlu dimulai. PDF output akan disimpan ke disk. Potongan kode berikut menunjukkan cara memisahkan halaman PDF ke akhir menggunakan jalur file.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SplitPdfPagesToEndUsingFilePaths()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Split pages
    pdfEditor.SplitToEnd(dataDir + "MultiplePages.pdf", 3, dataDir + "SplitPagesToEndUsingPaths_out.pdf");
}
```

## Memisahkan Halaman PDF ke Akhir Menggunakan Aliran

[SplitToEnd](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/pdffileeditor/methods/splittoend/index) metode dari kelas [PdfFileEditor](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/pdffileeditor) memungkinkan Anda untuk memisahkan PDF dari nomor halaman yang ditentukan hingga akhir file PDF dan menyimpannya sebagai PDF baru. Untuk melakukan ini, menggunakan aliran, Anda perlu mengirimkan aliran input dan output serta nomor halaman dari mana pemisahan perlu dimulai. PDF output akan disimpan ke aliran output. Potongan kode berikut menunjukkan cara memisahkan halaman PDF ke akhir menggunakan aliran.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SplitPdfPagesToEndUsingStreams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Create streams
    using (var inputStream = new FileStream(dataDir + "MultiplePages.pdf", FileMode.Open))
    {
        using (var outputStream = new FileStream(dataDir + "SplitPagesToEndUsingStreams_out.pdf", FileMode.Create))
        {
            // Split pages
            pdfEditor.SplitToEnd(inputStream, 3, outputStream);   
        }
    }
}
```

## Memisahkan PDF ke Halaman Individu Menggunakan Jalur File

{{% alert color="primary" %}}

Anda dapat mencoba memisahkan dokumen PDF dan melihat hasilnya secara online di tautan ini:

[products.aspose.app/pdf/splitter](https://products.aspose.app/pdf/splitter) {{% /alert %}}

Untuk memisahkan file PDF ke halaman individu, Anda perlu mengirimkan PDF sebagai jalur file ke metode [SplitToPages](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/pdffileeditor/methods/splittopages/index). Metode ini akan mengembalikan array MemoryStream yang berisi halaman-halaman individu dari file PDF. Anda dapat melakukan loop melalui array MemoryStream ini dan menyimpan halaman-halaman individu sebagai file PDF terpisah di disk. Potongan kode berikut menunjukkan cara memisahkan PDF ke halaman individu menggunakan jalur file.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SplitPdfToIndividualPagesUsingFilePaths()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    var fileNumber = 1;
    // Split to pages
    var outBuffer = pdfEditor.SplitToPages(dataDir + "splitPdfToIndividualPagesInput.pdf");
    // Save individual files
    foreach (var outStream in outBuffer)
    {
        using (var outFileStream = new FileStream(dataDir + "File_" + fileNumber.ToString() + "_out.pdf", FileMode.Create))
        {
            outStream.WriteTo(outFileStream);
            fileNumber++;
        }
    }
}
```

## Memisahkan PDF ke Halaman Individu Menggunakan Aliran

Untuk memisahkan file PDF ke halaman individu, Anda perlu mengirimkan PDF sebagai aliran ke metode [SplitToPages](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/pdffileeditor/methods/splittopages/index). Metode ini akan mengembalikan array MemoryStream yang berisi halaman-halaman individu dari file PDF. Anda dapat melakukan loop melalui array MemoryStream ini dan menyimpan halaman-halaman individu sebagai file PDF terpisah di disk, atau Anda dapat menyimpan halaman-halaman individu ini dalam aliran memori untuk digunakan nanti dalam aplikasi Anda. Potongan kode berikut menunjukkan cara memisahkan PDF ke halaman individu menggunakan aliran.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SplitPdfToIndividualPagesUsingStreams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Create input stream
    using (var inputStream = new FileStream(dataDir + "splitPdfToIndividualPagesInput.pdf", FileMode.Open))
    {
        var fileNumber = 1;
        // Split to pages
        var outBuffer = pdfEditor.SplitToPages(inputStream);
        // Save individual files
        foreach (var outStream in outBuffer)
        {
            using (var outFileStream = new FileStream(dataDir + "File_" + fileNumber.ToString() + "_out.pdf", FileMode.Create))
            {
                outStream.WriteTo(outFileStream);
                fileNumber++;
            }
        }
    }
}
```