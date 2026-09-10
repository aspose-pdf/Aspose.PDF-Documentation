---
title: Annotations basées sur du texte utilisant Java
linktitle: Annotations de texte
type: docs
weight: 10
url: /java/pdfannotationeditor-class/text-based-annotations/
description: Découvrez comment ajouter, inspecter et supprimer du texte, du texte libre et des annotations barrées dans des documents PDF à l'aide de Java.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Travailler avec des annotations PDF texte en Java
Abstract: Cet article explique comment créer, lire et supprimer des annotations textuelles dans des documents PDF à l'aide de Java. Il couvre les annotations de texte, les annotations de texte libre et les annotations barrées basées sur les exemples d'implémentation Java.
---
## Ajouter une annotation de texte


1. 
Ouvrez le PDF d'entrée et ciblez la page où l'annotation de texte doit être placée.

2. 
Créez le `TextAnnotation`, définissez son rectangle et définissez son titre, son sujet, ses drapeaux et sa couleur.

3. 
Ajoutez l'annotation à la page et enregistrez le document mis à jour.


```java
public static void textAnnotationAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextAnnotation textAnnotation = new TextAnnotation(
                document.getPages().get_Item(1), new Rectangle(299.988, 613.664, 428.708, 680.769, true));
        textAnnotation.setTitle("Aspose User");
        textAnnotation.setSubject("Inserted text 1");
        textAnnotation.setFlags(AnnotationFlags.Print);
        textAnnotation.setColor(Color.getBlue());

        document.getPages().get_Item(1).getAnnotations().add(textAnnotation, false);
        document.save(outputFile.toString());
    }
}
```

## 
Ajouter une annotation de texte libre

1. Chargez le PDF source et sélectionnez la page et le rectangle cibles pour la note en texte libre.

2. 
Créez le `FreeTextAnnotation`, initialisez son apparence par défaut et définissez le titre et la couleur.

3. 
Ajoutez l'annotation à la page et enregistrez le résultat.

```java
public static void freeTextAnnotationAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        FreeTextAnnotation freeTextAnnotation = new FreeTextAnnotation(
                document.getPages().get_Item(1),
                new Rectangle(299, 713, 308, 720, true),
                new DefaultAppearance());
        freeTextAnnotation.setTitle("Aspose User");
        freeTextAnnotation.setColor(Color.getLightGreen());

        document.getPages().get_Item(1).getAnnotations().add(freeTextAnnotation);
        document.save(outputFile.toString());
    }
}
```
