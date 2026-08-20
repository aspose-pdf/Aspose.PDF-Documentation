---
title: Agregar formas de elipse a PDF en Java
linktitle: Agregar elipse
type: docs
weight: 60
url: /java/add-ellipse/
description: Aprenda a dibujar, rellenar y etiquetar formas de elipses en archivos PDF en Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Dibuje formas de elipse en archivos PDF usando Java
Abstract: Este artículo muestra cómo agregar formas de elipse a documentos PDF usando Aspose.PDF para Java. Cubre elipses delineadas, elipses rellenas y colocación de fragmentos de texto dentro de formas de elipses.
---
## Agregar contornos de elipse


1. 
Cree un nuevo [Documento] PDF (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Agregue una [Página](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) al documento.

1. 
Cree un contenedor [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) y agréguelo a la página.

1. 
Crea la forma [Elipse](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/ellipse/) y configura su geometría.
1. Agregue la [Elipse](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/ellipse/) al contenedor [Gráfico](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/).

1. 
Establezca las propiedades de forma requeridas por el ejemplo, incluidos [Color](https://reference.aspose.com/pdf/java/com.aspose.pdf/color/) y [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/).

1. 
Guarde el [Documento] PDF de salida(https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).


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


## 
Agregar elipses rellenas

`createEllipseFilled` llena dos elipses con `Color.getGreenYellow()` y `Color.getDarkRed()`.


## 
Agregar texto dentro de elipses


1. 
Cree un nuevo [Documento] PDF (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Agregue una [Página](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) al documento.

1. 
Cree un [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/) y configure las opciones de formato de texto requeridas.
1. Cree un contenedor [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) y agréguelo a la página.

1. 
Crea la forma [Elipse](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/ellipse/) y configura su geometría.

1. 
Agregue la [Elipse](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/ellipse/) al contenedor [Gráfico](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/).

1. 
Guarde el [Documento] PDF de salida(https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

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
