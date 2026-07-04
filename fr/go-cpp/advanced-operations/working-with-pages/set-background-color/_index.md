---
title: Définir la couleur de fond pour PDF avec Go
linktitle: Définir la couleur de fond
type: docs
weight: 80
url: /fr/go-cpp/set-background-color/
description: Définir la couleur de fond pour votre fichier PDF avec Go.
lastmod: "2026-07-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Définir la couleur de fond pour PDF avec Aspose.PDF for Go
Abstract: Aspose.PDF for Go via C++ offre une fonctionnalité permettant de définir la couleur de fond des pages PDF, permettant aux développeurs de personnaliser l’apparence des documents. Cette fonctionnalité permet l’application de couleurs unies sur l’ensemble du fond de la page, améliorant la présentation visuelle du document. Les développeurs peuvent facilement spécifier les valeurs de couleur à l'aide de modèles de couleur standard tels que RGB ou CMYK. La documentation fournit des instructions détaillées et des exemples de code pour aider les développeurs à mettre en œuvre la personnalisation de la couleur de fond efficacement dans leurs applications C++.
SoftwareApplication: go-cpp
---

1. L’extrait de code fourni montre comment définir une couleur de fond pour un fichier PDF en utilisant la bibliothèque Aspose.PDF en Go.
1. Le [Open](https://reference.aspose.com/pdf/go-cpp/core/open/) la méthode charge le fichier PDF spécifié en mémoire, permettant d’autres manipulations, comme la modification de son apparence ou de son contenu.
1. Le [SetBackground](https://reference.aspose.com/pdf/go-cpp/organize/setbackground/) la méthode applique une nouvelle couleur d’arrière-plan au document PDF. Les valeurs RVB permettent aux utilisateurs de personnaliser le style visuel du document.
1. Le [SaveAs](https://reference.aspose.com/pdf/go-cpp/core/saveas/) la méthode enregistre le PDF mis à jour sous un nouveau nom.

Ce code est idéal pour les applications qui doivent automatiser les personnalisations de PDF, telles que la création de rapports de marque, l'ajout de filigranes ou l'amélioration de la cohérence visuelle entre plusieurs documents.

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
      // SetBackground(r, g, b int32) sets PDF-document background color
      err = pdf.SetBackground(200, 100, 101)
      if err != nil {
        log.Fatal(err)
      }
      // SaveAs(filename string) saves previously opened PDF-document with new filename
      err = pdf.SaveAs("sample_SetBackground.pdf")
      if err != nil {
        log.Fatal(err)
      }
      // Close() releases allocated resources for PDF-document
      defer pdf.Close()
    }
```