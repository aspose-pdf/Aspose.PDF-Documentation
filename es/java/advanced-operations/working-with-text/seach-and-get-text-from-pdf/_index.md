---
title: Buscar y extraer texto PDF en Java
linktitle: Buscar y obtener texto
type: docs
weight: 60
url: /es/java/search-and-get-text-from-pdf/
description: Aprenda cómo buscar, inspeccionar y extraer texto de documentos PDF en Java.
lastmod: "2026-09-29"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Buscar texto en PDF e inspeccionar fragmentos extraídos en Java
Abstract: Este artículo explica cómo buscar y extraer texto de documentos PDF usando Aspose.PDF for Java. Cubre TextAbsorber y TextFragmentAbsorber, incluyendo extracción basada en regiones, búsquedas específicas de página, coincidencia con expresiones regulares y frases, inserción de hipervínculos, inspección de texto con estilo y resaltado de fragmentos.
---
Aspose.PDF for Java admite la extracción de texto sin formato y la búsqueda a nivel de fragmento con coordenadas, estilos y coincidencia de expresiones regulares.

## Extraer texto de todas las páginas con TextAbsorber

Utilice este ejemplo cuando necesite texto extraído sin formato de una región seleccionada del documento en todas las páginas.

1. Abra el documento PDF fuente.
1. Cree `TextExtractionOptions` y basado en regiones `TextSearchOptions`.
1. Ejecute `TextAbsorber` en todas las páginas y genere el texto extraído.

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

## Extraer texto de una página con TextAbsorber

Utilice este ejemplo cuando la extracción de texto sin formato deba limitarse a una página.

1. Abra el documento PDF fuente.
1. Configure la extracción de texto y las opciones de búsqueda con la región objetivo.
1. Ejecute `TextAbsorber` en la página seleccionada y genere el resultado.

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

## Inspeccionar todos los fragmentos de texto en el documento

Utilice este ejemplo cuando necesite contenido de texto junto con metadatos de fuente, posición y color.

1. Abra el documento PDF fuente.
1. Ejecute `TextFragmentAbsorber` en todas las páginas.
1. Itere a través de los fragmentos y muestre sus metadatos.

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

## Buscar una frase en una página específica

Utilice este ejemplo cuando una palabra objetivo debe encontrarse solo en una página seleccionada.

1. Abra el documento PDF fuente.
1. Cree `TextFragmentAbsorber` con la frase objetivo.
1. Visite la página elegida y muestre las posiciones del fragmento coincidente.

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

## Continuar una búsqueda secuencial a través de las páginas

Utilice este ejemplo cuando desee reutilizar un absorber mientras pasa de una búsqueda de página a la siguiente.

1. Abra el documento PDF de origen y cree un absorber reutilizable.
1. Busque la primera página e inspecciona los resultados.
1. Continúe buscando páginas adicionales y revise las coincidencias actualizadas.

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

## Buscar una frase dentro de un rectángulo seleccionado

Utilice este ejemplo cuando la coincidencia de frases debe limitarse a una región en una página.

1. Abra el documento PDF fuente.
1. Cree `TextFragmentAbsorber` con la frase objetivo y basado en rectángulos `TextSearchOptions`.
1. Visite la página y muestre las posiciones del fragmento coincidente.

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

## Buscar texto por expresión regular

Utilice este ejemplo cuando las coincidencias deban encontrarse mediante un patrón regex en lugar de una frase fija.

1. Abra el documento PDF fuente.
1. Cree un regex habilitado `TextFragmentAbsorber`.
1. Visite la página de destino y devuelva los fragmentos coincidentes.

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

## Buscar una lista de frases por patrones regex

Utilice este ejemplo cuando se deban encontrar varias frases objetivo en una sola pasada.

1. Abra el documento PDF fuente.
1. Cree una matriz de patrones regex y pásela a `TextFragmentAbsorber`.
1. Visite el documento y examine los resultados agrupados de expresiones regulares.

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

## Buscar texto y convertirlo en hipervínculos

Utilice este ejemplo cuando las palabras coincidentes deban resaltarse y convertirse en enlaces clicables.

1. Abra el documento PDF fuente.
1. Busque las palabras objetivo con la búsqueda regex habilitada.
1. Actualice el estilo del texto, agregue hipervínculos y guarde el PDF modificado.

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

## Buscar texto por características de estilo

Utilice este ejemplo cuando necesite inspeccionar fragmentos basados en el formato, como negrita o texto invisible.

1. Abra el documento PDF fuente.
1. Ejecute `TextFragmentAbsorber` en la página de destino.
1. Verifique cada estilo de fragmento y genere las entradas coincidentes.

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

## Resaltar resultados de búsqueda en vistas previas de página renderizadas

Utilice este ejemplo cuando las coincidencias de texto deben correlacionarse con las imágenes de página renderizadas para una inspección visual.

1. Cree un dispositivo PNG con la resolución requerida.
1. Busque en cada página con `TextFragmentAbsorber` y renderice la página a un flujo de imagen.
1. Escriba las imágenes de vista previa de la página y las coordenadas de fragmentos de salida para inspección.

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
