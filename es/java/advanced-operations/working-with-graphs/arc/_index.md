---
title: Agregar formas de arco a PDF en Java
linktitle: Agregar arco
type: docs
weight: 10
url: /es/java/add-arc/
description: Aprende cómo dibujar y rellenar formas de arco en archivos PDF con Java.
lastmod: "2026-09-29"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Dibujar formas de arco en archivos PDF usando Java
Abstract: Este artículo muestra cómo agregar formas de arco a documentos PDF usando Aspose.PDF for Java. Cubre el dibujo de múltiples arcos contorneados con diferentes colores y la creación de un segmento de arco relleno combinando un arco con una línea de cierre.
---
Aspose.PDF for Java utiliza `Graph` junto con objetos de forma como `Arc` y `Line` para renderizar gráficos vectoriales.

## Agregar contornos de arco

1. Cree un nuevo PDF [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Agregue un [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) al documento.
1. Cree un [`Graph`](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) contenedor y añádalo a la página.
1. Cree el [`Arc`](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/arc/) forma y configure su geometría.
1. Agregue el [`Arc`](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/arc/) al [`Graph`](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) contenedor.
1. Establezca las propiedades de forma requeridas por el ejemplo, incluyendo [`Color`](https://reference.aspose.com/pdf/java/com.aspose.pdf/color/).
1. Guarde el PDF de salida [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void addArc(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        Graph graph = new Graph(400.0, 400.0);
        graph.setBorder(new BorderInfo(BorderSide.All, Color.getGreen()));

        Arc arc1 = new Arc(100, 100, 95, 0, 90);
        arc1.getGraphInfo().setColor(Color.getGreenYellow());
        graph.getShapes().addItem(arc1);

        page.getParagraphs().add(graph);
        document.save(outputFile.toString());
    }
}
```

El ejemplo completo agrega tres arcos con diferentes radios, ángulos y colores al mismo gráfico.

## Agregar un segmento de arco relleno

1. Cree un nuevo PDF [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Agregue un [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) al documento.
1. Cree un [`Graph`](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) contenedor y añádalo a la página.
1. Cree el [`Line`](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/line/) forma y configure sus coordenadas.
1. Cree el [`Arc`](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/arc/) forma y configure su geometría.
1. Agregue el [`Line`](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/line/) y [`Arc`](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/arc/) al [`Graph`](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) contenedor.
1. Guarde el PDF de salida [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void addArcFilled(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        Graph graph = new Graph(400.0, 400.0);
        graph.setBorder(new BorderInfo(BorderSide.All, Color.getGreen()));

        Arc arc = new Arc(100, 100, 95, 0, 90);
        arc.getGraphInfo().setFillColor(Color.getGreenYellow());
        graph.getShapes().addItem(arc);

        Line line = new Line(new float[]{195, 100, 100, 100, 100, 195});
        line.getGraphInfo().setFillColor(Color.getGreenYellow());
        graph.getShapes().addItem(line);

        page.getParagraphs().add(graph);
        document.save(outputFile.toString());
    }
}
```
