---
title: Convertir varios formatos de imágenes a PDF
linktitle: Convertir Imágenes a PDF
type: docs
weight: 60
url: /es/java/convert-images-format-to-pdf/
lastmod: "2021-11-19"
description: Este tema muestra cómo la biblioteca Aspose.PDF para Java permite convertir varios formatos de imágenes a PDF.
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

**Aspose.PDF para Java** te permite convertir diferentes formatos de imágenes a archivos PDF. Nuestra biblioteca demuestra fragmentos de código para convertir los formatos de imagen más populares, como - formatos BMP, CGM, DICOM, EMF, JPG, PNG, SVG y TIFF.

## Convertir BMP a PDF

Convierte archivos BMP a documentos PDF usando la biblioteca **Aspose.PDF para Java**.

Las imágenes <abbr title="Archivo de Imagen de Mapa de Bits">BMP</abbr> son archivos con la extensión .BMP que representan archivos de imagen de mapa de bits que se utilizan para almacenar imágenes digitales de mapa de bits. Estas imágenes son independientes del adaptador gráfico y también se llaman formato de archivo de mapa de bits independiente del dispositivo (DIB). Puedes convertir BMP a PDF con la API Aspose.PDF para Java.
 Por lo tanto, puedes seguir los siguientes pasos para convertir imágenes BMP:

1. Inicializa un nuevo Documento
1. Carga el archivo de imagen BMP de muestra
1. Finalmente, guarda el archivo PDF de salida

Así que el siguiente fragmento de código sigue estos pasos y muestra cómo convertir BMP a PDF usando Java:

```java
package com.aspose.pdf.examples;

import java.io.FileNotFoundException;
import java.nio.file.Path;
import java.nio.file.Paths;

import com.aspose.pdf.*;

public final class ConvertBMPtoPDF {

    private ConvertBMPtoPDF() {
    }

    private static Path _dataDir = Paths.get("<set path to samples>");

    public static void main(String[] args) throws FileNotFoundException {
        // Inicializa el objeto documento
        Document document = new Document();

        Page page = document.getPages().add();        
        Image image = new Image();
        
        // Carga el archivo de imagen BMP de muestra
        image.setFile(Paths.get(_dataDir.toString(), "Sample.bmp").toString());
        page.getParagraphs().add(image);
        
        // Guarda el documento PDF de salida
        document.save(Paths.get(_dataDir.toString(),"BMPtoPDF.pdf").toString());
    }
}
```

{{% alert color="success" %}}
**Intenta convertir BMP a PDF en línea**

