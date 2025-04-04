---
title: Mengatur Metadata XMP dari PDF yang ada
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /id/net/set-xmp-metadata-of-an-existing-pdf/
description: Bagian ini menjelaskan cara mengatur Metadata XMP dari PDF yang ada dengan Aspose.PDF Facades.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Set XMP Metadata of an existing PDF",
    "alternativeHeadline": "Set XMP Metadata for Existing PDF Files",
    "abstract": "Memperkenalkan fitur yang kuat yang memungkinkan pengguna untuk mengatur metadata XMP untuk file PDF yang ada menggunakan Aspose.PDF for .NET Facades. Fungsionalitas ini memberdayakan pengguna untuk dengan mudah mengikat dokumen PDF dan menyesuaikan properti metadata penting, meningkatkan manajemen dokumen dan kemampuan pengambilan informasi. Dengan metode yang sederhana untuk menambahkan, memodifikasi, dan menyimpan metadata, pengguna dapat mengoptimalkan file PDF mereka untuk organisasi yang lebih baik dan kepatuhan.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "317",
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
    "url": "/net/set-xmp-metadata-of-an-existing-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/set-xmp-metadata-of-an-existing-pdf/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF dapat melakukan tidak hanya tugas yang sederhana dan mudah tetapi juga mengatasi tujuan yang lebih kompleks. Periksa bagian berikut untuk pengguna dan pengembang tingkat lanjut."
}
</script>

Untuk mengatur metadata XMP dalam file PDF, Anda perlu membuat objek [PdfXmpMetadata](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfxmpmetadata) dan mengikat file PDF menggunakan metode [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index). Anda dapat menggunakan metode [Add](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfxmpmetadata/methods/add/index) dari kelas [PdfXmpMetadata](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfxmpmetadata) untuk menambahkan berbagai properti. Akhirnya, panggil metode [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save/index) dari kelas [PdfXmpMetadata](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfxmpmetadata). Potongan kode berikut menunjukkan kepada Anda cara menambahkan metadata XMP dalam file PDF.

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddXmpMetadata()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_WorkingDocuments();

    // Create PdfXmpMetadata object
    using (var xmpMetaData = new Aspose.Pdf.Facades.PdfXmpMetadata())
    {
        // Bind PDF document
        xmpMetaData.BindPdf(dataDir + "SetXMPMetadata.pdf");

        // Add create date
        xmpMetaData.Add(Aspose.Pdf.Facades.DefaultMetadataProperties.CreateDate, DateTime.Now.ToString());

        // Change meta data date
        xmpMetaData[Aspose.Pdf.Facades.DefaultMetadataProperties.MetadataDate] = DateTime.Now.ToString();

        // Add creator tool
        xmpMetaData.Add(Aspose.Pdf.Facades.DefaultMetadataProperties.CreatorTool, "Creator tool name");

        // Remove modify date
        xmpMetaData.Remove(Aspose.Pdf.Facades.DefaultMetadataProperties.ModifyDate);

        // Add user defined property
        // Register namespace prefix and URI
        xmpMetaData.RegisterNamespaceURI("customNamespace", "http:// Www.customNameSpaces.com/ns/");

        // Add user property with the prefix
        xmpMetaData.Add("customNamespace:UserPropertyName", "UserPropertyValue");

        // Change user defined property
        xmpMetaData["customNamespace:UserPropertyName"] = "UserPropertyValue2";

        // Save PDF document
        xmpMetaData.Save(dataDir + "SetXMPMetadata_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddXmpMetadata()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_WorkingDocuments();

    // Create PdfXmpMetadata object
    using var xmpMetaData = new Aspose.Pdf.Facades.PdfXmpMetadata();

    // Bind PDF document
    xmpMetaData.BindPdf(dataDir + "SetXMPMetadata.pdf");

    // Add create date
    xmpMetaData.Add(Aspose.Pdf.Facades.DefaultMetadataProperties.CreateDate, DateTime.Now.ToString());

    // Change meta data date
    xmpMetaData[Aspose.Pdf.Facades.DefaultMetadataProperties.MetadataDate] = DateTime.Now.ToString();

    // Add creator tool
    xmpMetaData.Add(Aspose.Pdf.Facades.DefaultMetadataProperties.CreatorTool, "Creator tool name");

    // Remove modify date
    xmpMetaData.Remove(Aspose.Pdf.Facades.DefaultMetadataProperties.ModifyDate);

    // Add user defined property
    // register namespace prefix and URI
    xmpMetaData.RegisterNamespaceURI("customNamespace", "http:// Www.customNameSpaces.com/ns/");

    // Add user property with the prefix
    xmpMetaData.Add("customNamespace:UserPropertyName", "UserPropertyValue");

    // Change user defined property
    xmpMetaData["customNamespace:UserPropertyName"] = "UserPropertyValue2";

    // Save PDF document
    xmpMetaData.Save(dataDir + "SetXMPMetadata_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}