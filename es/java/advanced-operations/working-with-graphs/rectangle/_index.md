---
title: Agregar formas rectangulares a PDF en Java
linktitle: Agregar rectángulo
type: docs
weight: 50
url: /java/add-rectangle/
description: Aprenda a dibujar y rellenar formas rectangulares en archivos PDF en Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Dibuje formas rectangulares en archivos PDF usando Java
Abstract: Este artículo muestra cómo agregar formas rectangulares a documentos PDF usando Aspose.PDF para Java. Cubre rectángulos delineados, rellenos sólidos, rellenos degradados, transparencia alfa y control de orden z para formas superpuestas.
---
## Agregar un contorno de rectángulo


1. Cree un nuevo [Documento] PDF (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. Agregue una [Página](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) al documento.

1. Cree un contenedor [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) y agréguelo a la página.

1. Crea la forma [Rectángulo](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/rectangle/) y configura su geometría.
1. Agregue el [Rectángulo](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/rectangle/) al contenedor [Gráfico](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/).

1. Guarde el [Documento] PDF de salida(https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).


```java
public static void addRectangle(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        Graph graph = new Graph(400.0, 300.0);
        page.getParagraphs().add(graph);
        graph.setBorder(new BorderInfo(BorderSide.All, Color.getRed()));

        Rectangle rectangle = new Rectangle(20, 20, 350, 250);
        graph.getShapes().addItem(rectangle);

        document.save(outputFile.toString());
    }
}
```

## 
Rellenar un rectángulo con color sólido o degradado



Los ejemplos de rectángulos incluyen:


- `createRectangleFilled` para un relleno sólido con `Color.getRed()`
- `addDrawingWithGradientFill` para un relleno `GradientAxialShading`


## 
Usar transparencia alfa



`createRectangleWithAlphaColorChannel` aplica colores translúcidos con `Color.fromArgb(...)` para que los rectángulos superpuestos permanezcan visibles.


## 
Controlar el orden z de los rectángulos


1. Cree un nuevo [Documento] PDF (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Agregue una [Página](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) al documento.

1. Establezca el tamaño de [Página](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) requerido.

1. Agregue las formas [Rectángulo](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/rectangle/) configuradas a la página de destino con el orden z requerido.

1. Guarde el [Documento] PDF de salida(https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void controlZOrderOfRectangle(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        page.setPageSize(375, 300);
        page.getPageInfo().getMargin().setLeft(0);
        page.getPageInfo().getMargin().setTop(0);

        addRectangleToPage(page, 50, 40, 60, 40, Color.getRed(), 2);
        addRectangleToPage(page, 20, 20, 30, 30, Color.getBlue(), 1);
        addRectangleToPage(page, 40, 40, 60, 30, Color.getGreen(), 0);

        document.save(outputFile.toString());
    }
}
```
