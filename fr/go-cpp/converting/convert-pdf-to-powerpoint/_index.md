---
title: Convertir PDF en PPTX en Go
linktitle: Convertir PDF en PowerPoint
type: docs
weight: 30
url: /fr/go-cpp/convert-pdf-to-powerpoint/
lastmod: "2026-07-04"
description: Aspose.PDF vous permet de convertir un PDF au format PPTX en utilisant Go.
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Outil Golang pour convertir PDF en PowerPoint
Abstract: Aspose.PDF for Go via C++ fournit une solution fiable pour convertir des documents PDF au format PowerPoint (PPTX) tout en préservant la mise en page, le formatage et la structure du contenu d'origine. Cette fonctionnalité permet aux développeurs de transformer sans effort les fichiers PDF statiques en présentations dynamiques et éditables. La bibliothèque offre des options de personnalisation pour contrôler le processus de conversion, garantissant une sortie de haute qualité adaptée à un usage professionnel et commercial. La documentation fournit des instructions étape par étape ainsi que des exemples de code pour aider les développeurs à intégrer efficacement la conversion PDF vers PowerPoint dans leurs applications.
SoftwareApplication: go-cpp
---

## Convertir PDF en PPTX

L'extrait de code Go fourni montre comment convertir un document PDF en PPTX en utilisant la bibliothèque Aspose.PDF :

1. Ouvrez un document PDF.
1. Convertissez un fichier PDF en PPTX en utilisant [SavePptx](https://reference.aspose.com/pdf/go-cpp/convert/savepptx/) fonction.
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
      // SavePptX(filename string) saves previously opened PDF-document as PptX-document with filename
      err = pdf.SavePptX("sample.pptx")
      if err != nil {
        log.Fatal(err)
      }
      // Close() releases allocated resources for PDF-document
      defer pdf.Close()
    }
```

{{% alert color="success" %}}
**Essayer de convertir le PDF en PowerPoint en ligne**

Aspose.PDF for Go vous propose une application en ligne gratuite [“PDF to PPTX”](https://products.aspose.app/pdf/conversion/pdf-to-pptx), où vous pouvez essayer d'explorer la fonctionnalité et la qualité de son fonctionnement.

[![Aspose.PDF Conversion PDF en PPTX avec App gratuite](pdf_to_pptx.png)](https://products.aspose.app/pdf/conversion/pdf-to-pptx)
{{% /alert %}}