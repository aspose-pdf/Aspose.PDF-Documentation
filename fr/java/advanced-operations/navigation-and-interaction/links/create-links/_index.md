---
title: Créer des liens PDF en Java
linktitle: Créer des liens
type: docs
weight: 10
url: /java/create-links/
description: Découvrez comment créer des liens PDF internes, externes et distants en Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Créer des annotations de lien dans des fichiers PDF avec Java
Abstract: Cet article montre comment créer des annotations de lien à l'aide d'Aspose.PDF pour Java. Il couvre les actions de lancement, la navigation dans les documents à distance, la navigation dans les pages du document et les liens Web basés sur des URI en attachant des actions aux objets LinkAnnotation.
---
Aspose.PDF pour Java utilise `LinkAnnotation` avec un objet d'action pour définir le comportement des liens.


## 
Créer un lien de lancement-action



Utilisez cet exemple lorsqu'une annotation de lien doit lancer un fichier ou une cible externe.


1. 
Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) et sélectionnez la page cible.

1. 
Créez une [LinkAnnotation] (https://reference.aspose.com/pdf/java/com.aspose.pdf/linkannotation/) et configurez sa bordure et sa couleur.
1. Attribuez une [LaunchAction] (https://reference.aspose.com/pdf/java/com.aspose.pdf/launchaction/) et enregistrez le document.


```java
public static void createLinkAnnotationLaunchAction(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);

        LinkAnnotation link = new LinkAnnotation(page, new Rectangle(10, 580, 120, 600, true));
        Border border = new Border(link);
        border.setWidth(5);
        border.setDash(new Dash(1, 1));
        link.setBorder(border);
        link.setColor(Color.getGreen());
        link.setAction(new LaunchAction(document, inputFile.toString()));
        page.getAnnotations().add(link);
        document.save(outputFile.toString());
    }
}
```

## 
Créer un lien d'accès à distance



Utilisez cet exemple lorsque le lien doit ouvrir une page dans un autre document PDF.


1. 
Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Créez une [LinkAnnotation] (https://reference.aspose.com/pdf/java/com.aspose.pdf/linkannotation/) sur la page cible.
1. Attribuez un [GoToRemoteAction] (https://reference.aspose.com/pdf/java/com.aspose.pdf/gotoremoteaction/) et enregistrez le fichier de sortie.


```java
public static void createLinkAnnotationGoToRemoteAction(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);

        LinkAnnotation link = new LinkAnnotation(page, new Rectangle(10, 580, 120, 600, true));
        link.setColor(Color.getGreen());
        link.setAction(new GoToRemoteAction(inputFile.toString(), 1));
        page.getAnnotations().add(link);
        document.save(outputFile.toString());
    }
}
```

## 
Créer un lien de référence interne



Utilisez cet exemple lorsque le lien doit diriger vers une autre page du même document PDF.


1. 
Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Créez une [LinkAnnotation] (https://reference.aspose.com/pdf/java/com.aspose.pdf/linkannotation/) et configurez son apparence.
1. Attribuez un [GoToAction] (https://reference.aspose.com/pdf/java/com.aspose.pdf/gotoaction/) à la page de destination et enregistrez le document.


```java
public static void createLinkAnnotationGoToAction(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);

        LinkAnnotation link = new LinkAnnotation(page, new Rectangle(10, 580, 120, 600, true));
        Border border = new Border(link);
        border.setWidth(5);
        border.setDash(new Dash(1, 1));
        link.setBorder(border);
        link.setColor(Color.getGreen());
        if (document.getPages().size() >= 4) {
            link.setAction(new GoToAction(document.getPages().get_Item(4)));
        } else {
            link.setAction(new GoToAction(document.getPages().get_Item(document.getPages().size())));
        }
        page.getAnnotations().add(link);
        document.save(outputFile.toString());
    }
}
```

## 
Créer un lien URI



Utilisez cet exemple lorsque le lien doit ouvrir une ressource Web via une action URI.


1. 
Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Créez une [LinkAnnotation] (https://reference.aspose.com/pdf/java/com.aspose.pdf/linkannotation/) sur la page.
1. Attribuez une [GoToURIAction] (https://reference.aspose.com/pdf/java/com.aspose.pdf/gotouriaction/) et enregistrez le fichier de sortie.

```java
public static void createLinkAnnotationGoToUriAction(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);

        LinkAnnotation link = new LinkAnnotation(page, new Rectangle(10, 580, 120, 600, true));
        link.setColor(Color.getGreen());
        link.setAction(new GoToURIAction("https://docs.aspose.com/pdf/python"));
        page.getAnnotations().add(link);
        document.save(outputFile.toString());
    }
}
```
