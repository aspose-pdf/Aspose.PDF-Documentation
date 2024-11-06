---
title: Añadir Objeto Rectángulo al archivo PDF
linktitle: Añadir Rectángulo
type: docs
weight: 50
url: es/java/add-rectangle/
description: Este artículo explica cómo crear un objeto Rectángulo en tu PDF utilizando Aspose.PDF para Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Añadir objeto Rectángulo

Aspose.PDF para Java admite la función de agregar objetos gráficos (por ejemplo gráfico, línea, rectángulo, etc.) a documentos PDF. También tienes la ventaja de agregar un objeto [Rectángulo](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/Rectangle) donde también se ofrece la función de llenar el objeto rectángulo con un cierto color, controlar el orden Z, agregar relleno de color degradado, etc.

Primero, veamos la posibilidad de crear un objeto Rectángulo.

Sigue los pasos a continuación:

1. Crea un nuevo [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) PDF

1. Agrega una [Página](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) a la colección de páginas del archivo PDF

1. Agregar [Fragmento de texto](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragment) a la colección de párrafos de la instancia de la página

1. Crear una instancia de [Gráfico](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/Graph)

1. Establecer borde para el [Objeto de Dibujo](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/package-frame)

1. Crear instancia de Rectángulo

1. Agregar el objeto [Rectángulo](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/Rectangle) a la colección de formas del objeto Gráfico

1. Agregar objeto gráfico a la colección de párrafos de la instancia de la página

1. Agregar [Fragmento de texto](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragment) a la colección de párrafos de la instancia de la página

1. Y guardar tu archivo PDF

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.BorderInfo;
import com.aspose.pdf.BorderSide;
import com.aspose.pdf.Color;
import com.aspose.pdf.Document;
import com.aspose.pdf.Page;
import com.aspose.pdf.Point;
import com.aspose.pdf.TextFragment;
import com.aspose.pdf.drawing.*;

public class WorkingWithGraphs {

    private static String _dataDir = "/home/aspose/pdf-examples/Samples/";

