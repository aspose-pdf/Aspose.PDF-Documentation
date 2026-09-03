---
title: Agregar formas de elipse al PDF en Java
linktitle: Agregar elipse
type: docs
weight: 60
url: /es/java/add-ellipse/
description: Aprenda cómo dibujar, rellenar y etiquetar formas de elipse en archivos PDF en Java.
lastmod: "2026-09-03"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Dibujar formas de elipse en archivos PDF usando Java
Abstract: Este artículo muestra cómo agregar formas de elipse a documentos PDF usando Aspose.PDF for Java. Cubre elipses con contorno, elipses rellenas y la colocación de fragmentos de texto dentro de formas de elipse.
---
## Agregar contornos de elipse

1. Crear un nuevo PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Agregar un [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) al documento.
1. Crear un [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) contenedor y añádelo a la página.
1. Crear el [Ellipse](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/ellipse/) forma y configura su geometría.
1. Añadir el [Ellipse](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/ellipse/) al [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) contenedor.
1. Establezca las propiedades de forma requeridas por el ejemplo, incluyendo [Color](https://reference.aspose.com/pdf/java/com.aspose.pdf/color/) y [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/).
1. Guardar el PDF de salida [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void addEllipse(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        Graph graph = new Graph(400.0, 400.0);
        graph.setBorder(new BorderInfo(BorderSide.All, Color.getGreen()));

        Ellipse ellipse1 = new Ellipse(150, 100, 120, 60);
        ellipse1.getGraphInfo().setColor(Color.getGreenYellow());
        ellipse1.setText(new TextFragment("Ellipse"));
        graph.getShapes().addItem(ellipse1);

        page.getParagraphs().add(graph);
        document.save(outputFile.toString());
    }
}
```

El ejemplo completo agrega dos elipses de contorno diferentes al mismo gráfico.

## Agregar elipses rellenas

`createEllipseFilled` rellena dos elipsis con `Color.getGreenYellow()` y `Color.getDarkRed()`.

## Agregar texto dentro de las elipses

1. Crear un nuevo PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Agregar un [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) al documento.
1. Crear un [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/) y establecer las opciones de formato de texto requeridas.
1. Crear un [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) contenedor y añádelo a la página.
1. Crear el [Ellipse](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/ellipse/) forma y configura su geometría.
1. Añadir el [Ellipse](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/ellipse/) al [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) contenedor.
1. Guardar el PDF de salida [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void addTextInsideEllipse(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        Graph graph = new Graph(400.0, 400.0);
        graph.setBorder(new BorderInfo(BorderSide.All, Color.getGreen()));

        TextFragment textFragment = new TextFragment("Ellipse");
        textFragment.getTextState().setFont(FontRepository.findFont("Helvetica"));
        textFragment.getTextState().setFontSize(24);

        Ellipse ellipse1 = new Ellipse(100, 100, 120, 180);
        ellipse1.getGraphInfo().setFillColor(Color.getGreenYellow());
        ellipse1.setText(textFragment);
        graph.getShapes().addItem(ellipse1);

        page.getParagraphs().add(graph);
        document.save(outputFile.toString());
    }
}
```
