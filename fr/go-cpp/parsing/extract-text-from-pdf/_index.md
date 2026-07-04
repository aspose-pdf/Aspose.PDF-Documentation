---
title: Extraire du texte d'un PDF avec Go
linktitle: Extraire du texte du PDF
type: docs
weight: 30
url: /fr/go-cpp/extract-text-from-pdf/
description: Cet article décrit différentes manières d'extraire du texte des documents PDF à l'aide d'Aspose.PDF for Go.
lastmod: "2026-07-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Extraire du texte avec Aspose.PDF for Go
Abstract: Aspose.PDF for Go via C\u002B\u002B offre un moyen puissant et efficace d'extraire du texte des documents PDF. La bibliothèque prend en charge plusieurs techniques d'extraction, permettant aux utilisateurs de récupérer du texte de documents entiers, de pages spécifiques ou de zones prédéfinies au sein d'un PDF.
SoftwareApplication: go-cpp
---

## Extraire du texte du document PDF

Extraire du texte du document PDF est une tâche très courante et utile. Les PDF contiennent souvent des informations essentielles qui doivent être consultées, analysées ou traitées à diverses fins. Extraire du texte permet de réutiliser plus facilement ces données dans des bases de données, des rapports ou d’autres documents.

L’extraction de texte rend le contenu PDF interrogeable, permettant aux utilisateurs de localiser rapidement des informations spécifiques sans devoir parcourir manuellement l’ensemble du document.

Au cas où vous voudriez extraire du texte d’un document PDF, vous pouvez utiliser [ExtractText](https://reference.aspose.com/pdf/go-cpp/core/extracttext/) fonction.
Veuillez vérifier le fragment de code suivant afin d’extraire du texte d’un fichier PDF en utilisant Go.

1. Ouvrez un document PDF avec le nom de fichier donné.
1. [ExtractText](https://reference.aspose.com/pdf/go-cpp/core/extracttext/) extrait le contenu texte du document PDF.
1. Affichez le texte extrait dans la console.

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
        // ExtractText() returns PDF-document contents as plain text
        txt, err := pdf.ExtractText()
        if err != nil {
            log.Fatal(err)
        }
        // Print
        fmt.Println("Extracted text:\n", txt)
        // Close() releases allocated resources for PDF-document
        defer pdf.Close()
    }
```