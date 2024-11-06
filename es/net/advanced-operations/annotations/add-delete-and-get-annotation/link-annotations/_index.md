---
title: Uso de Anotaciones de Enlace en PDF
linktitle: Anotaciones de Enlace
type: docs
weight: 70
url: es/net/link-annotations/
description: Aspose.PDF para .NET te permite Agregar, Obtener y Eliminar Anotación de Enlace de tu documento PDF.
lastmod: "2024-07-28"
sitemap:
    changefreq: "monthly"
    priority: 0.5
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Uso de Anotación de Enlace para PDF",
    "alternativeHeadline": "Cómo agregar Anotación de Enlace en PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "generación de documentos pdf",
    "keywords": "pdf, c#, anotación de texto",
    "wordcount": "302",
    "proficiencyLevel":"Principiante",
    "publisher": {
        "@type": "Organization",
        "name": "Equipo de Documentación de Aspose.PDF",
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
                "contactType": "ventas",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "ventas",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "ventas",
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
    "description": "Aspose.PDF para .NET te permite Agregar, Obtener y Eliminar Anotación de Texto de tu documento PDF."
}
</script>

## Agregando anotación de enlace en un archivo PDF existente

> El siguiente fragmento de código también funciona con la biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

Una [Anotación de Enlace](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/linkannotation) representa un hipervínculo, un destino en otro lugar y un documento. Según el Estándar PDF, la anotación de enlace se puede utilizar en tres casos: abrir vista de página, abrir archivo y abrir página web.

### Usando la anotación de enlace para abrir la vista de página

Se realizaron varios pasos adicionales para crear la anotación. Usamos 2 TextFragmentAbsorbers para encontrar fragmentos para demostrar. El primero es para el texto de la anotación de enlace, y el segundo indica algunos lugares en el documento.

```cs
Document document = new Document(System.IO.Path.Combine(_dataDir, "Link Annotation Demo.pdf"));

var page = document.Pages[1];

var regEx = new Regex(@"Link Annotation Demo \d");
TextFragmentAbsorber textFragmentAbsorber1 = new TextFragmentAbsorber(regEx);
textFragmentAbsorber1.Visit(document);

regEx = new Regex(@"Sample text \d");
TextFragmentAbsorber textFragmentAbsorber2 = new TextFragmentAbsorber(regEx);
textFragmentAbsorber2.Visit(document);

var linkFragments = textFragmentAbsorber1.TextFragments;
var sampleTextFragments = textFragmentAbsorber2.TextFragments;

var linkAnnotation1 = new LinkAnnotation(page, linkFragments[1].Rectangle)
{
    Action = new GoToAction(
        new XYZExplicitDestination(
            sampleTextFragments[1].Page,
            sampleTextFragments[1].Rectangle.LLX,
            sampleTextFragments[1].Rectangle.URX, 1.5))
};

page.Annotations.Add(linkAnnotation1);

document.Save("test.pdf");
```
Para crear la anotación hemos seguido ciertos pasos:

1. Crear `LinkAnnotation` y pasar el objeto de página y el rectángulo del fragmento de texto que corresponde con la anotación.
1. Establecer `Action` como `GoToAction` y pasar `XYZExplicitDestination` como destino deseado. Creamos `XYZExplicitDestination` en base a la página, las coordenadas izquierdas y superiores y el zoom.
1. Añadir la anotación a la colección de anotaciones de página.
1. Guardar el documento

### Usando Link Annotation con destino nombrado

Cuando se procesan varios documentos, surge una situación en la que estás escribiendo y no sabes a dónde apuntará la anotación.
En este caso puedes usar un destino especial (nombrado) y el código se verá como aquí:

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
### Uso de anotación de enlace para abrir archivo

Se utiliza el mismo enfoque al crear una anotación para abrir un archivo, como en los ejemplos anteriores.

```cs
var linkAnnotation3 = new LinkAnnotation(page, linkFragments[3].Rectangle)
{
    Action = new GoToRemoteAction("another.pdf", 2)
};
```

La diferencia es que usaremos `GoToRemoteAction` en lugar de `GoToAction`. El constructor de GoToRemoteAction recibe dos parámetros: nombre del archivo y número de página.
También puedes usar otra forma y pasar el nombre del archivo y algún destino. Obviamente, necesitas crear tal destino antes de usarlo.

### Uso de anotación de enlace para abrir página web

Para abrir una página web solo establece `Action` con el objeto `GoToURIAction`.
Puedes pasar un hipervínculo como parámetro del constructor o cualquier otro tipo de URI. Por ejemplo, puedes usar `callto` para implementar una acción con llamada a número telefónico.

```cs
var linkAnnotation4 = new LinkAnnotation(page, linkFragments[4].Rectangle)
{
    Action = new GoToURIAction("https://products.aspose.com/pdf/net"),
    // Crear anotación de enlace y establecer la acción para llamar a un número telefónico
    //Action = new GoToURIAction("callto:678-555-0103")
    Color = Color.Blue
};
```
## Añadiendo Anotación de Enlace Decorado

Puedes personalizar la Anotación de Enlace usando bordes. En el ejemplo a continuación, crearemos un borde azul punteado con un ancho de 3pt.

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

Otro ejemplo muestra cómo simular el estilo de navegador y usar Subrayado para enlaces.

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

Por favor intenta usar el siguiente fragmento de código para Obtener Anotaciones de Enlace de un documento PDF.

```csharp
class ExampleLinkAnnotations
{
    // La ruta al directorio de documentos.
    private const string _dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();
    public static void GetLinkAnnotations()
    {
        // Cargar el archivo PDF
        Document document = new Document(System.IO.Path.Combine(_dataDir, "SimpleResume_mod.pdf"));
        var linkAnnotations = document.Pages[1].Annotations.Where(a => a.AnnotationType == AnnotationType.Link);
        foreach (Aspose.Pdf.Annotations.Annotation annot in linkAnnotations)
        {
            // Imprimir la URL de cada Anotación de Enlace
            Console.WriteLine("URI: " + ((annot as LinkAnnotation).Action as GoToURIAction).URI);
            TextAbsorber absorber = new TextAbsorber();
            absorber.TextSearchOptions.LimitToPageBounds = true;
            absorber.TextSearchOptions.Rectangle = annot.Rect;
            document.Pages[1].Accept(absorber);
            string extractedText = absorber.Text;
            // Imprimir el texto asociado con el hipervínculo
            Console.WriteLine(extractedText);
        }
    }
}
```

### Eliminar Anotaciones de Enlace

El siguiente fragmento de código muestra cómo eliminar una Anotación de Enlace de un archivo PDF. Para esto necesitamos encontrar y eliminar todas las anotaciones de enlace en la 1ª página. Después de esto, guardaremos el documento con la anotación eliminada.

```csharp
class ExampleLinkAnnotations
{
    // La ruta al directorio de documentos.
    private const string _dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();
    public static void DeleteLinkAnnotations()
    {
        // Cargar el archivo PDF
        Document document = new Document(System.IO.Path.Combine(_dataDir, "SimpleResume_mod.pdf"));
        // Encontrar y eliminar todas las anotaciones de enlace en la 1ª página
        var linkAnnotations = document.Pages[1].Annotations.Where(a => a.AnnotationType == AnnotationType.Link);

        foreach (var la in linkAnnotations)
            document.Pages[1].Annotations.Delete(la);
        // Guardar el documento con la anotación eliminada
        document.Save(System.IO.Path.Combine(_dataDir, "SimpleResume_del.pdf"));
    }
}
```
