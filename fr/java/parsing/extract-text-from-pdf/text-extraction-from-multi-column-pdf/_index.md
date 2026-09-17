---
title: Amélioration de l'extraction de texte à partir de PDF multicolonnes
linktitle: Extraction de texte à partir de PDF multicolonnes
type: docs
weight: 30
url: /java/text-extraction-from-multi-column-pdf/
description: Apprenez des techniques pour améliorer l'extraction de texte à partir de mises en page PDF multicolonnes avec Aspose.PDF pour Java.
lastmod: "2026-06-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Les mises en page multicolonnes nécessitent souvent un traitement supplémentaire pour améliorer l'ordre de lecture et la qualité de l'extraction.


## 
Extraire le texte après avoir réduit la taille de la police

Cette technique met à jour les tailles de police des fragments de texte, enregistre le document ajusté en mémoire, puis extrait le texte du résultat transformé.


1. 
Ouvrez le PDF source dans une instance [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Créez un [TextFragmentAbsorber] (https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragmentabsorber/) et visitez toutes les pages du document pour collecter des objets [TextFragment] (https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/).

1. 
Parcourez les fragments et réduisez la taille de chaque police selon le rapport demandé afin que la disposition des colonnes denses puisse être normalisée avant l'extraction.

1. 
Enregistrez le [Document] ajusté (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) dans un flux d'octets en mémoire.
1. Rouvrez un deuxième [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) à partir de cette mémoire tampon.

1. 
Créez un [TextAbsorber] (https://reference.aspose.com/pdf/java/com.aspose.pdf/textabsorber/), visitez toutes les pages du document transformé et écrivez le texte extrait dans le fichier de sortie.


```java
public static void extractTextReduceFont(Path inputFile, Path outputFile, double reduceRatio) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber fragmentAbsorber = new TextFragmentAbsorber();
        document.getPages().accept(fragmentAbsorber);
        for (TextFragment fragment : fragmentAbsorber.getTextFragments()) {
            fragment.getTextState().setFontSize((float) (fragment.getTextState().getFontSize() * reduceRatio));
        }

        ByteArrayOutputStream stream = new ByteArrayOutputStream();
        document.save(stream);
        try (Document document2 = new Document(new ByteArrayInputStream(stream.toByteArray()))) {
            TextAbsorber textAbsorber = new TextAbsorber();
            document2.getPages().accept(textAbsorber);
            Files.writeString(outputFile, textAbsorber.getText());
        }
    }
}
```

## 
Extraire du texte avec un facteur d'échelle



Utilisez `TextExtractionOptions` en mode de formatage pur et ajustez le facteur d'échelle pour les mises en page comportant beaucoup de colonnes.


1. 
Ouvrez le PDF source dans une instance [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Créez un [TextAbsorber] (https://reference.aspose.com/pdf/java/com.aspose.pdf/textabsorber/) pour l'extraction du document complet.

1. 
Créez [TextExtractionOptions] (https://reference.aspose.com/pdf/java/com.aspose.pdf/textextractionoptions/) en mode de formatage pur afin d'utiliser un comportement d'extraction sensible à la mise en page.

1. 
Définissez le facteur d'échelle et appliquez les options d'extraction à l'absorbeur avant de visiter les pages.

1. 
Visitez toutes les pages du document et écrivez le texte extrait dans le fichier de sortie.

```java
public static void extractTextScaleFactor(Path inputFile, Path outputFile, double scaleFactor) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        TextAbsorber textAbsorber = new TextAbsorber();
        TextExtractionOptions extractionOptions =
                new TextExtractionOptions(TextExtractionOptions.TextFormattingMode.Pure);
        extractionOptions.setScaleFactor(scaleFactor);
        textAbsorber.setExtractionOptions(extractionOptions);
        document.getPages().accept(textAbsorber);
        Files.writeString(outputFile, textAbsorber.getText());
    }
}
```
