---
title: Travailler avec des Images
type: docs
weight: 30
url: /fr/java/working-with-image/
description: Cette section explique comment remplacer une image avec Aspose.PDF Facades - un ensemble d'outils pour les opérations populaires avec PDF.
lastmod: "2021-06-25"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Supprimer des Images d'une Page Particulière de PDF (Facades)

[PdfContentEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor) la classe vous permet de remplacer une image dans un fichier PDF existant.
 Le [replaceImage](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor#replaceImage-int-int-java.lang.String-) méthode vous aide à atteindre cet objectif. Vous devez créer un objet de la classe [PdfContentEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor) et lier le fichier PDF d'entrée à l'aide de la méthode bindPdf. Après cela, vous devez appeler la méthode [replaceImage](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor#replaceImage-int-int-java.lang.String-) avec trois paramètres : un numéro de page, l'index de l'image à remplacer, et le chemin de l'image à remplacer.

Le code suivant vous montre comment remplacer une image dans un fichier PDF existant.

```java
public class PdfContentEditorImages {

    private static String _dataDir = "/home/aspose/pdf-examples/Samples/facades/PdfContentEditor/";

    public static void DeleteImage()
    {
        PdfContentEditor editor = new PdfContentEditor(new Document(_dataDir + "sample.pdf"));
        editor.deleteImage(2, new int [] { 1,3 });
        editor.save(_dataDir + "PdfContentEditorDemo10.pdf");
    }
```

## Supprimer toutes les images d'un fichier PDF (Facades)

Toutes les images peuvent être supprimées d'un fichier PDF en utilisant la méthode [deleteImage](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor#deleteImage--) de [PdfContentEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor). Appelez la méthode [deleteImage](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor#deleteImage--) – la surcharge sans aucun paramètre – pour supprimer toutes les images, puis enregistrez le fichier PDF mis à jour en utilisant la méthode Save.

```java
   public static void DeleteImages()
    {
        PdfContentEditor editor = new PdfContentEditor(new Document(_dataDir + "sample.pdf"));
        editor.deleteImage();
        editor.save(_dataDir + "PdfContentEditorDemo11.pdf");
    }
```

## Remplacer les images dans un fichier PDF (Facades)

Vous pouvez remplacer les images dans un fichier PDF en utilisant la méthode [replaceImage](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor#replaceImage-int-int-java.lang.String-) de [PdfContentEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor).

```java
   public static void ReplaceImage()
    {
        // Remplace une image dans le document PDF
        PdfContentEditor editor = new PdfContentEditor(new Document(_dataDir + "sample_cats_dogs.pdf"));
        editor.replaceImage(2, 4, _dataDir+"cat04.jpg");
        editor.save(_dataDir + "PdfContentEditorDemo12.pdf");
    }
```