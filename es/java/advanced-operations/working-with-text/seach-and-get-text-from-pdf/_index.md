---
title: Buscar y extraer texto PDF en Java
linktitle: Buscar y obtener texto
type: docs
weight: 60
url: /java/search-and-get-text-from-pdf/
description: Aprenda a buscar, inspeccionar y extraer texto de documentos PDF en Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Busque texto PDF e inspeccione fragmentos extraídos en Java
Abstract: Este artículo explica cómo buscar y extraer texto de documentos PDF usando Aspose.PDF para Java. Cubre TextAbsorber y TextFragmentAbsorber, incluida la extracción basada en regiones, búsquedas específicas de páginas, concordancia de frases y expresiones regulares, inserción de hipervínculos, inspección de texto con estilo y resaltado de fragmentos.
---
Aspose.PDF para Java admite la extracción de texto sin formato y la búsqueda a nivel de fragmentos con coordenadas, estilos y coincidencia de expresiones regulares.


## 
Extraiga texto de todas las páginas con TextAbsorber



Utilice este ejemplo cuando necesite texto extraído sin formato de una región de documento seleccionada en todas las páginas.


1. Abra el documento PDF de origen.

1. Cree `TextExtractionOptions` y `TextSearchOptions` basado en regiones.
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

## 
Extraiga texto de una página con TextAbsorber



Utilice este ejemplo cuando la extracción de texto sin formato deba limitarse a una página.


1. Abra el documento PDF de origen.

1. Configure las opciones de extracción y búsqueda de texto con la región de destino.
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

## 
Inspeccionar todos los fragmentos de texto del documento.



Utilice este ejemplo cuando necesite contenido de texto junto con metadatos de fuente, posición y color.


1. Abra el documento PDF de origen.

1. Ejecute `TextFragmentAbsorber` en todas las páginas.
1. Itere a través de los fragmentos y genere sus metadatos.


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
Buscar una frase en una página específica



Utilice este ejemplo cuando una palabra de destino deba encontrarse únicamente en una página seleccionada.


1. Abra el documento PDF de origen.

1. Cree `TextFragmentAbsorber` con la frase objetivo.
1. Visite la página elegida y genere las posiciones de los fragmentos coincidentes.


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
Continuar una búsqueda secuencial en todas las páginas



Utilice este ejemplo cuando desee reutilizar un absorbente mientras pasa de una página de búsqueda a la siguiente.


1. Abra el documento PDF fuente y cree un absorbente reutilizable.

1. Busque en la primera página e inspeccione los resultados.
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

## 
Buscar una frase dentro de un rectángulo seleccionado



Utilice este ejemplo cuando la concordancia de frases deba limitarse a una región de una página.


1. Abra el documento PDF de origen.

1. Cree `TextFragmentAbsorber` con la frase de destino y `TextSearchOptions` basado en rectángulo.
1. Visite la página y genere las posiciones de los fragmentos coincidentes.


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
Buscar texto por expresión regular



Utilice este ejemplo cuando las coincidencias se deban encontrar mediante un patrón de expresiones regulares en lugar de una frase fija.


1. Abra el documento PDF de origen.

1. Cree un `TextFragmentAbsorber` habilitado para expresiones regulares.
1. Visite la página de destino y genere los fragmentos coincidentes.


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
Buscar una lista de frases por patrones de expresiones regulares



Utilice este ejemplo cuando deban encontrarse varias frases objetivo en una sola pasada.


1. Abra el documento PDF de origen.

1. Cree una serie de patrones de expresiones regulares y páselo a `TextFragmentAbsorber`.
1. Visite el documento e inspeccione los resultados de expresiones regulares agrupados.


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
Encuentra texto y conviértelo en hipervínculos.



Utilice este ejemplo cuando las palabras coincidentes deban resaltarse y convertirse en enlaces en los que se pueda hacer clic.


1. Abra el documento PDF de origen.

1. Busque las palabras de destino con la búsqueda de expresiones regulares habilitada.
1. Actualice el estilo del texto, adjunte hipervínculos y guarde el PDF modificado.


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
Buscar texto por características de estilo



Utilice este ejemplo cuando necesite inspeccionar fragmentos según el formato, como texto en negrita o invisible.


1. Abra el documento PDF de origen.

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

## 
Resalte los resultados de búsqueda en vistas previas de páginas renderizadas



Utilice este ejemplo cuando las coincidencias de texto deban correlacionarse con las imágenes de la página renderizadas para una inspección visual.


1. Cree un dispositivo PNG con la resolución requerida.

1. Busque cada página con `TextFragmentAbsorber` y renderice la página en una secuencia de imágenes.
1. Escriba las imágenes de vista previa de la página y las coordenadas de los fragmentos de salida para su inspección.

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
