---
title: Plataforma de Metadatos Extensible - XMP
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /es/net/working-with-extensible-metadata-platform-xmp/
description: Esta sección explica cómo trabajar con la Plataforma de Metadatos Extensible - XMP utilizando la clase PdfXmpMetadata.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Extensible Metadata Platform - XMP",
    "alternativeHeadline": "Enhanced PDF Metadata Management with XMP Integration",
    "abstract": "La funcionalidad de la Plataforma de Metadatos Extensible (XMP) en Aspose.PDF for .NET permite a los usuarios incrustar y manipular de manera eficiente metadatos estandarizados y propietarios dentro de archivos PDF. Utilizando la clase PdfXmpMetadata, esta característica simplifica el proceso de seguimiento de cambios y mejora las capacidades semánticas de los documentos PDF, convirtiéndola en una herramienta valiosa para los desarrolladores que buscan integrar una gestión avanzada de metadatos.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "412",
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
    "url": "/net/working-with-extensible-metadata-platform-xmp/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/working-with-extensible-metadata-platform-xmp/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF puede realizar no solo tareas simples y fáciles, sino también afrontar objetivos más complejos. Consulta la siguiente sección para usuarios y desarrolladores avanzados."
}
</script>

{{% alert color="primary" %}}

La Plataforma de Metadatos Extensible (XMP) es un estándar creado por Adobe Systems Inc. Este estándar fue desarrollado para procesar y almacenar metadatos estandarizados y propietarios. Estos metadatos pueden ser incrustados en diferentes formatos de archivo, pero en este artículo nos centraremos únicamente en el formato de archivo PDF. Veremos cómo podemos incrustar metadatos en un archivo PDF utilizando el espacio de nombres Aspose.Pdf.Facades en Aspose.PDF for .NET. Usaremos la clase [PdfXmpMetadata](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfxmpmetadata) para manipular XMP en el documento PDF.

{{% /alert %}}

## Antecedentes

Un archivo PDF pasa por muchas etapas durante su vida útil. Creamos un documento PDF y luego lo pasamos a otras personas o departamentos para su posterior procesamiento. Sin embargo, durante este proceso necesitamos hacer un seguimiento de diferentes aspectos de los cambios realizados. XMP sirve para este propósito de seguimiento de los cambios u otra información sobre los datos en el archivo.

## Explicación

Para manipular XMP utilizando Aspose.Pdf.Facades, utilizaremos la clase [PdfXmpMetadata](http://www.aspose.com/docs/display/pdfnet/PdfXmpMetadata+Class). Usaremos esta clase para manipular propiedades de metadatos predefinidas. La clase [PdfXmpMetadata](http://www.aspose.com/docs/display/pdfnet/PdfXmpMetadata+Class) agrega estas propiedades a un archivo PDF. También ayuda a abrir y guardar archivos PDF en los que estamos agregando metadatos. Así que, utilizando la clase [PdfXmpMetadata](http://www.aspose.com/docs/display/pdfnet/PdfXmpMetadata+Class), podemos manipular fácilmente XMP en un archivo PDF. El siguiente fragmento de código te ayudará a entender cómo usar la clase [PdfXmpMetadata](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfxmpmetadata) para trabajar con XMP:

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddXmpMetadata()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_TechnicalArticles();

    // Create an object of PdfXmpMetadata class
    var xmpMetaData = new Aspose.Pdf.Facades.PdfXmpMetadata();

    // Create input and output file streams
    using (var input = new FileStream(dataDir + "FilledForm.pdf", FileMode.Open))
    {
        using (var output = new FileStream(dataDir + "xmp_out.pdf", FileMode.Create))
        {
            // Bind PDF document
            xmpMetaData.BindPdf(input);

            // Add base URL property to xmp metadata
            xmpMetaData.Add(Aspose.Pdf.Facades.DefaultMetadataProperties.BaseURL, "xmlns:pdf=http:// Ns.adobe.com/pdf/1.3/");

            // Add creation date property to xmp metadata
            xmpMetaData.Add(Aspose.Pdf.Facades.DefaultMetadataProperties.CreateDate, DateTime.Now.ToString());

            // Add Metadata Date property to xmp metadata
            xmpMetaData.Add(Aspose.Pdf.Facades.DefaultMetadataProperties.MetadataDate, DateTime.Now.ToString());

            // Add Creator Tool property to xmp metadata
            xmpMetaData.Add(Aspose.Pdf.Facades.DefaultMetadataProperties.CreatorTool, "Creator Tool Name");

            // Add Modify Date to xmp metadata
            xmpMetaData.Add(Aspose.Pdf.Facades.DefaultMetadataProperties.ModifyDate, DateTime.Now.ToString());

            // Add Nick Name to xmp metadata
            xmpMetaData.Add(Aspose.Pdf.Facades.DefaultMetadataProperties.Nickname, "Test");

            // Save PDF document
            xmpMetaData.Save(output);
        }
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
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_TechnicalArticles();

    // Create an object of PdfXmpMetadata class
    var xmpMetaData = new Aspose.Pdf.Facades.PdfXmpMetadata();

    // Create input and output file streams
    using var input = new FileStream(dataDir + "FilledForm.pdf", FileMode.Open);

    using var output = new FileStream(dataDir + "xmp_out.pdf", FileMode.Create);

    // Bind PDF document
    xmpMetaData.BindPdf(input);

    // Add base URL property to xmp metadata
    xmpMetaData.Add(Aspose.Pdf.Facades.DefaultMetadataProperties.BaseURL, "xmlns:pdf=http:// Ns.adobe.com/pdf/1.3/");

    // Add creation date property to xmp metadata
    xmpMetaData.Add(Aspose.Pdf.Facades.DefaultMetadataProperties.CreateDate, DateTime.Now.ToString());

    // Add Metadata Date property to xmp metadata
    xmpMetaData.Add(Aspose.Pdf.Facades.DefaultMetadataProperties.MetadataDate, DateTime.Now.ToString());

    // Add Creator Tool property to xmp metadata
    xmpMetaData.Add(Aspose.Pdf.Facades.DefaultMetadataProperties.CreatorTool, "Creator Tool Name");

    // Add Modify Date to xmp metadata
    xmpMetaData.Add(Aspose.Pdf.Facades.DefaultMetadataProperties.ModifyDate, DateTime.Now.ToString());

    // Add Nick Name to xmp metadata
    xmpMetaData.Add(Aspose.Pdf.Facades.DefaultMetadataProperties.Nickname, "Test");

    // Save PDF document
    xmpMetaData.Save(output);
}
```
{{< /tab >}}
{{< /tabs >}}

## Conclusión

{{% alert color="primary" %}}
En este artículo, hemos visto cómo podemos trabajar con XMP utilizando Aspose.Pdf.Facades. La clase [PdfXmpMetadata](http://www.aspose.com/docs/display/pdfnet/PdfXmpMetadata+Class), utilizada en este artículo, facilita mucho al usuario la manipulación de metadatos en un documento PDF. Si se utiliza correctamente la clase [PdfXmpMetadata](http://www.aspose.com/docs/display/pdfnet/PdfXmpMetadata+Class), será muy fácil incorporar inteligencia en los archivos PDF, acercando un poco más la web semántica a la realización.
{{% /alert %}}