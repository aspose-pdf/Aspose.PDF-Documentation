---
title: Añadir Anotaciones de Figuras usando C#
linktitle: Anotaciones de Figuras
type: docs
weight: 30
url: /net/figures-annotation/
description: Este artículo describe cómo añadir, obtener y eliminar anotaciones de figuras de su documento PDF con Aspose.PDF para .NET
lastmod: "2023-09-12"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Añadir Anotaciones de Figuras usando C#",
    "alternativeHeadline": "Cómo añadir Anotaciones de Figuras en PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "generación de documentos PDF",
    "keywords": "pdf, c#, anotaciones de figuras, anotación de polígono, anotación de línea, anotación de cuadrado, anotación de círculo",
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
                "availableLanguage": "es"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "ventas",
                "areaServed": "GB",
                "availableLanguage": "es"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "ventas",
                "areaServed": "AU",
                "availableLanguage": "es"
            }
        ]
    },
    "url": "/net/figures-annotation/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/figures-annotation/"
    },
    "dateModified": "2022-02-04",
    "description": "Este artículo describe cómo añadir, obtener y eliminar anotaciones de figuras de su documento PDF con Aspose.PDF para .NET"
}
</script>
La aplicación de gestión de documentos PDF proporciona diversas herramientas para anotar documentos. Desde la perspectiva de la estructura interna del PDF, estas herramientas son anotaciones. Apoyamos los siguientes tipos de herramientas de dibujo.

* Anotación de Línea - herramienta para dibujar líneas y flechas
* Anotación de Cuadrado - para dibujar cuadrados y rectángulos
* Anotación de Círculo - para óvalos y círculos
* Anotación de Texto Libre - para comentarios de llamada
* Anotación de Polígono - para polígonos y nubes
* Anotación de Polilínea - para Líneas Conectadas

## Agregando Formas y Figuras en la Página

El enfoque para agregar la anotación es típico para cualquiera de ellas.

El siguiente fragmento de código también funciona con la biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

1. Carga el archivo PDF o crea uno nuevo por [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).
1. Crea la nueva anotación y establece parámetros (nuevo Rectángulo, nuevo Punto, título, color, ancho, etc).
1. Vincular la anotación emergente con la original.
1. Añadir anotación a la página

## Añadiendo Líneas o Flechas

El propósito de la anotación de línea es mostrar una línea o flecha sencilla en la página.
Para crear una Línea necesitamos un nuevo objeto LineAnnotation.
El constructor de la clase LineAnnotation toma cuatro parámetros:

* la página donde se añadirá la anotación,
* el rectángulo que define el límite de la anotación,
* y los dos puntos que definen el inicio y el fin de la línea.

También necesitamos inicializar algunas propiedades:

* `Title` - usualmente, es el nombre del usuario que hizo este comentario
* `Subject` - puede ser cualquier cadena, pero en casos comunes es el nombre de la anotación

Para estilizar nuestra línea necesitamos establecer el color, el ancho, el estilo inicial y el estilo final.
Para estilizar nuestra línea necesitamos establecer el color, ancho, estilo de inicio y estilo de finalización.

El siguiente fragmento de código muestra cómo agregar una Anotación de Línea a un archivo PDF:

```csharp
// Cargar el archivo PDF
Document document = new Document(System.IO.Path.Combine(_dataDir, "Appartments.pdf"));

// Crear Anotación de Línea
var lineAnnotation = new LineAnnotation(
    document.Pages[1],
    new Rectangle(550, 93, 562, 439),
    new Point(556, 99), new Point(556, 443))
{
    Title = "John Smith",
    Color = Color.Red,
    Width = 3,
    StartingStyle = LineEnding.OpenArrow,
    EndingStyle = LineEnding.OpenArrow,
    Popup = new PopupAnnotation(document.Pages[1], new Rectangle(842, 124, 1021, 266))
};

// Añadir anotación a la página
document.Pages[1].Annotations.Add(lineAnnotation);
document.Save(System.IO.Path.Combine(_dataDir, "Appartments_mod.pdf"));
```

## Añadiendo Cuadrado o Círculo

Las anotaciones [Square](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/squareannotation) y [Circle](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/circleannotation) mostrarán un rectángulo o un elipse en la página.
Las anotaciones [Square](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/squareannotation) y [Circle](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/circleannotation) mostrarán un rectángulo o una elipse en la página.

### Agregar anotación de Círculo

Para dibujar una nueva anotación de círculo o elipse, necesitamos crear un nuevo objeto CircleAnnotation. El constructor de la clase `CircleAnnotation` toma dos parámetros:

* la página donde se agregará la anotación,
* y el rectángulo que define el límite de la anotación

