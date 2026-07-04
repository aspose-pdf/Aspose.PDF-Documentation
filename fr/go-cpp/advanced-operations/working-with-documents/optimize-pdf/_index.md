---
title: Optimiser le PDF en utilisant Aspose.PDF for Go via C++
linktitle: Optimiser le fichier PDF
type: docs
weight: 10
url: /fr/go-cpp/optimize-pdf/
description: Optimiser et compresser les fichiers PDF en utilisant l'outil Go.
lastmod: "2026-07-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Optimiser et compresser les fichiers PDF en utilisant Aspose.PDF for Go
Abstract: Aspose.PDF for Go via C++ offre des fonctionnalités d'optimisation puissantes pour réduire la taille et améliorer les performances des documents PDF. La bibliothèque fournit diverses options d'optimisation, y compris la compression des images, la suppression des objets inutilisés, la réduction de la taille des Font, et l'optimisation des flux de contenu. Ces fonctionnalités contribuent à améliorer l'efficacité du stockage des documents et assurent des temps de traitement et de chargement plus rapides. La documentation fournit des instructions étape par étape et des exemples de code pour aider les développeurs à mettre en œuvre l'optimisation PDF efficacement dans leurs applications.
SoftwareApplication: go-cpp
---

## Optimiser le document PDF

Le kit d'outils avec Aspose.PDF for Go via C++ vous permet d'optimiser un document PDF.

Cet extrait de code est utile pour les applications où réduire la taille ou améliorer l'efficacité des fichiers PDF est crucial, par exemple pour les téléchargements web, l'archivage ou le partage avec une bande passante limitée.

1. Le [Ouvrir](https://reference.aspose.com/pdf/go-cpp/core/open/) la méthode charge le fichier PDF spécifié (sample.pdf) en mémoire.
1. Le [Méthode Optimize](https://reference.aspose.com/pdf/go-cpp/organize/optimize/) réduit la taille du fichier en effectuant des optimisations telles que la suppression d'objets inutilisés, la compression des images, l'aplatissement des annotations, le désembarquement des polices et l'activation de la réutilisation du contenu. Ces étapes aident à réduire les besoins de stockage et à améliorer la vitesse de traitement du document PDF.
1. Le [SaveAs](https://reference.aspose.com/pdf/go-cpp/core/saveas/) La méthode enregistre le PDF optimisé dans un nouveau fichier.

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
      // Optimize() optimizes PDF-document content
      err = pdf.Optimize()
      if err != nil {
        log.Fatal(err)
      }
      // SaveAs(filename string) saves previously opened PDF-document with new filename
      err = pdf.SaveAs("sample_Optimize.pdf")
      if err != nil {
        log.Fatal(err)
      }
      // Close() releases allocated resources for PDF-document
      defer pdf.Close()
    }
```