---
title: Travailler avec un élément de liste
type: docs
weight: 30
url: /fr/java/working-with-list-item/
description: Cette section explique comment travailler avec un élément de liste avec com.aspose.pdf.facades en utilisant la classe FormEditor.
lastmod: "2021-06-05"
draft: false
---

## Ajouter un élément de liste dans un fichier PDF existant

La méthode [addListItem](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor#addListItem-java.lang.String-java.lang.String-) vous permet d'ajouter un élément dans un champ ListBox. Le premier argument est le nom du champ et le deuxième argument est l'élément du champ. Vous pouvez soit passer un seul élément de champ, soit passer un tableau de chaînes contenant une liste d'éléments. Cette méthode est fournie par la classe [FormEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor). Le snippet de code suivant vous montre comment ajouter des éléments de liste dans un fichier PDF.

```java
public static void AddListItem() {
        FormEditor editor = new FormEditor();
        editor.bindPdf(_dataDir + "Sample-Form-01.pdf");
        editor.addField(FieldType.ListBox, "Country", 1, 232.56f, 476.75f, 352.28f, 514.03f);
        editor.addListItem("Country", "USA");
        editor.addListItem("Country", "Canada");
        editor.addListItem("Country", "France");
        editor.addListItem("Country", "Spain");
        editor.save(_dataDir + "Sample-Form-01-mod.pdf");
    }
```


## Supprimer un élément de liste d'un fichier PDF existant

La méthode [delListItem](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor#delListItem-java.lang.String-java.lang.String-) vous permet de supprimer un élément particulier de la ListBox. Le premier paramètre est le nom du champ tandis que le deuxième paramètre est l'élément que vous souhaitez supprimer de la liste. Cette méthode est fournie par la classe [FormEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor). Le code suivant vous montre comment supprimer un élément de liste du fichier PDF.

```java
    public static void DelListItem() {
        FormEditor editor = new FormEditor();
        editor.bindPdf(_dataDir + "Sample-Form-04.pdf");
        // -----
        editor.delListItem("Country", "France");
        // -----
        editor.save(_dataDir + "Sample-Form-04-mod.pdf");
    }
```