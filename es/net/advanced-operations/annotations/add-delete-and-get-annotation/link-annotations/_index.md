---
title: Usando Anotaciones de Enlace en PDF
linktitle: Anotaciones de Enlace
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 70
url: /es/net/link-annotations/
description: Aspose.PDF for .NET te permite Agregar, Obtener y Eliminar Anotaciones de Enlace de tu documento PDF.
lastmod: "2024-07-28"
sitemap:
    changefreq: "monthly"
    priority: 0.5
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Using Link Annotation for PDF",
    "alternativeHeadline": "How to add Link Annotation in PDF",
    "abstract": "Aspose.PDF for .NET introduce capacidades robustas para gestionar anotaciones de enlace dentro de documentos PDF, permitiendo a los usuarios agregar, recuperar y eliminar hipervínculos sin problemas. Esta función mejora la interactividad del documento al permitir que los enlaces abran páginas específicas, archivos externos o URLs web, todo personalizable con varios estilos y acciones. Desbloquea nuevas posibilidades para la navegación en PDF y el compromiso del usuario con esta poderosa funcionalidad de anotación.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "pdf, c#, text annotation",
    "wordcount": "302",
    "proficiencyLevel": "Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF Doc Team",
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
    "url": "/net/link-annotation/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/link-annotation/"
    },
    "dateModified": "2022-02-04",
    "description": "Aspose.PDF for .NET te permite Agregar, Obtener y Eliminar Anotación de Texto de tu documento PDF."
}
</script>

## Agregando Anotación de Enlace en un archivo PDF existente

> El siguiente fragmento de código también funciona con la biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

Una [Anotación de Enlace](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/linkannotation) representa un hipervínculo, un destino en otro lugar y un documento. Según el Estándar PDF, la anotación de enlace se puede utilizar en tres casos: vista de página abierta, abrir archivo y abrir página web.

### Usando Anotación de Enlace para abrir vista de página

Se realizaron varios pasos adicionales para crear la anotación. Usamos 2 TextFragmentAbsorbers para encontrar fragmentos para la demostración. El primero es para el texto de la anotación de enlace, y el segundo indica algunos lugares en el documento.

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddLinkAnnotation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "Link Annotation Demo.pdf"))
    {
        // Get first page
        var page = document.Pages[1];

        // Define regular expressions for text fragments
        var regEx1 = new Regex(@"Link Annotation Demo \d");
        var regEx2 = new Regex(@"Sample text \d");

        // Create TextFragmentAbsorber for the first regular expression
        var textFragmentAbsorber1 = new Aspose.Pdf.Text.TextFragmentAbsorber(regEx1);
        textFragmentAbsorber1.Visit(document);

        // Create TextFragmentAbsorber for the second regular expression
        var textFragmentAbsorber2 = new Aspose.Pdf.Text.TextFragmentAbsorber(regEx2);
        textFragmentAbsorber2.Visit(document);

        // Get the text fragments for both absorbers
        var linkFragments = textFragmentAbsorber1.TextFragments;
        var sampleTextFragments = textFragmentAbsorber2.TextFragments;

        // Create a LinkAnnotation
        var linkAnnotation1 = new Aspose.Pdf.Annotations.LinkAnnotation(page, linkFragments[1].Rectangle)
        {
            Action = new Aspose.Pdf.Annotations.GoToAction(
                new Aspose.Pdf.Annotations.XYZExplicitDestination(
                    sampleTextFragments[1].Page,
                    sampleTextFragments[1].Rectangle.LLX,
                    sampleTextFragments[1].Rectangle.URX, 1.5))
        };

        // Add the link annotation to the page
        page.Annotations.Add(linkAnnotation1);

        // Save PDF document
        document.Save(dataDir + "AddLinkAnnotation_out.pdf");
    }
}
```

Para crear la anotación hemos seguido ciertos pasos:

1. Crear `LinkAnnotation` y pasar el objeto de página y el rectángulo del fragmento de texto que corresponde con la anotación.
1. Establecer `Action` como `GoToAction` y pasar `XYZExplicitDestination` como destino deseado. Creamos `XYZExplicitDestination` basado en la página, las coordenadas izquierda y superior y el zoom.
1. Agregar la anotación a la colección de anotaciones de la página.
1. Guardar el documento.

### Usando Anotación de Enlace con destino nombrado

Al procesar varios documentos, surge una situación en la que estás escribiendo y no sabes a dónde apuntará la anotación. En este caso, puedes usar un destino especial (nombrado) y el código se verá así:

```cs
var destinationName = "Link2";
var linkAnnotation2 = new LinkAnnotation(page, linkFragments[2].Rectangle)
{
    Action = new GoToAction(document, destinationName)
};
```

En otro lugar puedes crear un Destino Nombrado.

```cs
document.NamedDestinations.Add(destinationName,
    new XYZExplicitDestination(
        sampleTextFragments[2].Page,
        sampleTextFragments[2].Rectangle.LLX,
        sampleTextFragments[2].Rectangle.URX, 1));
