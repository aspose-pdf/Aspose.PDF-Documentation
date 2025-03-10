---
title: Convertir un FDF a formato XML
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /es/net/converting-an-fdf-to-xml-format/
description: Esta sección explica cómo puedes convertir un FDF a formato XML con la clase FormDataConverter.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Converting an FDF to XML format",
    "alternativeHeadline": "Convert FDF Files to XML Easily",
    "abstract": "Descubre cómo convertir eficientemente archivos FDF a formato XML utilizando la clase FormDataConverter en Aspose.PDF for .NET. Esta funcionalidad optimiza el manejo de datos al transformar pares clave/valor de FDF en una estructura XML fácilmente legible, mejorando la interoperabilidad y la gestión de datos en tus aplicaciones.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "288",
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
    "url": "/net/converting-an-fdf-to-xml-format/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/converting-an-fdf-to-xml-format/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF puede realizar no solo tareas simples y fáciles, sino también afrontar objetivos más complejos. Consulta la siguiente sección para usuarios y desarrolladores avanzados."
}
</script>

{{% alert color="primary" %}}

El [Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) namespace en [Aspose.PDF for .NET](/pdf/es/net/) soporta muy bien AcroForms. También soporta la importación y exportación de datos de formularios a diferentes formatos de archivo como FDF, XFDF y XML. Sin embargo, a veces los desarrolladores pueden necesitar convertir un formato en otro. Este artículo analiza la función que convierte FDF en XML.

{{% /alert %}}

## Detalles de implementación

FDF significa Formato de Datos de Formularios, y un archivo FDF contiene los valores del formulario en un par clave/valor. También sabemos que un archivo XML contiene los valores como etiquetas. Donde, principalmente la clave se representa como el nombre de la etiqueta y el valor se representa como el valor dentro de esa etiqueta. Ahora, [Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) nos proporciona la flexibilidad para convertir un formato de archivo FDF en un formato XML.

Podemos usar la clase [FormDataConverter](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formdataconverter) para este propósito. Esta clase nos proporciona diferentes métodos para convertir un formato de datos en otro formato. En este artículo, solo utilizaremos un método llamado [ConvertFdfToXml](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formdataconverter/methods/convertfdftoxml). Este método toma un archivo FDF como entrada o flujo de origen y lo guarda en formato XML.

El siguiente fragmento de código te muestra cómo convertir un archivo FDF en un archivo XML:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
private static void ConvertFdftoXml()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_TechnicalArticles();

    // Create a file stream for FDF file - input file
    using (var fdfInputStream = new FileStream(dataDir + "input.fdf", FileMode.Open))
    {
        // Create a file stream for XML file - output file
        using (var xmlOutputStream = new FileStream(dataDir + "ConvertFdfToXML_out.xml", FileMode.Create))
        {
            FormDataConverter.ConvertFdfToXml(fdfInputStream, xmlOutputStream);
        }
    }
}
```