También podemos establecer algunas propiedades del objeto `CircleAnnotation`, como el título, el color, el color interior, la opacidad. Estas propiedades controlan cómo se verá y se comportará la anotación en el visor de PDF. Aquí y más adelante en Square el color `InteriorColor` es el color de relleno y `Color` es el color del borde.

### Agregar anotación de Cuadrado

Dibujar un rectángulo es lo mismo que dibujar un círculo.
Dibujar un rectángulo es lo mismo que dibujar un círculo.

```csharp
var dataDir = "<path-to-file>";
// Cargar el archivo PDF
Document document = new Document(System.IO.Path.Combine(dataDir, "appartments.pdf"));

// Crear Anotación de Círculo
var circleAnnotation = new CircleAnnotation(document.Pages[1], new Rectangle(270, 160, 483, 383))
{
    Title = "John Smith",
    Subject = "Círculo",
    Color = Color.Red,
    InteriorColor = Color.MistyRose,
    Opacity = 0.5,        
    Popup = new PopupAnnotation(document.Pages[1], new Rectangle(842, 316, 1021, 459))
};

// Crear Anotación de Cuadrado
var squareAnnotation = new SquareAnnotation(document.Pages[1], new Rectangle(67, 317, 261, 459))
{
    Title = "John Smith",
    Subject = "Rectángulo",
    Color = Color.Blue,
    InteriorColor = Color.BlueViolet,
    Opacity = 0.25,
    Popup = new PopupAnnotation(document.Pages[1], new Rectangle(842, 196, 1021, 338))
};

// Añadir anotación a la página
document.Pages[1].Annotations.Add(circleAnnotation);
document.Pages[1].Annotations.Add(squareAnnotation);
document.Save(System.IO.Path.Combine(dataDir, "appartments_mod.pdf"));
```
Como ejemplo, veremos el siguiente resultado de agregar anotaciones de Cuadrado y Círculo a un documento PDF:

![Demostración de anotación de Círculo y Cuadrado](circle_demo.png)

## Agregando Anotaciones de Polígono y Polilínea

La herramienta Poly- te permite crear formas y contornos con un número arbitrario de lados en el documento.

**Anotaciones de Polígono** representan polígonos en una página. Pueden tener cualquier número de vértices conectados por líneas rectas.
**Anotaciones de Polilínea** también son similares a los polígonos, la única diferencia es que los vértices primero y último no están implícitamente conectados.

### Agregando Anotación de Polígono

PolygonAnnotation es responsable de las anotaciones de polígonos. El constructor de la clase PolygonAnnotation toma tres parámetros:

* la página donde se agregará la anotación,
* el rectángulo que define el límite de la anotación,
* y un arreglo de puntos que definen los vértices del polígono.

`Color` y `InteriorColor` se utilizan para los colores del borde y del relleno respectivamente.

### Agregando Anotación de Polilínea
### Agregando Anotación de Polilínea

PolygonAnnotation es responsable de las anotaciones de polígonos. El constructor de la clase PolygonAnnotation toma tres parámetros:

* la página donde se añadirá la anotación,
* el rectángulo que define el límite de la anotación,
* y un arreglo de puntos que definen los vértices del polígono.

En lugar de `PolygonAnnotation` no podemos rellenar esta forma, así que no necesitamos usar `InteriorColor`.

El siguiente fragmento de código muestra cómo agregar Anotaciones de Polígono y Polilínea a un archivo PDF:

```csharp
// Cargar el archivo PDF
Document document = new Document(System.IO.Path.Combine(dataDir, "appartments.pdf"));

// Crear Anotación de Polígono
var polygonAnnotation = new PolygonAnnotation(document.Pages[1],
    new Rectangle(270, 193, 571, 383),
    new Point[] {
        new Point(274, 381),
        new Point(555, 381),
        new Point(555, 304),
        new Point(570, 304),
        new Point(570, 195),
        new Point(274, 195)})
{
    Title = "John Smith",
    Color = Color.Blue,
    InteriorColor = Color.BlueViolet,
    Opacity = 0.25,
    Popup = new PopupAnnotation(document.Pages[1], new Rectangle(842, 196, 1021, 338))
};

// Crear Anotación de Polilínea
var polylineAnnotation = new PolylineAnnotation(document.Pages[1],
    new Rectangle(270, 193, 571, 383),
    new Point[] {
        new Point(545,150),
        new Point(545,190),
        new Point(667,190),
        new Point(667,110),
        new Point(626,111)
        })
{
    Title = "John Smith",
    Color = Color.Red,
    Popup = new PopupAnnotation(document.Pages[1], new Rectangle(842, 196, 1021, 338))
};

// Añadir anotación a la página
document.Pages[1].Annotations.Add(polygonAnnotation);
document.Pages[1].Annotations.Add(polylineAnnotation);
document.Save(System.IO.Path.Combine(dataDir, "appartments_mod.pdf"));
```
## Obtención de Figuras

