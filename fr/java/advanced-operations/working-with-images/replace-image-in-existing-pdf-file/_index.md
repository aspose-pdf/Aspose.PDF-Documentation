---
title: Remplacer l'image dans un fichier PDF existant à l'aide de Java
linktitle: Remplacer l'image
type: docs
weight: 70
url: /java/replace-image-in-existing-pdf-file/
description: Découvrez comment remplacer les images intégrées dans des fichiers PDF existants en Java.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Remplacer les images dans les fichiers PDF existants avec Java
Abstract: Cet article montre comment remplacer des images dans des documents PDF à l'aide d'Aspose.PDF pour Java. Il couvre le remplacement d'une image par son index de ressources et le remplacement du premier emplacement d'image correspondant trouvé avec ImagePlacementAbsorber.
---
Utilisez soit la collection d'images de page, soit la recherche basée sur l'emplacement en fonction de la précision avec laquelle vous devez cibler l'image.


## 
Remplacer une image par un index de ressources


1. 
Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Accédez aux ressources d'images sur la [Page] cible (https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).

1. 
Remplacez la ressource image cible par le nouveau fichier image.
1. Enregistrez le [Document] PDF mis à jour (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).


```java
public static void replaceImage(Path inputFile, Path imageFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString());
         InputStream imageStream = Files.newInputStream(imageFile)) {
        document.getPages().get_Item(1).getResources().getImages().replace(1, imageStream);
        document.save(outputFile.toString());
    }
}
```

## 
Remplacez une image en utilisant `ImagePlacementAbsorber`


1. 
Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Créez un [ImagePlacementAbsorber] (https://reference.aspose.com/pdf/java/com.aspose.pdf/imageplacementabsorber/) et visitez la [Page] cible (https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).

1. 
Obtenez la cible [ImagePlacement] (https://reference.aspose.com/pdf/java/com.aspose.pdf/imageplacement/) et remplacez-la par le nouveau flux d'images.
1. Enregistrez le [Document] PDF mis à jour (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void replaceImageWithAbsorber(Path inputFile, Path imageFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        ImagePlacementAbsorber absorber = new ImagePlacementAbsorber();
        document.getPages().get_Item(1).accept(absorber);

        if (absorber.getImagePlacements().size() > 0) {
            ImagePlacement imagePlacement = absorber.getImagePlacements().get_Item(1);
            try (InputStream imageStream = Files.newInputStream(imageFile)) {
                imagePlacement.replace(imageStream);
            }
        }

        document.save(outputFile.toString());
    }
}
```
