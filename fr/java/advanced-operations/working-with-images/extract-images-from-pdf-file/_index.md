---
title: Extraire des images d'un fichier PDF à l'aide de Java
linktitle: Extraire des images
type: docs
weight: 30
url: /java/extract-images-from-pdf-file/
description: Découvrez comment extraire des images intégrées à partir de fichiers PDF en Java.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Extraire des images de fichiers PDF avec Java
Abstract: Cet article montre comment extraire des images de documents PDF à l'aide d'Aspose.PDF pour Java. Il couvre l'enregistrement d'une ressource d'image spécifique à partir d'une page et l'exportation d'images qui se trouvent dans une région rectangulaire sélectionnée.
---
Aspose.PDF pour Java prend en charge l'extraction directe des ressources d'image et le filtrage basé sur le placement.


## 
Extraire une image intégrée par index



Utilisez cet exemple lorsque vous devez enregistrer une ressource image spécifique à partir d’une page PDF.


1. 
Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Accédez à la cible [XImage] (https://reference.aspose.com/pdf/java/com.aspose.pdf/ximage/) à partir des ressources de la page.
1. Enregistrez le flux d'images dans un fichier de sortie.


```java
public static void extractImage(Path inputFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString());
         OutputStream outputImage = Files.newOutputStream(outputFile)) {
        XImage image = document.getPages().get_Item(1).getResources().getImages().get_Item(1);
        image.save(outputImage);
    }
}
```

## 
Extraire des images d'une région de page spécifique



Utilisez cet exemple lorsque seules les images placées à l’intérieur d’un rectangle sélectionné doivent être exportées.


1. 
Définissez la cible [Rectangle] (https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/) et ouvrez le PDF source.

1. 
Utilisez [ImagePlacementAbsorber] (https://reference.aspose.com/pdf/java/com.aspose.pdf/imageplacementabsorber/) pour inspecter les emplacements d'images sur la page.
1. Enregistrez uniquement les images dont le placement correspond à la région sélectionnée.

```java
public static void extractImageFromSpecificRegion(Path inputFile, Path outputFile) throws Exception {
    Rectangle rectangle = new Rectangle(0, 0, 590, 590, true);

    try (Document document = new Document(inputFile.toString())) {
        ImagePlacementAbsorber absorber = new ImagePlacementAbsorber();
        document.getPages().get_Item(1).accept(absorber);
        int index = 1;
        for (ImagePlacement imagePlacement : absorber.getImagePlacements()) {
            Point point1 = new Point(imagePlacement.getRectangle().getLLX(), imagePlacement.getRectangle().getLLY());
            Point point2 = new Point(imagePlacement.getRectangle().getURX(), imagePlacement.getRectangle().getURX());
            if (rectangle.contains(point1, true) && rectangle.contains(point2, true)) {
                Path indexedOutputFile = Path.of(outputFile.toString().replace("index", String.valueOf(index)));
                try (OutputStream outputImage = Files.newOutputStream(indexedOutputFile)) {
                    imagePlacement.getImage().save(outputImage);
                }
                index++;
            }
        }
    }
}
```
