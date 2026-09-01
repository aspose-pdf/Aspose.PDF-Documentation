---
title: Ajouter des filigranes au PDF en Java
linktitle: Ajout d'un filigrane
type: docs
weight: 30
url: /java/add-watermarks/
description: Découvrez comment ajouter, extraire et supprimer des artefacts de filigrane dans des fichiers PDF à l'aide d'Aspose.PDF pour Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Comment ajouter un filigrane au PDF avec Java
Abstract: Cet article explique comment ajouter, inspecter et supprimer des artefacts de filigrane dans des documents PDF à l'aide d'Aspose.PDF pour Java. Il couvre la création d'un filigrane de texte avec les paramètres d'alignement, de rotation, d'opacité et d'arrière-plan, l'inspection des artefacts de filigrane sur une page et leur suppression.
---
Les artefacts de filigrane vous permettent de placer des marquages ​​visuels persistants sur une page sans les mélanger au contenu principal du document.


## 
Extraire les artefacts de filigrane d'un PDF



Utilisez cet exemple lorsque vous devez inspecter des artefacts de filigrane existants et lire leur texte ou leur position.


1. 
Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Parcourez la collection d’artefacts de la page cible.
1. Filtrez les artefacts de pagination des filigranes et imprimez leur texte et leurs rectangles.


```java
public static void extractWatermarkFromPdf(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Artifact artifact : document.getPages().get_Item(1).getArtifacts()) {
            if (artifact.getType() == Artifact.ArtifactType.Pagination
                    && artifact.getSubtype() == Artifact.ArtifactSubtype.Watermark) {
                System.out.println(artifact.getText() + " " + artifact.getRectangle());
            }
        }
    }
}
```

## 
Ajouter un artefact de filigrane



Utilisez cet exemple lorsque la page doit afficher un filigrane de texte centré avec une rotation, une opacité et un placement d'arrière-plan personnalisés.


1. 
Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Créez un [WatermarkArtifact] (https://reference.aspose.com/pdf/java/com.aspose.pdf/watermarkartifact/) et configurez son état du texte et ses paramètres de placement.
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

## 
Supprimer les artefacts de filigrane



Utilisez cette approche lorsque les artefacts de filigrane existants doivent être supprimés de la page.


1. 
Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Parcourez la collection d’artefacts de page dans l’ordre inverse.
1. Supprimez les artefacts de pagination dont le sous-type est un filigrane, puis enregistrez le document.

```java
public static void deleteWatermarkArtifact(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (int i = document.getPages().get_Item(1).getArtifacts().size(); i >= 1; i--) {
            Artifact artifact = document.getPages().get_Item(1).getArtifacts().get_Item(i);
            if (artifact.getType() == Artifact.ArtifactType.Pagination
                    && artifact.getSubtype() == Artifact.ArtifactSubtype.Watermark) {
                document.getPages().get_Item(1).getArtifacts().delete(artifact);
            }
        }

        document.save(outputFile.toString());
    }
}
```
