---
title: Rechercher et extraire du texte PDF en Java
linktitle: Rechercher et obtenir du texte
type: docs
weight: 60
url: /java/search-and-get-text-from-pdf/
description: Découvrez comment rechercher, inspecter et extraire du texte à partir de documents PDF en Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Rechercher du texte PDF et inspecter les fragments extraits en Java
Abstract: Cet article explique comment rechercher et extraire du texte à partir de documents PDF à l'aide d'Aspose.PDF pour Java. Il couvre TextAbsorber et TextFragmentAbsorber, y compris l'extraction basée sur la région, les recherches spécifiques à une page, la correspondance d'expressions régulières et de phrases, l'insertion de liens hypertexte, l'inspection de texte stylisé et la mise en évidence de fragments.
---
Aspose.PDF pour Java prend en charge l'extraction de texte brut et la recherche au niveau des fragments avec des coordonnées, des styles et une correspondance d'expressions régulières.


## 
Extraire le texte de toutes les pages avec TextAbsorber



Utilisez cet exemple lorsque vous avez besoin de texte brut extrait d’une zone de document sélectionnée sur toutes les pages.


1. 
Ouvrez le document PDF source.

1. 
Créez `TextExtractionOptions` et `TextSearchOptions` par région.
1. Exécutez `TextAbsorber` sur toutes les pages et affichez le texte extrait.


```java
public static void textAbsorberSearch(Path inputFile) {
        try (Document document = new Document(inputFile.toString())) {
            TextExtractionOptions textExtractionOptions = new TextExtractionOptions(TextExtractionOptions.TextFormattingMode.Pure);
            TextSearchOptions textSearchOptions = new TextSearchOptions(new Rectangle(0, 0, 842, 250, true));
            TextAbsorber absorber = new TextAbsorber(textExtractionOptions, textSearchOptions);

            document.getPages().accept(absorber);
            System.out.println("Text fragments found: " + absorber.getText());
        }
    }
```

## 
Extraire le texte d'une page avec TextAbsorber



Utilisez cet exemple lorsque l’extraction de texte brut doit être limitée à une page.


1. 
Ouvrez le document PDF source.

1. 
Configurez les options d'extraction de texte et de recherche avec la région cible.
1. Exécutez `TextAbsorber` sur la page sélectionnée et affichez le résultat.


```java
public static void textAbsorberSearchPage(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextExtractionOptions textExtractionOptions = new TextExtractionOptions(TextExtractionOptions.TextFormattingMode.Pure);
        TextSearchOptions textSearchOptions = new TextSearchOptions(new Rectangle(0, 0, 842, 250, true));
        TextAbsorber absorber = new TextAbsorber(textExtractionOptions, textSearchOptions);

        document.getPages().get_Item(2).accept(absorber);
        System.out.println("Text fragments found: " + absorber.getText());
    }
}
```

## 
Inspecter tous les fragments de texte du document



Utilisez cet exemple lorsque vous avez besoin d'un contenu textuel ainsi que de métadonnées de police, de position et de couleur.


1. 
Ouvrez le document PDF source.

1. 
Exécutez `TextFragmentAbsorber` sur toutes les pages.
1. Parcourez les fragments et affichez leurs métadonnées.


```java
public static void textFragmentAbsorberSearch(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber absorber = new TextFragmentAbsorber();
        document.getPages().accept(absorber);

        for (TextFragment fragment : absorber.getTextFragments()) {
            System.out.println("Text: " + fragment.getText());
            System.out.println("Position: " + fragment.getPosition());
            System.out.println("XIndent: " + fragment.getPosition().getXIndent());
            System.out.println("YIndent: " + fragment.getPosition().getYIndent());
            System.out.println("Font - Name: " + fragment.getTextState().getFont().getFontName());
            System.out.println("Font - IsAccessible: " + fragment.getTextState().getFont().isAccessible());
            System.out.println("Font - IsEmbedded: " + fragment.getTextState().getFont().isEmbedded());
            System.out.println("Font - IsSubset: " + fragment.getTextState().getFont().isSubset());
            System.out.println("Font Size: " + fragment.getTextState().getFontSize());
            System.out.println("Foreground Color: " + fragment.getTextState().getForegroundColor());
        }
    }
}
```

