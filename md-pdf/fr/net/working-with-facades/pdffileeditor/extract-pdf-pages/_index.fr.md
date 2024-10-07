---
title: Extraire des pages PDF
type: docs
weight: 40
url: /net/extract-pdf-pages/
description: Cette section explique comment extraire des pages PDF avec Aspose.PDF Facades en utilisant la classe PdfFileEditor.
lastmod: "2021-06-05"
draft: false
---

## Extraire des pages PDF entre deux numéros en utilisant les chemins de fichiers

La méthode [Extract](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/extract/index) de la classe [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) vous permet d'extraire une plage spécifique de pages d'un fichier PDF. Cette surcharge vous permet d'extraire des pages tout en manipulant les fichiers PDF à partir du disque. Cette surcharge nécessite les paramètres suivants : chemin du fichier d'entrée, page de début, page de fin et chemin du fichier de sortie. Les pages de la page de début à la page de fin seront extraites et le résultat sera enregistré sur le disque. Le code suivant vous montre comment extraire des pages PDF entre deux numéros en utilisant les chemins de fichiers.

```csharp
public static void Extract_PDFPages_FilePaths()
{
    // Créer un objet PdfFileEditor
    PdfFileEditor pdfEditor = new PdfFileEditor();

    // Extraire les pages
    pdfEditor.Extract(_dataDir + "MultiplePages.pdf", 1, 3, _dataDir + "ExtractPagesBetweenNumbers_out.pdf");
}
```

## Extraire un tableau de pages PDF en utilisant des chemins de fichiers

Si vous ne souhaitez pas extraire une plage de pages, mais plutôt un ensemble de pages particulières, la méthode [Extract](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/extract/index) vous permet de le faire également. Vous devez d'abord créer un tableau d'entiers avec tous les numéros de pages à extraire. Cette surcharge de la méthode [Extract](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/extract/index) prend les paramètres suivants : fichier PDF d'entrée, tableau d'entiers des pages à extraire et fichier PDF de sortie. L'extrait de code suivant vous montre comment extraire des pages PDF en utilisant des chemins de fichiers.

```csharp
public static void Extract_PDFPages_Streams()
{
    // Créer un objet PdfFileEditor
    PdfFileEditor pdfEditor = new PdfFileEditor();
    // Créer des flux
    using (FileStream inputStream = new FileStream(_dataDir + "MultiplePages.pdf", FileMode.Open))
    using (FileStream outputStream = new FileStream(_dataDir + "ExtractPagesBetweenTwoNumbers_out.pdf", FileMode.Create))
        // Extraire les pages
        pdfEditor.Extract(inputStream, 1, 3, outputStream);
}
```

## Extraire des Pages PDF entre Deux Nombres en Utilisant des Flux

La méthode [Extract](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/extract/index) de la classe [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) vous permet d'extraire une plage de pages en utilisant des flux. Vous devez passer les paramètres suivants à cette surcharge : flux d'entrée, page de début, page de fin et flux de sortie. Les pages spécifiées par la plage entre la page de début et la page de fin seront extraites du flux d'entrée et sauvegardées dans le flux de sortie. Le code suivant vous montre comment extraire des pages PDF entre deux nombres en utilisant des flux.

```csharp
public static void Extract_ArrayPDFPages_FilePaths()
{
    // Créer un objet PdfFileEditor
    PdfFileEditor pdfEditor = new PdfFileEditor();
    int[] pagesToExtract = new int[] { 1, 2 };
    // Extraire les pages
    pdfEditor.Extract(_dataDir + "Extract.pdf", pagesToExtract, _dataDir + "ExtractArrayOfPages_out.pdf");
}
```

## Extraire un Tableau de Pages PDF en Utilisant des Flux

Un tableau de pages peut être extrait du flux PDF et sauvegardé dans le flux de sortie en utilisant la surcharge appropriée de la méthode [Extract](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/extract/index). Si vous ne souhaitez pas extraire une plage de pages, mais plutôt un ensemble de pages particulières, la méthode [Extract](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/extract/index) vous permet également de le faire. Vous devez d'abord créer un tableau d'entiers avec tous les numéros de pages qui doivent être extraits. Cette surcharge de la méthode [Extract](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/extract/index) prend les paramètres suivants : flux d'entrée, tableau d'entiers des pages à extraire et flux de sortie. Le code suivant vous montre comment extraire des pages PDF en utilisant des flux.

```csharp
public static void Extract_ArrayPDFPages_Streams()
{
    // Créer un objet PdfFileEditor
    PdfFileEditor pdfEditor = new PdfFileEditor();
    // Créer des flux
    using (FileStream inputStream = new FileStream(_dataDir + "MultiplePages.pdf", FileMode.Open))
    using (FileStream outputStream = new FileStream(_dataDir + "ExtractArrayOfPagesUsingStreams_out.pdf", FileMode.Create))
    {
        int[] pagesToExtract = new int[] { 1, 2 };
        // Extraire les pages
        pdfEditor.Extract(inputStream, pagesToExtract, outputStream);
    }
}
```