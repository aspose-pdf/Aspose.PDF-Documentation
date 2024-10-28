---
title: PDF Text Annotation
Texttitle: Text Annotation
type: docs
weight: 10
url: /java/text-annotation/
description: Aspose.PDF para Java le permite Agregar, Obtener y Eliminar Anotaciones de Texto de su documento PDF.
lastmod: "2021-11-24"
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

Agregar, Eliminar y Obtener Anotaciones son similares para diferentes tipos de anotaciones. Tomemos como ejemplo una Anotación de Texto.

## Cómo agregar una Anotación de Texto en un archivo PDF existente

En este tutorial, aprenderá cómo agregar texto a un documento PDF existente. La herramienta de texto le permite agregar texto en cualquier parte del documento. Una Anotación de Texto es una anotación adjunta a una ubicación específica en un documento PDF. Cuando está cerrada, la anotación se muestra como un icono; cuando está abierta, debe mostrar una ventana emergente que contenga el texto de la nota en la fuente y tamaño elegidos por el lector.

Las anotaciones están contenidas por la colección [Annotations](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/AnnotationCollection) de una Página particular.
 Esta colección contiene las anotaciones solo para esa página individual; cada página tiene su propia colección de Anotaciones.

Para agregar una anotación a una página en particular, agrégala a la colección de Anotaciones de esa página con el método Add.

1. Primero, crea una anotación que deseas agregar al PDF.
1. Luego abre el PDF de entrada.
1. Agrega la anotación a la colección de Anotaciones del objeto [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page).

El siguiente fragmento de código muestra cómo agregar una anotación a una página PDF.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;
import java.util.*;

public class ExampleTextAnnotation {

    private static String _dataDir = "/home/aspose/pdf-examples/Samples/";

    public static void AddTextAnnotation()
    {
        // Cargar el archivo PDF
        Document document = new Document(_dataDir + "sample.pdf");
        Page page = document.getPages().get_Item(1);
        Rectangle rect = new Rectangle(200, 750, 400, 790);
        TextAnnotation textAnnotation = new TextAnnotation(page, rect);

        textAnnotation.setTitle("Usuario de Aspose");
        textAnnotation.setSubject("Asunto de ejemplo");
        textAnnotation.setState (AnnotationState.Accepted);
        textAnnotation.setContents("Contenido de ejemplo para la anotación");
        textAnnotation.setOpen(true);
        textAnnotation.setIcon(TextIcon.Circle);

        Border border = new Border(textAnnotation);
        border.setWidth(5);
        border.setDash(new Dash(1, 1));
        textAnnotation.setBorder(border);
        textAnnotation.setRect(rect);

        page.getAnnotations().add(textAnnotation);
        document.save(_dataDir + "sample_textannot.pdf");
    }
}
```

## Agregar Nueva (o Crear) Anotación de Texto Libre

Una anotación de texto libre muestra texto directamente en la página. El método PdfContentEditor.CreateFreeText permite crear este tipo de anotación. En el siguiente fragmento, añadimos una anotación de texto libre sobre la primera aparición de la cadena.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;
import java.util.*;

public class ExampleFreeTextAnnotation {

    private static String _dataDir = "/home/aspose/pdf-examples/Samples/";

    public static void AddFreeTextAnnotation()
    {
        // Cargar el archivo PDF
        Document document = new Document(_dataDir + "sample.pdf");
        Page page = document.getPages().get_Item(1);

        DefaultAppearance defaultAppearance = new DefaultAppearance();
        defaultAppearance.setFontName("Helvetica");
        defaultAppearance.setFontSize(12);
        defaultAppearance.setTextColor(java.awt.Color.BLUE);

        FreeTextAnnotation freeTextAnnotation = new FreeTextAnnotation(page, new Rectangle(300.0, 770.0, 400.0, 790.0), defaultAppearance);

        freeTextAnnotation.setRichText("Demostración de Texto Libre");
        page.getAnnotations().add(freeTextAnnotation);
        document.save(_dataDir + "sample_freetext.pdf");
    }
}
```


