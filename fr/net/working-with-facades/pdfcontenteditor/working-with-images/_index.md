---
title: Travailler avec des Images en utilisant PdfContentEditor
type: docs
weight: 50
url: fr/net/working-with-images-in-pdf
description: Cette section explique comment ajouter et supprimer des images avec Aspose.PDF Facades en utilisant la classe PdfContentEditor.
lastmod: "2021-06-24"
---

## Supprimer des Images d'une Page Particulière du PDF (Facades)

Pour supprimer les images d'une page particulière, vous devez appeler la méthode [DeleteImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfcontenteditor/deleteimage/methods/1) avec les paramètres pageNumber et index. Le paramètre index représente un tableau d'entiers - les index des images à supprimer. Tout d'abord, vous devez créer un objet de la classe [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) et ensuite appeler la méthode [DeleteImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfcontenteditor/deleteimage/methods/1). Après cela, vous pouvez enregistrer le fichier PDF mis à jour en utilisant la méthode [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save/index).

Le code suivant vous montre comment supprimer des images d'une page particulière d'un PDF.

```csharp
public static void DeleteImage()
{
    PdfContentEditor editor = new PdfContentEditor(new Document(_dataDir + "sample.pdf"));
    editor.DeleteImage(2, new[] { 2 });
    editor.Save(_dataDir + "PdfContentEditorDemo10.pdf");
}
```

## Supprimer toutes les images d'un fichier PDF (Facades)

Toutes les images peuvent être supprimées d'un fichier PDF en utilisant la méthode [DeleteImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/deleteimage/methods/1) de la classe [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor). Appelez la méthode [DeleteImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfcontenteditor/deleteimage/methods/1) – la surcharge sans aucun paramètre – pour supprimer toutes les images, puis enregistrez le fichier PDF mis à jour en utilisant la méthode [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save/index).

L'extrait de code suivant vous montre comment supprimer toutes les images d'un fichier PDF.

```csharp
public static void DeleteImages()
{
    PdfContentEditor editor = new PdfContentEditor(new Document(_dataDir + "sample.pdf"));
    editor.DeleteImage();
    editor.Save(_dataDir + "PdfContentEditorDemo11.pdf");
}
```

## Remplacer une image dans un fichier PDF (Facades)

le [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) vous permet de remplacer votre image dans un fichier PDF, appelez pour cela la méthode [ReplaceImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/replaceimage), et Enregistrez le résultat.

```csharp
public static void ReplaceImage()
{
    PdfContentEditor editor = new PdfContentEditor(new Document(_dataDir + "sample_cats_dogs.pdf"));
    editor.ReplaceImage(2, 4, @"C:\Samples\Facades\PdfContentEditor\cat04.jpg");
    editor.Save(_dataDir + "PdfContentEditorDemo12.pdf");
}
```