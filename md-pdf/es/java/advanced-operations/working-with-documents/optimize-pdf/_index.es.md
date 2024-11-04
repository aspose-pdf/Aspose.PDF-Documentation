---
title: Optimize, Compress or Reduce PDF Size in Java
linktitle: Optimize PDF Document
type: docs
weight: 40
url: /java/optimize-pdf/
description: Optimizar archivo PDF, reducir el tamaño de todas las imágenes, reducir tamaño PDF, quitar incrustación de fuentes, eliminar objetos no utilizados con Java.
lastmod: "2021-06-05"
---

Un documento PDF a veces puede contener datos adicionales. Reducir el tamaño de un archivo PDF te ayudará a optimizar la transferencia de red y el almacenamiento. Esto es especialmente útil para publicar en páginas web, compartir en redes sociales, enviar por correo electrónico o archivar en almacenamiento. Podemos usar varias técnicas para optimizar PDF:

- Optimizar el contenido de la página para navegación en línea
- Reducir o comprimir todas las imágenes
- Habilitar la reutilización del contenido de la página
- Combinar flujos duplicados
- Quitar incrustación de fuentes
- Eliminar objetos no utilizados
- Eliminar o aplanar los campos de formulario
- Eliminar o aplanar anotaciones

## Optimizar Documento PDF para la Web

La optimización o linealización se refiere al proceso de hacer que un archivo PDF sea adecuado para la navegación en línea usando un navegador web.
 Aspose.PDF soporta este proceso.

Para optimizar un PDF para visualización en la web:

1. Abre el documento de entrada en un objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).
1. Utiliza el método [optimize()](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#optimize--).
1. Guarda el documento optimizado utilizando el método save(..).

El siguiente fragmento de código muestra cómo optimizar un documento PDF para la web.

```java
package com.aspose.pdf.examples;

import java.io.FileNotFoundException;
import java.time.Clock;
import java.time.Duration;

import com.aspose.pdf.*;
import com.aspose.pdf.optimization.ImageCompressionVersion;
import com.aspose.pdf.optimization.ImageEncoding;

public class ExampleOptimize {

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void OptimizePDFDocumentForTheWeb() {

        // Abrir documento
        Document pdfDocument = new Document(_dataDir + "sample.pdf");

        // Optimizar para la web
        pdfDocument.optimize();

        // Guardar documento de salida
        pdfDocument.save(_dataDir + "OptimizeDocument_out.pdf");
    }
```

## Reducir el Tamaño del Archivo PDF

Este tema explica los pasos para optimizar/reducir el tamaño del archivo PDF. La API Aspose.PDF proporciona la clase [OptimizationOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf.optimization/class-use/OptimizationOptions) que ofrece la flexibilidad para optimizar el PDF de salida eliminando objetos innecesarios y comprimiendo archivos PDF que tienen imágenes. Ambas opciones se explican en las siguientes secciones.

### Eliminar Objetos Innecesarios
Podemos optimizar el tamaño de los documentos PDF eliminando objetos duplicados y no utilizados. El siguiente fragmento de código muestra cómo.

```java
public static void ReduceSizePDF() {

        // Abrir documento
        Document pdfDocument = new Document(_dataDir + "sample.pdf");

        // Optimizar documento PDF. Sin embargo, tenga en cuenta que este método no puede garantizar
        // la reducción del documento
        pdfDocument.optimizeResources();

        // Guardar documento de salida
        pdfDocument.save(_dataDir + "OptimizeDocument_out.pdf");
    }
```

## Reducir o Comprimir Todas las Imágenes

Si el archivo PDF de origen contiene imágenes, considera comprimir las imágenes y ajustar su calidad. Para habilitar la compresión de imágenes, pasa true como argumento al método setCompressImages(..). Todas las imágenes en un documento serán re-comprimidas. La compresión se define mediante el método setImageQuality(..), que es el valor de la calidad en porcentaje. 100% es calidad y tamaño de imagen sin cambios. Para disminuir el tamaño de la imagen, pasa un argumento menor de 100 al método setImageQuality(..).

```java
public static void ShrinkingCompressing() {
        // Abrir documento
        Document pdfDocument = new Document(_dataDir + "Shrinkimage.pdf");

        // Inicializar OptimizationOptions
        com.aspose.pdf.optimization.OptimizationOptions optimizationOptions = new com.aspose.pdf.optimization.OptimizationOptions();

        // Establecer opción CompressImages
        optimizationOptions.getImageCompressionOptions().setCompressImages(true);

        // Establecer opción ImageQuality
        optimizationOptions.getImageCompressionOptions().setImageQuality(50);

        // Optimizar documento PDF utilizando OptimizationOptions
        pdfDocument.optimizeResources(optimizationOptions);
        _dataDir = _dataDir + "Shrinkimage_out.pdf";
        // Guardar documento actualizado
        pdfDocument.save(_dataDir);
    }
```

Otra forma es redimensionar las imágenes con una resolución más baja. En este caso, debemos establecer ResizeImages en true y MaxResolution al valor apropiado.

```java
public static void ShrinkingCompressing2() {
        // Abrir documento
        Document pdfDocument = new Document(_dataDir + "ResizeImage.pdf");

        // Inicializar OptimizationOptions
        com.aspose.pdf.optimization.OptimizationOptions optimizationOptions = new com.aspose.pdf.optimization.OptimizationOptions();

        // Establecer opción CompressImages
        optimizationOptions.getImageCompressionOptions().setCompressImages(true);
        // Establecer opción ImageQuality
        optimizationOptions.getImageCompressionOptions().setImageQuality(75);

        // Establecer opción ResizeImage
        optimizationOptions.getImageCompressionOptions().setResizeImages(true);

        // Establecer opción MaxResolution
        optimizationOptions.getImageCompressionOptions().setMaxResolution(300);

        // Optimizar documento PDF usando OptimizationOptions
        pdfDocument.optimizeResources(optimizationOptions);
        _dataDir = _dataDir + "ResizeImages_out.pdf";
        // Guardar documento actualizado
        pdfDocument.save(_dataDir);
    }
```

Otro problema importante es el tiempo de ejecución. Pero nuevamente, podemos gestionar esta configuración también. Actualmente, podemos usar dos algoritmos - Estándar y Rápido. Para controlar el tiempo de ejecución, debemos establecer una propiedad de Versión. El siguiente fragmento demuestra el algoritmo Rápido:

```java
public static void ShrinkingCompressing3() {

        Clock clock = Clock.systemUTC();

        Duration tickDuration = Duration.ofNanos(250000);
        Clock clock1 = Clock.tick(clock, tickDuration);
        System.out.println("Inicio : " + clock.instant());

        // Abrir documento
        Document pdfDocument = new Document(_dataDir + "ResizeImage.pdf");

        // Inicializar OptimizationOptions
        com.aspose.pdf.optimization.OptimizationOptions optimizationOptions = new com.aspose.pdf.optimization.OptimizationOptions();

        // Establecer opción CompressImages
        optimizationOptions.getImageCompressionOptions().setCompressImages(true);

        // Establecer opción ImageQuality
        optimizationOptions.getImageCompressionOptions().setImageQuality(75);

        // Establecer Versión de Compresión de Imagen a rápida
        optimizationOptions.getImageCompressionOptions().setVersion(ImageCompressionVersion.Fast);

        // Optimizar documento PDF usando OptimizationOptions
        pdfDocument.optimizeResources(optimizationOptions);

        _dataDir = _dataDir + "ResizeImages_out.pdf";

        // Guardar documento actualizado
        pdfDocument.save(_dataDir);
        System.out.println("Fin : " + clock1.instant());
    }
```

## Eliminando Objetos No Utilizados

Un documento PDF a veces contiene objetos PDF que no están referenciados desde ningún otro objeto en el documento. Esto puede ocurrir, por ejemplo, cuando se elimina una página del árbol de páginas del documento pero el objeto de la página en sí no se elimina. Eliminar estos objetos no invalida el documento, sino que lo reduce.

```java
    public static void RemovingUnusedObjects() {

        // Abrir documento
        Document pdfDocument = new Document(_dataDir + "OptimizeDocument.pdf");
        com.aspose.pdf.optimization.OptimizationOptions optimizationOptions = new com.aspose.pdf.optimization.OptimizationOptions();
        
        optimizationOptions.setRemoveUnusedObjects(true);
        pdfDocument.optimizeResources(optimizationOptions);
        
        _dataDir = _dataDir + "emoveUnusedObjects_out.pdf";

        // Guardar documento actualizado
        pdfDocument.save(_dataDir);

    }
```
## Eliminando Flujos No Utilizados

A veces, un documento contiene flujos de recursos no utilizados.
 Estos flujos no son “objetos no utilizados” porque están referenciados desde el diccionario de recursos de una página. Esto puede suceder en casos donde una imagen ha sido eliminada de la página pero no de los recursos de la página. Además, esta situación ocurre a menudo cuando las páginas son extraídas del documento y las páginas del documento tienen recursos “comunes”, es decir, el mismo objeto de Recursos. Se analizan los contenidos de la página para determinar si un flujo de recursos es utilizado o no. Los flujos no utilizados son eliminados. A veces esto disminuye el tamaño del documento.

```java
public static void RemovingUnusedStream() {
        // Abrir documento
        Document pdfDocument = new Document(_dataDir + 
        "OptimizeDocument.pdf");
        com.aspose.pdf.optimization.OptimizationOptions optimizationOptions = new com.aspose.pdf.optimization.OptimizationOptions();
        optimizationOptions.setRemoveUnusedStreams(true);
        pdfDocument.optimizeResources(optimizationOptions);
        _dataDir = _dataDir + "removeUnusedObjects_out.pdf";
        
        // Guardar documento actualizado
        pdfDocument.save(_dataDir);
        
    }
```
## Enlazando Flujos Duplicados

A veces un documento contiene varios flujos de recursos idénticos (por ejemplo, imágenes). Esto puede suceder, por ejemplo, cuando un documento se concatena consigo mismo. El documento de salida contiene dos copias independientes del mismo flujo de recursos. Analizamos todos los flujos de recursos y los comparamos. Si los flujos están duplicados, se fusionan, es decir, solo queda una copia, las referencias se cambian adecuadamente y se eliminan las copias del objeto. A veces esto disminuye el tamaño del documento.

```java
    public static void LinkingDuplicateStream() {
        // Abrir documento
        Document pdfDocument = new Document(_dataDir + "OptimizeDocument.pdf");
        com.aspose.pdf.optimization.OptimizationOptions optimizationOptions = new com.aspose.pdf.optimization.OptimizationOptions();
        optimizationOptions.setRemoveUnusedStreams(true);
        
        // Optimizar documento PDF usando OptimizationOptions
        pdfDocument.optimizeResources(optimizationOptions);
        _dataDir = _dataDir + "OptimizeDocument_out.pdf";
        
        // Guardar documento actualizado
        pdfDocument.save(_dataDir);
    }
```

Además, podemos usar la configuración AllowReusePageContent. Si esta propiedad está configurada en true, el contenido de la página se reutilizará al optimizar el documento para páginas idénticas.

```java
public static void AllowReusePageContent() {
        // Abrir documento
        Document pdfDocument = new Document(_dataDir + "OptimizeDocument.pdf");
        com.aspose.pdf.optimization.OptimizationOptions optimizationOptions = new com.aspose.pdf.optimization.OptimizationOptions();
        optimizationOptions.setAllowReusePageContent(true);
        
        // Optimizar documento PDF usando OptimizationOptions
        pdfDocument.optimizeResources(optimizationOptions);
        _dataDir = _dataDir + "OptimizeDocument_out.pdf";
        
        // Guardar documento actualizado
        pdfDocument.save(_dataDir);
    }
```
## Desincrustar fuentes

Si el documento utiliza fuentes incrustadas significa que todos los datos de fuentes están ubicados en el documento.
 La ventaja es que el documento es visible independientemente de si la fuente está instalada en la máquina del usuario o no. Pero incrustar fuentes hace que el documento sea más grande. El método de eliminar la incrustación de fuentes elimina todas las fuentes incrustadas. Esto disminuye el tamaño del documento, pero el documento puede volverse ilegible si la fuente correcta no está instalada.

```java
    public static void UnembedFonts() {
        // Abrir documento
        Document pdfDocument = new Document(_dataDir + "OptimizeDocument.pdf");
        com.aspose.pdf.optimization.OptimizationOptions optimizationOptions = new com.aspose.pdf.optimization.OptimizationOptions();
        optimizationOptions.setUnembedFonts(true);
        
        // Optimizar documento PDF usando OptimizationOptions
        pdfDocument.optimizeResources(optimizationOptions);
        
        _dataDir = _dataDir + "OptimizeDocument_out.pdf";
        // Guardar documento actualizado
        pdfDocument.save(_dataDir);
    }
```

## Eliminación o aplanamiento de anotaciones

Las anotaciones se pueden eliminar cuando son innecesarias. Cuando son necesarios pero no requieren edición adicional, pueden ser aplanados. Ambas técnicas reducirán el tamaño del archivo.

```java
    public static void FlatteningAnnotations() {
        // Abrir documento
        Document pdfDocument = new Document(_dataDir + "OptimizeDocument.pdf");

        for (Page page : pdfDocument.getPages()) {
            for (Annotation annotation : page.getAnnotations())
                annotation.flatten();
        }

        _dataDir = _dataDir + "OptimizeDocument_out.pdf";
        // Guardar documento actualizado
        pdfDocument.save(_dataDir);
    }

```
## Eliminación de Campos de Formulario

Si el documento PDF contiene AcroForms, podemos intentar reducir el tamaño del archivo aplanando los campos del formulario.

```java
    public static void RemovingFormFields() {
        // Abrir documento
        Document pdfDocument = new Document(_dataDir + "OptimizeDocument.pdf");

        // Aplanar Formularios
        if (pdfDocument.getForm().getFields().length > 0) {
            for (Field field : pdfDocument.getForm().getFields()) {
                field.flatten();
            }
        }
        _dataDir = _dataDir + "FlattenForms_out.pdf";
        // guardar el documento actualizado
        pdfDocument.save(_dataDir);
    }

```
## Convertir un PDF de espacio de color RGB a escala de grises

Un archivo PDF está compuesto por Texto, Imagen, Adjuntos, Anotaciones, Gráficos y otros objetos. Puede encontrarse con la necesidad de convertir un PDF de espacio de color RGB a escala de grises para que sea más rápido al imprimir esos archivos PDF. Además, cuando el archivo se convierte a escala de grises, el tamaño del documento también se reduce, pero con este cambio, la calidad del documento puede disminuir. Actualmente, esta característica es soportada por la función Pre-Flight de Adobe Acrobat, pero al hablar de automatización de oficinas, Aspose.PDF es una solución definitiva para proporcionar tales ventajas para la manipulación de documentos.

Para cumplir con este requisito, se puede usar el siguiente fragmento de código.

```java
    public static void ConvertRGBtoGrayscale() {

        // Abrir documento
        Document pdfDocument = new Document(_dataDir + "OptimizeDocument.pdf");

        com.aspose.pdf.RgbToDeviceGrayConversionStrategy strategy = new com.aspose.pdf.RgbToDeviceGrayConversionStrategy();
        for (int idxPage = 1; idxPage <= pdfDocument.getPages().size(); idxPage++) {
            Page page = pdfDocument.getPages().get_Item(idxPage);
            strategy.convert(page);
        }
        pdfDocument.save("output.pdf");
    }
```

## FlateDecode Compresión

Aspose.PDF para Java proporciona soporte de compresión FlateDecode para la funcionalidad de Optimización de PDF. El siguiente fragmento de código muestra cómo usar la opción en Optimización para almacenar imágenes con compresión FlateDecode:

```java
    public static void FlateDecodeCompression() {

        // Abrir documento
        Document pdfDocument = new Document(_dataDir + "OptimizeDocument.pdf");
        com.aspose.pdf.optimization.OptimizationOptions optimizationOptions = new com.aspose.pdf.optimization.OptimizationOptions();

        optimizationOptions.getImageCompressionOptions().setEncoding(ImageEncoding.Flate);

        // Optimizar documento PDF usando OptimizationOptions
        pdfDocument.optimizeResources(optimizationOptions);

        _dataDir = _dataDir + "OptimizeDocument_out.pdf";
        // Guardar documento actualizado
        pdfDocument.save(_dataDir);
    }
```
## Almacenar Imagen en XImageCollection

Aspose.PDF para Java proporciona la capacidad de almacenar nuevas imágenes en [XImageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/XImageCollection) con compresión FlateDecode.
 Para habilitar esta opción, puede usar el indicador ImageFilterType.Flate. El siguiente fragmento de código muestra cómo usar esta funcionalidad:

```java
    public static void StoreImageInXImageCollection() {
        // Inicializar Documento
        Document document = new Document();
        document.getPages().add();
        Page page = document.getPages().get_Item(1);

        // Cargar imagen en el flujo
        java.io.FileInputStream imageStream = null;
        try {
            imageStream = new java.io.FileInputStream(new java.io.File("input_image1.jpg"));
        } catch (FileNotFoundException e) {
            e.printStackTrace();
            return;
        }
        page.getResources().getImages().add(imageStream, ImageFilterType.Flate);
        XImage ximage = page.getResources().getImages().get_Item(page.getResources().getImages().size());
        page.getContents().add(new com.aspose.pdf.operators.GSave());

        // Establecer coordenadas
        int lowerLeftX = 0;
        int lowerLeftY = 0;
        int upperRightX = 600;
        int upperRightY = 600;
        Rectangle rectangle = new Rectangle(lowerLeftX, lowerLeftY, upperRightX, upperRightY);
        Matrix matrix = new Matrix(new double[] { rectangle.getURX() - rectangle.getLLX(), 0, 0,
                rectangle.getURY() - rectangle.getLLY(), rectangle.getLLX(), rectangle.getLLY() });
        // Usando el operador ConcatenateMatrix (concatenar matriz): define cómo debe colocarse la imagen
        page.getContents().add(new com.aspose.pdf.operators.ConcatenateMatrix(matrix));
        page.getContents().add(new com.aspose.pdf.operators.Do(ximage.getName()));
        page.getContents().add(new com.aspose.pdf.operators.GRestore());

        document.save(_dataDir + "FlateDecodeCompression.pdf");
    }

}
```