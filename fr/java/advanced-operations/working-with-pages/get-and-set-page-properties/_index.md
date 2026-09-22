---
title: Obtenir et définir les propriétés des pages PDF en Java
linktitle: Getting and Setting Page Properties
type: docs
weight: 90
url: /fr/java/get-and-set-page-properties/
description: Découvrez comment inspecter les propriétés des pages PDF en Java, notamment leur nombre, leurs zones, leur rotation et leur type de couleur.
lastmod: "2026-09-22"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Inspecter le nombre de pages, les zones de page et le type de couleur des fichiers PDF avec Java
Abstract: Cet article explique comment inspecter les propriétés des pages avec Aspose.PDF for Java. Il couvre la lecture du nombre de pages, la génération de paragraphes et le calcul du nombre de pages avant l’enregistrement, l’affichage des dimensions des principales zones de page et l’identification du type de couleur de chaque page.
---
Aspose.PDF for Java peut inspecter le nombre de pages, les zones de page, la rotation et le type de couleur de la page.

## Obtenir le nombre de pages

Utilisez cet exemple lorsque vous devez lire le nombre total de pages dans un PDF.

1. Ouvrez le PDF source [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Lisez la taille de la collection de pages.
1. Affichez le nombre total de pages.

```java
public static void getPageCount(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        System.out.println("Page Count: " + document.getPages().size());
    }
}
```

## Obtenir le nombre de pages avant d'enregistrer

Utilisez cet exemple lorsque vous avez besoin de savoir combien de pages le contenu généré produira avant d'écrire le fichier.

1. Créez un nouveau document PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) et ajoutez du contenu à une page.
1. Traitez les paragraphes pour forcer le calcul de la mise en page.
1. Lisez le nombre de pages résultant et affichez-le.

```java
public static void getPageCountWithoutSaving(Path inputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        for (int i = 0; i < 300; i++) {
            page.getParagraphs().add(new TextFragment("Pages count test"));
        }
        document.processParagraphs();
        System.out.println("Number of pages in document = " + document.getPages().size());
    }
}
```

## Obtenir les propriétés de la zone de page

Utilisez cet exemple lorsque vous devez inspecter toutes les principales dimensions des zones de page et valeurs de rotation de page.

1. Ouvrez le PDF source [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) et accédez à la page cible.
1. Collectez les valeurs de la zone de page dans une carte.
1. Affichez les dimensions et les informations de rotation des pages.

```java
public static void getPageProperties(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);
        Map<String, Rectangle> boxes = new LinkedHashMap<>();
        boxes.put("ArtBox", page.getArtBox());
        boxes.put("BleedBox", page.getBleedBox());
        boxes.put("CropBox", page.getCropBox());
        boxes.put("MediaBox", page.getMediaBox());
        boxes.put("TrimBox", page.getTrimBox());
        boxes.put("Rect", page.getRect());

        for (Map.Entry<String, Rectangle> entry : boxes.entrySet()) {
            Rectangle box = entry.getValue();
            System.out.println(entry.getKey() + " : Height=" + box.getHeight()
                    + ",Width=" + box.getWidth()
                    + ",LLX=" + box.getLLX()
                    + ",LLY=" + box.getLLY()
                    + ",URX=" + box.getURX()
                    + ",URY=" + box.getURY());
        }

        System.out.println("Page Number : " + page.getNumber());
        System.out.println("Rotate : " + page.getRotate());
    }
}
```

## Obtenir le type de couleur de chaque page

Utilisez cet exemple lorsque vous devez déterminer si les pages sont en noir et blanc, en niveaux de gris ou RVB.

1. Ouvrez le PDF source [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Parcourez toutes les pages et lisez chaque page [ColorType](https://reference.aspose.com/pdf/java/com.aspose.pdf/colortype/).
1. Convertissez la valeur enum en texte lisible et affichez le résultat.

```java
public static void getPageColorType(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (int pageNumber = 1; pageNumber <= document.getPages().size(); pageNumber++) {
            ColorType pageColorType = document.getPages().get_Item(pageNumber).getColorType();
            String colorDescription = switch (pageColorType) {
                case BlackAndWhite -> "Black and white";
                case Grayscale -> "Gray Scale";
                case Rgb -> "RGB";
                case Undefined -> "undefined";
            };
            System.out.println("Page # " + pageNumber + " is " + colorDescription + ".");
        }
    }
}
```