Aspose te presenta una aplicación en línea gratuita ["BMP a PDF"](https://products.aspose.app/pdf/conversion/bmp-to-pdf/), donde puedes intentar investigar la funcionalidad y calidad con la que funciona.

[![Aspose.PDF Convertion BMP to PDF using Free App](bmp_to_pdf.png)](https://products.aspose.app/pdf/conversion/bmp-to-pdf/)
{{% /alert %}}

## Convertir CGM a PDF

<abbr title="Metarchivo de Gráficos por Computadora">CGM</abbr> es un estándar ISO que proporciona un formato de archivo de imagen 2D basado en vectores para el almacenamiento y recuperación de información gráfica. CGM es un formato independiente del dispositivo. CGM es un formato de gráficos vectoriales que soporta tres métodos de codificación diferentes: binario (mejor para la velocidad de lectura de programas), basado en caracteres (produce el tamaño de archivo más pequeño y permite transferencias de datos más rápidas) o codificación de texto claro (permite a los usuarios leer y modificar el archivo con un editor de texto).

El siguiente fragmento de código te muestra cómo convertir archivos CGM a formato PDF usando Aspose.PDF para Java.

1. Crear una clase [CgmLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/cgmloadoptions/).
1. Crear una instancia de la clase [Document](https://reference.aspose.com/page/java/com.aspose.page/Document) con el nombre de archivo de origen mencionado y las opciones.
1. Guardar el documento con el nombre de archivo deseado.

```java
package com.aspose.pdf.examples;

import java.io.FileNotFoundException;
import java.nio.file.Path;
import java.nio.file.Paths;

import com.aspose.pdf.*;

public final class ConvertCGMtoPDF {

    private ConvertCGMtoPDF() {
    }

    private static Path _dataDir = Paths.get("/home/admin1/pdf-examples/Samples");

    public static void main(String[] args) throws FileNotFoundException {
        
        // Crear opciones de carga CGM
        CgmLoadOptions options = new CgmLoadOptions();

        // Inicializar objeto de documento
        String cgmFileName = Paths.get(_dataDir.toString(), "corvette.cgm").toString();
        Document document = new Document(cgmFileName, options);

        // Guardar documento PDF de salida
        document.save(Paths.get(_dataDir.toString(),"CGMtoPDF.pdf").toString());
    }
}
```


## Convertir DICOM a PDF

<abbr title="Digital Imaging and Communications in Medicine">DICOM</abbr> es un estándar para manejar, almacenar, imprimir y transmitir información en imágenes médicas. Incluye una definición de formato de archivo y un protocolo de comunicación de red.

Aspose.PDF para Java te permite convertir archivos DICOM a formato PDF, revisa el siguiente fragmento de código:

1. Cargar imagen en el flujo
1. Inicializar [objeto Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document)
1. Cargar archivo de imagen DICOM de muestra
1. Guardar documento PDF de salida

```java
package com.aspose.pdf.examples;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.nio.file.Path;
import java.nio.file.Paths;

import com.aspose.pdf.*;

public final class ConvertDICOMtoPDF {

    private ConvertDICOMtoPDF() {
    }

    private static Path _dataDir = Paths.get("/home/admin1/pdf-examples/Samples");

    public static void main(String[] args) throws FileNotFoundException {
        
        // Cargar imagen en el flujo
        FileInputStream imageStream = new FileInputStream(
            new java.io.File(Paths.get(_dataDir.toString(),"0002.dcm").toString()));

        // Inicializar objeto documento
        Document document = new Document();
        document.getPages().add();
        
        // Cargar archivo de imagen DICOM de muestra
        Image image = new Image();
        image.setFileType(ImageFileType.Dicom);
        image.setImageStream(imageStream);

        document.getPages().get_Item(1).getParagraphs().add(image);

        // Guardar documento PDF de salida
        document.save(Paths.get(_dataDir.toString(),"CGMtoPDF.pdf").toString());
    }
}
```


{{% alert color="success" %}}
**Intenta convertir DICOM a PDF en línea**

Aspose te presenta una aplicación gratuita en línea ["DICOM a PDF"](https://products.aspose.app/pdf/conversion/dicom-to-pdf/), donde puedes intentar investigar la funcionalidad y calidad con la que trabaja.

[![Conversión Aspose.PDF de DICOM a PDF usando App Gratuita](dicom_to_pdf.png)](https://products.aspose.app/pdf/conversion/dicom-to-pdf/)
{{% /alert %}}

## Convertir EMF a PDF

El formato de metarchivo mejorado (<abbr title="Enhanced metafile format">EMF</abbr>) almacena imágenes gráficas de forma independiente del dispositivo. Los metarchivos EMF comprenden registros de longitud variable en orden cronológico que pueden renderizar la imagen almacenada después de analizarse en cualquier dispositivo de salida.

Tenemos varios enfoques para convertir EMF en PDF.

## Usando la clase Image

Un documento PDF comprende páginas y cada página contiene uno o más objetos de párrafo. Un párrafo puede ser un texto, imagen, tabla, cuadro flotante, gráfico, encabezado, campo de formulario o un archivo adjunto.

Para convertir un archivo de imagen en formato PDF, encierra la imagen en un párrafo.

Es posible convertir imágenes en una ubicación física en el disco duro local, encontradas en una URL web o en una instancia de Stream.

Para agregar una imagen:

1. Cree un objeto de la clase com.aspose.pdf.Image.
1. Agregue la imagen a una colección [Paragraphs](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/paragraphs) de una instancia de página.
1. Especifique la ruta o fuente de la imagen.
    - Si una imagen está en una ubicación en el disco duro, especifique la ubicación de la ruta utilizando el método [Image.setFile(…)](https://reference.aspose.com/pdf/java/com.aspose.pdf/Image).
    - Si una imagen se coloca en un FileInputStream, pase el objeto que contiene la imagen al método [Image.setImageStream(…)](https://reference.aspose.com/pdf/java/com.aspose.pdf/Image).

El siguiente fragmento de código muestra cómo cargar un objeto de imagen, establecer el margen de página, colocar la imagen en la página y guardar el resultado como PDF.

```java
package com.aspose.pdf.examples;

import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;
import java.io.File;

/**
 * Convertir EMF a PDF
 */

import java.io.FileNotFoundException;
import java.io.IOException;
import java.nio.file.Path;
import java.nio.file.Paths;

import javax.imageio.ImageIO;

import com.aspose.pdf.*;

public final class ConvertEMFtoPDF {

    private ConvertEMFtoPDF() {
    }

    private static Path _dataDir = Paths.get("/home/admin1/pdf-examples/Samples");

    public static void main(String[] args) throws IOException {

        convertEMFtoPDF_01();
        convertEMFtoPDF_02();
    }

    

    public static void convertEMFtoPDF_01() throws FileNotFoundException {                
        // Instanciar objeto Document
        Document doc = new Document();
        // Agregar una página a la colección de páginas del documento
        Page page = doc.getPages().add();
        // Cargar el archivo de imagen de origen en el objeto Stream
        java.io.FileInputStream fs = new java.io.FileInputStream(
            Paths.get(_dataDir.toString(),"source.emf").toString());

        // Establecer márgenes para que la imagen quepa, etc.
        page.getPageInfo().getMargin().setBottom(0);
        page.getPageInfo().getMargin().setTop(0);
        page.getPageInfo().getMargin().setLeft(0);
        page.getPageInfo().getMargin().setRight(0);

        page.setCropBox(new Rectangle(0, 0, 400, 400));
        // Crear un objeto de imagen
        Image image1 = new Image();
        // Agregar la imagen en la colección de párrafos de la sección
        page.getParagraphs().add(image1);
        // Establecer el flujo de archivo de imagen
        image1.setImageStream(fs);
        // Guardar el archivo PDF resultante
        doc.save("EMFtoPDF_01.pdf");
    }   
    public static void convertEMFtoPDF_02() throws IOException {
        // ver código abajo
    } 
}
```


### Agregar imagen desde BufferedImage

Aspose.PDF para Java también ofrece la función de cargar una imagen desde una instancia de Stream donde una imagen puede cargarse en un objeto BufferedImage y colocarse dentro de la colección de párrafos del archivo Pdf.

```java
public static void convertEMFtoPDF_02() throws IOException {    
    Document doc = new Document();
    // agregar una página a la colección de páginas del archivo Pdf
    Page page = doc.getPages().add();
    // crear instancia de imagen
    Image image1 = new Image();
    // crear instancia de BufferedImage
    java.awt.image.BufferedImage bufferedImage = ImageIO.read(new File("source.emf"));
    ByteArrayOutputStream baos = new ByteArrayOutputStream();
    // escribir imagen en buffer a instancia de OutputStream
    ImageIO.write(bufferedImage, "emf", baos);
    baos.flush();
    ByteArrayInputStream bais = new ByteArrayInputStream(baos.toByteArray());
    // agregar imagen a la colección de párrafos de la primera página
    page.getParagraphs().add(image1);
    // establecer flujo de imagen como OutputStream que contiene imagen en buffer
    image1.setImageStream(bais);
    // guardar el archivo PDF resultante
    doc.save("BufferedImage.pdf");
}
```


## Agregar Imagen usando Operadores PDF

Cada objeto de página de PDF contiene los métodos [getResources()](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#getResources--) y [getContents()](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#getContents--). Los recursos pueden ser imágenes y formularios, por ejemplo, mientras que el contenido está representado por un conjunto de operadores PDF. Cada operador tiene su propio nombre y argumento.

Este ejemplo utiliza operadores para agregar una imagen a un archivo PDF.

Para agregar una imagen a un archivo PDF existente:

1. Cree un objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) y abra el documento PDF de entrada.
1. Obtenga la página a la que desea agregar una imagen.
1. Agregue la imagen a la colección [getResources()](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#getResources--) de la página.
1. Use operadores para colocar la imagen en la página:
   1. Use el operador GSave para guardar el estado gráfico actual.
   1. Use el operador ConcatenateMatrix para especificar dónde se colocará la imagen.

1. Usa el operador Do para dibujar la imagen en la página.
1. Finalmente, usa el operador GRestore para guardar el estado gráfico actualizado.
1. Guarda el archivo.

El siguiente fragmento de código muestra cómo agregar una imagen a un documento PDF.

```java
// Para ejemplos completos y archivos de datos, por favor visita https://github.com/aspose-pdf/Aspose.Pdf-for-Java
// Abre un documento
Document pdfDocument1 = new Document("input.pdf");

// Establecer coordenadas
int lowerLeftX = 100;
int lowerLeftY = 100;
int upperRightX = 200;
int upperRightY = 200;

// Obtener la página a la que quieres agregar la imagen
Page page = pdfDocument1.getPages().get_Item(1);

// Cargar imagen en el flujo
java.io.FileInputStream imageStream = new java.io.FileInputStream(new java.io.File("input_image1.jpg"));

// Agregar una imagen a la colección de Imágenes de los recursos de la página
page.getResources().getImages().add(imageStream);

// Usando el operador GSave: este operador guarda el estado gráfico actual
page.getContents().add(new Operator.GSave());

// Crear objetos Rectangle y Matrix
Rectangle rectangle = new Rectangle(lowerLeftX, lowerLeftY, upperRightX, upperRightY);
Matrix matrix = new Matrix(new double[] { rectangle.getURX() - rectangle.getLLX(), 0, 0, rectangle.getURY() - rectangle.getLLY(), rectangle.getLLX(), rectangle.getLLY() });

// Usando el operador ConcatenateMatrix (concatenar matriz): define cómo debe colocarse la imagen
page.getContents().add(new Operator.ConcatenateMatrix(matrix));
XImage ximage = page.getResources().getImages().get_Item(page.getResources().getImages().size());

// Usando el operador Do: este operador dibuja la imagen
page.getContents().add(new Operator.Do(ximage.getName()));

// Usando el operador GRestore: este operador restaura el estado gráfico
page.getContents().add(new Operator.GRestore());

// Guardar el nuevo PDF
pdfDocument1.save("Updated_document.pdf");

// Cerrar flujo de imagen
imageStream.close();
```


{{% alert color="success" %}}
**Intenta convertir EMF a PDF en línea**

Aspose te presenta la aplicación gratuita en línea ["EMF to PDF"](https://products.aspose.app/pdf/conversion/emf-to-pdf/), donde puedes intentar investigar la funcionalidad y calidad con la que trabaja.

[![Aspose.PDF Convertion EMF to PDF using Free App](emf_to_pdf.png)](https://products.aspose.app/pdf/conversion/emf-to-pdf/)
{{% /alert %}}

## Convertir JPG a PDF

No necesitas preguntarte cómo convertir JPG a PDF, porque la biblioteca Apose.PDF para Java tiene la mejor solución.

Puedes convertir muy fácilmente imágenes JPG a PDF con Aspose.PDF para Java siguiendo estos pasos:

1. Inicializa un objeto de la clase [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document)
1. Carga la imagen JPG y añádela al párrafo
1. Guarda el PDF de salida

El fragmento de código a continuación muestra cómo convertir una imagen JPG a PDF usando Java:

```java
package com.aspose.pdf.examples;

import java.io.FileNotFoundException;
import java.nio.file.Path;
import java.nio.file.Paths;

import com.aspose.pdf.*;

public final class ConvertJPEGtoPDF {

    private static Path _dataDir = Paths.get("/home/aspose/pdf-examples/Samples");

    public static void main(String[] args) throws FileNotFoundException {
        // Inicializar objeto documento
        Document document = new Document();

        Page page = document.getPages().add();
        Image image = new Image();

        // Cargar archivo de imagen JPEG de ejemplo
        image.setFile(Paths.get(_dataDir.toString(), "Sample.jpg").toString());
        page.getParagraphs().add(image);

        // Guardar documento PDF de salida
        document.save(Paths.get(_dataDir.toString(),"JPEGtoPDF.pdf").toString());
    }
}
```


{{% alert color="success" %}}
**Intenta convertir JPG a PDF en línea**

Aspose te presenta la aplicación gratuita en línea ["JPG a PDF"](https://products.aspose.app/pdf/conversion/jpg-to-pdf/), donde puedes intentar investigar la funcionalidad y calidad con la que trabaja.

[![Conversión Aspose.PDF de JPG a PDF usando la aplicación gratuita](jpg_to_pdf.png)](https://products.aspose.app/pdf/conversion/jpg-to-pdf/)
{{% /alert %}}

## Convertir PNG a PDF

**Aspose.PDF para Java** soporta la función de convertir imágenes PNG a formato PDF. Revisa el siguiente fragmento de código para realizar tu tarea.

<abbr title="Portable Network Graphics">PNG</abbr> se refiere a un tipo de formato de archivo de imagen ráster que utiliza compresión sin pérdida, lo que lo hace popular entre sus usuarios.

Puedes convertir una imagen PNG a PDF utilizando los siguientes pasos:

1. Cargar la imagen PNG de entrada
1. Leer los valores de altura y anchura
1. Crear un nuevo documento y agregar una página
1. Establecer las dimensiones de la página
1. Guardar el archivo de salida

Además, el fragmento de código a continuación muestra cómo convertir PNG a PDF en tus aplicaciones Java:

```java
package com.aspose.pdf.examples;

/**
 * Convertir PNG a PDF
 */

import java.io.FileNotFoundException;
import java.nio.file.Path;
import java.nio.file.Paths;

import com.aspose.pdf.*;

public final class ConvertPNGtoPDF {

    private ConvertPNGtoPDF() {
    }

    private static Path _dataDir = Paths.get("/home/admin1/pdf-examples/Samples");

    public static void main(String[] args) throws FileNotFoundException {
        // Inicializar el objeto documento
        Document document = new Document();

        Page page = document.getPages().add();
        Image image = new Image();

        // Cargar el archivo de imagen BMP de muestra
        image.setFile(Paths.get(_dataDir.toString(), "Sample.png").toString());


        page.getPageInfo().getMargin().setBottom(0);
        page.getPageInfo().getMargin().setTop(0);
        page.getPageInfo().getMargin().setRight(0);
        page.getPageInfo().getMargin().setLeft(0);
        page.getParagraphs().add(image);

        // Guardar el documento PDF de salida
        document.save(Paths.get(_dataDir.toString(), "PNGtoPDF.pdf").toString());
    }
}

```


{{% alert color="success" %}}
**Intenta convertir PNG a PDF en línea**

Aspose te presenta una aplicación gratuita en línea ["PNG a PDF"](https://products.aspose.app/pdf/conversion/png-to-pdf/), donde puedes intentar investigar la funcionalidad y calidad con la que trabaja.

[![Aspose.PDF Conversión PNG a PDF usando aplicación gratuita](png_to_pdf.png)](https://products.aspose.app/pdf/conversion/png-to-pdf/)
{{% /alert %}}

## Convertir SVG a PDF

Gráficos Vectoriales Escalables (SVG) es una familia de especificaciones de un formato de archivo basado en XML para gráficos vectoriales bidimensionales, tanto estáticos como dinámicos (interactivos o animados). La especificación SVG es un estándar abierto que ha estado en desarrollo por el Consorcio World Wide Web (W3C) desde 1999.

Las imágenes SVG y sus comportamientos se definen en archivos de texto XML.
 Esto significa que pueden ser buscados, indexados, guionizados y, si es necesario, comprimidos. Como archivos XML, las imágenes SVG pueden ser creadas y editadas con cualquier editor de texto, pero a menudo es más conveniente crearlas con programas de dibujo como Inkscape.

## Cómo convertir un archivo SVG al formato PDF

Para convertir archivos SVG a PDF, utiliza la clase llamada [SvgLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/svgloadoptions) que se usa para inicializar el objeto [LoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/LoadOptions). Más tarde, este objeto se pasa como un argumento durante la inicialización del objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document) y ayuda al motor de renderizado de PDF a determinar el formato de entrada del documento fuente.

El siguiente fragmento de código muestra el proceso de conversión de un archivo SVG al formato PDF.

```java
// Inicializar objeto de documento

String pdfDocumentFileName = Paths.get(_dataDir.toString(), "svg_test.pdf").toString();
String svgDocumentFileName = Paths.get(_dataDir.toString(), "car.svg").toString();

SvgLoadOptions option = new SvgLoadOptions();
Document pdfDocument = new Document(svgDocumentFileName, option);
pdfDocument.save(pdfDocumentFileName);
```

{{% alert color="success" %}}
**Intenta convertir el formato SVG a PDF en línea**

Aspose.PDF para Java te ofrece una aplicación en línea gratuita ["SVG a PDF"](https://products.aspose.app/pdf/conversion/svg-to-pdf), donde puedes probar la funcionalidad y calidad con la que trabaja.

[![Conversión de Aspose.PDF de SVG a PDF con Aplicación Gratuita](svg_to_pdf.png)](https://products.aspose.app/pdf/conversion/svg-to-pdf)
{{% /alert %}}

## Convertir TIFF a PDF

**Aspose.PDF para Java** admite el formato de archivo, ya sea una imagen <abbr title="Tag Image File Format">TIFF</abbr> de un solo cuadro o de varios cuadros. Esto significa que puedes convertir la imagen TIFF a PDF en tus aplicaciones Java.

TIFF o TIF, Formato de Archivo de Imagen Etiquetada, representa imágenes ráster que están destinadas a ser usadas en una variedad de dispositivos que cumplen con este estándar de formato de archivo.
 TIFF image puede contener varios cuadros con diferentes imágenes. El formato de archivo Aspose.PDF también es compatible, ya sea una imagen TIFF de un solo cuadro o de múltiples cuadros. Por lo tanto, puedes convertir la imagen TIFF a PDF en tus aplicaciones Java. Por lo tanto, consideraremos un ejemplo de conversión de imagen TIFF de varias páginas a documento PDF de varias páginas con los siguientes pasos:

1. Instanciar una instancia de la clase Document
1. Cargar la imagen TIFF de entrada
1. Finalmente, guardar la imagen como página PDF

Además, el siguiente fragmento de código muestra cómo convertir una imagen TIFF de varias páginas o de múltiples cuadros a PDF:

```java
import com.aspose.pdf.Document;
import com.aspose.pdf.Image;
import com.aspose.pdf.Page;

import java.io.IOException;
import java.nio.file.Path;
import java.nio.file.Paths;

/**
 * Convertir TIFF a PDF.
 */
public final class ConvertTIFFtoPDF {

    private static final Path DATA_DIR = Paths.get("/home/aspose/pdf-examples/Samples");

    private ConvertTIFFtoPDF() {
    }

    public static void run() throws IOException {
        // Inicializar objeto de documento
        Document document = new Document();

        Page page = document.getPages().add();
        Image image = new Image();

        image.setFile(Paths.get(DATA_DIR.toString(), "Sample.tiff").toString());
        page.getParagraphs().add(image);

        // Guardar documento PDF de salida
        document.save(Paths.get(DATA_DIR.toString(), "TIFFtoPDF.pdf").toString());
        document.close();
    }    
}
```