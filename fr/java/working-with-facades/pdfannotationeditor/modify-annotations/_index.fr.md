---
title: Modifier les annotations dans votre fichier PDF (facades)
type: docs
weight: 50
url: /java/modify-annotations/
description: Cette section explique comment modifier les annotations d'un fichier PDF en XFDF avec Aspose.PDF Facades.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

La méthode [modifyAnnotations](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor#modifyAnnotations-int-int-com.aspose.pdf.Annotation-) vous permet de changer les attributs de base d'une annotation, c'est-à-dire le sujet, la date de modification, l'auteur, la couleur de l'annotation, et le drapeau d'ouverture. Vous pouvez également définir l'auteur directement en utilisant la méthode ModifyAnnotations. Cette classe propose également deux méthodes surchargées pour supprimer des annotations. La première méthode appelée DeleteAnnotations supprime toutes les annotations d'un fichier PDF.

Par exemple, dans le code suivant, envisagez de changer l'auteur de notre annotation en utilisant [modifyAnnotationsAuthor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor#modifyAnnotationsAuthor-int-int-java.lang.String-java.lang.String-).

```java
 public static void ModifyAnnotationsAuthor() {
        PdfAnnotationEditor annotationEditor = new PdfAnnotationEditor();
        annotationEditor.bindPdf(_dataDir + "sample_cats_dogs.pdf");
        annotationEditor.modifyAnnotationsAuthor(1, 2, "Aspose User", "Utilisateur Aspose.PDF");
        annotationEditor.save(_dataDir + "ModifyAnnotationsAuthor.pdf");
    }
```

La deuxième méthode vous permet de supprimer toutes les annotations d'un type spécifié.

```java
    public static void ModifyAnnotations() {
        Document document = new Document(_dataDir + "sample_cats_dogs.pdf");
        PdfAnnotationEditor annotationEditor = new PdfAnnotationEditor();
        annotationEditor.bindPdf(document);

        // Créez un nouvel objet de type Annotation pour modifier les attributs d'annotation
        DefaultAppearance defaultAppearance = new DefaultAppearance();
        FreeTextAnnotation annotation = new FreeTextAnnotation(document.getPages().get_Item(1),
                new Rectangle(1, 1, 1, 1), defaultAppearance);

        annotation.setTitle("Utilisateur Démo Aspose.PDF");
        annotation.setSubject("Article Technique");

        // Modifiez les annotations dans le fichier PDF
        annotationEditor.modifyAnnotations(1, 1, annotation);
        annotationEditor.save(_dataDir + "ModifyAnnotations.pdf");
    }
```


## Voir aussi

Essayez de comparer et de trouver une manière de travailler avec les annotations qui vous convient. Apprenons la section [Annotations PDF](/pdf/java/annotations/).