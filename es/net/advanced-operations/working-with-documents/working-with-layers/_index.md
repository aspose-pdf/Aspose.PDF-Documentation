---
title: Trabajar con capas PDF usando C#
linktitle: Trabajar con capas PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 50
url: /es/net/work-with-pdf-layers/
description: La siguiente tarea explica cómo bloquear una capa PDF, extraer elementos de la capa PDF, aplanar un PDF con capas y fusionar todas las capas dentro de un PDF en una sola.
lastmod: "2024-09-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Work with PDF layers using C#",
    "alternativeHeadline": "Manage PDF layers effortlessly with C#",
    "abstract": "Experimenta una gestión mejorada de documentos PDF con la nueva función Aspose.PDF for .NET que permite a los usuarios trabajar eficazmente con capas PDF. Esta funcionalidad permite bloquear y desbloquear capas, extraer elementos en archivos separados, aplanar contenido en capas y fusionar múltiples capas en una, proporcionando un mayor control sobre la visibilidad y organización del documento. Desbloquea el potencial de tus documentos PDF y optimiza tus flujos de trabajo con estas poderosas herramientas",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "PDF layers, lock PDF layer, extract PDF layer elements, flatten layered PDF, merge PDF layers, Aspose.PDF for .NET, layer.Lock(), layer.Flatten(), layer.Save()",
    "wordcount": "501",
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
    "url": "/net/work-with-pdf-layers/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/work-with-pdf-layers/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF puede realizar no solo tareas simples y fáciles, sino también afrontar objetivos más complejos. Consulta la siguiente sección para usuarios y desarrolladores avanzados."
}
</script>

Las capas PDF permiten que un documento PDF contenga diferentes conjuntos de contenido que pueden ser visualizados o ocultados selectivamente. Cada capa en un PDF puede incluir texto, imágenes o gráficos, y los usuarios pueden activar o desactivar estas capas, dependiendo de sus necesidades. Las capas se utilizan a menudo en documentos complejos donde diferentes contenidos necesitan ser organizados o separados.

## Bloquear una capa PDF

Con Aspose.PDF for .NET puedes abrir un PDF, bloquear una capa específica en la primera página y guardar el documento con los cambios.

Desde la versión 24.5, esta función ha sido implementada.

Se han añadido dos nuevos métodos y una propiedad:

- Layer.Lock(); - Bloquea la capa.
- Layer.Unlock(); - Desbloquea la capa.
- Layer.Locked; - Propiedad que indica el estado de bloqueo de la capa.

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void LockLayerInPDF()
{
	// The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Layers();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Get the first page and the first layer
        var page = document.Pages[1];
        var layer = page.Layers[0];

        // Lock the layer
        layer.Lock();

        // Save PDF document
        document.Save(dataDir + "LockLayerInPDF_out.pdf");
    }
}
```

## Extraer elementos de la capa PDF

La biblioteca Aspose.PDF for .NET permite extraer cada capa de la primera página y guardar cada capa en un archivo separado.

Para crear un nuevo PDF a partir de una capa, se puede utilizar el siguiente fragmento de código:

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SaveLayersFromPdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Get layers from the first page
        var layers = document.Pages[1].Layers;

        // Save each layer to the output path
        foreach (var layer in layers)
        {
            layer.Save(dataDir + "Layers_out.pdf");
        }
    }
}
```

La versión 24.9 ha resultado en una actualización de esta función.

Es posible extraer elementos de la capa PDF y guardarlos en un nuevo flujo de archivo PDF:

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SaveLayersToOutputStream(Stream outputStream)
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();
	
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Get layers from the first page
        var layers = document.Pages[1].Layers;

        // Save each layer to the output stream
        foreach (var layer in layers)
        {
            layer.Save(outputStream);
        }
    }
}
```

## Aplanar un PDF con capas

La biblioteca Aspose.PDF for .NET abre un PDF, itera a través de cada capa en la primera página y aplana cada capa, haciéndola permanente en la página.

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void FlattenLayersInPdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Get the first page
        var page = document.Pages[1];

        // Flatten each layer on the page
        foreach (var layer in page.Layers)
        {
            layer.Flatten(true);
        }
    }
}
```

El método 'Layer.Flatten(bool cleanupContentStream)' acepta el parámetro booleano que especifica si se deben eliminar los marcadores de grupo de contenido opcional del flujo de contenido. Configurar el parámetro cleanupContentStream en falso acelera el proceso de aplanamiento.

## Fusionar todas las capas dentro del PDF en una

La biblioteca Aspose.PDF for .NET permite fusionar todas las capas PDF o una capa específica en la primera página en una nueva capa y guardar el documento actualizado.

Se han añadido dos métodos para fusionar todas las capas en la página:

- void MergeLayers(string newLayerName).
- void MergeLayers(string newLayerName, string newOptionalContentGroupId).

El segundo parámetro permite renombrar el marcador de grupo de contenido opcional. El valor predeterminado es "oc1" (/OC /oc1 BDC).

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MergeLayersInPdf(string newLayerName, string optionalLayerName = null)
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Get the first page
        var page = document.Pages[1];

        // Merge layers with a new layer name
        if (optionalLayerName != null)
        {
            page.MergeLayers(newLayerName, optionalLayerName);
        }
        else
        {
            page.MergeLayers(newLayerName);
        }

        // Save PDF document
        document.Save(dataDir + "MergeLayersInPdf_out.pdf");
    }
}
```