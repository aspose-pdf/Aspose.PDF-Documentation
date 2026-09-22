---
title: Exemple Hello World en Java
linktitle: Exemple Hello World
type: docs
weight: 20
url: /java/hello-world-example/
description: Cet exemple montre comment créer un document PDF simple avec le texte Hello World mis en forme à l'aide d'Aspose.PDF for Java.
lastmod: "2026-09-21"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Exemple Hello World en Java
Abstract: Cet article fournit un exemple Hello World pour Aspose.PDF for Java. L'exemple crée un nouveau document PDF, ajoute une page, crée un TextFragment avec une position, une police et des couleurs personnalisées, ajoute le texte à la page avec TextBuilder et enregistre le résultat sous forme de fichier PDF.
---
Un exemple « Hello World » permet de découvrir les étapes de base de la création d’un PDF. Dans cet article, l'exemple crée un nouveau PDF, place un fragment de texte mis en forme sur la page et enregistre le fichier de sortie.

L'exemple Java suit ces étapes :

1. Créez un objet [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. Ajoutez une [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) au document.

1. Créez un objet [`TextFragment`](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/) avec le texte `Hello, world!`.
1. Définissez la position du fragment avec [`Position`](https://reference.aspose.com/pdf/java/com.aspose.pdf/position/), puis sa police, sa taille de police et ses couleurs d’arrière-plan et de premier plan avec [`TextState`](https://reference.aspose.com/pdf/java/com.aspose.pdf/textstate/).

1. Créez un objet [`TextBuilder`](https://reference.aspose.com/pdf/java/com.aspose.pdf/textbuilder/) pour la page.

1. Ajoutez le [`TextFragment`](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/) à la [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).

1. Enregistrez le [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) au format PDF.

Le code Java suivant est basé sur `GetStartedExamples.java`.

```java
public static void simpleExample(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        TextFragment textFragment = new TextFragment("Hello, world!");
        textFragment.setPosition(new Position(100, 600));
        textFragment.getTextState().setFontSize(12);
        textFragment.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));
        textFragment.getTextState().setBackgroundColor(Color.getBlue());
        textFragment.getTextState().setForegroundColor(Color.getYellow());

        TextBuilder textBuilder = new TextBuilder(page);
        textBuilder.appendText(textFragment);

        document.save(outputFile.toString());
    }
}
```
