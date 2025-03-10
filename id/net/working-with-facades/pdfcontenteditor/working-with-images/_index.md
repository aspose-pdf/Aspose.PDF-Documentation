---
title: Bekerja dengan Gambar menggunakan PdfContentEditor
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 50
url: /id/net/working-with-images-in-pdf
description: Bagian ini menjelaskan cara menambahkan dan menghapus Gambar dengan Aspose.PDF Facades menggunakan Kelas PdfContentEditor.
lastmod: "2021-06-24"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Work with Images using PdfContentEditor",
    "alternativeHeadline": "Enhance PDF Images with PdfContentEditor Features",
    "abstract": "Aspose.PDF for .NET sekarang menawarkan kemampuan manajemen gambar yang ditingkatkan melalui kelas PdfContentEditor, memungkinkan pengguna untuk dengan mudah menghapus gambar tertentu dari halaman yang ditentukan atau sepenuhnya menghapus semua gambar dari file PDF. Selain itu, fitur ini memungkinkan penggantian gambar yang mulus, menyederhanakan proses pengeditan dan meningkatkan kustomisasi dokumen",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "415",
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
    "url": "/net/working-with-images-in-pdf",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/working-with-images-in-pdf"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF dapat melakukan tidak hanya tugas yang sederhana dan mudah tetapi juga dapat menangani tujuan yang lebih kompleks. Periksa bagian berikut untuk pengguna dan pengembang tingkat lanjut."
}
</script>

## Hapus Gambar dari Halaman Tertentu PDF (Facades)

Untuk menghapus gambar dari halaman tertentu, Anda perlu memanggil metode [DeleteImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfcontenteditor/deleteimage/methods/1) dengan parameter pageNumber dan index. Parameter index mewakili array bilangan bulat – indeks gambar yang akan dihapus. Pertama-tama, Anda perlu membuat objek dari kelas [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) dan kemudian memanggil metode [DeleteImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfcontenteditor/deleteimage/methods/1). Setelah itu, Anda dapat menyimpan file PDF yang diperbarui menggunakan metode [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save/index).

Potongan kode berikut menunjukkan kepada Anda cara menghapus gambar dari halaman tertentu PDF.

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DeleteImage()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Instantiate PdfContentEditor object
    using (var editor = new Aspose.Pdf.Facades.PdfContentEditor(new Aspose.Pdf.Document(dataDir + "sample.pdf")))
    {
        editor.DeleteImage(2, new[] { 2 });

        // Save PDF document
        editor.Save(dataDir + "PdfContentEditorDemo10.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DeleteImage()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Instantiate PdfContentEditor Object
    using var editor = new Aspose.Pdf.Facades.PdfContentEditor(new Aspose.Pdf.Document(dataDir + "sample.pdf"));

    editor.DeleteImage(2, new[] { 2 });

    // Save PDF document
    editor.Save(dataDir + "PdfContentEditorDemo10.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

## Hapus Semua Gambar dari File PDF (Facades)

Semua gambar dapat dihapus dari file PDF menggunakan metode [DeleteImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfcontenteditor/deleteimage/methods/1) dari [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor). Panggil metode [DeleteImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfcontenteditor/deleteimage/methods/1) – overload tanpa parameter – untuk menghapus semua gambar, dan kemudian simpan file PDF yang diperbarui menggunakan metode [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save/index).

Potongan kode berikut menunjukkan kepada Anda cara menghapus semua gambar dari file PDF.

{{< tabs tabID="2" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DeleteImages()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Instantiate PdfContentEditor object
    using (var editor = new Aspose.Pdf.Facades.PdfContentEditor(new Aspose.Pdf.Document(dataDir + "sample.pdf")))
    {
        editor.DeleteImage();

        // Save PDF document
        editor.Save(dataDir + "PdfContentEditorDemo11.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DeleteImages()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Instantiate PdfContentEditor object
    using var editor = new Aspose.Pdf.Facades.PdfContentEditor(new Aspose.Pdf.Document(dataDir + "sample.pdf"));

    editor.DeleteImage();

    // Save PDF document
    editor.Save(dataDir + "PdfContentEditorDemo11.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

## Ganti Gambar dalam File PDF (Facades)

Kelas [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) memungkinkan Anda mengganti gambar Anda dalam file PDF, panggil untuk ini metode [ReplaceImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/replaceimage), dan simpan hasilnya.

{{< tabs tabID="3" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ReplaceImage()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Instantiate PdfContentEditor object
    using (var editor = new Aspose.Pdf.Facades.PdfContentEditor(new Aspose.Pdf.Document(dataDir + "sample_cats_dogs.pdf")))
    {
        editor.ReplaceImage(2, 4, dataDir + "Image.jpg");

        // Save PDF document
        editor.Save(dataDir + "PdfContentEditorDemo12.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ReplaceImage()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Instantiate PdfContentEditor object
    using var editor = new Aspose.Pdf.Facades.PdfContentEditor(new Aspose.Pdf.Document(dataDir + "sample_cats_dogs.pdf"));
    editor.ReplaceImage(2, 4, dataDir + "Image.jpg");

    // Save PDF document
    editor.Save(dataDir + "PdfContentEditorDemo12.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}