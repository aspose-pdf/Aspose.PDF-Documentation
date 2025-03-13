---
title: Verificar límites de forma en la colección de Shapes
type: docs
weight: 70
url: /es/net/aspose-pdf-drawing-graph-shapes-bounds-check/
description: Aprenda cómo verificar los límites de una forma cuando se inserta en la colección de Shapes para asegurarse de que se ajuste dentro de su contenedor padre.
lastmod: "2025-02-28"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Checking Element Bounds in Shapes Collection",
    "alternativeHeadline": "Configurable Bounds Checking for Aspose.PDF Shapes with Exception Mode",
    "abstract": "La nueva función de verificación de límites de Aspose.PDF for .NET en la colección `Drawing.Graph.Shapes` valida automáticamente las dimensiones de los elementos contra los contenedores padres, evitando el desbordamiento del diseño. Se activan excepciones cuando los elementos exceden los límites del contenedor, aplicando restricciones de tamaño estrictas durante la inserción para garantizar un formato PDF preciso y optimizar la precisión del diseño.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1000",
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
    "url": "/net/aspose-pdf-drawing-graph-shapes-bounds-check/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/aspose-pdf-drawing-graph-shapes-bounds-check/"
    },
    "dateModified": "2025-02-28",
    "description": ""
}
</script>

## Introducción
Este documento proporciona una guía detallada sobre el uso de la función de verificación de límites en la colección de Shapes. Esta función asegura que los elementos se ajusten dentro de su contenedor padre y se puede configurar para lanzar una excepción si el componente no se ajusta. Vamos a repasar los pasos para implementar esta funcionalidad y proporcionar un ejemplo completo.

## Requisitos previos
Necesitará lo siguiente:
* Visual Studio 2019 o posterior
* Aspose.PDF for .NET 25.3 o posterior
* Un archivo PDF de muestra que contenga algunas páginas

Puede descargar la biblioteca Aspose.PDF for .NET desde el sitio web oficial o instalarla utilizando el Administrador de paquetes NuGet en Visual Studio.

## Pasos
Aquí están los pasos para completar la tarea:
1. Crear un nuevo documento y agregar una página.
2. Crear un objeto `Graph` con dimensiones especificadas.
3. Crear un objeto `Shape` con dimensiones especificadas.
4. Establecer el `BoundsCheckMode` en `ThrowExceptionIfDoesNotFit`.
5. Intentar agregar la forma al gráfico.

Veamos cómo implementar estos pasos en código C#.

### Paso 1: Crear un nuevo documento y agregar una página
Primero, cree un nuevo documento PDF y agregue una página a él.

```csharp
using (var doc = new Aspose.Pdf.Document())
{
    Aspose.Pdf.Page page = doc.Pages.Add();
}
```

### Paso 2: Crear un objeto Graph con dimensiones especificadas
A continuación, cree un objeto `Graph` con un ancho y alto de 100 unidades. Posicione el gráfico a 10 unidades desde la parte superior y 15 unidades desde la izquierda de la página. Agregue un borde negro al gráfico.

```csharp
var graph = new Aspose.Pdf.Drawing.Graph(100d, 100d)
{
    Top = 10,
    Left = 15,
    Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.Box, 1F, Aspose.Pdf.Color.Black)
};
page.Paragraphs.Add(graph);
```

### Paso 3: Crear un objeto Aspose.Pdf.Drawing.Shape (por ejemplo, Aspose.Pdf.Drawing.Rectangle) con dimensiones especificadas
Cree un objeto Rectangle con un ancho y alto de 50 unidades. Posicione el rectángulo en (-1, 0), que está fuera de los límites del gráfico.

```csharp
Aspose.Pdf.Drawing.Rectangle rect = new Aspose.Pdf.Drawing.Rectangle(-1, 0, 50, 50)
{
    GraphInfo =
    {
        FillColor = Aspose.Pdf.Color.Tomato
    }
};
```

### Paso 4: Establecer el BoundsCheckMode en ThrowExceptionIfDoesNotFit
Establezca el `BoundsCheckMode` en `ThrowExceptionIfDoesNotFit` para asegurarse de que se lance una excepción si el rectángulo no se ajusta dentro del gráfico.

