---
title: Buat Buku Saku dari PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 80
url: /id/net/make-booklet-of-pdf/
description: Bagian ini menjelaskan cara membuat buku saku dari PDF dengan Aspose.PDF Facades menggunakan kelas PdfFileEditor.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Make Booklet of PDF",
    "alternativeHeadline": "Create Booklets from PDFs with Enhanced Flexibility",
    "abstract": "Fitur Buat Buku Saku dari PDF di Aspose.PDF memungkinkan pengguna untuk dengan mudah membuat buku saku dari file PDF menggunakan kelas PdfFileEditor. Fungsionalitas ini mendukung baik jalur file maupun aliran, memungkinkan kustomisasi ukuran halaman dan spesifikasi halaman kiri dan kanan untuk kontrol output yang lebih baik. Alat yang kuat ini menyederhanakan proses pembuatan buku saku, menjadikannya sumber daya penting untuk manipulasi PDF.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "946",
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
    "url": "/net/make-booklet-of-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/make-booklet-of-pdf/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF dapat melakukan tidak hanya tugas yang sederhana dan mudah tetapi juga menangani tujuan yang lebih kompleks. Periksa bagian berikut untuk pengguna dan pengembang tingkat lanjut."
}
</script>

## Buat Buku Saku dari PDF Menggunakan Jalur File

[MakeBooklet](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/makebooklet/index)  metode dari kelas [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) memungkinkan Anda untuk membuat buku saku dari file PDF input dan menyimpannya ke file PDF output. Overload ini memungkinkan Anda untuk membuat buku saku menggunakan jalur file. Potongan kode berikut menunjukkan cara membuat buku saku menggunakan jalur file.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MakeBookletOfPdfUsingFilePaths()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Make booklet
    pdfEditor.MakeBooklet(dataDir + "MakeBookletInput.pdf", dataDir + "MakeBookletUsingPaths_out.pdf");
}
```

## Buat Buku Saku dari PDF Menggunakan Ukuran Halaman dan Jalur File

[MakeBooklet](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/makebooklet/index)  metode dari kelas [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) memungkinkan Anda untuk membuat buku saku dari file PDF input dan menyimpannya ke file PDF output. Overload ini memungkinkan Anda untuk membuat buku saku menggunakan jalur file. Anda juga dapat mengatur ukuran halaman dari file PDF output dengan overload ini. Potongan kode berikut menunjukkan cara membuat buku saku menggunakan ukuran halaman dan jalur file.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MakeBookletOfPdfUsingPageSizeAndFilePaths()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Make booklet
    pdfEditor.MakeBooklet(dataDir + "MakeBookletInput.pdf", dataDir + "MakeBookletUsingPageSizeAndPaths_out.pdf", PageSize.A5);
}
```

## Buat Buku Saku dari PDF Menggunakan Ukuran Halaman, Halaman Kiri dan Kanan yang Ditentukan, dan Jalur File

[MakeBooklet](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/makebooklet/index) metode dari kelas [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) memungkinkan Anda untuk membuat buku saku dari file PDF input dan menyimpannya ke file PDF output. Overload ini memungkinkan Anda untuk membuat buku saku menggunakan jalur file. Anda juga dapat mengatur ukuran halaman dari file PDF output dan menentukan halaman tertentu untuk sisi kiri dan kanan dari file PDF output dengan overload ini. Potongan kode berikut menunjukkan cara membuat buku saku menggunakan ukuran halaman, halaman kiri dan kanan yang ditentukan, dan jalur file.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MakeBookletOfPdfUsingPageSizeSpecifiedLeftAndRightPagesAndFilePaths()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Set left and right pages
    var leftPages = new int[] { 1, 5 };
    var rightPages = new int[] { 2, 3 };
    // Make booklet
    pdfEditor.MakeBooklet(dataDir + "MakeBookletMultiplePagesInput.pdf", dataDir + "MakeBookletUsingLeftRightPagesAndPaths_out.pdf", PageSize.A5, leftPages, rightPages);
}
```

## Buat Buku Saku dari PDF Menggunakan Halaman Kiri dan Kanan yang Ditentukan, dan Jalur File

[MakeBooklet](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/makebooklet/index)  metode dari kelas [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) memungkinkan Anda untuk membuat buku saku dari file PDF input dan menyimpannya ke file PDF output. Overload ini memungkinkan Anda untuk membuat buku saku menggunakan jalur file. Anda juga dapat menentukan halaman tertentu untuk sisi kiri dan kanan dari file PDF output dengan overload ini. Potongan kode berikut menunjukkan cara membuat buku saku menggunakan halaman kiri dan kanan yang ditentukan dan jalur file.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MakeBookletOfPdfUsingSpecifiedLeftAndRightPagesAndFilePaths()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Set left and right pages
    var leftPages = new int[] { 1, 5 };
    var rightPages = new int[] { 2, 3 };
    // Make booklet
    pdfEditor.MakeBooklet(dataDir + "MakeBookletMultiplePagesInput.pdf", dataDir + "MakeBookletUsingLeftRightPagesAndPaths_out.pdf", leftPages, rightPages);
}
```

