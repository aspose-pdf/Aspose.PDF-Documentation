---
title: Importar y Exportar Anotaciones al formato XFDF
linktitle: Importar y Exportar Anotaciones al formato XFDF
type: docs
weight: 40
url: es/java/import-export-xfdf/
description: Puede importar y exportar anotaciones con el formato XFDF usando la biblioteca Aspose.PDF para Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

{{% alert color="primary" %}}

XFDF significa Formato de Datos de Formularios XML. Es un formato de archivo basado en XML. Este formato de archivo se utiliza para representar datos de formularios o anotaciones contenidas en un formulario PDF. XFDF se puede usar para muchos propósitos diferentes, pero en nuestro caso, se puede usar para enviar o recibir datos de formularios o anotaciones a otros ordenadores o servidores, etc., o se puede usar para archivar los datos de formularios o anotaciones. En este artículo, veremos cómo Aspose.Pdf.Facades ha tomado este concepto en consideración y cómo podemos importar y exportar datos de anotaciones a un archivo XFDF.

{{% /alert %}}

**Aspose.PDF para Java** es un componente rico en funciones cuando se trata de editar documentos PDF.
 Como sabemos, XFDF es un aspecto importante de la manipulación de formularios PDF, el espacio de nombres Aspose.Pdf.Facades en Aspose.PDF para Java ha considerado esto muy bien, y ha proporcionado métodos para importar y exportar datos de anotaciones a archivos XFDF.

La clase [PDFAnnotationEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor) contiene dos métodos para trabajar con la importación y exportación de anotaciones a un archivo XFDF. [ExportAnnotationsXfdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor) método proporciona la funcionalidad para exportar anotaciones de un documento PDF a un archivo XFDF, mientras que el método [ImportAnnotationFromXfdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor) le permite importar anotaciones desde un archivo XFDF existente. Para importar o exportar anotaciones, necesitamos especificar los tipos de anotaciones. Podemos especificar estos tipos en forma de una enumeración y luego pasar esta enumeración como un argumento a cualquiera de estos métodos. De esta manera, las anotaciones de los tipos especificados solo se importarán o exportarán a un archivo XFDF.

El siguiente fragmento de código le muestra cómo exportar anotaciones a un archivo XFDF:

```java
package com.aspose.pdf.examples;

import java.io.FileOutputStream;
import java.io.IOException;
import com.aspose.pdf.*;
import com.aspose.pdf.facades.PdfAnnotationEditor;

public class ExampleAnnotationImportExport {
    // La ruta al directorio de documentos.
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";
    /*
     * Importando anotaciones desde un archivo XFDF Archivo de Formato de Datos de Formularios XML (XFDF)
     * creado por Adobe Acrobat, una aplicación de creación de PDF; almacena descripciones de
     * elementos de formulario de página y sus valores, como los nombres y valores de los campos de texto;
     * utilizado para guardar datos de formularios que pueden ser importados a un documento PDF.
     * Puede importar datos de anotación desde el archivo XFDF al PDF usando el
     * método ImportAnnotationsFromXfdf en la clase PdfAnnotationEditor.
     */

    public static void ExportAnnotationXFDF() throws IOException {
        // Crear objeto PdfAnnotationEditor
        PdfAnnotationEditor AnnotationEditor = new PdfAnnotationEditor();

        // Vincular documento PDF al Editor de Anotaciones
        AnnotationEditor.bindPdf(_dataDir + "AnnotationDemo1.pdf");

        // Exportar anotaciones
        FileOutputStream fileStream = new FileOutputStream(_dataDir + "exportannotations.xfdf");
        int[] annotType = { AnnotationType.Line, AnnotationType.Square };
        AnnotationEditor.exportAnnotationsXfdf(fileStream, 1, 1, annotType);
        fileStream.flush();
        fileStream.close();
    }
```

El siguiente fragmento de código describe cómo importar anotaciones a un archivo XFDF:

```java
public static void ImportAnnotationXFDF()
{
    // Crear objeto PdfAnnotationEditor
    PdfAnnotationEditor AnnotationEditor = new PdfAnnotationEditor();
    // Crear un nuevo documento PDF
    var document = new Document();
    document.Pages.Add();
    AnnotationEditor.BindPdf(document);

    var exportFileName = Path.Combine(_dataDir, "exportannotations.xfdf");
    if (!File.Exists(exportFileName))
        ExportAnnotationXFDF();

    // Importar anotación
    AnnotationEditor.ImportAnnotationsFromXfdf(exportFileName);

    // Guardar PDF de salida
    document.Save(Path.Combine(_dataDir, "AnnotationDemo2.pdf"));
}
```

## Otra manera de exportar/importar anotaciones de una vez

En el código a continuación, un método ImportAnnotations permite importar anotaciones directamente desde otro documento PDF.

```java
    public static void ImportAnnotationFromPDF() throws IOException {
        // Crear objeto PdfAnnotationEditor
        PdfAnnotationEditor AnnotationEditor = new PdfAnnotationEditor();
        // Crear un nuevo documento PDF
        Document document = new Document();

        document.getPages().add();
        AnnotationEditor.bindPdf(document);
        String exportFileName = _dataDir + "exportannotations.xfdf";
        java.io.File f = new java.io.File(exportFileName);
        if (!f.exists()) {
            ExportAnnotationXFDF();
        }

        // Annotation Editor permite importar anotaciones de varios documentos PDF,
        // pero en este ejemplo, usamos solo uno.
        String[] fileNames = { _dataDir + "AnnotationDemo1.pdf" };
        AnnotationEditor.importAnnotations(fileNames);

        // Guardar PDF de salida
        document.save(_dataDir + "AnnotationDemo3.pdf");
    }
}
```