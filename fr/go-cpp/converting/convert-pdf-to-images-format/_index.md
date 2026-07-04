---
title: Convertir le PDF en formats d'image avec Go
linktitle: Convertir le PDF en images
type: docs
weight: 70
url: /fr/go-cpp/convert-pdf-to-images-format/
lastmod: "2026-07-04"
description: Ce sujet vous montre comment utiliser Aspose.PDF for Go pour convertir des PDF en divers formats d'images, par ex. TIFF, BMP, JPEG, PNG, SVG, en quelques lignes de code.
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: Outil de conversion de PDF en formats d'images avec Aspose.PDF for Go
Abstract: Aspose.PDF for Go via C++ permet une conversion transparente de documents PDF vers divers formats d'image, notamment JPEG, PNG, BMP et TIFF. Cette fonctionnalité permet aux développeurs de rendre des images de haute qualité tout en préservant le contenu, la mise en page et la résolution du document original. La bibliothèque offre des options flexibles pour les paramètres de sortie tels que la résolution, la qualité d'image et la profondeur de couleur. La documentation propose des instructions étape par étape ainsi que des extraits de code pour aider les développeurs à intégrer efficacement la conversion PDF vers image dans leurs applications.
SoftwareApplication: go-cpp
---

## Go Convertir PDF en Image

Dans cet article, nous vous montrerons les options de conversion de PDF en formats d'image.

Les documents numérisés précédemment sont souvent enregistrés au format PDF. Cependant, avez‑vous besoin de les modifier dans un éditeur graphique ou de les transmettre ultérieurement au format image ? Nous disposons d’un outil universel pour convertir les PDF en images en utilisant **Aspose.PDF for Go via C++**.
La tâche la plus courante est lorsque vous devez enregistrer un document PDF complet ou certaines pages spécifiques d'un document sous forme d'ensemble d'images. **Aspose.PDF for Go via C++** vous permet de convertir le PDF en formats JPG et PNG afin de simplifier les étapes nécessaires pour obtenir vos images à partir d'un fichier PDF spécifique.

