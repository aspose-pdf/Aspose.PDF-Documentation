---
title: Optimizar archivos PDF en Java
linktitle: Optimizar PDF
type: docs
weight: 30
url: /java/optimize-pdf/
description: Aprenda a optimizar, comprimir y reducir el tamaño de un archivo PDF en Java usando Aspose.PDF.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Comprima recursos PDF y reduzca el tamaño del archivo con Java
Abstract: Este artículo explica cómo optimizar archivos PDF usando Aspose.PDF para Java. Cubre la optimización de todo el documento, la compresión de recursos, la reducción de la calidad de la imagen, la eliminación de objetos y secuencias no utilizados, la vinculación de secuencias duplicadas, la eliminación de incrustaciones de fuentes, el aplanamiento de anotaciones y formularios, la conversión en escala de grises y la compresión de imágenes Flate.
---
Aspose.PDF para Java expone funciones de optimización a través de `Document.optimize`, `optimizeResources` y `OptimizationOptions`.


## 
Optimice un PDF con optimización general de documentos



Utilice este ejemplo cuando desee que Aspose.PDF aplique la rutina integrada de optimización de todo el documento.


1. Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. Llame a `optimize()` en el documento.
1. Guarde el archivo optimizado y compare los tamaños original y de salida.


```java
public static void optimizePdf(Path inputFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        document.optimize();
        document.save(outputFile.toString());
    }
    printFileSizes(inputFile, outputFile);
}
```

## 
Reducir el tamaño del PDF optimizando los recursos



Este ejemplo se centra en la optimización a nivel de recursos sin configurar manualmente opciones individuales.


1. Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. Ejecute `optimizeResources()` para optimizar los recursos internos.
1. Guarde el resultado e imprima los tamaños de los archivos de entrada y salida.


```java
public static void reduceSizePdf(Path inputFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        document.optimizeResources();
        document.save(outputFile.toString());
    }
    printFileSizes(inputFile, outputFile);
}
```

## 
Comprimir todas las imágenes en un PDF



Utilice este enfoque cuando los documentos con muchas imágenes necesiten un tamaño de archivo más pequeño y sea aceptable cierta reducción en la calidad de la imagen.


1. Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. Cree [Opciones de optimización](https://reference.aspose.com/pdf/java/com.aspose.pdf/optimizationoptions/) y habilite la compresión de imágenes con el nivel de calidad requerido.
1. Optimice los recursos del documento con esas configuraciones.

1. Guarde el archivo optimizado y compare los tamaños de archivo.


```java
public static void shrinkingOrCompressingAllImages(Path inputFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        OptimizationOptions optimizeOptions = new OptimizationOptions();
        optimizeOptions.getImageCompressionOptions().setCompressImages(true);
        optimizeOptions.getImageCompressionOptions().setImageQuality(50);
        document.optimizeResources(optimizeOptions);
        document.save(outputFile.toString());
    }
    printFileSizes(inputFile, outputFile);
}
```

## 
Eliminar objetos no utilizados de un PDF



Este ejemplo elimina objetos no utilizados que pueden permanecer en la estructura del documento después de ediciones o fusiones.


1. Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Cree [Opciones de optimización](https://reference.aspose.com/pdf/java/com.aspose.pdf/optimizationoptions/) y habilite la eliminación de objetos no utilizados.

1. Optimice los recursos y guarde el archivo actualizado.

1. Imprima los tamaños de archivo original y reducido.


```java
public static void removingUnusedObjects(Path inputFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        OptimizationOptions optimizeOptions = new OptimizationOptions();
        optimizeOptions.setRemoveUnusedObjects(true);
        document.optimizeResources(optimizeOptions);
        document.save(outputFile.toString());
    }
    printFileSizes(inputFile, outputFile);
}
```

## 
Eliminar transmisiones no utilizadas de un PDF



Utilice este enfoque cuando desee descartar datos de flujo a los que el documento ya no hace referencia.

1. Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. Configure [Opciones de optimización](https://reference.aspose.com/pdf/java/com.aspose.pdf/optimizationoptions/) para eliminar transmisiones no utilizadas.

1. Optimice los recursos, guarde el documento de salida y compare tamaños de archivos.


```java
public static void removingUnusedStreams(Path inputFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        OptimizationOptions optimizeOptions = new OptimizationOptions();
        optimizeOptions.setRemoveUnusedStreams(true);
        document.optimizeResources(optimizeOptions);
        document.save(outputFile.toString());
    }
    printFileSizes(inputFile, outputFile);
}
```

## 
Vincular transmisiones duplicadas en un PDF



Este ejemplo deduplica transmisiones repetidas para que el contenido idéntico se pueda almacenar solo una vez.

1. Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. Cree [Opciones de optimización](https://reference.aspose.com/pdf/java/com.aspose.pdf/optimizationoptions/) y habilite la vinculación de secuencias duplicadas.

1. Optimice los recursos, guarde el documento de salida e imprima los tamaños de archivo.


```java
public static void linkingDuplicateStreams(Path inputFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        OptimizationOptions optimizeOptions = new OptimizationOptions();
        optimizeOptions.setLinkDuplicateStreams(true);
        document.optimizeResources(optimizeOptions);
        document.save(outputFile.toString());
    }
    printFileSizes(inputFile, outputFile);
}
```

## 
Desincrustar fuentes de un PDF



Utilice esta opción cuando reducir el tamaño del archivo sea más importante que mantener los datos de fuente incrustados en la salida.

1. Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. Configure [Opciones de optimización](https://reference.aspose.com/pdf/java/com.aspose.pdf/optimizationoptions/) para eliminar fuentes.

1. Optimice los recursos, guarde el documento y compare tamaños de archivos.


```java
public static void unembedFonts(Path inputFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        OptimizationOptions optimizeOptions = new OptimizationOptions();
        optimizeOptions.setUnembedFonts(true);
        document.optimizeResources(optimizeOptions);
        document.save(outputFile.toString());
    }
    printFileSizes(inputFile, outputFile);
}
```

## 
Aplanar anotaciones en un PDF



Este ejemplo convierte las anotaciones en contenido de página estática para que ya no sigan siendo objetos interactivos.

1. Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. Itere a través de cada [Página](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) y su colección [Anotación](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotation/).

1. Aplana cada anotación y guarda el documento actualizado.


```java
public static void flattenAnnotations(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Page page : document.getPages()) {
            for (Annotation annotation : page.getAnnotations()) {
                annotation.flatten();
            }
        }
        document.save(outputFile.toString());
    }
}
```

## 
Aplanar campos de formulario PDF



Utilice este enfoque cuando los campos de formulario que se pueden completar deban convertirse en contenido fijo antes de su distribución o archivo.

1. Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. Compruebe si el documento contiene widgets de formulario.

1. Aplana cada [Campo](https://reference.aspose.com/pdf/java/com.aspose.pdf/field/) representado por una [WidgetAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/widgetannotation/).

1. Guarde el archivo de salida e imprima los tamaños de archivo.


```java
public static void flattenForms(Path inputFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        if (document.getForm() != null && document.getForm().size() > 0) {
            for (WidgetAnnotation annotation : document.getForm()) {
                if (annotation instanceof Field field) {
                    field.flatten();
                }
            }
        }
        document.save(outputFile.toString());
    }
    printFileSizes(inputFile, outputFile);
}
```

## 
Convertir un PDF a escala de grises

Este ejemplo cambia cada página a escala de grises, lo que puede ayudar a reducir la complejidad del color y estandarizar la salida para flujos de trabajo de archivo o impresión.


1. Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. Repita cada [Página](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) en el documento.

1. Llame a `makeGrayscale()` en cada página y guarde el archivo de salida.


```java
public static void convertPdfFromRgbColorspaceToGrayscale(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Page page : document.getPages()) {
            page.makeGrayscale();
        }
        document.save(outputFile.toString());
    }
}
```

## 
Utilice la compresión de imágenes FlateDecode

Utilice este patrón cuando desee aplicar compresión basada en Flate a imágenes durante la optimización de recursos PDF.


1. Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. Cree [Opciones de optimización](https://reference.aspose.com/pdf/java/com.aspose.pdf/optimizationoptions/) y establezca la codificación de la imagen en [ImageEncoding](https://reference.aspose.com/pdf/java/com.aspose.pdf/imageencoding/).`Flate`.

1. Optimice los recursos del documento y guarde el archivo de salida.


```java
public static void usingFlatedecodeCompression(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        OptimizationOptions optimizationOptions = new OptimizationOptions();
        optimizationOptions.getImageCompressionOptions().setEncoding(ImageEncoding.Flate);
        document.optimizeResources(optimizationOptions);
        document.save(outputFile.toString());
    }
}
```

## 
Imprima tamaños de archivos originales y optimizados

Este método auxiliar informa la diferencia de tamaño entre el archivo fuente y el archivo de salida optimizado.


1. Lea el tamaño del archivo de entrada.

1. Lea el tamaño del archivo de salida.

1. Imprima ambos valores en un solo mensaje de estado.

```java
private static void printFileSizes(Path inputFile, Path outputFile) throws Exception {
    System.out.println("Original file size: " + Files.size(inputFile)
            + ". Reduced file size: " + Files.size(outputFile));
}
```
