---
title: Enregistrer le document PDF de manière programmatique
linktitle: Enregistrer le PDF
type: docs
weight: 30
url: /fr/go-cpp/save-pdf-document/
description: Apprenez comment enregistrer un fichier PDF avec Aspose.PDF for Go via C++.
lastmod: "2026-07-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Enregistrer le document PDF avec Aspose.PDF for Go via C++
Abstract: Aspose.PDF for Go via C++ offre une fonctionnalité complète pour enregistrer des documents PDF dans différents formats et emplacements avec une grande efficacité et flexibilité. La bibliothèque permet aux développeurs d’enregistrer les PDF sur des systèmes de fichiers, des flux mémoire, ou de les exporter vers des formats alternatifs tels que DOCX, XLSX et des images. Elle fournit des options pour personnaliser les paramètres d’enregistrement, optimiser la taille du fichier et garantir l’intégrité des données. La documentation comprend des instructions détaillées et des exemples de code pour aider les développeurs à implémenter efficacement les capacités d’enregistrement de PDF dans leurs applications.
SoftwareApplication: go-cpp
---

## Enregistrer le document PDF sur le système de fichiers

L'exemple démontre le [Nouveau](https://reference.aspose.com/pdf/go-cpp/core/new/) méthode de création d'un nouveau document PDF, qui est une fonctionnalité fondamentale pour générer des documents dynamiquement, tels que des rapports ou des factures.

Le code est simple et peut servir de modèle pour des fonctionnalités plus avancées comme l'ajout de texte, d'images ou d'annotations au PDF.

Cet exemple démontre l'utilisation directe de la bibliothèque Aspose.PDF Go, mettant en avant son potentiel pour créer, modifier et enregistrer des documents.

```go

    package main

    import "github.com/aspose-pdf/aspose-pdf-go-cpp"
    import "log"

    func main() {
        // New creates a new PDF-document
        pdf, err := asposepdf.New()
        if err != nil {
            log.Fatal(err)
        }
        // SaveAs(filename string) saves previously opened PDF-document with new filename
        err = pdf.SaveAs("sample_New_SaveAs.pdf")
        if err != nil {
            log.Fatal(err)
        }
        // Close() releases allocated resources for PDF-document
        defer pdf.Close()
    }
```
