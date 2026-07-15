---
title: Faire pivoter les pages PDF avec Go
linktitle: Faire pivoter les pages PDF
type: docs
weight: 50
url: /fr/go-cpp/rotate-pages/
description: Ce sujet décrit comment faire pivoter l'orientation de la page dans un fichier PDF existant de manière programmatique avec Go via C++
lastmod: "2026-07-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Faire pivoter les pages PDF avec Aspose.PDF for Go
Abstract: Aspose.PDF for Go via C++ offre une fonctionnalité robuste pour faire pivoter les pages des documents PDF, permettant aux développeurs de modifier l'orientation des pages selon les besoins. La bibliothèque prend en charge la rotation des pages de 90, 180 ou 270 degrés, permettant des ajustements rapides et efficaces de la mise en page du document. Cette fonctionnalité est utile pour corriger les pages mal orientées ou modifier la présentation du document\u2019s. La documentation comprend des instructions étape par étape ainsi que des exemples de code pour aider les développeurs à intégrer de manière transparente les capacités de rotation des pages dans leurs applications.
SoftwareApplication: go-cpp
---

Cette section décrit comment changer l'orientation de la page du mode paysage au mode portrait et vice versa dans un fichier PDF existant en utilisant Go.

Faire pivoter les pages garantit un alignement correct pour l'impression ou l'affichage des PDF dans des environnements professionnels.

1. Ouvrez le document PDF.
1. Faire pivoter les pages PDF. Le [PageRotate](https://reference.aspose.com/pdf/go-cpp/organize/rotate/) La fonction applique une rotation spécifique (dans ce cas, 180 degrés) à une page donnée.
1. Enregistrez les modifications dans un nouveau fichier. Le [SaveAs](https://reference.aspose.com/pdf/go-cpp/core/saveas/) La fonction crée un nouveau fichier PDF pour conserver l'original tout en enregistrant la version mise à jour.

Dans cet exemple, vous faites pivoter une page spécifique d'un document PDF :

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
    // PageRotate(num int32, rotation int32) rotates page
    err = pdf.PageRotate(1, asposepdf.RotationOn180)
    if err != nil {
      log.Fatal(err)
    }
    // SaveAs(filename string) saves previously opened PDF-document with new filename
    err = pdf.SaveAs("sample_page1_Rotate.pdf")
    if err != nil {
      log.Fatal(err)
    }
    // Close() releases allocated resources for PDF-document
    defer pdf.Close()
  }
```

Vous avez également la possibilité de faire pivoter toutes les pages PDF de votre document :

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
    // Rotate(rotation int32) rotates PDF-document
    err = pdf.Rotate(asposepdf.RotationOn270)
    if err != nil {
      log.Fatal(err)
    }
    // SaveAs(filename string) saves previously opened PDF-document with new filename
    err = pdf.SaveAs("sample_Rotate.pdf")
    if err != nil {
      log.Fatal(err)
    }
    // Close() releases allocated resources for PDF-document
    defer pdf.Close()
  }
```