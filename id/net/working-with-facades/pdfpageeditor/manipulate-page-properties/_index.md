---
title: Manipulasi Properti Halaman
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 80
url: /id/net/manipulate-page-properties/
description: Bagian ini menjelaskan cara memanipulasi Properti Halaman dengan Aspose.PDF Facades menggunakan Kelas PdfPageEditor.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Manipulate Page Properties",
    "alternativeHeadline": "Enhance PDF Page Control with PdfPageEditor Features",
    "abstract": "Memperkenalkan kelas PdfPageEditor, alat yang kuat untuk mengelola properti halaman PDF dengan Aspose.PDF for .NET Facades. Fitur ini memungkinkan pengembang untuk mengambil dan memodifikasi atribut halaman penting seperti rotasi, tingkat zoom, dan dimensi halaman, memberikan kontrol yang lebih baik atas presentasi konten PDF. Dengan metode yang sederhana untuk mendapatkan dan mengatur properti, termasuk kemampuan untuk mengubah ukuran konten halaman tertentu, meningkatkan dokumen PDF tidak pernah semudah ini.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "483",
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
    "url": "/net/manipulate-page-properties/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/manipulate-page-properties/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF dapat melakukan tidak hanya tugas yang sederhana dan mudah tetapi juga menangani tujuan yang lebih kompleks. Periksa bagian berikut untuk pengguna dan pengembang tingkat lanjut."
}
</script>

## Dapatkan Properti Halaman PDF dari File PDF yang Ada

[PdfPageEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor) memungkinkan Anda bekerja dengan halaman individual dari file PDF. Ini membantu Anda mendapatkan properti halaman individual seperti ukuran kotak halaman yang berbeda, rotasi halaman, zoom halaman, dll. Untuk mendapatkan properti tersebut, Anda perlu membuat objek [PdfPageEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor) dan mengikat file PDF input menggunakan metode [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3). Setelah itu, Anda dapat menggunakan berbagai metode untuk mendapatkan properti halaman seperti [GetPageRotation](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor/methods/getpagerotation), [GetPages](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor/methods/getpages), [GetPageBoxSize](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor/methods/getpageboxsize), dll.

Potongan kode berikut menunjukkan cara mendapatkan properti halaman PDF dari file PDF yang ada.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetPdfPageProperties()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var pageEditor = new Aspose.Pdf.Facades.PdfPageEditor())
    {
        // Bind PDF document
        pageEditor.BindPdf(dataDir + "input.pdf");

        // Get page properties and print them to the console
        Console.WriteLine($"Page 1 Rotation: {pageEditor.GetPageRotation(1)}");
        Console.WriteLine($"Total Pages: {pageEditor.GetPages()}");
        Console.WriteLine($"Trim Box Size of Page 1: {pageEditor.GetPageBoxSize(1, "trim")}");
        Console.WriteLine($"Art Box Size of Page 1: {pageEditor.GetPageBoxSize(1, "art")}");
        Console.WriteLine($"Bleed Box Size of Page 1: {pageEditor.GetPageBoxSize(1, "bleed")}");
        Console.WriteLine($"Crop Box Size of Page 1: {pageEditor.GetPageBoxSize(1, "crop")}");
        Console.WriteLine($"Media Box Size of Page 1: {pageEditor.GetPageBoxSize(1, "media")}");
    }
}
```

## Atur Properti Halaman PDF dalam File PDF yang Ada

Untuk mengatur properti halaman seperti rotasi halaman, zoom, atau titik asal, Anda perlu menggunakan kelas [PdfPageEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor). Kelas ini menyediakan berbagai metode dan properti untuk mengatur properti halaman ini. Pertama-tama, Anda perlu membuat objek dari kelas [PdfPageEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor) dan mengikat file PDF input menggunakan metode [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3). Setelah itu, Anda dapat menggunakan metode dan properti ini untuk mengatur properti halaman. Terakhir, simpan file PDF yang diperbarui menggunakan metode [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save).

Potongan kode berikut menunjukkan cara mengatur properti halaman PDF dalam file PDF yang ada.

```csharp
 // For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetPdfPageProperties()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var pageEditor = new Aspose.Pdf.Facades.PdfPageEditor())
    {
        // Bind PDF document
        pageEditor.BindPdf(dataDir + "input.pdf");

        // Set page properties
        // Move origin from (0,0)
        pageEditor.MovePosition(100, 100);

        // Set page rotations
        var pageRotations = new System.Collections.Hashtable
        {
            { 1, 90 },
            { 2, 180 },
            { 3, 270 }
        };

        // Set zoom where 1.0f = 100% zoom
        pageEditor.Zoom = 2.0f;

        // Save PDF document
        pageEditor.Save(dataDir + "SetPageProperties_out.pdf");
    }
}
```

## Ubah Ukuran Konten Halaman dari Halaman Tertentu dalam File PDF

Metode ResizeContents dari kelas [PdfPageEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor) memungkinkan Anda untuk mengubah ukuran konten halaman dalam file PDF. Kelas [ContentsResizeParameters](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffileeditor/contentsresizeparameters) digunakan untuk menentukan parameter yang akan digunakan untuk mengubah ukuran halaman, misalnya margin dalam persentase atau unit, dll. Anda dapat mengubah ukuran semua halaman atau menentukan array halaman yang akan diubah ukurannya menggunakan metode ResizeContents.

Potongan kode berikut menunjukkan cara mengubah ukuran konten dari beberapa halaman tertentu dalam file PDF. 

```csharp
  // For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
 private static void ResizePdfPageContents()
 {
     // The path to the documents directory
     var dataDir = RunExamples.GetDataDir_AsposePdf();

     // Create PdfFileEditor Object
     var fileEditor = new Aspose.Pdf.Facades.PdfFileEditor();

     // Open PDF Document
     using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
     {
         // Specify Parameters to be used for resizing
         var parameters = new Aspose.Pdf.Facades.PdfFileEditor.ContentsResizeParameters(
             // Left margin = 10% of page width
             PdfFileEditor.ContentsResizeValue.Percents(10),
             // New contents width calculated automatically as width - left margin - right margin (100% - 10% - 10% = 80%)
             null,
             // Right margin is 10% of page
             PdfFileEditor.ContentsResizeValue.Percents(10),
             // Top margin = 10% of height
             PdfFileEditor.ContentsResizeValue.Percents(10),
             // New contents height is calculated automatically (similar to width)
             null,
             // Bottom margin is 10%
             PdfFileEditor.ContentsResizeValue.Percents(10)
         );

         // Resize Page Contents
         fileEditor.ResizeContents(document, new[] { 1, 2 }, parameters);

         // Save PDF document
         document.Save(dataDir + "ResizePageContents_out.pdf");
     }
 }
```