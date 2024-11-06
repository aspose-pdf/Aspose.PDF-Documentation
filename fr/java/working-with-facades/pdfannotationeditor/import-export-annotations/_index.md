---
title: Importer et Exporter des Annotations au format XFDF en utilisant com.aspose.pdf.facades
type: docs
weight: 20
url: fr/java/import-export-annotations/
description: Cette section explique comment exporter et importer des annotations d'un fichier PDF vers XFDF avec Aspose.PDF Facades.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

XFDF signifie XML Forms Data Format. C'est un format de fichier basé sur XML. Ce format de fichier est utilisé pour représenter les données de formulaire ou les annotations contenues dans un formulaire PDF. XFDF peut être utilisé à de nombreuses fins différentes, mais dans notre cas, il peut être utilisé soit pour envoyer ou recevoir des données de formulaire ou des annotations à d'autres ordinateurs ou serveurs, etc., soit il peut être utilisé pour archiver les données de formulaire ou les annotations. Dans cet article, nous verrons comment Aspose.Pdf.Facades a pris ce concept en considération et comment nous pouvons importer et exporter des données d'annotations vers un fichier XFDF.

La classe [PDFAnnotationEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor) contient deux méthodes pour travailler avec l'importation et l'exportation d'annotations vers un fichier XFDF.
 [ExportAnnotationsXfdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor#exportAnnotationsToXfdf-java.io.OutputStream-) méthode fournit la fonctionnalité pour exporter des annotations d'un document PDF vers un fichier XFDF, tandis que la méthode [ImportAnnotationFromXfdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor#importAnnotationFromXfdf-java.io.InputStream-) vous permet d'importer des annotations à partir d'un fichier XFDF existant. Afin d'importer ou d'exporter des annotations, nous devons spécifier les types d'annotation. Nous pouvons spécifier ces types sous la forme d'une énumération puis passer cette énumération comme argument à l'une de ces méthodes.

Le code suivant vous montre comment importer des annotations dans un fichier XFDF :

```java
public static void ImportAnnotation() {
        String[] sources = new String[] { _dataDir + "sample_cats_dogs.pdf" };
        PdfAnnotationEditor annotationEditor = new PdfAnnotationEditor();
        annotationEditor.bindPdf(_dataDir + "sample.pdf");
        annotationEditor.importAnnotations(sources);
        annotationEditor.save(_dataDir + "sample_demo.pdf");
    }
```

Le prochain extrait de code décrit comment importer/exporter des annotations vers un fichier XFDF :

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

De cette façon, les annotations des types spécifiés seront uniquement importées ou exportées vers un fichier XFDF.

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