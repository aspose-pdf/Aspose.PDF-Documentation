---
title: Mettre à jour les liens PDF en Java
linktitle: Mettre à jour les liens
type: docs
weight: 20
url: /java/update-links/
description: Découvrez comment mettre à jour l’apparence et les destinations des liens PDF en Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Mettre à jour l'apparence des annotations de lien et les destinations Web dans les fichiers PDF avec Java
Abstract: Cet article montre comment mettre à jour les annotations de liens existantes à l'aide d'Aspose.PDF pour Java. Les exemples montrent la modification de la couleur du texte couvert par un lien, la mise à jour de la couleur de l'annotation du lien et le remplacement de l'URI cible pour les liens Web.
---
Les liens existants peuvent être modifiés en recherchant l'annotation du lien sur une page et en mettant à jour son apparence ou son action.


## 
Mettre à jour la couleur du texte lié



Utilisez cet exemple lorsque la zone de texte couverte par une annotation de lien doit être recolorée.


1. 
Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Recherchez des annotations de lien et créez un rectangle de recherche de texte à partir de chaque zone d'annotation.
1. Recolorez les fragments de texte correspondants et enregistrez le document.


```java
public static void linkAnnotationUpdateTextColor(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Link) {
                TextFragmentAbsorber absorber = new TextFragmentAbsorber();
                Rectangle rect = annotation.getRect();
                rect.setLLX(rect.getLLX() - 2);
                rect.setLLY(rect.getLLY() - 2);
                rect.setURX(rect.getURX() + 2);
                rect.setURY(rect.getURY() + 2);
                absorber.setTextSearchOptions(new TextSearchOptions(rect));
                absorber.visit(document.getPages().get_Item(1));
                for (TextFragment textFragment : absorber.getTextFragments()) {
                    textFragment.getTextState().setForegroundColor(Color.getRed());
                }
            }
        }

        document.save(outputFile.toString());
    }
}
```

## 
Mettre à jour la couleur de la bordure du lien



Utilisez cet exemple lorsque la couleur visible des annotations de liens existantes doit être modifiée.


1. 
Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Parcourez les annotations de la page et filtrez les objets [LinkAnnotation] (https://reference.aspose.com/pdf/java/com.aspose.pdf/linkannotation/).
1. Mettez à jour la couleur de l'annotation du lien et enregistrez le document.


```java
public static void linkAnnotationUpdateBorder(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Link && annotation instanceof LinkAnnotation) {
                LinkAnnotation linkAnnotation = (LinkAnnotation) annotation;
                linkAnnotation.setColor(Color.getRed());
            }
        }

        document.save(outputFile.toString());
    }
}
```

## 
Mettre à jour une destination de lien Web



Utilisez cet exemple lorsqu'un lien Web existant doit pointer vers un nouvel URI.


1. 
Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Recherchez les annotations de lien dont l'action est une [GoToURIAction] (https://reference.aspose.com/pdf/java/com.aspose.pdf/gotouriaction/).
1. Remplacez l'URI et enregistrez le document mis à jour.

```java
public static void linkAnnotationUpdateWebDestination(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Link && annotation instanceof LinkAnnotation) {
                LinkAnnotation linkAnnotation = (LinkAnnotation) annotation;
                if (linkAnnotation.getAction() instanceof GoToURIAction) {
                    GoToURIAction action = (GoToURIAction) linkAnnotation.getAction();
                    action.setURI("https://www.aspose.com");
                }
            }
        }
        document.save(outputFile.toString());
    }
}
```
