---
title: Copier le Champ Intérieur et Extérieur
type: docs
weight: 40
url: /fr/java/copy-inner-and-outer-field/
description: Cette section explique comment copier le champ intérieur et extérieur avec com.aspose.pdf.facades en utilisant la classe FormEditor.
lastmod: "2021-06-05"
draft: false
---

La méthode [copyInnerField](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor#copyInnerField-java.lang.String-java.lang.String-int-) vous permet de copier un champ dans le même fichier, aux mêmes coordonnées, sur la page spécifiée. Cette méthode nécessite le nom du champ que vous souhaitez copier, le nouveau nom du champ et le numéro de la page sur laquelle le champ doit être copié. La classe [FormEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor) fournit cette méthode. Le code suivant vous montre comment copier le champ au même emplacement dans le même fichier.

```java
    public static void CopyInnerField() {
        FormEditor editor = new FormEditor();
        Document document = new Document(_dataDir + "Sample-Form-01.pdf");
        document.getPages().add();
        editor.bindPdf(document);
        editor.copyInnerField("Last Name", "Last Name 2", 2);
        editor.save(_dataDir + "Sample-Form-01-mod.pdf");
    }
```


## Copier un champ extérieur dans un fichier PDF existant

La méthode [copyOuterField](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor#copyOuterField-java.lang.String-java.lang.String-) vous permet de copier un champ de formulaire à partir d'un fichier PDF externe, puis de l'ajouter au fichier PDF d'entrée au même emplacement et au numéro de page spécifié. Cette méthode nécessite le fichier PDF à partir duquel le champ doit être copié, le nom du champ et le numéro de page auquel le champ doit être copié. Cette méthode est fournie par la classe [FormEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor). Le snippet de code suivant vous montre comment copier un champ à partir d'un fichier PDF externe.

```java
  public static void CopyOuterField() {
        FormEditor editor = new FormEditor();
        Document document = new Document();
        document.getPages().add();
        editor.bindPdf(document);
        editor.copyOuterField(_dataDir + "Sample-Form-01.pdf", "First Name", 1);
        editor.copyOuterField(_dataDir + "Sample-Form-01.pdf", "Last Name", 1);
        editor.save(_dataDir + "Sample-Form-02-mod.pdf");
    }
```