Todas las anotaciones se almacenan en la colección `Annotations`. Cualquier anotación puede introducir su tipo a través de la propiedad `AnnotationType`. Por lo tanto, podemos hacer una consulta LINQ para filtrar las anotaciones deseadas.

### Obtención de Anotaciones de Línea

El ejemplo a continuación explica cómo obtener todas las Anotaciones de Línea de la primera página del documento PDF.

```csharp
// Cargar el archivo PDF
Document document = new Document(System.IO.Path.Combine(_dataDir, "Appartments_mod.pdf"));
var lineAnnotations = document.Pages[1].Annotations
    .Where(a => a.AnnotationType == AnnotationType.Line)
    .Cast<LineAnnotation>();
foreach (var la in lineAnnotations)
{
    Console.WriteLine($"[{la.Starting.X},{la.Starting.Y}]-[{la.Ending.X},{la.Ending.Y}]");
}   
```

### Obtención de Anotaciones de Círculo

El ejemplo a continuación explica cómo obtener todas las Anotaciones de Polilínea de la primera página del documento PDF.

```csharp
// Cargar el archivo PDF
Document document = new Document(System.IO.Path.Combine(_dataDir, "Appartments_mod.pdf"));
var circleAnnotations = document.Pages[1].Annotations
    .Where(a => a.AnnotationType == AnnotationType.Line)
    .Cast<CircleAnnotation>();
foreach (var ca in circleAnnotations)
{
    Console.WriteLine($"[{ca.Rect}]");
}   
```
### Obtención de Anotaciones Cuadradas

El ejemplo a continuación explica cómo obtener todas las Anotaciones Cuadradas de la primera página del documento PDF.

```csharp
// Cargar el archivo PDF
Document document = new Document(System.IO.Path.Combine(_dataDir, "Appartments_mod.pdf"));
var squareAnnotations = document.Pages[1].Annotations
    .Where(a => a.AnnotationType == AnnotationType.Square)
    .Cast<SquareAnnotation>();
foreach (var sq in squareAnnotations)
{
    Console.WriteLine($"[{sq.Rect}]");
}
```

### Obtención de Anotaciones de Polilínea

El ejemplo a continuación explica cómo obtener todas las Anotaciones de Polilínea de la primera página del documento PDF.

```csharp
// Cargar el archivo PDF
Document document = new Document(System.IO.Path.Combine(_dataDir, "Appartments_mod.pdf"));
var polyAnnotations = document.Pages[1].Annotations
    .Where(a => a.AnnotationType == AnnotationType.PolyLine)
    .Cast<PolylineAnnotation>();
foreach (var pa in polyAnnotations)
{
    Console.WriteLine($"[{pa.Rect}]");
}     
```

### Obtención de Anotaciones de Polígono

El ejemplo a continuación explica cómo obtener todas las Anotaciones de Polígono de la primera página del documento PDF.

```csharp
Document document = new Document(System.IO.Path.Combine(_dataDir, "Appartments_mod.pdf"));
var polyAnnotations = document.Pages[1].Annotations
    .Where(a => a.AnnotationType == AnnotationType.Polygon)
    .Cast<PolygonAnnotation>();
foreach (var pa in polyAnnotations)
{
    Console.WriteLine($"[{pa.Rect}]");
} 
```

## Eliminando Figuras

El enfoque para eliminar anotaciones de un PDF es bastante simple:

* Selecciona las anotaciones a eliminar (hacer alguna colección)
* Itera sobre la colección usando un bucle foreach, y elimina cada anotación de la colección de anotaciones usando el método Delete.

### Eliminando Anotación de Línea

```csharp
// Cargar el archivo PDF
Document document = new Document(System.IO.Path.Combine(_dataDir, "Appartments_mod.pdf"));
var lineAnnotations = document.Pages[1].Annotations
    .Where(a => a.AnnotationType == AnnotationType.Line)
    .Cast<LineAnnotation>();

foreach (var la in lineAnnotations)
{
    document.Pages[1].Annotations.Delete(la);
}
```
### Eliminar Anotaciones de Círculo y Cuadrado

```csharp
// Cargar el archivo PDF
Document document = new Document(System.IO.Path.Combine(_dataDir, "Appartments_mod.pdf"));
var figures = document.Pages[1].Annotations
    .Where(a =>
        a.AnnotationType == AnnotationType.Circle
        || a.AnnotationType == AnnotationType.Square);

foreach (var fig in figures)
{
    document.Pages[1].Annotations.Delete(fig);
}
document.Save(System.IO.Path.Combine(_dataDir, "Appartments_del.pdf"));
```

