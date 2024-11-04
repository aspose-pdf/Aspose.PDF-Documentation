---
title: Modifier les annotations dans votre PDF 
type: docs
weight: 50
url: /net/modify-annotations/
description: Cette section explique comment modifier les annotations d'un fichier PDF en XFDF avec Aspose.PDF Facades.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

La méthode [ModifyAnnotations](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor/methods/modifyannotations) vous permet de changer les attributs de base d'une annotation, c'est-à-dire le sujet, la date de modification, l'auteur, la couleur de l'annotation et le drapeau ouvert. Vous pouvez également définir l'auteur directement en utilisant la méthode ModifyAnnotations. Cette classe fournit également deux méthodes surchargées pour supprimer les annotations. La première méthode appelée DeleteAnnotations supprime toutes les annotations d'un fichier PDF.

Par exemple, dans le code suivant, envisagez de changer l'auteur dans notre annotation en utilisant [ModifyAnnotationsAuthor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor/methods/modifyannotationsauthor).

```csharp
   public static void ModifyAnnotationsAuthor()
        {
            PdfAnnotationEditor annotationEditor = new PdfAnnotationEditor();
            annotationEditor.BindPdf(_dataDir + "sample_cats_dogs.pdf");
            annotationEditor.ModifyAnnotationsAuthor(1, 2, "Aspose User", "Aspose.PDF user");
            annotationEditor.Save(_dataDir + "ModifyAnnotationsAuthor.pdf");
        }
```

La deuxième méthode vous permet de supprimer toutes les annotations d'un type spécifié.

```csharp
   public static void ModifyAnnotations()
        {
            var document = new Document(_dataDir + "sample_cats_dogs.pdf");
            PdfAnnotationEditor annotationEditor = new PdfAnnotationEditor();
            annotationEditor.BindPdf(document);

            // Créer un nouvel objet de type Annotation pour modifier les attributs d'annotation
            var defaultAppearance = new Aspose.Pdf.Annotations.DefaultAppearance();
            Aspose.Pdf.Annotations.FreeTextAnnotation annotation = new Aspose.Pdf.Annotations.FreeTextAnnotation(
                document.Pages[1],
                new Aspose.Pdf.Rectangle(1, 1, 1, 1),
                defaultAppearance)
            {

                // Définir de nouveaux attributs d'annotation
                Title = "Utilisateur Démo Aspose.PDF",
                Subject = "Article Technique"
            };
            // Modifier les annotations dans le fichier PDF
            annotationEditor.ModifyAnnotations(1, 1, annotation);
            annotationEditor.Save(_dataDir + "ModifyAnnotations.pdf");
        }
```

## Voir aussi

Essayez de comparer et de trouver un moyen de travailler avec les annotations qui vous convient. Apprenons la section [Annotations PDF](/pdf/net/annotations/).