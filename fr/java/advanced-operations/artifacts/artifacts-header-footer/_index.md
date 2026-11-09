---
title: Ajouter des en-têtes et pieds de page PDF en Java
linktitle: Ajouter des en-têtes et pieds de page
type: docs
weight: 70
url: /fr/java/artifacts-header-footer/
description: Créer des artefacts d'en-tête et de pied de page stylisés et les ajouter aux pages PDF en Java.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Ajouter des en-têtes et pieds de page en Java
Abstract: Créer des artefacts d'en-tête et de pied de page stylisés et les ajouter aux pages PDF en Java.
---
Les artefacts d’en-tête et de pied de page sont des éléments de pagination non liés au contenu, généralement utilisés pour des libellés répétés, des identifiants de page et le cadrage de la mise en page.

## Créer un artefact d’en-tête

Utilisez cet assistant lorsque vous avez besoin d’un artefact d’en-tête réutilisable avec une mise en forme et un alignement du texte cohérents.

1. Créez un [HeaderArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/headerartifact/).
1. Définissez son texte, les paramètres de police et la couleur de premier plan.
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

## Créer un artefact de pied de page

Cet assistant crée un artefact de pied de page réutilisable avec le même modèle de style que l'artefact d'en-tête.

1. Créez un [FooterArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/footerartifact/).
1. Définissez son texte, son état de texte et sa couleur de premier plan.
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

## Ajoutez un artefact d'en-tête

Utilisez cet exemple lorsqu’une page doit afficher un artefact d’en-tête réutilisable.

1. Ouvrez le PDF source avec [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Créez l’artefact d’en-tête à l’aide de la méthode utilitaire.
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

## Ajouter un artefact de pied de page

Utilisez cet exemple lorsque la page doit afficher un artefact de pied de page avec un formatage réutilisable.

1. Ouvrez le PDF source avec [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Créez l'artefact de pied de page via la méthode utilitaire.
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

## Rubriques connexes

- [Supprimer les en-têtes et les pieds de page](/pdf/fr/java/remove-headers-footers/)
- [Travailler avec les artefacts PDF en Java](/pdf/fr/java/artifacts/)
