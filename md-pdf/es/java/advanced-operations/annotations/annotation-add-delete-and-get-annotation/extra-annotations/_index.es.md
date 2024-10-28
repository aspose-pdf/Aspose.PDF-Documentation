---
title: Uso de tipos adicionales de anotaciones PDF
linktitle: Anotaciones Extra
type: docs
weight: 60
url: /java/extra-annotations/
description: Esta sección describe cómo agregar, obtener y eliminar tipos adicionales de anotaciones de su documento PDF.
lastmod: "2021-11-24"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Cómo agregar una anotación de intercalado en un archivo PDF existente

La anotación de intercalado es un símbolo que indica la edición de texto. La anotación de intercalado también es una anotación de marcado, por lo que la clase Caret deriva de la clase Markup y también proporciona funciones para obtener o establecer propiedades de la anotación de intercalado y restablecer el flujo de la apariencia de la anotación de intercalado.

Pasos con los que creamos la anotación de intercalado:

1. Cargar el archivo PDF - nuevo [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

1. Crear una nueva [Caret Annotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/CaretAnnotation) y establecer los parámetros de Caret (new Rectangle, título, Asunto, Banderas, color, ancho, StartingStyle y EndingStyle). Esta anotación se utiliza para indicar la inserción de texto.
1. Crear una nueva [StrikeOutAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/StrikeOutAnnotation) y establecer parámetros (new Rectangle, título, color, new QuadPoints y nuevos puntos, Asunto, InReplyTo, ReplyType).
1. Después podemos agregar anotaciones a la página.

El siguiente fragmento de código muestra cómo agregar una anotación de caret a un archivo PDF:

```java
package com.aspose.pdf.examples;

import java.util.*;
import com.aspose.pdf.*;

public class ExampleCaretAnnotation {
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void AddCaretAnnotation() {
        // Cargar el archivo PDF
        Document document = new Document(_dataDir + "sample.pdf");
        // Esta anotación se utiliza para indicar la inserción de texto
        CaretAnnotation caretAnnotation1 = new CaretAnnotation(
                document.getPages().get_Item(1), new Rectangle(299.988, 713.664, 308.708, 720.769));
        caretAnnotation1.setTitle("Usuario de Aspose");
        caretAnnotation1.setSubject("Texto insertado 1");
        caretAnnotation1.setFlags(AnnotationFlags.Print);
        caretAnnotation1.setColor(Color.getBlue());

        // Esta anotación se utiliza para indicar la sustitución de texto
        CaretAnnotation caretAnnotation2 = new CaretAnnotation(
                document.getPages().get_Item(1), new Rectangle(361.246, 727.908, 370.081, 735.107));

        caretAnnotation2.setTitle("Usuario de Aspose");
        caretAnnotation2.setFlags(AnnotationFlags.Print);
        caretAnnotation2.setSubject("Texto insertado 2");
        caretAnnotation2.setColor(Color.getBlue());

        StrikeOutAnnotation strikeOutAnnotation = new StrikeOutAnnotation(
                document.getPages().get_Item(1), new Rectangle(318.407, 727.826, 368.916, 740.098));

        strikeOutAnnotation.setColor(Color.getBlue());
        strikeOutAnnotation.setQuadPoints(new Point[] { new Point(321.66, 739.416),
                new Point(365.664, 739.416), new Point(321.66, 728.508),
                new Point(365.664, 728.508) });

        strikeOutAnnotation.setSubject("Tachado");
        strikeOutAnnotation.setInReplyTo(caretAnnotation2);
        strikeOutAnnotation.setReplyType(ReplyType.Group);

        document.getPages().get_Item(1).getAnnotations().add(caretAnnotation1);
        document.getPages().get_Item(1).getAnnotations().add(caretAnnotation2);
        document.getPages().get_Item(1).getAnnotations().add(strikeOutAnnotation);

        document.save(_dataDir + "sample_caret.pdf");

    }
```


## Obtener Anotación de Intercalación

Por favor, intente usar el siguiente fragmento de código para obtener la anotación de intercalación en un documento PDF

```java
    public static void GetCaretAnnotation() {
        // Cargar el archivo PDF
        Document document = new Document(_dataDir + "sample_caret.pdf");

        // Filtrar anotaciones usando AnnotationSelector
        Page page = document.getPages().get_Item(1);
        AnnotationSelector annotationSelector = new AnnotationSelector(
                new CaretAnnotation(page, Rectangle.getTrivial()));
        page.accept(annotationSelector);
        List<Annotation> caretAnnotations = annotationSelector.getSelected();

        // imprimir resultados
        for (Annotation ca : caretAnnotations) {
            System.out.println(ca.getRect());
        }
    }
```

## Eliminar Anotación de Intercalación

El siguiente fragmento de código muestra cómo eliminar la anotación de intercalación de un archivo PDF.

```java
public static void DeleteCaretAnnotation() {
        // Cargar el archivo PDF
        Document document = new Document(_dataDir + "sample_caret.pdf");

        // Filtrar anotaciones usando AnnotationSelector
        Page page = document.getPages().get_Item(1);
        AnnotationSelector annotationSelector = new AnnotationSelector(
                new CaretAnnotation(page, Rectangle.getTrivial()));
        page.accept(annotationSelector);
        List<Annotation> caretAnnotations = annotationSelector.getSelected();

        // eliminar anotación
        for (Annotation ca : caretAnnotations) {
            document.getPages().get_Item(1).getAnnotations().delete(ca);
        }
        document.save(_dataDir + "sample_caret_del.pdf");
    }
```


Un [Link Annotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/LinkAnnotation) es un enlace de hipertexto que conduce a un destino en otra parte del documento o a una acción que se debe realizar.

## Añadir Anotación de Enlace

Un enlace es un área rectangular que se puede colocar en cualquier parte de la página. Cada enlace tiene una acción PDF correspondiente asociada con él. Esta acción se realiza cuando el usuario hace clic en el área de este enlace.

El siguiente fragmento de código muestra cómo añadir una Anotación de Enlace a un archivo PDF utilizando un ejemplo de número de teléfono:

```java
package com.aspose.pdf.examples;

import java.util.*;
import com.aspose.pdf.*;

public class ExampleLinkAnnotation {

    // La ruta al directorio de documentos.

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void AddLinkAnnotation() {
        try {
            // Cargar el archivo PDF
            Document document = new Document(_dataDir + "SimpleResume.pdf");
            Page page = document.getPages().get_Item(1);

            // Crear objeto TextFragmentAbsorber para encontrar un número de teléfono
            TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("678-555-0103");

            // Aceptar el absorbedor solo para la 1ª página
            page.accept(textFragmentAbsorber);

            TextFragment phoneNumberFragment = textFragmentAbsorber.getTextFragments().get_Item(1);

            // Crear Anotación de Enlace y establecer la acción para llamar a un número de teléfono
            LinkAnnotation linkAnnotation = new LinkAnnotation(page, phoneNumberFragment.getRectangle());
            linkAnnotation.setAction(new GoToURIAction("callto:678-555-0103"));

            // Añadir anotación a la página
            page.getAnnotations().add(linkAnnotation);
            document.save(_dataDir + "SimpleResume_mod.pdf");
        } catch (Exception ex) {
            System.out.println(ex.getMessage());
        }
    }
```


## Obtener Anotación de Enlace

Por favor, intente usar el siguiente fragmento de código para Obtener Anotación de Enlace del documento PDF.

```java
    public static void GetLinkAnnotations() {

        // Cargar el archivo PDF
        Document document = new Document(_dataDir + "SimpleResume_mod.pdf");

        // Filtrar anotaciones usando AnnotationSelector
        Page page = document.getPages().get_Item(1);
        AnnotationSelector annotationSelector = new AnnotationSelector(
                new LinkAnnotation(page, Rectangle.getTrivial()));
        page.accept(annotationSelector);
        List<Annotation> linkAnnotations = annotationSelector.getSelected();

        // imprimir resultados
        for (Annotation la : linkAnnotations) {

            LinkAnnotation l = (LinkAnnotation) la;

            // Imprimir la URL de cada Anotación de Enlace
            System.out.println("URI: " + ((GoToURIAction) l.getAction()).getURI());

            TextAbsorber absorber = new TextAbsorber();
            absorber.getTextSearchOptions().setLimitToPageBounds(true);
            absorber.getTextSearchOptions().setRectangle(l.getRect());
            page.accept(absorber);

            String extractedText = absorber.getText();

            // Imprimir el texto asociado con el hipervínculo
            System.out.println(extractedText);
        }
    }
```


## Eliminar anotación de enlace

El siguiente fragmento de código muestra cómo eliminar la anotación de enlace de un archivo PDF. Para esto, necesitamos encontrar y eliminar todas las anotaciones de enlace en la primera página. Después de esto, guardaremos el documento con la anotación eliminada.

```java
    public static void DeleteLinkAnnotations() {
        // Cargar el archivo PDF
        Document document = new Document(_dataDir + "SimpleResume_mod.pdf");

        // Filtrar anotaciones usando AnnotationSelector
        Page page = document.getPages().get_Item(1);
        AnnotationSelector annotationSelector = new AnnotationSelector(
                new LinkAnnotation(page, Rectangle.getTrivial()));
        page.accept(annotationSelector);
        List<Annotation> linkAnnotations = annotationSelector.getSelected();

        for (Annotation la : linkAnnotations)
            page.getAnnotations().delete(la);

        // Guardar documento con la anotación eliminada
        document.save(_dataDir + "SimpleResume_del.pdf");
    }
```

## Censurar cierta región de la página con la anotación de redacción usando Aspose.PDF para Java

Aspose.PDF para Java admite la función de agregar y manipular anotaciones en un archivo PDF existente. Recientemente, algunos de nuestros clientes solicitaron la necesidad de redactar (eliminar texto, imágenes, etc. de elementos) una cierta región de la página de un documento PDF. Para cumplir con este requisito, se proporciona una clase llamada RedactionAnnotation, que se puede usar para redactar ciertas regiones de la página o se puede usar para manipular RedactionAnnotations existentes y redactarlas (es decir, aplanar la anotación y eliminar el texto debajo de ella).

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;
import com.aspose.pdf.facades.PdfAnnotationEditor;

public class ExampleRedactAnnotation {
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void RedactionAnnotation() {

        // Abrir documento
        Document document = new Document(_dataDir + "sample.pdf");
        Page page = document.getPages().get_Item(1);

        // Crear instancia de RedactionAnnotation para una región específica de la página
        RedactionAnnotation annot = new RedactionAnnotation(page, new Rectangle(200, 500, 300, 600));
        annot.setFillColor(Color.getGreen());
        annot.setBorderColor(Color.getYellow());
        annot.setColor(Color.getBlue());

        // Texto a imprimir en la anotación de redacción
        annot.setOverlayText("REDACTED");
        annot.setTextAlignment(HorizontalAlignment.Center);

        // Repetir texto de superposición sobre la anotación de redacción
        annot.setRepeat(true);

        // Agregar anotación a la colección de anotaciones de la primera página
        page.getAnnotations().add(annot);

        // Aplana la anotación y redacta el contenido de la página (es decir, elimina texto e imagen
        // bajo la anotación redactada)
        annot.redact();
        document.save(_dataDir + "RedactPage_out.pdf");
    }
```


## Enfoque de Facades

El espacio de nombres Aspose.PDF.Facades también tiene una clase llamada [PdfAnnotationEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor) que proporciona la funcionalidad para manipular las anotaciones existentes dentro de un archivo PDF. Esta clase contiene un método llamado [RedactArea(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf/Redaction#getredactArea-com.aspose.pdf.Page-com.aspose.pdf.Rectangle-java.awt.Color-) que proporciona la capacidad de eliminar ciertas regiones de la página.

```java
    public static void RedactionAnnotationFacades(){
        PdfAnnotationEditor editor = new PdfAnnotationEditor();

        editor.bindPdf(_dataDir + "sample.pdf");

        // Censurar cierta región de la página
        editor.redactArea(1, new Rectangle(100, 100, 20, 70), java.awt.Color.white);
        editor.bindPdf(_dataDir + "sample.pdf");
        editor.save( _dataDir + "FacadesApproach_out.pdf");
    }
```