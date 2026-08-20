---
title: Agregar formas circulares a PDF en Java
linktitle: Agregar círculo
type: docs
weight: 20
url: /java/add-circle/
description: Aprenda a dibujar y rellenar formas circulares en archivos PDF en Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Dibuje formas circulares en archivos PDF usando Java
Abstract: Este artículo muestra cómo agregar formas circulares a documentos PDF usando Aspose.PDF para Java. Cubre dibujar contornos de círculos, rellenar círculos con color y colocar texto dentro de una forma de círculo.
---
## Agregar un contorno circular


1. 
Cree un nuevo [Documento] PDF (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Agregue una [Página](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) al documento.

1. 
Cree un contenedor [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) y agréguelo a la página.

1. 
Crea la forma [Círculo](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/circle/) y configura su geometría.
1. Agregue el [Círculo](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/circle/) al contenedor [Gráfico](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/).

1. 
Establezca las propiedades de forma requeridas por el ejemplo, incluido [Color](https://reference.aspose.com/pdf/java/com.aspose.pdf/color/).

1. 
Guarde el [Documento] PDF de salida(https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).


```java
public static void addCircle(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        Graph graph = new Graph(400.0, 200.0);
        graph.setBorder(new BorderInfo(BorderSide.All, Color.getGreen()));

        Circle circle = new Circle(100, 100, 40);
        circle.getGraphInfo().setColor(Color.getGreenYellow());
        graph.getShapes().addItem(circle);

        page.getParagraphs().add(graph);
        document.save(outputFile.toString());
    }
}
```

## 
Añade un círculo relleno con texto.


1. 
Cree un nuevo [Documento] PDF (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Agregue una [Página](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) al documento.

1. 
Cree un contenedor [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) y agréguelo a la página.

1. 
Crea la forma [Círculo](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/circle/) y configura su geometría.

1. 
Agregue el [Círculo](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/circle/) al contenedor [Gráfico](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/).

1. 
Establezca las propiedades de forma requeridas por el ejemplo, incluidos [Color](https://reference.aspose.com/pdf/java/com.aspose.pdf/color/) y [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/).
1. Guarde el [Documento] PDF de salida(https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void addCircleFilled(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        Graph graph = new Graph(400.0, 200.0);
        graph.setBorder(new BorderInfo(BorderSide.All, Color.getGreen()));

        Circle circle = new Circle(100, 100, 40);
        circle.getGraphInfo().setColor(Color.getGreenYellow());
        circle.getGraphInfo().setFillColor(Color.getGreen());
        circle.setText(new TextFragment("Circle"));
        graph.getShapes().addItem(circle);

        page.getParagraphs().add(graph);
        document.save(outputFile.toString());
    }
}
```
