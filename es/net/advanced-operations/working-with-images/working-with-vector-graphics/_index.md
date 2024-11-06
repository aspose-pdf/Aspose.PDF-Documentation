---
title: Trabajando con Gráficos Vectoriales
linktitle: Trabajando con Gráficos Vectoriales
type: docs
weight: 120
url: es/net/working-with-vector-graphics/
description: Este artículo describe las características del uso de la herramienta GraphicsAbsorber utilizando C#.
lastmod: "2024-02-17"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Trabajando con GraphicsAbsorber",
    "alternativeHeadline": "Cómo obtener la posición de una imagen en un archivo PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "generación de documentos PDF",
    "keywords": "pdf, c#, GraphicsAbsorber en pdf",
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
    "url": "/net/working-with-vector-graphics/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/working-with-vector-graphics/"
    },
    "dateModified": "2022-02-04",
    "description": "Esta sección describe las características del trabajo con el archivo PDF GraphicsAbsorber utilizando la biblioteca C#."
}
</script>

En este capítulo, exploraremos cómo usar la poderosa clase `GraphicsAbsorber` para interactuar con gráficos vectoriales dentro de documentos PDF. Ya sea que necesites mover, eliminar o agregar gráficos, esta guía te mostrará cómo realizar estas tareas de manera efectiva. ¡Empecemos!

## Introducción<a name="introduction"></a>

Los gráficos vectoriales son un componente crucial de muchos documentos PDF, utilizados para representar imágenes, formas y otros elementos gráficos. Aspose.PDF proporciona la clase `GraphicsAbsorber`, que permite a los desarrolladores acceder y manipular programáticamente estos gráficos. Al usar el método `Visit` de `GraphicsAbsorber`, puedes extraer gráficos vectoriales de una página especificada y realizar varias operaciones, como moverlos, eliminarlos o copiarlos a otras páginas.

## 1. Extracción de gráficos con `GraphicsAbsorber`<a name="extracting-graphics"></a>

El primer paso para trabajar con gráficos vectoriales es extraerlos de un documento PDF. Aquí te mostramos cómo puedes hacerlo usando la clase `GraphicsAbsorber`:

```csharp
public static void UsingGraphicsAbsorber()
{
    // Paso 1: Crear un objeto Document.
    var document = new Document(@"C:\Samples\Sample-Document-01.pdf");

    // Paso 2: Crear una instancia de GraphicsAbsorber.
    var graphicsAbsorber = new GraphicsAbsorber();

    // Seleccionar la primera página del documento.
    var page = document.Pages[1];

    // Paso 3: Usar el método `Visit` para extraer gráficos de la página.
    graphicsAbsorber.Visit(page);

    // Mostrar información sobre los elementos extraídos.
    foreach (var element in graphicsAbsorber.Elements)
    {
        Console.WriteLine($"Número de página: {element.SourcePage.Number}");
        Console.WriteLine($"Posición: ({element.Position.X}, {element.Position.Y})");
        Console.WriteLine($"Número de operadores: {element.Operators.Count}");
    }
}
```
### Explicación:

1. **Crear un Objeto Documento**: Se instancia un nuevo objeto `Document` con la ruta al archivo PDF objetivo.
2. **Crear una Instancia de `GraphicsAbsorber`**: Esta clase captura todos los elementos gráficos de una página especificada.
3. **Método Visit**: El método `Visit` es llamado en la primera página, permitiendo que `GraphicsAbsorber` absorba los gráficos vectoriales.
4. **Iterar a través de los Elementos Extraídos**: El código itera a través de cada elemento extraído, imprimiendo información como el número de página, la posición y el número de operadores de dibujo involucrados.

## 2. Mover Gráficos<a name="moving-graphics"></a>

Una vez que has extraído los gráficos, puedes moverlos a una posición diferente en la misma página. Aquí te mostramos cómo puedes lograrlo:

```csharp
public static void MoveGraphics()
{
    var document = new Document(@"C:\Samples\Sample-Document-01.pdf");
    var graphicsAbsorber = new GraphicsAbsorber();
    var page = document.Pages[1];
    graphicsAbsorber.Visit(page);

    // Temporalmente suspende las actualizaciones para mejorar el rendimiento.
    graphicsAbsorber.SuppressUpdate();

    foreach (var element in graphicsAbsorber.Elements)
    {
        var position = element.Position;
        // Mueve los gráficos desplazando sus coordenadas X e Y.
        element.Position = new Point(position.X + 150, position.Y - 10);
    }

    // Reanuda las actualizaciones y aplica los cambios.
    graphicsAbsorber.ResumeUpdate();
    document.Save("test.pdf");
}
```
### Puntos Clave:

- **SuppressUpdate**: Este método suspende temporalmente las actualizaciones para mejorar el rendimiento cuando se realizan múltiples cambios.
- **ResumeUpdate**: Este método reanuda las actualizaciones y aplica los cambios realizados en las posiciones de los gráficos.
- **Posicionamiento de Elementos**: La posición de cada gráfico se ajusta cambiando sus coordenadas `X` y `Y`.

## 3. Eliminación de Gráficos<a name="removing-graphics"></a>

Existen escenarios en los que podrías querer eliminar gráficos específicos de una página. Aspose.PDF ofrece dos métodos para lograr esto:

### Método 1: Usando Límites Rectangulares

```csharp
public static void RemoveGraphicsMethod1()
{
    var document = new Document(@"C:\Samples\Sample-Document-01.pdf");
    var graphicsAbsorber = new GraphicsAbsorber();
    var page = document.Pages[1];
    graphicsAbsorber.Visit(page);
    var rectangle = new Rectangle(70, 248, 170, 252);

    graphicsAbsorber.SuppressUpdate();
    foreach (var element in graphicsAbsorber.Elements)
    {
        // Verificar si la posición del gráfico se encuentra dentro del rectángulo.
        if (rectangle.Contains(element.Position))
        {
            element.Remove(); // Eliminar el elemento gráfico.
        }
    }
    graphicsAbsorber.ResumeUpdate();
    document.Save("test.pdf");
}
```
### Método 2: Utilizando una Colección de Elementos Eliminados

```csharp
public static void RemoveGraphicsMethod2()
{
    var document = new Document(@"C:\Samples\Sample-Document-01.pdf");
    var graphicsAbsorber = new GraphicsAbsorber();
    var page = document.Pages[1];
    var rectangle = new Rectangle(70, 248, 170, 252);

    graphicsAbsorber.Visit(page);
    var removedElementsCollection = new GraphicElementCollection();
    foreach (var item in graphicsAbsorber.Elements.Where(el => rectangle.Contains(el.Position)))
    {
        removedElementsCollection.Add(item);
    }

    page.Contents.SuppressUpdate();
    page.DeleteGraphics(removedElementsCollection);
    page.Contents.ResumeUpdate();
    document.Save("test.pdf");
}
```

### Explicación:

- **Límites del Rectángulo**: Define una área rectangular para especificar qué gráficos eliminar.
- **Suprimir y Reanudar Actualizaciones**: Asegura la eliminación eficiente sin renderización intermedia.

## 4. Añadiendo Gráficos a Otra Página<a name="adding-graphics"></a>

Los gráficos absorbidos de una página pueden ser añadidos a otra página dentro del mismo documento.
Los gráficos absorbidos de una página pueden ser añadidos a otra página dentro del mismo documento.

### Método 1: Añadiendo Gráficos Individualmente

```csharp
public static void AddToAnotherPageMethod1()
{
    var document = new Document(@"C:\Samples\Sample-Document-01.pdf");
    var graphicsAbsorber = new GraphicsAbsorber();
    var page1 = document.Pages[1];
    var page2 = document.Pages[2];

    graphicsAbsorber.Visit(page1);
    page2.Contents.SuppressUpdate();
    foreach (var element in graphicsAbsorber.Elements)
    {
        element.AddOnPage(page2); // Añadir cada elemento gráfico a la segunda página.
    }
    page2.Contents.ResumeUpdate();
    document.Save("test.pdf");
}
```

### Método 2: Añadiendo Gráficos como una Colección

```csharp
public static void AddToAnotherPageMethod2()
{
    var document = new Document(@"C:\Samples\Sample-Document-01.pdf");
    var graphicsAbsorber = new GraphicsAbsorber();
    var page1 = document.Pages[1];
    var page2 = document.Pages[2];

    graphicsAbsorber.Visit(page1);
    page2.Contents.SuppressUpdate();
    page2.AddGraphics(graphicsAbsorber.Elements); // Añadir todos los gráficos de una sola vez.
    page2.Contents.ResumeUpdate();
    document.Save("test.pdf");
}
```
### Puntos clave:

- **SuppressUpdate y ResumeUpdate**: Estos métodos ayudan a mantener el rendimiento mientras se realizan cambios en masa.
- **AddOnPage vs. AddGraphics**: Usa `AddOnPage` para adiciones individuales y `AddGraphics` para adiciones en masa.

## Conclusión

En este capítulo, exploramos cómo usar la clase `GraphicsAbsorber` para extraer, mover, eliminar y añadir gráficos vectoriales dentro de documentos PDF utilizando Aspose.PDF. Al dominar estas técnicas, puedes mejorar significativamente la presentación visual de tus PDFs y crear documentos dinámicos y visualmente atractivos.

Siéntete libre de experimentar con los ejemplos de código y adaptarlos a tus casos de uso específicos. ¡Feliz programación!

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for .NET Library",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
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
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "PDF Manipulation Library for .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/net/create-pdf-document/screenshot.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>