### Eliminar Anotaciones de Polígono y Polilínea

El siguiente fragmento de código muestra cómo eliminar Anotaciones de Polígono y Polilínea de un archivo PDF.

```csharp
// Cargar el archivo PDF
Document document = new Document(System.IO.Path.Combine(_dataDir, "Appartments_mod.pdf"));
var polyAnnotations = document.Pages[1].Annotations
                .Where(a => a.AnnotationType == AnnotationType.PolyLine
                || a.AnnotationType == AnnotationType.Polygon);

foreach (var pa in polyAnnotations)
{
    document.Pages[1].Annotations.Delete(pa);
}
document.Save(System.IO.Path.Combine(_dataDir, "Appartments_del.pdf"));
```
## Cómo agregar una Anotación de Tinta a un archivo PDF

Una Anotación de Tinta representa un "garabato" a mano alzada compuesto de una o más trayectorias disjuntas. Cuando se abre, debe mostrar una ventana emergente que contiene el texto de la nota asociada.

La [InkAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/inkannotation) representa un garabato a mano alzada compuesto de uno o más puntos disjuntos. Por favor, intente usar el siguiente fragmento de código para agregar InkAnnotation en un documento PDF.

```csharp
// Cargar el archivo PDF
Document document = new Document(System.IO.Path.Combine(_dataDir, "appartments.pdf"));
Page page = document.Pages[1];

Rectangle arect = new Rectangle(156.574, 521.316, 541.168, 575.703);

IList<Point[]> inkList = new List<Point[]>();
Point[] arrpt = new[]
{
    new Point(209.727,542.263),
    new Point(209.727,541.94),
    new Point(209.727,541.616)
};
inkList.Add(arrpt);

InkAnnotation ia = new InkAnnotation(page, arect, inkList)
{
    Title = "John Smith",
    Subject = "Lápiz",
    Color = Color.LightBlue,
    CapStyle = CapStyle.Rounded,
    Opacity = 0.5
};
Border border = new Border(ia)
{
    Width = 25
};
ia.Border = border;
page.Annotations.Add(ia);

// Guardar archivo de salida
document.Save(System.IO.Path.Combine(_dataDir, "appartments_mod.pdf"));
```
### Establecer el ancho de línea de InkAnnotation

El ancho de [InkAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/inkannotation) se puede cambiar utilizando los objetos LineInfo y Border.

```csharp
// Para ejemplos completos y archivos de datos, por favor vaya a https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

Document doc = new Document();
doc.Pages.Add();
IList<Point[]> inkList = new List<Point[]>();
LineInfo lineInfo = new LineInfo();
lineInfo.VerticeCoordinate = new float[] { 55, 55, 70, 70, 70, 90, 150, 60 };
lineInfo.Visibility = true;
lineInfo.LineColor = System.Drawing.Color.Red;
lineInfo.LineWidth = 2;
int length = lineInfo.VerticeCoordinate.Length / 2;
Aspose.Pdf.Point[] gesture = new Aspose.Pdf.Point[length];
for (int i = 0; i < length; i++)
{
   gesture[i] = new Aspose.Pdf.Point(lineInfo.VerticeCoordinate[2 * i], lineInfo.VerticeCoordinate[2 * i + 1]);
}

inkList.Add(gesture);
InkAnnotation a1 = new InkAnnotation(doc.Pages[1], new Aspose.Pdf.Rectangle(100, 100, 300, 300), inkList);
a1.Subject = "Prueba";
a1.Title = "Título";
a1.Color = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.Green);
Border border = new Border(a1);
border.Width = 3;
border.Effect = BorderEffect.Cloudy;
border.Dash = new Dash(1, 1);
border.Style = BorderStyle.Solid;
doc.Pages[1].Annotations.Add(a1);

dataDir = dataDir + "lnkAnnotationLineWidth_out.pdf";
// Guardar archivo de salida
doc.Save(dataDir);
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
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "Biblioteca de Manipulación de PDF para .NET",
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
```
### Eliminar Anotación de Círculo

El siguiente fragmento de código muestra cómo eliminar una Anotación de Círculo de un archivo PDF.

```csharp
public static void DeleteCircleAnnotation()
{
    // Cargar el archivo PDF
    Document document = new Document(System.IO.Path.Combine(dataDir, "Appartments_mod.pdf"));
    var circleAnnotations = document.Pages[1].Annotations
        .Where(a => a.AnnotationType == AnnotationType.Circle)
        .Cast<CircleAnnotation>();

    foreach (var ca in circleAnnotations)
    {
        document.Pages[1].Annotations.Delete(ca);
    }
    document.Save(System.IO.Path.Combine(dataDir, "Appartments_del.pdf"));
}
```
