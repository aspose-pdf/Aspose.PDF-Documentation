---
title: Agregar formas de curva a PDF en Java
linktitle: Agregar curva
type: docs
weight: 30
url: /es/java/add-curve/
description: Aprenda cómo dibujar y rellenar formas de curva en archivos PDF en Java.
lastmod: "2026-09-03"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Dibujar formas de curva en archivos PDF usando Java
Abstract: Este artículo muestra cómo agregar formas de curva a documentos PDF usando Aspose.PDF for Java. Cubre la creación de una curva a partir de matrices de coordenadas y la aplicación de color de trazo o color de relleno dentro de un contenedor Graph.
---
Las curvas en Aspose.PDF for Java se definen mediante una matriz de coordenadas float que se pasa a `Curve`.

## Agregar un contorno de curva

1. Crear un nuevo PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Agregar un [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) al documento.
1. Crear un [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) contenedor y agréguelo a la página.
1. Crear el [Curve](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/curve/) forma y configure sus puntos de control.
1. Agregar el [Curve](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/curve/) al [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) contenedor.
1. Establezca las propiedades de forma requeridas por el ejemplo, incluyendo [Color](https://reference.aspose.com/pdf/java/com.aspose.pdf/color/).
1. Guarde el PDF de salida [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void addCurve(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        Graph graph = new Graph(400.0, 200.0);
        graph.setBorder(new BorderInfo(BorderSide.All, Color.getGreen()));

        Curve curve1 = new Curve(new float[]{10, 10, 50, 60, 70, 10, 100, 120});
        curve1.getGraphInfo().setColor(Color.getGreenYellow());
        graph.getShapes().addItem(curve1);

        page.getParagraphs().add(graph);
        document.save(outputFile.toString());
    }
}
```
