---
title: Importer et Exporter des Annotations vers XFDF 
type: docs
weight: 20
url: /net/import-export-annotations/
description: Cette section explique comment importer et exporter des annotations d'un fichier PDF vers XFDF avec Aspose.PDF Facades.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

XFDF signifie XML Forms Data Format. Il s'agit d'un format de fichier basé sur XML. Ce format de fichier est utilisé pour représenter les données de formulaire ou les annotations contenues dans un formulaire PDF. XFDF peut être utilisé pour de nombreuses fins différentes, mais dans notre cas, il peut être utilisé soit pour envoyer ou recevoir des données de formulaire ou des annotations à d'autres ordinateurs ou serveurs, etc., soit il peut être utilisé pour archiver les données de formulaire ou les annotations. Dans cet article, nous verrons comment Aspose.Pdf.Facades a pris en compte ce concept et comment nous pouvons importer et exporter des données d'annotations vers un fichier XFDF.

## Importer et Exporter des Annotations vers XFDF

[Aspose.PDF pour .NET](/pdf/net/) est un composant riche en fonctionnalités lorsqu'il s'agit de modifier des documents PDF. ```
Comme nous le savons, XFDF est un aspect important de la manipulation des formulaires PDF, le [namespace Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) dans [Aspose.PDF for .NET](/pdf/net/) l'a très bien pris en compte et a fourni des méthodes pour importer et exporter des données d'annotations vers des fichiers XFDF.

La classe [PDFAnnotationEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor) contient deux méthodes pour travailler avec l'importation et l'exportation des annotations vers un fichier XFDF.
``` [ExportAnnotationsXfdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor/methods/exportannotationsxfdf/index) méthode fournit la fonctionnalité pour exporter les annotations d'un document PDF vers un fichier XFDF, tandis que la méthode [ImportAnnotationFromXfdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor/methods/importannotationfromxfdf/index) vous permet d'importer des annotations à partir d'un fichier XFDF existant. Afin d'importer ou d'exporter des annotations, nous devons spécifier les types d'annotations. Nous pouvons spécifier ces types sous forme d'une énumération et ensuite passer cette énumération comme argument à l'une de ces méthodes. De cette façon, les annotations des types spécifiés seront uniquement importées ou exportées vers un fichier XFDF.

L'extrait de code suivant vous montre comment importer des annotations vers un fichier XFDF :

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
Le prochain extrait de code décrit comment importer/exporter des annotations vers un fichier XFDF :

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

De cette façon, les annotations des types spécifiés seront uniquement importées ou exportées vers un fichier XFDF.

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