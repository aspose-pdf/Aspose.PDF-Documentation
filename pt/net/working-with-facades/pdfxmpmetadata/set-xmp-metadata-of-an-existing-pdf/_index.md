---
title: Definir Metadados XMP de um PDF existente
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /pt/net/set-xmp-metadata-of-an-existing-pdf/
description: Esta seção explica como definir Metadados XMP de um PDF existente com Aspose.PDF Facades.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Set XMP Metadata of an existing PDF",
    "alternativeHeadline": "Set XMP Metadata for Existing PDF Files",
    "abstract": "Apresentando um recurso poderoso que permite aos usuários definir metadados XMP para arquivos PDF existentes usando Aspose.PDF for .NET Facades. Essa funcionalidade capacita os usuários a vincular facilmente documentos PDF e personalizar propriedades essenciais de metadados, melhorando a gestão de documentos e as capacidades de recuperação de informações. Com métodos simples para adicionar, modificar e salvar metadados, os usuários podem otimizar seus arquivos PDF para melhor organização e conformidade.",
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
    "description": "Aspose.PDF pode realizar não apenas tarefas simples e fáceis, mas também lidar com objetivos mais complexos. Confira a próxima seção para usuários e desenvolvedores avançados."
}
</script>

Para definir metadados XMP em um arquivo PDF, você precisa criar um objeto [PdfXmpMetadata](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfxmpmetadata) e vincular o arquivo PDF usando o método [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index). Você pode usar o método [Add](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfxmpmetadata/methods/add/index) da classe [PdfXmpMetadata](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfxmpmetadata) para adicionar diferentes propriedades. Finalmente, chame o método [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save/index) da classe [PdfXmpMetadata](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfxmpmetadata). O seguinte trecho de código mostra como adicionar metadados XMP em um arquivo PDF.

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