---
title: Agregar formas de curvas a PDF en Java
linktitle: Agregar curva
type: docs
weight: 30
url: /java/add-curve/
description: Aprenda a dibujar y rellenar formas curvas en archivos PDF en Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Dibuje formas curvas en archivos PDF usando Java
Abstract: Este artículo muestra cómo agregar formas curvas a documentos PDF usando Aspose.PDF para Java. Cubre la creación de una curva a partir de matrices de coordenadas y la aplicación de color de trazo o color de relleno dentro de un contenedor de gráficos.
---
Las curvas en Aspose.PDF para Java se definen mediante una matriz de coordenadas flotantes pasada a `Curve`.


## 
Agregar un contorno de curva


1. 
Cree un nuevo [Documento] PDF (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Agregue una [Página](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) al documento.

1. 
Cree un contenedor [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) y agréguelo a la página.
1. Cree la forma [Curva](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/curve/) y configure sus puntos de control.

1. 
Agregue la [Curva](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/curve/) al contenedor [Gráfico](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/).

1. 
Establezca las propiedades de forma requeridas por el ejemplo, incluido [Color](https://reference.aspose.com/pdf/java/com.aspose.pdf/color/).

1. 
Guarde el [Documento] PDF de salida(https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

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
