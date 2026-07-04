---
title: Convertir PDF en Excel avec Go
linktitle: Convertir PDF en Excel
type: docs
weight: 20
url: /fr/go-cpp/convert-pdf-to-xlsx/
lastmod: "2026-07-04"
description: Aspose.PDF for Go vous permet de convertir un PDF au format XLSX.
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Outil Golang pour convertir des documents PDF en Excel
Abstract: La bibliothèque Aspose.PDF for Go via C++ fournit une solution robuste pour convertir des documents PDF au format XLSX avec une grande précision et efficacité. Cette fonctionnalité permet aux développeurs d'extraire les données tabulaires des PDF tout en préservant la disposition originale, la structure et le formatage des feuilles de calcul Excel. La documentation propose des directives détaillées pour mettre en œuvre le processus de conversion, incluant du code d'exemple et des instructions étape par étape afin de faciliter une intégration transparente dans les applications Go.
SoftwareApplication: go-cpp
---

**Aspose.PDF for Go** prend en charge la fonctionnalité de conversion des fichiers PDF au format Excel.

## Convertir le PDF en XLSX

Excel offre des outils avancés pour trier, filtrer et analyser les données, facilitant ainsi l'exécution de tâches telles que l'analyse des tendances ou la modélisation financière, qui sont difficiles avec des fichiers PDF statiques. Copier manuellement les données des PDF vers Excel prend du temps et est sujet aux erreurs. La conversion automatise ce processus, économisant un temps considérable pour les grands ensembles de données.

Aspose.PDF for Go utilise [SaveXlsX](https://reference.aspose.com/pdf/go-cpp/convert/savexlsx/) pour convertir le fichier PDF téléchargé en une feuille de calcul Excel et l'enregistrer.

1. Importer les packages requis.
1. Ouvrir un fichier PDF.
1. Convertir le PDF en XLSX en utilisant [SaveXlsX](https://reference.aspose.com/pdf/go-cpp/convert/savexlsx/).
1. Fermer le document PDF.

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
    // SaveXlsX(filename string) saves previously opened PDF-document as XlsX-document with filename
    err = pdf.SaveXlsX("sample.xlsx")
    if err != nil {
      log.Fatal(err)
    }
    // Close() releases allocated resources for PDF-document
    defer pdf.Close()
  }
```

{{% alert color="success" %}}
**Essayez de convertir le PDF en Excel en ligne**

Aspose.PDF for Go vous présente une application en ligne gratuite [\"PDF vers XLSX\"](https://products.aspose.app/pdf/conversion/pdf-to-xlsx), où vous pouvez essayer d'examiner la fonctionnalité et la qualité avec lesquelles il fonctionne.

[![Aspose.PDF Conversion PDF vers Excel avec Application gratuite](pdf_to_xlsx.png)](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)
{{% /alert %}}