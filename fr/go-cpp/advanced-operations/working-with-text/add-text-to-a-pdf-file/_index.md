---
title: Ajouter du texte à un PDF avec Go
linktitle: Ajouter du texte à un PDF
type: docs
weight: 10
url: /fr/go-cpp/add-text-to-pdf-file/
description: Apprenez comment ajouter du texte à un document PDF en Go en utilisant Aspose.PDF pour l'amélioration du contenu et l'édition de documents.
lastmod: "2026-07-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
AlternativeHeadline: Ajouter du texte à un PDF en utilisant Aspose.PDF pour Go
Abstract: La section « Add Text to PDF File » de la documentation Aspose.PDF pour C++ et Go fournit des instructions étape par étape sur l’insertion de texte dans des documents PDF de manière programmatique. Elle couvre diverses méthodes d’ajout de texte, y compris le positionnement, la personnalisation des polices, les ajustements de couleur et les options d’alignement du texte. Le guide démontre comment ajouter du texte à des pages et des emplacements spécifiques dans un PDF, assurant un placement précis du contenu. Avec des exemples de code détaillés et des explications, les développeurs peuvent facilement intégrer des fonctionnalités d’insertion de texte dans leurs applications pour une gestion améliorée des documents PDF.
SoftwareApplication: go-cpp
---

Pour ajouter du texte à un fichier PDF existant :

1. Ouvrez un fichier PDF.
1. Ajoutez le texte au document PDF avec [PageAddText](https://reference.aspose.com/pdf/go-cpp/organize/pageaddtext/) fonction.
1. Enregistre les modifications dans le même fichier.

## Ajout de texte

L'extrait de code suivant montre comment ajouter du texte dans un fichier PDF existant.

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
        // PageAddText(num int32, addText string) adds text on page
        err = pdf.PageAddText(1, "added text")
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
