---
title: Ajouter des arrière-plans PDF en Java
linktitle: Ajouter des arrière-plans
type: docs
weight: 20
url: /fr/java/add-backgrounds/
description: Ajouter des arrière-plans d'image et de couleur unie aux pages PDF en Java et ajuster l'opacité de l'image.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Ajouter des arrière-plans en Java
Abstract: Ajouter des arrière-plans d'image et de couleur unie aux pages PDF en Java et ajuster l'opacité de l'image.
---
Les artefacts d'arrière-plan vous permettent de placer des éléments visuels non contenus derrière le contenu principal de la page sans modifier le texte logique du document.

## Ajoutez une image d'arrière-plan à un PDF

Utilisez cet exemple lorsque la page doit afficher une image en tant qu'artefact d'arrière-plan.

1. Ouvrez le PDF source avec [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) et ouvrez le flux d’image.
1. Créez un [BackgroundArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/backgroundartifact/) et attribuez le flux d'image.
1. Ajoutez l’artefact à la page cible et enregistrez le PDF de sortie.

```java
public static void addBackgroundImageToPdf(Path inputFile, Path imageFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString());
         InputStream imageStream = Files.newInputStream(imageFile)) {
        BackgroundArtifact artifact = new BackgroundArtifact();
        artifact.setBackgroundImage(imageStream);
        document.getPages().get_Item(1).getArtifacts().add(artifact);
        document.save(outputFile.toString());
    }
}
```

## Ajouter une image d'arrière-plan avec opacité

Cet exemple place une image d'arrière-plan semi-transparente derrière le contenu de la page.

1. Ouvrez le PDF source avec [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) et ouvrez le flux d’image.
1. Créez un [BackgroundArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/backgroundartifact/), assignez l'image, et définissez l'opacité.
1. Ajoutez l'artefact à la page et enregistrez le document.

```java
public static void addBackgroundImageWithOpacityToPdf(Path inputFile, Path imageFile, Path outputFile)
        throws Exception {
    try (Document document = new Document(inputFile.toString());
         InputStream imageStream = Files.newInputStream(imageFile)) {
        BackgroundArtifact artifact = new BackgroundArtifact();
        artifact.setBackgroundImage(imageStream);
        artifact.setOpacity(0.5);
        document.getPages().get_Item(1).getArtifacts().add(artifact);
        document.save(outputFile.toString());
    }
}
```

## Ajouter une couleur d'arrière-plan à un PDF

Utilisez cet exemple lorsque la page doit utiliser une couleur d'arrière-plan unie au lieu d'une image.

1. Ouvrez le PDF source avec [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Créez un [BackgroundArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/backgroundartifact/) et attribuez la couleur d'arrière-plan.
1. Ajoutez l'artefact à la page et enregistrez le fichier de sortie.

```java
public static void addBackgroundColorToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        BackgroundArtifact artifact = new BackgroundArtifact();
        artifact.setBackgroundColor(Color.getDarkKhaki().toRgb());
        document.getPages().get_Item(1).getArtifacts().add(artifact);
        document.save(outputFile.toString());
    }
}
```

## Rubriques connexes

- [Supprimer les arrière-plans](/pdf/fr/java/remove-backgrounds/)
- [Travailler avec les artefacts PDF en Java](/pdf/fr/java/artifacts/)
