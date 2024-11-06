---
title: Ajout d'Annotations à un fichier PDF existant
type: docs
weight: 80
url: fr/java/adding-annotations-to-existing-pdf-file/
description: Cette section explique comment ajouter des annotations à un fichier PDF existant avec Aspose.PDF Facades.
lastmod: "2021-06-30"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Ajouter une Annotation de Texte Libre dans un Fichier PDF Existant (facades)

Une annotation de texte libre affiche du texte directement sur la page. [PdfContentEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor) vous permet d'ajouter des annotations de différents types dans un fichier PDF existant. Vous pouvez utiliser la méthode respective pour ajouter une annotation particulière. Par exemple, dans l'extrait de code suivant, nous avons utilisé la méthode [createFreeText](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor#createFreeText-java.awt.Rectangle-java.lang.String-int-) pour ajouter une annotation de type FreeText.

Tout type d'annotations peut être ajouté au fichier PDF de la même manière.
 Tout d'abord, vous devez créer un objet de type [PdfContentEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor) et lier le fichier PDF d'entrée en utilisant la méthode bindPdf. Deuxièmement, vous devez créer un objet Rectangle pour spécifier la zone de l'annotation. Après cela, vous pouvez appeler la méthode [createFreeText](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor#createFreeText-java.awt.Rectangle-java.lang.String-int-) pour ajouter une annotation FreeText, le numéro de page sur lequel l'annotation est située, puis utiliser la méthode save pour enregistrer le fichier PDF mis à jour.

Le code suivant vous montre comment ajouter une annotation de texte libre dans un fichier PDF.

```java
  public static void AddFreeTextAnnotation()
    {
        var document = new Document(_dataDir + "sample.pdf");
        PdfContentEditor editor = new PdfContentEditor(document);
        TextFragmentAbsorber tfa = new TextFragmentAbsorber("PDF");
        tfa.visit(document.getPages().get_Item(1));

        java.awt.Rectangle rect = new  java.awt.Rectangle();
        rect.x = (int)tfa.getTextFragments().get_Item(1).getRectangle().getLLX();
        rect.y = (int)tfa.getTextFragments().get_Item(1).getRectangle().getURY() + 5;
        rect.height = 18;
        rect.width = 100;        

        editor.createFreeText(rect, "Démonstration de texte libre", 1); // le dernier paramètre est un numéro de page
        editor.save(_dataDir + "PdfContentEditorDemo_FreeTextAnnotation.pdf");
    }
```

## Ajouter une Annotation de Texte dans un Fichier PDF Existant (facades)

Dans cet exemple également, vous devez créer un objet de type [PdfContentEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor) et lier le fichier PDF d'entrée en utilisant la méthode [bindPdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor#bindPdf-java.lang.String-). Ensuite, vous devez créer un objet Rectangle pour spécifier la zone de l'annotation. Après cela, vous pouvez appeler la méthode [createFreeText](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor#createFreeText-java.awt.Rectangle-java.lang.String-int-) pour ajouter une annotation de texte libre, créer le titre de vos annotations, et le numéro de la page sur laquelle l'annotation est située.

```java
 public static void AddTextAnnotation()
    {
        var document = new Document(_dataDir + "sample.pdf");
        PdfContentEditor editor = new PdfContentEditor(document);
        TextFragmentAbsorber tfa = new TextFragmentAbsorber("PDF");
        tfa.visit(document.getPages().get_Item(1));

        java.awt.Rectangle rect = new  java.awt.Rectangle();
        rect.x = (int)tfa.getTextFragments().get_Item(1).getRectangle().getLLX();
        rect.y = (int)tfa.getTextFragments().get_Item(1).getRectangle().getURY() + 5;
        rect.height = 18;
        rect.width = 100;        

        // Créer une annotation de texte
        editor.createText(rect, "Utilisateur Aspose", "PDF est un meilleur format pour les documents modernes", false, "Key", 1);
        editor.save(_dataDir + "PdfContentEditorDemo_TextAnnotation.pdf");
    }
```


## Ajouter une Annotation de Ligne dans un Fichier PDF Existant (façades)

Nous spécifions également le Rectangle, les coordonnées du début et de la fin de la ligne, le numéro de page, l'épaisseur, le style et la couleur du cadre de l'annotation, le type de tiret de ligne, le type de début et de fin de la ligne.

```java

    public static void AddLineAnnotation()
    {
        var document = new Document(_dataDir + "Appartments.pdf");
        PdfContentEditor editor = new PdfContentEditor(document);
        // Créer une Annotation de Ligne
        editor.createLine(
            new java.awt.Rectangle(550, 93, 562, 439),
            "Test",
            556, 99, 556, 443, 1, 1,
            java.awt.Color.RED,
            "dash",
            new int[] { 1, 0, 3 },
            new String[] { "Open", "Open" });
        editor.save(_dataDir + "PdfContentEditorDemo_LineAnnotation.pdf");
    }
```