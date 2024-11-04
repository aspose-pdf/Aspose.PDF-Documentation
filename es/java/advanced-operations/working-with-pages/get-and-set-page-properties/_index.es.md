---
title: Obtener y Establecer Propiedades de Página
type: docs
weight: 30
url: /java/get-and-set-page-properties/
description: Este tema explica cómo obtener números en un archivo PDF, obtener propiedades de página y determinar el color de la página utilizando Aspose.PDF para Java.
lastmod: "2021-06-05"
---

Aspose.PDF para Java te permite leer y establecer propiedades de páginas en un archivo PDF en tus aplicaciones Java. Esta sección muestra cómo obtener el número de páginas en un archivo PDF, obtener información sobre propiedades de página del PDF como el color y establecer propiedades de página.

## Obtener Número de Páginas en un Archivo PDF

Cuando trabajas con documentos, a menudo quieres saber cuántas páginas contienen. Con Aspose.PDF esto no lleva más de dos líneas de código.

Para obtener el número de páginas en un archivo PDF:

1. Abre el archivo PDF usando la clase [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

1. Luego, use la propiedad Count de la colección [PageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/PageCollection) (del objeto Document) para obtener el número total de páginas en el documento.

El siguiente fragmento de código muestra cómo obtener el número de páginas de un archivo PDF.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

public class ExampleGetAndSetPageProperties {
    // La ruta al directorio de documentos.
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void GetNumberOfPagesInaPDFFile() {

        // Abrir documento
        Document pdfDocument = new Document(_dataDir + "GetNumberofPages.pdf");

        // Obtener el conteo de páginas
        System.out.println("Conteo de páginas : " + pdfDocument.getPages().size());
        _dataDir = _dataDir + "ApplyNumberStyle_out.pdf";
        pdfDocument.save(_dataDir);

    }
```

### Obtener el conteo de páginas sin guardar el documento

A menos que el archivo PDF sea guardado y todos los elementos estén realmente colocados dentro del archivo PDF, no podemos obtener el conteo de páginas para un documento en particular (porque no podemos estar seguros del número de páginas en las que todos los elementos serán acomodados).
 Sin embargo, a partir del lanzamiento de Aspose.PDF para Java 10.1.0, hemos introducido un método llamado [processParagraphs(...)](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#processParagraphs--) que proporciona la funcionalidad de obtener el conteo de páginas para el documento PDF, sin guardar el archivo. Así que podemos obtener la información del conteo de páginas al instante. Por favor, intente usar el siguiente fragmento de código para cumplir con este requisito.

```java
public static void GetPageCountWithoutSavingTheDocument() {

        // Para ejemplos completos y archivos de datos, por favor visite
        // https://github.com/aspose-pdf/Aspose.Pdf-for-Java
        // instanciar la instancia del Documento
        Document doc = new Document();
        // agregar página a la colección de páginas del archivo PDF
        Page page = doc.getPages().add();
        // crear un bucle para agregar 300 instancias de TextFragment
        for (int i = 0; i < 300; i++)
            // agregar TextFragment a la colección de párrafos de la primera página del PDF
            page.getParagraphs().add(new TextFragment("Prueba de conteo de páginas"));
        // procesar párrafos para obtener la información del conteo de páginas
        doc.processParagraphs();
        System.out.println("Número de páginas en PDF = " + doc.getPages().size());
    }
```

## Obtener Propiedades de la Página

Cada página en un archivo PDF tiene una serie de propiedades, como el ancho, la altura, bleed-, crop- y trimbox. Aspose.PDF te permite acceder a estas propiedades.

### **Comprendiendo las Propiedades de la Página: la Diferencia entre Artbox, BleedBox, CropBox, MediaBox, TrimBox y la propiedad Rect**

- **Media box**: El media box es la caja de página más grande. Corresponde al tamaño de la página (por ejemplo, A4, A5, Carta de EE. UU., etc.) seleccionado cuando el documento fue impreso en PostScript o PDF. En otras palabras, el media box determina el tamaño físico del medio en el que el documento PDF se muestra o imprime.
- **Bleed box**: Si el documento tiene sangrado, el PDF también tendrá un bleed box.
 Bleed es la cantidad de color (o arte) que se extiende más allá del borde de una página. Se utiliza para asegurarse de que cuando el documento se imprima y corte al tamaño deseado ("recortado"), la tinta llegue hasta el borde de la página. Incluso si la página se corta incorrectamente, ligeramente fuera de las marcas de recorte, no aparecerán bordes blancos en la página.
- **Trim box**: La caja de recorte indica el tamaño final de un documento después de imprimirlo y recortarlo.
- **Art box**: La caja de arte es la caja dibujada alrededor del contenido real de las páginas en sus documentos. Esta caja de página se utiliza al importar documentos PDF en otras aplicaciones.
- **Crop box**: La caja de recorte es el tamaño de "página" en el que su documento PDF se muestra en Adobe Acrobat. En vista normal, solo se muestran los contenidos de la caja de recorte en Adobe Acrobat.
  Para descripciones detalladas de estas propiedades, lea la especificación de Adobe.Pdf, particularmente 10.10.1 Límites de Página.
- **Page.Rect**: la intersección (rectángulo comúnmente visible) del MediaBox y DropBox. La imagen a continuación ilustra estas propiedades.

Para más detalles, por favor visite [esta página](http://www.enfocus.com/manuals/ReferenceGuide/PP/10/enUS/en-us/concept/c_aa1095731.html).

### Accediendo a las Propiedades de la Página

La clase [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) proporciona todas las propiedades relacionadas con una página PDF en particular. Todas las páginas de los archivos PDF están contenidas en la colección [PageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/PageCollection) del objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

Desde allí, es posible acceder a objetos Page individuales usando su índice, o recorrer la colección usando un bucle foreach para obtener todas las páginas. Una vez que se accede a una página individual, podemos obtener sus propiedades. El siguiente fragmento de código muestra cómo obtener propiedades de la página.

```java
    public static void AccessingPageProperties() {

        Document pdfDocument = new Document("input.pdf");

        // Obtener la colección de páginas
        PageCollection pageCollection = pdfDocument.getPages();

        // Obtener una página específica
        Page pdfPage = pageCollection.get_Item(1);

        // Obtener las propiedades de la página
        System.out.printf("\n ArtBox : Altura = " + pdfPage.getArtBox().getHeight() + ", Ancho = "
                + pdfPage.getArtBox().getWidth() + ", LLX = " + pdfPage.getArtBox().getLLX() + ", LLY = "
                + pdfPage.getArtBox().getLLY() + ", URX = " + pdfPage.getArtBox().getURX() + ", URY = "
                + pdfPage.getArtBox().getURY());
        System.out.printf("\n BleedBox : Altura = " + pdfPage.getBleedBox().getHeight() + ", Ancho = "
                + pdfPage.getBleedBox().getWidth() + ", LLX = " + pdfPage.getBleedBox().getLLX() + ", LLY = "
                + pdfPage.getBleedBox().getLLY() + ", URX = " + pdfPage.getBleedBox().getURX() + ", URY = "
                + pdfPage.getBleedBox().getURY());
        System.out.printf("\n CropBox : Altura = " + pdfPage.getCropBox().getHeight() + ", Ancho = "
                + pdfPage.getCropBox().getWidth() + ", LLX = " + pdfPage.getCropBox().getLLX() + ", LLY = "
                + pdfPage.getCropBox().getLLY() + ", URX = " + pdfPage.getCropBox().getURX() + ", URY = "
                + pdfPage.getCropBox().getURY());
        System.out.printf("\n MediaBox : Altura = " + pdfPage.getMediaBox().getHeight() + ", Ancho = "
                + pdfPage.getMediaBox().getWidth() + ", LLX = " + pdfPage.getMediaBox().getLLX() + ", LLY = "
                + pdfPage.getMediaBox().getLLY() + ", URX = " + pdfPage.getMediaBox().getURX() + ", URY = "
                + pdfPage.getMediaBox().getURY());
        System.out.printf("\n TrimBox : Altura = " + pdfPage.getTrimBox().getHeight() + ", Ancho = "
                + pdfPage.getTrimBox().getWidth() + ", LLX = " + pdfPage.getTrimBox().getLLX() + ", LLY = "
                + pdfPage.getTrimBox().getLLY() + ", URX = " + pdfPage.getTrimBox().getURX() + ", URY = "
                + pdfPage.getTrimBox().getURY());
        System.out.printf(
                "\n Rect : Altura = " + pdfPage.getRect().getHeight() + ", Ancho = " + pdfPage.getRect().getWidth()
                        + ", LLX = " + pdfPage.getRect().getLLX() + ", LLY = " + pdfPage.getRect().getLLY() + ", URX = "
                        + pdfPage.getRect().getURX() + ", URY = " + pdfPage.getRect().getURY());
        System.out.printf("\n Número de Página :- " + pdfPage.getNumber());
        System.out.printf("\n Rotar :-" + pdfPage.getRotate());
    }
```

## Determinar el Color de la Página

La clase [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) proporciona las propiedades relacionadas con una página en particular en un documento PDF, incluyendo qué tipo de color - RGB, blanco y negro, escala de grises o indefinido - utiliza la página.

Todas las páginas de los archivos PDF están contenidas en la colección [PageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageCollection). La propiedad [ColorType](https://reference.aspose.com/pdf/java/com.aspose.pdf/ColorType) especifica el color de los elementos en la página. Para obtener o determinar la información de color para una página PDF en particular, use la propiedad [ColorType](https://reference.aspose.com/pdf/java/com.aspose.pdf/ColorType) del objeto de la clase [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page).

El siguiente fragmento de código muestra cómo iterar a través de cada página del archivo PDF para obtener información de color.

```java
    public static void DeterminePageColor () {

        Document pdfDocument = new Document("input.pdf");
        // Iterar a través de todas las páginas del archivo PDF
        for (int pageCount = 1; pageCount <= pdfDocument.getPages().size(); pageCount++) {
            // Obtener la información del tipo de color para una página PDF en particular
            int pageColorType = pdfDocument.getPages().get_Item(pageCount).getColorType();
            switch (pageColorType) {
            case 2:
                System.out.println("Página # -" + pageCount + " es Blanco y negro..");
                break;
            case 1:
                System.out.println("Página # -" + pageCount + " es Escala de grises...");
                break;
            case 0:
                System.out.println("Página # -" + pageCount + " es RGB..");
                break;
            case 3:
                System.out.println("Página # -" + pageCount + " Color es indefinido..");
                break;
            }
        }
    }
}
```