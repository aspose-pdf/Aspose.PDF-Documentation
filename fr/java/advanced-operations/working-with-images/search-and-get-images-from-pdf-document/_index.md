---
title: Obtenir et rechercher des images au format PDF
linktitle: Obtenir et rechercher des images
type: docs
weight: 40
url: /java/search-and-get-images-from-pdf-document/
description: Découvrez comment rechercher et inspecter des images dans des documents PDF en Java.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Rechercher et inspecter des images dans des fichiers PDF avec Java
Abstract: Cet article montre comment rechercher et inspecter des images dans des documents PDF à l'aide d'Aspose.PDF pour Java. Il couvre la lecture de la géométrie de placement d'image, la détection du type de couleur, l'extraction de texte alternatif et le calcul de la résolution d'image efficace à partir des opérateurs de page.
---
Aspose.PDF pour Java peut inspecter les informations de placement d'image ainsi que les données de dessin de niveau inférieur.


## 
Obtenir les paramètres de placement d'image



Utilisez cet exemple lorsque vous devez inspecter la géométrie de l’image et la résolution effective sur une page.


1. 
Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Utilisez [ImagePlacementAbsorber] (https://reference.aspose.com/pdf/java/com.aspose.pdf/imageplacementabsorber/) pour collecter les emplacements d'images.
1. Affichez la taille, les coordonnées et la résolution de chaque image placée.


```java
public static void extractImageParams(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        ImagePlacementAbsorber absorber = new ImagePlacementAbsorber();
        document.getPages().get_Item(1).accept(absorber);

        for (ImagePlacement imagePlacement : absorber.getImagePlacements()) {
            System.out.println("image width: " + imagePlacement.getRectangle().getWidth());
            System.out.println("image height: " + imagePlacement.getRectangle().getHeight());
            System.out.println("image LLX: " + imagePlacement.getRectangle().getLLX());
            System.out.println("image LLY: " + imagePlacement.getRectangle().getLLY());
            System.out.println("image horizontal resolution: " + imagePlacement.getResolution().getX());
            System.out.println("image vertical resolution: " + imagePlacement.getResolution().getY());
        }
    }
}
```

## 
Détecter les types de couleurs d'image



Utilisez cet exemple lorsque vous devez compter les images en niveaux de gris et RVB dans une page PDF.


1. 
Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Utilisez [ImagePlacementAbsorber] (https://reference.aspose.com/pdf/java/com.aspose.pdf/imageplacementabsorber/) pour parcourir les images de page.
1. Lisez le [ColorType] (https://reference.aspose.com/pdf/java/com.aspose.pdf/colortype/) de chaque image et affichez les totaux.


```java
public static void extractImageTypesFromPdf(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        ImagePlacementAbsorber absorber = new ImagePlacementAbsorber();
        int grayscaled = 0;
        int rgb = 0;

        document.getPages().get_Item(1).accept(absorber);

        System.out.println("--------------------------------");
        System.out.println("Total Images = " + absorber.getImagePlacements().size());

        int imageCounter = 1;
        for (ImagePlacement imagePlacement : absorber.getImagePlacements()) {
            ColorType colorType = imagePlacement.getImage().getColorType();
            if (colorType == ColorType.Grayscale) {
                grayscaled++;
                System.out.println("Image " + imageCounter + " is Grayscale...");
            } else if (colorType == ColorType.Rgb) {
                rgb++;
                System.out.println("Image " + imageCounter + " is RGB...");
            }
            imageCounter++;
        }

        System.out.println("--------------------------------");
        System.out.println("Grayscale Images = " + grayscaled);
        System.out.println("RGB Images = " + rgb);
    }
}
```

## 
Extraire le texte alternatif de l'image



Utilisez cet exemple lorsque vous devez inspecter le texte d’accessibilité associé aux images de page.


1. 
Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Utilisez [ImagePlacementAbsorber] (https://reference.aspose.com/pdf/java/com.aspose.pdf/imageplacementabsorber/) pour collecter les emplacements d'images.
1. Lisez le texte alternatif pour chaque image et affichez le résultat.


```java
public static void extractImageAltText(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        ImagePlacementAbsorber absorber = new ImagePlacementAbsorber();
        document.getPages().get_Item(1).accept(absorber);

        for (ImagePlacement imagePlacement : absorber.getImagePlacements()) {
            System.out.println("Name in collection: " + imagePlacement.getImage().getNameInCollection());
            List<String> lines = imagePlacement.getImage().getAlternativeText(document.getPages().get_Item(1));
            if (!lines.isEmpty()) {
                System.out.println("Alt Text: " + lines.get(0));
            } else {
                System.out.println("Alt Text: ");
            }
        }
    }
}
```

## 
Calculer les informations d'image à partir des opérateurs de page



Utilisez cet exemple lorsque vous devez dériver la taille et la résolution efficaces de l’image à partir d’opérateurs de contenu de page de bas niveau.


1. 
Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) et collectez les noms des ressources d'image.

1. 
Suivez l’état des graphiques tout en parcourant les opérateurs de page.
1. Résolvez chaque opération de dessin d’image et calculez ses dimensions et sa résolution effectives.

```java
public static void extractImageInformationFromPdf(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        int defaultResolution = 72;
        List<Matrix> graphicsState = new ArrayList<>();
        List<String> imageNames = Arrays.asList(document.getPages().get_Item(1).getResources().getImages().getNames());

        graphicsState.add(new Matrix(1, 0, 0, 1, 0, 0));

        for (Operator operator : document.getPages().get_Item(1).getContents()) {
            if (operator instanceof GSave) {
                graphicsState.add(new Matrix(graphicsState.get(graphicsState.size() - 1)));
            } else if (operator instanceof GRestore) {
                graphicsState.remove(graphicsState.size() - 1);
            } else if (operator instanceof ConcatenateMatrix concatenateMatrix) {
                Matrix current = graphicsState.get(graphicsState.size() - 1);
                graphicsState.set(graphicsState.size() - 1, current.multiply(concatenateMatrix.getMatrix()));
            } else if (operator instanceof Do doOperator) {
                if (imageNames.contains(doOperator.getName())) {
                    Matrix lastCtm = graphicsState.get(graphicsState.size() - 1);
                    int index = imageNames.indexOf(doOperator.getName()) + 1;
                    XImage image = document.getPages().get_Item(1).getResources().getImages().get_Item(index);

                    double scaledWidth = Math.sqrt(Math.pow(lastCtm.getA(), 2) + Math.pow(lastCtm.getB(), 2));
                    double scaledHeight = Math.sqrt(Math.pow(lastCtm.getC(), 2) + Math.pow(lastCtm.getD(), 2));

                    double originalWidth = image.getWidth();
                    double originalHeight = image.getHeight();

                    double resHorizontal = originalWidth * defaultResolution / scaledWidth;
                    double resVertical = originalHeight * defaultResolution / scaledHeight;

                    String info = String.format(
                            "%s image %s (%.2f:%.2f): res %.2f x %.2f",
                            inputFile,
                            doOperator.getName(),
                            scaledWidth,
                            scaledHeight,
                            resHorizontal,
                            resVertical);
                    System.out.println(info);
                }
            }
        }
    }
}
```
