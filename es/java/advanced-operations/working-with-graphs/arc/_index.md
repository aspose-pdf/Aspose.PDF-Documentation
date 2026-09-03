---
title: Agregar formas de arco a PDF en Java
linktitle: Agregar arco
type: docs
weight: 10
url: /java/add-arc/
description: Aprenda a dibujar y rellenar formas de arco en archivos PDF en Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Dibuje formas de arco en archivos PDF usando Java
Abstract: Este artículo muestra cómo agregar formas de arco a documentos PDF usando Aspose.PDF para Java. Cubre dibujar múltiples arcos delineados con diferentes colores y crear un segmento de arco relleno combinando un arco con una línea de cierre.
---
Aspose.PDF para Java utiliza `Graph` junto con objetos de forma como `Arc` y `Line` para representar gráficos vectoriales.


## 
Agregar contornos de arco


1. Cree un nuevo [Documento] PDF (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. Agregue una [Página](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) al documento.

1. Cree un contenedor [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) y agréguelo a la página.
1. Crea la forma [Arco](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/arc/) y configura su geometría.

1. Agregue el [Arco](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/arc/) al contenedor [Gráfico](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/).

1. Establezca las propiedades de forma requeridas por el ejemplo, incluido [Color](https://reference.aspose.com/pdf/java/com.aspose.pdf/color/).

1. Guarde el [Documento] PDF de salida(https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).


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


1. Cree un nuevo [Documento] PDF (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. Agregue una [Página](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) al documento.

1. Cree un contenedor [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) y agréguelo a la página.

1. Crea la forma [Línea](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/line/) y configura sus coordenadas.
1. Crea la forma [Arco](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/arc/) y configura su geometría.

1. Agregue la [Línea](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/line/) y el [Arco](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/arc/) al contenedor [Gráfico](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/).

1. Guarde el [Documento] PDF de salida(https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

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
