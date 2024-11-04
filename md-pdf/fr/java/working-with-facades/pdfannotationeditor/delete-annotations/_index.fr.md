---
title: Supprimer les annotations (facades)
type: docs
weight: 10
url: /java/delete-annotations/
description: Cette section explique comment supprimer des annotations avec Aspose.PDF Facades en utilisant la classe PdfAnnotationEditor.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Vous pouvez utiliser la classe [PdfAnnotationEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor) pour supprimer des annotations, par type d'annotation spécifié, du fichier PDF existant.
 Afin de faire cela, vous devez créer un objet [PdfAnnotationEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor) et lier le fichier PDF d'entrée en utilisant la méthode bindPdf. Après cela, appelez la méthode [deleteAnnotations](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor#deleteAnnotation-java.lang.String-) avec le paramètre de type chaîne, pour supprimer toutes les annotations du fichier ; le paramètre de type chaîne représente le type d'annotation à supprimer. Enfin, utilisez la méthode save pour enregistrer le fichier PDF mis à jour.

L'extrait de code suivant vous montre comment supprimer une annotation par type d'annotation spécifié.

```java
public static void DeleteAnnotation() {
        // Ouvrir le document
        Scanner consoleScanner = new Scanner(System.in);
        Document document = new Document(_dataDir + "sample_cats_dogs.pdf");
        int index;
        for (index = 1; index <= document.getPages().get_Item(1).getAnnotations().size(); index++) {
            System.out.println(index + ". " + document.getPages().get_Item(1).getAnnotations().get_Item(index).getName()
                    + " " + document.getPages().get_Item(1).getAnnotations().get_Item(index).toString());
        }
        System.out.print("Veuillez entrer un numéro :");
        index = consoleScanner.nextInt();

        PdfAnnotationEditor annotationEditor = new PdfAnnotationEditor();
        annotationEditor.bindPdf(document);
        annotationEditor.deleteAnnotation(document.getPages().get_Item(1).getAnnotations().get_Item(1).getName());

        // Enregistrer le PDF mis à jour
        annotationEditor.save(_dataDir + "DeleteAnnotation.pdf");
        consoleScanner.close();
    }
    ```
[PdfAnnotationEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor) vous permet de supprimer toutes les annotations du fichier PDF existant.

Tout d'abord, créez un [PdfAnnotationEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor) et liez le fichier PDF d'entrée en utilisant la méthode BindPdf.

Ensuite, appelez la méthode [deleteAnnotations](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor#deleteAnnotation-java.lang.String-), pour supprimer toutes les annotations du fichier, puis utilisez la méthode Save pour enregistrer le fichier PDF mis à jour. Le snippet de code suivant vous montre comment supprimer toutes les annotations du fichier PDF.

```java
public static void DeleteAllAnnotations() {
    // Ouvrir le document
    PdfAnnotationEditor annotationEditor = new PdfAnnotationEditor();
    annotationEditor.bindPdf(_dataDir + "sample_cats_dogs.pdf");
    // Supprimer toutes les annotations
    annotationEditor.deleteAnnotations();
    // Enregistrer le PDF mis à jour
    annotationEditor.save(_dataDir + "DeleteAllAnnotations_out.pdf");
}
```