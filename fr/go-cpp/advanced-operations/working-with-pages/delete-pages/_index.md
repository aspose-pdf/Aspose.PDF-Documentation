---
title: Supprimer des pages PDF avec Go
linktitle: Supprimer des pages PDF
type: docs
weight: 30
url: /fr/go-cpp/delete-pages/
description: Vous pouvez supprimer des pages de votre fichier PDF en utilisant Aspose.PDF for Go via C++.
lastmod: "2026-07-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Supprimer des pages PDF avec Aspose.PDF for Go
Abstract: Aspose.PDF for Go via C++ offre une fonctionnalité efficace pour supprimer des pages de documents PDF, permettant aux développeurs de retirer facilement les pages indésirables ou superflues. La bibliothèque permet la suppression de pages uniques ou multiples en spécifiant les numéros de page ou les plages, garantissant des modifications précises du document. Cette fonctionnalité aide à rationaliser les fichiers PDF en éliminant le contenu redondant et en optimisant la structure du document. La documentation fournit des instructions étape par étape ainsi que des exemples de code pour aider les développeurs à implémenter efficacement la fonctionnalité de suppression de pages dans leurs applications.
SoftwareApplication: go-cpp
---

Vous pouvez supprimer des pages d'un fichier PDF en utilisant **Aspose.PDF for Go via C++**. Le fragment de code suivant montre comment manipuler un document PDF en supprimant une page spécifique. Cette méthode est efficace pour les tâches de manipulation de documents PDF, notamment pour la suppression de pages, l'enregistrement du document modifié et la garantie d'une gestion appropriée des ressources.

1. Ouverture d'un fichier PDF.
1. Suppression d'une page spécifique avec [PageDelete](https://reference.aspose.com/pdf/go-cpp/core/pagedelete/) fonction.
1. Enregistrement du document avec [Save](https://reference.aspose.com/pdf/go-cpp/core/save/) méthode.

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
      // PageDelete(num int32) deletes specified page in PDF-document
      err = pdf.PageDelete(1)
      if err != nil {
        log.Fatal(err)
      }
      // Save() saves previously opened PDF-document
      err = pdf.Save()
      if err != nil {
        log.Fatal(err)
      }
      // Close() releases allocated resources for PDF-document
      defer pdf.Close()
    }
```
