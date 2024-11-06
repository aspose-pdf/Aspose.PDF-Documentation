---
title: Anotación de Resaltados en PDF 
linktitle: Anotación de Resaltados
type: docs
weight: 20
url: es/java/highlights-annotation/
description: Las anotaciones de marcado se presentan en el texto como resaltados, subrayados, tachados o subrayados ondulados en el texto de un documento.
lastmod: "2021-11-24"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Las anotaciones de marcado de texto deben aparecer como resaltados, subrayados, tachados o subrayados ondulados en el texto de un documento. Al abrirse, deben mostrar una ventana emergente que contenga el texto de la nota asociada.

Las propiedades de las anotaciones de marcado de texto en el documento PDF se pueden editar usando la ventana de propiedades proporcionada en el control del visor de PDF. Se pueden modificar el color, la opacidad, el autor y el tema de la anotación de marcado de texto.

Es posible obtener o establecer las configuraciones de las anotaciones de resaltado usando la propiedad highlightSettings.
 La propiedad highlightSettings se utiliza para establecer el color, opacidad, autor, asunto, fecha de modificación y las propiedades isLocked de las anotaciones de resaltado.

También es posible obtener o establecer la configuración de las anotaciones de tachado utilizando la propiedad strikethroughSettings. La propiedad strikethroughSettings se utiliza para establecer el color, opacidad, autor, asunto, fecha de modificación y las propiedades isLocked de las anotaciones de tachado.

La siguiente característica es la capacidad de obtener o establecer la configuración de las anotaciones de subrayado utilizando la propiedad underlineSettings. La propiedad underlineSettings se utiliza para establecer el color, opacidad, autor, asunto, fecha de modificación y las propiedades isLocked de las anotaciones de subrayado.

## Añadir Anotación de Marcado de Texto

Para añadir una Anotación de Marcado de Texto al documento PDF, necesitamos realizar las siguientes acciones:

1. Cargar el archivo PDF - nuevo objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).
1. Crear anotaciones:

    - [HighlightAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/HighlightAnnotation) y establecer parámetros (título, color).- [StrikeOutAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/StrikeOutAnnotation) y configurar parámetros (título, color).
- [SquigglyAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/SquigglyAnnotation) y configurar parámetros (título, color).
- [UnderlineAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/UnderlineAnnotation) y configurar parámetros (título, color).
1. Después, deberíamos agregar todas las anotaciones a la página.

```java
package com.aspose.pdf.examples;

import java.util.*;
import com.aspose.pdf.*;

public class ExampleTextMarkupAnnotation {
    // La ruta al directorio de documentos.
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void AddTextMarkupAnnotation() {
        try {
            // Cargar el archivo PDF
            Document document = new Document(_dataDir + "sample.pdf");
            Page page = document.getPages().get_Item(1);
            TextFragmentAbsorber tfa = new TextFragmentAbsorber("PDF");
            tfa.visit(page);

            // Crear anotaciones
            HighlightAnnotation highlightAnnotation = new HighlightAnnotation(page,
                    tfa.getTextFragments().get_Item(1).getRectangle());
            highlightAnnotation.setTitle("Usuario de Aspose");
            highlightAnnotation.setColor(Color.getLightGreen());

            StrikeOutAnnotation strikeOutAnnotation = new StrikeOutAnnotation(page,
                    tfa.getTextFragments().get_Item(2).getRectangle());
            strikeOutAnnotation.setTitle("Usuario de Aspose");
            strikeOutAnnotation.setColor(Color.getBlue());

            SquigglyAnnotation squigglyAnnotation = new SquigglyAnnotation(page,
                    tfa.getTextFragments().get_Item(3).getRectangle());
            squigglyAnnotation.setTitle("Usuario de Aspose");
            squigglyAnnotation.setColor(Color.getRed());

            UnderlineAnnotation underlineAnnotation = new UnderlineAnnotation(page,
                    tfa.getTextFragments().get_Item(4).getRectangle());
            underlineAnnotation.setTitle("Usuario de Aspose");
            underlineAnnotation.setColor(Color.getViolet());

            // Agregar anotación a la página
            page.getAnnotations().add(highlightAnnotation);
            page.getAnnotations().add(squigglyAnnotation);
            page.getAnnotations().add(strikeOutAnnotation);
            page.getAnnotations().add(underlineAnnotation);
            document.save(_dataDir + "sample_mod.pdf");
        } catch (Exception ex) {
            System.out.println(ex.getMessage());
        }
    }
}
```


Si desea resaltar un fragmento de varias líneas, debe usar un ejemplo avanzado:

```java
    /// <summary>
    /// Ejemplo avanzado para cuando desea resaltar un fragmento de varias líneas
    /// </summary>
    public static void AddHighlightAnnotationAdvanced() {
        Document document = new Document(_dataDir + "sample_mod.pdf");
        Page page = document.getPages().get_Item(1);
        TextFragmentAbsorber tfa = new TextFragmentAbsorber("Adobe\\W+Acrobat\\W+Reader", new TextSearchOptions(true));
        tfa.visit(page);
        for (TextFragment textFragment : tfa.getTextFragments()) {
            HighlightAnnotation highlightAnnotation = HighLightTextFragment(page, textFragment, Color.getYellow());
            page.getAnnotations().add(highlightAnnotation);
        }
        document.save(_dataDir + "sample_mod.pdf");
    }

    private static HighlightAnnotation HighLightTextFragment(Page page, TextFragment textFragment, Color color) {
        HighlightAnnotation ha;
        if (textFragment.getSegments().size() == 1) {
            ha = new HighlightAnnotation(page, textFragment.getSegments().get_Item(1).getRectangle());
            ha.setTitle("Aspose User");
            ha.setColor(color);
            ha.setModified(new Date());
            Rectangle rect = textFragment.getSegments().get_Item(1).getRectangle();
            ha.setQuadPoints(
                    new Point[] { new Point(rect.getLLX(), rect.getURY()), new Point(rect.getURX(), rect.getURY()),
                            new Point(rect.getLLX(), rect.getLLY()), new Point(rect.getURX(), rect.getLLY()) });
            return ha;
        }

        int offset = 0;
        Point[] quadPoints = new Point[textFragment.getSegments().size() * 4];
        for (TextSegment segment : textFragment.getSegments()) {
            Rectangle r = segment.getRectangle();
            quadPoints[offset + 0] = new Point(r.getLLX(), r.getURY());
            quadPoints[offset + 1] = new Point(r.getURX(), r.getURY());
            quadPoints[offset + 2] = new Point(r.getLLX(), r.getLLY());
            quadPoints[offset + 3] = new Point(r.getURX(), r.getLLY());
            offset += 4;
        }

        double llx = quadPoints[0].getX();
        double lly = quadPoints[0].getY();
        double urx = quadPoints[0].getX();
        double ury = quadPoints[0].getY();
        for (Point pt : quadPoints) {
            if (llx > pt.getX())
                llx = pt.getX();
            if (lly > pt.getY())
                lly = pt.getY();
            if (urx < pt.getX())
                urx = pt.getX();
            if (ury < pt.getY())
                ury = pt.getY();
        }
        ha = new HighlightAnnotation(page, new Rectangle(llx, lly, urx, ury));
        ha.setTitle("Aspose User");
        ha.setColor(color);
        ha.setModified(new Date());
        ha.setQuadPoints(quadPoints);
        return ha;
    }

    /// <summary>
    /// Cómo obtener un texto resaltado
    /// </summary>
    public static void GetHighlightedText() {
        // Cargar el archivo PDF
        Document document = new Document(_dataDir + "sample_mod.pdf");
        Page page = document.getPages().get_Item(1);

        AnnotationSelector annotationSelector1 = new AnnotationSelector(
                new HighlightAnnotation(page, Rectangle.getTrivial()));
        page.accept(annotationSelector1);
        List<Annotation> highlightAnnotations = annotationSelector1.getSelected();
        for (Annotation ta : highlightAnnotations) {
            System.out.println("[" + ((HighlightAnnotation) ta).getMarkedText() + "]");
        }
    }
```


## Obtener la Anotación de Marcado de Texto

Por favor, intenta usar el siguiente fragmento de código para obtener la anotación de marcado de texto del documento PDF.

```java
     public static void GetTextMarkupAnnotation() {
        // Cargar el archivo PDF
        Document document = new Document(_dataDir + "sample_mod.pdf");
        Page page = document.getPages().get_Item(1);

        AnnotationSelector annotationSelector1 = new AnnotationSelector(
                new HighlightAnnotation(page, Rectangle.getTrivial()));
        page.accept(annotationSelector1);
        AnnotationSelector annotationSelector2 = new AnnotationSelector(
                new SquigglyAnnotation(page, Rectangle.getTrivial()));
        page.accept(annotationSelector2);

        List<Annotation> textMarkupAnnotations = annotationSelector1.getSelected();
        textMarkupAnnotations.addAll(annotationSelector2.getSelected());

        // imprimir resultados
        for (Annotation ta : textMarkupAnnotations) {
            System.out.printf("[" + ta.getAnnotationType() + ta.getRect() + "]");
        }
    }
```


## Eliminar anotación de marcado de texto

El siguiente fragmento de código muestra cómo eliminar la anotación de marcado de texto de un archivo PDF.

```java
   public static void DeleteTextMarkupAnnotation() {
        // Cargar el archivo PDF
        Document document = new Document(_dataDir + "sample_mod.pdf");
        Page page = document.getPages().get_Item(1);

        AnnotationSelector annotationSelector1 = new AnnotationSelector(
                new HighlightAnnotation(page, Rectangle.getTrivial()));
        page.accept(annotationSelector1);
        AnnotationSelector annotationSelector2 = new AnnotationSelector(
                new SquigglyAnnotation(page, Rectangle.getTrivial()));
        page.accept(annotationSelector2);

        List<Annotation> textMarkupAnnotations = annotationSelector1.getSelected();
        textMarkupAnnotations.addAll(annotationSelector2.getSelected());

        // imprimir resultados
        for (Annotation ta : textMarkupAnnotations) {
            page.getAnnotations().delete(ta);
        }
        document.save(_dataDir + "sample_del.pdf");
    }
```