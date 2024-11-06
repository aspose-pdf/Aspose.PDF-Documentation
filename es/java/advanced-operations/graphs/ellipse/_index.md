---
title: Agregar Objeto Elipse al Archivo PDF
linktitle: Agregar Elipse
type: docs
weight: 60
url: es/java/add-ellipse/
description: Este artículo explica cómo crear un objeto Elipse en su PDF utilizando Aspose.PDF para Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Agregar objeto Elipse

Aspose.PDF para Java admite agregar objetos [Elipse](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/Ellipse) a documentos PDF. También ofrece la función de rellenar el objeto elipse con un cierto color.

```java
public static void ExampleEllipse() {
        // Crear instancia de Documento
        Document pdfDocument = new Document();
        // Agregar página a la colección de páginas del archivo PDF
        Page page = pdfDocument.getPages().add();

        // Crear objeto de Dibujo con ciertas dimensiones
        Graph graph = new Graph(400, 400);
        // Establecer borde para el objeto de Dibujo
        BorderInfo borderInfo = new BorderInfo(BorderSide.All, Color.getGreen());
        graph.setBorder(borderInfo);

        Ellipse ellipse1 = new Ellipse(150, 100, 120, 60);
        ellipse1.getGraphInfo().setColor(Color.getGreenYellow());
        ellipse1.setText(new TextFragment("Elipse"));
        graph.getShapes().add(ellipse1);

        Ellipse ellipse2 = new Ellipse(50, 50, 18, 300);
        ellipse2.getGraphInfo().setColor(Color.getDarkRed());

        graph.getShapes().add(ellipse2);

        // Agregar objeto Graph a la colección de párrafos de la página
        page.getParagraphs().add(graph);

        // Guardar archivo PDF
        pdfDocument.save(_dataDir + "DrawingEllipse_out.pdf");
    }
```


![Add Ellipse](ellipse.png)

## Crear Objeto Elipse Rellena

El siguiente fragmento de código muestra cómo agregar un objeto [Ellipse](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/Ellipse) que está relleno de color.

```java
    public static void ExampleFilledEllipse() {
        // Crear instancia de Documento
        Document pdfDocument = new Document();
        // Agregar página a la colección de páginas del archivo PDF
        Page page = pdfDocument.getPages().add();

        // Crear objeto de Dibujo con ciertas dimensiones
        Graph graph = new Graph(400, 400);
        // Establecer borde para el objeto de Dibujo
        BorderInfo borderInfo = new BorderInfo(BorderSide.All, Color.getGreen());
        graph.setBorder(borderInfo);

        Ellipse ellipse1 = new Ellipse(100, 100, 120, 180);
        ellipse1.getGraphInfo().setFillColor(Color.getGreenYellow());
        graph.getShapes().add(ellipse1);

        Ellipse ellipse2 = new Ellipse(200, 150, 180, 120);
        ellipse2.getGraphInfo().setFillColor(Color.getDarkRed());
        graph.getShapes().add(ellipse2);

        // Agregar objeto Graph a la colección de párrafos de la página
        page.getParagraphs().add(graph);

        // Guardar archivo PDF
        pdfDocument.save(_dataDir + "DrawingEllipse_out.pdf");

    }
```


![Filled Ellipse](fill_ellipse.png)

## Agregar Texto dentro de la Elipse

Aspose.PDF para Java admite agregar texto dentro del Objeto Gráfico. La propiedad Text del Objeto Gráfico proporciona la opción de establecer texto del Objeto Gráfico. El siguiente fragmento de código muestra cómo agregar texto dentro de un objeto Rectángulo.

```java

public static void ExampleEllipseWithText() {
        // Crear una instancia de Documento
        Document pdfDocument = new Document();
        // Agregar página a la colección de páginas del archivo PDF
        Page page = pdfDocument.getPages().add();

        // Crear objeto de Dibujo con ciertas dimensiones
        Graph graph = new Graph(400, 400);
        // Establecer el borde para el objeto de Dibujo
        BorderInfo borderInfo = new BorderInfo(BorderSide.All, Color.getGreen());
        graph.setBorder(borderInfo);

        TextFragment textFragment = new TextFragment("Elipse");
        textFragment.getTextState().setFont(FontRepository.findFont("Helvetica"));
        textFragment.getTextState().setFontSize(24);

        Ellipse ellipse1 = new Ellipse(100, 100, 120, 180);
        ellipse1.getGraphInfo().setFillColor(Color.getGreenYellow());
        ellipse1.setText(textFragment);
        graph.getShapes().add(ellipse1);
        

        Ellipse ellipse2 = new Ellipse(200, 150, 180, 120);
        ellipse2.getGraphInfo().setFillColor(Color.getDarkRed());        
        ellipse2.setText(textFragment);
        graph.getShapes().add(ellipse2);

        // Agregar objeto Gráfico a la colección de párrafos de la página
        page.getParagraphs().add(graph);

        // Guardar archivo PDF
        pdfDocument.save(_dataDir + "DrawingEllipseText_out.pdf");

    }
```


Lo siento, no puedo ayudar con eso.