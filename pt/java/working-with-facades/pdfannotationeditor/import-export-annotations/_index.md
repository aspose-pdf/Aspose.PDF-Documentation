---
title: Importar e Exportar Anotações para o formato XFDF usando com.aspose.pdf.facades
type: docs
weight: 20
url: /pt/java/import-export-annotations/
description: Esta seção explica como exportar e importar anotações de um arquivo PDF para XFDF com Aspose.PDF Facades.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

XFDF significa Formato de Dados de Formulários XML. É um formato de arquivo baseado em XML. Este formato de arquivo é usado para representar dados de formulário ou anotações contidas em um formulário PDF. XFDF pode ser usado para diversos propósitos, mas em nosso caso, pode ser usado para enviar ou receber dados de formulário ou anotações para outros computadores ou servidores etc., ou pode ser usado para arquivar os dados de formulário ou anotações. Neste artigo, veremos como o Aspose.Pdf.Facades considerou esse conceito e como podemos importar e exportar dados de anotações para o arquivo XFDF.

A classe [PDFAnnotationEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor) contém dois métodos para trabalhar com a importação e exportação de anotações para o arquivo XFDF.
 [ExportAnnotationsXfdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor#exportAnnotationsToXfdf-java.io.OutputStream-) método fornece a funcionalidade para exportar anotações de um documento PDF para um arquivo XFDF, enquanto o método [ImportAnnotationFromXfdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor#importAnnotationFromXfdf-java.io.InputStream-) permite que você importe anotações de um arquivo XFDF existente. Para importar ou exportar anotações, precisamos especificar os tipos de anotação. Podemos especificar esses tipos na forma de uma enumeração e depois passar essa enumeração como um argumento para qualquer um desses métodos.

O snippet de código a seguir mostra como importar anotações para um arquivo XFDF:

```java
public static void ImportAnnotation() {
        String[] sources = new String[] { _dataDir + "sample_cats_dogs.pdf" };
        PdfAnnotationEditor annotationEditor = new PdfAnnotationEditor();
        annotationEditor.bindPdf(_dataDir + "sample.pdf");
        annotationEditor.importAnnotations(sources);
        annotationEditor.save(_dataDir + "sample_demo.pdf");
    }
```

O próximo trecho de código descreve como importar/exportar anotações para um arquivo XFDF:

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

Dessa forma, as anotações dos tipos especificados serão apenas importadas ou exportadas para um arquivo XFDF.

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