---
title: Extraer páginas de PDF
type: docs
weight: 20
url: es/java/extract-pdf-pages/
description: Esta sección explica cómo extraer páginas de PDF con com.aspose.pdf.facades usando la clase PdfFileEditor.
lastmod: "2021-06-05"
draft: false
---

## Extraer páginas de PDF entre dos números usando rutas de archivo

El método [Extract](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileEditor#extract-java.io.InputStream-int:A-java.io.OutputStream-) de la clase [PdfFileEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileEditor) te permite extraer un rango específico de páginas de un archivo PDF. Esta sobrecarga te permite extraer páginas mientras manipulas los archivos PDF desde el disco. Esta sobrecarga requiere los siguientes parámetros: ruta del archivo de entrada, página de inicio, página final y ruta del archivo de salida. Las páginas desde la página de inicio hasta la página final serán extraídas y el resultado se guardará en el disco. El siguiente fragmento de código te muestra cómo extraer páginas de PDF entre dos números usando rutas de archivo.

```java
  public static void Extract_PDFPages_FilePaths() {
        // Crear objeto PdfFileEditor
        PdfFileEditor pdfEditor = new PdfFileEditor();

        // Extraer páginas
        pdfEditor.Extract(_dataDir + "MultiplePages.pdf", 1, 3, _dataDir + "ExtractPagesBetweenNumbers_out.pdf");
    }
```


## Extraer Array de Páginas de PDF Usando Rutas de Archivos

Si no deseas extraer un rango de páginas, sino un conjunto de páginas particulares, el método [Extract](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileEditor#extract-java.io.InputStream-int:A-java.io.OutputStream-) te permite hacer eso también. Primero necesitas crear un array de enteros con todos los números de página que necesitas extraer. Esta sobrecarga del método [Extract](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileEditor#extract-java.io.InputStream-int:A-java.io.OutputStream-) toma los siguientes parámetros: archivo PDF de entrada, array de enteros de las páginas a extraer, y archivo PDF de salida. El siguiente fragmento de código te muestra cómo extraer páginas de PDF usando rutas de archivos.

```java
 public static void Extract_ArrayPDFPages_FilePaths() {
        // Crear objeto PdfFileEditor
        PdfFileEditor pdfEditor = new PdfFileEditor();
        int[] pagesToExtract = new int[] { 1, 2 };
        // Extraer páginas
        pdfEditor.Extract(_dataDir + "Extract.pdf", pagesToExtract, _dataDir + "ExtractArrayOfPages_out.pdf");
    }
```


## Extraer Páginas PDF entre Dos Números Usando Streams

El método [Extract](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileEditor#extract-java.io.InputStream-int:A-java.io.OutputStream-) de la clase [PdfFileEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileEditor) te permite extraer un rango de páginas usando streams. Necesitas pasar los siguientes parámetros a esta sobrecarga: flujo de entrada, página de inicio, página final y flujo de salida. Las páginas especificadas por el rango entre la página de inicio y la página final serán extraídas del flujo de entrada y guardadas en el flujo de salida. El siguiente fragmento de código te muestra cómo extraer páginas PDF entre dos números usando streams.

```java
public static void Extract_PDFPages_Streams()
    {
         // Crear objeto PdfFileEditor
            PdfFileEditor pdfEditor = new PdfFileEditor();
         // Crear streams
         using (FileStream inputStream = new FileStream(_dataDir + "MultiplePages.pdf", FileMode.Open))
         using (FileStream outputStream = new FileStream(_dataDir + "ExtractPagesBetweenTwoNumbers_out.pdf", FileMode.Create))
         // Extraer páginas
         pdfEditor.Extract(inputStream, 1, 3, outputStream);

    }
```


## Extraer Array de Páginas de PDF Usando Streams

Un array de páginas puede ser extraído del flujo de PDF y guardado en el flujo de salida usando la sobrecarga apropiada del método [Extract](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileEditor#extract-java.io.InputStream-int:A-java.io.OutputStream-). Si no deseas extraer un rango de páginas, sino un conjunto de páginas particulares, el método [Extract](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileEditor#extract-java.io.InputStream-int:A-java.io.OutputStream-) te permite hacerlo también. Primero necesitas crear un array de enteros con todos los números de página que necesitan ser extraídos. Esta sobrecarga del método [Extract](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileEditor#extract-java.io.InputStream-int:A-java.io.OutputStream-) toma los siguientes parámetros: flujo de entrada, array de enteros de las páginas a ser extraídas y flujo de salida. El siguiente fragmento de código te muestra cómo extraer páginas de PDF usando streams.

```java
public static void Extract_ArrayPDFPages_Streams()
        {
            // Crear objeto PdfFileEditor
            PdfFileEditor pdfEditor = new PdfFileEditor();
            // Crear streams
            using (FileStream inputStream = new FileStream(_dataDir + "MultiplePages.pdf", FileMode.Open))
            using (FileStream outputStream = new FileStream(_dataDir + "ExtractArrayOfPagesUsingStreams_out.pdf", FileMode.Create))
            {
                int[] pagesToExtract = new int[] { 1, 2 };
                // Extraer páginas
                pdfEditor.Extract(inputStream, pagesToExtract, outputStream);
            }
        }
```