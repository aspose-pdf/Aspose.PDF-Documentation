---
title: Añadir Objeto Rectángulo al Archivo PDF
linktitle: Añadir Rectángulo
type: docs
weight: 50
url: es/cpp/add-rectangle/
description: Este artículo explica cómo crear un objeto Rectángulo en su PDF usando Aspose.PDF para C++.
lastmod: "2021-12-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Añadir objeto Rectángulo

Aspose.PDF para C++ soporta la función de añadir objetos gráficos (por ejemplo gráfico, línea, rectángulo, etc.) a documentos PDF. También obtiene la ventaja de añadir el objeto [Rectángulo](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.rectangle/) donde también ofrece la función de llenar el objeto rectángulo con un cierto color, controlar el orden Z, añadir relleno de color degradado, etc.

Primero, veamos la posibilidad de crear un objeto Rectángulo.

Siga los pasos a continuación:

1. Cree un nuevo [Documento](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document/) PDF

1. Añada [Página](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page/) a la colección de páginas del archivo PDF

1. Añadir [Fragmento de texto](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.te_x_fragment/) a la colección de párrafos de la instancia de página

1. Crear instancia de [Gráfico](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.graph/)

1. Establecer borde para el [Objeto de Dibujo](https://reference.aspose.com/pdf/cpp/namespace/aspose.pdf.drawing)

1. Crear instancia de Rectángulo

1. Agregar objeto [Rectángulo](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.rectangle/) a la colección de formas del objeto Gráfico

1. Agregar objeto gráfico a la colección de párrafos de la instancia de página

1. Añadir [Fragmento de texto](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.te_x_fragment/) a la colección de párrafos de la instancia de página

1. Y guarda tu archivo PDF

```csharp
 private static void AddRectangle(Page page, float x, float y, float width, float height, Color color, int zindex)
        {
            // Crear objeto gráfico con dimensiones iguales a las especificadas para el objeto Rectángulo
            Aspose.Pdf.Drawing.Graph graph = new Aspose.Pdf.Drawing.Graph(width, height)
            {
                // ¿Podemos cambiar la posición de la instancia del gráfico?
                IsChangePosition = false,
                // Establecer la posición de la coordenada izquierda para la instancia del gráfico
                Left = x,
                // Establecer la posición de la coordenada superior para el objeto gráfico
                Top = y
            };
            // Añadir un rectángulo dentro del "gráfico"
            Rectangle rect = new Rectangle(0, 0, width, height);
            // Establecer el color de relleno del rectángulo
            rect.GraphInfo.FillColor = color;
            // Color del objeto gráfico
            rect.GraphInfo.Color = color;
            // Añadir rectángulo a la colección de formas de la instancia del gráfico
            graph.Shapes.Add(rect);
            // Establecer el índice Z para el objeto rectángulo
            graph.ZIndex = zindex;
            // Añadir gráfico a la colección de párrafos del objeto página
            page.Paragraphs.Add(graph);
        }
```
![Crear Rectángulo](create_rectangle.png)

## Crear Objeto de Rectángulo Relleno

Aspose.PDF para C++ también ofrece la función de rellenar un objeto de rectángulo con un color determinado.

El siguiente fragmento de código muestra cómo añadir un objeto [Rectangle](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.rectangle/) que está relleno de color.

```csharp
    {
        private const string _dataDir = "C:\\Samples\\";
        public static void RectangleFilled()
        {
            // Crear instancia de Documento
            var doc = new Document();

            // Añadir página a la colección de páginas del archivo PDF
            var page = doc.Pages.Add();
            // Crear instancia de Gráfico
            var graph = new Aspose.Pdf.Drawing.Graph(100, 400);

            // Añadir objeto gráfico a la colección de párrafos de la instancia de página
            page.Paragraphs.Add(graph);

            // Crear instancia de Rectángulo
            var rect = new Rectangle(100, 100, 200, 120);

            // Especificar color de relleno para el objeto Gráfico
            rect.GraphInfo.FillColor = Color.Red;

            // Añadir objeto rectángulo a la colección de formas del objeto Gráfico
            graph.Shapes.Add(rect);

            // Guardar archivo PDF
            doc.Save(_dataDir + "CreateFilledRectangle_out.pdf");
        }
```

Mira el resultado del rectángulo relleno con color sólido:

![Rectángulo Relleno](fill_rectangle.png)

## Añadir Dibujo con Relleno de Degradado

Aspose.PDF para C++ soporta la funcionalidad de añadir objetos gráficos a documentos PDF y, a veces, se requiere llenar los objetos gráficos con Color Degradado. Para llenar los objetos gráficos con Color Degradado, necesitamos establecer setPatterColorSpace con el objeto gradientAxialShading de la siguiente manera.

El siguiente fragmento de código muestra cómo añadir un objeto [Rectangle](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.rectangle/) que está relleno con Color Degradado.

```csharp
 public static void CreateFilledRectangletGradientFill()
        {
            // Crear instancia de Documento
            var doc = new Document();

            // Añadir página a la colección de páginas del archivo PDF
            var page = doc.Pages.Add();
            // Crear instancia de Graph
            var graph = new Aspose.Pdf.Drawing.Graph(400, 400);
            // Añadir objeto gráfico a la colección de párrafos de la instancia de página
            page.Paragraphs.Add(graph);
            // Crear instancia de Rectángulo
            var rect = new Rectangle(0, 0, 300, 300);
            // Especificar color de relleno para el objeto Graph
            var gradientColor = new Color();
            var gradientSettings = new GradientAxialShading(Color.Red, Color.Blue)
            {
                Start = new Point(0, 0),
                End = new Point(350, 350)
            };
            gradientColor.PatternColorSpace = gradientSettings;
            rect.GraphInfo.FillColor = gradientColor;

            // Añadir objeto rectángulo a la colección de formas del objeto Graph
            graph.Shapes.Add(rect);

            // Guardar archivo PDF
            doc.Save(_dataDir + "CreateFilledRectangle_out.pdf");
        }
```

![Gradient Rectangle](gradient.png)

## Crear Rectángulo con canal de color Alfa

Aspose.PDF para C+++ admite rellenar un objeto rectángulo con un color determinado. Un objeto rectángulo también puede tener un canal de color Alfa para dar una apariencia transparente. El siguiente fragmento de código muestra cómo agregar un objeto [Rectangle](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.rectangle/) con canal de color Alfa.

Los píxeles de la imagen pueden almacenar información sobre su opacidad junto con el valor del color. Esto permite crear imágenes con áreas transparentes o semitransparentes.

En lugar de hacer un color transparente, cada píxel almacena información sobre cuán opaco es. Estos datos de opacidad se llaman canal alfa y normalmente se almacenan después de los canales de color del píxel.

```csharp
     public static void RectangleFilled_AlphaChannel()
        {
            // Crear instancia de Documento
            var doc = new Document();

            // Agregar página a la colección de páginas del archivo PDF
            var page = doc.Pages.Add();
            // Crear instancia de Gráfico
            var graph = new Aspose.Pdf.Drawing.Graph(100, 400);
            // Agregar objeto gráfico a la colección de párrafos de la instancia de página
            page.Paragraphs.Add(graph);
            // Crear instancia de Rectángulo
            var rect = new Rectangle(100, 100, 200, 120);
            // Especificar color de relleno para el objeto Gráfico
            rect.GraphInfo.FillColor = Color.FromArgb(128, 244, 180, 0);

            // Agregar objeto rectángulo a la colección de formas del objeto Gráfico
            graph.Shapes.Add(rect);

            // Crear segundo objeto rectángulo
            var rect1 = new Rectangle(200, 150, 200, 100);
            rect1.GraphInfo.FillColor = Color.FromArgb(160, 120, 0, 120);
            graph.Shapes.Add(rect1);

            // Agregar instancia de gráfico a la colección de párrafos del objeto página
            page.Paragraphs.Add(graph);

            // Guardar archivo PDF
            doc.Save(_dataDir + "CreateFilledRectangle_out.pdf");
        }
```

![Rectangle Alpha Channel Color](rectangle_color.png)

## Controlar el orden Z del rectángulo

Aspose.PDF para C++ admite la función de agregar objetos gráficos (por ejemplo, gráfico, línea, rectángulo, etc.) a documentos PDF. Al agregar más de una instancia del mismo objeto dentro del archivo PDF, podemos controlar su renderizado especificando el orden Z. El orden Z también se utiliza cuando necesitamos renderizar objetos uno encima del otro.

El siguiente fragmento de código muestra los pasos para renderizar objetos [Rectangle](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.rectangle/) uno encima del otro.

```csharp
 public static void AddRectangleZOrder()
        {
            // Instantiate Document class object
            Document doc1 = new Document();
            /// Add page to pages collection of PDF file
            Page page1 = doc1.Pages.Add();
            // Set size of PDF page
            page1.SetPageSize(375, 300);
            // Set left margin for page object as 0
            page1.PageInfo.Margin.Left = 0;
            // Set top margin of page object as 0
            page1.PageInfo.Margin.Top = 0;
            // Create a new rectangle with Color as Red, Z-Order as 0 and certain dimensions
            AddRectangle(page1, 50, 40, 60, 40, Color.Red, 2);
            // Create a new rectangle with Color as Blue, Z-Order as 0 and certain dimensions
            AddRectangle(page1, 20, 20, 30, 30, Color.Blue, 1);
            // Create a new rectangle with Color as Green, Z-Order as 0 and certain dimensions
            AddRectangle(page1, 40, 40, 60, 30, Color.Green, 0);
            // Save resultant PDF file
            doc1.Save(_dataDir + "ControlRectangleZOrder_out.pdf");
        }
```

![Controlando el Orden Z](control.png)