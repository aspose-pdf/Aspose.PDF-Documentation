---
title: Guardar Documento PDF 
linktitle: Guardar
type: docs
weight: 30
url: es/java/save-pdf-document/
description: Aprende cómo guardar un archivo PDF con la biblioteca Aspose.PDF para Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Guardar documento PDF en el sistema de archivos

Puede guardar el documento PDF creado o manipulado en el sistema de archivos usando el método Save de la clase [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).
Cuando no proporciona el tipo de formato (opciones), el documento se guarda en el formato Aspose.PDF v.1.7 (*.pdf).

```java
package com.aspose.pdf.examples;


import java.io.FileOutputStream;

import java.nio.file.Path;
import java.nio.file.Paths;
import com.aspose.pdf.*;

public final class BasicOperationsSave {

    private BasicOperationsSave() {
    }

    private static Path _dataDir = Paths.get("/home/admin1/pdf-examples/Samples");

    public static void main(String[] args) {
        SaveDocument();
        SaveDocumentStream();
        SaveDocumentAsPDFx();
    }

    public static void SaveDocument() {
        String originalFileName = _dataDir + "/SimpleResume.pdf";
        String modifiedFileName = _dataDir + "/SimpleResumeModified.pdf";

        Document pdfDocument = new Document(originalFileName);
        // realizar algunas manipulaciones, por ejemplo, añadir una nueva página vacía
        pdfDocument.getPages().add();
        pdfDocument.save(modifiedFileName);
    }
```


## Guardar documento PDF en un flujo

También puede guardar el documento PDF creado o manipulado en un flujo utilizando las sobrecargas de los métodos Save.

```java
public static void SaveDocumentStream() {
        String originalFileName = _dataDir + "/SimpleResume.pdf";
        String modifiedFileName = _dataDir + "/SimpleResumeModified.pdf";

        Document pdfDocument = new Document(originalFileName);
        // hacer alguna manipulación, por ejemplo, agregar una nueva página vacía
        pdfDocument.getPages().add();
        try {
            pdfDocument.save(new FileOutputStream(modifiedFileName));
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }

    }

```

## Guardar documento PDF en aplicaciones web

Para guardar documentos en aplicaciones web, puede utilizar las formas propuestas anteriormente. Además, la clase [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) tiene un método sobrecargado Save.
```java
    // @RequestMapping(value = "/files/{file_name}", method = RequestMethod.GET)
    // public void getFile(@PathVariable("file_name") String fileName, HttpServletResponse response) {
    //     try {
    //         response.setContentType("application/pdf");
    //         // obtén tu archivo como InputStream
    //         InputStream is = new FileInputStream(_dataDir + fileName);
    //         // cópialo al OutputStream de la respuesta
    //         org.apache.commons.io.IOUtils.copy(is, response.getOutputStream());
    //         response.flushBuffer();
    //     } catch (IOException ex) {
    //         log.info("Error al escribir el archivo en el flujo de salida. El nombre del archivo era '{}'", fileName, ex);
    //         throw new RuntimeException("Error de E/S al escribir el archivo en el flujo de salida");
    //     }
    // }
```


Para una explicación más detallada, por favor dirígete a la sección [Showcase]().

## Guardar en formato PDF/A o PDF/X

PDF/A es una versión del Formato de Documento Portátil (PDF) estandarizada por ISO para su uso en el archivo y preservación a largo plazo de documentos electrónicos.
PDF/A se diferencia de PDF en que prohíbe características no adecuadas para el archivo a largo plazo, como el enlace de fuentes (a diferencia de la incrustación de fuentes) y la encriptación. Los requisitos ISO para los visores de PDF/A incluyen pautas de gestión del color, soporte de fuentes incrustadas y una interfaz de usuario para leer anotaciones incrustadas.

PDF/X es un subconjunto del estándar ISO PDF. El propósito de PDF/X es facilitar el intercambio de gráficos y, por lo tanto, tiene una serie de requisitos relacionados con la impresión que no se aplican a los archivos PDF estándar.

En ambos casos, se utiliza el método Save para almacenar los documentos, mientras que los documentos deben ser preparados usando el método Convert.

```java
public static void SaveDocumentAsPDFx() {
        Document pdfDocument = new Document("../../../Samples/SimpleResume.pdf");
        pdfDocument.getPages().add();
        pdfDocument.convert(new PdfFormatConversionOptions(PdfFormat.PDF_X_3));
        pdfDocument.save("../../../Samples/SimpleResume_X3.pdf");
    }

}
```