    public static void ExampleRectangle() {

        // Crear un nuevo documento PDF
        Document pdfDocument = new Document();

        // Agregar una página a la colección de páginas del archivo PDF
        Page page = pdfDocument.getPages().add();

        // Agregar fragmento de texto a la colección de párrafos de la instancia de la página
        page.getParagraphs().add(new TextFragment("Texto antes del objeto Gráfico"));

        // Crear instancia de Gráfico
        Graph graph = new Graph(400, 200);

        // Establecer borde para el objeto de Dibujo
        BorderInfo borderInfo = new BorderInfo(BorderSide.All, Color.getRed());
        graph.setBorder(borderInfo);

        // Crear instancia de Rectángulo
        Rectangle rect = new Rectangle(10, 10, 380, 180);

        // Agregar objeto rectángulo a la colección de formas del objeto Gráfico
        graph.getShapes().add(rect);

        // Agregar objeto gráfico a la colección de párrafos de la instancia de la página
        page.getParagraphs().add(graph);

        // Agregar fragmento de texto a la colección de párrafos de la instancia de la página
        page.getParagraphs().add(new TextFragment("Texto después del objeto Gráfico"));

        // Guardar archivo PDF
        pdfDocument.save(_dataDir + "CreateRectangle_out.pdf");
    }
```


![Create Rectangle](create_rectangle.png)

## Crear Objeto Rectángulo Relleno

Aspose.PDF para Java también ofrece la función de llenar un objeto rectángulo con un cierto color.

El siguiente fragmento de código muestra cómo agregar un objeto [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/Rectangle) que está lleno de color.

```java
   public static void ExampleRectangleFilledSolidColor() {

        Document pdfDocument = new Document();

        // Agregar página a la colección de páginas del archivo PDF
        Page page = pdfDocument.getPages().add();
        // Crear instancia de Graph
        Graph graph = new Graph(100, 400);

        // Agregar objeto gráfico a la colección de párrafos de la instancia de página
        page.getParagraphs().add(graph);

        // Crear instancia de Rectangle
        Rectangle rect = new Rectangle(100, 100, 200, 120);

        // Especificar el color de relleno para el objeto Graph
        rect.getGraphInfo().setFillColor(Color.getRed());

        // Agregar objeto rectángulo a la colección de formas del objeto Graph
        graph.getShapes().add(rect);

        // Guardar el archivo PDF
        pdfDocument.save(_dataDir + "CreateFilledRectangle_out.pdf");
    }
```


Mira el resultado del rectángulo relleno de color sólido:

![Rectángulo Relleno](fill_rectangle.png)

## Agregar Dibujo con Relleno Degradado

Aspose.PDF para Java admite la característica de agregar objetos de gráfico a documentos PDF y, a veces, es necesario rellenar objetos de gráfico con Color Degradado. Para rellenar objetos de gráfico con Color Degradado, necesitamos establecer setPatterColorSpace con el objeto gradientAxialShading de la siguiente manera.

El siguiente fragmento de código muestra cómo agregar un objeto [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/Rectangle) que se rellena con Color Degradado.

```java
   public static void ExampleRectangleFilledGradient() {

        Document pdfDocument = new Document();
        Page page = pdfDocument.getPages().add();

        Graph graph = new Graph(300, 300);
        page.getParagraphs().add(graph);
        Rectangle rect = new Rectangle(0, 0, 300, 300);
        graph.getShapes().add(rect);

        // Especificar color de relleno degradado para el objeto Graph y rellenar
        Color gradientFill = new com.aspose.pdf.Color();
        rect.getGraphInfo().setFillColor(gradientFill);

        GradientAxialShading gradientAxialShading = new GradientAxialShading(Color.getRed(), Color.getBlue());

        gradientAxialShading.setStart(new Point(0, 0));
        gradientAxialShading.setEnd(new Point(300, 300));
        gradientFill.setPatternColorSpace(gradientAxialShading);

        // Guardar archivo PDF
        pdfDocument.save(_dataDir + "AddDrawingWithGradientFill_out.pdf");
    }
```


![Gradient Rectangle](gradient.png)

## Crear Rectángulo con Canal de Color Alfa

Aspose.PDF para Java admite llenar un objeto rectángulo con un cierto color. Un objeto rectángulo también puede tener un canal de color Alfa para darle una apariencia transparente. El siguiente fragmento de código muestra cómo agregar un objeto [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/Rectangle) con canal de color Alfa.

Los píxeles de la imagen pueden almacenar información sobre su opacidad junto con el valor del color. Esto permite crear imágenes con áreas transparentes o semitransparentes.

En lugar de hacer un color transparente, cada píxel almacena información sobre cuán opaco es. Estos datos de opacidad se llaman canal alfa y generalmente se almacenan después de los canales de color del píxel.

En nuestro fragmento de código usamos el método [fromArgb](https://reference.aspose.com/pdf/java/com.aspose.pdf/Color#fromArgb-int-int-int-) de [com.aspose.pdf.Color](https://reference.aspose.com/pdf/java/com.aspose.pdf/Color).
 Necesitamos especificar valores donde los primeros 3 son componentes de color, especificados en el rango de 0 a 255, y el último es el nivel de opacidad (canal alfa), especificado por números fraccionarios de 0 a 1.

```java
    public static void ExampleRectangleAlphaChannelColor() {
        Document pdfDocument = new Document();
        Page page = pdfDocument.getPages().add();

        // Crear instancia de Graph
        Graph graph = new Graph(100, 400);

        // Crear objeto rectángulo con dimensiones específicas
        Rectangle rect1 = new Rectangle(100, 100, 200, 100);
        Color color1 = Color.fromArgb(128, 224, 0, 224);
        rect1.getGraphInfo().setFillColor(color1);
        // Agregar objeto rectángulo a la colección de formas de la instancia de Graph
        graph.getShapes().add(rect1);

        // Crear segundo objeto rectángulo
        Rectangle rect2 = new Rectangle(200, 150, 200, 100);
        Color color2 = Color.fromArgb(64, 0, 224, 224);
        rect2.getGraphInfo().setFillColor(color2);
        graph.getShapes().add(rect2);

        // Agregar instancia de graph a la colección de párrafos del objeto página
        page.getParagraphs().add(graph);

        // Guardar archivo PDF
        pdfDocument.save(_dataDir + "CreateRectangleWithAlphaColor_out.pdf");
    }
```

![Rectangle Alpha Channel Color](rectangle_color.png)

## Controlar el Orden Z de un Rectángulo

Aspose.PDF para Java admite la función de agregar objetos gráficos (por ejemplo, gráfico, línea, rectángulo, etc.) a documentos PDF. Al agregar más de una instancia del mismo objeto dentro del archivo PDF, podemos controlar su renderizado especificando el Orden Z. El Orden Z también se utiliza cuando necesitamos renderizar objetos uno encima del otro.

El siguiente fragmento de código muestra los pasos para renderizar objetos [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/Rectangle) uno encima del otro.

```java
   public static void Controlling_Z_Order() {

        Document pdfDocument = new Document();
        Page page = pdfDocument.getPages().add();

        // Crear un nuevo rectángulo con Color Rojo, Orden Z como 0 y ciertas dimensiones
        AddRectangle(page, 50, 40, 60, 40, Color.getRed(), 2);
        // Crear un nuevo rectángulo con Color Azul, Orden Z como 0 y ciertas
        // dimensiones
        AddRectangle(page, 20, 20, 30, 30, Color.getBlue(), 1);
        // Crear un nuevo rectángulo con Color Verde, Orden Z como 0 y ciertas
        // dimensiones
        AddRectangle(page, 40, 40, 60, 30, Color.getGreen(), 0);

        // Guardar el archivo PDF resultante
        pdfDocument.save(_dataDir + "ControlRectangleZOrder_out.pdf");

    }
```


![Controlando el Orden Z](control.png)