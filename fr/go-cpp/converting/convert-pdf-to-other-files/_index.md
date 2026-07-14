---
title: Convertir le PDF en EPUB, TeX, texte, XPS en Go
linktitle: Convertir le PDF en d'autres formats
type: docs
weight: 90
url: /fr/go-cpp/convert-pdf-to-other-files/
lastmod: "2026-07-04"
description: Ce sujet vous montre comment convertir un fichier PDF en d'autres formats tels que EPUB, LaTeX, Texte, XPS, etc. en utilisant Go.
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: Outil Golang pour convertir PDF en EPUB, TeX, Texte et XPS
Abstract: Aspose.PDF for Go via C++ offre des capacités puissantes pour convertir des documents PDF en divers formats de fichiers, y compris DOCX, PPTX, HTML, EPUB, SVG, et plus encore. Cette fonctionnalité permet aux développeurs d'extraire et de réutiliser le contenu PDF de manière transparente tout en préservant la mise en forme, la structure et la qualité à travers différents formats de sortie. La bibliothèque fournit des options flexibles pour personnaliser le processus de conversion selon des exigences spécifiques. La documentation comprend des directives complètes et des exemples de code pour aider les développeurs à mettre en œuvre efficacement la conversion PDF-vers-fichier au sein de leurs applications.
SoftwareApplication: go-cpp
---

## Convertir le PDF en EPUB

**<abbr title="Electronic Publication">EPUB</abbr>** est une norme libre et ouverte d'e-book du International Digital Publishing Forum (IDPF). Les fichiers portent l'extension .epub.
EPUB est conçu pour du contenu reflowable, signifiant qu'un lecteur EPUB peut optimiser le texte pour un appareil d'affichage particulier. EPUB prend également en charge le contenu à mise en page fixe. Le format est destiné à être un format unique que les éditeurs et les maisons de conversion peuvent utiliser en interne, ainsi que pour la distribution et la vente. Il remplace la norme Open eBook.

L'extrait de code Go fourni montre comment convertir un document PDF en EPUB à l'aide de la bibliothèque Aspose.PDF :

1. Ouvrez un document PDF.
1. Convertir un fichier PDF en EPUB en utilisant [EnregistrerEpub]() fonction.
1. Fermez le document PDF et libérez toutes les ressources allouées.

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
      // SaveEpub(filename string) saves previously opened PDF-document as Epub-document with filename
      err = pdf.SaveEpub("sample.epub")
      if err != nil {
        log.Fatal(err)
      }
      // Close() releases allocated resources for PDF-document
      defer pdf.Close()
    }
```

{{% alert color="success" %}}
**Essayez de convertir le PDF en EPUB en ligne**

Aspose.PDF for Go vous présente une application gratuite en ligne ["PDF en EPUB"](https://products.aspose.app/pdf/conversion/pdf-to-epub), où vous pouvez essayer d'examiner la fonctionnalité et la qualité de son fonctionnement.

[![Aspose.PDF Conversion PDF en EPUB avec une application gratuite](pdf_to_epub.png)](https://products.aspose.app/pdf/conversion/pdf-to-epub)
{{% /alert %}}

## Convertir le PDF en TeX

**Aspose.PDF for Go** prend en charge la conversion de PDF en TeX.
Le format de fichier LaTeX est un format de fichier texte avec une balise spéciale et est utilisé dans le système de préparation de documents basé sur TeX pour une composition de haute qualité.

L'extrait de code Go fourni démontre comment convertir un document PDF en TeX à l'aide de la bibliothèque Aspose.PDF :

1. Ouvrez un document PDF.
1. Convertir un fichier PDF en TeX en utilisant [SaveTeX](https://reference.aspose.com/pdf/go-cpp/convert/savetex/) fonction.
1. Fermez le document PDF et libérez toutes les ressources allouées.

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
      // SaveTeX(filename string) saves previously opened PDF-document as TeX-document with filename
      err = pdf.SaveTeX("sample.tex")
      if err != nil {
        log.Fatal(err)
      }
      // Close() releases allocated resources for PDF-document
      defer pdf.Close()
    }
```

{{% alert color="success" %}}
**Essayez de convertir PDF en LaTeX/TeX en ligne**

