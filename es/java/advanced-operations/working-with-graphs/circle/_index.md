---
title: Agregar formas de círculo a PDF en Java
linktitle: Agregar círculo
type: docs
weight: 20
url: /es/java/add-circle/
description: Aprenda cómo dibujar y rellenar formas de círculo en archivos PDF en Java.
lastmod: "2026-09-03"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Dibujar formas de círculo en archivos PDF usando Java
Abstract: Este artículo muestra cómo agregar formas de círculo a documentos PDF usando Aspose.PDF for Java. Cubre cómo dibujar contornos de círculo, rellenar círculos con color y colocar texto dentro de una forma de círculo.
---
## Agregar un contorno de círculo

1. Crear un nuevo PDF [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Agregar un [Página](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) al documento.
1. Crear un [Gráfico](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) contenedor y agrégalo a la página.
1. Crear el [Círculo](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/circle/) forma y configura su geometría.
1. Agregar el [Círculo](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/circle/) al [Gráfico](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) contenedor.
1. Establezca las propiedades de forma requeridas por el ejemplo, incluyendo [Color](https://reference.aspose.com/pdf/java/com.aspose.pdf/color/).
1. Guarde el PDF de salida [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

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

## Agregar un círculo relleno con texto

1. Crear un nuevo PDF [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Agregar un [Página](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) al documento.
1. Crear un [Gráfico](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) contenedor y agrégalo a la página.
1. Crear el [Círculo](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/circle/) forma y configura su geometría.
1. Agregar el [Círculo](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/circle/) al [Gráfico](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) contenedor.
1. Establezca las propiedades de forma requeridas por el ejemplo, incluyendo [Color](https://reference.aspose.com/pdf/java/com.aspose.pdf/color/) y [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/).
1. Guarde el PDF de salida [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

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
