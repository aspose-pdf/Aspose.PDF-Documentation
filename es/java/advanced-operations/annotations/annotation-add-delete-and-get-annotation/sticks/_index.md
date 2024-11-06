---
title: Anotaciones Adhesivas en PDF
linktitle: Anotación Adhesiva
type: docs
weight: 50
url: es/java/sticky-annotations/
description: Este tema trata sobre las anotaciones adhesivas, como ejemplo mostramos la Anotación de Marca de Agua en el texto. Se utiliza para representar gráficos en la página. Consulte el fragmento de código para resolver esta tarea.
lastmod: "2021-11-24"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Añadir Anotación de Marca de Agua

Se debe utilizar una anotación de marca de agua para representar gráficos que se imprimirán en un tamaño y posición fijos en una página, independientemente de las dimensiones de la página impresa.

Puede agregar Texto de Marca de Agua utilizando [WatermarkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/WatermarkAnnotation) en una posición específica de la página PDF. La opacidad de la Marca de Agua también puede controlarse utilizando la propiedad de opacidad.

Por favor, consulte el siguiente fragmento de código para agregar WatermarkAnnotation.

```java
 package com.aspose.pdf.examples;

import com.aspose.pdf.*;
import java.util.*;

public class ExampleWatermarkAnnotation {

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void AddWaterMarkAnnotation()
    {
        // Cargar el archivo PDF
        Document document = new Document(_dataDir + "sample.pdf");
        Page page = document.getPages().get_Item(1);

        //Crear Anotación
        WatermarkAnnotation wa = new WatermarkAnnotation(page, new Rectangle(100, 500, 400, 600));

        //Añadir anotación a la colección de Anotaciones de la Página
        page.getAnnotations().add(wa);

        //Crear TextState para la configuración de la Fuente
        TextState ts = new TextState();

        ts.setForegroundColor(Color.getBlue());
        ts.setFont(FontRepository.findFont("Times New Roman"));
        ts.setFontSize(32);

        //Establecer nivel de opacidad del Texto de la Anotación
        wa.setOpacity(0.5);

        //Añadir Texto a la Anotación
        wa.setTextAndState(new String[] { "Aspose.PDF", "Marca de Agua", "Demostración" }, ts);

        //Guardar el Documento
        document.save(_dataDir + "sample_watermark.pdf");
    }
}
```


## Obtener Anotación de Marca de Agua

```java
    public static void GetWatermarkAnnotation() {
        // Cargar el archivo PDF
        Document document = new Document(_dataDir + "sample_watermark.pdf");

        // Filtrar anotaciones usando AnnotationSelector
        Page page = document.getPages().get_Item(1);
        AnnotationSelector annotationSelector = new AnnotationSelector(
                new WatermarkAnnotation(page, Rectangle.getTrivial()));
        page.accept(annotationSelector);
        List<Annotation> WatermarkAnnotations = annotationSelector.getSelected();

        // imprimir resultados
        for (Annotation fa : WatermarkAnnotations) {
            System.out.println(fa.getRect());
        }
    }
```

## Eliminar Anotación de Marca de Agua

```java
    public static void DeleteWatermarkAnnotation() {
         // Cargar el archivo PDF
         Document document = new Document(_dataDir + "sample_watermark.pdf");

         // Filtrar anotaciones usando AnnotationSelector
         Page page = document.getPages().get_Item(1);
         AnnotationSelector annotationSelector = new AnnotationSelector(
                 new WatermarkAnnotation(page, Rectangle.getTrivial()));
         page.accept(annotationSelector);
         List<Annotation> WatermarkAnnotations = annotationSelector.getSelected();

         // eliminar anotaciones
         for (Annotation fa : WatermarkAnnotations) {
            page.getAnnotations().delete(fa);
        }
        document.save(_dataDir + "sample_watermark_del.pdf");
    }
```