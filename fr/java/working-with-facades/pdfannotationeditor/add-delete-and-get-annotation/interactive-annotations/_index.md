---
title: Annotations interactives utilisant Java
linktitle: Annotations interactives
type: docs
weight: 30
url: /java/pdfannotationeditor-class/interactive-annotations/
description: Découvrez comment ajouter, inspecter et supprimer des annotations de lien dans des documents PDF à l'aide de Java.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Travailler avec des annotations PDF interactives en Java
Abstract: Cet article explique comment utiliser des annotations de liens interactifs dans des fichiers PDF à l'aide de Java. Il couvre la localisation du texte, la création d'une annotation de lien sur la zone de texte correspondante, la lecture des annotations de lien existantes et leur suppression.
---
## Ajouter une annotation de lien


1. 
Chargez le document PDF source et recherchez le texte cible dans la première page.

2. 
Utilisez le rectangle de texte correspondant pour créer un `LinkAnnotation` et attribuer l'URI de destination.

3. 
Ajoutez l'annotation à la page et enregistrez le PDF mis à jour.

```java
public static void linkAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("file");
        document.getPages().get_Item(1).accept(textFragmentAbsorber);

        TextFragment phoneNumberFragment = textFragmentAbsorber.getTextFragments().get_Item(1);

        LinkAnnotation linkAnnotation = new LinkAnnotation(
                document.getPages().get_Item(1), phoneNumberFragment.getRectangle());
        linkAnnotation.setAction(new GoToURIAction("www.aspose.com"));

        document.getPages().get_Item(1).getAnnotations().add(linkAnnotation);
        document.save(outputFile.toString());
    }
}
```
