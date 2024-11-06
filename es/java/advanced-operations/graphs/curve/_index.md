---
title: Agregar Objeto de Curva al Archivo PDF
linktitle: Agregar Curva
type: docs
weight: 30
url: es/java/add-curve/
description: Este artículo explica cómo crear un objeto de curva en su PDF utilizando Aspose.PDF para Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Agregar objeto de Curva

Un gráfico [Curva](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/Curve) es una unión conectada de líneas proyectivas, cada línea se encuentra con otras tres en puntos dobles ordinarios.

Aspose.PDF para Java muestra cómo usar curvas de Bézier en sus gráficos.
Las curvas de Bézier se utilizan ampliamente en gráficos por computadora para modelar curvas suaves. La curva está completamente contenida en el casco convexo de sus puntos de control, los puntos pueden mostrarse gráficamente y utilizarse para manipular la curva de manera intuitiva.
Toda la curva está contenida en el cuadrilátero cuyos vértices son los cuatro puntos dados (su casco convexo).

En este artículo, investigaremos simplemente curvas gráficas y curvas rellenas que puede crear en su documento PDF.

Sigue los pasos a continuación:

1. Crear una instancia de [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

1. Crear un [objeto de Dibujo](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/package-frame) con ciertas dimensiones.

1. Establecer [Borde](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/Graph#setBorder-com.aspose.pdf.BorderInfo-) para el objeto de Dibujo.

1. Agregar el objeto [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/Graph) a la colección de párrafos de la página.

1. Guardar tu archivo PDF

```java
    public static void ExampleCurve() {
        // Crear instancia de Documento
        Document pdfDocument = new Document();
        // Agregar página a la colección de páginas del archivo PDF
        Page page = pdfDocument.getPages().add();

        // Crear objeto de Dibujo con ciertas dimensiones
        Graph graph = new Graph(400, 200);
        // Establecer borde para el objeto de Dibujo
        BorderInfo borderInfo = new BorderInfo(BorderSide.All, Color.getGreen());
        graph.setBorder(borderInfo);

        Curve curve1 = new Curve(new float[] { 10, 10, 50, 60, 70, 10, 100, 120});

        curve1.getGraphInfo().setColor(Color.getGreenYellow());
        graph.getShapes().add(curve1);

        // Agregar el objeto Graph a la colección de párrafos de la página
        page.getParagraphs().add(graph);

        // Guardar archivo PDF
        pdfDocument.save(_dataDir + "DrawingCurve1_out.pdf");
    }
```


La siguiente imagen muestra el resultado ejecutado con nuestro fragmento de código:

![Dibujo de Curva](drawing_curve.png)

## Crear Objeto de Curva Relleno

Este ejemplo muestra cómo agregar un objeto Curve que está relleno con color.

```java
    public static void ExampleFilledCurve() {
        // Crear instancia de Documento
        Document pdfDocument = new Document();
        // Agregar página a la colección de páginas del archivo PDF
        Page page = pdfDocument.getPages().add();

        // Crear objeto de Dibujo con ciertas dimensiones
        Graph graph = new Graph(400, 200);
        // Establecer borde para el objeto de Dibujo
        BorderInfo borderInfo = new BorderInfo(BorderSide.All, Color.getGreen());
        graph.setBorder(borderInfo);

        Curve curve1 = new Curve(new float[] { 10, 10, 50, 60, 70, 10, 100, 120});
        curve1.getGraphInfo().setFillColor(Color.getGreenYellow());
        graph.getShapes().add(curve1);

        // Agregar objeto Graph a la colección de párrafos de la página
        page.getParagraphs().add(graph);

        // Guardar archivo PDF
        pdfDocument.save(_dataDir + "DrawingCurve2_out.pdf");
    }
```


Mira el resultado de añadir una Curva Rellena:

![Curva Rellena](filled_curve.png)