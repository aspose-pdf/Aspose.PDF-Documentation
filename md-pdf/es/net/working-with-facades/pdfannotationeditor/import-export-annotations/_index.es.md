---
title: Importar y Exportar Anotaciones a XFDF
type: docs
weight: 20
url: /net/import-export-annotations/
description: Esta sección explica cómo importar y exportar anotaciones de un archivo PDF a XFDF con Aspose.PDF Facades.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

XFDF significa Formato de Datos de Formularios XML. Es un formato de archivo basado en XML. Este formato de archivo se usa para representar datos de formularios o anotaciones contenidas en un formulario PDF. XFDF puede usarse para muchos propósitos diferentes, pero en nuestro caso, puede usarse para enviar o recibir datos de formularios o anotaciones a otras computadoras o servidores, etc., o puede usarse para archivar los datos de formularios o anotaciones. En este artículo, veremos cómo Aspose.Pdf.Facades ha tomado en consideración este concepto y cómo podemos importar y exportar datos de anotaciones a un archivo XFDF.

## Importando y Exportando Anotaciones a XFDF

[Aspose.PDF para .NET](/pdf/net/) es un componente rico en características cuando se trata de editar documentos PDF. As we know XFDF es un aspecto importante de la manipulación de formularios PDF, [Aspose.Pdf.Facades namespace](https://reference.aspose.com/pdf/net/aspose.pdf.facades) en [Aspose.PDF for .NET](/pdf/net/) ha considerado esto muy bien, y ha proporcionado métodos para importar y exportar datos de anotaciones a archivos XFDF.

La clase [PDFAnnotationEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor) contiene dos métodos para trabajar con la importación y exportación de anotaciones a un archivo XFDF. [ExportAnnotationsXfdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor/methods/exportannotationsxfdf/index) método proporciona la funcionalidad para exportar anotaciones de un documento PDF a un archivo XFDF, mientras que el método [ImportAnnotationFromXfdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor/methods/importannotationfromxfdf/index) le permite importar anotaciones desde un archivo XFDF existente. Para importar o exportar anotaciones, necesitamos especificar los tipos de anotaciones. Podemos especificar estos tipos en forma de una enumeración y luego pasar esta enumeración como argumento a cualquiera de estos métodos. De esta manera, las anotaciones de los tipos especificados solo se importarán o exportarán a un archivo XFDF.

El siguiente fragmento de código le muestra cómo importar anotaciones a un archivo XFDF:

```csharp
public static void ImportAnnotation()
        {
            var sources = new string[] { _dataDir + "sample_cats_dogs.pdf" };
            PdfAnnotationEditor annotationEditor = new PdfAnnotationEditor();
            annotationEditor.BindPdf(_dataDir + "sample.pdf");
            annotationEditor.ImportAnnotations(sources);
            annotationEditor.Save(_dataDir + "sample_demo.pdf");
        }
```
El siguiente fragmento de código describe cómo importar/exportar anotaciones a un archivo XFDF:

```csharp
public static void ImportExportXFDF01()
        {
            PdfAnnotationEditor annotationEditor = new PdfAnnotationEditor();
            annotationEditor.BindPdf(_dataDir + "sample_cats_dogs.pdf");
            System.IO.FileStream xmlOutputStream = System.IO.File.OpenWrite(_dataDir + "sample.xfdf");
            annotationEditor.ExportAnnotationsToXfdf(xmlOutputStream);
            xmlOutputStream.Close();
            var document = new Document();
            document.Pages.Add();
            annotationEditor.BindPdf(document);
            annotationEditor.ImportAnnotationsFromXfdf(System.IO.File.OpenRead(_dataDir + "sample.xfdf"));
            annotationEditor.Save(_dataDir + "ImportedAnnotation.pdf");
        }
```

De esta manera, las anotaciones de los tipos especificados solo se importarán o exportarán a un archivo XFDF.

```csharp
   public static void ImportExportXFDF02()
        {
            PdfAnnotationEditor annotationEditor = new PdfAnnotationEditor();
            annotationEditor.BindPdf(_dataDir + "sample_cats_dogs.pdf");
            System.IO.FileStream xmlOutputStream = System.IO.File.OpenWrite(_dataDir + "sample.xfdf");
            var annotationTypes = new[] { AnnotationType.FreeText, AnnotationType.Text };
            annotationEditor.ExportAnnotationsXfdf(xmlOutputStream, 2, 2, annotationTypes);
            xmlOutputStream.Close();

            var document = new Document(_dataDir + "sample.pdf");
            document.Pages.Add();
            annotationEditor.BindPdf(document);
            annotationEditor.ImportAnnotationsFromXfdf(System.IO.File.OpenRead(_dataDir + "sample.xfdf"));
            annotationEditor.Save(_dataDir + "ImportedAnnotation.pdf");
        }
```