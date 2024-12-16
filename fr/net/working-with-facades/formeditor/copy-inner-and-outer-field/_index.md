---
title: Copier le Champ Intérieur et Extérieur
type: docs
weight: 40
url: /fr/net/copy-inner-and-outer-field/
description: Cette section explique comment copier le Champ Intérieur et Extérieur avec Aspose.PDF Facades en utilisant la classe FormEditor.
lastmod: "2021-06-05"
draft: false
---

La méthode [CopyInnerField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/copyinnerfield/index) vous permet de copier un champ dans le même fichier, aux mêmes coordonnées, sur la page spécifiée. Cette méthode nécessite le nom du champ que vous souhaitez copier, le nouveau nom du champ, et le numéro de page sur lequel le champ doit être copié. La classe [FormEditor](https://reference.aspose.com/html/net/aspose.html.forms/formeditor) fournit cette méthode. Le fragment de code suivant vous montre comment copier le champ au même endroit dans le même fichier.

```csharp
  public static void CopyInnerField()
        {
            var editor = new FormEditor();
            var document = new Aspose.Pdf.Document(_dataDir + "Sample-Form-01.pdf");
            document.Pages.Add();
            editor.BindPdf(document);
            editor.CopyInnerField("Last Name", "Last Name 2", 2);
            editor.Save(_dataDir + "Sample-Form-01-mod.pdf");
        }
```

## Copier un champ externe dans un fichier PDF existant

La méthode [CopyOuterField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/copyouterfield/index) vous permet de copier un champ de formulaire à partir d'un fichier PDF externe, puis de l'ajouter au fichier PDF d'entrée à la même position et au numéro de page spécifié. Cette méthode nécessite le fichier PDF à partir duquel le champ doit être copié, le nom du champ et le numéro de page où le champ doit être copié. Cette méthode est fournie par la classe [FormEditor](https://reference.aspose.com/html/net/aspose.html.forms/formeditor). Le code suivant vous montre comment copier un champ depuis un fichier PDF externe.

```csharp
   public static void CopyOuterField()
        {
            var editor = new FormEditor();
            var document = new Aspose.Pdf.Document();
            document.Pages.Add();
            editor.BindPdf(document);
            editor.CopyOuterField(_dataDir + "Sample-Form-01.pdf", "First Name", 1);
            editor.CopyOuterField(_dataDir + "Sample-Form-01.pdf", "Last Name", 1);
            editor.Save(_dataDir + "Sample-Form-02-mod.pdf");
        }
```