## Buat Buku Saku dari PDF Menggunakan Aliran

[MakeBooklet](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/makebooklet/index)  metode dari kelas [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) memungkinkan Anda untuk membuat buku saku dari aliran PDF input dan menyimpannya ke aliran PDF output. Overload ini memungkinkan Anda untuk membuat buku saku menggunakan aliran alih-alih jalur file. Potongan kode berikut menunjukkan cara membuat buku saku menggunakan aliran.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MakeBookletOfPdfUsingStreams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Create streams
    using (var inputStream = new FileStream(dataDir + "MakeBookletInput.pdf", FileMode.Open))
    {
        using (var outputStream = new FileStream(dataDir + "MakeBookletUsingStreams_out.pdf", FileMode.Create))
        {
            // Make booklet
            pdfEditor.MakeBooklet(inputStream, outputStream);
        }
    }
}
```

## Buat Buku Saku dari PDF Menggunakan Ukuran Halaman dan Aliran

[MakeBooklet](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/makebooklet/index)  metode dari kelas [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) memungkinkan Anda untuk membuat buku saku dari aliran PDF input dan menyimpannya ke aliran PDF output. Overload ini memungkinkan Anda untuk membuat buku saku menggunakan aliran alih-alih jalur file. Anda juga dapat mengatur ukuran halaman dari aliran PDF output dengan overload ini. Potongan kode berikut menunjukkan cara membuat buku saku menggunakan ukuran halaman dan aliran.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MakeBookletOfPdfUsingPageSizeAndStreams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Create streams
    using (var inputStream = new FileStream(dataDir + "MakeBookletInput.pdf", FileMode.Open))
    {
        using (var outputStream = new FileStream(dataDir + "MakeBookletUsingPageSizeAndStreams_out.pdf", FileMode.Create))
        {
            // Make booklet
            pdfEditor.MakeBooklet(inputStream, outputStream, PageSize.A5);
        }
    }
}
```

## Buat Buku Saku dari PDF Menggunakan Ukuran Halaman, Halaman Kiri dan Kanan yang Ditentukan, dan Aliran

[MakeBooklet](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/makebooklet/index)  metode dari kelas [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) memungkinkan Anda untuk membuat buku saku dari aliran PDF input dan menyimpannya ke aliran PDF output. Overload ini memungkinkan Anda untuk membuat buku saku menggunakan aliran alih-alih jalur file. Anda juga dapat mengatur ukuran halaman dari file PDF output dan menentukan halaman tertentu untuk sisi kiri dan kanan dari aliran PDF output dengan overload ini. Potongan kode berikut menunjukkan cara membuat buku saku menggunakan ukuran halaman, halaman kiri dan kanan yang ditentukan, dan aliran.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MakeBookletOfPdfUsingPageSizeSpecifiedLeftAndRightPagesAndStreams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Create streams
    using (var inputStream = new FileStream(dataDir + "MakeBookletMultiplePagesInput.pdf", FileMode.Open))
    {
        using (var outputStream = new FileStream(dataDir + "MakeBookletUsingPageSizeLeftRightPagesAndStreams_out.pdf", FileMode.Create))
        {
            // Set left and right pages
            var leftPages = new int[] { 1, 5 };
            var rightPages = new int[] { 2, 3 };
            // Make booklet
            pdfEditor.MakeBooklet(inputStream, outputStream, PageSize.A5, leftPages, rightPages);
        }
    }
}
```

## Buat Buku Saku dari PDF Menggunakan Halaman Kiri dan Kanan yang Ditentukan, dan Aliran

[MakeBooklet](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/makebooklet/index)  metode dari kelas [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) memungkinkan Anda untuk membuat buku saku dari aliran PDF input dan menyimpannya ke aliran PDF output. Overload ini memungkinkan Anda untuk membuat buku saku menggunakan aliran alih-alih jalur file. Anda juga dapat menentukan halaman tertentu untuk sisi kiri dan kanan dari aliran PDF output dengan overload ini. Potongan kode berikut menunjukkan cara membuat buku saku menggunakan halaman kiri dan kanan yang ditentukan dan aliran.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MakeBookletOfPdfUsingSpecifiedLeftAndRightPagesAndStreams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Create streams
    using (var inputStream = new FileStream(dataDir + "MakeBookletMultiplePagesInput.pdf", FileMode.Open))
    {
        using (var outputStream = new FileStream(dataDir + "MakeBookletUsingLeftRightPagesAndStreams_out.pdf", FileMode.Create))
        {
            // Set left and right pages
            var leftPages = new int[] { 1, 5 };
            var rightPages = new int[] { 2, 3 };
            // Make booklet
            pdfEditor.MakeBooklet(inputStream, outputStream, leftPages, rightPages);
        }
    }
}
```