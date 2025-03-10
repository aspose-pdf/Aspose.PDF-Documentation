---
title: Agregar Anotaciones de Figuras usando C#
linktitle: Anotaciones de Figuras
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 30
url: /es/net/figures-annotation/
description: Este artículo describe cómo agregar, obtener y eliminar anotaciones de figuras de su documento PDF con Aspose.PDF for .NET
lastmod: "2023-09-12"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Add Figures Annotations using C#",
    "alternativeHeadline": "Enhance PDF Documents with Comprehensive Figure Annotations",
    "abstract": "Presentamos la nueva función de Anotaciones de Figuras en Aspose.PDF for .NET, que permite a los usuarios agregar, recuperar y eliminar sin problemas varios tipos de anotaciones, incluidas líneas, cuadrados, círculos, polígonos y polilíneas en documentos PDF. Esta funcionalidad mejora la interactividad del documento, permitiendo una comunicación más clara y un marcado visual directamente dentro de los archivos PDF. Optimice sus tareas de edición de PDF con este robusto conjunto de herramientas de anotación diseñado para desarrolladores que utilizan C#",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "pdf, figures annotations, line annotation, square annotation, circle annotation, polygon annotation, polyline annotation, free text annotation, ink annotation, Aspose.PDF for .NET",
    "wordcount": "2125",
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
    "url": "/net/figures-annotation/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/figures-annotation/"
    },
    "dateModified": "2024-11-25",
    "description": "Este artículo describe cómo agregar, obtener y eliminar anotaciones de figuras de su documento PDF con Aspose.PDF for .NET"
}
</script>

La aplicación de gestión de documentos PDF proporciona varias herramientas para anotar documentos. Desde la perspectiva de la estructura interna del PDF, estas herramientas son anotaciones. Soportamos los siguientes tipos de herramientas de dibujo.

* Anotación de Línea - herramienta para dibujar líneas y flechas.
* Anotación de Cuadrado - para dibujar cuadrados y rectángulos.
* Anotación de Círculo - para óvalos y círculos.
* Anotación de Texto Libre - para comentarios de llamada.
* Anotación de Polígono - para polígonos y nubes.
* Anotación de Polilínea - para líneas conectadas.

## Agregar Formas y Figuras en la Página

El enfoque para agregar la anotación es típico para cualquiera de ellas.

El siguiente fragmento de código también funciona con la biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

1. Cargar el archivo PDF o crear uno nuevo mediante [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).
1. Crear la nueva anotación y establecer parámetros (nuevo Rectángulo, nuevo Punto, título, color, ancho, etc.).
1. Crear la nueva [PopupAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/popupannotation/methods/index).
1. Vincular la anotación emergente con la original.
1. Agregar la anotación a la página.

## Agregar Líneas o Flechas

El propósito de la anotación de línea es mostrar una línea o flecha sencilla en la página. Para crear una línea necesitamos un nuevo objeto LineAnnotation.  
El constructor de la clase LineAnnotation toma cuatro parámetros:

* La página donde se agregará la anotación.
* El rectángulo que define el límite de la anotación.
* Los dos puntos que definen el inicio y el final de la línea.

También necesitamos inicializar algunas propiedades:

* `Title` - generalmente, es el nombre del usuario que hizo este comentario.
* `Subject` - puede ser cualquier cadena, pero en casos comunes es el nombre de la anotación.

Para estilizar nuestra línea necesitamos establecer el color, el ancho, el estilo de inicio y el estilo de finalización. Estas propiedades controlan cómo se verá y se comportará la anotación en el visor de PDF. Por ejemplo, las propiedades `StartingStyle` y `EndingStyle` determinan qué tipo de forma se dibujará en los extremos de la línea, como una flecha abierta, una flecha cerrada, un círculo, etc.

