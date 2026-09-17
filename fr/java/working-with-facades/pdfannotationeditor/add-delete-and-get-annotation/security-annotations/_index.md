---
title: Annotations de sécurité utilisant Java
linktitle: Annotations de sécurité
type: docs
weight: 60
url: /java/pdfannotationeditor-class/security-annotations/
description: Découvrez comment marquer du texte à rédiger, appliquer des annotations de rédaction et rédiger des zones de page sélectionnées dans des fichiers PDF à l'aide de Java.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Rédigez du contenu PDF sensible en Java avec des annotations de sécurité
Abstract: Cet article explique comment utiliser les annotations de rédaction dans les documents PDF à l'aide de Java. Il couvre le marquage du texte correspondant avec des annotations de rédaction, l'application permanente de rédactions et la rédaction de zones sélectionnées en fonction des rectangles de placement d'image détectés.
---
## Marquer le texte pour rédaction


1. 
Chargez le PDF et recherchez dans toutes les pages le texte qui doit être rédigé.

2. 
Créez un `RedactionAnnotation` pour chaque fragment de texte correspondant et configurez son apparence.

3. 
Ajoutez les annotations de rédaction à leurs pages et enregistrez le document.

```java
public static void markTextRedaction(Path inputFile, Path outputFile, String searchTerm) {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber(searchTerm);
        TextSearchOptions textSearchOptions = new TextSearchOptions(true);
        textFragmentAbsorber.setTextSearchOptions(textSearchOptions);
        document.getPages().accept(textFragmentAbsorber);

        for (TextFragment textFragment : textFragmentAbsorber.getTextFragments()) {
            Page page = textFragment.getPage();
            Rectangle annotationRectangle = textFragment.getRectangle();
            RedactionAnnotation annotation = new RedactionAnnotation(page, annotationRectangle);
            annotation.setFillColor(Color.getGray());
            annotation.setBorderColor(Color.getRed());
            annotation.setColor(Color.getWhite());
            annotation.setOverlayText("REDACTED");
            annotation.setTextAlignment(HorizontalAlignment.Center);
            annotation.setRepeat(true);
            page.getAnnotations().add(annotation, true);
        }

        document.save(outputFile.toString());
    }
}
```
