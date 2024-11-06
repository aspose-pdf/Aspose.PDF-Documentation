---
title: Trabajando con Encabezados en PDF
type: docs
weight: 70
url: es/java/working-with-headings/
lastmod: "2021-06-05"
description: Cree numeración en el encabezado de su documento PDF con Java. Aspose.PDF para Java ofrece diferentes tipos de estilos de numeración.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Aplicar Estilo de Numeración en el Encabezado

Los encabezados son las partes importantes de cualquier documento. Los escritores siempre intentan hacer que los encabezados sean más destacados y significativos para sus lectores. Si hay más de un encabezado en un documento, un escritor tiene varias opciones para organizar estos encabezados. Uno de los enfoques más comunes para organizar encabezados es escribir los encabezados en Estilo de Numeración.

Aspose.PDF para Java ofrece muchos estilos de numeración predefinidos. Estos estilos de numeración predefinidos se almacenan en una enumeración, NumberingStyle. Los valores predefinidos de la enumeración NumberingStyle y sus descripciones se dan a continuación:

|**Tipos de Encabezado**|**Descripción**|
| :- | :- |
|NumeralsArabic|Tipo árabe, por ejemplo, 1,1.1,...|

|NumeralsRomanUppercase|Tipo romano en mayúsculas, por ejemplo, I,I.II, ...|
|NumeralsRomanLowercase|Tipo romano en minúsculas, por ejemplo, i,i.ii, ...|
|LettersUppercase|Tipo inglés en mayúsculas, por ejemplo, A,A.B, ...|
|LettersLowercase|Tipo inglés en minúsculas, por ejemplo, a,a.b, ...|
La propiedad [setStyle](https://reference.aspose.com/pdf/java/com.aspose.pdf/Heading) de la clase [com.aspose.pdf.Heading](https://reference.aspose.com/pdf/java/com.aspose.pdf/Heading) se utiliza para establecer los estilos de numeración de los encabezados.

El código fuente, para obtener la salida mostrada en la figura anterior, se proporciona a continuación en el ejemplo.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

public class ExampleHeading {
    // La ruta al directorio de documentos.
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void ApplyNumberingStyleinHeading() {

        Document pdfDoc = new Document();
        pdfDoc.getPageInfo().setWidth(612.0);
        pdfDoc.getPageInfo().setHeight(792.0);
        pdfDoc.getPageInfo().setMargin(new MarginInfo());
        pdfDoc.getPageInfo().getMargin().setLeft(72);
        pdfDoc.getPageInfo().getMargin().setRight(72);
        pdfDoc.getPageInfo().getMargin().setTop(72);
        pdfDoc.getPageInfo().getMargin().setBottom(72);

        Page pdfPage = pdfDoc.getPages().add();
        pdfPage.getPageInfo().setWidth(612.0);
        pdfPage.getPageInfo().setHeight(792.0);
        pdfDoc.getPageInfo().setMargin(new MarginInfo());
        pdfDoc.getPageInfo().getMargin().setLeft(72);
        pdfDoc.getPageInfo().getMargin().setRight(72);
        pdfDoc.getPageInfo().getMargin().setTop(72);
        pdfDoc.getPageInfo().getMargin().setBottom(72);

        FloatingBox floatBox = new FloatingBox();
        floatBox.setMargin(pdfPage.getPageInfo().getMargin());

        pdfPage.getParagraphs().add(floatBox);

        Heading heading = new Heading(1);
        heading.setInList(true);
        heading.setStartNumber(1);
        heading.setText("Lista 1");
        heading.setStyle(NumberingStyle.NumeralsRomanLowercase);
        heading.setAutoSequence(true);

        floatBox.getParagraphs().add(heading);
        Heading heading2 = new Heading(1);
        heading2.setInList(true);
        heading2.setStartNumber(13);
        heading2.setText("Lista 2");
        heading2.setStyle(NumberingStyle.NumeralsRomanLowercase);
        heading2.setAutoSequence(true);

        floatBox.getParagraphs().add(heading2);

        Heading heading3 = new Heading(2);
        heading3.setInList(true);
        heading3.setStartNumber(1);
        heading3.setText("el valor, a partir de la fecha efectiva del plan, de la propiedad que se distribuirá bajo el plan en relación con cada permitido");
        heading3.setStyle (NumberingStyle.LettersLowercase);
        heading3.setAutoSequence(true);

        floatBox.getParagraphs().add(heading3);
        _dataDir = _dataDir + "ApplyNumberStyle_out.pdf";
        pdfDoc.save(_dataDir);

    }

}
```