## 
Rechercher une phrase sur une page spécifique



Utilisez cet exemple lorsqu'un mot cible doit être trouvé sur une page sélectionnée uniquement.


1. 
Ouvrez le document PDF source.

1. 
Créez `TextFragmentAbsorber` avec la phrase cible.
1. Visitez la page choisie et affichez les positions des fragments correspondants.


```java
public static void textFragmentAbsorberSearchPage(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber absorber = new TextFragmentAbsorber("whale");
        document.getPages().get_Item(2).accept(absorber);

        for (TextFragment fragment : absorber.getTextFragments()) {
            System.out.println("Text: " + fragment.getText());
            System.out.println("Position: " + fragment.getPosition());
        }
    }
}
```

## 
Continuer une recherche séquentielle sur les pages



Utilisez cet exemple lorsque vous souhaitez réutiliser un absorbeur tout en passant d'une recherche de page à la suivante.


1. 
Ouvrez le document PDF source et créez un absorbeur réutilisable.

1. 
Recherchez la première page et inspectez les résultats.
1. Continuez à rechercher des pages supplémentaires et examinez les correspondances mises à jour.


```java
public static void textFragmentAbsorberSequentialSearch(Path inputFile) {
    Document document = new Document(inputFile.toString());
    TextFragmentAbsorber absorber = new TextFragmentAbsorber();
    absorber.setPhrase("whale");

    document.getPages().get_Item(1).accept(absorber);
    for (TextFragment fragment : absorber.getTextFragments()) {
        System.out.println("Text: " + fragment.getText());
        System.out.println("Page: " + fragment.getPage().getNumber());
        System.out.println("Position: " + fragment.getPosition());
    }

    System.out.println("--");

    document.getPages().get_Item(2).accept(absorber);
    absorber.visit(document);

    for (TextFragment fragment : absorber.getTextFragments()) {
        System.out.println("Text: " + fragment.getText());
        System.out.println("Page: " + fragment.getPage().getNumber());
        System.out.println("Position: " + fragment.getPosition());
    }
}
```

## 
Rechercher une phrase à l'intérieur d'un rectangle sélectionné



Utilisez cet exemple lorsque la correspondance d’expressions doit être limitée à une région d’une page.


1. 
Ouvrez le document PDF source.

1. 
Créez `TextFragmentAbsorber` avec la phrase cible et `TextSearchOptions` basé sur un rectangle.
1. Visitez la page et affichez les positions des fragments correspondants.


```java
public static void textFragmentAbsorberSearchPhrase(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber absorber = new TextFragmentAbsorber(
                "elephant", new TextSearchOptions(new Rectangle(0, 0, 842, 250, true)));

        document.getPages().get_Item(2).accept(absorber);

        for (TextFragment fragment : absorber.getTextFragments()) {
            System.out.println("Text: " + fragment.getText());
            System.out.println("Position: " + fragment.getPosition());
        }
    }
}
```

## 
Rechercher du texte par expression régulière



Utilisez cet exemple lorsque les correspondances doivent être trouvées par un modèle regex au lieu d'une phrase fixe.


1. 
Ouvrez le document PDF source.

1. 
Créez un `TextFragmentAbsorber` compatible avec les expressions régulières.
1. Visitez la page cible et affichez les fragments correspondants.


```java
public static void textFragmentAbsorberSearchRegex(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber absorber = new TextFragmentAbsorber(
                Pattern.compile("\\d+\\.\\d+"), new TextSearchOptions(true));

        document.getPages().get_Item(2).accept(absorber);

        for (TextFragment fragment : absorber.getTextFragments()) {
            System.out.println("Text: " + fragment.getText());
            System.out.println("Position: " + fragment.getPosition());
        }
    }
}
```

## 
Rechercher une liste d'expressions par modèles d'expression régulière



Utilisez cet exemple lorsque plusieurs phrases cibles doivent être trouvées en un seul passage.


1. 
Ouvrez le document PDF source.

1. 
Créez un tableau de modèles d'expressions régulières et transmettez-le à `TextFragmentAbsorber`.
1. Visitez le document et inspectez les résultats d’expression régulière groupés.


