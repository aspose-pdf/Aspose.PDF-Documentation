---
title: Obtenir et définir les propriétés de page
linktitle: Obtenir et définir les propriétés de page
type: docs
url: /fr/go-cpp/get-and-set-page-properties/
description: Apprenez comment obtenir et définir les propriétés de page pour les documents PDF à l'aide d'Aspose.PDF for Go, permettant une mise en forme personnalisée du document.
lastmod: "2026-07-04"
TechArticle: true
AlternativeHeadline: Obtenir et définir les propriétés de page avec Aspose.PDF for Go
Abstract: Aspose.PDF for Go via C++ fournit des fonctionnalités complètes pour obtenir et définir les propriétés de page dans les documents PDF, permettant aux développeurs d'accéder et de modifier divers attributs de page tels que la taille, la rotation, les marges et les métadonnées. Ces capacités permettent un contrôle précis de la mise en page et de l'apparence du document afin de répondre aux exigences spécifiques de l'application. La bibliothèque garantit une personnalisation et une optimisation transparentes des pages PDF. La documentation offre des instructions détaillées et des exemples de code pour aider les développeurs à récupérer et mettre à jour efficacement les propriétés de page dans leurs applications.
SoftwareApplication: go-cpp
---


Aspose.PDF for Go vous permet de lire et de définir les propriétés des pages d'un fichier PDF. Cette section montre comment obtenir le nombre de pages d'un fichier PDF, récupérer des informations sur les propriétés des pages PDF telles que la couleur et définir les propriétés de page.

## Obtenir le nombre de pages dans un fichier PDF

Lorsque vous travaillez avec des documents, vous souhaitez souvent savoir combien de pages ils contiennent. Avec Aspose.PDF, cela ne nécessite pas plus de deux lignes de code.

**Aspose.PDF for Go via C\u002B\u002B** vous permet de compter les Pages avec [PageCount](https://reference.aspose.com/pdf/go-cpp/core/pagecount/) fonction.

Le fragment de code suivant est conçu pour ouvrir un document PDF, récupérer le nombre de ses pages, puis afficher le résultat.

Le [PageCount](https://reference.aspose.com/pdf/go-cpp/core/pagecount/) la méthode est appelée pour obtenir le nombre total de pages du document PDF. Ceci est utile pour les tâches qui doivent connaître la longueur du document, comme lors de l'extraction de pages spécifiques ou de l'exécution d'opérations sur toutes les pages. Cette méthode est un moyen simple d'interroger la structure du document.

Pour obtenir le nombre de pages dans un fichier PDF :

```go

    package main

    import "github.com/aspose-pdf/aspose-pdf-go-cpp"
    import "log"
    import "fmt"

    func main() {
      // Open(filename string) opens a PDF-document with filename
      pdf, err := asposepdf.Open("sample.pdf")
      if err != nil {
        log.Fatal(err)

      }
      // PageCount() returns page count in PDF-document
      count, err := pdf.PageCount()
      if err != nil {
        log.Fatal(err)
      }
      // Print
      fmt.Println("Count:", count)
      // Close() releases allocated resources for PDF-document
      defer pdf.Close()
    }
```

## Définir la taille de la page

Dans cet exemple, la méthode pdf.PageSetSize() modifie la taille de la première page du document PDF. La constante PageSizeA1 garantit que la première page est définie au format de papier A1. Ceci est utile lors de la conversion de documents vers un format standardisé ou pour s'assurer que le contenu spécifique s'adapte correctement aux pages.

1. Ouverture du document PDF avec [Ouvrir](https://reference.aspose.com/pdf/go-cpp/core/open/) méthode.
1. Définir la taille de la page avec [PageSetSize](https://reference.aspose.com/pdf/go-cpp/organize/pagesetsize/) fonction.
1. Enregistrement du document avec [SaveAs](https://reference.aspose.com/pdf/go-cpp/core/saveas/) méthode.

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
        // PageSetSize(num int32, pageSize int32) sets size of page
        err = pdf.PageSetSize(1, asposepdf.PageSizeA1)
        if err != nil {
            log.Fatal(err)
        }
        // SaveAs(filename string) saves previously opened PDF-document with new filename
        err = pdf.SaveAs("sample_page1_SetSize_A1.pdf")
        if err != nil {
            log.Fatal(err)
        }
        // Close() releases allocated resources for PDF-document
        defer pdf.Close()
    }
```