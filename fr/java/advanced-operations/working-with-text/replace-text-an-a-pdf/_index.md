---
title: Remplacer le texte dans un PDF par Java
linktitle: Remplacer le texte dans un PDF
type: docs
weight: 40
url: /java/replace-text-in-pdf/
description: Découvrez comment remplacer, réorganiser et supprimer du texte dans des documents PDF à l'aide de Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
aliases:
    - /python-net/replace-text-in-a-pdf-document/
TechArticle: true
AlternativeHeadline: Remplacer, supprimer et ajuster le contenu du texte dans un PDF à l'aide de Java
Abstract: Cet article explique les flux de travail de remplacement de texte dans les documents PDF à l'aide d'Aspose.PDF pour Java. Il couvre le remplacement du texte sur toutes les pages, la limitation du remplacement à une région sélectionnée, l'ajustement de la mise en page de remplacement, l'utilisation de la correspondance basée sur les expressions régulières, le remplacement des polices, la suppression de tout le texte et la suppression du texte masqué.
---
Aspose.PDF pour Java fournit à la fois des fonctionnalités de remplacement simples et de remplacement tenant compte de la mise en page via `TextFragmentAbsorber` et des options de remplacement.


## 
Remplacer le texte sur toutes les pages



Utilisez cet exemple lorsque la même phrase doit être remplacée dans tout le document.


1. 
Ouvrez le document PDF source.

1. 
Recherchez dans toutes les pages la phrase cible avec `TextFragmentAbsorber`.
1. Remplacez le texte correspondant et enregistrez le PDF mis à jour.


```java
public static void replaceTextOnAllPages(Path inputFile, Path outputFile) {
        String searchPhrase = "PDF";
        String replacePhrase = "pdf";

        try (Document document = new Document(inputFile.toString())) {
            TextFragmentAbsorber absorber = new TextFragmentAbsorber(searchPhrase);
            document.getPages().accept(absorber);

            for (TextFragment fragment : absorber.getTextFragments()) {
                fragment.setText(replacePhrase);
            }

            document.save(outputFile.toString());
        }
    }
```

## 
Remplacer le texte dans une zone de page spécifique



Utilisez cet exemple lorsque le remplacement doit être limité à un rectangle sélectionné sur une page.


1. 
Ouvrez le document PDF source.

1. 
Configurez `TextSearchOptions` avec des limites de page et un rectangle cible.
1. Remplacez le texte correspondant à l'intérieur de cette région et enregistrez le document.


```java
public static void replaceTextInParticularPageRegion(Path inputFile, Path outputFile) {
    String searchPhrase = "doc";
    String replacePhrase = "DOC";

    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber absorber = new TextFragmentAbsorber(searchPhrase);
        absorber.getTextSearchOptions().setLimitToPageBounds(true);
        absorber.getTextSearchOptions().setRectangle(new Rectangle(300, 442, 500, 742, true));
        document.getPages().get_Item(1).accept(absorber);

        for (TextFragment fragment : absorber.getTextFragments()) {
            fragment.setText(replacePhrase);
        }

        document.save(outputFile.toString());
    }
}
```

## 
Remplacez le texte et ajustez l'espacement à l'intérieur d'un rectangle décalé



Utilisez cet exemple lorsque le texte de remplacement doit rester sur la page avec un espacement ajusté mais que la taille de la police doit rester inchangée.


1. 
Ouvrez le PDF source et collectez des fragments de texte de la page cible.

1. 
Modifiez le rectangle de remplacement et choisissez le comportement `AdjustSpaceWidth`.
1. Définissez le nouveau texte et enregistrez le document.


```java
public static void replaceTextAndResizeAndShiftWithoutChangingFontSize(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber absorber = new TextFragmentAbsorber();
        absorber.visit(document.getPages().get_Item(1));

        TextFragment fragment = absorber.getTextFragments().get_Item(1);
        String text = fragment.getText();
        Rectangle rectangle = fragment.getRectangle();
        rectangle.setLLX(rectangle.getLLX() + 50);
        rectangle.setURX(rectangle.getURX() - 50);
        fragment.getReplaceOptions().setRectangle(rectangle);
        fragment.getReplaceOptions().setReplaceAdjustmentAction(TextReplaceOptions.ReplaceAdjustment.AdjustSpaceWidth);
        fragment.setText(text + " " + text);

        document.save(outputFile.toString());
    }
}
```

## 
Remplacer le texte à l'intérieur d'un rectangle de paragraphe plus grand



Utilisez cet exemple lorsque le texte de remplacement doit s’étendre sur une zone de page plus grande.


1. 
Ouvrez le PDF source et récupérez le premier fragment de texte de la page cible.

1. 
Créez un rectangle de remplacement plus grand à partir de la zone multimédia de la page.
1. Appliquez les options de remplacement et enregistrez le PDF.


