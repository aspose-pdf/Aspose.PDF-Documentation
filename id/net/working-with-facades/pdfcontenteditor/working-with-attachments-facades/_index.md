---
title: Bekerja dengan Lampiran - Facades
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 50
url: /id/net/working-with-attachments-facades/
description: Bagian ini menjelaskan cara bekerja dengan Lampiran - Facades menggunakan Kelas PdfContentEditor.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Working with Attachments - Facades",
    "alternativeHeadline": "Enhanced PDF Attachment Management",
    "abstract": "Fitur Bekerja dengan Lampiran - Facades di Aspose.PDF for .NET memungkinkan pengguna untuk dengan mudah mengelola lampiran file dalam dokumen PDF. Dengan fungsionalitas untuk menambahkan, mengambil, dan menghapus berbagai jenis file secara programatis menggunakan kelas PdfContentEditor, fitur ini menyederhanakan proses peningkatan interaktivitas PDF dengan memungkinkan lampiran diintegrasikan secara mulus",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "589",
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
    "url": "/net/working-with-attachments-facades/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/working-with-attachments-facades/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF dapat melakukan tidak hanya tugas sederhana dan mudah tetapi juga menangani tujuan yang lebih kompleks. Periksa bagian berikut untuk pengguna dan pengembang tingkat lanjut."
}
</script>

Dalam bagian ini, kami akan menjelaskan cara bekerja dengan lampiran dalam PDF menggunakan Aspose.PDF for .NET Facades. Lampiran adalah file tambahan yang dilampirkan pada dokumen induk, bisa berupa berbagai jenis file, seperti pdf, word, gambar, atau file lainnya. Anda akan belajar cara menambahkan lampiran ke pdf, mendapatkan informasi tentang lampiran, dan menyimpannya ke file, menghapus lampiran dari PDF secara programatis dengan C#.

## Tambahkan Lampiran dari File dalam PDF yang Ada

Anda dapat menambahkan lampiran dalam file PDF yang ada menggunakan kelas [PdfContentEditor](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/pdfcontenteditor). Lampiran dapat ditambahkan dari file di disk menggunakan jalur file. Anda dapat menambahkan lampiran menggunakan metode [AddDocumentAttachment](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/pdfcontenteditor/methods/adddocumentattachment). Metode ini mengambil dua argumen: jalur file dan deskripsi lampiran. Pertama, Anda perlu membuka file PDF yang ada dan menambahkan lampiran ke dalamnya. Kemudian Anda dapat menyimpan file PDF keluaran menggunakan metode [Save](https://reference.aspose.com/pdf/id/net/aspose.pdf/document/methods/save/index) dari [PdfContentEditor](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/pdfcontenteditor).

Potongan kode berikut menunjukkan cara menambahkan lampiran dari file. Misalnya, mari kita tambahkan file MP3.

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddAttachment()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Instantiate PdfContentEditor object
    using (var editor =  new Aspose.Pdf.Facades.PdfContentEditor(new Aspose.Pdf.Document(dataDir + "AddAttachment.pdf")))
    {
        editor.AddDocumentAttachment(dataDir + "Demo_MP3.mp3", "Demo MP3 file");

        // Save PDF document
        editor.Save(dataDir + "AddAttachment_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddAttachment()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Instantiate PdfContentEditor object
    using var editor = new Aspose.Pdf.Facades.PdfContentEditor(new Aspose.Pdf.Document(dataDir + "AddAttachment.pdf"));
    editor.AddDocumentAttachment(dataDir + "Demo_MP3.mp3", "Demo MP3 file");

    // Save PDF document
    editor.Save(dataDir + "AddAttachment_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

## Tambahkan Lampiran dari Stream dalam PDF yang Ada

Lampiran dapat ditambahkan dalam file PDF dari stream – FileStream – menggunakan metode [AddDocumentAttachment](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/pdfcontenteditor/methods/adddocumentattachment). Metode ini mengambil tiga argumen: stream, nama lampiran, dan deskripsi lampiran. Untuk menambahkan lampiran, Anda perlu membuat objek dari kelas [PdfContentEditor](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/pdfcontenteditor) dan mengikat file PDF input menggunakan metode [BindPdf](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/facade/methods/bindpdf/index). Setelah itu, Anda dapat memanggil metode [AddDocumentAttachment](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/pdfcontenteditor/methods/adddocumentattachment) untuk menambahkan lampiran. Akhirnya, Anda dapat memanggil metode Save untuk menyimpan file PDF yang diperbarui. Potongan kode berikut menunjukkan cara menambahkan lampiran dari Stream.

{{< tabs tabID="2" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddAttachment()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Instantiate PdfContentEditor object
    using (var editor = new Aspose.Pdf.Facades.PdfContentEditor(new Aspose.Pdf.Document(dataDir + "AddAttachment.pdf")))
    {
        var fileStream = File.OpenRead(dataDir + "Demo_MP3.mp3");
        editor.AddDocumentAttachment(fileStream, "Demo_MP3.mp3", "Demo MP3 file");

        // Save PDF document
        editor.Save(dataDir + "AddAttachment_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddAttachment()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Instantiate PdfContentEditor object
    using var editor = new Aspose.Pdf.Facades.PdfContentEditor(new Aspose.Pdf.Document(dataDir + "AddAttachment.pdf"));

    var fileStream = File.OpenRead(dataDir + "Demo_MP3.mp3");
    editor.AddDocumentAttachment(fileStream, "Demo_MP3.mp3", "Demo MP3 file");

    // Save PDF document
    editor.Save(dataDir + "AddAttachment_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

## Hapus Semua Lampiran dari File PDF yang Ada

Metode [DeleteAttachments](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/pdfcontenteditor/methods/deleteattachments) dari kelas [PdfContentEditor](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/pdfcontenteditor) memungkinkan Anda untuk menghapus semua lampiran dari file PDF yang ada. Panggil metode [DeleteAttachments](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/pdfcontenteditor/methods/deleteattachments). Akhirnya, Anda harus memanggil metode [Save](https://reference.aspose.com/pdf/id/net/aspose.pdf/document/methods/save/index) untuk menyimpan file PDF yang diperbarui. Potongan kode berikut menunjukkan cara menghapus semua lampiran dari file PDF yang ada.

{{< tabs tabID="3" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DeleteAllAttachments()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Instantiate PdfContentEditor object
    using (var editor = new Aspose.Pdf.Facades.PdfContentEditor(new Aspose.Pdf.Document(dataDir + "DeleteAllAttachments.pdf")))
    {
        editor.DeleteAttachments();

        // Save PDF document
        editor.Save(dataDir + "DeleteAllAttachments_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DeleteAllAttachments()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Instantiate PdfContentEditor object
    using var editor = new Aspose.Pdf.Facades.PdfContentEditor(new Aspose.Pdf.Document(dataDir + "DeleteAllAttachments.pdf"));
    editor.DeleteAttachments();

    // Save PDF document
    editor.Save(dataDir + "DeleteAllAttachments_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}