Aspose.PDF for Go vous présente une application gratuite en ligne ["PDF en LaTeX"](https://products.aspose.app/pdf/conversion/pdf-to-tex), où vous pouvez essayer d'examiner la fonctionnalité et la qualité de son fonctionnement.

[![Aspose.PDF Conversion PDF en LaTeX/TeX avec une application gratuite](pdf_to_latex.png)](https://products.aspose.app/pdf/conversion/pdf-to-tex)
{{% /alert %}}

## Convertir le PDF en TXT

L'extrait de code Go fourni montre comment convertir un document PDF en TXT à l'aide de la bibliothèque Aspose.PDF :

1. Ouvrez un document PDF.
1. Convertir un fichier PDF en TXT en utilisant [SaveTxt](https://reference.aspose.com/pdf/go-cpp/convert/savetxt/) fonction.
1. Fermez le document PDF et libérez toutes les ressources allouées.

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
      // SaveTxt(filename string) saves previously opened PDF-document as Txt-document with filename
      err = pdf.SaveTxt("sample.txt")
      if err != nil {
        log.Fatal(err)
      }
      // Close() releases allocated resources for PDF-document
      defer pdf.Close()
    }
```

{{% alert color="success" %}}
**Essayez de convertir Convert PDF en texte en ligne**

Aspose.PDF for Go vous présente une application gratuite en ligne ["PDF en texte"](https://products.aspose.app/pdf/conversion/pdf-to-txt), où vous pouvez essayer d'examiner la fonctionnalité et la qualité de son fonctionnement.

[![Conversion Aspose.PDF PDF en texte avec une application gratuite](pdf_to_text.png)](https://products.aspose.app/pdf/conversion/pdf-to-txt)
{{% /alert %}}

## Convertir PDF en XPS

Le type de fichier XPS est principalement associé à la XML Paper Specification de Microsoft Corporation. La XML Paper Specification (XPS), anciennement nom de code Metro et englobant le concept marketing Next Generation Print Path (NGPP), est l'initiative de Microsoft visant à intégrer la création et la visualisation de documents dans le système d'exploitation Windows.

**Aspose.PDF for Go** donne la possibilité de convertir des fichiers PDF en <abbr title="XML Paper Specification">XPS</abbr> format. Essayons d'utiliser le fragment de code présenté pour convertir des fichiers PDF au format XPS avec Go.

L'extrait de code Go fourni montre comment convertir un document PDF en XPS à l'aide de la bibliothèque Aspose.PDF:

1. Ouvrez un document PDF.
1. Convertir un fichier PDF en XPS en utilisant [SaveXps](https://reference.aspose.com/pdf/go-cpp/convert/savexps/) fonction.
1. Fermez le document PDF et libérez toutes les ressources allouées.

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
      // SaveXps(filename string) saves previously opened PDF-document as Xps-document with filename
      err = pdf.SaveXps("sample.xps")
      if err != nil {
        log.Fatal(err)
      }
      // Close() releases allocated resources for PDF-document
      defer pdf.Close()
    }
```

{{% alert color="success" %}}
**Essayez de convertir le PDF en XPS en ligne**

Aspose.PDF for Go vous présente une application gratuite en ligne [PDF vers XPS](https://products.aspose.app/pdf/conversion/pdf-to-xps), où vous pouvez essayer d'examiner la fonctionnalité et la qualité de son fonctionnement.

[![Aspose.PDF Conversion PDF en XPS avec l'application gratuite](pdf_to_xps.png)](https://products.aspose.app/pdf/conversion/pdf-to-xps)
{{% /alert %}}

## Convertir le PDF en PDF en niveaux de gris

L'extrait de code Go fourni montre comment convertir la première page d'un document PDF en PDF en niveaux de gris en utilisant la bibliothèque Aspose.PDF :

1. Ouvrez un document PDF.
1. Convertir une page PDF en PDF en niveaux de gris en utilisant [PageGrayscale](https://reference.aspose.com/pdf/go-cpp/organize/pagegrayscale/) fonction.
1. Fermez le document PDF et libérez toutes les ressources allouées.

Cet exemple convertit une page spécifique de votre PDF en niveaux de gris :

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
      // PageGrayscale(num int32) converts page to black and white
      err = pdf.PageGrayscale(1)
      if err != nil {
        log.Fatal(err)
      }
      // SaveAs(filename string) saves previously opened PDF-document with new filename
      err = pdf.SaveAs("sample_page1_Grayscale.pdf")
      if err != nil {
        log.Fatal(err)
      }
      // Close() releases allocated resources for PDF-document
      defer pdf.Close()
    }
```

Cet exemple convertira l'ensemble du document PDF en niveaux de gris :

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
      // Grayscale() converts PDF-document to black and white
      err = pdf.Grayscale()
      if err != nil {
        log.Fatal(err)
      }
      // SaveAs(filename string) saves previously opened PDF-document with new filename
      err = pdf.SaveAs("sample_Grayscale.pdf")
      if err != nil {
        log.Fatal(err)
      }
      // Close() releases allocated resources for PDF-document
      defer pdf.Close()
    }
```