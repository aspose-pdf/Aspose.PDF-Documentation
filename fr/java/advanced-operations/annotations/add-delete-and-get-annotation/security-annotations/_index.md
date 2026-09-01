---
title: Annotations de sécurité utilisant Java
linktitle: Annotations de sécurité
type: docs
weight: 75
url: /java/security-annotations/
description: Découvrez comment marquer du texte à rédiger, appliquer des annotations de rédaction et rédiger des zones de page sélectionnées dans des fichiers PDF à l'aide d'Aspose.PDF pour Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Rédigez du contenu PDF sensible en Java avec des annotations de sécurité.
Abstract: Cet article explique comment utiliser les annotations de rédaction dans les documents PDF à l'aide d'Aspose.PDF pour Java. Il couvre le marquage du texte correspondant avec des annotations de rédaction, l'application permanente de rédactions et la rédaction de zones sélectionnées en fonction des rectangles de placement d'image détectés.
---
Les flux de travail d'annotation de sécurité de cette section se concentrent sur la préparation et l'application de suppressions au contenu PDF sensible.


## 
Marquer le texte avec des annotations de rédaction



Utilisez cet exemple lorsque le texte correspondant doit être couvert par des annotations de rédaction avant que la rédaction soit appliquée de manière permanente.


1. 
Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Recherchez le texte cible et créez une [RedactionAnnotation] (https://reference.aspose.com/pdf/java/com.aspose.pdf/redactionannotation/) pour chaque correspondance.
1. Configurez l'apparence de la rédaction et enregistrez le document.


```java
public static void markTextRedaction(Path inputFile, Path outputFile, String searchTerm) {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber(searchTerm);
        TextSearchOptions textSearchOptions = new TextSearchOptions(true);
        textFragmentAbsorber.setTextSearchOptions(textSearchOptions);
        document.getPages().accept(textFragmentAbsorber);

        for (var textFragment : textFragmentAbsorber.getTextFragments()) {
            Page page = textFragment.getPage();
            RedactionAnnotation redactionAnnotation = new RedactionAnnotation(page, textFragment.getRectangle());
            redactionAnnotation.setFillColor(Color.getGray());
            redactionAnnotation.setBorderColor(Color.getRed());
            redactionAnnotation.setColor(Color.getWhite());
            redactionAnnotation.setOverlayText("REDACTED");
            redactionAnnotation.setTextAlignment(HorizontalAlignment.Center);
            redactionAnnotation.setRepeat(true);
            page.getAnnotations().add(redactionAnnotation, true);
        }
        document.save(outputFile.toString());
    }
}
```

## 
Appliquer les rédactions existantes



Cet exemple applique de manière permanente les annotations de rédaction qui existent déjà sur la page.


1. 
Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Collectez les annotations de type [AnnotationType] (https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/).`Redaction`.
1. Appelez `redact()` sur chaque annotation collectée et enregistrez le fichier mis à jour.


```java
public static void applyRedaction(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        List<RedactionAnnotation> redactionAnnotations = new ArrayList<>();
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Redaction) {
                redactionAnnotations.add((RedactionAnnotation) annotation);
            }
        }
        for (RedactionAnnotation redactionAnnotation : redactionAnnotations) {
            redactionAnnotation.redact();
        }
        document.save(outputFile.toString());
    }
}
```

## 
Rédiger une zone de page sélectionnée



Utilisez cette approche lorsque le contenu cible est identifié par position plutôt que par correspondance de texte.


1. 
Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Détectez le rectangle cible sur la page, par exemple à partir d'un placement d'image.
1. Créez une [RedactionAnnotation] (https://reference.aspose.com/pdf/java/com.aspose.pdf/redactionannotation/) pour cette zone et enregistrez le document.


```java
public static void redactArea(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        ImagePlacementAbsorber imagePlacementAbsorber = new ImagePlacementAbsorber();
        Page page = document.getPages().get_Item(1);
        page.accept(imagePlacementAbsorber);

        com.aspose.pdf.Rectangle targetRect = imagePlacementAbsorber.getImagePlacements().get_Item(2).getRectangle();
        RedactionAnnotation redactionAnnotation = new RedactionAnnotation(page, targetRect);
        redactionAnnotation.setFillColor(Color.getGray());
        redactionAnnotation.setBorderColor(Color.getRed());
        redactionAnnotation.setColor(Color.getWhite());
        redactionAnnotation.setOverlayText("REDACTED");
        redactionAnnotation.setTextAlignment(HorizontalAlignment.Center);
        redactionAnnotation.setRepeat(true);

        page.getAnnotations().add(redactionAnnotation, true);
        document.save(outputFile.toString());
    }
}
```

## 
Sujets d'annotations associés


- 
[Annotations interactives] (/pdf/java/interactive-annotations/)

- 
[Annotations de balisage] (/pdf/java/markup-annotations/)

- 
[Annotations de forme] (/pdf/java/shape-annotations/)
- [Annotations de texte] (/pdf/java/text-based-annotations/)

- 
[Annotations en filigrane] (/pdf/java/watermark-annotations/)

- 
[Importer et exporter des annotations] (/pdf/java/import-export-annotations/)
