---
title: Importar y Exportar Anotaciones al formato XFDF usando com.aspose.pdf.facades
type: docs
weight: 20
url: /java/import-export-annotations/
description: Esta sección explica cómo exportar e importar anotaciones de un archivo PDF a XFDF con Aspose.PDF Facades.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

XFDF significa Formato de Datos de Formularios XML. Es un formato de archivo basado en XML. Este formato de archivo se utiliza para representar datos de formulario o anotaciones contenidas en un formulario PDF. XFDF puede usarse para muchos propósitos diferentes, pero en nuestro caso, puede usarse para enviar o recibir datos de formulario o anotaciones a otras computadoras o servidores, etc., o puede usarse para archivar los datos de formulario o anotaciones. En este artículo, veremos cómo Aspose.Pdf.Facades ha tomado en consideración este concepto y cómo podemos importar y exportar datos de anotaciones a un archivo XFDF.

La clase [PDFAnnotationEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor) contiene dos métodos para trabajar con la importación y exportación de anotaciones al archivo XFDF.
 [ExportAnnotationsXfdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor#exportAnnotationsToXfdf-java.io.OutputStream-) método proporciona la funcionalidad para exportar anotaciones de un documento PDF a un archivo XFDF, mientras que el método [ImportAnnotationFromXfdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor#importAnnotationFromXfdf-java.io.InputStream-) le permite importar anotaciones desde un archivo XFDF existente. Para importar o exportar anotaciones necesitamos especificar los tipos de anotaciones. Podemos especificar estos tipos en forma de una enumeración y luego pasar esta enumeración como un argumento a cualquiera de estos métodos.

El siguiente fragmento de código le muestra cómo importar anotaciones a un archivo XFDF:

```java
public static void ImportAnnotation() {
        String[] sources = new String[] { _dataDir + "sample_cats_dogs.pdf" };
        PdfAnnotationEditor annotationEditor = new PdfAnnotationEditor();
        annotationEditor.bindPdf(_dataDir + "sample.pdf");
        annotationEditor.importAnnotations(sources);
        annotationEditor.save(_dataDir + "sample_demo.pdf");
    }
```

El siguiente fragmento de código describe cómo importar/exportar anotaciones a un archivo XFDF:

```java
    public static void ImportExportXFDF01() {
        PdfAnnotationEditor annotationEditor = new PdfAnnotationEditor();
        annotationEditor.bindPdf(_dataDir + "sample_cats_dogs.pdf");
        OutputStream xmlOutputStream;
        try {
            xmlOutputStream = new FileOutputStream(_dataDir + "sample.xfdf");
            annotationEditor.exportAnnotationsToXfdf(xmlOutputStream);
            xmlOutputStream.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
        Document document = new Document();
        document.getPages().add();
        annotationEditor.bindPdf(document);
        annotationEditor.importAnnotationsFromXfdf(_dataDir + "sample.xfdf");
        annotationEditor.save(_dataDir + "ImportedAnnotation.pdf");
    }
```

De esta manera, las anotaciones de los tipos especificados solo serán importadas o exportadas a un archivo XFDF.

```java
    public static void ImportExportXFDF02() {
        PdfAnnotationEditor annotationEditor = new PdfAnnotationEditor();
        annotationEditor.bindPdf(_dataDir + "sample_cats_dogs.pdf");
        OutputStream xmlOutputStream;

        try {
            xmlOutputStream = new FileOutputStream(_dataDir + "sample.xfdf");
            int[] annotationTypes = new int[] { AnnotationType.FreeText, AnnotationType.Text };
            annotationEditor.exportAnnotationsXfdf(xmlOutputStream, 2, 2, annotationTypes);
            xmlOutputStream.close();
        } catch (IOException e) {            
            e.printStackTrace();
        }

        Document document = new Document(_dataDir + "sample.pdf");
        document.getPages().add();
        annotationEditor.bindPdf(document);
        annotationEditor.importAnnotationsFromXfdf(_dataDir + "sample.xfdf");
        annotationEditor.save(_dataDir + "ImportedAnnotation.pdf");
    }
```