---
title: Dapatkan Metadata XMP dari File PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 30
url: /id/net/get-xmp-metadata-of-an-existing-pdf-file/
description: Bagian ini menjelaskan cara mendapatkan Metadata XMP dari PDF yang ada dengan Aspose.PDF Facades.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Get XMP Metadata of PDF File",
    "alternativeHeadline": "Extract XMP Metadata from PDF Files Easily",
    "abstract": "Buka wawasan mendetail dari file PDF Anda dengan fitur Metadata XMP baru di Aspose.PDF for .NET. Fungsionalitas ini memungkinkan Anda untuk dengan mudah mengekstrak properti metadata XMP tertentu, memungkinkan pengelolaan dan pengkategorian dokumen Anda yang lebih baik. Sederhanakan alur kerja Anda dan tingkatkan kegunaan PDF Anda dengan ekstraksi metadata yang tepat",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "213",
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
    "url": "/net/get-xmp-metadata-of-an-existing-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/get-xmp-metadata-of-an-existing-pdf-file/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF dapat melakukan tidak hanya tugas yang sederhana dan mudah tetapi juga dapat menangani tujuan yang lebih kompleks. Periksa bagian berikut untuk pengguna dan pengembang tingkat lanjut."
}
</script>

Untuk mendapatkan metadata XMP dari file PDF, Anda perlu membuat objek [PdfXmpMetadata](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/pdfxmpmetadata) dan mengikat file PDF menggunakan metode [BindPdf](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/facade/methods/bindpdf/index). Anda dapat mengirimkan properti metadata XMP tertentu ke objek [PdfXmpMetadata](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/pdfxmpmetadata) untuk mendapatkan nilainya. Potongan kode berikut menunjukkan cara mendapatkan metadata XMP dari file PDF.

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetXmpMetadata()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_WorkingDocuments();

    // Create PdfXmpMetadata object
    using (var xmpMetaData = new Aspose.Pdf.Facades.PdfXmpMetadata())
    {
        // Bind PDF document
        xmpMetaData.BindPdf(dataDir + "GetXMPMetadata.pdf");

        // Get XMP Meta Data properties
        Console.WriteLine(": {0}", xmpMetaData[Aspose.Pdf.Facades.DefaultMetadataProperties.CreateDate].ToString());
        Console.WriteLine(": {0}", xmpMetaData[Aspose.Pdf.Facades.DefaultMetadataProperties.MetadataDate].ToString());
        Console.WriteLine(": {0}", xmpMetaData[Aspose.Pdf.Facades.DefaultMetadataProperties.CreatorTool].ToString());
        Console.WriteLine(": {0}", xmpMetaData["customNamespace:UserPropertyName"].ToString());

        Console.ReadLine();
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetXmpMetadata()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_WorkingDocuments();

    // Create PdfXmpMetadata object
    using var xmpMetaData = new Aspose.Pdf.Facades.PdfXmpMetadata();

    // Bind PDF document
    xmpMetaData.BindPdf(dataDir + "GetXMPMetadata.pdf");

    // Get XMP Meta Data properties
    Console.WriteLine(": {0}", xmpMetaData[Aspose.Pdf.Facades.DefaultMetadataProperties.CreateDate].ToString());
    Console.WriteLine(": {0}", xmpMetaData[Aspose.Pdf.Facades.DefaultMetadataProperties.MetadataDate].ToString());
    Console.WriteLine(": {0}", xmpMetaData[Aspose.Pdf.Facades.DefaultMetadataProperties.CreatorTool].ToString());
    Console.WriteLine(": {0}", xmpMetaData["customNamespace:UserPropertyName"].ToString());

    Console.ReadLine();
}
```
{{< /tab >}}
{{< /tabs >}}