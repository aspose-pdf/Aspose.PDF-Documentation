---
title: Ajouter des tampons d'image au PDF en Java
linktitle: Tampons d'image dans un fichier PDF
type: docs
weight: 10
url: /java/image-stamps-in-pdf-page/
description: Découvrez comment ajouter des tampons d'image aux pages PDF en Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Ajoutez des tampons d'image et des arrière-plans d'images aux pages PDF avec Java
Abstract: Cet article explique comment ajouter des tampons d'image aux fichiers PDF à l'aide d'Aspose.PDF pour Java. Il couvre les tampons d'image avec le positionnement, la rotation, l'opacité et le contrôle de qualité, et utilise une image comme arrière-plan d'une boîte flottante.
---
Aspose.PDF pour Java prend en charge les tampons d'image en tant que superpositions et éléments de mise en page basés sur des images.


## 
Ajouter un tampon d'image



Utilisez cet exemple lorsqu'une page doit afficher un tampon d'image avec un emplacement et une opacité personnalisés.


1. 
Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Créez un [ImageStamp] (https://reference.aspose.com/pdf/java/com.aspose.pdf/imagestamp/) et configurez son apparence.
1. Ajoutez le tampon à la page et enregistrez le document.


```java
public static void addImageStamp(Path inputFile, Path imageFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        ImageStamp imageStamp = new ImageStamp(imageFile.toString());
        imageStamp.setBackground(true);
        imageStamp.setXIndent(100);
        imageStamp.setYIndent(100);
        imageStamp.setHeight(300);
        imageStamp.setWidth(300);
        imageStamp.setRotate(Rotation.on270);
        imageStamp.setOpacity(0.5);

        document.getPages().get_Item(1).addStamp(imageStamp);
        document.save(outputFile.toString());
    }
}
```

## 
Ajouter un tampon d'image avec contrôle qualité



Utilisez cet exemple lorsque vous devez ajuster la qualité de rendu du tampon d'image.


1. 
Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Créez un [ImageStamp] (https://reference.aspose.com/pdf/java/com.aspose.pdf/imagestamp/) et définissez la valeur de qualité.
1. Ajoutez le tampon à la page et enregistrez le résultat.


```java
public static void addImageStampWithQualityControl(Path inputFile, Path imageFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        ImageStamp imageStamp = new ImageStamp(imageFile.toString());
        imageStamp.setQuality(10);
        document.getPages().get_Item(1).addStamp(imageStamp);
        document.save(outputFile.toString());
    }
}
```

## 
Utiliser une image comme arrière-plan d'une boîte flottante



Utilisez cet exemple lorsqu’une image doit servir d’arrière-plan à un conteneur de mise en page stylisé.


1. 
Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) et accédez à la page cible.

1. 
Créez une [FloatingBox] (https://reference.aspose.com/pdf/java/com.aspose.pdf/floatingbox/) avec des paramètres de texte et de bordure.
1. Définissez l'image d'arrière-plan, ajoutez la zone à la page et enregistrez le document.

```java
public static void addImageAsBackgroundInFloatingBox(Path inputFile, Path imageFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);
        FloatingBox box = new FloatingBox(200.0f, 100.0f);
        box.setLeft(40);
        box.setTop(80);
        box.setHorizontalAlignment(HorizontalAlignment.Center);
        box.getParagraphs().add(new TextFragment("Text in Floating Box"));
        box.setBorder(new BorderInfo(BorderSide.All, Color.getRed()));

        Image image = new Image();
        image.setFile(imageFile.toString());
        box.setBackgroundImage(image);
        box.setBackgroundColor(Color.getYellow());
        page.getParagraphs().add(box);

        document.save(outputFile.toString());
    }
}
```
