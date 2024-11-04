---
title: Añadir sellos de texto en PDF programáticamente
linktitle: Sellos de texto en archivo PDF
type: docs
weight: 20
url: /java/text-stamps-in-the-pdf-file/
description: Añadir un sello de texto a un archivo PDF usando la clase TextStamp con Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Añadir Sello de Texto con Java

Aspose.PDF para Java proporciona la clase [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp) para añadir un sello de texto en un archivo PDF.
 La clase [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp) proporciona métodos necesarios para especificar tamaño de fuente, estilo de fuente y color de fuente, etc., para el objeto de sello. Para agregar un sello de texto, primero necesitas crear un objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) y un objeto [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp) usando métodos requeridos. Después de eso, puedes llamar al método [addStamp(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#addStamp-com.aspose.pdf.Stamp-) de la clase [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) para agregar el sello en el documento PDF.

El siguiente fragmento de código muestra cómo agregar un sello de texto en el archivo PDF.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;
import com.aspose.pdf.facades.*;
import com.aspose.pdf.facades.Stamp;

public class ExampleStampingImage {
    // La ruta al directorio de documentos.
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void AddTextStamp() {
        // abrir documento
        Document pdfDocument = new Document("input.pdf");
        // crear sello de texto
        TextStamp textStamp = new TextStamp("Sello de Ejemplo");
        // establecer si el sello está en el fondo
        textStamp.setBackground(true);
        // establecer origen
        textStamp.setXIndent(100);
        textStamp.setYIndent(100);
        // rotar sello
        textStamp.setRotate(Rotation.on90);
        // establecer propiedades de texto
        textStamp.getTextState().setFont(FontRepository.findFont("Arial"));
        textStamp.getTextState().setFontSize(14.0F);
        textStamp.getTextState().setFontStyle(FontStyles.Bold);
        textStamp.getTextState().setFontStyle(FontStyles.Italic);
        textStamp.getTextState().setForegroundColor(Color.getGreen());
        // agregar sello a una página en particular
        pdfDocument.getPages().get_Item(1).addStamp(textStamp);
        // guardar documento de salida
        pdfDocument.save("TextStamp_output.pdf");
    }
```

## Definir alineación para el objeto TextStamp

Agregar marcas de agua a documentos PDF es una de las características más demandadas, y Aspose.PDF para Java es completamente capaz de agregar marcas de agua de Imagen, así como de Texto. La clase [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp) proporciona la función para agregar sellos de texto sobre el archivo PDF. Recientemente, ha habido un requisito para admitir la función de especificar la alineación del texto al usar el objeto [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp). Así que, para cumplir con este requisito, hemos introducido el método setTextAlignment(..) en la clase [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp). Al usar este método, puedes especificar la alineación horizontal del texto.

Los siguientes fragmentos de código muestran un ejemplo de cómo cargar un documento PDF existente y agregar [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp) sobre él.

```java
    public static void DefineAlignmentTextStamp() {
        // Instanciar objeto Document con el archivo de entrada
        Document pdfDocument = new Document("input.pdf");
        // instanciar objeto FormattedText con una cadena de ejemplo
        FormattedText text = new FormattedText("This");
        
        // agregar nueva línea de texto a FormattedText
        text.addNewLineText("is sample");
        text.addNewLineText("Center Aligned");
        text.addNewLineText("TextStamp");
        text.addNewLineText("Object");
        // crear objeto TextStamp utilizando FormattedText
        TextStamp stamp = new TextStamp(text);
        // especificar la alineación horizontal del sello de texto como centrado
        stamp.setHorizontalAlignment(HorizontalAlignment.Center);
        // especificar la alineación vertical del sello de texto como centrado
        stamp.setVerticalAlignment(VerticalAlignment.Center);
        // especificar la alineación horizontal del texto de TextStamp como centrado
        stamp.setTextAlignment(HorizontalAlignment.Center);
        // establecer el margen superior para el objeto sello
        stamp.setTopMargin(20);
        // agregar sello a todas las páginas del archivo PDF
        pdfDocument.getPages().get_Item(1).addStamp(stamp);
        
        // guardar documento de salida
        pdfDocument.save("TextStamp_output.pdf");
    }
```


## Rellenar texto con contorno como sello en archivo PDF

Hemos implementado la configuración del modo de renderizado para escenarios de adición y edición de texto. Para renderizar texto con contorno, por favor crea un objeto [TextState](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextState) y establece RenderingMode a TextRenderingMode.StrokeText y también selecciona un color para la propiedad StrokingColor. Más tarde, enlaza TextState al sello usando el método BindTextState().

El siguiente fragmento de código demuestra cómo agregar texto con relleno y contorno:

```java
   public static void FillStrokeTextAsStampInPDFFile(){
        // Crear objeto TextState para transferir propiedades avanzadas
        TextState ts = new TextState();
        
        // Establecer color para el contorno
        ts.setStrokingColor(Color.getGray());
        
        // Establecer modo de renderizado de texto
        ts.setRenderingMode (TextRenderingMode.StrokeText);
        
        // Cargar un documento PDF de entrada
        PdfFileStamp fileStamp = new PdfFileStamp(new Document(_dataDir + "input.pdf"));

        Stamp stamp = new Stamp();
        stamp.bindLogo(new FormattedText("PAID IN FULL", java.awt.Color.GRAY, "Arial", EncodingType.Winansi, true, 78));

        // Enlazar TextState
        stamp.bindTextState(ts);
        // Establecer origen X,Y
        stamp.setOrigin(100, 100);
        stamp.setOpacity (5);
        stamp.setBlendingSpace (BlendingColorSpace.DeviceRGB);
        stamp.setRotation (45.0F);
        stamp.setBackground(false);
        // Agregar sello
        fileStamp.addStamp(stamp);
        fileStamp.save(_dataDir + "ouput_out.pdf");
        fileStamp.close();
    }
```