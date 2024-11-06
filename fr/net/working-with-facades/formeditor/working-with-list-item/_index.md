---
title: Travailler avec l'élément de liste
type: docs
weight: 30
url: fr/net/working-with-list-item/
description: Cette section explique comment travailler avec l'élément de liste avec Aspose.PDF Facades en utilisant la classe FormEditor.
lastmod: "2021-06-05"
draft: false
---

## Ajouter un élément de liste dans un fichier PDF existant

La méthode [AddListItem](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/addlistitem) vous permet d'ajouter un élément dans un champ [ListBox](https://reference.aspose.com/pdf/net/aspose.pdf.forms/listboxfield). Le premier argument est le nom du champ et le deuxième argument est l'élément du champ. Vous pouvez soit passer un seul élément de champ, soit passer un tableau de chaînes contenant une liste d'éléments. Cette méthode est fournie par la classe [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor). Le fragment de code suivant vous montre comment ajouter des éléments de liste dans un fichier PDF.

```csharp
  public static void AddListItem()
        {
            var editor = new FormEditor();
            editor.BindPdf(_dataDir + "Sample-Form-01.pdf");
            editor.AddField(FieldType.ListBox, "Country", 1, 232.56f, 476.75f, 352.28f, 514.03f);
            editor.AddListItem("Country", "USA");
            editor.AddListItem("Country", "Canada");
            editor.AddListItem("Country", "France");
            editor.AddListItem("Country", "Spain");
            editor.Save(_dataDir + "Sample-Form-01-mod.pdf");
        }
```

## Supprimer un élément de liste d'un fichier PDF existant

La méthode [DelListItem](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/dellistitem) vous permet de supprimer un élément particulier de la [ListBox](https://reference.aspose.com/pdf/net/aspose.pdf.forms/listboxfield). Le premier paramètre est le nom du champ tandis que le deuxième paramètre est l'élément que vous souhaitez supprimer de la liste. Cette méthode est fournie par la classe [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor). Le code suivant vous montre comment supprimer un élément de liste du fichier PDF.

```csharp
      public static void DelListItem()
        {
            var editor = new FormEditor();
            editor.BindPdf(_dataDir + "Sample-Form-04.pdf");
            //-----
            editor.DelListItem("Country", "France");
            //-----
            editor.Save(_dataDir + "Sample-Form-04-mod.pdf");
        }
```