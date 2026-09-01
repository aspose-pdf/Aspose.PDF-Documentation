---
title: Ajouter une image au PDF à l'aide de Java
linktitle: Ajouter une image
type: docs
weight: 10
url: /java/add-image-to-existing-pdf-file/
description: Découvrez comment ajouter des images à des fichiers PDF existants en Java.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Ajouter des images aux fichiers PDF existants avec Java
Abstract: Cet article montre comment ajouter des images aux documents PDF à l'aide d'Aspose.PDF pour Java. Il couvre le placement d'une image à des coordonnées fixes, l'ajout d'images via des opérateurs de page de bas niveau, la définition d'un texte alternatif pour l'accessibilité et l'intégration de données d'image avec la compression Flate.
---
Aspose.PDF pour Java prend en charge à la fois le placement d'images de haut niveau et le dessin basé sur un opérateur de bas niveau.


## 
Ajouter une image avec les coordonnées de la page



Utilisez cet exemple lorsque vous devez placer une image à une position fixe sur une page PDF.


1. 
Créez un nouveau [Document] PDF (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) et ajoutez une page.

1. 
Appelez `page.addImage()` avec le chemin de l'image source et le rectangle cible.
1. Enregistrez le fichier PDF généré.


```java
public static void addImage(Path imageFile, Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        page.addImage(imageFile.toString(), new Rectangle(20, 730, 120, 830, true));
        document.save(outputFile.toString());
    }
}
```

## 
Ajouter une image avec les opérateurs de page



Utilisez cet exemple lorsque vous avez besoin d'un contrôle de bas niveau sur le placement et la mise à l'échelle des images via les opérateurs de page.


1. 
Créez un nouveau [Document] PDF (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) et ouvrez le flux d'images source.

1. 
Ajoutez l'image aux ressources de la page et calculez le rectangle cible.
1. Écrivez les opérateurs graphiques requis et enregistrez le document.


```java
public static void addImageUsingOperators(Path imageFile, Path outputFile) throws Exception {
    try (Document document = new Document();
         InputStream imageStream = Files.newInputStream(imageFile)) {
        Page page = document.getPages().add();
        page.setPageSize(842, 595);

        XImageCollection resourcesImages = page.getResources().getImages();
        String imageId = resourcesImages.add(imageStream);
        XImage xImage = resourcesImages.get_Item(resourcesImages.size());

        Rectangle rectangle = new Rectangle(
                0,
                0,
                page.getMediaBox().getWidth(),
                (page.getMediaBox().getWidth() * xImage.getHeight()) / xImage.getWidth(),
                true);

        page.getContents().add(new GSave());

        Matrix matrix = new Matrix(
                rectangle.getURX() - rectangle.getLLX(),
                0,
                0,
                rectangle.getURY() - rectangle.getLLY(),
                rectangle.getLLX(),
                rectangle.getLLX() + (page.getMediaBox().getHeight() - rectangle.getHeight()) / 2);
        page.getContents().add(new ConcatenateMatrix(matrix));
        page.getContents().add(new Do(imageId));
        page.getContents().add(new GRestore());

        document.save(outputFile.toString());
    }
}
```

## 
Ajouter une image et définir un texte alternatif



Utilisez cet exemple lorsque l'image doit inclure des métadonnées d'accessibilité pour les lecteurs d'écran.


1. 
Créez un nouveau [Document] PDF (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) et ajoutez l'image à la page.

1. 
Obtenez le [XImage] (https://reference.aspose.com/pdf/java/com.aspose.pdf/ximage/) inséré à partir des ressources de la page.
1. Définissez le texte alternatif et enregistrez le PDF.


```java
public static void addImageSetAlternativeTextForImage(Path imageFile, Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        page.setPageSize(842, 595);

        page.addImage(imageFile.toString(), new Rectangle(0, 0, 842, 595, true));

        XImage xImage = page.getResources().getImages().get_Item(1);
        boolean result = xImage.trySetAlternativeText("Alternative text for image", page);
        if (result) {
            System.out.println("Text has been added successfuly");
        }
        document.save(outputFile.toString());
    }
}
```

## 
Ajouter une image avec la compression Flate



Utilisez cet exemple lorsque vous souhaitez intégrer des données d'image à l'aide de la compression Flate.


1. 
Créez un nouveau [Document] PDF (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) et ouvrez le flux d'images.

1. 
Ajoutez l'image aux ressources de la page avec `ImageFilterType.Flate`.
1. Dessinez l'image via les opérateurs de page et enregistrez le résultat.

```java
public static void addImageToPdfWithFlateCompression(Path imageFile, Path outputFile) throws Exception {
    try (Document document = new Document();
         InputStream imageStream = Files.newInputStream(imageFile)) {
        Page page = document.getPages().add();
        XImageCollection resourcesImages = page.getResources().getImages();
        String imageId = resourcesImages.add(imageStream, ImageFilterType.Flate);

        page.getContents().add(new GSave());

        Rectangle rectangle = new Rectangle(0, 0, 600, 600, true);
        Matrix matrix = new Matrix(
                rectangle.getURX() - rectangle.getLLX(),
                0,
                0,
                rectangle.getURY() - rectangle.getLLY(),
                rectangle.getLLX(),
                rectangle.getLLY());

        page.getContents().add(new ConcatenateMatrix(matrix));
        page.getContents().add(new Do(imageId));
        page.getContents().add(new GRestore());

        document.save(outputFile.toString());
    }
}
```
