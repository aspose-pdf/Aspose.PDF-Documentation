---
title: Obter Metadados XMP de Arquivo PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 30
url: /pt/net/get-xmp-metadata-of-an-existing-pdf-file/
description: Esta seção explica como obter Metadados XMP de um PDF existente com Aspose.PDF Facades.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Get XMP Metadata of PDF File",
    "alternativeHeadline": "Extract XMP Metadata from PDF Files Easily",
    "abstract": "Desbloqueie insights detalhados de seus arquivos PDF com o novo recurso de Metadados XMP em Aspose.PDF for .NET. Essa funcionalidade permite que você extraia facilmente propriedades específicas de metadados XMP, possibilitando uma melhor gestão e categorização de seus documentos. Otimize seu fluxo de trabalho e aumente a utilidade de seus PDFs com a extração precisa de metadados",
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
    "description": "Aspose.PDF pode realizar não apenas tarefas simples e fáceis, mas também lidar com objetivos mais complexos. Confira a próxima seção para usuários e desenvolvedores avançados."
}
</script>

Para obter metadados XMP de um arquivo PDF, você precisa criar um objeto [PdfXmpMetadata](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfxmpmetadata) e vincular o arquivo PDF usando o método [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index). Você pode passar propriedades específicas de metadados XMP para o objeto [PdfXmpMetadata](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfxmpmetadata) para obter seus valores. O seguinte trecho de código mostra como obter metadados XMP de um arquivo PDF.

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