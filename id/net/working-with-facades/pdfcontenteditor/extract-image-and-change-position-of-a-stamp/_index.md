---
title: Ekstrak gambar dan ubah posisi cap
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 30
url: /id/net/extract-image-and-change-position-of-a-stamp/
description: Bagian ini menjelaskan cara mengekstrak Gambar dan Mengubah Posisi Cap dengan Aspose.PDF Facades.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Extract image and change stamp position",
    "alternativeHeadline": "Extract Images and Adjust Stamp Positions in PDF",
    "abstract": "Fitur dalam Aspose.PDF for .NET memungkinkan pengguna untuk secara efisien mengekstrak gambar dari cap PDF dan memposisikannya kembali dengan presisi. Dengan memanfaatkan kelas PdfContentEditor, pengembang dapat dengan mudah mengelola dan memanipulasi gambar cap, meningkatkan kemampuan pengeditan PDF mereka dan memperbaiki presentasi dokumen secara keseluruhan",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "393",
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
    "url": "/net/extract-image-and-change-position-of-a-stamp/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/extract-image-and-change-position-of-a-stamp/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF dapat melakukan tidak hanya tugas sederhana dan mudah tetapi juga menangani tujuan yang lebih kompleks. Periksa bagian berikut untuk pengguna dan pengembang tingkat lanjut."
}
</script>

## Ekstrak Gambar dari Cap Gambar

Kelas [PdfContentEditor](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/pdfcontenteditor) memungkinkan Anda untuk mengekstrak gambar dari cap dalam file PDF. Pertama, Anda perlu membuat objek dari kelas [PdfContentEditor](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/pdfcontenteditor) dan mengikat file PDF input menggunakan metode [BindPdf](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades.facade/bindpdf/methods/3). Setelah itu, panggil metode [GetStamps](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/pdfcontenteditor/methods/getstamps) untuk mendapatkan array objek StampInfo dari halaman tertentu dalam file PDF. Kemudian Anda dapat mendapatkan gambar dari StampInfo menggunakan properti StampInfo.Image. Setelah Anda mendapatkan gambar, Anda dapat menyimpan gambar tersebut atau bekerja dengan berbagai properti gambar. Potongan kode berikut menunjukkan cara mengekstrak gambar dari cap gambar.

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractImageFromStamp()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_StampsWatermarks();

    // Instantiate PdfContentEditor object
    using (var pdfContentEditor = new Aspose.Pdf.Facades.PdfContentEditor())
    {
        // Bind PDF document
        pdfContentEditor.BindPdf(dataDir + "ExtractImage-ImageStamp.pdf");

        // Get Stamp info for the first stamp
        var infos = pdfContentEditor.GetStamps(1);

        // Get the image from Stamp Info
        var image = infos[0].Image;

        // Save the extracted image
        image.Save(dataDir + "image_out.jpg");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractImageFromStamp()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_StampsWatermarks();

    // Instantiate PdfContentEditor object
    using var pdfContentEditor = new Aspose.Pdf.Facades.PdfContentEditor();

    // Bind PDF document
    pdfContentEditor.BindPdf(dataDir + "ExtractImage-ImageStamp.pdf");

    // Get Stamp info for the first stamp
    var infos = pdfContentEditor.GetStamps(1);

    // Get the image from Stamp Info
    var image = infos[0].Image;

    // Save the extracted image
    image.Save(dataDir + "image_out.jpg");
}
```
{{< /tab >}}
{{< /tabs >}}

## Ubah Posisi Cap dalam file PDF

Kelas [PdfContentEditor](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/pdfcontenteditor) memungkinkan Anda untuk mengubah posisi cap dalam file PDF. Pertama, Anda perlu membuat objek dari kelas [PdfContentEditor](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/pdfcontenteditor) dan mengikat file PDF input menggunakan metode [BindPdf](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades.facade/bindpdf/methods/3). Setelah itu, panggil metode [MoveStamp](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/pdfcontenteditor/methods/movestamp) dengan indeks cap dan posisi baru di halaman tertentu dalam file PDF. Kemudian, Anda dapat menyimpan file yang diperbarui menggunakan metode [Save](https://reference.aspose.com/pdf/id/net/aspose.pdf/document/methods/save). Potongan kode berikut menunjukkan cara memindahkan cap di halaman tertentu.

{{< tabs tabID="2" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ChangeStampPosition()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_StampsWatermarks();

    // Instantiate PdfContentEditor object
    using (var pdfContentEditor = new Aspose.Pdf.Facades.PdfContentEditor())
    {
        // Bind PDF document
        pdfContentEditor.BindPdf(dataDir + "ChangeStampPosition.pdf");

        int pageId = 1;
        int stampIndex = 1;
        double x = 200;
        double y = 200;

        // Change the position of the stamp to new x and y position
        pdfContentEditor.MoveStamp(pageId, stampIndex, x, y);

        // Save PDF document
        pdfContentEditor.Save(dataDir + "ChangeStampPosition_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ChangeStampPosition()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_StampsWatermarks();

    // Instantiate PdfContentEditor object
    using var pdfContentEditor = new Aspose.Pdf.Facades.PdfContentEditor();

    // Bind PDF document
    pdfContentEditor.BindPdf(dataDir + "ChangeStampPosition.pdf");

    int pageId = 1;
    int stampIndex = 1;
    double x = 200;
    double y = 200;

    // Change the position of the stamp to new x and y position
    pdfContentEditor.MoveStamp(pageId, stampIndex, x, y);

    // Save PDF document
    pdfContentEditor.Save(dataDir + "ChangeStampPosition_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

Selain itu, Anda dapat menggunakan metode [MoveStampById](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/pdfcontenteditor/methods/movestampbyid) untuk memindahkan cap tertentu dengan menggunakan StampId.

{{< tabs tabID="3" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MoveStampById()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_StampsWatermarks();

    // Instantiate PdfContentEditor Object
    using (var pdfContentEditor = new Aspose.Pdf.Facades.PdfContentEditor())
    {
        // Bind PDF document
        pdfContentEditor.BindPdf(dataDir + "ChangeStampPosition.pdf");

        int pageId = 1;
        int stampId = 1;
        double x = 200;
        double y = 200;

        // Change the position of the stamp to new x and y position
        pdfContentEditor.MoveStamp(pageId, stampId, x, y);

        // Save PDF document
        pdfContentEditor.Save(dataDir + "ChangeStampPositionByID_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MoveStampById()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_StampsWatermarks();

    // Instantiate PdfContentEditor Object
    using var pdfContentEditor = new Aspose.Pdf.Facades.PdfContentEditor();

    // Bind PDF document
    pdfContentEditor.BindPdf(dataDir + "ChangeStampPosition.pdf");

    int pageId = 1;
    int stampId = 1;
    double x = 200;
    double y = 200;

    // Change the position of the stamp to new x and y position
    pdfContentEditor.MoveStamp(pageId, stampId, x, y);

    // Save PDF document
    pdfContentEditor.Save(dataDir + "ChangeStampPositionByID_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}