El siguiente fragmento de código muestra cómo agregar una Anotación de Línea a un archivo PDF:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddLineAnnotation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "Appartments.pdf"))
    {
        // Create Line Annotation
        var lineAnnotation = new Aspose.Pdf.Annotations.LineAnnotation(
            document.Pages[1],
            new Aspose.Pdf.Rectangle(550, 93, 562, 439),
            new Aspose.Pdf.Point(556, 99), new Aspose.Pdf.Point(556, 443))
        {
            Title = "John Smith",
            Color = Aspose.Pdf.Color.Red,
            Width = 3,
            StartingStyle = Aspose.Pdf.Annotations.LineEnding.OpenArrow,
            EndingStyle = Aspose.Pdf.Annotations.LineEnding.OpenArrow,
            Popup = new Aspose.Pdf.Annotations.PopupAnnotation(document.Pages[1], new Aspose.Pdf.Rectangle(842, 124, 1021, 266))
        };

        // Add annotation to the page
        document.Pages[1].Annotations.Add(lineAnnotation);

        // Save PDF document
        document.Save(dataDir + "AddLineAnnotation_out.pdf");
    }
}
```

## Agregar Cuadrado o Círculo

Las anotaciones [Square](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/squareannotation) y [Circle](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/circleannotation) mostrarán un rectángulo o una elipse en la página. Cuando se abran, mostrarán una ventana emergente que contiene el texto de la nota asociada. Las anotaciones cuadradas son como las anotaciones de círculo (instancias de la clase Aspose. Pdf. Annotations. CircleAnnotation) aparte de la forma.

### Agregar anotación de Círculo

Para dibujar una nueva anotación de círculo o elipse, necesitamos crear un nuevo objeto CircleAnnotation. El constructor de la clase `CircleAnnotation` toma dos parámetros:

* La página donde se agregará la anotación.
* El rectángulo que define el límite de la anotación.

También podemos establecer algunas propiedades del objeto `CircleAnnotation`, como el título, el color, el color interior, la opacidad. Estas propiedades controlan cómo se verá y se comportará la anotación en el visor de PDF. Aquí y más adelante en el Cuadrado, el color `InteriorColor` es el color de relleno y `Color` es el color del borde.

### Agregar anotación de Cuadrado

Dibujar un rectángulo es lo mismo que dibujar un círculo. El siguiente fragmento de código muestra cómo agregar anotaciones de círculo y cuadrado a una página PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddCircleAndSquareAnnotations()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "appartments.pdf"))
    {
        // Create Circle Annotation
        var circleAnnotation = new Aspose.Pdf.Annotations.CircleAnnotation(document.Pages[1], new Aspose.Pdf.Rectangle(270, 160, 483, 383))
        {
            Title = "John Smith",
            Subject = "Circle",
            Color = Aspose.Pdf.Color.Red,
            InteriorColor = Aspose.Pdf.Color.MistyRose,
            Opacity = 0.5,
            Popup = new Aspose.Pdf.Annotations.PopupAnnotation(document.Pages[1], new Aspose.Pdf.Rectangle(842, 316, 1021, 459))
        };

        // Create Square Annotation
        var squareAnnotation = new Aspose.Pdf.Annotations.SquareAnnotation(document.Pages[1], new Aspose.Pdf.Rectangle(67, 317, 261, 459))
        {
            Title = "John Smith",
            Subject = "Rectangle",
            Color = Aspose.Pdf.Color.Blue,
            InteriorColor = Aspose.Pdf.Color.BlueViolet,
            Opacity = 0.25,
            Popup = new Aspose.Pdf.Annotations.PopupAnnotation(document.Pages[1], new Aspose.Pdf.Rectangle(842, 196, 1021, 338))
        };

        // Add annotations to the page
        document.Pages[1].Annotations.Add(circleAnnotation);
        document.Pages[1].Annotations.Add(squareAnnotation);

        // Save PDF document
        document.Save(dataDir + "AddCircleAndSquareAnnotations_out.pdf");
    }
}
```

Como ejemplo, veremos el siguiente resultado de agregar anotaciones de Cuadrado y Círculo a un documento PDF:

## Agregar Anotaciones de Polígono y Polilínea

La herramienta Polí permite crear formas y contornos con un número arbitrario de lados en el documento.

**Las Anotaciones de Polígono** representan polígonos en una página. Pueden tener cualquier número de vértices conectados por líneas rectas.  
**Las Anotaciones de Polilínea** son también similares a los polígonos, la única diferencia es que los primeros y últimos vértices no están conectados implícitamente.

### Agregar Anotación de Polígono

PolygonAnnotation es responsable de las anotaciones de polígonos. El constructor de la clase PolygonAnnotation toma tres parámetros:

* La página donde se agregará la anotación.
* El rectángulo que define el límite de la anotación.
* El arreglo de puntos que definen los vértices del polígono.

`Color` e `InteriorColor` se utilizan para los colores de borde y relleno respectivamente.

### Agregar Anotación de Polilínea

PolygonAnnotation es responsable de las anotaciones de polígonos. El constructor de la clase PolygonAnnotation toma tres parámetros:

* La página donde se agregará la anotación.
* El rectángulo que define el límite de la anotación.
* El arreglo de puntos que definen los vértices del polígono.

