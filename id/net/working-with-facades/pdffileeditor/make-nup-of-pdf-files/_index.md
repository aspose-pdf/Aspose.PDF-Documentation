---
title: Buat NUp dari file PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 90
url: /id/net/make-nup-of-pdf-files/
description: Artikel ini menunjukkan cara membuat NUp dari file PDF menggunakan Aspose.PDF Facades dengan kelas PdfFileEditor.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Make NUp of PDF files",
    "alternativeHeadline": "Create NUp PDFs with Flexible Input Methods",
    "abstract": "Fitur NUp dalam Aspose.PDF for .NET memungkinkan pengguna untuk menggabungkan beberapa file PDF menjadi satu dokumen output secara efisien, menyesuaikan ukuran halaman dan konfigurasi tata letak. Fungsionalitas ini mendukung baik jalur file maupun aliran, memungkinkan integrasi yang fleksibel ke dalam berbagai alur kerja sambil meningkatkan presentasi dokumen.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "895",
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
    "url": "/net/make-nup-of-pdf-files/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/make-nup-of-pdf-files/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF dapat melakukan tidak hanya tugas yang sederhana dan mudah tetapi juga menangani tujuan yang lebih kompleks. Periksa bagian berikut untuk pengguna dan pengembang tingkat lanjut."
}
</script>

## Buat NUp dari PDF Menggunakan Jalur File

[MakeNUp](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/pdffileeditor/methods/makenup/index) metode dari kelas [PdfFileEditor](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/pdffileeditor) memungkinkan Anda untuk membuat NUp dari file PDF input dan menyimpannya ke file PDF output. Overload ini memungkinkan Anda untuk membuat NUp menggunakan jalur file. Potongan kode berikut menunjukkan cara membuat NUP menggunakan jalur file.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MakeNupOfPdfUsingFilePaths()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Make NUp
    pdfEditor.MakeNUp(dataDir + "MakeNupInput.pdf", dataDir + "MakeNupInput2.pdf", "MakeNUpUsingPaths_out.pdf");
}
```

## Buat NUp Menggunakan Ukuran Halaman dan Jalur File

[MakeNUp](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/pdffileeditor/methods/makenup/index) metode dari kelas [PdfFileEditor](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/pdffileeditor) memungkinkan Anda untuk membuat NUp dari file PDF input dan menyimpannya ke file PDF output. Overload ini memungkinkan Anda untuk membuat NUp menggunakan jalur file. Anda juga dapat mengatur ukuran halaman dari file PDF output menggunakan overload ini. Potongan kode berikut menunjukkan cara membuat NUp menggunakan ukuran halaman dan jalur file.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MakeNupUsingPageSizeAndFilePaths()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Make NUp
    pdfEditor.MakeNUp(dataDir + "MakeNupMultiplePagesInput.pdf", dataDir + "MakeNUpUsingPageSizeAndPaths_out.pdf", 2, 3, PageSize.A5);
}
```

## Buat NUp dari PDF Menggunakan Ukuran Halaman, Nilai Horizontal dan Vertikal, dan Jalur File

[MakeNUp](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/pdffileeditor/methods/makenup/index) metode dari kelas [PdfFileEditor](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/pdffileeditor) memungkinkan Anda untuk membuat NUp dari file PDF input dan menyimpannya ke file PDF output. Overload ini memungkinkan Anda untuk membuat NUp menggunakan jalur file. Anda juga dapat mengatur ukuran halaman dari file PDF output dan jumlah halaman horizontal dan vertikal pada setiap halaman output menggunakan overload ini. Potongan kode berikut menunjukkan cara membuat NUp menggunakan ukuran halaman, nilai horizontal dan vertikal, dan jalur file.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MakeNupOfPdfUsingPageSizeHorizontalAndVerticalValuesAndFilePaths()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Make NUp
    pdfEditor.MakeNUp(dataDir + "MakeNupInput.pdf", "MakeNUpUsingPageSizeHorizontalAndVerticalValues_out.pdf", 2, 3);
}
```

## Buat NUp dari PDF Menggunakan Array File PDF dan Jalur File

[MakeNUp](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/pdffileeditor/methods/makenup/index) metode dari kelas [PdfFileEditor](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/pdffileeditor) memungkinkan Anda untuk membuat NUp dari array file PDF input dan menyimpannya ke satu file PDF output. Overload ini memungkinkan Anda untuk membuat NUp menggunakan jalur file. Potongan kode berikut menunjukkan cara membuat NUp menggunakan array file PDF dan jalur file.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MakeNupOfPdfUsingArrayOfPdfFilesAndFilePaths()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Create array of files
    string[] filesArray = new string[2];
    filesArray[0] = dataDir + "MakeNupInput.pdf";
    filesArray[1] = dataDir + "MakeNupInput2.pdf";
    // Make NUp
    pdfEditor.MakeNUp(filesArray, dataDir + "MakeNupUsingArrayOfFilesAndPaths_out.pdf", true);
}
```