```java
public static void replaceTextAndResizeAndShiftParagraph(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber absorber = new TextFragmentAbsorber();
        absorber.visit(document.getPages().get_Item(1));

        TextFragment fragment = absorber.getTextFragments().get_Item(1);
        String text = fragment.getText();
        Rectangle rectangle = document.getPages().get_Item(1).getMediaBox();
        rectangle.setLLX(rectangle.getLLX() + 20);
        rectangle.setURX(rectangle.getURX() - 20);
        rectangle.setURY(rectangle.getURY() - 20);
        fragment.getReplaceOptions().setRectangle(rectangle);
        fragment.getReplaceOptions().setReplaceAdjustmentAction(TextReplaceOptions.ReplaceAdjustment.AdjustSpaceWidth);
        fragment.setText(text + " " + text);

        document.save(outputFile.toString());
    }
}
```

## 
Remplacez le texte et redimensionnez la police pour remplir le rectangle



Utilisez cet exemple lorsque le texte de remplacement doit s'agrandir pour remplir une zone cible.


1. 
Ouvrez le PDF source et accédez au fragment de texte cible.

1. 
Définissez un rectangle de remplacement et activez l'ajustement de la police `ScaleToFill`.
1. Définissez le nouveau texte et enregistrez le document mis à jour.


```java
public static void replaceTextAndResizeAndExpandFont(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber absorber = new TextFragmentAbsorber();
        absorber.visit(document.getPages().get_Item(1));

        TextFragment fragment = absorber.getTextFragments().get_Item(1);
        String text = fragment.getText();
        fragment.getReplaceOptions().setRectangle(new Rectangle(100, 300, 512, 692, true));
        fragment.getReplaceOptions().setReplaceAdjustmentAction(TextReplaceOptions.ReplaceAdjustment.AdjustSpaceWidth);
        fragment.getReplaceOptions().setFontSizeAdjustmentAction(TextReplaceOptions.FontSizeAdjustment.ScaleToFill);
        fragment.setText(text + " " + text);

        document.save(outputFile.toString());
    }
}
```

## 
Remplacez le texte et réduisez-le pour l'adapter



Utilisez cet exemple lorsque le texte de remplacement doit rester à l’intérieur du rectangle de texte d’origine.


1. 
Ouvrez le PDF source et sélectionnez le fragment cible.

1. 
Réutilisez le rectangle de fragment actuel et activez `ShrinkToFit`.
1. Remplacez le texte et enregistrez le document.


```java
public static void replaceTextAndFitTextIntoRectangle(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber absorber = new TextFragmentAbsorber();
        absorber.visit(document.getPages().get_Item(1));

        TextFragment fragment = absorber.getTextFragments().get_Item(1);
        String text = fragment.getText();
        fragment.getReplaceOptions().setRectangle(fragment.getRectangle());
        fragment.getReplaceOptions().setFontSizeAdjustmentAction(TextReplaceOptions.FontSizeAdjustment.ShrinkToFit);
        fragment.getReplaceOptions().setReplaceAdjustmentAction(TextReplaceOptions.ReplaceAdjustment.AdjustSpaceWidth);
        fragment.setText(text + " " + text);

        document.save(outputFile.toString());
    }
}
```

## 
Remplacer le texte par une expression régulière



Utilisez cet exemple lorsque le texte correspondant doit être trouvé par un modèle regex et relooké lors du remplacement.


1. 
Ouvrez le document PDF source.

1. 
Recherchez la page avec un `TextFragmentAbsorber` compatible avec les expressions régulières.
1. Remplacez chaque correspondance, mettez à jour son style de texte et enregistrez le résultat.


```java
public static void replaceTextBasedOnRegex(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber absorber = new TextFragmentAbsorber(Pattern.compile("\\d{4}-\\d{4}"));
        absorber.setTextSearchOptions(new TextSearchOptions(true));
        document.getPages().get_Item(1).accept(absorber);

        for (TextFragment fragment : absorber.getTextFragments()) {
            fragment.setText("ABC1-2XZY");
            fragment.getTextState().setFont(FontRepository.findFont("Verdana"));
            fragment.getTextState().setFontSize(12);
            fragment.getTextState().setForegroundColor(Color.getBlue());
            fragment.getTextState().setBackgroundColor(Color.getLightGreen());
        }

        document.save(outputFile.toString());
    }
}
```

## 
Remplacez le texte de l'espace réservé et laissez la page se réorganiser



Utilisez cet exemple lorsqu'un espace réservé doit être remplacé par une valeur réelle plus longue tout en préservant la mise en page.


1. 
Ouvrez le PDF source et recherchez le texte d'espace réservé.

1. 
Attribuez le texte de remplacement et mettez à jour ses paramètres de police.
1. Enregistrez le document pour que la mise en page soit recalculée.


