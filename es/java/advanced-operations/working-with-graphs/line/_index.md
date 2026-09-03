---
title: Agregar formas de línea a PDF en Java
linktitle: Agregar línea
type: docs
weight: 40
url: /es/java/add-line/
description: Aprenda cómo dibujar formas de línea y líneas con estilo en archivos PDF en Java.
lastmod: "2026-09-03"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Dibujar formas de línea en archivos PDF usando Java
Abstract: Este artículo muestra cómo agregar formas de línea a documentos PDF usando Aspose.PDF for Java. Cubre la creación de líneas a partir de matrices de coordenadas, la aplicación de estilo discontinuo y color, y el dibujo de líneas en todo el área de la página.
---
## Agregar una línea discontinua

1. Crear un nuevo PDF [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Agregar un [Página](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) al documento.
1. Crear un [Gráfica](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) contenedor y añádelo a la página.
1. Crea el [Línea](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/line/) forma y configura sus coordenadas.
1. Añade el [Línea](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/line/) al [Gráfica](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) contenedor.
1. Guardar el PDF de salida [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void addLine(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        Graph graph = new Graph(100.0, 400.0);
        page.getParagraphs().add(graph);

        Line line = new Line(new float[]{100, 100, 200, 100});
        line.getGraphInfo().setDashArray(new int[]{0, 1, 0});
        line.getGraphInfo().setDashPhase(1);
        graph.getShapes().addItem(line);

        document.save(outputFile.toString());
    }
}
```

## Agregar una línea de puntos o guiones coloreada

`addDottedDashedLine` utiliza las mismas coordenadas y configuraciones de guiones, pero también aplica `Color.getRed()`.

## Dibujar líneas a través de la página

1. Crear un nuevo PDF [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Agregar un [Página](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) al documento.
1. Crear un [Gráfica](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) contenedor y añádelo a la página.
1. Crea el [Línea](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/line/) forma y configura sus coordenadas.
1. Añade el [Línea](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/line/) al [Gráfica](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) contenedor.
1. Guardar el PDF de salida [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void drawLineAcrossPage(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        page.getPageInfo().getMargin().setLeft(0);
        page.getPageInfo().getMargin().setRight(0);
        page.getPageInfo().getMargin().setBottom(0);
        page.getPageInfo().getMargin().setTop(0);

        Graph graph = new Graph(page.getPageInfo().getWidth(), page.getPageInfo().getHeight());
        Line line = new Line(new float[]{
                (float) page.getRect().getLLX(),
                0,
                (float) page.getPageInfo().getWidth(),
                (float) page.getRect().getURY()
        });
        graph.getShapes().addItem(line);
        page.getParagraphs().add(graph);

        document.save(outputFile.toString());
    }
}
```
