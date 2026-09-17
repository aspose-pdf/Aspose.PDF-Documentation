---
title: Exemple de Hello World utilisant Java
linktitle: Bonjour tout le monde Exemple
type: docs
weight: 20
url: /java/hello-world-example/
description: Cet exemple montre comment créer un document PDF simple avec du texte Hello World stylisé à l'aide d'Aspose.PDF pour Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Exemple Hello World via Java
Abstract: Cet article fournit un exemple Hello World pour Aspose.PDF pour Java. L'exemple crée un nouveau document PDF, ajoute une page, crée un TextFragment avec une position, une police et des couleurs personnalisées, ajoute le texte à la page avec TextBuilder et enregistre le résultat sous forme de fichier PDF.
---
Un exemple « Hello World » est le chemin le plus court pour comprendre le flux de travail de base de création de PDF. Dans cet article, l'exemple crée un nouveau PDF, place un fragment de texte stylisé sur la page et enregistre le fichier de sortie.



L'exemple Java suit ces étapes :


1. 
Créez un objet [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Ajoutez une [Page] (https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) au document.

1. 
Créez un [TextFragment] (https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/) avec le texte `Hello, world!`.
1. Définissez la [Position] (https://reference.aspose.com/pdf/java/com.aspose.pdf/position/), la police, la taille de la police, la couleur d'arrière-plan et la couleur de premier plan via le fragment [TextState] (https://reference.aspose.com/pdf/java/com.aspose.pdf/textstate/).

1. 
Créez un [TextBuilder] (https://reference.aspose.com/pdf/java/com.aspose.pdf/textbuilder/) pour la page.

1. 
Ajoutez le [TextFragment] (https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/) à la [Page] (https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).

1. 
Enregistrez le [Document] PDF (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).



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