```csharp
graph.Shapes.UpdateBoundsCheckMode(Aspose.Pdf.BoundsCheckMode.ThrowExceptionIfDoesNotFit);
```

### Paso 5: Intentar agregar el rectángulo al gráfico
Intente agregar el rectángulo al gráfico. Esto lanzará una `Aspose.Pdf.BoundsOutOfRangeException` porque el rectángulo no se ajusta dentro de las dimensiones del gráfico.

```csharp
graph.Shapes.Add(rect);
```

## Salida
Después de ejecutar el código, la salida esperada será una `Aspose.Pdf.BoundsOutOfRangeException` con el mensaje:

```
Bounds not fit. Container dimensions: 100x100
```

## Solución de problemas
En caso de problemas, aquí hay algunos consejos:
* Asegúrese de que el `BoundsCheckMode` esté configurado correctamente.
* Verifique que las dimensiones del elemento y del contenedor sean precisas.
* Verifique la posición del elemento dentro del contenedor.

## Ejemplo completo
A continuación se muestra un ejemplo completo que demuestra todos los pasos combinados:

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CheckShapeBounds()
{
    // Create a new document and add a page
    using (var doc = new Aspose.Pdf.Document())
    {
        Aspose.Pdf.Page page = doc.Pages.Add();
        
        // Create a Graph Object with Specified Dimensions
        var graph = new Aspose.Pdf.Drawing.Graph(100d, 100d)
        {
            Top = 10,
            Left = 15,
            Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.Box, 1F, Aspose.Pdf.Color.Black)
        };
        page.Paragraphs.Add(graph);
        
        // Create a Aspose.Pdf.Drawing.Shape object (for example, Aspose.Pdf.Drawing.Rectangle) with specified dimensions
        Aspose.Pdf.Drawing.Rectangle rect = new Aspose.Pdf.Drawing.Rectangle(-1, 0, 50, 50)
        {
            GraphInfo =
            {
                FillColor = Aspose.Pdf.Color.Tomato
            }
        };
        
        // Set the BoundsCheckMode to ThrowExceptionIfDoesNotFit
        graph.Shapes.UpdateBoundsCheckMode(Aspose.Pdf.BoundsCheckMode.ThrowExceptionIfDoesNotFit);
        
        // Attempt to add the rectangle to the graph
        graph.Shapes.Add(rect);
    }
}```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CheckShapeBounds()
{
    // Create a new document and add a page
    using var doc = new Aspose.Pdf.Document();
    Aspose.Pdf.Page page = doc.Pages.Add();

    // Create a Graph Object with Specified Dimensions
    var graph = new Aspose.Pdf.Drawing.Graph(100d, 100d)
    {
        Top = 10,
        Left = 15,
        Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.Box, 1F, Aspose.Pdf.Color.Black)
    };
    page.Paragraphs.Add(graph);

    // Create a Aspose.Pdf.Drawing.Shape object (for example, Aspose.Pdf.Drawing.Rectangle) with specified dimensions
    Aspose.Pdf.Drawing.Rectangle rect = new Aspose.Pdf.Drawing.Rectangle(-1, 0, 50, 50)
    {
        GraphInfo =
        {
            FillColor = Aspose.Pdf.Color.Tomato
        }
    };

    // Set the BoundsCheckMode to ThrowExceptionIfDoesNotFit
    graph.Shapes.UpdateBoundsCheckMode(Aspose.Pdf.BoundsCheckMode.ThrowExceptionIfDoesNotFit);

    // Attempt to add the rectangle to the graph
    graph.Shapes.Add(rect);
}
```
{{< /tab >}}
{{< /tabs >}}

## Conclusión
La función de verificación de límites en la colección de Shapes es una herramienta poderosa para garantizar que los elementos se ajusten dentro de los contenedores padres. Puede prevenir problemas de diseño en sus documentos PDF configurando el BoundsCheckMode en ThrowExceptionIfDoesNotFit. Esta función es particularmente útil en escenarios donde la posición y el tamaño precisos de los elementos son críticos. Para más detalles, visite la [documentación oficial](https://docs.aspose.com/pdf/net/).