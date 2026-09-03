---
title: Agregar tooltips al texto PDF en Java
linktitle: Tooltip de PDF
type: docs
weight: 20
url: /es/java/pdf-tooltip/
description: Aprenda cómo agregar tooltips a fragmentos de texto en documentos PDF en Java.
lastmod: "2026-09-03"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Agregar tooltips interactivos a fragmentos de texto PDF usando Java
Abstract: Este artículo muestra cómo agregar ayuda interactiva al texto PDF usando Aspose.PDF for Java. Describe cómo adjuntar texto de tooltip a campos de botón invisibles colocados sobre fragmentos de texto coincidentes y crear un campo de texto oculto que aparece cuando el puntero entra en un área de activación.
---
Aspose.PDF for Java le permite agregar ayuda interactiva colocando campos de formulario sobre fragmentos de texto.

## Agregar tooltips al texto coincidente

Utilice este ejemplo cuando el texto existente en el PDF deba mostrar un tooltip al pasar el cursor.

1. Cree el PDF de muestra y vuelva a abrirlo para editar.
1. Buscar los fragmentos de texto objetivo con `TextFragmentAbsorber`.
1. Lugar `ButtonField` superpone sobre el texto coincidente y asigna texto de información emergente.
1. Guarde el documento actualizado.

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

## Mostrar un bloque de texto flotante al pasar el cursor

Utilice este ejemplo cuando al pasar el cursor sobre un área de texto se revele un campo de texto oculto.

1. Cree el PDF de muestra y vuelva a abrirlo para editar.
1. Buscar el fragmento de texto desencadenante con `TextFragmentAbsorber`.
1. Crear un oculto `TextBoxField` y un `ButtonField` con acciones de entrada y salida.
1. Guarde el PDF final.

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
