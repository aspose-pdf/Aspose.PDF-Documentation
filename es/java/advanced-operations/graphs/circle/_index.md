---
title: Añadir Objeto Círculo al archivo PDF
linktitle: Añadir Círculo
type: docs
weight: 20
url: /es/java/add-circle/
description: Este artículo explica cómo crear un objeto círculo en tu PDF usando Aspose.PDF para Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Añadir objeto Círculo

Al igual que los gráficos de barras, los gráficos circulares se pueden usar para mostrar datos en varias categorías separadas. Sin embargo, a diferencia de los gráficos de barras, los gráficos circulares se pueden usar solo cuando tienes datos para todas las categorías que componen el conjunto. Así que echemos un vistazo a cómo añadir un objeto [Círculo](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/Circle) con Aspose.PDF para Java.

Sigue los pasos a continuación:

1. Crea una instancia de [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document)

1. Crea un [objeto de Dibujo](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/package-frame) con ciertas dimensiones

1. Establecer [Borde](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/Graph#setBorder-com.aspose.pdf.BorderInfo-) para el objeto de Dibujo

1. Agregar objeto [Gráfico](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/Graph) a la colección de párrafos de la página

1. Guardar nuestro archivo PDF

```java
public static void ExampleCircle() {
        // Crear instancia de Documento
        Document pdfDocument = new Document();
        // Agregar página a la colección de páginas del archivo PDF
        Page page = pdfDocument.getPages().add();

        // Crear objeto de Dibujo con ciertas dimensiones
        Graph graph = new Graph(400, 200);
        // Establecer borde para el objeto de Dibujo
        BorderInfo borderInfo = new BorderInfo(BorderSide.All, Color.getGreen());
        graph.setBorder(borderInfo);

        Circle circle = new Circle(100,100,40);

        circle.getGraphInfo().setColor(Color.getGreenYellow());
        graph.getShapes().add(circle);

        // Agregar objeto Gráfico a la colección de párrafos de la página
        page.getParagraphs().add(graph);

        // Guardar archivo PDF
        pdfDocument.save(_dataDir + "DrawingCircle1_out.pdf");
    }
```


Nuestro círculo dibujado se verá así:

![Dibujo del Círculo](drawing_circle.png)

## Crear Objeto Círculo Relleno

Este ejemplo muestra cómo agregar un objeto Círculo que está relleno de color.

```java

    public static void ExampleFilledCircle() {
        // Crear instancia de Documento
        Document pdfDocument = new Document();
        // Agregar página a la colección de páginas del archivo PDF
        Page page = pdfDocument.getPages().add();

        // Crear objeto Dibujo con ciertas dimensiones
        Graph graph = new Graph(400, 200);
        // Establecer borde para el objeto Dibujo
        BorderInfo borderInfo = new BorderInfo(BorderSide.All, Color.getGreen());
        graph.setBorder(borderInfo);

        Circle circle = new Circle(100,100,40);
        circle.getGraphInfo().setColor(Color.getGreenYellow());       
        circle.getGraphInfo().setFillColor(Color.getGreenYellow());

        graph.getShapes().add(circle);

        // Agregar objeto Graph a la colección de párrafos de la página
        page.getParagraphs().add(graph);

        // Guardar archivo PDF
        pdfDocument.save(_dataDir + "DrawingCircle2_out.pdf");
    }
```


Let's see the result of adding a filled Circle:

![Círculo Relleno](filled_circle.png)