En lugar de `PolygonAnnotation` no podemos rellenar esta forma, por lo que no necesitamos usar `InteriorColor`.

El siguiente fragmento de código muestra cómo agregar Anotaciones de Polígono y Polilínea a un archivo PDF:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddPolygonAndPolylineAnnotations()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "appartments.pdf"))
    {
        // Create Polygon Annotation
        var polygonAnnotation = new Aspose.Pdf.Annotations.PolygonAnnotation(
            document.Pages[1],
            new Aspose.Pdf.Rectangle(270, 193, 571, 383),
            new Aspose.Pdf.Point[] {
                new Aspose.Pdf.Point(274, 381),
                new Aspose.Pdf.Point(555, 381),
                new Aspose.Pdf.Point(555, 304),
                new Aspose.Pdf.Point(570, 304),
                new Aspose.Pdf.Point(570, 195),
                new Aspose.Pdf.Point(274, 195)
            })
        {
            Title = "John Smith",
            Color = Aspose.Pdf.Color.Blue,
            InteriorColor = Aspose.Pdf.Color.BlueViolet,
            Opacity = 0.25,
            Popup = new Aspose.Pdf.Annotations.PopupAnnotation(document.Pages[1], new Aspose.Pdf.Rectangle(842, 196, 1021, 338))
        };

        // Create Polyline Annotation
        var polylineAnnotation = new Aspose.Pdf.Annotations.PolylineAnnotation(
            document.Pages[1],
            new Aspose.Pdf.Rectangle(270, 193, 571, 383),
            new Aspose.Pdf.Point[] {
                new Aspose.Pdf.Point(545, 150),
                new Aspose.Pdf.Point(545, 190),
                new Aspose.Pdf.Point(667, 190),
                new Aspose.Pdf.Point(667, 110),
                new Aspose.Pdf.Point(626, 111)
            })
        {
            Title = "John Smith",
            Color = Aspose.Pdf.Color.Red,
            Popup = new Aspose.Pdf.Annotations.PopupAnnotation(document.Pages[1], new Aspose.Pdf.Rectangle(842, 196, 1021, 338))
        };

        // Add annotations to the page
        document.Pages[1].Annotations.Add(polygonAnnotation);
        document.Pages[1].Annotations.Add(polylineAnnotation);

        // Save PDF document
        document.Save(dataDir + "AddPolygonAndPolylineAnnotations_out.pdf");
    }
}
```

## Obtener Figuras

Todas las anotaciones se almacenan en la colección `Annotations`. Cualquier anotación puede introducir su tipo a través de la propiedad `AnnotationType`. Por lo tanto, podemos hacer una consulta LINQ para filtrar las anotaciones deseadas.

### Obtener Anotaciones de Línea

El ejemplo a continuación explica cómo obtener todas las Anotaciones de Línea de la primera página del documento PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ReadLineAnnotations()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "Appartments_mod.pdf"))
    {
        // Get all line annotations from the first page
        var lineAnnotations = document.Pages[1].Annotations
            .Where(a => a.AnnotationType == Aspose.Pdf.Annotations.AnnotationType.Line)
            .Cast<Aspose.Pdf.Annotations.LineAnnotation>();

        // Iterate through each line annotation and print its coordinates
        foreach (var la in lineAnnotations)
        {
            Console.WriteLine($"[{la.Starting.X},{la.Starting.Y}]-[{la.Ending.X},{la.Ending.Y}]");
        }
    }
}
```

### Obtener Anotaciones de Círculo

El ejemplo a continuación explica cómo obtener todas las Anotaciones de Polilínea de la primera página del documento PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ReadCircleAnnotations()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "Appartments_mod.pdf"))
    {
        // Get all circle annotations from the first page
        var circleAnnotations = document.Pages[1].Annotations
            .Where(a => a.AnnotationType == Aspose.Pdf.Annotations.AnnotationType.Circle)
            .Cast<Aspose.Pdf.Annotations.CircleAnnotation>();

        // Iterate through each circle annotation and print its rectangle
        foreach (var ca in circleAnnotations)
        {
            Console.WriteLine($"[{ca.Rect}]");
        }
    }
}
```

### Obtener Anotaciones de Cuadrado

El ejemplo a continuación explica cómo obtener todas las Anotaciones de Polilínea de la primera página del documento PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ReadSquareAnnotations()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "Appartments_mod.pdf"))
    {
        // Get all square annotations from the first page
        var squareAnnotations = document.Pages[1].Annotations
            .Where(a => a.AnnotationType == Aspose.Pdf.Annotations.AnnotationType.Square)
            .Cast<Aspose.Pdf.Annotations.SquareAnnotation>();

        // Iterate through each square annotation and print its rectangle
        foreach (var sq in squareAnnotations)
        {
            Console.WriteLine($"[{sq.Rect}]");
        }
    }
}
```