```java
public static void automaticallyRearrangePageContents(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber absorber = new TextFragmentAbsorber("[Long_placeholder_Long_placeholder]");
        document.getPages().accept(absorber);

        for (TextFragment textFragment : absorber.getTextFragments()) {
            textFragment.setText("John Smith, South Development Studio");
            textFragment.getTextState().setFont(FontRepository.findFont("Calibri"));
            textFragment.getTextState().setFontSize(12);
            textFragment.getTextState().setForegroundColor(Color.getNavy());
        }

        document.save(outputFile.toString());
    }
}
```

## 
Remplacer une police par une autre



Utilisez cet exemple lorsque le texte utilisant une police intégrée spécifique doit être remplacé par une autre police.


1. 
Ouvrez le PDF source et collectez tous les fragments de texte.

1. 
Vérifiez le nom de police de chaque fragment et remplacez la police cible.
1. Enregistrez le PDF mis à jour.


```java
public static void replaceFonts(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber absorber = new TextFragmentAbsorber();
        document.getPages().accept(absorber);

        for (TextFragment fragment : absorber.getTextFragments()) {
            if ("Arial-BoldMT".equals(fragment.getTextState().getFont().getFontName())) {
                fragment.getTextState().setFont(FontRepository.findFont("Verdana"));
            }
        }

        document.save(outputFile.toString());
    }
}
```

## 
Remplacez les polices et supprimez les ressources de polices inutilisées



Utilisez cet exemple lorsque le document doit être nettoyé après le remplacement de la police.


1. 
Ouvrez le PDF source et configurez `TextEditOptions` pour supprimer les polices inutilisées.

1. 
Absorbez les fragments de texte et attribuez la police de remplacement.
1. Enregistrez le document optimisé.


```java
public static void removeUnusedFonts(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextEditOptions options = new TextEditOptions(TextEditOptions.FontReplace.RemoveUnusedFonts);
        TextFragmentAbsorber absorber = new TextFragmentAbsorber(options);
        document.getPages().accept(absorber);

        for (TextFragment textFragment : absorber.getTextFragments()) {
            textFragment.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));
        }

        document.save(outputFile.toString());
    }
}
```

## 
Supprimer tout le texte du document



Utilisez cet exemple lorsque tout le contenu textuel doit être supprimé de chaque page.


1. 
Ouvrez le document PDF source.

1. 
Créez un `TextFragmentAbsorber` et appelez `removeAllText(document)`.
1. Enregistrez le PDF nettoyé.


```java
public static void removeAllTextUsingAbsorber1(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber absorber = new TextFragmentAbsorber();
        absorber.removeAllText(document);
        document.save(outputFile.toString());
    }
}
```

## 
Supprimer tout le texte d'une page



Utilisez cet exemple lorsque tout le texte doit être supprimé uniquement d’une page spécifique.


1. 
Ouvrez le document PDF source.

1. 
Créez un `TextFragmentAbsorber` et supprimez le texte de la page cible.
1. Enregistrez le document mis à jour.


```java
public static void removeAllTextUsingAbsorber2(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber absorber = new TextFragmentAbsorber();
        absorber.removeAllText(document.getPages().get_Item(1));
        document.save(outputFile.toString());
    }
}
```

## 
Supprimer le texte d'un rectangle sélectionné



Utilisez cet exemple lorsque le texte doit être supprimé uniquement à l’intérieur d’une zone de page choisie.


1. 
Ouvrez le document PDF source.

1. 
Créez un `TextFragmentAbsorber` et définissez le rectangle à nettoyer.
1. Supprimez le texte de cette région et enregistrez le document.


```java
public static void removeAllTextUsingAbsorber3(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber absorber = new TextFragmentAbsorber();
        absorber.removeAllText(document.getPages().get_Item(1), new Rectangle(10, 200, 120, 600, true));
        document.save(outputFile.toString());
    }
}
```

## 
Supprimer le texte masqué



Utilisez cet exemple lorsque des fragments de texte invisibles doivent être supprimés du PDF.


1. 
Ouvrez le PDF source et absorbez tous les fragments de texte.

1. 
Vérifiez chaque fragment pour l'état du texte invisible.
1. Effacez le texte masqué et enregistrez le document.

```java
public static void removeHiddenText(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber textAbsorber = new TextFragmentAbsorber();
        textAbsorber.setTextReplaceOptions(new TextReplaceOptions(TextReplaceOptions.ReplaceAdjustment.None));
        document.getPages().accept(textAbsorber);

        for (TextFragment fragment : textAbsorber.getTextFragments()) {
            if (fragment.getTextState().isInvisible()) {
                fragment.setText("");
            }
        }

        document.save(outputFile.toString());
    }
}
```
