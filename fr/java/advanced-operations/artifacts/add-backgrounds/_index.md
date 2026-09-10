---
title: Ajouter des arrière-plans PDF en Java
linktitle: Ajout d'arrière-plans
type: docs
weight: 20
url: /java/add-backgrounds/
description: Découvrez comment ajouter une image d'arrière-plan ou une couleur d'arrière-plan aux pages PDF en Java en utilisant `BackgroundArtifact` avec Aspose.PDF.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Comment ajouter un arrière-plan au PDF avec Java
Abstract: Cet article explique comment ajouter ou supprimer des arrière-plans de pages PDF en Java à l'aide d'Aspose.PDF. Il couvre l'ajout d'une image d'arrière-plan, le réglage de l'opacité de l'image, l'application d'une couleur d'arrière-plan et la suppression des artefacts d'arrière-plan d'une page.
---
Les artefacts d'arrière-plan vous permettent de placer des éléments visuels hors contenu derrière le contenu de la page principale sans modifier le texte logique du document.


## 
Ajouter une image d'arrière-plan à un PDF



Utilisez cet exemple lorsque la page doit afficher une image comme artefact d’arrière-plan.


1. 
Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) et le flux d'entrée de l'image.

1. 
Créez un [BackgroundArtifact] (https://reference.aspose.com/pdf/java/com.aspose.pdf/backgroundartifact/) et attribuez le flux d'images.
1. Ajoutez l'artefact à la page cible et enregistrez le PDF de sortie.


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

## 
Ajouter une image de fond avec opacité



Cet exemple place une image d'arrière-plan semi-transparente derrière le contenu de la page.


1. 
Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) et le flux d'images.

1. 
Créez un [BackgroundArtifact] (https://reference.aspose.com/pdf/java/com.aspose.pdf/backgroundartifact/), attribuez l'image et définissez l'opacité.
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

## 
Ajouter une couleur d'arrière-plan à un PDF



Utilisez cet exemple lorsque la page doit utiliser une couleur d’arrière-plan unie au lieu d’une image.


1. 
Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Créez un [BackgroundArtifact] (https://reference.aspose.com/pdf/java/com.aspose.pdf/backgroundartifact/) et attribuez la couleur d'arrière-plan.
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

## 
Supprimer les artefacts d'arrière-plan



Utilisez cette approche lorsque les artefacts d’arrière-plan existants doivent être supprimés de la page.


1. 
Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Parcourez la collection d’artefacts de page dans l’ordre inverse.
1. Supprimez les artefacts dont le type est la pagination et le sous-type est l'arrière-plan, puis enregistrez le document.

```java
public static void removeBackground(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (int i = document.getPages().get_Item(1).getArtifacts().size(); i >= 1; i--) {
            Artifact artifact = document.getPages().get_Item(1).getArtifacts().get_Item(i);
            if (artifact.getType() == Artifact.ArtifactType.Pagination
                    && artifact.getSubtype() == Artifact.ArtifactSubtype.Background) {
                document.getPages().get_Item(1).getArtifacts().delete(artifact);
            }
        }

        document.save(outputFile.toString());
    }
}
```
