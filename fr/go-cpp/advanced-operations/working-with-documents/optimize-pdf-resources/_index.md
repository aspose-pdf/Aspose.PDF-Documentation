---
title: Optimiser les ressources PDF à l'aide de Go
linktitle: Optimiser les ressources PDF
type: docs
weight: 15
url: /fr/go-cpp/optimize-pdf-resources/
description: Optimiser les ressources des fichiers PDF à l'aide de l'outil Go.
lastmod: "2026-07-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Optimiser les ressources PDF à l'aide d'Aspose.PDF for Go
Abstract: Aspose.PDF for Go via C++ offre des capacités avancées pour optimiser les ressources PDF, améliorant l'efficacité du document et réduisant la taille du fichier. La bibliothèque permet aux développeurs d'optimiser les polices, les images et les métadonnées en supprimant les données redondantes et en compressant les ressources sans compromettre la qualité du document. Ces techniques d'optimisation améliorent les performances du document, rendant les PDF plus adaptés au partage et au stockage. La documentation propose des directives détaillées et des exemples de code pour aider les développeurs à mettre en œuvre efficacement l'optimisation des ressources dans leurs applications.
SoftwareApplication: go-cpp
---

## Optimiser les ressources PDF

Optimiser les ressources dans le document :

  1. Les ressources qui ne sont pas utilisées sur les pages du document sont supprimées.
  1. Les ressources égales sont regroupées en un seul objet.
  1. Les objets inutilisés sont supprimés.

L'optimisation peut inclure la compression d'images, la suppression d'objets inutilisés et l'optimisation des polices pour réduire la taille du fichier et améliorer les performances. Toute erreur survenant pendant cette opération est enregistrée et termine le programme.  
 
1. Le [Ouvrir](https://reference.aspose.com/pdf/go-cpp/core/open/) La méthode charge le fichier PDF spécifié (sample.pdf) en mémoire.
1. Optimise les ressources du PDF pour l'efficacité en utilisant [OptimizeResource](https://reference.aspose.com/pdf/go-cpp/organize/optimizeresource/) méthode.
1. Le [SaveAs](https://reference.aspose.com/pdf/go-cpp/core/saveas/) La méthode enregistre le PDF optimisé dans un nouveau fichier.

Le fragment de code suivant montre comment optimiser un document PDF.

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
      // OptimizeResource() optimizes resources of PDF-document
      err = pdf.OptimizeResource()
      if err != nil {
        log.Fatal(err)
      }
      // SaveAs(filename string) saves previously opened PDF-document with new filename
      err = pdf.SaveAs("sample_OptimizeResource.pdf")
      if err != nil {
        log.Fatal(err)
      }
      // Close() releases allocated resources for PDF-document
      defer pdf.Close()
    }
```