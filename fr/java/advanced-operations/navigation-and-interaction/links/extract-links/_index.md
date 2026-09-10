---
title: Extraire des liens PDF en Java
linktitle: Extraire les liens
type: docs
weight: 30
url: /java/extract-links/
description: Découvrez comment extraire des annotations de liens et des hyperliens à partir de documents PDF en Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Extraire les annotations de lien et les cibles URI des fichiers PDF avec Java
Abstract: Cet article explique comment extraire des annotations de lien à partir de documents PDF à l'aide d'Aspose.PDF pour Java. Il montre comment énumérer les annotations de lien sur une page, lire leur index et leur rectangle de page et extraire les cibles URI des instances GoToURIAction.
---
Vous pouvez inspecter les liens PDF en parcourant les annotations de page et en filtrant `AnnotationType.Link`.


## 
Extraire les annotations du lien



Utilisez cet exemple lorsque vous avez besoin des informations d'emplacement et de page pour les annotations de lien sur une page.


1. 
Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Parcourez les annotations de page et filtrez les annotations de lien.
1. Lisez l'index de la page et le rectangle pour chaque lien correspondant.


```java
public static void extractLinkAnnotation(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Link && annotation instanceof LinkAnnotation) {
                LinkAnnotation linkAnnotation = (LinkAnnotation) annotation;
                System.out.println("Page: " + linkAnnotation.getPageIndex()
                        + ", location: " + linkAnnotation.getRect());
            }
        }
    }
}
```

## 
Extraire les destinations des hyperliens



Utilisez cet exemple lorsque vous devez lire les URI cibles à partir des annotations de liens Web.


1. 
Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Recherchez les objets [LinkAnnotation] (https://reference.aspose.com/pdf/java/com.aspose.pdf/linkannotation/) dont l'action est une [GoToURIAction] (https://reference.aspose.com/pdf/java/com.aspose.pdf/gotouriaction/).
1. Imprimez l'index de la page et la cible URI pour chaque lien hypertexte.

```java
public static void extractHyperlinks(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Link && annotation instanceof LinkAnnotation) {
                LinkAnnotation linkAnnotation = (LinkAnnotation) annotation;
                if (linkAnnotation.getAction() instanceof GoToURIAction) {
                    GoToURIAction action = (GoToURIAction) linkAnnotation.getAction();
                    System.out.println("Page " + linkAnnotation.getPageIndex() + ", URI:" + action.getURI());
                }
            }
        }
    }
}
```
