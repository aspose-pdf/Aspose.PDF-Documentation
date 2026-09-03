---
title: Agregar formas de rectángulo a PDF en Java
linktitle: Agregar rectángulo
type: docs
weight: 50
url: /es/java/add-rectangle/
description: Aprenda cómo dibujar y rellenar formas de rectángulo en archivos PDF con Java.
lastmod: "2026-09-03"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Dibujar formas de rectángulo en archivos PDF usando Java
Abstract: Este artículo muestra cómo agregar formas de rectángulo a documentos PDF usando Aspose.PDF for Java. Incluye rectángulos contorneados, rellenos sólidos, rellenos degradados, transparencia alfa y control de orden z para formas superpuestas.
---
## Agregar contorno de rectángulo

1. Crear un nuevo PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Agregar un [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) al documento.
1. Crear un [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) contenedor y agrégalo a la página.
1. Crear el [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/rectangle/) forma y configura su geometría.
1. Agregar el [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/rectangle/) al [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) contenedor.
1. Guardar el PDF de salida [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

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

## Rellena un rectángulo con color sólido o degradado

Los ejemplos de rectángulo incluyen:

- `createRectangleFilled` para un relleno sólido con `Color.getRed()`
- `addDrawingWithGradientFill` para un `GradientAxialShading` llenar

## Usa transparencia alfa

`createRectangleWithAlphaColorChannel` aplica colores translúcidos con `Color.fromArgb(...)` para que los rectángulos superpuestos permanezcan visibles.

## Controlar el orden z de los rectángulos

1. Crear un nuevo PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Agregar un [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) al documento.
1. Establecer lo requerido [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) tamaño.
1. Agregar lo configurado [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/rectangle/) formas a la página de destino con el orden z requerido.
1. Guardar el PDF de salida [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

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
