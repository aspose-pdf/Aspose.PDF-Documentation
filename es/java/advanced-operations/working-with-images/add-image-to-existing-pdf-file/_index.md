---
title: Agregar Imagen a un Archivo PDF Existente
linktitle: Agregar Imagen
type: docs
weight: 10
url: /es/java/add-image-to-existing-pdf-file/
description: Esta sección describe cómo agregar una imagen a un archivo PDF existente usando la biblioteca de Java.
lastmod: "2021-06-05"
---

Cada página de PDF contiene propiedades de Recursos y Contenidos. Los recursos pueden ser imágenes y formularios, por ejemplo, mientras que el contenido está representado por un conjunto de operadores PDF. Cada operador tiene su nombre y argumento. Este ejemplo utiliza operadores para agregar una imagen a un archivo PDF.

Para agregar una imagen a un archivo PDF existente:

- Cree un objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) y abra el documento PDF de entrada.
- Obtenga la página a la que desea agregar una imagen.
- Agregue la imagen en la colección [getResources](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#getResources--) de la página.
- Use operadores para colocar la imagen en la página:
- Use el operador GSave para guardar el estado gráfico actual.

- Use el operador [ConcatenateMatrix](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators.class-use/concatenatematrix) para especificar dónde se colocará la imagen.
- Use el operador [Do](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/class-use/Do) para dibujar la imagen en la página.
- Finalmente, use el operador [GRestore](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators.class-use/grestore) para guardar el estado gráfico actualizado.
- Guarda el archivo.

El siguiente fragmento de código muestra cómo agregar la imagen en un documento PDF.

```java
package com.aspose.pdf.examples;

import java.awt.image.BufferedImage;
import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;

import javax.imageio.ImageIO;

import com.aspose.pdf.*;
import com.aspose.pdf.facades.PdfFileMend;
import com.aspose.pdf.operators.*;

public class ExampleAddImages {

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void AddImageToExistingPDF() throws IOException {
        // Abre un documento
        Document pdfDocument1 = new Document(_dataDir + "sample.pdf");

        // Establecer coordenadas
        int lowerLeftX = 50;
        int lowerLeftY = 750;
        int upperRightX = 100;
        int upperRightY = 800;

        // Obtén la página a la que deseas agregar la imagen
        Page page = pdfDocument1.getPages().get_Item(1);

        // Cargar imagen en el flujo
        java.io.FileInputStream imageStream = new java.io.FileInputStream(new java.io.File(_dataDir + "logo.png"));

        // Agregar una imagen a la colección de imágenes de los recursos de la página
        page.getResources().getImages().add(imageStream);

        // Usando el operador GSave: este operador guarda el estado gráfico actual
        page.getContents().add(new GSave());

        // Crear objetos Rectangle y Matrix
        Rectangle rectangle = new Rectangle(lowerLeftX, lowerLeftY, upperRightX, upperRightY);
        Matrix matrix = new Matrix(new double[] { rectangle.getURX() - rectangle.getLLX(), 0, 0,
                rectangle.getURY() - rectangle.getLLY(), rectangle.getLLX(), rectangle.getLLY() });

        // Usando el operador ConcatenateMatrix (concatenar matriz): define cómo debe
        // colocarse la imagen
        page.getContents().add(new ConcatenateMatrix(matrix));
        XImage ximage = page.getResources().getImages().get_Item(page.getResources().getImages().size());

        // Usando el operador Do: este operador dibuja la imagen
        page.getContents().add(new Do(ximage.getName()));

        // Usando el operador GRestore: este operador restaura el estado gráfico
        page.getContents().add(new GRestore());

        // Guardar el nuevo PDF
        pdfDocument1.save(_dataDir + "updated_document.pdf");

        // Cerrar flujo de imagen
        imageStream.close();
    }
```


## Añadiendo imagen desde BufferedImage en PDF

A partir del lanzamiento de Aspose.PDF para Java 9.5.0, hemos introducido el soporte para añadir una imagen desde una instancia de BufferedImage al documento PDF. Para cumplir con este requisito, se ha implementado un método: [XImageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/XImageCollection).add(BufferedImage image);

```java
    public static void AddingImageFromBufferedImageIntoPDF() throws IOException {
        BufferedImage originalImage = ImageIO.read(new File("anyImage.jpg"));
        Document pdfDocument = new Document();
        Page page = pdfDocument.getPages().add();
        page.getResources().getImages().add(originalImage);
    }
```
Puede usar cualquier InputStream y no solo el objeto FileInputStream para añadir la imagen. Así que cuando use el objeto java.io.ByteArrayInputStream, no necesita almacenar ningún archivo en el sistema:

```java
    public static void AddingImageFromBufferedImageIntoPDF2() throws IOException {
        BufferedImage originalImage = ImageIO.read(new File("anyImage.jpg"));
        ByteArrayOutputStream baos = new ByteArrayOutputStream();

        Document pdfDocument = new Document();
        ImageIO.write(originalImage, "jpg", baos);
        baos.flush();
        Page page = pdfDocument.getPages().get_Item(1);
        page.getResources().getImages().add(new ByteArrayInputStream(baos.toByteArray()));
    }
```


## Añadir Imagen en un Archivo PDF Existente (Facades)

También hay una manera alternativa y más fácil de añadir una Imagen a un archivo PDF. Puedes usar el método AddImage de la clase [PdfFileMend](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileMend). El método AddImage requiere la imagen a añadir, el número de página en la que se necesita añadir la imagen y la información de las coordenadas. Después de eso, guarda el archivo PDF actualizado usando el método Close.

El siguiente fragmento de código te muestra cómo añadir una imagen en un archivo PDF existente.

```java
    public static void AddImageInAnExistingPDFFile_Facades() {
        // Abrir documento
        PdfFileMend mender = new PdfFileMend();

        // Crear objeto PdfFileMend para añadir texto
        mender.bindPdf(_dataDir + "AddImage.pdf");

        // Añadir imagen en el archivo PDF
        mender.addImage(_dataDir + "aspose-logo.jpg", 1, 100, 600, 200, 700);

        // Guardar cambios
        mender.save(_dataDir + "AddImage_out.pdf");

        // Cerrar objeto PdfFileMend
        mender.close();
    }
```


## Agregar Referencia de una sola Imagen múltiples veces en un Documento PDF

A veces tenemos el requisito de usar la misma imagen varias veces en un documento PDF. Agregar una nueva instancia aumenta el documento PDF resultante. Hemos añadido un nuevo método XImageCollection.add(XImage) que soporta el objeto Ximage para añadir en la Colección de Imágenes. Este método permite agregar referencia al mismo objeto PDF como imagen original que optimiza el tamaño del Documento PDF.

```java
    public static void AddReferenceOfaSingleImageMultipleTimes() throws FileNotFoundException {
        Rectangle imageRectangle = new Rectangle(0, 0, 30, 15);
        Document document = new Document(_dataDir + "sample.pdf");
        document.getPages().add();
        document.getPages().add();
        java.io.FileInputStream imageStream = new java.io.FileInputStream(
                new java.io.File(_dataDir + "aspose-logo.png"));

        XImage image = null;

        for (Page page : document.getPages()) {
            WatermarkAnnotation annotation = new WatermarkAnnotation(page, page.getRect());
            XForm form = annotation.getAppearance().get_Item("N");
            form.setBBox(page.getRect());
            String name;
            if (image == null) {
                name = form.getResources().getImages().add(imageStream);
                image = form.getResources().getImages().get_Item(name);
            } else {
                name = form.getResources().getImages().add(image);
            }
            form.getContents().add(new GSave());
            form.getContents().add(new ConcatenateMatrix(
                    new Matrix(imageRectangle.getWidth(), 0, 0, imageRectangle.getHeight(), 0, 0)));
            form.getContents().add(new Do(name));
            form.getContents().add(new GRestore());
            page.getAnnotations().add(annotation, false);
            imageRectangle = new Rectangle(0, 0, imageRectangle.getWidth() * 1.01, imageRectangle.getHeight() * 1.01);
        }
        document.save(_dataDir + "output.pdf");
    }
```


## Identificar si la imagen dentro del PDF es en Color o en Blanco y Negro

Diferentes tipos de compresión pueden aplicarse sobre las imágenes para reducir su tamaño. El tipo de compresión que se aplica a una imagen depende del Espacio de Color de la imagen fuente, es decir, si la imagen es en Color (RGB), entonces se aplica la compresión JPEG2000, y si es en Blanco y Negro, entonces se debe aplicar la compresión JBIG2/JBIG2000. Por lo tanto, identificar cada tipo de imagen y usar un tipo de compresión apropiado creará el mejor/optimizado resultado.

Un archivo PDF puede contener elementos como Texto, Imagen, Gráfico, Adjunto, Anotación, etc., y si el archivo PDF fuente contiene imágenes, podemos determinar el espacio de color de la imagen y aplicar la compresión apropiada para la imagen para reducir el tamaño del archivo PDF. El siguiente fragmento de código muestra los pasos para identificar si la imagen dentro del PDF es en Color o en Blanco y Negro.

```java
    public static void CheckColors() {

        Document document = new Document(_dataDir + "test4.pdf");
        try {
            // iterar a través de todas las páginas del archivo PDF
            for (Page page : (Iterable<Page>) document.getPages()) {
                // crear una instancia del Absorbedor de Colocación de Imágenes
                ImagePlacementAbsorber abs = new ImagePlacementAbsorber();
                page.accept(abs);
                for (ImagePlacement ia : (Iterable<ImagePlacement>) abs.getImagePlacements()) {
                    /* Tipo de Color */
                    int colorType = ia.getImage().getColorType();
                    switch (colorType) {
                    case ColorType.Grayscale:
                        System.out.println("Imagen en Escala de Grises");
                        break;
                    case ColorType.Rgb:
                        System.out.println("Imagen en Color");
                        break;
                    }
                }
            }
        } catch (Exception ex) {
            System.out.println("Error al leer el archivo = " + document.getFileName());
        }
    }
}
```