**Aspose.PDF for Go via C++** prend en charge la conversion de divers formats PDF en images. Veuillez vérifier la section. [Formats de fichier pris en charge par Aspose.PDF](https://docs.aspose.com/pdf/go-cpp/supported-file-formats/).

## Convertir le PDF en JPEG

L'extrait de code Go fourni montre comment convertir la première page d'un document PDF en image JPEG à l'aide de la bibliothèque Aspose.PDF :

1. Ouvrez un document PDF.
1. Convertir une page en JPEG en utilisant [PageEnJpg](https://reference.aspose.com/pdf/go-cpp/convert/pagetojpg/) fonction.
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
      // PageToJpg(num int32, resolution_dpi int32, filename string) saves the specified page as Jpg-image file
      err = pdf.PageToJpg(1, 100, "sample_page1.jpg")
      if err != nil {
        log.Fatal(err)
      }
      // Close() releases allocated resources for PDF-document
      defer pdf.Close()
    }
```

{{% alert color="success" %}}
**Essayez de convertir le PDF en JPEG en ligne**

Aspose.PDF for Go vous présente une application en ligne gratuite ["PDF en JPEG"](https://products.aspose.app/pdf/conversion/pdf-to-jpg), où vous pouvez essayer d'enquêter sur la fonctionnalité et la qualité de son fonctionnement.

[![Conversion Aspose.PDF PDF en JPEG avec application gratuite](pdf_to_jpg.png)](https://products.aspose.app/pdf/conversion/pdf-to-jpg)
{{% /alert %}}

## Convertir le PDF en TIFF

L'extrait de code Go fourni montre comment convertir la première page d'un document PDF en image TIFF en utilisant la bibliothèque Aspose.PDF :

1. Ouvrez un document PDF.
1. Convertir une page en TIFF en utilisant [PageToTiff](https://reference.aspose.com/pdf/go-cpp/convert/pagetotiff/) fonction.
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
      // PageToTiff(num int32, resolution_dpi int32, filename string) saves the specified page as Tiff-image file
      err = pdf.PageToTiff(1, 100, "sample_page1.tiff")
      if err != nil {
        log.Fatal(err)
      }
      // Close() releases allocated resources for PDF-document
      defer pdf.Close()
    }
```

{{% alert color="success" %}}
**Essayez de convertir le PDF en TIFF en ligne**

Aspose.PDF for Go vous présente une application en ligne gratuite ["PDF en TIFF"](https://products.aspose.app/pdf/conversion/pdf-to-tiff), où vous pouvez essayer d'enquêter sur la fonctionnalité et la qualité de son fonctionnement.

[![Aspose.PDF conversion PDF vers TIFF avec application gratuite](pdf_to_tiff.png)](https://products.aspose.app/pdf/conversion/pdf-to-tiff)
{{% /alert %}}

## Convertir le PDF en PNG

L'extrait de code Go fourni montre comment convertir la première page d'un document PDF en image PNG en utilisant la bibliothèque Aspose.PDF :

1. Ouvrez un document PDF.
1. Convertir une page en PNG en utilisant [PageEnPng](https://reference.aspose.com/pdf/go-cpp/convert/pagetopng/) fonction.
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
      // PageToPng(num int32, resolution_dpi int32, filename string) saves the specified page as Png-image file
      err = pdf.PageToPng(1, 100, "sample_page1.png")
      if err != nil {
        log.Fatal(err)
      }
      // Close() releases allocated resources for PDF-document
      defer pdf.Close()
    }
```

{{% alert color="success" %}}
**Essayez de convertir le PDF en PNG en ligne**

À titre d'exemple de la façon dont nos applications gratuites fonctionnent, veuillez consulter la fonctionnalité suivante.

Aspose.PDF for Go vous présente une application en ligne gratuite ["PDF en PNG"](https://products.aspose.app/pdf/conversion/pdf-to-png), où vous pouvez essayer d'enquêter sur la fonctionnalité et la qualité de son fonctionnement.

[![Comment convertir un PDF en PNG à l'aide d'une application gratuite](pdf_to_png.png)](https://products.aspose.app/pdf/conversion/pdf-to-png)
{{% /alert %}}

**Scalable Vector Graphics (SVG)** est une famille de spécifications d’un format de fichier basé sur XML pour les graphiques vectoriels bidimensionnels, à la fois statiques et dynamiques (interactifs ou animés). La spécification SVG est une norme ouverte qui est développée par le World Wide Web Consortium (W3C) depuis 1999.

## Convertir PDF en SVG

L'extrait de code Go fourni montre comment convertir la première page d'un document PDF en image SVG en utilisant la bibliothèque Aspose.PDF :

1. Ouvrez un document PDF.
1. Convertir une page en SVG en utilisant [PageToSvg](https://reference.aspose.com/pdf/go-cpp/convert/pagetosvg/) fonction.
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
      // PageToSvg(num int32, filename string) saves the specified page as Svg-image file
      err = pdf.PageToSvg(1, "sample_page1.svg")
      if err != nil {
        log.Fatal(err)
      }
      // Close() releases allocated resources for PDF-document
      defer pdf.Close()
    }
```

{{% alert color="success" %}}
**Essayez de convertir le PDF en SVG en ligne**

Aspose.PDF for Go vous présente une application en ligne gratuite ["PDF vers SVG"](https://products.aspose.app/pdf/conversion/pdf-to-svg), où vous pouvez essayer d'enquêter sur la fonctionnalité et la qualité de son fonctionnement.

[![Aspose.PDF Conversion PDF en SVG avec une application gratuite](pdf_to_svg.png)](https://products.aspose.app/pdf/conversion/pdf-to-svg)
{{% /alert %}}

## Convertir le PDF en DICOM

L'extrait de code Go fourni montre comment convertir la première page d'un document PDF en image DICOM en utilisant la bibliothèque Aspose.PDF :

1. Ouvrez un document PDF.
1. Convertir une page en DICOM en utilisant [PageToDICOM](https://reference.aspose.com/pdf/go-cpp/convert/pagetodicom/) fonction.
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
      // PageToDICOM(num int32, resolution_dpi int32, filename string) saves the specified page as DICOM-image file
      err = pdf.PageToDICOM(1, 100, "sample_page1.dcm")
      if err != nil {
        log.Fatal(err)
      }
      // Close() releases allocated resources for PDF-document
      defer pdf.Close()
    }
```

## Convertir le PDF en BMP

L'extrait de code Go fourni montre comment convertir la première page d'un document PDF en image BMP en utilisant la bibliothèque Aspose.PDF :

1. Ouvrez un document PDF.
1. Convertir une page en BMP à l'aide de [PageToBmp](https://reference.aspose.com/pdf/go-cpp/convert/pagetobmp/) fonction.
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
      // PageToBmp(num int32, resolution_dpi int32, filename string) saves the specified page as Bmp-image file
      err = pdf.PageToBmp(1, 100, "sample_page1.bmp")
      if err != nil {
        log.Fatal(err)
      }
      // Close() releases allocated resources for PDF-document
      defer pdf.Close()
    }
```