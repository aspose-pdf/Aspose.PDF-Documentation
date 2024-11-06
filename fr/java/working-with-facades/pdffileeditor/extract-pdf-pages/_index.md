---
title: Extraire des pages PDF
type: docs
weight: 20
url: fr/java/extract-pdf-pages/
description: Cette section explique comment extraire des pages PDF avec com.aspose.pdf.facades en utilisant la classe PdfFileEditor.
lastmod: "2021-06-05"
draft: false
---

## Extraire des pages PDF entre deux numéros en utilisant des chemins de fichiers

La méthode [Extract](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileEditor#extract-java.io.InputStream-int:A-java.io.OutputStream-) de la classe [PdfFileEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileEditor) vous permet d'extraire une plage de pages spécifiée d'un fichier PDF. Cette surcharge vous permet d'extraire des pages tout en manipulant les fichiers PDF depuis le disque. Cette surcharge nécessite les paramètres suivants : chemin du fichier d'entrée, page de début, page de fin et chemin du fichier de sortie. Les pages de la page de début à la page de fin seront extraites et la sortie sera enregistrée sur le disque. Le code suivant montre comment extraire des pages PDF entre deux numéros en utilisant des chemins de fichiers.

```java
  public static void Extract_PDFPages_FilePaths() {
        // Créer un objet PdfFileEditor
        PdfFileEditor pdfEditor = new PdfFileEditor();

        // Extraire les pages
        pdfEditor.Extract(_dataDir + "MultiplePages.pdf", 1, 3, _dataDir + "ExtractPagesBetweenNumbers_out.pdf");
    }
```


## Extraire un Tableau de Pages PDF en Utilisant les Chemins de Fichier

Si vous ne souhaitez pas extraire une plage de pages, mais plutôt un ensemble de pages particulières, la méthode [Extract](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileEditor#extract-java.io.InputStream-int:A-java.io.OutputStream-) vous permet également de le faire. Vous devez d'abord créer un tableau d'entiers avec tous les numéros de pages à extraire. Cette surcharge de la méthode [Extract](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileEditor#extract-java.io.InputStream-int:A-java.io.OutputStream-) prend les paramètres suivants : fichier PDF d'entrée, tableau d'entiers des pages à extraire, et fichier PDF de sortie. Le code suivant vous montre comment extraire des pages PDF en utilisant les chemins de fichier.

```java
 public static void Extract_ArrayPDFPages_FilePaths() {
        // Créer un objet PdfFileEditor
        PdfFileEditor pdfEditor = new PdfFileEditor();
        int[] pagesToExtract = new int[] { 1, 2 };
        // Extraire les pages
        pdfEditor.Extract(_dataDir + "Extract.pdf", pagesToExtract, _dataDir + "ExtractArrayOfPages_out.pdf");
    }
```


## Extraire des Pages PDF entre Deux Nombres en Utilisant des Flux

La méthode [Extract](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileEditor#extract-java.io.InputStream-int:A-java.io.OutputStream-) de la classe [PdfFileEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileEditor) vous permet d'extraire une plage de pages en utilisant des flux. Vous devez passer les paramètres suivants à cette surcharge : flux d'entrée, page de début, page de fin et flux de sortie. Les pages spécifiées par la plage entre la page de début et la page de fin seront extraites du flux d'entrée et enregistrées dans le flux de sortie. Le code suivant vous montre comment extraire des pages PDF entre deux nombres en utilisant des flux.

```java
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


## Extraire un tableau de pages PDF en utilisant des flux

Un tableau de pages peut être extrait du flux PDF et enregistré dans le flux de sortie en utilisant une surcharge appropriée de la méthode [Extract](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileEditor#extract-java.io.InputStream-int:A-java.io.OutputStream-). Si vous ne souhaitez pas extraire une plage de pages, mais plutôt un ensemble de pages particulières, la méthode [Extract](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileEditor#extract-java.io.InputStream-int:A-java.io.OutputStream-) vous permet également de le faire. Vous devez d'abord créer un tableau d'entiers avec tous les numéros de pages qui doivent être extraites. Cette surcharge de la méthode [Extract](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileEditor#extract-java.io.InputStream-int:A-java.io.OutputStream-) prend les paramètres suivants : flux d'entrée, tableau d'entiers des pages à extraire et flux de sortie. Le code suivant montre comment extraire des pages PDF en utilisant des flux.

```java
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