### Obtener Anotaciones de Polilínea

El ejemplo a continuación explica cómo obtener todas las Anotaciones de Polilínea de la primera página del documento PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ReadPolylineAnnotations()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "Appartments_mod.pdf"))
    {
        // Get all polyline annotations from the first page
        var polyAnnotations = document.Pages[1].Annotations
            .Where(a => a.AnnotationType == Aspose.Pdf.Annotations.AnnotationType.PolyLine)
            .Cast<Aspose.Pdf.Annotations.PolylineAnnotation>();

        // Iterate through each polyline annotation and print its rectangle
        foreach (var pa in polyAnnotations)
        {
            Console.WriteLine($"[{pa.Rect}]");
        }
    }
}
```

### Obtener Anotaciones de Polígono

El ejemplo a continuación explica cómo obtener todas las Anotaciones de Polígono de la primera página del documento PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ReadPolygonAnnotations()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "Appartments_mod.pdf"))
    {
        // Get all polygon annotations from the first page
        var polyAnnotations = document.Pages[1].Annotations
            .Where(a => a.AnnotationType == Aspose.Pdf.Annotations.AnnotationType.Polygon)
            .Cast<Aspose.Pdf.Annotations.PolygonAnnotation>();

        // Iterate through each polygon annotation and print its rectangle
        foreach (var pa in polyAnnotations)
        {
            Console.WriteLine($"[{pa.Rect}]");
        }
    }
}
```

## Eliminar Figuras

El enfoque para eliminar anotaciones de PDF es bastante simple:

* Seleccionar anotaciones para eliminar (hacer alguna colección).
* Iterar sobre la colección usando un bucle foreach y eliminar cada anotación de la colección de anotaciones usando el método Delete.

### Eliminar Anotación de Línea

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DeleteLineAnnotations()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "Appartments_mod.pdf"))
    {
        // Get all line annotations from the first page
        var lineAnnotations = document.Pages[1].Annotations
            .Where(a => a.AnnotationType == Aspose.Pdf.Annotations.AnnotationType.Line)
            .Cast<Aspose.Pdf.Annotations.LineAnnotation>();

        // Iterate through each line annotation and delete it
        foreach (var la in lineAnnotations)
        {
            document.Pages[1].Annotations.Delete(la);
        }

        // Save PDF document
        document.Save(dataDir + "DeleteLineAnnotations_out.pdf");
    }
}
```

### Eliminar Anotaciones de Círculo y Cuadrado

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DeleteCircleAndSquareAnnotations()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "Appartments_mod.pdf"))
    {
        // Get all circle and square annotations from the first page
        var figures = document.Pages[1].Annotations
            .Where(a =>
                a.AnnotationType == Aspose.Pdf.Annotations.AnnotationType.Circle
                || a.AnnotationType == Aspose.Pdf.Annotations.AnnotationType.Square);

        // Iterate through each figure annotation and delete it
        foreach (var fig in figures)
        {
            document.Pages[1].Annotations.Delete(fig);
        }

        // Save PDF document
        document.Save(dataDir + "DeleteCircleAndSquareAnnotations_out.pdf");
    }
}
```

### Eliminar Anotaciones de Polígono y Polilínea

