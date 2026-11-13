---
title: Ajouter des filigranes au PDF en Java
linktitle: Ajouter des filigranes
type: docs
weight: 30
url: /fr/java/add-watermarks/
description: Ajouter des artefacts de filigrane de texte stylisé aux pages PDF en Java.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Ajouter des filigranes en Java
Abstract: Ajouter des artefacts de filigrane de texte stylisé aux pages PDF en Java.
---
Les artefacts de filigrane vous permettent de placer des marques visuelles persistantes sur une page sans les mélanger au contenu principal du document.

## Ajouter un artefact de filigrane

Utilisez cet exemple lorsque la page doit afficher un filigrane texte centré avec une rotation personnalisée, une opacité et un placement en arrière-plan.

1. Ouvrez le PDF source avec [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Créez un [WatermarkArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/watermarkartifact/) et configurez ses paramètres d'état du texte et de placement.
1. Ajoutez le filigrane à la page et enregistrez le fichier de sortie.

```java
public static void addWatermarkArtifact(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextState textState = new TextState();
        textState.setFontSize(72);
        textState.setForegroundColor(Color.getBlueViolet());
        textState.setFontStyle(FontStyles.Bold);
        textState.setFont(FontRepository.findFont("Arial"));

        WatermarkArtifact watermark = new WatermarkArtifact();
        watermark.setTextAndState("WATERMARK", textState);
        watermark.setArtifactHorizontalAlignment(HorizontalAlignment.Center);
        watermark.setArtifactVerticalAlignment(VerticalAlignment.Center);
        watermark.setRotation(60);
        watermark.setOpacity(0.2);
        watermark.setBackground(true);

        document.getPages().get_Item(1).getArtifacts().add(watermark);
        document.save(outputFile.toString());
    }
}
```

## Rubriques connexes

- [Extraire les détails du filigrane](/pdf/fr/java/extract-watermarks/)
- [Supprimer les filigranes](/pdf/fr/java/remove-watermarks/)
- [Travailler avec les artefacts PDF en Java](/pdf/fr/java/artifacts/)
