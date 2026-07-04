---
title: Ouvrir un document PDF programmatiquement
linktitle: Ouvrir PDF
type: docs
weight: 20
url: /fr/go-cpp/open-pdf-document/
description: Apprenez comment ouvrir un fichier PDF avec Aspose.PDF for Go via C++.
lastmod: "2026-07-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Ouvrez un document PDF avec Aspose.PDF for Go via C++
Abstract: Aspose.PDF for Go via C++ offre une fonctionnalité puissante pour ouvrir et charger des documents PDF programmatiquement, permettant aux développeurs d'accéder et de manipuler le contenu PDF avec facilité. La bibliothèque prend en charge l'ouverture de fichiers PDF à partir de diverses sources, telles que les chemins de fichiers et les flux mémoire, tout en assurant un traitement efficace et une gestion des ressources. Elle propose des fonctionnalités pour inspecter les propriétés du document, extraire le texte et les images, et effectuer d'autres opérations sur les PDF chargés. La documentation comprend des instructions détaillées et des exemples de code pour aider les développeurs à intégrer les capacités d'ouverture de PDF dans leurs applications de manière transparente.
SoftwareApplication: go-cpp
---

## Ouvrir un document PDF existant

L'extrait de code démontre les opérations essentielles pour travailler avec des PDF en utilisant Aspose.PDF for Go. Il s'agit d'ouvrir un fichier, d'enregistrer les modifications et de fermer correctement les ressources. Cela en fait un exemple de base pour les développeurs qui manipulent des documents PDF.

L'exemple est simple, ce qui le rend facile à comprendre et à modifier. Il est idéal pour les débutants ou comme base pour des applications plus complexes.

La capacité d'ouvrir et d'enregistrer des documents PDF est une exigence fondamentale dans de nombreux scénarios, tels que la génération de rapports, la modification de documents ou la création de flux de travail automatisés.

Cet exemple met en avant la facilité d'utilisation de l'API pour la manipulation simple de PDF, qui peut être étendue pour inclure des fonctionnalités avancées comme l'extraction de texte, l'annotation ou le remplissage de formulaires.

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
        // Save() saves previously opened PDF-document
        err = pdf.Save()
        if err != nil {
            log.Fatal(err)
        }
        // Close() releases allocated resources for PDF-document
        defer pdf.Close()
    }
```
