---
title: Annotations en filigrane utilisant Java
linktitle: Annotations en filigrane
type: docs
weight: 70
url: /java/pdfannotationeditor-class/watermark-annotations/
description: Découvrez comment ajouter, inspecter et supprimer des annotations en filigrane dans des documents PDF à l'aide de Java.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Travailler avec des annotations en filigrane dans des fichiers PDF à l'aide de Java
Abstract: Cet article explique comment créer, inspecter et supprimer des annotations en filigrane dans des documents PDF à l'aide de Java. Il couvre l'ajout d'une annotation de filigrane de texte avec un état et une opacité de texte personnalisés, la lecture des zones d'annotation de filigrane existantes et la suppression des annotations de filigrane.
---
## Ajouter une annotation en filigrane


1. 
Ouvrez le PDF d'entrée et définissez le rectangle où l'annotation en filigrane sera placée.

2. 
Créez le `WatermarkAnnotation`, ajoutez-le à la page et configurez l'état et l'opacité du texte du filigrane.

3. 
Appliquez les lignes de texte en filigrane et enregistrez le PDF modifié.

```java
public static void watermarkAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        WatermarkAnnotation watermarkAnnotation = new WatermarkAnnotation(
                document.getPages().get_Item(1), new Rectangle(100, 0, 400, 100, true));

        document.getPages().get_Item(1).getAnnotations().add(watermarkAnnotation);

        TextState textState = new TextState();
        textState.setForegroundColor(Color.getBlue());
        textState.setFontSize(25);
        textState.setFont(FontRepository.findFont("Arial"));

        watermarkAnnotation.setOpacity(0.5);
        watermarkAnnotation.setTextAndState(new String[]{"HELLO", "Line 1", "Line 2"}, textState);

        document.save(outputFile.toString());
    }
}
```
