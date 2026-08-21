---
title: Get and Set PDF Page Properties in Java
linktitle: Getting and Setting Page Properties
type: docs
weight: 90
url: /java/get-and-set-page-properties/
description: Learn how to inspect PDF page properties such as count, boxes, rotation, and color information in Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Inspect page count, boxes, and color type in PDF files with Java
Abstract: This article explains how to inspect page properties using Aspose.PDF for Java. It covers reading the page count, generating paragraphs and checking the resulting count before saving, printing all major page box values, and identifying the color type of each page.
---
Aspose.PDF pour Java peut inspecter le nombre de pages, les boîtes de page, la rotation et le type de couleur de la page.


## 
Obtenir le nombre de pages



Utilisez cet exemple lorsque vous devez lire le nombre total de pages dans un PDF.


1. 
Ouvrez le PDF source [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Lisez la taille de la collection de pages.
1. Affichez le nombre total de pages.


```java
public static void getPageCount(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        System.out.println("Page Count: " + document.getPages().size());
    }
}
```

## 
Obtenez le nombre de pages avant d'enregistrer



Utilisez cet exemple lorsque vous avez besoin de savoir combien de pages le contenu généré produira avant d'écrire le fichier.


1. 
Créez un nouveau [Document] PDF (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) et ajoutez du contenu à une page.

1. 
Traitez les paragraphes pour forcer le calcul de la mise en page.
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

## 
Obtenir les propriétés de la zone de page



Utilisez cet exemple lorsque vous devez inspecter toutes les principales dimensions de boîte et valeurs de rotation de page.


1. 
Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) et accédez à la page cible.

1. 
Collectez les valeurs de la zone de page dans une carte.
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

## 
Obtenez le type de couleur de chaque page



Utilisez cet exemple lorsque vous devez déterminer si les pages sont en noir et blanc, en niveaux de gris ou RVB.


1. 
Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Parcourez toutes les pages et lisez chaque page [ColorType] (https://reference.aspose.com/pdf/java/com.aspose.pdf/colortype/).
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
