---
title: Importer et Exporter des Annotations au format XFDF 
linktitle: Importer et Exporter des Annotations au format XFDF
type: docs
weight: 40
url: fr/java/import-export-xfdf/
description: Vous pouvez importer et exporter des annotations au format XFDF en utilisant la bibliothèque Aspose.PDF pour Java. 
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

{{% alert color="primary" %}}

XFDF signifie XML Forms Data Format. C'est un format de fichier basé sur XML. Ce format de fichier est utilisé pour représenter les données de formulaire ou les annotations contenues dans un formulaire PDF. XFDF peut être utilisé à de nombreuses fins différentes, mais dans notre cas, il peut être utilisé pour envoyer ou recevoir des données de formulaire ou des annotations à d'autres ordinateurs ou serveurs, etc., ou il peut être utilisé pour archiver les données de formulaire ou les annotations. Dans cet article, nous verrons comment Aspose.Pdf.Facades a pris ce concept en considération et comment nous pouvons importer et exporter des données d'annotations vers un fichier XFDF.

{{% /alert %}}

**Aspose.PDF pour Java** est un composant riche en fonctionnalités lorsqu'il s'agit de modifier des documents PDF.
 As we know XFDF est un aspect important de la manipulation des formulaires PDF, le namespace Aspose.Pdf.Facades dans Aspose.PDF pour Java l'a très bien pris en compte et a fourni des méthodes pour importer et exporter les données d'annotations vers des fichiers XFDF.

[PDFAnnotationEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor) classe contient deux méthodes pour travailler avec l'importation et l'exportation d'annotations vers un fichier XFDF. [ExportAnnotationsXfdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor) méthode fournit la fonctionnalité d'exporter des annotations d'un document PDF vers un fichier XFDF, tandis que la méthode [ImportAnnotationFromXfdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor) vous permet d'importer des annotations à partir d'un fichier XFDF existant. Afin d'importer ou d'exporter des annotations, nous devons spécifier les types d'annotations. Nous pouvons spécifier ces types sous forme d'une énumération, puis passer cette énumération comme argument à l'une de ces méthodes. De cette façon, les annotations des types spécifiés seront uniquement importées ou exportées vers un fichier XFDF.

Le code suivant vous montre comment exporter des annotations vers un fichier XFDF :

```java
package com.aspose.pdf.examples;

import java.io.FileOutputStream;
import java.io.IOException;
import com.aspose.pdf.*;
import com.aspose.pdf.facades.PdfAnnotationEditor;

public class ExampleAnnotationImportExport {
    // Le chemin vers le répertoire des documents.
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";
    /*
     * Importation des annotations à partir d'un fichier XFDF XML Forms Data Format (XFDF)
     * créé par Adobe Acrobat, une application d'édition de PDF ; stocke des descriptions des
     * éléments de formulaire de page et leurs valeurs, telles que les noms et valeurs pour les champs
     * de texte ; utilisé pour enregistrer des données de formulaire pouvant être importées dans un document PDF.
     * Vous pouvez importer des données d'annotation depuis le fichier XFDF vers PDF en utilisant la
     * méthode ImportAnnotationsFromXfdf dans la classe PdfAnnotationEditor.
     */

    public static void ExportAnnotationXFDF() throws IOException {
        // Créer un objet PdfAnnotationEditor
        PdfAnnotationEditor AnnotationEditor = new PdfAnnotationEditor();

        // Lier le document PDF à l'éditeur d'annotations
        AnnotationEditor.bindPdf(_dataDir + "AnnotationDemo1.pdf");

        // Exporter les annotations
        FileOutputStream fileStream = new FileOutputStream(_dataDir + "exportannotations.xfdf");
        int[] annotType = { AnnotationType.Line, AnnotationType.Square };
        AnnotationEditor.exportAnnotationsXfdf(fileStream, 1, 1, annotType);
        fileStream.flush();
        fileStream.close();
    }
```

Le prochain extrait de code décrit comment importer des annotations dans un fichier XFDF :

```java
public static void ImportAnnotationXFDF()
{
    // Créer un objet PdfAnnotationEditor
    PdfAnnotationEditor AnnotationEditor = new PdfAnnotationEditor();
    // Créer un nouveau document PDF
    var document = new Document();
    document.Pages.Add();
    AnnotationEditor.BindPdf(document);

    var exportFileName = Path.Combine(_dataDir, "exportannotations.xfdf");
    if (!File.Exists(exportFileName))
        ExportAnnotationXFDF();

    // Importer l'annotation
    AnnotationEditor.ImportAnnotationsFromXfdf(exportFileName);

    // Enregistrer le PDF de sortie
    document.Save(Path.Combine(_dataDir, "AnnotationDemo2.pdf"));
}
```

## Une autre façon d'exporter/importer des annotations en une fois

Dans le code ci-dessous, une méthode ImportAnnotations permet d'importer des annotations directement à partir d'un autre document PDF.

```java
    public static void ImportAnnotationFromPDF() throws IOException {
        // Créer un objet PdfAnnotationEditor
        PdfAnnotationEditor AnnotationEditor = new PdfAnnotationEditor();
        // Créer un nouveau document PDF
        Document document = new Document();

        document.getPages().add();
        AnnotationEditor.bindPdf(document);
        String exportFileName = _dataDir + "exportannotations.xfdf";
        java.io.File f = new java.io.File(exportFileName);
        if (!f.exists()) {
            ExportAnnotationXFDF();
        }

        // L'éditeur d'annotations permet d'importer des annotations depuis plusieurs documents PDF,
        // mais dans cet exemple, nous n'en utilisons qu'un.
        String[] fileNames = { _dataDir + "AnnotationDemo1.pdf" };
        AnnotationEditor.importAnnotations(fileNames);

        // Enregistrer le PDF de sortie
        document.save(_dataDir + "AnnotationDemo3.pdf");
    }
}
```