## Obtener Anotación de Texto Libre

Aspose.PDF para Java le permite obtener Anotación de Texto Libre de su documento PDF.

Por favor, revise el siguiente fragmento de código para resolver esta tarea:

```java
public static void GetFreeTextAnnotation() {
        // Cargar el archivo PDF
        Document document = new Document(_dataDir + "sample_freetext.pdf");

        // Filtrar anotaciones usando AnnotationSelector
        Page page = document.getPages().get_Item(1);
        AnnotationSelector annotationSelector = new AnnotationSelector(
                new FreeTextAnnotation(page, Rectangle.getTrivial(), new DefaultAppearance()));
        page.accept(annotationSelector);
        List<Annotation> freeTextAnnotations = annotationSelector.getSelected();

        // imprimir resultados
        for (Annotation fa : freeTextAnnotations) {
            System.out.println(fa.getRect());
        }
    }
```

## Eliminar Anotación de Texto Libre

Aspose.PDF para Java le permite eliminar Anotación de Texto Libre de su documento PDF.

Por favor, revise el siguiente fragmento de código para resolver esta tarea:

```java
  public static void DeleteFreeTextAnnotation() {
         // Cargar el archivo PDF
         Document document = new Document(_dataDir + "sample_freetext.pdf");

         // Filtrar anotaciones usando AnnotationSelector
         Page page = document.getPages().get_Item(1);
         AnnotationSelector annotationSelector = new AnnotationSelector(
                 new FreeTextAnnotation(page, Rectangle.getTrivial(), new DefaultAppearance()));
         page.accept(annotationSelector);
         List<Annotation> freeTextAnnotations = annotationSelector.getSelected();

         // eliminar anotaciones
         for (Annotation fa : freeTextAnnotations) {
            page.getAnnotations().delete(fa);
        }
        document.save(_dataDir + "sample_freetext_del.pdf");
    }
```

## Eliminar Todas las Anotaciones de la Página de un Archivo PDF

La colección [AnnotationCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/AnnotationCollection) de un objeto [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) contiene todas las anotaciones para esa página en particular.
 Para eliminar todas las anotaciones de una página, llame al método *Delete* de la colección AnnotationCollection.

El siguiente fragmento de código muestra cómo eliminar todas las anotaciones de una página en particular.

```java
    public static void DeleteTextAnnotation() {
         // Cargar el archivo PDF
         Document document = new Document(_dataDir + "sample_textannot.pdf");

         // Filtrar anotaciones usando AnnotationSelector
         Page page = document.getPages().get_Item(1);
         AnnotationSelector annotationSelector = new AnnotationSelector(
                 new TextAnnotation(page, Rectangle.getTrivial()));
         page.accept(annotationSelector);
         List<Annotation> TextAnnotations = annotationSelector.getSelected();

         // eliminar anotaciones
         for (Annotation fa : TextAnnotations) {
            page.getAnnotations().delete(fa);
        }
        document.save(_dataDir + "sample_textannot_del.pdf");
    }
```

## Obtener Todas las Anotaciones de la Página de un Documento PDF

Aspose.PDF te permite obtener anotaciones de un documento completo o de una página determinada. Para obtener todas las anotaciones de la página en un documento PDF, recorre la colección [AnnotationCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/AnnotationCollection) de los recursos de la página deseada. El siguiente fragmento de código te muestra cómo obtener todas las anotaciones de una página.

```java
  public static void GetTextAnnotation() {
        // Cargar el archivo PDF
        Document document = new Document(_dataDir + "sample_textannot.pdf");

        // Filtrar anotaciones usando AnnotationSelector
        Page page = document.getPages().get_Item(1);
        AnnotationSelector annotationSelector = new AnnotationSelector(
                new TextAnnotation(page, Rectangle.getTrivial()));
        page.accept(annotationSelector);
        List<Annotation> TextAnnotations = annotationSelector.getSelected();

        // imprimir resultados
        for (Annotation fa : TextAnnotations) {
            System.out.println(fa.getRect());
        }
    }
```