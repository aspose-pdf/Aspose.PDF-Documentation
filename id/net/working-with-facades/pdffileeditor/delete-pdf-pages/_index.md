---
title: Hapus Halaman PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 70
url: /id/net/delete-pdf-pages/
description: Bagian ini menjelaskan cara menghapus halaman PDF dengan Aspose.PDF Facades menggunakan kelas PdfFileEditor.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Delete PDF pages",
    "alternativeHeadline": "Effortlessly Remove Pages from PDF Files",
    "abstract": "Hapus halaman tertentu dari dokumen PDF Anda dengan mudah menggunakan Aspose.PDF for .NET Facades. Dengan memanfaatkan kelas PdfFileEditor, Anda dapat menghapus halaman yang tidak diinginkan dari jalur file dan aliran, menyederhanakan proses pengeditan PDF Anda dengan kontrol yang tepat atas output akhir. Tingkatkan kemampuan manajemen dokumen Anda dengan fitur penghapusan halaman yang efisien ini.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "262",
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
    "url": "/net/delete-pdf-pages/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/delete-pdf-pages/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF dapat melakukan tidak hanya tugas yang sederhana dan mudah tetapi juga dapat menangani tujuan yang lebih kompleks. Periksa bagian berikut untuk pengguna dan pengembang tingkat lanjut."
}
</script>

Jika Anda ingin menghapus sejumlah halaman dari file PDF yang berada di disk, maka Anda dapat menggunakan overload dari metode [Delete](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/pdffileeditor/methods/delete/index) yang mengambil tiga parameter berikut: jalur file input, array nomor halaman yang akan dihapus, dan jalur file PDF output. Parameter kedua adalah array integer yang mewakili semua halaman yang perlu dihapus. Halaman yang ditentukan dihapus dari file input dan hasilnya disimpan sebagai file output. Cuplikan kode berikut menunjukkan cara menghapus halaman PDF menggunakan jalur file.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DeletePages()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Array of pages to delete
    var pagesToDelete = new int[] { 1, 2 };
    // Delete pages
    pdfEditor.Delete(dataDir + "DeletePagesInput.pdf", pagesToDelete, dataDir + "DeletePagesUsingFilePath_out.pdf");
}
```

## Hapus Halaman PDF Menggunakan Aliran

Metode [Delete](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/pdffileeditor/methods/delete/index) dari kelas [PdfFileEditor](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/pdffileeditor) juga menyediakan overload yang memungkinkan Anda untuk menghapus halaman dari file PDF input, sementara kedua file input dan output berada dalam aliran. Overload ini mengambil tiga parameter berikut: aliran input, array integer dari halaman PDF yang akan dihapus, dan aliran output. Cuplikan kode berikut menunjukkan cara menghapus halaman PDF menggunakan aliran.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DeletePagesUsingStreams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Create streams
    using (var inputStream = new FileStream(dataDir + "DeletePagesInput.pdf", FileMode.Open))
    {
        using (var outputStream = new FileStream(dataDir + "DeletePagesUsingStream_out.pdf", FileMode.Create))
        {
            // Array of pages to delete
            var pagesToDelete = new int[] { 1, 2 };
            // Delete pages
            pdfEditor.Delete(inputStream, pagesToDelete, outputStream);
        }
    }
}
```