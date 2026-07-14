---
title: Licence Aspose PDF
linktitle: Licence et limitations
type: docs
weight: 90
url: /fr/go-cpp/licensing/
description: Aspose PDF for Go invite ses clients à obtenir une Licence Classic. Il est également possible d’utiliser une licence limitée pour mieux explorer le produit.
lastmod: "2026-07-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Licence d'Aspose.PDF pour Go via C++
Abstract: La page de licence d'Aspose.PDF pour Go via C++ explique les options de licence disponibles pour le produit. Les clients peuvent choisir entre une Licence Classic, une Licence au compteur, ou une licence limitée à des fins d'évaluation. La page met également en avant les avantages d'obtenir une licence appropriée, tels que le déverrouillage de toutes les fonctionnalités et la suppression des limitations d'évaluation.
SoftwareApplication: go-cpp
---


## Limitation d'une version d'évaluation

Nous souhaitons que nos clients testent nos composants de manière approfondie avant d’acheter, c’est pourquoi la version d’évaluation vous permet de l’utiliser comme vous le feriez normalement.

- **Documents créés avec un filigrane d'évaluation.** La version d'évaluation d'Aspose.PDF for Go offre toutes les fonctionnalités du produit, mais toutes les pages des fichiers générés sont filigranées avec le texte "Evaluation Only. Created with Aspose.PDF. Copyright 2002-2025 Aspose Pty Ltd." en haut.

- **Limiter le nombre de pages pouvant être traitées.**
Dans la version d'évaluation, vous ne pouvez traiter que les quatre premières pages d’un document.

>Si vous souhaitez tester Aspose.PDF for Go sans les limitations de la version d'évaluation, vous pouvez également demander une licence temporaire de 30 jours. Veuillez vous référer à [Comment obtenir une licence temporaire ?](https://purchase.aspose.com/temporary-license)

## Licence classique

Appliquer une licence pour activer toutes les fonctionnalités de la bibliothèque Aspose.PDF en utilisant un fichier de licence (Aspose.PDF.GoViaCPP.lic).

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
        // SetLicense(filename string) licenses with filename
        err = pdf.SetLicense("Aspose.PDF.GoViaCPP.lic")
        if err != nil {
            log.Fatal(err)
        }
        // Working with PDF-document
        // ...
        // Close() releases allocated resources for PDF-document
        defer pdf.Close()
    }
```
