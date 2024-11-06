---
title: Importer et Exporter des Annotations au format XFDF en utilisant Aspose.PDF pour C++
linktitle: Importer et Exporter des Annotations au format XFDF
type: docs
weight: 40
url: fr/cpp/import-export-xfdf/
description: Vous pouvez importer et exporter des annotations avec le format XFDF avec C++ et la bibliothèque Aspose.PDF pour C++.
lastmod: "2021-12-02"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

{{% alert color="primary" %}}

XFDF est un format de fichier compatible avec les lecteurs PDF. Les fichiers XFDF utilisent le format XML pour stocker des données telles que l'encodage de formulaire et les annotations, qui peuvent être enregistrées et importées/exportées vers le PDF et visualisées.

XFDF peut être utilisé pour de nombreuses autres tâches différentes, mais dans notre cas, il peut être utilisé soit pour envoyer ou recevoir des données de formulaire ou des annotations vers d'autres ordinateurs ou serveurs, etc., soit il peut être utilisé pour archiver des données de formulaire ou des annotations.

{{% /alert %}}

**Aspose.PDF pour C++** est un composant riche en fonctionnalités lorsqu'il s'agit de modifier des documents PDF. Comme nous le savons, XFDF est un aspect important de la manipulation des formulaires PDF, l'espace de noms Aspose.Pdf.Facades dans Aspose.PDF pour C++ l'a très bien pris en compte et a fourni des méthodes pour importer et exporter des données d'annotations vers des fichiers XFDF.

La classe [PDFAnnotationEditor](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.facades.pdf_annotation_editor/) contient deux méthodes pour travailler avec l'importation et l'exportation d'annotations vers un fichier XFDF. [ExportAnnotationsXfdf](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.facades.pdf_annotation_editor#a533c7c17dfd25a2a192617492bbb561c) méthode fournit la fonctionnalité pour exporter des annotations d'un document PDF vers un fichier XFDF, tandis que [ImportAnnotationFromXfdf](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.facades.pdf_annotation_editor#a17902042e1b48f5a85c0cfb8c428af0a) méthode vous permet d'importer des annotations à partir d'un fichier XFDF existant. Afin d'importer ou d'exporter des annotations, nous devons spécifier les types d'annotation. Nous pouvons spécifier ces types sous forme d'une énumération, puis passer cette énumération en tant qu'argument à l'une de ces méthodes.

Le fragment de code suivant vous montre comment exporter des annotations vers un fichier XFDF :

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Annotations;
using namespace Aspose::Pdf::Facades;

void AnnotationImportExport::ExportAnnotationXFDF() {

    String _dataDir("C:\\Samples\\");

    // Créer un objet PdfAnnotationEditor
    auto annotationEditor = MakeObject<PdfAnnotationEditor>();

    // Lier le document PDF à l'éditeur d'annotations
    annotationEditor->BindPdf(_dataDir + u"AnnotationDemo1.pdf");

    // Exporter les annotations
    auto fileStream = System::IO::File::OpenWrite(_dataDir +u"exportannotations.xfdf");
    auto annotType = MakeArray<AnnotationType>({ AnnotationType::Line, AnnotationType::Square });
    annotationEditor->ExportAnnotationsXfdf(fileStream, 1, 1, annotType);
    fileStream->Flush();
    fileStream->Close();
}
```
Le prochain extrait de code décrit comment importer des annotations dans un fichier XFDF :

```cpp
void AnnotationImportExport::ImportAnnotationXFDF() {

    // Créer un objet PdfAnnotationEditor
    auto annotationEditor = MakeObject<PdfAnnotationEditor>();

    // Créer un nouveau document PDF
    auto document = new Document();
    document->get_Pages()->Add();

    annotationEditor->BindPdf(document);

    String _dataDir("C:\\Samples\\");
    String exportFileName = _dataDir + u"exportannotations.xfdf";

    if (!System::IO::File::Exists(exportFileName))
        ExportAnnotationXFDF();

    // Importer l'annotation
    annotationEditor->ImportAnnotationsFromXfdf(exportFileName);

    // Enregistrer le PDF de sortie
    document->Save(_dataDir + u"AnnotationDemo2.pdf");
}
```

## Encore une autre façon d'exporter/importer des annotations à la fois

Dans le code ci-dessous, une méthode ImportAnnotations permet d'importer des annotations directement à partir d'un autre document PDF.

```cpp
void AnnotationImportExport::ImportAnnotationFromPDF() {

    // Créer un objet PdfAnnotationEditor
    auto annotationEditor = MakeObject<PdfAnnotationEditor>();

    // Créer un nouveau document PDF
    auto document = new Document();
    document->get_Pages()->Add();

    annotationEditor->BindPdf(document);
    String _dataDir("C:\\Samples\\");
    String exportFileName = _dataDir + u"exportannotations.xfdf";

    if (!System::IO::File::Exists(exportFileName))
        ExportAnnotationXFDF();

    // L'éditeur d'annotations permet d'importer des annotations à partir de plusieurs documents PDF,
    // mais dans cet exemple, nous n'utilisons qu'un seul.
    auto fileStreams = MakeArray<String>({ _dataDir + u"AnnotationDemo1.pdf" });
    annotationEditor->ImportAnnotations(fileStreams);

    // Enregistrer le PDF de sortie
    document->Save(_dataDir + u"AnnotationDemo3.pdf");
}
```