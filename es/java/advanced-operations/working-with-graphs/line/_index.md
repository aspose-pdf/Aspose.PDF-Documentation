---
title: Agregar formas de línea a PDF en Java
linktitle: Agregar línea
type: docs
weight: 40
url: /java/add-line/
description: Aprenda a dibujar formas de líneas y líneas con estilo en archivos PDF en Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Dibuje formas de líneas en archivos PDF usando Java
Abstract: Este artículo muestra cómo agregar formas de líneas a documentos PDF usando Aspose.PDF para Java. Cubre la creación de líneas a partir de matrices de coordenadas, la aplicación de estilos y colores discontinuos y el dibujo de líneas en toda el área de la página.
---
## Añade una línea discontinua


1. 
Cree un nuevo [Documento] PDF (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Agregue una [Página](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) al documento.

1. 
Cree un contenedor [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) y agréguelo a la página.

1. 
Crea la forma [Línea](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/line/) y configura sus coordenadas.
1. Agregue la [Línea](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/line/) al contenedor [Gráfico](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/).

1. 
Guarde el [Documento] PDF de salida(https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).


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

## 
Añade una línea punteada o discontinua de color



`addDottedDashedLine` usa las mismas coordenadas y configuración de guión, pero también aplica `Color.getRed()`.


## 
Dibuja líneas a lo largo de la página.

1. Cree un nuevo [Documento] PDF (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Agregue una [Página](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) al documento.

1. 
Cree un contenedor [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) y agréguelo a la página.

1. 
Crea la forma [Línea](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/line/) y configura sus coordenadas.

1. 
Agregue la [Línea](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/line/) al contenedor [Gráfico](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/).
1. Guarde el [Documento] PDF de salida(https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

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
