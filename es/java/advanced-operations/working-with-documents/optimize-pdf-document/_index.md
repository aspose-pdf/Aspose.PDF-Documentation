---
title: Optimizar archivos PDF en Java
linktitle: Optimizar PDF
type: docs
weight: 30
url: /es/java/optimize-pdf/
description: Aprenda cómo optimizar, comprimir y reducir el tamaño de archivo PDF en Java usando Aspose.PDF.
lastmod: "2026-09-03"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Comprima los recursos PDF y reduzca el tamaño del archivo con Java
Abstract: Este artículo explica cómo optimizar archivos PDF usando Aspose.PDF for Java. Cubre la optimización de todo el documento, la compresión de recursos, la reducción de la calidad de imágenes, la eliminación de objetos y flujos no utilizados, la vinculación de flujos duplicados, la desincorporación de fuentes, la aplanación de anotaciones y formularios, la conversión a escala de grises y la compresión de imágenes Flate.
---
Aspose.PDF for Java expone funciones de optimización a través de `Document.optimize`, `optimizeResources`, y `OptimizationOptions`.

## Optimizar un PDF con optimización general de documentos

Utilice este ejemplo cuando quiera que Aspose.PDF aplique la rutina de optimización de documento completo incorporada.

1. Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Llamar `optimize()` en el documento.
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

## Reducir el tamaño del PDF optimizando los recursos

Este ejemplo se centra en la optimización a nivel de recurso sin configurar manualmente opciones individuales.

1. Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Ejecutar `optimizeResources()` para optimizar los recursos internos.
1. Guarda el resultado e imprime los tamaños de los archivos de entrada y salida.

```java
public static void reduceSizePdf(Path inputFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        document.optimizeResources();
        document.save(outputFile.toString());
    }
    printFileSizes(inputFile, outputFile);
}
```

## Comprimir todas las imágenes en un PDF

Utilice este enfoque cuando los documentos con muchas imágenes requieran un tamaño de archivo más pequeño y sea aceptable una reducción de la calidad de imagen.

1. Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Crear [OpcionesDeOptimización](https://reference.aspose.com/pdf/java/com.aspose.pdf/optimizationoptions/) y habilite la compresión de imágenes con el nivel de calidad requerido.
1. Optimiza los recursos del documento con esas configuraciones.
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

## Eliminar objetos no utilizados de un PDF

Este ejemplo elimina los objetos no utilizados que pueden permanecer en la estructura del documento después de ediciones o fusiones.

1. Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Crear [OpcionesDeOptimización](https://reference.aspose.com/pdf/java/com.aspose.pdf/optimizationoptions/) y habilitar la eliminación de objetos no utilizados.
1. Optimiza los recursos y guarda el archivo actualizado.
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

## Eliminar flujos no utilizados de un PDF

Utilice este enfoque cuando desee descartar los datos del flujo que ya no son referenciados por el documento.

1. Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Configurar [OpcionesDeOptimización](https://reference.aspose.com/pdf/java/com.aspose.pdf/optimizationoptions/) para eliminar streams no utilizados.
1. Optimice los recursos, guarde el documento de salida y compare los tamaños de archivo.

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

## Enlazar flujos duplicados en un PDF

Este ejemplo deduplica streams repetidos para que el contenido idéntico pueda almacenarse solo una vez.

1. Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Crear [OpcionesDeOptimización](https://reference.aspose.com/pdf/java/com.aspose.pdf/optimizationoptions/) y habilitar la vinculación de flujos duplicados.
1. Optimiza los recursos, guarda el documento de salida y muestra los tamaños de archivo.

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

## Desincorporar fuentes de un PDF

Utilice esta opción cuando reducir el tamaño del archivo sea más importante que mantener los datos de fuentes incrustados en la salida.

1. Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Configurar [OpcionesDeOptimización](https://reference.aspose.com/pdf/java/com.aspose.pdf/optimizationoptions/) para desincorporar fuentes.
1. Optimiza los recursos, guarda el documento y compara los tamaños de archivo.

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

## Aplanar anotaciones en un PDF

Este ejemplo convierte las anotaciones en contenido estático de la página, de modo que ya no permanezcan como objetos interactivos.

1. Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Iterar a través de cada [Página](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) y su [Anotación](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotation/) colección.
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

## Aplanar campos de formulario PDF

Utilice este enfoque cuando los campos de formulario rellenables deban convertirse en contenido fijo antes de la distribución o el archivado.

1. Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Compruebe si el documento contiene widgets de formulario.
1. Aplanar cada [Campo](https://reference.aspose.com/pdf/java/com.aspose.pdf/field/) representado por un [Anotación de Widget](https://reference.aspose.com/pdf/java/com.aspose.pdf/widgetannotation/).
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

## Convertir un PDF a escala de grises

Este ejemplo convierte cada página a escala de grises, lo que puede ayudar a reducir la complejidad de color y a estandarizar la salida para flujos de trabajo de archivado o impresión.

1. Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Iterar a través de cada [Página](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) en el documento.
1. Llamar `makeGrayscale()` en cada página y guarda el archivo de salida.

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

## Usar compresión de imagen FlateDecode

Utiliza este patrón cuando desees aplicar compresión basada en Flate a imágenes durante la optimización de recursos PDF.

1. Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Crear [OpcionesDeOptimización](https://reference.aspose.com/pdf/java/com.aspose.pdf/optimizationoptions/) y establezca la codificación de la imagen a [Codificación de imagen](https://reference.aspose.com/pdf/java/com.aspose.pdf/imageencoding/).`Flate`.
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

## Imprimir tamaños de archivo originales y optimizados

Este método auxiliar informa la diferencia de tamaño entre el archivo de origen y el archivo de salida optimizado.

1. Leer el tamaño del archivo de entrada.
1. Lee el tamaño del archivo de salida.
1. Imprima ambos valores en un solo mensaje de estado.

```java
private static void printFileSizes(Path inputFile, Path outputFile) throws Exception {
    System.out.println("Original file size: " + Files.size(inputFile)
            + ". Reduced file size: " + Files.size(outputFile));
}
```