## Buat NUp dari PDF Menggunakan Aliran

[MakeNUp](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/pdffileeditor/methods/makenup/index) metode dari kelas [PdfFileEditor](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/pdffileeditor) memungkinkan Anda untuk membuat NUp dari aliran PDF input dan menyimpannya ke aliran PDF output. Overload ini memungkinkan Anda untuk membuat NUp menggunakan aliran alih-alih jalur file. Potongan kode berikut menunjukkan cara membuat NUp menggunakan aliran.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MakeNupOfPdfUsingStreams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Create streams
    using (var inputStream1 = new FileStream(dataDir + "MakeNupInput.pdf", FileMode.Open))
    {
        using (var inputStream2 = new FileStream(dataDir + "MakeNupInput2.pdf", FileMode.Open))
        {
            using (var outputStream = new FileStream(dataDir + "MakeNUpUsingStreams_out.pdf", FileMode.Create))
            {
                // Make NUp
                pdfEditor.MakeNUp(inputStream1, inputStream2, outputStream);
            }
        }
    }
}
```

## Buat NUp dari PDF Menggunakan Ukuran Halaman dan Aliran

[MakeNUp](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/pdffileeditor/methods/makenup/index) metode dari kelas [PdfFileEditor](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/pdffileeditor) memungkinkan Anda untuk membuat NUp dari aliran PDF input dan menyimpannya ke aliran PDF output. Overload ini memungkinkan Anda untuk membuat NUp menggunakan aliran alih-alih jalur file. Anda juga dapat mengatur ukuran halaman dari aliran PDF output menggunakan overload ini. Potongan kode berikut menunjukkan cara membuat NUp menggunakan ukuran halaman dan aliran.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MakeNupOfPdfUsingPageSizeAndStreams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Create streams
    using (var inputStream = new FileStream(dataDir + "MakeNupInput.pdf", FileMode.Open))
    {
        using (var outputStream = new FileStream(dataDir + "MakeNUpUsingPageSizeAndStreams_out.pdf", FileMode.Create))
        {
            // Make NUp
            pdfEditor.MakeNUp(inputStream, outputStream, 2, 3, PageSize.A5);    
        }    
    }
}
```

## Buat NUp dari PDF Menggunakan Ukuran Halaman, Nilai Horizontal dan Vertikal, dan Aliran

[MakeNUp](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/pdffileeditor/methods/makenup/index) metode dari kelas [PdfFileEditor](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/pdffileeditor) memungkinkan Anda untuk membuat NUp dari aliran PDF input dan menyimpannya ke aliran PDF output. Overload ini memungkinkan Anda untuk membuat NUp menggunakan aliran alih-alih jalur file. Anda juga dapat mengatur ukuran halaman dari aliran PDF output dan jumlah halaman horizontal dan vertikal pada setiap halaman output menggunakan overload ini. Potongan kode berikut menunjukkan cara membuat NUp menggunakan ukuran halaman, nilai horizontal dan vertikal, dan aliran.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MakeNupOfPdfUsingPageSizeHorizontalAndVerticalValuesAndStreams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Create streams
    using (var inputStream = new FileStream(dataDir + "MakeNupInput.pdf", FileMode.Open))
    {
        using (var outputStream = new FileStream(dataDir + "MakeNUpUsingPageSizeHorizontalVerticalValuesAndStreams_out.pdf", FileMode.Create))
        {
            // Make NUp
            pdfEditor.MakeNUp(inputStream, outputStream, 2, 3); 
        }
    }
}
```

## Buat NUp dari PDF Menggunakan Array File PDF dan Aliran

[MakeNUp](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/pdffileeditor/methods/makenup/index) metode dari kelas [PdfFileEditor](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/pdffileeditor) memungkinkan Anda untuk membuat NUp dari array aliran PDF input dan menyimpannya ke satu aliran PDF output. Overload ini memungkinkan Anda untuk membuat NUp menggunakan aliran alih-alih jalur file. Potongan kode berikut menunjukkan cara membuat NUp menggunakan array file PDF menggunakan aliran.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MakeNupOfPdfUsingArrayOfPdfFilesAndStreams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Create streams
    using (var stream1 = new FileStream(dataDir + "MakeNupInput.pdf", FileMode.Open))
    {
        using (var stream2 = new FileStream(dataDir + "MakeNupInput2.pdf", FileMode.Open))
        {
            using (var outputStream = new FileStream(dataDir + "MakeNUpUsingArrayOfFilesAndStreams_out.pdf", FileMode.Create))
            {
                var fileStreams = new Stream[2];
                fileStreams[0] = stream1;
                fileStreams[1] = stream2;
                // Make NUp
                pdfEditor.MakeNUp(fileStreams, outputStream, true);
            }
        }
    }
}
```