```java
public static void textFragmentAbsorberSearchListOfPhrases(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Pattern[] patterns = new Pattern[] {
                Pattern.compile("whale"),
                Pattern.compile("elephant")
        };
        TextFragmentAbsorber absorber = new TextFragmentAbsorber(patterns, new TextSearchOptions(true));
        document.getPages().accept(absorber);

        for (TextFragmentCollection fragments : absorber.getRegexResults().values()) {
            for (TextFragment fragment : fragments) {
                System.out.println("Text: " + fragment.getText());
                System.out.println("Position: " + fragment.getPosition());
            }
        }
    }
}
```

## 
Recherchez du texte et transformez-le en hyperliens



Utilisez cet exemple lorsque les mots correspondants doivent être mis en surbrillance et convertis en liens cliquables.


1. 
Ouvrez le document PDF source.

1. 
Recherchez les mots cibles avec la recherche regex activée.
1. Mettez à jour le style du texte, attachez des liens hypertexte et enregistrez le PDF modifié.


```java
public static void textFragmentAbsorberSearchAndAddHyperlink(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber absorber = new TextFragmentAbsorber("whale|elephant");
        absorber.setTextSearchOptions(new TextSearchOptions(true));
        absorber.visit(document.getPages().get_Item(1));

        for (TextFragment fragment : absorber.getTextFragments()) {
            fragment.getTextState().setForegroundColor(Color.getBlue());
            fragment.getTextState().setUnderline(true);
            fragment.setHyperlink(new WebHyperlink("https://en.wikipedia.org/wiki/" + fragment.getText()));
        }

        document.save(inputFile.toString().replace("in.pdf", "out.pdf"));
    }
}
```

## 
Rechercher du texte par caractéristiques de style



Utilisez cet exemple lorsque vous devez inspecter des fragments en fonction d'un formatage tel qu'un texte en gras ou invisible.


1. 
Ouvrez le document PDF source.

1. 
Exécutez `TextFragmentAbsorber` sur la page cible.
1. Vérifiez chaque style de fragment et affichez les entrées correspondantes.


```java
public static void textFragmentAbsorberSearchStyledText(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber absorber = new TextFragmentAbsorber();
        absorber.setTextSearchOptions(new TextSearchOptions(true));
        absorber.visit(document.getPages().get_Item(1));

        for (TextFragment fragment : absorber.getTextFragments()) {
            if (fragment.getTextState().getFontStyle() == FontStyles.Bold) {
                System.out.println("Bold: " + fragment.getText());
            }
            if (fragment.getTextState().isInvisible()) {
                System.out.println("Invisible: " + fragment.getText());
            }
        }
    }
}
```

## 
Mettre en surbrillance les résultats de recherche dans les aperçus de page rendus



Utilisez cet exemple lorsque les correspondances de texte doivent être corrélées aux images de page rendues pour une inspection visuelle.


1. 
Créez un périphérique PNG avec la résolution requise.

1. 
Recherchez chaque page avec `TextFragmentAbsorber` et affichez la page dans un flux d'images.
1. Écrivez les images d’aperçu de la page et les coordonnées des fragments de sortie pour inspection.

```java
public static void textFragmentAbsorberSearchAndHighlight(Path inputFile) throws Exception {
    int resolution = 150;
    PngDevice pngDevice = new PngDevice(new Resolution(resolution, resolution));

    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber absorber = new TextFragmentAbsorber(Pattern.compile("[\\S]+"));
        absorber.setTextSearchOptions(new TextSearchOptions(true));

        for (int pageNumber = 1; pageNumber <= document.getPages().size(); pageNumber++) {
            Page page = document.getPages().get_Item(pageNumber);
            page.accept(absorber);

            try (ByteArrayOutputStream stream = new ByteArrayOutputStream()) {
                pngDevice.process(page, stream);
                Path output = Path.of(inputFile.toString().replace("_in.pdf", page.getNumber() + "_out.png"));
                Files.write(output, stream.toByteArray());
            }

            for (TextFragment textFragment : absorber.getTextFragments()) {
                Rectangle pageRect = page.getPageRect(true);
                System.out.println("TextFragment = " + textFragment.getText()
                        + " Page URY = " + pageRect.getURY()
                        + " TextFragment URY = " + textFragment.getRectangle().getURY());
            }
        }
    }
}
```
