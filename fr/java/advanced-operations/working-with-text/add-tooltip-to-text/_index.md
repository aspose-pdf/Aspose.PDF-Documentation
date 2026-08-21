---
title: Ajouter des info-bulles au texte PDF en Java
linktitle: Info-bulle PDF
type: docs
weight: 20
url: /java/pdf-tooltip/
description: Découvrez comment ajouter des info-bulles aux fragments de texte dans des documents PDF en Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Ajouter des info-bulles interactives aux fragments de texte PDF à l'aide de Java
Abstract: Cet article montre comment ajouter une aide interactive au texte PDF à l'aide d'Aspose.PDF pour Java. Il couvre l'attachement d'un texte d'info-bulle à des champs de boutons invisibles placés sur des fragments de texte correspondants et la création d'un champ de texte masqué qui apparaît lorsque le pointeur entre dans une zone de déclenchement.
---
Aspose.PDF pour Java vous permet d'ajouter une aide interactive en plaçant des champs de formulaire sur des fragments de texte.


## 
Ajouter des info-bulles au texte correspondant



Utilisez cet exemple lorsque le texte existant dans le PDF doit afficher une info-bulle au survol.


1. 
Créez l'exemple de PDF et rouvrez-le pour le modifier.

1. 
Recherchez les fragments de texte cibles avec `TextFragmentAbsorber`.
1. Placez les superpositions `ButtonField` sur le texte correspondant et attribuez le texte de l'info-bulle.

1. 
Enregistrez le document mis à jour.


```java
public static void addToolTipToSearchedText(Path outputFile) {
        Document document = new Document();
        document.getPages().add().getParagraphs()
                .add(new TextFragment("Move the mouse cursor here to display a tooltip"));
        document.getPages().get_Item(1).getParagraphs()
                .add(new TextFragment("Move the mouse cursor here to display a very long tooltip"));
        document.save(outputFile.toString());
        document.close();

        document = new Document(outputFile.toString());
        TextFragmentAbsorber absorber = new TextFragmentAbsorber(
                "Move the mouse cursor here to display a tooltip");
        document.getPages().accept(absorber);

        for (TextFragment fragment : absorber.getTextFragments()) {
            ButtonField field = new ButtonField(fragment.getPage(), fragment.getRectangle());
            field.setAlternateName("Tooltip for text.");
            document.getForm().add(field);
        }

        absorber = new TextFragmentAbsorber("Move the mouse cursor here to display a very long tooltip");
        document.getPages().accept(absorber);

        for (TextFragment fragment : absorber.getTextFragments()) {
            ButtonField field = new ButtonField(fragment.getPage(), fragment.getRectangle());
            field.setAlternateName("Lorem ipsum dolor sit amet, consectetur adipiscing elit,"
                    + " sed do eiusmod tempor incididunt ut labore et dolore magna"
                    + " aliqua. Ut enim ad minim veniam, quis nostrud exercitation"
                    + " ullamco laboris nisi ut aliquip ex ea commodo consequat."
                    + " Duis aute irure dolor in reprehenderit in voluptate velit"
                    + " esse cillum dolore eu fugiat nulla pariatur. Excepteur sint"
                    + " occaecat cupidatat non proident, sunt in culpa qui officia"
                    + " deserunt mollit anim id est laborum.");
            document.getForm().add(field);
        }

        document.save(outputFile.toString());
        document.close();
    }
```

## 
Afficher un bloc de texte flottant au survol



Utilisez cet exemple lorsque le survol d'une zone de texte doit révéler un champ de texte masqué.


1. 
Créez l'exemple de PDF et rouvrez-le pour le modifier.
1. Recherchez le fragment de texte déclencheur avec `TextFragmentAbsorber`.

1. 
Créez un `TextBoxField` masqué et un `ButtonField` avec des actions d'entrée et de sortie.

1. 
Enregistrez le PDF final.

```java
public static void createHiddenTextBlock(Path outputFile) {
    Document document = new Document();
    document.getPages().add().getParagraphs()
            .add(new TextFragment("Move the mouse cursor here to display floating text"));
    document.save(outputFile.toString());
    document.close();

    document = new Document(outputFile.toString());
    TextFragmentAbsorber absorber = new TextFragmentAbsorber(
            "Move the mouse cursor here to display floating text");
    document.getPages().accept(absorber);
    TextFragment fragment = absorber.getTextFragments().get_Item(1);

    TextBoxField floatingField = new TextBoxField(
            fragment.getPage(), new Rectangle(100.0, 700.0, 220.0, 740.0, false));
    floatingField.setValue("This is the \"floating text field\".");
    floatingField.setReadOnly(true);
    floatingField.setFlags(floatingField.getFlags() | AnnotationFlags.Hidden);
    floatingField.setPartialName("FloatingField_1");
    floatingField.setDefaultAppearance(new DefaultAppearance("Helv", 10, java.awt.Color.BLUE));
    floatingField.getCharacteristics().setBackground(java.awt.Color.CYAN);
    floatingField.getCharacteristics().setBorder(java.awt.Color.BLUE);
    floatingField.setBorder(new Border(floatingField));
    floatingField.getBorder().setWidth(1);
    floatingField.setMultiline(true);

    document.getForm().add(floatingField);

    ButtonField buttonField = new ButtonField(fragment.getPage(), fragment.getRectangle());
    buttonField.getAnnotationActions().setOnEnter(new HideAction(floatingField, false));
    buttonField.getAnnotationActions().setOnExit(new HideAction(floatingField));

    document.getForm().add(buttonField);
    document.save(outputFile.toString());
    document.close();
}
```