```

### Usando Anotación de Enlace para abrir archivo

El mismo enfoque se utiliza al crear una anotación para abrir un archivo, como en los ejemplos anteriores.

```cs
var linkAnnotation3 = new LinkAnnotation(page, linkFragments[3].Rectangle)
{
    Action = new GoToRemoteAction("another.pdf", 2)
};
```

La diferencia es que usaremos `GoToRemoteAction` en lugar de `GoToAction`. El constructor de GoToRemoteAction recibe dos parámetros: nombre del archivo y número de página. También puedes usar otra forma y pasar el nombre del archivo y algún destino. Obviamente, necesitas crear tal destino antes de usarlo.

### Usando Anotación de Enlace para abrir página web

Para abrir una página web, simplemente establece `Action` con el objeto `GoToURIAction`. Puedes pasar un hipervínculo como parámetro del constructor o cualquier otro tipo de URI. Por ejemplo, puedes usar `callto` para implementar una acción con un número de teléfono.

```cs
var linkAnnotation4 = new LinkAnnotation(page, linkFragments[4].Rectangle)
{
    Action = new GoToURIAction("https://products.aspose.com/pdf/net"),
    // Create Link Annotation and set the action to call a phone number
    //Action = new GoToURIAction("callto:678-555-0103")
    Color = Color.Blue
};
```

## Agregando Anotación de Enlace decorada

Puedes personalizar la Anotación de Enlace usando bordes. En el ejemplo a continuación, crearemos un borde azul punteado de 3pt de ancho.

```cs
var linkAnnotation4 = new LinkAnnotation(page, linkFragments[4].Rectangle)
{
    Action = new GoToURIAction("https://products.aspose.com/pdf/net"),    
    Color = Color.Blue
};

linkAnnotation4.Border = new Border(linkAnnotation4)
{
    Style = BorderStyle.Dashed,
    Dash = new Dash(5, 5),
    Width = 3
};
```

Otro ejemplo muestra cómo simular el estilo del navegador y usar Subrayado para los enlaces.

```cs
var linkAnnotation5 = new LinkAnnotation(page, linkFragments[5].Rectangle)
{
    Color = Color.Blue
};
linkAnnotation5.Border = new Border(linkAnnotation5)
{
    Style = BorderStyle.Underline,
    Width = 3
};
```

### Obtener Anotaciones de Enlace

Por favor, intenta usar el siguiente fragmento de código para Obtener Anotaciones de Enlace del documento PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetLinkAnnotations()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SimpleResume_mod.pdf"))
    {
        // Get all Link annotations from the first page
        var linkAnnotations = document.Pages[1].Annotations.Where(a => a.AnnotationType == Aspose.Pdf.Annotations.AnnotationType.Link);

        // Iterate through each Link annotation
        foreach (Aspose.Pdf.Annotations.Annotation annot in linkAnnotations)
        {
            // Print the URL of each Link Annotation
            Console.WriteLine("URI: " + ((annot as Aspose.Pdf.Annotations.LinkAnnotation).Action as Aspose.Pdf.Annotations.GoToURIAction).URI);

            // Create a TextAbsorber to extract text within the annotation's rectangle
            var absorber = new Aspose.Pdf.Text.TextAbsorber();
            absorber.TextSearchOptions.LimitToPageBounds = true;
            absorber.TextSearchOptions.Rectangle = annot.Rect;

            // Accept the absorber for the first page
            document.Pages[1].Accept(absorber);

            // Extract and print the text associated with the hyperlink
            string extractedText = absorber.Text;
            Console.WriteLine(extractedText);
        }
    }
}
```

### Eliminar Anotaciones de Enlace

El siguiente fragmento de código muestra cómo Eliminar una Anotación de Enlace de un archivo PDF. Para esto, necesitamos encontrar y eliminar todas las anotaciones de enlace en la primera página. Después de esto, guardaremos el documento con la anotación eliminada.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DeleteLinkAnnotations()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SimpleResume_mod.pdf"))
    {
        // Find and delete all link annotations on the 1st page
        var linkAnnotations = document.Pages[1].Annotations.Where(a => a.AnnotationType == Aspose.Pdf.Annotations.AnnotationType.Link);

        foreach (var la in linkAnnotations)
        {
            document.Pages[1].Annotations.Delete(la);
        }

        // Save PDF document
        document.Save(dataDir + "DeleteLinkAnnotations_out.pdf");
    }
}
```