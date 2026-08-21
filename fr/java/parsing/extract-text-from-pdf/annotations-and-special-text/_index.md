---
title: Annotations et textes spéciaux utilisant Java
linktitle: Annotations et textes spéciaux
type: docs
weight: 40
url: /java/annotation-and-special-text/
description: Découvrez comment extraire le texte des annotations de tampon, du texte en surbrillance et du contenu en exposant ou en indice dans des documents PDF à l'aide d'Aspose.PDF pour Java.
lastmod: "2026-06-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
## 
Extraire le texte en surbrillance



Parcourez les annotations de page et lisez le texte marqué à partir de `HighlightAnnotation`.

1. Ouvrez le PDF source dans une instance [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Parcourez les objets [Annotation] (https://reference.aspose.com/pdf/java/com.aspose.pdf/annotation/) sur la [Page] cible (https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).

1. 
Vérifiez si chaque annotation est une [HighlightAnnotation] (https://reference.aspose.com/pdf/java/com.aspose.pdf/highlightannotation/) avant de la convertir en classe d'annotation typée.

1. 
Lisez le texte marqué de chaque annotation de surbrillance et imprimez-le sur la console.


```java
public static void extractHighlightedText(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation instanceof HighlightAnnotation) {
                HighlightAnnotation highlightAnnotation = (HighlightAnnotation) annotation;
                System.out.println(highlightAnnotation.getMarkedText());
            }
        }
    }
}
```

## 
Extraire le texte des annotations du tampon

Lisez le flux d'apparence normale à partir d'une annotation de tampon et transmettez-le via `TextAbsorber`.


1. 
Ouvrez le PDF source dans une instance [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Parcourez les objets [Annotation] (https://reference.aspose.com/pdf/java/com.aspose.pdf/annotation/) sur la [Page] cible (https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).

1. 
Filtrez les annotations sur celles dont le type est `Stamp`.

1. 
Créez un [TextAbsorber] (https://reference.aspose.com/pdf/java/com.aspose.pdf/textabsorber/) et demandez l'entrée d'apparence normale à partir du dictionnaire d'apparence d'annotation de tampon.
1. Visitez l'apparence [XForm] (https://reference.aspose.com/pdf/java/com.aspose.pdf/xform/) et imprimez le texte extrait.


```java
public static void extractStampText(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Stamp) {
                TextAbsorber absorber = new TextAbsorber();
                Object[] xforms = new Object[1];
                if (annotation.getAppearance().tryGetValue("N", xforms) && xforms[0] instanceof XForm) {
                    absorber.visit((XForm) xforms[0]);
                    System.out.println(absorber.getText());
                }
            }
        }
    }
}
```

## 
Extraire les détails du texte en exposant et en indice



Utilisez `TextFragmentAbsorber` lorsque vous avez besoin à la fois du texte extrait et des indicateurs en exposant ou en indice sur chaque fragment.


1. 
Ouvrez le PDF source dans une instance [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Créez un [TextFragmentAbsorber] (https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragmentabsorber/) pour l'analyse de texte au niveau des fragments.
1. Visitez la [Page] cible (https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) et récupérez ses objets [TextFragment] (https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/).

1. 
Parcourez ces fragments et lisez le texte avec les indicateurs en exposant et en indice de `fragment.getTextState()`.

1. 
Écrivez les détails extraits dans le fichier de sortie.

```java
public static void extractSuperSubDetails(Path inputFile, Path outputFile, int pageNumber) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber absorber = new TextFragmentAbsorber();
        document.getPages().get_Item(pageNumber).accept(absorber);
        StringBuilder details = new StringBuilder();
        for (TextFragment fragment : absorber.getTextFragments()) {
            details.append("Text: '").append(fragment.getText())
                    .append("' | Superscript: ").append(fragment.getTextState().isSuperscript())
                    .append(" | Subscript: ").append(fragment.getTextState().isSubscript())
                    .append(System.lineSeparator());
        }
        Files.writeString(outputFile, details.toString());
    }
}
```
