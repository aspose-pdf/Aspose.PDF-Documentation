---
title: Exemple de Hello World utilisant le langage Go
linktitle: Exemple Hello World
type: docs
weight: 40
url: /fr/go-cpp/hello-world-example/
description: Cet exemple montre comment créer un document PDF simple contenant le texte Hello World en utilisant Aspose.PDF for Go.
lastmod: "2026-07-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Hello World via Aspose.PDF for Go
Abstract: Le guide de démarrage pour Aspose.PDF for Go via C++ fournit une introduction à l'utilisation de la bibliothèque, couvrant les étapes de base pour créer et manipuler des documents PDF. Il inclut un exemple « Hello World » démontrant comment générer un fichier PDF simple avec du texte, aidant les développeurs à comprendre rapidement la fonctionnalité principale de l'API.
SoftwareApplication: go-cpp
---

Un exemple « Hello World » est traditionnellement utilisé pour présenter les fonctionnalités d'un langage de programmation ou d'un logiciel avec un cas d'utilisation simple.

**Aspose.PDF for Go** est une API PDF riche en fonctionnalités qui permet aux développeurs d’intégrer la création, la manipulation et la conversion de documents PDF avec Go. Elle prend en charge de nombreux formats de fichiers populaires, dont PDF, TXT, XPS, EPUB, TEX, DOC, DOCX, PPTX, les formats d’image, etc. Dans cet article, nous créons un document PDF contenant le texte "Hello World!" Après avoir installé Aspose.PDF for Go dans votre environnement, vous pouvez exécuter l’exemple de code pour voir comment fonctionne l’API Aspose.PDF.
Le fragment de code ci‑dessous suit ces étapes :

1. Créer une nouvelle instance de document PDF.
1. Ajouter une nouvelle page au document PDF en utilisant [PageAdd](https://reference.aspose.com/pdf/go-cpp/core/pageadd/) fonction.
1. Définir la taille de la page en utilisant [PageSetSize](https://reference.aspose.com/pdf/go-cpp/organize/pagesetsize/).
1. Ajouter le texte "Hello World!" à la première page en utilisant [PageAddText](https://reference.aspose.com/pdf/go-cpp/organize/pageaddtext/).
1. Enregistrer le document PDF réparé en utilisant [SaveAs](https://reference.aspose.com/pdf/go-cpp/core/saveas/) méthode.
1. Fermez le document PDF et libérez toutes les ressources allouées.

Le fragment de code suivant est un programme Hello World pour illustrer le fonctionnement de l'API Aspose.PDF for Go.

```go

    package main

    import "github.com/aspose-pdf/aspose-pdf-go-cpp"
    import "log"

    func main() {
        // Create new PDF-document
        pdf, err := asposepdf.New()
        if err != nil {
                log.Fatal(err)
        }
        // Add new page
        err = pdf.PageAdd()
        if err != nil {
                log.Fatal(err)
        }
        // Set page size A4
        err = pdf.PageSetSize(1, asposepdf.PageSizeA4)
        if err != nil {
                log.Fatal(err)
        }
        // Add text on first page
        err = pdf.PageAddText(1, "Hello World!")
        if err != nil {
                log.Fatal(err)
        }
        // Save PDF-document with "hello.pdf" name
        err = pdf.SaveAs("hello.pdf")
        if err != nil {
                log.Fatal(err)
        }
        // Release allocated resources
        defer pdf.Close()
    }
```
