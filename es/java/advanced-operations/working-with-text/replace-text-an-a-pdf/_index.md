---
title: Reemplazar texto en PDF con Java
linktitle: Reemplazar texto en PDF
type: docs
weight: 40
url: /java/replace-text-in-pdf/
description: Aprenda a reemplazar, reorganizar y eliminar texto en documentos PDF usando Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
aliases:
    - /python-net/replace-text-in-a-pdf-document/
TechArticle: true
AlternativeHeadline: Reemplace, elimine y ajuste el contenido de texto en PDF usando Java
Abstract: Este artículo explica los flujos de trabajo de reemplazo de texto en documentos PDF utilizando Aspose.PDF para Java. Cubre el reemplazo de texto en todas las páginas, la limitación del reemplazo a una región seleccionada, el ajuste del diseño del reemplazo, el uso de coincidencias basadas en expresiones regulares, el reemplazo de fuentes, la eliminación de todo el texto y la eliminación del texto oculto.
---
Aspose.PDF para Java proporciona funciones de reemplazo simples y de reemplazo según el diseño a través de `TextFragmentAbsorber` y opciones de reemplazo.


## 
Reemplazar texto en todas las páginas



Utilice este ejemplo cuando deba reemplazar la misma frase en todo el documento.


1. 
Abra el documento PDF de origen.

1. 
Busque en todas las páginas la frase objetivo con `TextFragmentAbsorber`.
1. Reemplace el texto coincidente y guarde el PDF actualizado.


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
Reemplazar texto en una región de página específica



Utilice este ejemplo cuando el reemplazo deba limitarse a un rectángulo seleccionado en una página.


1. 
Abra el documento PDF de origen.

1. 
Configure `TextSearchOptions` con límites de página y un rectángulo de destino.
1. Reemplace el texto coincidente dentro de esa región y guarde el documento.


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
Reemplazar texto y ajustar el espacio dentro de un rectángulo desplazado



Utilice este ejemplo cuando el texto de reemplazo deba permanecer en la página con el espaciado ajustado pero el tamaño de fuente no deba cambiarse.


1. 
Abra el PDF de origen y recopile fragmentos de texto de la página de destino.

1. 
Modifique el rectángulo de reemplazo y elija el comportamiento `AdjustSpaceWidth`.
1. Establezca el nuevo texto y guarde el documento.


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
Reemplazar texto dentro de un rectángulo de párrafo más grande



Utilice este ejemplo cuando el texto de reemplazo deba expandirse a un área de página más grande.


1. 
Abra el PDF de origen y obtenga el primer fragmento de texto de la página de destino.

1. 
Cree un rectángulo de reemplazo más grande a partir del cuadro de medios de la página.
1. Aplique las opciones de reemplazo y guarde el PDF.


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
Reemplace el texto y escale la fuente para llenar el rectángulo



Utilice este ejemplo cuando el texto de reemplazo deba ampliarse para llenar un área de destino.


1. 
Abra el PDF de origen y acceda al fragmento de texto de destino.

1. 
Defina un rectángulo de reemplazo y habilite el ajuste de fuente `ScaleToFill`.
1. Configure el nuevo texto y guarde el documento actualizado.


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
Reemplazar texto y reducirlo para que quepa



Utilice este ejemplo cuando el texto de reemplazo deba permanecer dentro del rectángulo de texto original.


1. 
Abra el PDF de origen y seleccione el fragmento de destino.

1. 
Reutilice el rectángulo del fragmento actual y habilite `ShrinkToFit`.
1. Reemplace el texto y guarde el documento.


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
Reemplazar texto por expresión regular



Utilice este ejemplo cuando el texto coincidente se deba encontrar mediante un patrón de expresiones regulares y cambiarle el estilo durante el reemplazo.


1. 
Abra el documento PDF de origen.

1. 
Busque en la página con un `TextFragmentAbsorber` habilitado para expresiones regulares.
1. Reemplace cada coincidencia, actualice su estilo de texto y guarde el resultado.


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
Reemplace el texto del marcador de posición y deje que la página se reorganice



Utilice este ejemplo cuando un marcador de posición deba reemplazarse por un valor real más largo preservando al mismo tiempo el diseño de la página.


1. 
Abra el PDF de origen y busque el texto del marcador de posición.

1. 
Asigne el texto de reemplazo y actualice su configuración de fuente.
1. Guarde el documento para volver a calcular el diseño.


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
Reemplazar una fuente por otra



Utilice este ejemplo cuando el texto que utiliza una fuente incrustada específica deba cambiarse a otra fuente.


1. 
Abra el PDF de origen y recopile todos los fragmentos de texto.

1. 
Verifique el nombre de la fuente de cada fragmento y reemplace la fuente de destino.
1. Guarde el PDF actualizado.


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
Reemplazar fuentes y eliminar recursos de fuentes no utilizados



Utilice este ejemplo cuando deba limpiar el documento después de reemplazar la fuente.


1. 
Abra el PDF de origen y configure `TextEditOptions` para eliminar las fuentes no utilizadas.

1. 
Absorba los fragmentos de texto y asigne la fuente de reemplazo.
1. Guarde el documento optimizado.


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
Eliminar todo el texto del documento.



Utilice este ejemplo cuando deba eliminar todo el contenido de texto de cada página.


1. 
Abra el documento PDF de origen.

1. 
Cree un `TextFragmentAbsorber` y llame a `removeAllText(document)`.
1. Guarde el PDF limpio.


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
Eliminar todo el texto de una página



Utilice este ejemplo cuando todo el texto deba eliminarse solo de una página específica.


1. 
Abra el documento PDF de origen.

1. 
Cree un `TextFragmentAbsorber` y elimine el texto de la página de destino.
1. Guarde el documento actualizado.


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
Eliminar texto de un rectángulo seleccionado



Utilice este ejemplo cuando el texto deba eliminarse solo dentro de un área de página elegida.


1. 
Abra el documento PDF de origen.

1. 
Cree un `TextFragmentAbsorber` y defina el rectángulo a limpiar.
1. Elimine el texto de esa región y guarde el documento.


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
Eliminar texto oculto



Utilice este ejemplo cuando deba eliminar fragmentos de texto invisibles del PDF.


1. 
Abra el PDF de origen y absorba todos los fragmentos de texto.

1. 
Verifique cada fragmento para ver el estado del texto invisible.
1. Borre el texto oculto y guarde el documento.

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
