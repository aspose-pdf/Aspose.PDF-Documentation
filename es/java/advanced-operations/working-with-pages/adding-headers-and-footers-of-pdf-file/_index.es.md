---
title: Añadir Encabezado y Pie de Página en PDF
linktitle: Añadir Encabezado y Pie de Página
type: docs
weight: 70
url: /java/add-headers-and-footers-of-pdf-file/
description: Aspose.PDF para Java te permite añadir encabezados y pies de página a tu archivo PDF usando la clase TextStamp.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Los sellos PDF se utilizan a menudo en contratos, informes y materiales restringidos, para demostrar que los documentos han sido revisados y marcados como "leído", "calificado" o "confidencial", etc. Este artículo te mostrará cómo podemos añadir sellos de imagen y sellos de texto a documentos PDF usando **Aspose.PDF para Java**.

Si lees los fragmentos de código anteriores línea por línea, encontrarás que la sintaxis y la lógica del código son bastante fáciles de entender.

## Añadiendo Texto en el Encabezado de un Archivo PDF

Puedes usar la clase [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp) para añadir texto en el encabezado de un archivo PDF.
 TextStamp class proporciona las propiedades necesarias para crear un sello basado en texto, como el tamaño de fuente, el estilo de fuente y el color de fuente, etc. Para agregar texto en el encabezado, necesitas crear un objeto Document y un objeto TextStamp usando las propiedades requeridas. Después de eso, puedes llamar al método AddStamp de la Page para agregar el texto en el encabezado del PDF.

Necesitas establecer la propiedad TopMargin de tal manera que ajuste el texto en el área del encabezado de tu PDF. También necesitas establecer HorizontalAlignment en Center y VerticalAlignment en Top.

El siguiente fragmento de código te muestra cómo agregar texto en el encabezado de un archivo PDF con Java.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

