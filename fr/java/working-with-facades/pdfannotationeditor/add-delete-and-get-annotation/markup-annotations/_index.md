---
title: Annotations de balisage utilisant Java
linktitle: Annotations de balisage
type: docs
weight: 20
url: /java/pdfannotationeditor-class/markup-annotations/
description: Découvrez comment ajouter, inspecter et supprimer des annotations surlignées, soulignées, ondulées et barrées dans des documents PDF à l'aide de Java.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Travailler avec des annotations de balisage dans des fichiers PDF à l'aide de Java
Abstract: Cet article explique comment créer, inspecter et supprimer des annotations de balisage de texte dans des documents PDF à l'aide de Java. Il couvre les annotations surlignées, soulignées, ondulées et barrées basées sur les exemples Java du référentiel.
---
## Ajouter des annotations surlignées, soulignées, ondulées ou barrées


1. 
Ouvrez le PDF d'entrée et sélectionnez la zone de page où l'annotation de balisage doit apparaître.

2. 
Créez le type d'annotation requis et configurez ses métadonnées ou ses propriétés visuelles.

3. 
Ajoutez l'annotation à la collection de pages et enregistrez le document.

```java
public static void addTextHighlightAnnotation(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        HighlightAnnotation highlightAnnotation = new HighlightAnnotation(
                document.getPages().get_Item(1), new Rectangle(300, 750, 320, 770, true));
        document.getPages().get_Item(1).getAnnotations().add(highlightAnnotation);
        document.save(outputFile.toString());
    }
}
```

```java
public static void addTextUnderlineAnnotation(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        UnderlineAnnotation underlineAnnotation = new UnderlineAnnotation(
                document.getPages().get_Item(1), new Rectangle(299.988, 713.664, 308.708, 720.769, true));
        underlineAnnotation.setTitle("Aspose User");
        underlineAnnotation.setSubject("Inserted Underline 1");
        underlineAnnotation.setFlags(AnnotationFlags.Print);
        underlineAnnotation.setColor(Color.getBlue());
        document.getPages().get_Item(1).getAnnotations().add(underlineAnnotation);
        document.save(outputFile.toString());
    }
}
```