El siguiente fragmento de código muestra cómo eliminar Anotaciones de Polígono y Polilínea de un archivo PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DeletePolylineAndPolygonAnnotations()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "Appartments_mod.pdf"))
    {
        // Get all polyline and polygon annotations from the first page
        var polyAnnotations = document.Pages[1].Annotations
            .Where(a => a.AnnotationType == Aspose.Pdf.Annotations.AnnotationType.PolyLine
                        || a.AnnotationType == Aspose.Pdf.Annotations.AnnotationType.Polygon);

        // Iterate through each polyline or polygon annotation and delete it
        foreach (var pa in polyAnnotations)
        {
            document.Pages[1].Annotations.Delete(pa);
        }

        // Save PDF document
        document.Save(dataDir + DeletePolylineAndPolygonAnnotations_out.pdf");
    }
}
```

## Cómo agregar Anotación de Tinta a un archivo PDF

Una Anotación de Tinta representa un "garabato" a mano alzada compuesto de uno o más caminos disjuntos. Cuando se abre, mostrará una ventana emergente que contiene el texto de la nota asociada.

La [InkAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/inkannotation) representa un garabato a mano alzada compuesto de uno o más puntos disjuntos. Por favor, intente usar el siguiente fragmento de código para agregar InkAnnotation en el documento PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddInkAnnotation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "appartments.pdf"))
    {
        // Get first page
        var page = document.Pages[1];

        // Define the rectangle for the ink annotation
        var arect = new Aspose.Pdf.Rectangle(156.574, 521.316, 541.168, 575.703);

        // Create a list of ink paths
        IList<Aspose.Pdf.Point[]> inkList = new List<Aspose.Pdf.Point[]>();
        var arrpt = new[]
        {
            new Aspose.Pdf.Point(209.727, 542.263),
            new Aspose.Pdf.Point(209.727, 541.94),
            new Aspose.Pdf.Point(209.727, 541.616)
        };
        inkList.Add(arrpt);

        // Create the ink annotation
        var ia = new Aspose.Pdf.Annotations.InkAnnotation(page, arect, inkList)
        {
            Title = "John Smith",
            Subject = "Pencil",
            Color = Aspose.Pdf.Color.LightBlue,
            CapStyle = Aspose.Pdf.Annotations.CapStyle.Rounded,
            Opacity = 0.5
        };

        // Set the border for the annotation
        var border = new Aspose.Pdf.Annotations.Border(ia)
        {
            Width = 25
        };
        ia.Border = border;

        // Add the annotation to the page
        page.Annotations.Add(ia);

        // Save PDF document
        document.Save(dataDir + "AddInkAnnotation_out.pdf");
    }
}
```

### Establecer el ancho de línea de InkAnnotation

El ancho de [InkAnnottion](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/inkannotation) se puede cambiar usando los objetos LineInfo y Border.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddInkAnnotationWithLineWidth()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();

        // Create a list of ink paths
        IList<Aspose.Pdf.Point[]> inkList = new List<Aspose.Pdf.Point[]>();

        // Define line information
        var lineInfo = new Aspose.Pdf.Facades.LineInfo
        {
            VerticeCoordinate = new float[] { 55, 55, 70, 70, 70, 90, 150, 60 },
            Visibility = true,
            LineColor = System.Drawing.Color.Red,
            LineWidth = 2
        };

        // Convert line coordinates to Aspose.Pdf.Point array
        int length = lineInfo.VerticeCoordinate.Length / 2;
        var gesture = new Aspose.Pdf.Point[length];
        for (int i = 0; i < length; i++)
        {
            gesture[i] = new Aspose.Pdf.Point(lineInfo.VerticeCoordinate[2 * i], lineInfo.VerticeCoordinate[2 * i + 1]);
        }

        // Add the gesture to the ink list
        inkList.Add(gesture);

        // Create the ink annotation
        var a1 = new Aspose.Pdf.Annotations.InkAnnotation(document.Pages[1], new Aspose.Pdf.Rectangle(100, 100, 300, 300), inkList)
        {
            Subject = "Test",
            Title = "Title",
            Color = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.Green)
        };

        // Set the border for the annotation
        var border = new Aspose.Pdf.Annotations.Border(a1)
        {
            Width = 3,
            Effect = Aspose.Pdf.Annotations.BorderEffect.Cloudy,
            Dash = new Aspose.Pdf.Annotations.Dash(1, 1),
            Style = Aspose.Pdf.Annotations.BorderStyle.Solid
        };
        a1.Border = border;

        // Add the annotation to the page
        page.Annotations.Add(a1);

        // Save PDF document
        document.Save(dataDir + "lnkAnnotationLineWidth_out.pdf");
    }
}
```

### Eliminar Anotación de Círculo

El siguiente fragmento de código muestra cómo eliminar la Anotación de Círculo de un archivo PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DeleteCircleAnnotation()
{
	// The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();
	
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "Appartments_mod.pdf"))
    {
        var circleAnnotations = document.Pages[1].Annotations
            .Where(a => a.AnnotationType == AnnotationType.Circle)
            .Cast<Aspose.Pdf.Annotations.CircleAnnotation>();

        foreach (var ca in circleAnnotations)
        {
            document.Pages[1].Annotations.Delete(ca);
        }

        // Save PDF document
        document.Save(dataDir + "DeleteCircleAnnotation_out.pdf");
    }
}
```

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