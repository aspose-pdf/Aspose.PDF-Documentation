---
title: Añadir Objeto Línea al Archivo PDF
linktitle: Añadir Línea
type: docs
weight: 40
url: es/java/add-line/
description: Este artículo explica cómo crear un objeto línea en su PDF usando Aspose.PDF para Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Añadir objeto Línea

Aspose.PDF para Java admite la función de agregar objetos gráficos (por ejemplo, gráfico, línea, rectángulo, etc.) a documentos PDF. También tiene la posibilidad de agregar un objeto [Línea](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/Line) donde también puede especificar el patrón de guiones, el color y otros formatos para el elemento Línea.

Siga los pasos a continuación:

1. Cree una instancia de [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

1. Agregue [Página](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) a la colección de páginas del archivo PDF.

1. Cree una instancia de [Gráfico](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/Graph).

1. Agregue el objeto Gráfico a la colección de párrafos de la instancia de página.

1. Crear una instancia de [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/Rectangle).

1. Establecer el ancho de línea.

1. Agregar el objeto [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/Rectangle) a la colección de formas del objeto Graph.

1. Guardar su archivo PDF.

El siguiente fragmento de código muestra cómo agregar un objeto [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/Rectangle) que está relleno de color.

```java
 public static void ExampleLine() {
        // Crear instancia de Document
        Document pdfDocument = new Document();
        // Agregar página a la colección de páginas del archivo PDF
        Page page = pdfDocument.getPages().add();
        // Crear instancia de Graph
        Graph graph = new Graph(100, 400);

        // Agregar objeto gráfico a la colección de párrafos de la instancia de página
        page.getParagraphs().add(graph);

        // Crear instancia de Rectangle
        Line line = new Line(new float[] { 100, 100, 200, 100 });
        
        line.getGraphInfo().setLineWidth(5);
        
        // Agregar objeto rectángulo a la colección de formas del objeto Graph
        graph.getShapes().add(line);

        // Guardar archivo PDF
        pdfDocument.save(_dataDir + "LineAdded.pdf");
    }
```


![Add Line](add_line.png)

## Cómo agregar una línea punteada discontinua a su documento PDF

```java
public static void ExampleDashedLine() {
        // Crear una instancia de Documento
        Document pdfDocument = new Document();
        // Agregar página a la colección de páginas del archivo PDF
        Page page = pdfDocument.getPages().add();

        // Crear objeto de Dibujo con ciertas dimensiones
        Graph canvas = new Graph(100, 400);
        // Agregar objeto de dibujo a la colección de párrafos de la instancia de página
        page.getParagraphs().add(canvas);

        // Crear objeto Línea
        Line line = new Line(new float[] { 100, 100, 200, 100 });

        // Establecer color para el objeto Línea
        line.getGraphInfo().setColor(Color.getRed());
        // Especificar matriz de guiones para el objeto línea
        line.getGraphInfo().setDashArray(new int[] { 0, 1, 0 });
        // Establecer la fase de guiones para la instancia de Línea
        line.getGraphInfo().setDashPhase(1);
        // Agregar línea a la colección de formas del objeto de dibujo
        canvas.getShapes().add(line);
        // Guardar documento PDF
        pdfDocument.save(_dataDir + "DashLength_out.pdf");
    }
```


Vamos a comprobar el resultado:

![Línea Discontinua](dash_line.png)

## Dibujar Línea a Través de la Página

También podemos usar un objeto línea para dibujar una cruz comenzando desde la esquina Inferior-Izquierda a la esquina Superior-Derecha y desde la esquina Superior-Izquierda a la esquina Inferior-Derecha.

Por favor, observe el siguiente fragmento de código para cumplir con este requisito.

```java
    public static void ExampleLineAcrossPage() {
        // Crear instancia de Documento
        Document pdfDocument = new Document();
        // Añadir página a la colección de páginas del archivo PDF
        Page page = pdfDocument.getPages().add();
        // Establecer margen de página en todos los lados como 0

        page.getPageInfo().getMargin().setLeft(0);
        page.getPageInfo().getMargin().setRight(0);
        page.getPageInfo().getMargin().setBottom(0);
        page.getPageInfo().getMargin().setTop(0);

        // Crear objeto Gráfico con Ancho y Alto iguales a las dimensiones de la página
        Graph graph = new Graph((float) page.getPageInfo().getWidth(), (float) page.getPageInfo().getHeight());

        // Crear primer objeto línea comenzando desde la esquina Inferior-Izquierda a la esquina Superior-Derecha de la página
        Line line = new Line(new float[] { (float) page.getRect().getLLX(), 0, (float) page.getPageInfo().getWidth(),
                (float) page.getRect().getURY() });

        // Añadir línea a la colección de formas del objeto Gráfico
        graph.getShapes().add(line);
        // Dibujar línea desde la esquina Superior-Izquierda de la página a la esquina Inferior-Derecha de la página
        Line line2 = new Line(new float[] { 0, (float) page.getRect().getURY(), (float) page.getPageInfo().getWidth(),
                (float) page.getRect().getLLX() });

        // Añadir línea a la colección de formas del objeto Gráfico
        graph.getShapes().add(line2);
        // Añadir objeto Gráfico a la colección de párrafos de la página
        page.getParagraphs().add(graph);

        // Guardar archivo PDF
        pdfDocument.save(_dataDir + "DrawingLine_out.pdf");
    }
```


![Dibujo de Línea](draw_line.png)