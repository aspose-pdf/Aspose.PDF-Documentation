---
title: Mengubah ukuran halaman dalam file PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 30
url: /id/net/changing-page-sizes-in-a-pdf-file/
description: Cobalah untuk mempelajari cara mengubah ukuran halaman dalam file PDF menggunakan PdfPageEditor Class.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Changing page sizes in PDF file",
    "alternativeHeadline": "Effortlessly Adjust PDF Page Sizes with PdfPageEditor",
    "abstract": "Fitur dari kelas PdfPageEditor di Aspose.Pdf memungkinkan pengguna untuk dengan mudah mengubah ukuran halaman dari halaman individu atau beberapa halaman dalam file PDF. Dengan memanfaatkan properti PageSize dan properti Pages, pengguna dapat memilih dari berbagai ukuran halaman yang telah ditentukan sebelumnya dan menerapkannya secara efektif, meningkatkan fleksibilitas dan kustomisasi tata letak dokumen PDF.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "197",
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
    "url": "/net/changing-page-sizes-in-a-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/changing-page-sizes-in-a-pdf-file/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF tidak hanya dapat melakukan tugas yang sederhana dan mudah, tetapi juga dapat mengatasi tujuan yang lebih kompleks. Periksa bagian berikut untuk pengguna dan pengembang yang lebih mahir."
}
</script>

## Detail Implementasi

Kelas [PdfPageEditor](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/pdfpageeditor) di dalam namespace [Aspose.Pdf.Facades namespace](https://docs-qa.aspose.com/display/pdftemp/Aspose.Pdf.Facades+namespace) mengandung properti bernama [PageSize](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/pdfpageeditor/properties/pagesize) yang dapat digunakan untuk mengubah ukuran halaman dari sebuah halaman atau beberapa halaman sekaligus. Properti Pages dapat digunakan untuk menetapkan nomor halaman di mana ukuran halaman baru harus diterapkan. Kelas PageSize memuat daftar berbagai ukuran halaman sebagai anggotanya. Salah satu anggota dari kelas ini dapat ditetapkan ke properti PageSize dari kelas [PdfPageEditor](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/pdfpageeditor). Anda juga dapat memperoleh ukuran halaman dari halaman manapun dengan menggunakan metode GetPageSize dan memasukkan nomor halaman.

```csharp
 // For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ChangePdfPageSize()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Create PdfPageEditor object
    using (var pdfPageEditor = new Aspose.Pdf.Facades.PdfPageEditor())
    {
        // Bind PDF document
        pdfPageEditor.BindPdf(dataDir + "FilledForm.pdf");

        // Change page size of the selected pages
        pdfPageEditor.ProcessPages = new[] { 1 };

        // Select a predefined page size (LETTER) and assign it
        pdfPageEditor.PageSize = Aspose.Pdf.PageSize.PageLetter;

        // Save the file with the updated page size
        pdfPageEditor.Save(dataDir + "ChangePageSizes_out.pdf");

        // Get and display the page size assigned
        pdfPageEditor.BindPdf(dataDir + "FilledForm.pdf");

        var pageSize = pdfPageEditor.GetPageSize(1);
        Console.WriteLine($"Width: {pageSize.Width}, Height: {pageSize.Height}");
    }
}
```