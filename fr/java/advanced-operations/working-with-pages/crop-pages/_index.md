---
title: Recadrer des pages PDF en Java
linktitle: Recadrer des pages PDF
type: docs
weight: 70
url: /java/crop-pages/
description: Découvrez comment recadrer des pages PDF et ajuster les zones de recadrage, de découpage, de fond perdu et de support en Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Recadrez les pages et ajustez les zones de page dans les fichiers PDF avec Java
Abstract: Cet article explique comment recadrer des pages PDF à l'aide d'Aspose.PDF pour Java. Il couvre l'attribution d'un nouveau rectangle de recadrage aux zones de recadrage, de rognage, d'illustration et de fond perdu, ainsi que le recadrage automatique d'une page en fonction du contenu de l'image détecté.
---
Aspose.PDF pour Java vous permet de recadrer des pages soit par des coordonnées de boîte explicites, soit en fonction du contenu détecté.


## 
Recadrer une page en définissant des zones de page



Utilisez cet exemple lorsque vous devez appliquer la même zone de recadrage aux zones de la page principale.


1. 
Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Créez le nouveau recadrage [Rectangle] (https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/).
1. Appliquez le rectangle aux zones de page liées au recadrage et enregistrez le document.


```java
public static void cropPage(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Rectangle newBox = new Rectangle(200, 220, 2170, 1520, true);
        document.getPages().get_Item(1).setCropBox(newBox);
        document.getPages().get_Item(1).setTrimBox(newBox);
        document.getPages().get_Item(1).setArtBox(newBox);
        document.getPages().get_Item(1).setBleedBox(newBox);
        document.save(outputFile.toString());
    }
}
```

## 
Recadrer une page en fonction du contenu détecté



Utilisez cet exemple lorsque la zone de recadrage doit être dérivée de la première image détectée sur la page.


1. 
Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Utilisez [ImagePlacementAbsorber] (https://reference.aspose.com/pdf/java/com.aspose.pdf/imageplacementabsorber/) pour détecter les emplacements d'images.
1. Set the crop box to the image rectangle if one is found, then save the document.

```java
public static void cropPageByContent(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        ImagePlacementAbsorber absorber = new ImagePlacementAbsorber();
        document.getPages().get_Item(1).accept(absorber);
        if (absorber.getImagePlacements().size() > 0) {
            document.getPages().get_Item(1).setCropBox(absorber.getImagePlacements().get_Item(1).getRectangle());
        } else {
            System.out.println("No images found on the first page");
        }
        document.save(outputFile.toString());
    }
}
```
