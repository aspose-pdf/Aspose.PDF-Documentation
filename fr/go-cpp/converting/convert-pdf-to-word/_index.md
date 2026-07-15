---
title: Convertir des PDF en documents Word en Go
linktitle: Convertir PDF en Word
type: docs
weight: 10
url: /fr/go-cpp/convert-pdf-to-doc/
lastmod: "2026-07-04"
description: Apprenez à écrire du code Go pour la conversion de PDF en DOC (DOCX).
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Outil de conversion de PDF en Word avec Aspose.PDF for Go
Abstract: Aspose.PDF for Go via C++ permet la conversion transparente des documents PDF au format DOC tout en préservant le texte original, les images, les tableaux et la structure globale du document. Cette fonctionnalité permet aux développeurs de transformer des PDF statiques en fichiers Word modifiables pour une modification et un traitement ultérieurs. La bibliothèque offre diverses options de personnalisation pour contrôler la sortie de conversion, garantissant une haute fidélité et précision. La documentation comprend des instructions détaillées et du code d'exemple pour aider les développeurs à implémenter efficacement la conversion PDF-to-DOC dans leurs applications.
SoftwareApplication: go-cpp
---

Pour modifier le contenu d'un fichier PDF dans Microsoft Word ou d'autres traitements de texte qui prennent en charge les formats DOC et DOCX. Les fichiers PDF sont modifiables, mais les fichiers DOC et DOCX sont plus flexibles et personnalisables.

## Convertir PDF en DOC

L'extrait de code Go fourni démontre comment convertir un document PDF en DOC à l'aide de la bibliothèque Aspose.PDF:

1. Ouvrez un document PDF.
1. Convertir un fichier PDF en DOC en utilisant [SaveDoc](https://reference.aspose.com/pdf/go-cpp/convert/savedoc/) fonction.
1. Fermez le document PDF et libérez toutes les ressources allouées.

```go

    package main

    import "github.com/aspose-pdf/aspose-pdf-go-cpp"
    import "log"

    func main() {
      // Open(filename string) opens a PDF-document with filename
      pdf, err := asposepdf.Open("sample.pdf")
      if err != nil {
        log.Fatal(err)
      }
      // SaveDoc(filename string) saves previously opened PDF-document as Doc-document with filename
      err = pdf.SaveDoc("sample.doc")
      if err != nil {
        log.Fatal(err)
      }
      // Close() releases allocated resources for PDF-document
      defer pdf.Close()
    }
```

{{% alert color="success" %}}
**Essayez de convertir PDF en DOC en ligne**

Aspose.PDF for Go vous présente une application en ligne gratuite [“PDF to DOC”](https://products.aspose.app/pdf/conversion/pdf-to-doc), où vous pouvez essayer d'examiner la fonctionnalité et la qualité de son fonctionnement.

[![Convertir PDF en DOC](pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-doc) 
{{% /alert %}}

## Convertir PDF en DOCX

L'API Aspose.PDF for Go vous permet de lire et de convertir des documents PDF en DOCX. DOCX est un format bien connu pour les documents Microsoft Word dont la structure est passée d'un binaire simple à une combinaison de fichiers XML et binaires. Les fichiers DOCX peuvent être ouverts avec Word 2007 et les versions ultérieures, mais pas avec les versions antérieures de MS Word qui ne prennent en charge que les extensions de fichiers DOC.

L'extrait de code Go fourni montre comment convertir un document PDF en DOCX en utilisant la bibliothèque Aspose.PDF :

1. Ouvrez un document PDF.
1. Convertir un fichier PDF en DOCX en utilisant [SaveDocX](https://reference.aspose.com/pdf/go-cpp/convert/savedocx/) fonction.
1. Fermez le document PDF et libérez toutes les ressources allouées.

```go

    package main

    import "github.com/aspose-pdf/aspose-pdf-go-cpp"
    import "log"

    func main() {
      // Open(filename string) opens a PDF-document with filename
      pdf, err := asposepdf.Open("sample.pdf")
      if err != nil {
        log.Fatal(err)
      }
      // SaveDocX(filename string) saves previously opened PDF-document as DocX-document with filename
      err = pdf.SaveDocX("sample.docx")
      if err != nil {
        log.Fatal(err)
      }
      // Close() releases allocated resources for PDF-document
      defer pdf.Close()
    }
```

{{% alert color="success" %}}
**Essayez de convertir PDF en DOCX en ligne**

Aspose.PDF for Go vous présente une application en ligne gratuite ["PDF en Word"](https://products.aspose.app/pdf/conversion/pdf-to-docx), où vous pouvez essayer d'examiner la fonctionnalité et la qualité de son fonctionnement.

[![Aspose.PDF Conversion PDF en Word Application gratuite](pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-docx)

{{% /alert %}}