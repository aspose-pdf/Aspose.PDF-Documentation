---
title: Gérer les en-têtes et pieds de page PDF à l'aide de Java
linktitle: Gérer les en-têtes et pieds de page PDF
type: docs
weight: 70
url: /java/artifacts-header-footer/
description: Découvrez comment ajouter et supprimer des artefacts d'en-tête et de pied de page dans des documents PDF à l'aide d'Aspose.PDF pour Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Comment ajouter, personnaliser et supprimer des en-têtes et pieds de page PDF à l'aide de Java
Abstract: Cet article explique comment gérer les artefacts d'en-tête et de pied de page dans les documents PDF à l'aide d'Aspose.PDF pour Java. Il couvre la création d'objets `HeaderArtifact` et `FooterArtifact` réutilisables avec un état et un alignement de texte personnalisés, leur ajout à une page et la suppression des artefacts d'en-tête et de pied de page existants.
---
Les artefacts d'en-tête et de pied de page sont des éléments de pagination hors contenu couramment utilisés pour les étiquettes répétées, les identifiants de page et le cadrage de mise en page.


## 
Créer un artefact d'en-tête



Utilisez cette assistante lorsque vous avez besoin d’un artefact d’en-tête réutilisable avec un style et un alignement de texte cohérents.


1. 
Create a [HeaderArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/headerartifact/).

1. 
Définissez son texte, ses paramètres de police et sa couleur de premier plan.
1. Configurez l'alignement horizontal et renvoyez l'artefact.


```java
public static HeaderArtifact createHeaderArtifact(String text) {
    HeaderArtifact artifact = new HeaderArtifact();
    artifact.setText(text);
    artifact.getTextState().setFontSize(14);
    artifact.getTextState().setFont(FontRepository.findFont("Arial"));
    artifact.getTextState().setForegroundColor(Color.getNavy());
    artifact.setArtifactHorizontalAlignment(HorizontalAlignment.Center);
    return artifact;
}
```

## 
Créer un artefact de pied de page



Cet assistant crée un artefact de pied de page réutilisable avec le même modèle de style que l'artefact d'en-tête.


1. 
Créez un [FooterArtifact] (https://reference.aspose.com/pdf/java/com.aspose.pdf/footerartifact/).

1. 
Définissez son texte, son état et sa couleur de premier plan.
1. Configurez l'alignement et renvoyez l'artefact.


```java
public static FooterArtifact createFooterArtifact(String text) {
    FooterArtifact artifact = new FooterArtifact();
    artifact.setText(text);
    artifact.getTextState().setFontSize(14);
    artifact.getTextState().setFont(FontRepository.findFont("Arial"));
    artifact.getTextState().setForegroundColor(Color.getNavy());
    artifact.setArtifactHorizontalAlignment(HorizontalAlignment.Center);
    return artifact;
}
```

## 
Ajouter un artefact d'en-tête



Utilisez cet exemple lorsqu'une page doit afficher un artefact d'en-tête réutilisable.


1. 
Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Créez l'artefact d'en-tête via la méthode d'assistance.
1. Ajoutez l'artefact à la page et enregistrez le fichier de sortie.


```java
public static void addHeaderArtifact(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        HeaderArtifact header = createHeaderArtifact("Sample Header");
        document.getPages().get_Item(1).getArtifacts().add(header);
        document.save(outputFile.toString());
    }
}
```

## 
Ajouter un artefact de pied de page



Utilisez cet exemple lorsque la page doit afficher un artefact de pied de page avec une mise en forme réutilisable.


1. 
Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Créez l'artefact de pied de page via la méthode d'assistance.
1. Ajoutez l'artefact à la page et enregistrez le fichier de sortie.


```java
public static void addFooterArtifact(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        FooterArtifact footer = createFooterArtifact("Sample Footer");
        document.getPages().get_Item(1).getArtifacts().add(footer);
        document.save(outputFile.toString());
    }
}
```

## 
Supprimer les artefacts d'en-tête et de pied de page



Utilisez cette approche lorsque les artefacts d’en-tête et de pied de page existants doivent être supprimés de la page.


1. 
Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Parcourez la collection d’artefacts de page dans l’ordre inverse.
1. Supprimez les artefacts de pagination dont le sous-type est en-tête ou pied de page, puis enregistrez le document.

```java
public static void deleteHeaderFooterArtifact(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (int i = document.getPages().get_Item(1).getArtifacts().size(); i >= 1; i--) {
            Artifact artifact = document.getPages().get_Item(1).getArtifacts().get_Item(i);
            if (artifact.getType() == Artifact.ArtifactType.Pagination
                    && (artifact.getSubtype() == Artifact.ArtifactSubtype.Header
                    || artifact.getSubtype() == Artifact.ArtifactSubtype.Footer)) {
                document.getPages().get_Item(1).getArtifacts().delete(artifact);
            }
        }

        document.save(outputFile.toString());
    }
}
```
