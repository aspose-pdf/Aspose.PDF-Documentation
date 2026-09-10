---
title: Modifier la taille de la page PDF en Java
linktitle: Changer la taille de la page
type: docs
weight: 40
url: /java/change-page-size/
description: Découvrez comment lire et modifier les dimensions d'une page PDF en Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Lire et mettre à jour les dimensions et les zones de page avec Java
Abstract: Cet article montre comment lire et modifier les dimensions d'une page PDF à l'aide d'Aspose.PDF pour Java. Il couvre l'obtention de la taille de la page, la mesure de la taille de la page avec la rotation appliquée et la mise à jour de la première page vers une nouvelle taille tout en imprimant les dimensions de la boîte avant et après la modification.
---
Aspose.PDF pour Java peut à la fois signaler les dimensions des pages et les mettre à jour.


## 
Changer la taille de la page



Utilisez cet exemple lorsque vous devez redimensionner une page existante et inspecter les zones de page avant et après la modification.


1. 
Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Obtenez la cible [Page] (https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) et imprimez ses valeurs de boîte actuelles.
1. Définissez la nouvelle taille de page et enregistrez le document.


```java
public static void setPageSize(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);
        printBoxes("Before set", page);
        page.setPageSize(597.6, 842.4);
        printBoxes("After set", page);
        document.save(outputFile.toString());
    }
}
```

## 
Obtenir la taille de la page



Utilisez cet exemple lorsque vous devez lire les dimensions visibles d'une page.


1. 
Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Obtenez le rectangle de la page avec la gestion de la rotation activée.
1. Output the page width and height.


```java
public static void getPageSize(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Rectangle rectangle = document.getPages().get_Item(1).getPageRect(true);
        System.out.println(rectangle.getWidth() + " : " + rectangle.getHeight());
    }
}
```

## 
Get the page size with rotation applied



Use this example when you need to compare page dimensions before and after accounting for rotation.


1. 
Open the source PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Rotate the target [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. Lisez le rectangle de la page avec et sans gestion de rotation et affichez les deux valeurs.

```java
public static void getPageSizeRotation(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);
        page.setRotate(Rotation.on90);
        Rectangle rectangle = page.getPageRect(false);
        System.out.println(rectangle.getWidth() + " : " + rectangle.getHeight());
        rectangle = page.getPageRect(true);
        System.out.println(rectangle.getWidth() + " : " + rectangle.getHeight());
    }
}
```
