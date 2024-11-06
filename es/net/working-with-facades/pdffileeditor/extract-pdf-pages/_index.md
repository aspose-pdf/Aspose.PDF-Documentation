---
title: Extraer páginas de PDF
type: docs
weight: 40
url: es/net/extract-pdf-pages/
description: Esta sección explica cómo extraer páginas de PDF con Aspose.PDF Facades usando la clase PdfFileEditor.
lastmod: "2021-06-05"
draft: false
---

## Extraer páginas de PDF entre dos números usando rutas de archivo

El método [Extract](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/extract/index) de la clase [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) te permite extraer un rango especificado de páginas de un archivo PDF. Esta sobrecarga te permite extraer páginas mientras manipulas los archivos PDF desde el disco. Esta sobrecarga requiere los siguientes parámetros: ruta del archivo de entrada, página de inicio, página final y ruta del archivo de salida. Las páginas desde la página de inicio hasta la página final serán extraídas y el resultado se guardará en el disco. El siguiente fragmento de código te muestra cómo extraer páginas de PDF entre dos números usando rutas de archivo.

```csharp
public static void Extract_PDFPages_FilePaths()
{
    // Crear objeto PdfFileEditor
    PdfFileEditor pdfEditor = new PdfFileEditor();

    // Extraer páginas
    pdfEditor.Extract(_dataDir + "MultiplePages.pdf", 1, 3, _dataDir + "ExtractPagesBetweenNumbers_out.pdf");
}
```

## Extraer un Array de Páginas PDF Usando Rutas de Archivos

Si no deseas extraer un rango de páginas, sino un conjunto de páginas en particular, el método [Extract](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/extract/index) te permite hacerlo también. Primero necesitas crear un array de enteros con todos los números de página que necesitas extraer. Esta sobrecarga del método [Extract](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/extract/index) toma los siguientes parámetros: archivo PDF de entrada, array de enteros de las páginas a extraer, y archivo PDF de salida. El siguiente fragmento de código te muestra cómo extraer páginas PDF usando rutas de archivos.

```csharp
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

## Extraer Páginas de PDF entre Dos Números Usando Streams

El método [Extract](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/extract/index) de la clase [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) te permite extraer un rango de páginas usando streams. Necesitas pasar los siguientes parámetros a esta sobrecarga: stream de entrada, página de inicio, página final y stream de salida. Las páginas especificadas por el rango entre la página de inicio y la página final se extraerán del stream de entrada y se guardarán en el stream de salida. El siguiente fragmento de código te muestra cómo extraer páginas de PDF entre dos números usando streams.

```csharp
public static void Extract_ArrayPDFPages_FilePaths()
{
    // Crear objeto PdfFileEditor
    PdfFileEditor pdfEditor = new PdfFileEditor();
    int[] pagesToExtract = new int[] { 1, 2 };
    // Extraer páginas
    pdfEditor.Extract(_dataDir + "Extract.pdf", pagesToExtract, _dataDir + "ExtractArrayOfPages_out.pdf");
}
```

## Extraer Array de Páginas de PDF Usando Streams

Un arreglo de páginas puede ser extraído del flujo PDF y guardado en el flujo de salida utilizando la sobrecarga adecuada del método [Extract](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/extract/index). Si no desea extraer un rango de páginas, sino un conjunto de páginas particulares, el método [Extract](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/extract/index) le permite hacerlo también. Primero necesita crear un arreglo de enteros con todos los números de página que necesitan ser extraídos. Esta sobrecarga del método [Extract](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/extract/index) toma los siguientes parámetros: flujo de entrada, arreglo de enteros de páginas a extraer y flujo de salida. El siguiente fragmento de código le muestra cómo extraer páginas PDF utilizando flujos.

```csharp
public static void Extract_ArrayPDFPages_Streams()
{
    // Crear objeto PdfFileEditor
    PdfFileEditor pdfEditor = new PdfFileEditor();
    // Crear flujos
    using (FileStream inputStream = new FileStream(_dataDir + "MultiplePages.pdf", FileMode.Open))
    using (FileStream outputStream = new FileStream(_dataDir + "ExtractArrayOfPagesUsingStreams_out.pdf", FileMode.Create))
    {
        int[] pagesToExtract = new int[] { 1, 2 };
        // Extraer páginas
        pdfEditor.Extract(inputStream, pagesToExtract, outputStream);
    }
}
```