public class ExampleAddPDFHeaderandFooter {
    // La ruta al directorio de documentos.
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void AddingTextInHeaderOfPDFFile() {

        // Abrir documento
        Document pdfDocument = new Document(_dataDir + "TextinHeader.pdf");

        // Crear encabezado
        TextStamp textStamp = new TextStamp("Texto del Encabezado");

        // Establecer propiedades del sello
        textStamp.setTopMargin(10);
        textStamp.setHorizontalAlignment(HorizontalAlignment.Center);
        textStamp.setVerticalAlignment(VerticalAlignment.Top);

        // Agregar encabezado en todas las páginas
        for (Page page : pdfDocument.getPages()) {
            page.addStamp(textStamp);
        }

        // Guardar documento actualizado
        pdfDocument.save(_dataDir + "TextinHeader_out.pdf");
    }
```

## Añadiendo Texto en el Pie de Página de un Archivo PDF

Puede usar la clase TextStamp para agregar texto en el pie de página de un archivo PDF. La clase TextStamp proporciona las propiedades necesarias para crear un sello basado en texto como el tamaño de fuente, estilo de fuente, color de fuente, etc. Para agregar texto en el pie de página, necesita crear un objeto Document y un objeto TextStamp usando las propiedades requeridas. Después de eso, puede llamar al método AddStamp de la Página para agregar el texto en el pie de página del PDF.

El siguiente fragmento de código le muestra cómo agregar texto en el pie de página de un archivo PDF con Java.

```java
    public static void AddingTextInFooterOfPDFFile() {
        // Abrir documento
        Document pdfDocument = new Document(_dataDir + "TextinFooter.pdf");
        // Crear pie de página
        TextStamp textStamp = new TextStamp("Texto del Pie de Página");
        // Establecer propiedades del sello
        textStamp.setBottomMargin(10);
        textStamp.setHorizontalAlignment(HorizontalAlignment.Center);
        textStamp.setVerticalAlignment(VerticalAlignment.Bottom);
        // Añadir pie de página en todas las páginas
        for (Page page : pdfDocument.getPages()) {
            page.addStamp(textStamp);
        }
        _dataDir = _dataDir + "TextinFooter_out.pdf";
        // Guardar archivo PDF actualizado
        pdfDocument.save(_dataDir);
    }
```


## Añadiendo Imagen en el Encabezado del Archivo PDF

Puede usar la clase [ImageStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/imagestamp) para agregar una imagen en el encabezado de un archivo PDF. La clase Image Stamp proporciona las propiedades necesarias para crear un sello basado en imagen como el tamaño de fuente, estilo de fuente y color de fuente, etc. Para agregar una imagen en el encabezado, necesita crear un objeto Document y un objeto Image Stamp usando las propiedades requeridas. Después de eso, puede llamar al método [AddStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/class-use/Stamp) de la página para agregar la imagen en el encabezado del PDF.

```java
public static void AddingImageInHeaderOfPDFFile() {

// Abrir documento
Document pdfDocument = new Document(_dataDir + "ImageInHeader.pdf");

// Crear encabezado
ImageStamp imageStamp = new ImageStamp(_dataDir + "aspose-logo.jpg");

// Establecer propiedades del sello
imageStamp.setTopMargin(10);
imageStamp.setHorizontalAlignment(HorizontalAlignment.Center);
imageStamp.setVerticalAlignment(VerticalAlignment.Top);
// Añadir encabezado en todas las páginas
for (Page page : pdfDocument.getPages()) {
page.addStamp(imageStamp);
}

_dataDir = _dataDir + "ImageInHeader_out.pdf";

// Guardar archivo PDF actualizado
pdfDocument.save(_dataDir);
}
```


El siguiente fragmento de código te muestra cómo agregar una imagen en el encabezado de un archivo PDF con Java.

## Agregar Imagen en el Pie de Página de un Archivo PDF

Puedes usar la clase Image Stamp para agregar una imagen en el pie de página de un archivo PDF. La clase Image Stamp proporciona las propiedades necesarias para crear un sello basado en imagen, como el tamaño de fuente, el estilo de fuente y el color de fuente, etc. Para agregar una imagen en el pie de página, necesitas crear un objeto Document y un objeto Image Stamp usando las propiedades requeridas. Después de eso, puedes llamar al método AddStamp de la Página para agregar la imagen en el pie de página del PDF.

{{% alert color="primary" %}}

Necesitas configurar la propiedad BottomMargin de tal manera que ajuste la imagen en el área del pie de página de tu PDF. También necesitas configurar [HorizontalAlignment](https://reference.aspose.com/pdf/java/com.aspose.pdf/HorizontalAlignment) a `Center` y [VerticalAlignment](https://reference.aspose.com/pdf/java/com.aspose.pdf/VerticalAlignment) a `Bottom`.

{{% /alert %}}

El siguiente fragmento de código te muestra cómo agregar una imagen en el pie de página de un archivo PDF con Java.

```java
    public static void AddingImageInFooterOfPDFFile() {

        // Abrir documento
        Document pdfDocument = new Document(_dataDir + "ImageInFooter.pdf");

        // Crear pie de página
        ImageStamp imageStamp = new ImageStamp(_dataDir + "aspose-logo.jpg");

        // Establecer propiedades del sello
        imageStamp.setBottomMargin(10);
        imageStamp.setHorizontalAlignment(HorizontalAlignment.Center);
        imageStamp.setVerticalAlignment(VerticalAlignment.Bottom);
        // Agregar pie de página en todas las páginas
        for (Page page : pdfDocument.getPages()) {
            page.addStamp(imageStamp);
        }

        _dataDir = _dataDir + "ImageInFooter_out.pdf";

        // Guardar archivo PDF actualizado
        pdfDocument.save(_dataDir);
    }
```

## Agregar diferentes encabezados en un archivo PDF

Sabemos que podemos agregar TextStamp en la sección de Encabezado/Pie de página del documento usando las propiedades TopMargin o Bottom Margin, pero a veces podemos tener el requisito de agregar múltiples encabezados/pies de página en un solo documento PDF.
 **Aspose.PDF for Java** explica cómo hacer esto.

Para cumplir con este requisito, crearemos objetos [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp) individuales (el número de objetos depende de la cantidad de encabezados/pies de página requeridos) y los añadiremos al documento PDF. También podemos especificar diferente información de formato para cada objeto de sello. En el siguiente ejemplo, hemos creado un objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) y tres objetos [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp) y luego hemos utilizado el método [AddStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/class-use/Stamp) de la Página para agregar el texto en la sección del encabezado del PDF. El siguiente fragmento de código muestra cómo agregar una imagen en el pie de página de un archivo PDF con Aspose.PDF para Java.

```java
public static void AddingDifferentHeadersInOnePDFFile() {

        // Abrir el documento fuente
        Document pdfDocument = new Document(_dataDir + "AddingDifferentHeaders.pdf");

        // Crear tres sellos
        TextStamp stamp1 = new TextStamp("Encabezado 1");
        TextStamp stamp2 = new TextStamp("Encabezado 2");
        TextStamp stamp3 = new TextStamp("Encabezado 3");

        // Establecer la alineación del sello (colocar el sello en la parte superior de la página, centrado horizontalmente)
        stamp1.setVerticalAlignment(VerticalAlignment.Top);
        stamp1.setHorizontalAlignment(HorizontalAlignment.Center);
        // Especificar el estilo de fuente como Negrita
        stamp1.getTextState().setFontStyle(FontStyles.Bold);
        // Establecer la información del color de primer plano del texto como rojo
        stamp1.getTextState().setForegroundColor(Color.getRed());
        // Especificar el tamaño de fuente como 14
        stamp1.getTextState().setFontSize(14);

        // Ahora necesitamos establecer la alineación vertical del segundo objeto de sello como Superior
        stamp2.setVerticalAlignment(VerticalAlignment.Top);
        // Establecer la información de alineación horizontal para el sello como Centrada
        stamp2.setHorizontalAlignment(HorizontalAlignment.Center);
        // Establecer el factor de zoom para el objeto de sello
        stamp2.setZoom(10);

        // Establecer el formato del tercer objeto de sello
        // Especificar la información de alineación vertical para el objeto de sello como SUPERIOR
        stamp3.setVerticalAlignment(VerticalAlignment.Top);
        // Establecer la información de alineación horizontal para el objeto de sello como Centrada
        stamp3.setHorizontalAlignment(HorizontalAlignment.Center);
        // Establecer el ángulo de rotación para el objeto de sello
        stamp3.setRotateAngle(35);
        // Establecer el color de fondo rosa para el sello
        stamp3.getTextState().setBackgroundColor(Color.getPink());
        
        // Cambiar la información de la fuente para el sello a Verdana
        stamp3.getTextState().setFont(FontRepository.findFont("Verdana"));
        // El primer sello se agrega en la primera página;
        pdfDocument.getPages().get_Item(1).addStamp(stamp1);
        // El segundo sello se agrega en la segunda página;
        pdfDocument.getPages().get_Item(2).addStamp(stamp2);
        // El tercer sello se agrega en la tercera página.
        pdfDocument.getPages().get_Item(3).addStamp(stamp3);

        _dataDir = _dataDir + "multiheader_out.pdf";

        // Guardar el archivo PDF actualizado
        pdfDocument.save(_dataDir);
    }

}
```