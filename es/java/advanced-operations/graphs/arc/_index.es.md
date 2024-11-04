---
title: Añadir Objeto de Arco al Archivo PDF
linktitle: Añadir Arco
type: docs
weight: 10
url: /java/add-arc/
description: Este artículo explica cómo crear un objeto de arco en su PDF usando Aspose.PDF para Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Añadir objeto de Arco

Aspose.PDF para Java admite la función de añadir objetos gráficos (por ejemplo, gráfico, línea, rectángulo, etc.) a documentos PDF. También ofrece la función de rellenar el objeto de arco con un cierto color.

Siga los pasos a continuación:

1. Crear una instancia de [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document)

1. Crear un [Drawing object](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/package-frame) con ciertas dimensiones

1. Establecer [Border](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/Graph#setBorder-com.aspose.pdf.BorderInfo-) para el objeto Drawing

1. Añadir objeto [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/Graph) a la colección de párrafos de la página

1. Guardar nuestro archivo PDF


El siguiente fragmento de código muestra cómo añadir un objeto [Arc](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/Arc).

```java
    public static void ExampleArc() {
        // Crear instancia de Documento
        Document pdfDocument = new Document();
        // Agregar página a la colección de páginas del archivo PDF
        Page page = pdfDocument.getPages().add();

        // Crear objeto de Dibujo con ciertas dimensiones
        Graph graph = new Graph(400, 400);
        // Establecer borde para el objeto de Dibujo
        BorderInfo borderInfo = new BorderInfo(BorderSide.All, Color.getGreen());
        graph.setBorder(borderInfo);

        Arc arc1 = new Arc(100, 100, 95, 0, 90);
        arc1.getGraphInfo().setColor(Color.getGreenYellow());
        graph.getShapes().add(arc1);

        Arc arc2 = new Arc(100, 100, 90, 70, 180);
        arc2.getGraphInfo().setColor(Color.getDarkBlue());
        graph.getShapes().add(arc2);

        Arc arc3 = new Arc(100, 100, 85, 120, 210);
        arc3.getGraphInfo().setColor(Color.getRed());
        graph.getShapes().add(arc3);

        // Agregar objeto Graph a la colección de párrafos de la página
        page.getParagraphs().add(graph);

        // Guardar archivo PDF
        pdfDocument.save(_dataDir + "DrawingArc_out.pdf");

    }
```


## Crear Objeto Arco Relleno

El siguiente ejemplo muestra cómo agregar un objeto Arco que está relleno con color y ciertas dimensiones.

```java
    public static void ExampleFilledArc() {
        // Crear instancia de Documento
        Document pdfDocument = new Document();
        // Añadir página a la colección de páginas del archivo PDF
        Page page = pdfDocument.getPages().add();

        // Crear objeto Dibujo con ciertas dimensiones
        Graph graph = new Graph(400, 400);
        // Establecer borde para el objeto Dibujo
        BorderInfo borderInfo = new BorderInfo(BorderSide.All, Color.getGreen());
        graph.setBorder(borderInfo);

        Arc arc = new Arc(100, 100, 95, 0, 90);
        arc.getGraphInfo().setFillColor(Color.getGreenYellow());
        graph.getShapes().add(arc);

        Line line = new Line(new float[] { 195, 100, 100, 100, 100, 195 });
        line.getGraphInfo().setFillColor(Color.getGreenYellow());
        graph.getShapes().add(line);

        // Añadir objeto Graph a la colección de párrafos de la página
        page.getParagraphs().add(graph);

        // Guardar archivo PDF
        pdfDocument.save(_dataDir + "DrawingArc_out.pdf");

    }
```


Let's see the result of adding a filled Arс:

![Arco Llena](filled_arc.png)