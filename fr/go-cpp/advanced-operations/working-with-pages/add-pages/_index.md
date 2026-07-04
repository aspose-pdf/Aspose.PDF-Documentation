---
title: Ajouter des pages au document PDF
linktitle: Ajouter des pages
type: docs
weight: 10
url: /fr/go-cpp/add-pages/
description: Découvrez comment ajouter des pages à un PDF existant en Go avec Aspose.PDF pour améliorer et étendre vos documents.
lastmod: "2026-07-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Ajouter des pages PDF avec Aspose.PDF for Go
Abstract: Aspose.PDF for Go via C++ offre des fonctionnalités puissantes pour ajouter des pages aux documents PDF, permettant aux développeurs de créer de nouvelles pages de manière dynamique et de les personnaliser selon des exigences spécifiques. La bibliothèque prend en charge l’insertion de pages vierges ou la copie de pages à partir de documents existants tout en offrant des options pour définir la taille de la page, l’orientation et le contenu. Ces capacités permettent une expansion et une personnalisation fluides du document. La documentation comprend des instructions détaillées et des exemples de code pour aider les développeurs à implémenter efficacement les fonctionnalités d’ajout de pages dans leurs applications.
SoftwareApplication: go-cpp
---

## Ajouter une page dans un fichier PDF

L'extrait de code Go fourni montre comment exécuter l'opération Add Page à la fin du PDF en utilisant la bibliothèque Aspose.PDF. 

1. Le [Ouvrir](https://reference.aspose.com/pdf/go-cpp/core/open/) La fonction permet au programme de charger un fichier PDF existant (sample.pdf) pour le manipuler. C’est essentiel pour toutes les opérations liées aux PDF, telles que l’édition, l’ajout de contenu ou la lecture de données.
1. Le [PageAdd](https://reference.aspose.com/pdf/go-cpp/core/pageadd/) La méthode est utilisée pour insérer une nouvelle page vierge dans le document PDF existant. Cela est utile pour étendre un document ou le préparer à du contenu supplémentaire.
1. Le [Enregistrer](https://reference.aspose.com/pdf/go-cpp/core/save/) la méthode garantit que les modifications du PDF sont réécrites dans le fichier. Cette étape est cruciale pour la persistance des modifications, comme l'ajout de nouvelles pages.
1. Le [Fermer](https://reference.aspose.com/pdf/go-cpp/core/close/) la méthode est appelée à l'aide de defer pour libérer toutes les ressources allouées pendant les opérations PDF. Cela est important pour prévenir les fuites de mémoire et assurer une utilisation efficace des ressources.

Cet extrait est un exemple concis et efficace montrant comment utiliser la bibliothèque Aspose.PDF Go pour des tâches de manipulation PDF de base.

Aspose.PDF for Go vous permet d'insérer une page dans un document PDF à n'importe quel emplacement du fichier ainsi que d'ajouter des pages à la fin d'un fichier PDF.

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
        // PageAdd() adds new page in PDF-document
        err = pdf.PageAdd()
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

## Insérer une page dans un fichier PDF

Le [PageInsert](https://reference.aspose.com/pdf/go-cpp/core/pageinsert/) Cette méthode insère une nouvelle page à la position spécifiée. Cette fonctionnalité est utile lorsque vous devez insérer des pages supplémentaires dans un document existant, par exemple en ajoutant une nouvelle section ou du contenu à un rapport ou à une présentation.

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
        // PageInsert(num int32) inserts new page at the specified position in PDF-document
        err = pdf.PageInsert(1)
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