---
title: Convertir un XML a formato FDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /es/net/converting-an-xml-to-fdf-format/
description: Esta sección explica cómo puedes convertir un XML a formato FDF con FormDataConverter.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Converting an XML to FDF format",
    "alternativeHeadline": "Convert XML Files to FDF Format Easily",
    "abstract": "La función permite a los desarrolladores convertir sin problemas archivos XML a formato FDF utilizando la clase FormDataConverter en Aspose.PDF for .NET. Esta funcionalidad mejora el intercambio de datos entre formatos de documentos, facilitando la gestión eficiente de datos de formularios en aplicaciones.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "274",
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
    "url": "/net/converting-an-xml-to-fdf-format/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/converting-an-xml-to-fdf-format/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF puede realizar no solo tareas simples y fáciles, sino también afrontar objetivos más complejos. Consulta la siguiente sección para usuarios y desarrolladores avanzados."
}
</script>

{{% alert color="primary" %}}

El [Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) namespace en [Aspose.PDF for .NET](/pdf/net/) soporta muy bien AcroForms. También soporta la importación y exportación de datos de formularios a diferentes formatos de archivo como FDF, XFDF y XML. Sin embargo, a veces un desarrollador necesita convertir un formato a otro. En este artículo, analizaremos la función que nos permite convertir un formato FDF a XML.

{{% /alert %}}

## Detalles de implementación

FDF significa Formato de Datos de Formularios, y un archivo FDF contiene los valores del formulario en un par clave/valor. También sabemos que un archivo XML contiene los valores como etiquetas. Donde, principalmente la clave se representa como el nombre de la etiqueta y el valor se representa como el valor dentro de esa etiqueta. Ahora, [Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) proporciona la flexibilidad para convertir un formato de archivo XML en formato FDF.

Utiliza la clase [FormDataConverter](https://reference.aspose.com/pdf/net/aspose.pdf.facades/FormDataConverter) para este propósito. Esta clase proporciona diferentes métodos para convertir un formato de datos en otro. Este artículo muestra cómo usar un método, ConvertXmlToFdf(..), que toma un archivo FDF como entrada o flujo de origen y lo guarda en formato XML. El siguiente fragmento de código muestra cómo convertir un archivo FDF en un archivo XML.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
private static void ConvertXmlToFdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_TechnicalArticles();

    using (var src = new FileStream(dataDir + "log.xml", FileMode.Open, FileAccess.Read))
    {
        using (var dest = new FileStream(dataDir + "XMLToPdf_out.pdf", FileMode.Create, FileAccess.ReadWrite))
        {
            FormDataConverter.ConvertXmlToFdf(src, dest);
        }
    }
}
```